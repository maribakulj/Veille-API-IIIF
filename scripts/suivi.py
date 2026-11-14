#!/usr/bin/env python3
"""Suivi par institution : consigne intégrale, étapes à cocher, contrôles automatiques.

Usage :
  python3 scripts/suivi.py init       crée institutions/<slug>/CONSIGNE-ET-SUIVI.md s'il n'existe pas
  python3 scripts/suivi.py sync       recopie la consigne intégrale (CONSIGNE.md + METHODOLOGY.md)
                                      et recalcule les contrôles automatiques dans chaque fichier
  python3 scripts/suivi.py validate   vérifie les cases cochées (justification, preuves existantes),
                                      la règle « g après a à f » et les règles de prudence (journaux)
  python3 scripts/suivi.py all        sync puis validate (utilisé par le crochet pre-commit)
  python3 scripts/suivi.py set <slug> <a-g> <x| |~> "<justification>" [preuve ...]
                                      coche ou décoche une étape avec justification et preuves
  python3 scripts/suivi.py data <slug> '<json>'
                                      fusionne des clés dans institutions/<slug>/data.json

Format d'une étape dans CONSIGNE-ET-SUIVI.md :
  ### a) Titre
  - [x] Fait               (« [ ] » : pas fait ; « [~] » : sans objet, décision de Marcel)
    - **Justification** : texte
    - **Preuves** : `chemin1`, `chemin2`          (chemins relatifs à la racine du dépôt)
"""
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import urlsplit

REPO = Path(__file__).resolve().parent.parent
INST = REPO / "institutions"
FICHIER = "CONSIGNE-ET-SUIVI.md"
DEBUT, FIN = "<!-- CONSIGNE:DEBUT -->", "<!-- CONSIGNE:FIN -->"
ADEBUT, AFIN = "<!-- AUTO:DEBUT -->", "<!-- AUTO:FIN -->"

ETAPES = [
    ("a", "Documentation lue en entier",
     "Toutes les pages de doc liées à l'API (développeurs, interfaces, conditions, FAQ, aide, mentions légales, robots.txt), téléchargées avec `scripts/fetch_doc.sh` (URL, date, SHA-256), lues en entier (`scripts/extract_text.py`)."),
    ("b", "Endpoints tirés de la doc",
     "Liste des endpoints citée par la doc (URL, exemples). Jamais devinée. Une interdiction ou une impossibilité écrite dans la doc justifie de renoncer (citer la phrase)."),
    ("c", "Configuration écrite AVANT les tests",
     "`config/<nom>.json` pilote `scripts/probe.py`, committée avant le lancement. Un endpoint absent de la doc mais non interdit se teste avec un script poli (identifiants issus de pages publiques ou d'exemples de la doc, pas de devinette)."),
    ("d", "Quota cherché dans la doc",
     "Pour chaque page lue : endpoint de statut, en-têtes de limite documentés, clé ou compte donnant un quota, contact pour un volume plus élevé. Chaque réponse cite sa source."),
    ("e", "Test systématique de chaque endpoint",
     "Chaque endpoint documenté est testé (budget 15 requêtes par passe, pause ≥ 6 s, GET/HEAD, UA du projet). Redirections du même hôte suivies. Un 403 arrête son hôte, un 429 arrête l'institution. Seules les interdictions écrites dans la doc dispensent de tester."),
    ("f", "Ce que disent les gens sur le web",
     "Plaintes, discussions, présentations de l'institution, politique envers les API et les bots, blogs, GitHub, forums, listes de diffusion. Sources étiquetées (officielle / institution / utilisateur / tiers), lues, citées."),
    ("g", "Crash test progressif",
     "Seulement après l'audit complet (a à f) de toutes les institutions et avec l'accord de Marcel : paliers jusqu'à 2 × la limite documentée, ou 200 req/min si illimité ou sans limite documentée. Arrêt au premier 429/403/CAPTCHA."),
]
CODES = [e[0] for e in ETAPES]


def lire_data(slug):
    p = INST / slug / "data.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def slugs():
    return sorted(p.name for p in INST.iterdir() if p.is_dir())


# ---------------------------------------------------------------- gabarit / init
def bloc_etape(code, titre, desc, etat=" ", justif="", preuves=()):
    pr = ", ".join(f"`{p}`" for p in preuves) if preuves else ""
    libelle = {"x": "Fait", " ": "Pas fait", "~": "Sans objet (décision de Marcel)"}[etat]
    return (f"### {code}) {titre}\n> {desc}\n\n- [{etat}] **{libelle}**\n"
            f"  - **Justification** : {justif}\n  - **Preuves** : {pr}\n")


