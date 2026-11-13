#!/usr/bin/env python3
"""Génère BENCHMARK.xlsx à partir de data/institutions.json.

Aucune valeur n'est saisie dans le classeur : tout vient de data/institutions.json,
lui-même alimenté par les fiches, les journaux et les sources du dépôt.

Usage : python3 scripts/build_benchmark.py   (nécessite openpyxl)
Sortie : BENCHMARK.xlsx à la racine du dépôt.
"""
import json
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from openpyxl import Workbook
from openpyxl.chart import BarChart, PieChart, Reference
from openpyxl.chart.label import DataLabelList
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

REPO = Path(__file__).resolve().parent.parent
DATA = REPO / "data" / "institutions.json"
OUT = REPO / "BENCHMARK.xlsx"

ETAPES = [
    ("a_doc_lue", "a) Doc lue en entier"),
    ("b_endpoints_doc", "b) Endpoints tirés de la doc"),
    ("c_config_avant_tests", "c) Configuration avant tests"),
    ("d_quota_dans_doc", "d) Quota dans la doc"),
    ("e_tests_endpoints", "e) Test des endpoints"),
    ("f_web", "f) Ce que disent les gens (web)"),
    ("g_crash_test", "g) Crash test"),
]
ETAPES_AUDIT = ETAPES[:6]  # a à f : comptées dans le score ; g après l'audit

VERT = PatternFill("solid", fgColor="C6EFCE")
ORANGE = PatternFill("solid", fgColor="FFEB9C")
ROUGE = PatternFill("solid", fgColor="FFC7CE")
GRIS = PatternFill("solid", fgColor="EDEDED")
ENTETE = PatternFill("solid", fgColor="1F3A5F")
TITRE = Font(bold=True, size=14, color="1F3A5F")
BLANC_GRAS = Font(bold=True, color="FFFFFF")


def couleur_etape(texte):
    t = (texte or "").lower()
    if t.startswith("fait"):
        return VERT
    if t.startswith(("partiel", "bloqué", "incomplet")):
        return ORANGE
    if t.startswith(("non applicable",)):
        return GRIS
    return ROUGE  # à faire, non fait, non


def score(inst):
    cl = inst.get("checklist", {})
    return sum(1 for k, _ in ETAPES_AUDIT if str(cl.get(k, "")).lower().startswith("fait"))


def entete(ws, ligne, valeurs, largeurs=None):
    for i, v in enumerate(valeurs, start=1):
        c = ws.cell(row=ligne, column=i, value=v)
        c.fill = ENTETE
        c.font = BLANC_GRAS
        c.alignment = Alignment(wrap_text=True, vertical="center")
    if largeurs:
        for i, w in enumerate(largeurs, start=1):
            ws.column_dimensions[get_column_letter(i)].width = w
    ws.freeze_panes = ws.cell(row=ligne + 1, column=1)


def version_depot():
    try:
        sha = subprocess.run(["git", "-C", str(REPO), "rev-parse", "--short", "HEAD"],
                             capture_output=True, text=True, check=True).stdout.strip()
        return sha
    except Exception:  # noqa: BLE001
        return "inconnu"


