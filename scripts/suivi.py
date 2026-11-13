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
        if re.search(r"outil de lecture|WebFetch|lecture web", ligne, re.I):
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
        if statut == "active" and etapes.get("g", (" ",))[0] == "x" and any(etapes.get(c, (" ",))[0] != "x" for c in "abcdef"):
            erreurs.append(f"{slug}: crash test (g) coché avant l'audit complet (a à f)")
        for a in analyser_journal(slug)["anomalies"]:
            erreurs.append(f"{slug}: journal : {a}")
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