def corps_defaut(slug, d):
    statut = d.get("statut_institution", "active")
    nom = d.get("nom", slug)
    cid = d.get("classeur_id", "")
    deja = (INST / slug / "tests" / "journal.log").exists() or (INST / slug / "fiche.md").exists()
    out = [f"# {nom} — consigne et suivi\n",
           f"- **Dossier** : `institutions/{slug}/`  ·  **Classeur de référence** : {cid}  ·  **Pays** : {d.get('pays', '')}",
           f"- **Statut d'institution** : {statut}",
           "- **Dernière mise à jour du suivi** : (à renseigner à chaque modification)\n",
           "## Suivi par étape (à cocher, avec justification et preuves)\n"]
    for code, titre, desc in ETAPES:
        if statut in ("écartée", "abandonnée"):
            out.append(bloc_etape(code, titre, desc, "~", f"Institution {statut} par décision de Marcel (voir CONSIGNE.md, C6)."))
        else:
            if deja:
                j = ("Passe antérieure non conforme à la méthode v2 (AUDIT-HAIKU.md) : à refaire. "
                     "Le matériel déjà présent dans ce dossier est conservé comme historique.")
            else:
                j = "Pas encore traitée : l'audit suit l'ordre du classeur de référence (une institution à la fois)."
            out.append(bloc_etape(code, titre, desc, " ", j))
    out.append("### Contrôles transversaux\n- Budget : 15 requêtes par passe · pauses ≥ 6 s · GET/HEAD seulement · UA du projet · aucun contournement. "
               "Ces contrôles sont calculés depuis le journal (voir « Contrôles automatiques »).\n")
    out.append(f"{ADEBUT}\n{AFIN}\n")
    out.append("## Consigne intégrale\n")
    out.append(f"{DEBUT}\n{FIN}\n")
    return "\n".join(out)


def cmd_init():
    n = 0
    for slug in slugs():
        f = INST / slug / FICHIER
        if f.exists():
            continue
        f.write_text(corps_defaut(slug, lire_data(slug)), encoding="utf-8")
        n += 1
    print(f"init : {n} fichier(s) créé(s)")


# ---------------------------------------------------------------- journaux : contrôles automatiques
ISO = re.compile(r"(\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d)Z")
URL = re.compile(r"https?://[^\s|)\"']+")
METH = re.compile(r"\|\s*(GET|HEAD|POST|PUT|PATCH|DELETE|OPTIONS)\b|\b(GET|HEAD|POST|PUT|PATCH|DELETE|OPTIONS)\b")


def analyser_journal(slug):
    """Retourne un dict : requêtes, sessions, max_par_session, min_pause, methodes, anomalies."""
    j = INST / slug / "tests" / "journal.log"
    res = {"requetes": 0, "sessions": 0, "max_par_session": 0, "min_pause": None,
           "methodes": set(), "anomalies": []}
    if not j.exists():
        return res
    derniere, dans_session, compte_session = {}, False, 0
    for ligne in j.read_text(encoding="utf-8", errors="replace").splitlines():
        if ligne.startswith("# Session"):
            dans_session, compte_session = True, 0
            res["sessions"] += 1
            continue
        if ligne.startswith("# Fin"):
            res["max_par_session"] = max(res["max_par_session"], compte_session)
            if compte_session > 15:
                res["anomalies"].append(f"session de {compte_session} requêtes (> 15)")
            dans_session = False
            continue
        if ligne.startswith("#") or not ligne.strip():
            continue
        if re.search(r"outil de lecture|WebFetch|lecture web|autorisé par Marcel \(C12\)", ligne, re.I):
            continue
        t, u = ISO.search(ligne), URL.search(ligne)
        if not (t and u) or "NON LANCÉ" in ligne:
            continue
        res["requetes"] += 1
        if dans_session:
            compte_session += 1
        m = METH.search(ligne)
        if m:
            meth = m.group(1) or m.group(2)
            res["methodes"].add(meth)
            if meth not in ("GET", "HEAD"):
                res["anomalies"].append(f"méthode {meth} interdite")
        ts = datetime.strptime(t.group(1), "%Y-%m-%dT%H:%M:%S")
        h = urlsplit(u.group(0)).hostname
        if h in derniere:
            dt = (ts - derniere[h]).total_seconds()
            res["min_pause"] = dt if res["min_pause"] is None else min(res["min_pause"], dt)
            if dt < 6:
                res["anomalies"].append(f"pause de {dt:.0f} s < 6 s vers {h}")
        derniere[h] = ts
    return res