def feuille_tableau_de_bord(wb, donnees, sha):
    ws = wb.active
    ws.title = "Tableau de bord"
    ws["A1"] = "BENCHMARK IIIF — quotas et politiques d'accès des API (généré)"
    ws["A1"].font = TITRE
    ws["A2"] = (f"Généré le {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC · commit {sha} · "
                f"{len(donnees)} institutions suivies")
    ws["A3"] = ("Lecture : « non trouvé » signifie « pas dans les pages lues » — "
                "ce n'est pas une preuve d'absence de limite.")

    classes = Counter(i.get("classe_quota", "non renseigné") for i in donnees)
    audit_complet = sum(1 for i in donnees if score(i) == len(ETAPES_AUDIT))
    limites_chiffrees = sum(1 for i in donnees for l in i.get("limites_documentees", [])
                            if any(ch.isdigit() for ch in str(l.get("valeur", ""))))
    observes = sum(len(i.get("en_tetes_observes", [])) for i in donnees)
    bloques = sum(1 for i in donnees for b in i.get("blocages", []) if b.get("code") == "403")

    ws["A5"] = "INDICATEURS"
    ws["A5"].font = Font(bold=True, size=12)
    kpi = [
        ("Institutions suivies", len(donnees)),
        ("Audit complet (étapes a à f)", audit_complet),
        ("Limites documentées chiffrées", limites_chiffrees),
        ("En-têtes de quota observés (lignes)", observes),
        ("Blocages 403 anti-bot consignés", bloques),
    ]
    for n, (k, v) in enumerate(kpi, start=6):
        ws.cell(row=n, column=1, value=k)
        ws.cell(row=n, column=2, value=v).font = Font(bold=True)

    # Tableau score par institution (pour le graphique)
    ligne0 = 13
    ws.cell(row=ligne0 - 1, column=1, value="AVANCEMENT DE L'AUDIT (étapes a à f)").font = Font(bold=True, size=12)
    entete(ws, ligne0, ["Institution", "Étapes faites (sur 6)"], [46, 22])
    for n, inst in enumerate(donnees, start=ligne0 + 1):
        ws.cell(row=n, column=1, value=inst["nom"])
        ws.cell(row=n, column=2, value=score(inst))
    fin = ligne0 + len(donnees)

    graph = BarChart()
    graph.type = "bar"
    graph.style = 10
    graph.title = "Étapes d'audit faites (sur 6), par institution"
    graph.y_axis.title = "Étapes faites"
    graph.y_axis.scaling.min = 0
    graph.y_axis.scaling.max = 6
    donnees_ref = Reference(ws, min_col=2, min_row=ligne0, max_row=fin)
    cats = Reference(ws, min_col=1, min_row=ligne0 + 1, max_row=fin)
    graph.add_data(donnees_ref, titles_from_data=True)
    graph.set_categories(cats)
    graph.height, graph.width = 12, 20
    ws.add_chart(graph, "D5")

    # Répartition des classes de quota
    l1 = fin + 3
    ws.cell(row=l1 - 1, column=1, value="CLASSES DE QUOTA (par institution)").font = Font(bold=True, size=12)
    entete(ws, l1, ["Classe", "Nombre d'institutions"], None)
    for n, (cl, nb) in enumerate(sorted(classes.items()), start=l1 + 1):
        ws.cell(row=n, column=1, value=cl)
        ws.cell(row=n, column=2, value=nb)
    fin2 = l1 + len(classes)
    pie = PieChart()
    pie.title = "Classes de quota (institutions)"
    pie.add_data(Reference(ws, min_col=2, min_row=l1, max_row=fin2), titles_from_data=True)
    pie.set_categories(Reference(ws, min_col=1, min_row=l1 + 1, max_row=fin2))
    pie.dataLabels = DataLabelList()
    pie.dataLabels.showPercent = True
    pie.height, pie.width = 10, 16
    ws.add_chart(pie, "D31")
    ws.column_dimensions["A"].width = 46


def feuille_institutions(wb, donnees):
    ws = wb.create_sheet("Institutions")
    cols = ["Institution", "Pays", "Statut d'audit"] + [e[1] for e in ETAPES] + \
           ["Classe de quota", "Conclusion (quota)", "Confiance", "Contact", "Notes"]
    entete(ws, 1, cols, [34, 14, 26] + [22] * 7 + [28, 60, 12, 30, 60])
    for n, inst in enumerate(donnees, start=2):
        cl = inst.get("checklist", {})
        vals = [inst["nom"], inst.get("pays", ""), inst.get("statut_audit", "")]
        vals += [cl.get(k, "non renseigné") for k, _ in ETAPES]
        vals += [inst.get("classe_quota", ""), inst.get("conclusion_quota", ""),
                 inst.get("confiance", ""), inst.get("contact", ""), inst.get("notes", "")]
        for c, v in enumerate(vals, start=1):
            cell = ws.cell(row=n, column=c, value=v)
            cell.alignment = Alignment(wrap_text=True, vertical="top")
        for c, (k, _) in enumerate(ETAPES, start=4):
            ws.cell(row=n, column=c).fill = couleur_etape(cl.get(k, ""))


