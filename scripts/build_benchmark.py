#!/usr/bin/env python3
"""Génère BENCHMARK.xlsx à partir des dossiers d'institutions.

Sources (rien n'est saisi dans le classeur) :
  institutions/<slug>/data.json              données structurées (limites, en-têtes, blocages, sources, web)
  institutions/<slug>/CONSIGNE-ET-SUIVI.md   étapes a à g : case, justification, preuves
Chaque preuve citée est VÉRIFIÉE sur le disque. Une limite n'est comptée comme « officielle
chiffrée » que si sa vérification est « officielle », qu'elle a un chiffre, que l'institution est
active, que l'étape d) est cochée et que les données ne sont pas marquées « à revalider ».

Usage : python3 scripts/build_benchmark.py   (nécessite openpyxl)
Sortie : BENCHMARK.xlsx à la racine du dépôt.
"""
import re
import subprocess
from urllib.parse import urlsplit
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import suivi  # noqa: E402

from openpyxl import Workbook  # noqa: E402
from openpyxl.chart import BarChart, PieChart, Reference  # noqa: E402
from openpyxl.chart.label import DataLabelList  # noqa: E402
from openpyxl.styles import Alignment, Font, PatternFill  # noqa: E402
from openpyxl.utils import get_column_letter  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "BENCHMARK.xlsx"
ETAPES = [(c, f"{c}) {t}") for c, t, _ in suivi.ETAPES]
ETAPES_AUDIT = "abcdef"

VERT = PatternFill("solid", fgColor="C6EFCE")
ORANGE = PatternFill("solid", fgColor="FFEB9C")
ROUGE = PatternFill("solid", fgColor="FFC7CE")
GRIS = PatternFill("solid", fgColor="EDEDED")
ENTETE = PatternFill("solid", fgColor="1F3A5F")
TITRE = Font(bold=True, size=14, color="1F3A5F")
BLANC_GRAS = Font(bold=True, color="FFFFFF")


# ------------------------------------------------------------------ chargement
def charger():
    """Liste de dicts : data.json + 'suivi' (statut, étapes) + 'preuves' vérifiées."""
    out = []
    for slug in suivi.slugs():
        d = suivi.lire_data(slug)
        d.setdefault("slug", slug)
        # Les agents écrivent parfois du texte au lieu d'objets dans ces listes : on normalise pour ne jamais planter.
        for champ in ("en_tetes_observes", "blocages", "limites_documentees", "sources", "web", "a_verifier_manuellement",
                      "endpoints_documentes", "endpoints_ecartes", "hotes_robots", "derogations"):
            v = d.get(champ)
            if isinstance(v, list):
                d[champ] = [x if isinstance(x, dict) else {"texte": str(x)} for x in v]
            elif v is not None and not isinstance(v, list):
                d[champ] = [{"texte": str(v)}]
        s = suivi.lire_suivi(slug)
        statut, etapes = s if s else ("active", {})
        d["statut_institution"] = statut
        d["etapes"] = etapes
        pre = []
        for code, (_e, _j, preuves) in etapes.items():
            for p in preuves:
                pre.append((code, p, (REPO / p).exists()))
        d["preuves"] = pre
        out.append(d)
    out.sort(key=lambda d: (d.get("classeur_id", "~") if str(d.get("classeur_id", "")).startswith("GLAM-") else "~~" + d["slug"]))
    return out


def etat(d, code):
    return d["etapes"].get(code, ("?", "", []))[0]


def libelle_etat(e):
    return {"x": "fait", " ": "pas fait", "~": "sans objet (décision de Marcel)"}.get(e, "non renseigné")


def couleur(e):
    return {"x": VERT, " ": ROUGE, "~": GRIS}.get(e, ROUGE)


def score(d):
    return sum(1 for c in ETAPES_AUDIT if etat(d, c) == "x")


def actif(d):
    return d["statut_institution"] == "active"