def texte_auto(slug):
    r = analyser_journal(slug)
    if r["requetes"] == 0:
        return "Aucune requête enregistrée dans `tests/journal.log`."
    mp = "—" if r["min_pause"] is None else f"{r['min_pause']:.0f} s"
    lignes = [f"- Requêtes enregistrées : **{r['requetes']}** (sessions de sonde : {r['sessions']}, "
              f"maximum par session : {r['max_par_session']})",
              f"- Plus courte pause vers un même hôte : **{mp}** (règle : ≥ 6 s)",
              f"- Méthodes utilisées : {', '.join(sorted(r['methodes'])) or '—'} (règle : GET/HEAD seulement)"]
    lignes.append("- Anomalies : " + ("**" + " ; ".join(r["anomalies"]) + "**" if r["anomalies"] else "aucune"))
    return "\n".join(lignes)


# ---------------------------------------------------------------- sync
def cmd_sync():
    consigne = (REPO / "CONSIGNE.md").read_text(encoding="utf-8").strip()
    methode = (REPO / "METHODOLOGY.md").read_text(encoding="utf-8").strip()
    integral = f"{consigne}\n\n---\n\n# Méthode (METHODOLOGY.md, recopiée)\n\n{methode}"
    n = 0
    for slug in slugs():
        f = INST / slug / FICHIER
        if not f.exists():
            continue
        t = f.read_text(encoding="utf-8")
        t2 = re.sub(re.escape(DEBUT) + r".*?" + re.escape(FIN), lambda _m: f"{DEBUT}\n{integral}\n{FIN}", t, flags=re.S)
        t2 = re.sub(re.escape(ADEBUT) + r".*?" + re.escape(AFIN),
                    lambda _m: f"{ADEBUT}\n## Contrôles automatiques (calculés depuis `tests/journal.log`)\n{texte_auto(slug)}\n{AFIN}",
                    t2, flags=re.S)
        if t2 != t:
            f.write_text(t2, encoding="utf-8")
            n += 1
    print(f"sync : {n} fichier(s) mis à jour")


# ---------------------------------------------------------------- validate
ETAPE_RE = re.compile(r"^### ([a-g])\) .*?\n(.*?)(?=^### |^## |\Z)", re.S | re.M)
CASE_RE = re.compile(r"^- \[( |x|~)\]", re.M)
JUST_RE = re.compile(r"\*\*Justification\*\* : (.*)")
PREU_RE = re.compile(r"\*\*Preuves\*\* : (.*)")


def lire_suivi(slug):
    """Retourne {code: (etat, justification, [preuves])} ou None si le fichier est absent."""
    f = INST / slug / FICHIER
    if not f.exists():
        return None
    t = f.read_text(encoding="utf-8")
    statut = re.search(r"\*\*Statut d'institution\*\* : (\S+)", t)
    out = {}
    for m in ETAPE_RE.finditer(t):
        bloc = m.group(2)
        c = CASE_RE.search(bloc)
        j = JUST_RE.search(bloc)
        p = PREU_RE.search(bloc)
        out[m.group(1)] = (c.group(1) if c else "?", j.group(1).strip() if j else "",
                           re.findall(r"`([^`]+)`", p.group(1)) if p else [])
    return (statut.group(1) if statut else "active"), out


CATEGORIES_WEB = ("institution", "utilisateurs", "tickets", "presentations")
ANCIENNES = REPO / "data" / "exigence_ancienne.txt"
EXEMPT_ORDRE = REPO / "data" / "exemption_ordre_travail_anterieur.txt"  # décision de Marcel 14/11/2026 : travail antérieur au verrou, exempté de l'ORDRE seulement
HAIKU = REPO / "data" / "ancien_travail_haiku.txt"  # commencées par l'ancienne méthode, à refaire dans l'ordre


def anciennes():
    return set(ANCIENNES.read_text(encoding="utf-8").split()) if ANCIENNES.exists() else set()


MOTIF_API = re.compile(r"(?i)(/oai\b|oai\.php|/iiif|/i3f|/api\b|/api/|manifest|info\.json|/sparql|/rest/|ftpack|/download/|/search\b|/v[0-9]/|/services/)")