def feuille_limites(wb, donnees):
    ws = wb.create_sheet("Limites documentées")
    cols = ["Institution", "Nature", "Périmètre", "Valeur", "Fenêtre", "Effet au dépassement", "Source (URL)", "Date de lecture"]
    entete(ws, 1, cols, [30, 26, 34, 26, 14, 26, 70, 14])
    n = 2
    for inst in donnees:
        for lim in inst.get("limites_documentees", []):
            vals = [inst["nom"], lim.get("nature"), lim.get("perimetre"), lim.get("valeur"),
                    lim.get("fenetre"), lim.get("effet"), lim.get("source"), lim.get("date")]
            for c, v in enumerate(vals, start=1):
                ws.cell(row=n, column=c, value=v).alignment = Alignment(wrap_text=True, vertical="top")
            n += 1


def feuille_entetes(wb, donnees):
    ws = wb.create_sheet("En-têtes observés")
    cols = ["Institution", "En-tête", "Valeur observée", "Endpoint", "Date", "Preuve (fichier du dépôt)"]
    entete(ws, 1, cols, [30, 24, 40, 40, 14, 50])
    n = 2
    for inst in donnees:
        for h in inst.get("en_tetes_observes", []):
            vals = [inst["nom"], h.get("nom"), h.get("valeur"), h.get("endpoint"), h.get("date"), h.get("preuve")]
            for c, v in enumerate(vals, start=1):
                ws.cell(row=n, column=c, value=v).alignment = Alignment(wrap_text=True, vertical="top")
            n += 1
    if n == 2:
        ws.cell(row=2, column=1, value="Aucun en-tête de quota observé, hors institutions listées dans les lignes ci-dessus.")


def feuille_blocages(wb, donnees):
    ws = wb.create_sheet("Blocages")
    cols = ["Institution", "Date (UTC)", "Hôte", "Code", "Nature", "Suite donnée"]
    entete(ws, 1, cols, [30, 22, 34, 12, 50, 50])
    n = 2
    for inst in donnees:
        for b in inst.get("blocages", []):
            vals = [inst["nom"], b.get("date"), b.get("hote"), b.get("code"), b.get("nature"), b.get("suite")]
            for c, v in enumerate(vals, start=1):
                ws.cell(row=n, column=c, value=v).alignment = Alignment(wrap_text=True, vertical="top")
            n += 1


def feuille_journal(wb, donnees, sha):
    ws = wb.create_sheet("Journal")
    entete(ws, 1, ["Élément", "Valeur"], [40, 80])
    lignes = [
        ("Généré le (UTC)", datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")),
        ("Commit du dépôt", sha),
        ("Source de données", "data/institutions.json"),
        ("Générateur", "scripts/build_benchmark.py"),
        ("Méthode", "METHODOLOGY.md, « Méthode v2 » (étapes a à g)"),
        ("Institutions", str(len(donnees))),
        ("Règle", "Une valeur absente de la doc n'est jamais déduite d'une autre source."),
    ]
    for n, (k, v) in enumerate(lignes, start=2):
        ws.cell(row=n, column=1, value=k)
        ws.cell(row=n, column=2, value=v).alignment = Alignment(wrap_text=True)


def main():
    donnees = json.loads(DATA.read_text(encoding="utf-8"))
    sha = version_depot()
    wb = Workbook()
    feuille_tableau_de_bord(wb, donnees, sha)
    feuille_institutions(wb, donnees)
    feuille_limites(wb, donnees)
    feuille_entetes(wb, donnees)
    feuille_blocages(wb, donnees)
    feuille_journal(wb, donnees, sha)
    wb.save(OUT)
    print(f"écrit : {OUT} ({len(donnees)} institutions, commit {sha})")


if __name__ == "__main__":
    try:
        main()
    except ImportError:
        sys.exit("openpyxl manquant : /Users/marcel/.venvs/veille/bin/python scripts/build_benchmark.py")