def limite_comptee(d, lim):
    return (actif(d) and etat(d, "d") == "x" and not d.get("donnees_a_revalider")
            and str(lim.get("verification", "")).lower().startswith("officielle")
            and any(ch.isdigit() for ch in str(lim.get("valeur", ""))))


# ------------------------------------------------------------------ utilitaires feuille
def entete(ws, ligne, valeurs, largeurs=None):
    for i, v in enumerate(valeurs, start=1):
        c = ws.cell(row=ligne, column=i, value=v)
        c.fill, c.font = ENTETE, BLANC_GRAS
        c.alignment = Alignment(wrap_text=True, vertical="center")
    if largeurs:
        for i, w in enumerate(largeurs, start=1):
            ws.column_dimensions[get_column_letter(i)].width = w
    ws.freeze_panes = ws.cell(row=ligne + 1, column=1)


def ecrire(ws, debut, lignes):
    for n, vals in enumerate(lignes, start=debut):
        for c, v in enumerate(vals, start=1):
            ws.cell(row=n, column=c, value=v).alignment = Alignment(wrap_text=True, vertical="top")
    return debut + len(lignes)


def sha():
    try:
        return subprocess.run(["git", "-C", str(REPO), "rev-parse", "--short", "HEAD"],
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:  # noqa: BLE001
        return "inconnu"


# ------------------------------------------------------------------ feuilles
def tableau_de_bord(wb, D, commit):
    ws = wb.active
    ws.title = "Tableau de bord"
    ws["A1"] = "BENCHMARK IIIF — quotas et politiques d'accès des API (généré)"
    ws["A1"].font = TITRE
    ws["A2"] = f"Généré le {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC · commit {commit} · {len(D)} dossiers d'institutions"
    ws["A3"] = ("« non trouvé » = absent des pages lues, pas une preuve d'absence de limite. "
                "Seules les étapes cochées avec preuves comptent.")
    act = [d for d in D if actif(d)]
    hors = [d for d in D if not actif(d)]
    complet = sum(1 for d in act if score(d) == 6)
    commence = sum(1 for d in act if score(d) > 0)
    chiffrees = sum(1 for d in act for l in d.get("limites_documentees", []) if limite_comptee(d, l))
    a_revalider = sum(1 for d in act if d.get("donnees_a_revalider"))
    observes = sum(len(d.get("en_tetes_observes", [])) for d in act if etat(d, "e") == "x")
    bloques = sum(1 for d in act for b in d.get("blocages", []) if b.get("code") == "403")
    pre = [p for d in D for p in d["preuves"]]
    ok_pre = sum(1 for _, _, e in pre if e)
    kpi = [
        ("Dossiers d'institutions", len(D)),
        ("Actives (à auditer)", len(act)),
        ("Écartées ou abandonnées (décision de Marcel)", len(hors)),
        ("Audit commencé (≥ 1 étape cochée)", commence),
        ("Audit complet (étapes a à f cochées)", complet),
        ("Limites officielles chiffrées (étape d cochée)", chiffrees),
        ("Institutions dont les données sont à revalider (ancienne passe)", a_revalider),
        ("En-têtes de quota observés (étape e cochée)", observes),
        ("Blocages 403 anti-bot consignés", bloques),
        ("Preuves citées présentes sur le disque", f"{ok_pre} / {len(pre)}"),
    ]
    ws["A5"] = "INDICATEURS"
    ws["A5"].font = Font(bold=True, size=12)
    for n, (k, v) in enumerate(kpi, start=6):
        ws.cell(row=n, column=1, value=k)
        ws.cell(row=n, column=2, value=v).font = Font(bold=True)
    ws.column_dimensions["A"].width = 58
    ws.column_dimensions["B"].width = 18

    # Graphique 1 : institutions ayant fait chaque étape
    l1 = 18
    ws.cell(row=l1 - 1, column=1, value="ÉTAPES COCHÉES (institutions actives)").font = Font(bold=True, size=12)
    entete(ws, l1, ["Étape", "Institutions qui l'ont faite"])
    for n, (c, t) in enumerate(ETAPES, start=l1 + 1):
        ws.cell(row=n, column=1, value=t)
        ws.cell(row=n, column=2, value=sum(1 for d in act if etat(d, c) == "x"))
    g1 = BarChart()
    g1.type, g1.title = "bar", "Institutions ayant fait chaque étape"
    g1.add_data(Reference(ws, min_col=2, min_row=l1, max_row=l1 + len(ETAPES)), titles_from_data=True)
    g1.set_categories(Reference(ws, min_col=1, min_row=l1 + 1, max_row=l1 + len(ETAPES)))
    g1.height, g1.width = 9, 18
    ws.add_chart(g1, "D5")

    # Graphique 2 : répartition du nombre d'étapes faites
    l2 = l1 + len(ETAPES) + 3
    ws.cell(row=l2 - 1, column=1, value="AVANCEMENT (nombre d'étapes a à f cochées)").font = Font(bold=True, size=12)
    entete(ws, l2, ["Étapes cochées", "Institutions"])
    rep = Counter(score(d) for d in act)
    for n, k in enumerate(range(0, 7), start=l2 + 1):
        ws.cell(row=n, column=1, value=f"{k} sur 6")
        ws.cell(row=n, column=2, value=rep.get(k, 0))
    g2 = BarChart()
    g2.type, g2.title = "col", "Institutions par nombre d'étapes cochées"
    g2.add_data(Reference(ws, min_col=2, min_row=l2, max_row=l2 + 7), titles_from_data=True)
    g2.set_categories(Reference(ws, min_col=1, min_row=l2 + 1, max_row=l2 + 7))
    g2.height, g2.width = 9, 18
    ws.add_chart(g2, "D25")

    # Graphique 3 : classes de quota (institutions dont l'étape d est cochée)
    l3 = l2 + 11
    ws.cell(row=l3 - 1, column=1, value="CLASSES DE QUOTA (étape d cochée)").font = Font(bold=True, size=12)
    classes = Counter(d.get("classe_quota", "non renseigné") for d in act if etat(d, "d") == "x")
    entete(ws, l3, ["Classe", "Institutions"])
    if classes:
        for n, (cl, nb) in enumerate(sorted(classes.items()), start=l3 + 1):
            ws.cell(row=n, column=1, value=cl)
            ws.cell(row=n, column=2, value=nb)
        pie = PieChart()
        pie.title = "Classes de quota"
        pie.add_data(Reference(ws, min_col=2, min_row=l3, max_row=l3 + len(classes)), titles_from_data=True)
        pie.set_categories(Reference(ws, min_col=1, min_row=l3 + 1, max_row=l3 + len(classes)))
        pie.dataLabels = DataLabelList()
        pie.dataLabels.showPercent = True
        pie.height, pie.width = 9, 14
        ws.add_chart(pie, "D43")
    else:
        ws.cell(row=l3 + 1, column=1, value="Aucune institution n'a encore l'étape d cochée.")


def feuille_institutions(wb, D):
    ws = wb.create_sheet("Institutions")
    cols = (["Classeur", "Institution", "Pays", "Dossier", "Statut"] + [t for _, t in ETAPES] +
            ["Étapes a–f cochées", "Preuves présentes", "Classe de quota", "Conclusion (quota)", "Contact"])
    entete(ws, 1, cols, [12, 40, 14, 38, 16] + [26] * 7 + [12, 14, 28, 60, 30])
    for n, d in enumerate(D, start=2):
        ok = sum(1 for _, _, e in d["preuves"] if e)
        vals = [d.get("classeur_id", ""), d.get("nom", d["slug"]), d.get("pays", ""),
                f"institutions/{d['slug']}/", d["statut_institution"]]
        for c, _ in ETAPES:
            e, just, _ = d["etapes"].get(c, ("?", "", []))
            vals.append(f"{libelle_etat(e)} — {just[:110]}")
        vals += [f"{score(d)} / 6", f"{ok} / {len(d['preuves'])}",
                 d.get("classe_quota", "") if etat(d, "d") == "x" else "",
                 d.get("conclusion_quota", "") if etat(d, "d") == "x" else "",
                 d.get("contact", "") if etat(d, "d") == "x" else ""]
        for c, v in enumerate(vals, start=1):
            ws.cell(row=n, column=c, value=v).alignment = Alignment(wrap_text=True, vertical="top")
        for i, (c, _) in enumerate(ETAPES, start=6):
            ws.cell(row=n, column=i).fill = couleur(etat(d, c))


def feuille_limites(wb, D):
    ws = wb.create_sheet("Limites")
    cols = ["Institution", "Nature", "Périmètre", "Valeur", "Fenêtre", "Effet au dépassement",
            "Vérification", "Compté comme officiel chiffré ?", "Données à revalider ?", "Source (URL)", "Date de lecture"]
    entete(ws, 1, cols, [34, 24, 30, 24, 14, 24, 34, 16, 14, 66, 14])
    lignes = []
    for d in D:
        for l in d.get("limites_documentees", []):
            lignes.append([d.get("nom", d["slug"]), l.get("nature"), l.get("perimetre"), l.get("valeur"),
                           l.get("fenetre"), l.get("effet"), l.get("verification", "non renseignée"),
                           "oui" if limite_comptee(d, l) else "non",
                           "oui (ancienne passe)" if d.get("donnees_a_revalider") else "non",
                           l.get("source"), l.get("date")])
    ecrire(ws, 2, lignes or [["(aucune)"] + [""] * 10])


LIMITE_RE = re.compile(r"(?i)^(x-)?(ratelimit|rate-limit|x-rate|retry-after|x-retry|quota|x-quota|x-.*rate.?limit|x-throttl|throttl|cf-mitigated)")


def _entetes_bruts(slug):
    """Lit tests/raw/*.headers.txt (écrits par la sonde) : {fichier: (date, méthode, url, statut, [(nom, valeur)])}."""
    out = []
    for f in sorted((suivi.INST / slug / "tests" / "raw").glob("*.headers.txt")):
        try:
            lignes = f.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError:
            continue
        if len(lignes) < 2:
            continue
        m = re.match(r"(\S+)\s+(\S+)\s+(\S+)", lignes[0])
        st = lignes[1].replace("HTTP", "").strip()
        h = [tuple(l.split(": ", 1)) for l in lignes[2:] if ": " in l]
        out.append((f, m.group(1) if m else "", m.group(2) if m else "", m.group(3) if m else "", st, h))
    return out


def feuille_entetes(wb, D):
    """Construit l'onglet DIRECTEMENT depuis les en-têtes bruts enregistrés (objectif, complet), une ligne par en-tête de limite."""
    ws = wb.create_sheet("En-têtes observés")
    entete(ws, 1, ["Institution", "GLAM", "Hôte", "En-tête de limite", "Valeur observée", "Réponse", "Date (UTC)", "Preuve (fichier brut)", "Réponses enregistrées", "Données à revalider ?"],
           [34, 11, 34, 26, 40, 10, 22, 60, 12, 12])
    lignes = []
    for d in D:
        brut = _entetes_bruts(d["slug"])
        trouves = 0
        for f, date, meth, url, st, hs in brut:
            for k, v in hs:
                if LIMITE_RE.match(k):
                    trouves += 1
                    lignes.append([d.get("nom", d["slug"]), d.get("classeur_id"), urlsplit(url).netloc, k, v, st, date,
                                   str(f.relative_to(REPO)), len(brut), "oui" if d.get("donnees_a_revalider") else "non"])
        if not trouves:
            lignes.append([d.get("nom", d["slug"]), d.get("classeur_id"), "—", "(aucun en-tête de limite)",
                           f"observé sur {len(brut)} réponse(s) enregistrée(s)" if brut else "aucune réponse enregistrée (hôtes bloqués ou non testés)",
                           "", "", "", len(brut), "oui" if d.get("donnees_a_revalider") else "non"])
    ecrire(ws, 2, lignes)
    ws.auto_filter.ref = f"A1:J{len(lignes) + 1}"


def feuille_blocages(wb, D):
    ws = wb.create_sheet("Blocages")
    entete(ws, 1, ["Institution", "Date (UTC)", "Hôte", "Code", "Nature", "Suite donnée"], [34, 22, 34, 12, 50, 50])
    lignes = [[d.get("nom", d["slug"]), b.get("date"), b.get("hote"), b.get("code"), b.get("nature"), b.get("suite")]
              for d in D for b in d.get("blocages", [])]
    ecrire(ws, 2, lignes or [["(aucun)"] + [""] * 5])


def feuille_manuel(wb, D):
    """Onglet de travail de Marcel : URL que la sonde n'a pas pu lire (403, CAPTCHA, délai…)."""
    ws = wb.create_sheet("À vérifier à la main")
    entete(ws, 1, ["Institution", "GLAM", "URL à ouvrir", "Pourquoi je n'ai pas pu la vérifier", "Ce qu'il faut chercher", "Résultat (Marcel)", "Fait ?"],
           [30, 11, 60, 40, 55, 40, 8])
    lignes, liens = [], []
    for d in D:
        for m in d.get("a_verifier_manuellement", []):
            lignes.append([d.get("nom", d["slug"]), d.get("classeur_id"), m.get("url"), m.get("pourquoi"), m.get("a_chercher"), "", ""])
    ecrire(ws, 2, lignes or [["(aucune)"] + [""] * 6])
    for n, l in enumerate(lignes, start=2):
        if l[2] and str(l[2]).startswith("http"):
            c = ws.cell(row=n, column=3); c.hyperlink = l[2]; c.font = Font(color="0563C1", underline="single")
    ws.auto_filter.ref = f"A1:G{max(len(lignes), 1) + 1}"


def feuille_couverture(wb, D):
    """Contrôle automatique des critères mesurables (exigence v3) pour chaque institution."""
    ws = wb.create_sheet("Couverture")
    entete(ws, 1, ["Institution", "GLAM", "Étapes a–f cochées", "Exigence v3", "Manques (à compléter)"], [34, 11, 18, 18, 110])
    anc = suivi.anciennes()
    lignes = []
    for d in D:
        etapes = (suivi.lire_suivi(d["slug"]) or ("", {}))[1]
        cochees = sum(1 for c in "abcdef" if etapes.get(c, (" ",))[0] == "x")
        if cochees < 6:
            continue
        manques = suivi.controle_v3(d["slug"], d)
        lignes.append([d.get("nom", d["slug"]), d.get("classeur_id"), f"{cochees}/6",
                       "conforme" if not manques else ("à compléter (ancienne)" if d["slug"] in anc else "NON CONFORME"),
                       "\n".join(manques)])
    ecrire(ws, 2, lignes or [["(aucune)"] + [""] * 4])


def feuille_doc_exclue(wb, D):
    """Pages de doc exclues du contrôle de couverture (HTML téléchargé, code 200) : à contrôler par Marcel."""
    ws = wb.create_sheet("Doc exclue")
    entete(ws, 1, ["Institution", "GLAM", "URL exclue", "Fichier téléchargé (preuve : HTML, code 200)"], [34, 11, 80, 70])
    lignes = []
    for d in D:
        for (h, seg), (u, f) in sorted(suivi.docs_html_lues(d["slug"]).items()):
            if suivi.MOTIF_API.search(urlsplit(u).path or "/"):
                lignes.append([d.get("nom", d["slug"]), d.get("classeur_id"), u, f])
    ecrire(ws, 2, lignes or [["(aucune)", "", "", ""]])


def feuille_sources(wb, D):
    ws = wb.create_sheet("Sources")
    entete(ws, 1, ["Institution", "URL", "Date de lecture", "Étiquette", "Preuve (fichier)", "Preuve présente ?"],
           [34, 70, 14, 30, 50, 14])
    lignes = []
    for d in D:
        for s in d.get("sources", []):
            p = (s.get("preuve") or "").split(" ")[0]
            lignes.append([d.get("nom", d["slug"]), s.get("url"), s.get("date"), s.get("etiquette"),
                           s.get("preuve"), "OUI" if p and (REPO / p).exists() else "NON"])
    ecrire(ws, 2, lignes or [["(aucune)"] + [""] * 5])


def feuille_web(wb, D):
    ws = wb.create_sheet("Web (étape f)")
    entete(ws, 1, ["Institution", "URL", "Date", "Étiquette", "Citation (texte exact ou résumé signalé)", "Preuve"],
           [34, 66, 16, 30, 80, 44])
    lignes = [[d.get("nom", d["slug"]), w.get("url"), w.get("date"), w.get("etiquette"), w.get("citation"), w.get("preuve")]
              for d in D for w in d.get("web", [])]
    ecrire(ws, 2, lignes or [["(aucune)"] + [""] * 5])


def feuille_preuves(wb, D):
    ws = wb.create_sheet("Preuves")
    entete(ws, 1, ["Institution", "Étape", "Chemin de la preuve", "Existe sur le disque ?"], [34, 10, 90, 18])
    lignes = [[d.get("nom", d["slug"]), c, p, "OUI" if e else "NON"] for d in D for c, p, e in d["preuves"]]
    ecrire(ws, 2, lignes or [["(aucune preuve citée)", "", "", ""]])


def feuille_journal(wb, D, commit):
    ws = wb.create_sheet("Journal")
    entete(ws, 1, ["Élément", "Valeur"], [46, 100])
    manquantes = sum(1 for d in D for _, _, e in d["preuves"] if not e)
    anomalies = sum(len(suivi.analyser_journal(d["slug"])["anomalies"]) for d in D)
    lignes = [
        ("Généré le (UTC)", datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")),
        ("Commit du dépôt au moment de la génération", commit),
        ("Sources", "institutions/<slug>/data.json et institutions/<slug>/CONSIGNE-ET-SUIVI.md"),
        ("Générateur", "scripts/build_benchmark.py (appelé par .githooks/pre-commit)"),
        ("Consigne", "CONSIGNE.md (recopiée dans chaque dossier) ; méthode : METHODOLOGY.md"),
        ("Preuves citées manquantes sur le disque", str(manquantes)),
        ("Anomalies de prudence dans les journaux (pause < 6 s, session > 15, méthode interdite)", str(anomalies)),
        ("Règle de comptage des limites", "Officielle + chiffre + institution active + étape d cochée + données non marquées « à revalider »."),
    ]
    ecrire(ws, 2, lignes)


def main():
    D = charger()
    commit = sha()
    wb = Workbook()
    tableau_de_bord(wb, D, commit)
    feuille_institutions(wb, D)
    feuille_limites(wb, D)
    feuille_entetes(wb, D)
    feuille_blocages(wb, D)
    feuille_manuel(wb, D)
    feuille_couverture(wb, D)
    feuille_doc_exclue(wb, D)
    feuille_sources(wb, D)
    feuille_web(wb, D)
    feuille_preuves(wb, D)
    feuille_journal(wb, D, commit)
    wb.save(OUT)
    manq = sum(1 for d in D for _, _, e in d["preuves"] if not e)
    print(f"écrit : {OUT} ({len(D)} institutions, commit {commit}, preuves manquantes : {manq})")


if __name__ == "__main__":
    try:
        main()
    except ImportError:
        sys.exit("openpyxl manquant : /Users/marcel/.venvs/veille/bin/python scripts/build_benchmark.py")