def urls_api_dans_la_doc(slug, hotes):
    """URL d'API citées par la doc téléchargée (sources/**/raw, text) sur les hôtes de l'institution : (hôte, 1er segment) -> exemple."""
    trouvees = {}
    for f in list((INST / slug / "sources").rglob("*.html")) + list((INST / slug / "sources").rglob("*.txt")) + \
            list((INST / slug / "sources").rglob("*.md")):
        if f.name in ("SHA256SUMS", "FETCH.log"):
            continue
        t = f.read_text(encoding="utf-8", errors="replace")
        for u in re.findall(r"https?://[^\s\"'<>)\]\\]+", t):
            u = u.rstrip(".,;:").replace("&amp;", "&")
            sp = urlsplit(u)
            if sp.netloc in hotes and MOTIF_API.search(sp.path or "/") and not re.search(r"\.(css|js|png|jpe?g|svg|ico|woff2?)$", sp.path):
                seg = sp.path.strip("/").split("/")[0] if sp.path.strip("/") else ""
                trouvees.setdefault((sp.netloc, seg), u)
    return trouvees


def docs_html_lues(slug):
    """Pages de doc exclues du contrôle de couverture, de façon MÉCANIQUE : {(hôte, 1er segment): (url, fichier)}.
    Conditions cumulatives : ligne de FETCH.log avec code 200 ET fichier téléchargé qui est de l'HTML
    (un endpoint qui répond en JSON, XML, texte brut ou image n'est JAMAIS exclu)."""
    out = {}
    for log in (INST / slug / "sources").rglob("FETCH.log"):
        lignes = [l for l in log.read_text(encoding="utf-8", errors="replace").splitlines() if re.match(r"\d{4}-\d\d-\d\dT", l)]
        for i, l in enumerate(lignes, start=1):
            parts = [x.strip() for x in l.split("|")]
            if len(parts) < 4 or parts[1] != "200":
                continue
            raw = log.parent / "raw" / f"{i:02d}.html"
            if not raw.exists():
                continue
            tete = raw.read_bytes()[:400].decode("utf-8", "replace").lstrip("\ufeff \n\r\t").lower()
            if not (tete.startswith("<!doctype html") or tete.startswith("<html") or tete.startswith("<head") or "<html" in tete[:200]):
                continue
            sp = urlsplit(parts[3])
            out[(sp.netloc, sp.path.strip("/").split("/")[0] if sp.path.strip("/") else "")] = (parts[3], str(raw.relative_to(REPO)))
    return out


def couverture_doc(slug, d):
    hotes = {h.get("hote") for h in d.get("hotes_robots", [])}
    couverts = {k for k in docs_html_lues(slug)}
    sources = list(d.get("endpoints_documentes", [])) + list(d.get("endpoints_ecartes", []))
    for f in (INST / slug / "config").glob("*.json"):
        try:
            sources += json.loads(f.read_text(encoding="utf-8")).get("endpoints", [])
        except ValueError:
            pass
    for e in sources:
        sp = urlsplit(e.get("url", ""))
        couverts.add((sp.netloc, sp.path.strip("/").split("/")[0] if sp.path.strip("/") else ""))
    return [f"URL d'API citée par la doc et ni testée ni justifiée : {u} (ajouter à endpoints_documentes, ou à endpoints_ecartes avec url + raison)"
            for k, u in sorted(urls_api_dans_la_doc(slug, hotes).items()) if k not in couverts]


def _git_ajout(path):
    """Date (UTC) du premier commit qui a ajouté ce fichier, ou None."""
    import subprocess
    r = subprocess.run(["git", "log", "--diff-filter=A", "--format=%cI", "--", str(path)], cwd=REPO, capture_output=True, text=True)
    l = [x for x in r.stdout.split() if x]
    return datetime.fromisoformat(l[-1]).astimezone(__import__("datetime").timezone.utc) if l else None


def config_avant_sessions(slug):
    """C8/étape c : chaque session du journal doit citer une configuration committée AVANT son lancement."""
    j = INST / slug / "tests" / "journal.log"
    m = []
    if not j.exists():
        return m
    for ts, cfg in re.findall(r"^# Session (\S+Z) — configuration (\S+\.json)", j.read_text(encoding="utf-8"), re.M):
        f = INST / slug / "config" / cfg
        t0 = datetime.fromisoformat(ts.replace("Z", "+00:00"))
        c = _git_ajout(f.relative_to(REPO)) if f.exists() else None
        if c is None:
            m.append(f"session {ts} : configuration {cfg} absente ou jamais committée")
        elif c > t0:
            m.append(f"session {ts} : configuration {cfg} committée APRÈS le lancement ({c.isoformat()})")
    return m


def crash_manques(slug):
    """Étape g : journal de crash test existant, terminé, avec configuration committée AVANT chaque lancement."""
    j = INST / slug / "tests" / "crash" / f"{slug}.log"
    if not j.exists():
        return ["aucun journal de crash test (tests/crash/<slug>.log) : lancer scripts/crash.py"]
    t = j.read_text(encoding="utf-8")
    m = []
    deb = re.findall(r"^# Crash test (\S+Z) — configuration (\S+\.json)", t, re.M)
    if not deb:
        m.append("journal de crash test sans session")
    if len(re.findall(r"^# Fin ", t, re.M)) < len(deb):
        m.append("crash test commencé mais non terminé (pas de ligne « # Fin »)")
    for ts, cfg in deb:
        f = INST / slug / "config" / cfg
        c = _git_ajout(f.relative_to(REPO)) if f.exists() else None
        t0 = datetime.fromisoformat(ts.replace("Z", "+00:00"))
        if c is None:
            m.append(f"crash test {ts} : configuration {cfg} absente ou jamais committée")
        elif c > t0:
            m.append(f"crash test {ts} : configuration {cfg} committée APRÈS le lancement")
    return m


def controle_par_etape(slug, d):
    """Critères mesurables de TOUTES les consignes, rangés par étape : {a..f: [manques]}."""
    E = {c: [] for c in "abcdefg"}
    fiche = INST / slug / "fiche.md"
    if not fiche.exists() or "onclusion" not in fiche.read_text(encoding="utf-8", errors="replace"):
        E["d"].append("fiche.md absente ou sans section Conclusion")
    if not list((INST / slug / "sources").rglob("SHA256SUMS")):
        E["a"].append("aucun SHA256SUMS : documentation non hachée (sources/…/SHA256SUMS)")
    hotes = {h.get("hote"): h for h in d.get("hotes_robots", [])}
    if not hotes:
        E["a"].append("hotes_robots vide (un robots.txt lu par hôte contacté ou cité)")
    for h in hotes.values():
        if not (h.get("preuve") and (REPO / h["preuve"]).exists()):
            E["a"].append(f"robots.txt de {h.get('hote')} sans preuve existante")
    eps = d.get("endpoints_documentes", [])
    if not eps:
        E["b"].append("endpoints_documentes vide (une ligne par famille d'API : teste / non_teste)")
    for e in eps:
        if e.get("statut") == "teste":
            if not (e.get("preuve") and (REPO / e["preuve"]).exists()):
                E["e"].append(f"endpoint « {e.get('famille')} » testé sans preuve existante")
        elif e.get("statut") == "non_teste":
            if len(e.get("raison", "")) < 30:
                E["e"].append(f"endpoint « {e.get('famille')} » non testé sans raison suffisante")
        else:
            E["b"].append(f"endpoint « {e.get('famille')} » sans statut teste/non_teste")
    for e in d.get("endpoints_ecartes", []):
        if len(e.get("raison", "")) < 30:
            E["b"].append(f"endpoint écarté {e.get('url')} sans raison suffisante")
    E["b"] += couverture_doc(slug, d)
    for f in sorted((INST / slug / "config").glob("*.json")):
        try:
            cfg = json.loads(f.read_text(encoding="utf-8"))
        except ValueError:
            E["c"].append(f"configuration {f.name} illisible")
            continue
        for ep in cfg.get("endpoints", []):
            h = re.sub(r"^https?://([^/]+)/.*$", r"\1", ep.get("url", ""))
            if h and h not in hotes:
                E["c"].append(f"hôte {h} contacté (config {f.name}) sans entrée hotes_robots")
    E["c"] += config_avant_sessions(slug)
    E["g"] += crash_manques(slug)
    for k in ("contact", "conclusion_quota", "classe_quota", "confiance"):
        if not str(d.get(k) or "").strip():
            E["d"].append(f"champ {k} vide")
    for l in d.get("limites_documentees", []):
        if not (l.get("verification") and l.get("source") and l.get("date")):
            E["d"].append(f"limite « {l.get('nature')} » sans verification/source/date")
    if d.get("rattrapage_a_faire"):
        E["e"].append(f"{len(d['rattrapage_a_faire'])} élément(s) de rattrapage_a_faire non traités")
    bloc = [b for b in d.get("blocages", []) if re.search(r"(?i)403|401|405|captcha|dns|tls|timeout|délai|reset", str(b.get("code", "")) + str(b.get("nature", "")))]
    if bloc and not d.get("a_verifier_manuellement"):
        E["e"].append("blocages (403/401/CAPTCHA/DNS/TLS/délai) sans aucune URL dans a_verifier_manuellement")
    cats = {w.get("categorie") for w in d.get("web", []) if w.get("categorie") in CATEGORIES_WEB
            and (w.get("url") or (w.get("aucun_resultat") and w.get("requete")))}
    if len(cats) < 4:
        E["f"].append(f"web : {len(cats)}/4 catégories ({', '.join(sorted(set(CATEGORIES_WEB) - cats))} manquantes)")
    return E


def controle_v3(slug, d):
    """Tous les manques, toutes étapes confondues (liste plate triée)."""
    return sorted({x for v in controle_par_etape(slug, d).values() for x in v})


def ordre():
    """Institutions du classeur dans l'ordre de la consigne (GLAM-001, 002…), extras exclus."""
    out = []
    for slug in slugs():
        d = lire_data(slug)
        if re.fullmatch(r"GLAM-\d{3}", str(d.get("classeur_id") or "")):
            out.append((d["classeur_id"], slug))
    return [s for _, s in sorted(out)]


def commencee(slug):
    d = INST / slug
    if any((d / "config").glob("*.json")):
        return True
    j = d / "tests" / "journal.log"
    if j.exists() and j.stat().st_size > 0:
        return True
    r = lire_suivi(slug)
    return bool(r and any(v[0] == "x" for v in r[1].values()))


def manques_complets(slug):
    """Tout ce qui empêche de dire « institution terminée » (étapes a–f cochées + exigence v3 + journal)."""
    r = lire_suivi(slug)
    m = []
    if r is None:
        return ["CONSIGNE-ET-SUIVI.md absent"]
    for c in "abcdefg":
        if r[1].get(c, (" ",))[0] != "x":
            m.append(f"étape {c}) non cochée")
    m += controle_v3(slug, lire_data(slug))
    m += analyser_journal(slug)["anomalies"]
    return m


def termine(slug):
    r = lire_suivi(slug)
    if r is None:
        return False
    if r[0] != "active":
        return True
    return not manques_complets(slug)


def verrou_ordre():
    """Impossible de commencer l'institution suivante avant d'avoir tout validé la précédente."""
    erreurs, o = [], ordre()
    for i, slug in enumerate(o):
        r = lire_suivi(slug)
        if not r or r[0] != "active" or slug in set(HAIKU.read_text().split() if HAIKU.exists() else []) or slug in set(EXEMPT_ORDRE.read_text().split() if EXEMPT_ORDRE.exists() else []) or not commencee(slug):
            continue
        for prec in o[:i]:
            if not termine(prec):
                erreurs.append(f"{slug}: VERROU : commencée alors que {prec} n'est pas terminée "
                               f"({'; '.join(manques_complets(prec))[:200]})")
                break
    return erreurs


def cmd_autorise(slug):
    """Utilisé par probe.py, crash.py, fetch_doc.sh : refuse de lancer du trafic pour une institution
    dont une antérieure (ordre du classeur) n'est pas terminée (étapes a–g + exigences)."""
    o = ordre()
    if slug not in o:
        return 0
    for prec in o[:o.index(slug)]:
        if not termine(prec):
            print(f"REFUSÉ : {slug} ne peut pas être traitée avant {prec} (non terminée : "
                  f"{'; '.join(manques_complets(prec))[:160]}). Lancer : python3 scripts/suivi.py porte {prec}")
            return 1
    return 0


def cmd_porte(slug=None):
    o = ordre()
    if slug is None:
        slug = next((s for s in o if not termine(s)), None)
        if slug is None:
            print("Toutes les institutions sont terminées.")
            return 0
    m = manques_complets(slug)
    print(f"{slug} : " + ("TERMINÉE, on peut passer à la suivante." if not m else f"{len(m)} manque(s) avant de passer à la suivante :"))
    for x in m:
        print("  ☐", x)
    nxt = [s for s in o if not termine(s)]
    print("Prochaine à traiter :", nxt[0] if nxt else "aucune")
    return 0 if not m else 1


def cmd_validate():
    erreurs = []
    for slug in slugs():
        s = lire_suivi(slug)
        if s is None:
            erreurs.append(f"{slug}: {FICHIER} absent")
            continue
        statut, etapes = s
        for code in CODES:
            if code not in etapes:
                erreurs.append(f"{slug}: étape {code}) absente")
                continue
            etat, just, preuves = etapes[code]
            if etat == "?":
                erreurs.append(f"{slug}: étape {code}) sans case à cocher")
            elif etat == "x":
                if len(just) < 20:
                    erreurs.append(f"{slug}: étape {code}) cochée sans justification suffisante")
                if not preuves:
                    erreurs.append(f"{slug}: étape {code}) cochée sans preuve")
                for p in preuves:
                    if not (REPO / p).exists():
                        erreurs.append(f"{slug}: étape {code}) preuve introuvable : {p}")
            elif etat == " ":
                if len(just) < 10:
                    erreurs.append(f"{slug}: étape {code}) non cochée sans justification")
            elif etat == "~":
                if statut not in ("écartée", "abandonnée"):
                    erreurs.append(f"{slug}: étape {code}) « sans objet » réservé aux institutions écartées ou abandonnées")
        if statut == "active":
            par = controle_par_etape(slug, lire_data(slug))
            for code in "abcdefg":
                if etapes.get(code, (" ",))[0] == "x":
                    for manque in par[code]:
                        erreurs.append(f"{slug}: étape {code}) cochée mais : {manque}")
        if statut == "active" and etapes.get("g", (" ",))[0] == "x" and any(etapes.get(c, (" ",))[0] != "x" for c in "abcdef"):
            erreurs.append(f"{slug}: crash test (g) coché avant l'audit complet (a à f)")
        for a in analyser_journal(slug)["anomalies"]:
            erreurs.append(f"{slug}: journal : {a}")
    erreurs += verrou_ordre()
    if erreurs:
        print("VALIDATION : ÉCHEC")
        for e in erreurs[:60]:
            print("  -", e)
        if len(erreurs) > 60:
            print(f"  … et {len(erreurs) - 60} autres")
        return 1
    print(f"VALIDATION : OK ({len(slugs())} institutions)")
    return 0


def cmd_set(slug, code, etat, justif, preuves):
    if code not in CODES or etat not in ("x", " ", "~"):
        sys.exit("usage : set <slug> <a-g> <x| |~> \"justification\" [preuve ...]")
    f = INST / slug / FICHIER
    if not f.exists():
        sys.exit(f"{f} absent (lancer : python3 scripts/suivi.py init)")
    titre, desc = [(t, d) for c, t, d in ETAPES if c == code][0]
    nouveau = bloc_etape(code, titre, desc, etat, justif, preuves)
    t = f.read_text(encoding="utf-8")
    t2, n = re.subn(r"### " + code + r"\) .*?(?=^### |^## |\Z)", lambda _m: nouveau + "\n", t, count=1, flags=re.S | re.M)
    if n != 1:
        sys.exit(f"étape {code}) introuvable dans {f}")
    t2 = re.sub(r"(\*\*Dernière mise à jour du suivi\*\* : ).*", lambda m: m.group(1) + datetime.now().strftime("%Y-%m-%d"), t2, count=1)
    f.write_text(t2, encoding="utf-8")
    print(f"{slug} étape {code}) -> [{etat}]")


def cmd_data(slug, js):
    p = INST / slug / "data.json"
    d = json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}
    d.update(json.loads(js))
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{slug} data.json mis à jour : {', '.join(json.loads(js))}")


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "all"
    if cmd == "init":
        cmd_init()
    elif cmd == "sync":
        cmd_sync()
    elif cmd == "autorise":
        sys.exit(cmd_autorise(sys.argv[2]))
    elif cmd == "porte":
        sys.exit(cmd_porte(sys.argv[2] if len(sys.argv) > 2 else None))
    elif cmd == "validate":
        sys.exit(cmd_validate())
    elif cmd == "all":
        cmd_sync()
        sys.exit(cmd_validate())
    elif cmd == "set":
        cmd_set(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6:])
    elif cmd == "data":
        cmd_data(sys.argv[2], sys.argv[3])
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
