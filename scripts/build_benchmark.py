#!/usr/bin/env python3
"""Génère BENCHMARK.xlsx à partir de data/institutions.json.

Règles :
- Aucune valeur n'est saisie dans le classeur : tout vient de data/institutions.json.
- Chaque preuve citée (fichier du dépôt) est VÉRIFIÉE sur le disque : OUI / NON.
- Une limite n'est comptée comme « documentée chiffrée » que si sa vérification est
  « officielle » ; les extraits tiers ou non vérifiés sont listés à part.

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
ETAPES_AUDIT = ETAPES[:6]  # a à f comptées ; g après l'audit complet

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
    if t.startswith("non applicable") or t.startswith("non (abandonnée)"):
        return GRIS
    return ROUGE


def est_officielle_verifiee(lim):
    v = str(lim.get("verification", "")).lower()
    return v.startswith("officielle")


def a_un_chiffre(lim):
    return any(ch.isdigit() for ch in str(lim.get("valeur", "")))


def score(inst):
    cl = inst.get("checklist", {})
    return sum(1 for k, _ in ETAPES_AUDIT if str(cl.get(k, "")).lower().startswith("fait"))


def preuves_verifiees(inst):
    """Retourne (ok, total, détail) en vérifiant chaque chemin sur le disque."""
    detail = []
    for etape, chemins in (inst.get("preuves") or {}).items():
        for c in chemins:
            existe = (REPO / c).exists()
            detail.append((etape, c, existe))
    ok = sum(1 for _, _, e in detail if e)
    return ok, len(detail), detail


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


def ecrire_lignes(ws, debut, lignes):
    for n, vals in enumerate(lignes, start=debut):
        for c, v in enumerate(vals, start=1):
            ws.cell(row=n, column=c, value=v).alignment = Alignment(wrap_text=True, vertical="top")
    return debut + len(lignes)


def version_depot():
    try:
        return subprocess.run(["git", "-C", str(REPO), "rev-parse", "--short", "HEAD"],
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:  # noqa: BLE001
        return "inconnu"


def feuille_tableau_de_bord(wb, donnees, sha):
    ws = wb.active
    ws.title = "Tableau de bord"
    ws["A1"] = "BENCHMARK IIIF — quotas et politiques d'accès des API (généré)"
    ws["A1"].font = TITRE
    ws["A2"] = (f"Généré le {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC · commit {sha} · "
                f"{len(donnees)} lignes (dont abandons)")
    ws["A3"] = ("« non trouvé » = absent des pages lues, pas une preuve d'absence de limite. "
                "Les chiffres non officiels sont listés à part.")

    actives = [d for d in donnees if "abandon" not in d.get("statut_audit", "").lower()]
    audit_complet = sum(1 for d in actives if score(d) == len(ETAPES_AUDIT))
    chiffrees = sum(1 for d in actives for l in d.get("limites_documentees", [])
                    if est_officielle_verifiee(l) and a_un_chiffre(l))
    non_verifiees = sum(1 for d in actives for l in d.get("limites_documentees", [])
                        if not est_officielle_verifiee(l))
    observes = sum(len(d.get("en_tetes_observes", [])) for d in actives)
    bloques = sum(1 for d in actives for b in d.get("blocages", []) if b.get("code") == "403")
    preuves_ok = sum(preuves_verifiees(d)[0] for d in donnees)
    preuves_tot = sum(preuves_verifiees(d)[1] for d in donnees)

    ws["A5"] = "INDICATEURS"
    ws["A5"].font = Font(bold=True, size=12)
    kpi = [
        ("Institutions actives", len(actives)),
        ("Abandons (hors périmètre)", len(donnees) - len(actives)),
        ("Audit complet (étapes a à f)", audit_complet),
        ("Limites officielles chiffrées", chiffrees),
        ("Limites non officielles ou non vérifiées", non_verifiees),
        ("En-têtes de quota observés", observes),
        ("Blocages 403 anti-bot consignés", bloques),
        ("Preuves présentes sur le disque", f"{preuves_ok} / {preuves_tot}"),
    ]
    for n, (k, v) in enumerate(kpi, start=6):
        ws.cell(row=n, column=1, value=k)
        ws.cell(row=n, column=2, value=v).font = Font(bold=True)

    ligne0 = 16
    ws.cell(row=ligne0 - 1, column=1, value="AVANCEMENT DE L'AUDIT (étapes a à f)").font = Font(bold=True, size=12)
    entete(ws, ligne0, ["Institution", "Étapes faites (sur 6)"], [46, 22])
    for n, inst in enumerate(donnees, start=ligne0 + 1):
        ws.cell(row=n, column=1, value=inst["nom"])
        ws.cell(row=n, column=2, value=score(inst))
    fin = ligne0 + len(donnees)
    g1 = BarChart()
    g1.type = "bar"
    g1.title = "Étapes d'audit faites (sur 6)"
    g1.y_axis.scaling.min = 0
    g1.y_axis.scaling.max = 6
    g1.add_data(Reference(ws, min_col=2, min_row=ligne0, max_row=fin), titles_from_data=True)
    g1.set_categories(Reference(ws, min_col=1, min_row=ligne0 + 1, max_row=fin))
    g1.height, g1.width = 13, 20
    ws.add_chart(g1, "D5")

    # Limites officielles chiffrées par institution
    l2 = fin + 3
    ws.cell(row=l2 - 1, column=1, value="LIMITES OFFICIELLES CHIFFRÉES (par institution)").font = Font(bold=True, size=12)
    entete(ws, l2, ["Institution", "Nombre de limites officielles chiffrées"])
    for n, inst in enumerate(donnees, start=l2 + 1):
        nb = sum(1 for l in inst.get("limites_documentees", []) if est_officielle_verifiee(l) and a_un_chiffre(l))
        ws.cell(row=n, column=1, value=inst["nom"])
        ws.cell(row=n, column=2, value=nb)
    fin2 = l2 + len(donnees)
    g2 = BarChart()
    g2.type = "bar"
    g2.title = "Limites officielles chiffrées, par institution"
    g2.add_data(Reference(ws, min_col=2, min_row=l2, max_row=fin2), titles_from_data=True)
    g2.set_categories(Reference(ws, min_col=1, min_row=l2 + 1, max_row=fin2))
    g2.height, g2.width = 13, 20
    ws.add_chart(g2, "D33")

    # Classes de quota
    l3 = fin2 + 3
    classes = Counter(d.get("classe_quota", "non renseigné") for d in donnees)
    ws.cell(row=l3 - 1, column=1, value="CLASSES DE QUOTA").font = Font(bold=True, size=12)
    entete(ws, l3, ["Classe", "Nombre d'institutions"])
    for n, (cl, nb) in enumerate(sorted(classes.items()), start=l3 + 1):
        ws.cell(row=n, column=1, value=cl)
        ws.cell(row=n, column=2, value=nb)
    fin3 = l3 + len(classes)
    pie = PieChart()
    pie.title = "Classes de quota"
    pie.add_data(Reference(ws, min_col=2, min_row=l3, max_row=fin3), titles_from_data=True)
    pie.set_categories(Reference(ws, min_col=1, min_row=l3 + 1, max_row=fin3))
    pie.dataLabels = DataLabelList()
    pie.dataLabels.showPercent = True
    pie.height, pie.width = 10, 16
    ws.add_chart(pie, "D56")
    ws.column_dimensions["A"].width = 46


def feuille_institutions(wb, donnees):
    ws = wb.create_sheet("Institutions")
    cols = (["Institution", "Pays", "Statut d'audit"] + [e[1] for e in ETAPES] +
            ["Preuves présentes", "Classe de quota", "Conclusion (quota)", "Confiance", "Contact", "Notes"])
    entete(ws, 1, cols, [34, 14, 28] + [24] * 7 + [14, 26, 60, 12, 30, 60])
    for n, inst in enumerate(donnees, start=2):
        cl = inst.get("checklist", {})
        ok, tot, _ = preuves_verifiees(inst)
        vals = [inst["nom"], inst.get("pays", ""), inst.get("statut_audit", "")]
        vals += [cl.get(k, "non renseigné") for k, _ in ETAPES]
        vals += [f"{ok} / {tot}", inst.get("classe_quota", ""), inst.get("conclusion_quota", ""),
                 inst.get("confiance", ""), inst.get("contact", ""), inst.get("notes", "")]
        for c, v in enumerate(vals, start=1):
            ws.cell(row=n, column=c, value=v).alignment = Alignment(wrap_text=True, vertical="top")
        for c, (k, _) in enumerate(ETAPES, start=4):
            ws.cell(row=n, column=c).fill = couleur_etape(cl.get(k, ""))


def feuille_limites(wb, donnees):
    ws = wb.create_sheet("Limites")
    cols = ["Institution", "Nature", "Périmètre", "Valeur", "Fenêtre", "Effet au dépassement",
            "Vérification", "Compté comme officiel chiffré ?", "Source (URL)", "Date de lecture"]
    entete(ws, 1, cols, [30, 24, 30, 24, 14, 24, 34, 16, 66, 14])
    lignes = []
    for inst in donnees:
        for lim in inst.get("limites_documentees", []):
            compte = "oui" if (est_officielle_verifiee(lim) and a_un_chiffre(lim)) else "non"
            lignes.append([inst["nom"], lim.get("nature"), lim.get("perimetre"), lim.get("valeur"),
                           lim.get("fenetre"), lim.get("effet"), lim.get("verification", "non renseignée"),
                           compte, lim.get("source"), lim.get("date")])
    ecrire_lignes(ws, 2, lignes)


def feuille_entetes(wb, donnees):
    ws = wb.create_sheet("En-têtes observés")
    cols = ["Institution", "En-tête", "Valeur observée", "Endpoint", "Date", "Preuve (fichier du dépôt)", "Existe ?"]
    entete(ws, 1, cols, [30, 24, 40, 40, 14, 50, 10])
    lignes = []
    for inst in donnees:
        for h in inst.get("en_tetes_observes", []):
            p = h.get("preuve", "")
            first = p.split(",")[0].split(" ")[0] if p else ""
            existe = "OUI" if first and (REPO / first).exists() else "NON"
            lignes.append([inst["nom"], h.get("nom"), h.get("valeur"), h.get("endpoint"), h.get("date"), p, existe])
    if not lignes:
        lignes = [["(aucun)", "", "Aucun en-tête de quota observé dans les institutions auditées.", "", "", "", ""]]
    ecrire_lignes(ws, 2, lignes)


def feuille_blocages(wb, donnees):
    ws = wb.create_sheet("Blocages")
    cols = ["Institution", "Date (UTC)", "Hôte", "Code", "Nature", "Suite donnée"]
    entete(ws, 1, cols, [30, 22, 34, 12, 50, 50])
    lignes = []
    for inst in donnees:
        for b in inst.get("blocages", []):
            lignes.append([inst["nom"], b.get("date"), b.get("hote"), b.get("code"), b.get("nature"), b.get("suite")])
    if not lignes:
        lignes = [["(aucun)", "", "", "", "", ""]]
    ecrire_lignes(ws, 2, lignes)


def feuille_sources(wb, donnees):
    ws = wb.create_sheet("Sources")
    cols = ["Institution", "URL", "Date de lecture", "Étiquette", "Statut", "Preuve (fichier)", "Preuve présente ?"]
    entete(ws, 1, cols, [30, 70, 14, 30, 36, 46, 14])
    lignes = []
    for inst in donnees:
        for s in inst.get("sources", []):
            p = s.get("preuve", "")
            fichier = p.split(" ")[0] if p else ""
            present = "OUI" if fichier and (REPO / fichier).exists() else "NON"
            lignes.append([inst["nom"], s.get("url"), s.get("date"), s.get("etiquette"),
                           s.get("statut", ""), p, present])
    if not lignes:
        lignes = [["(aucune source enregistrée)", "", "", "", "", "", ""]]
    ecrire_lignes(ws, 2, lignes)


def feuille_web(wb, donnees):
    ws = wb.create_sheet("Web (étape f)")
    cols = ["Institution", "URL", "Date", "Étiquette", "Citation (texte exact ou résumé signalé)", "Preuve (fichier)"]
    entete(ws, 1, cols, [30, 66, 16, 26, 80, 40])
    lignes = []
    for inst in donnees:
        for w in inst.get("web", []):
            lignes.append([inst["nom"], w.get("url"), w.get("date"), w.get("etiquette"),
                           w.get("citation"), w.get("preuve")])
    if not lignes:
        lignes = [["(à compléter)", "", "", "", "Recherche web non encore faite pour les institutions de ce tableau.", ""]]
    ecrire_lignes(ws, 2, lignes)


def feuille_preuves(wb, donnees):
    ws = wb.create_sheet("Preuves")
    cols = ["Institution", "Étape", "Chemin de la preuve", "Existe sur le disque ?"]
    entete(ws, 1, cols, [30, 34, 70, 18])
    lignes = []
    for inst in donnees:
        for etape, chemin, existe in preuves_verifiees(inst)[2]:
            lignes.append([inst["nom"], etape, chemin, "OUI" if existe else "NON"])
    ecrire_lignes(ws, 2, lignes)


def feuille_journal(wb, donnees, sha):
    ws = wb.create_sheet("Journal")
    entete(ws, 1, ["Élément", "Valeur"], [40, 90])
    manquantes = sum(1 for d in donnees for _, _, e in preuves_verifiees(d)[2] if not e)
    lignes = [
        ("Généré le (UTC)", datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")),
        ("Commit du dépôt au moment de la génération", sha),
        ("Source de données", "data/institutions.json"),
        ("Générateur", "scripts/build_benchmark.py"),
        ("Méthode", "METHODOLOGY.md, « Méthode v2 » (étapes a à g)"),
        ("Preuves manquantes sur le disque", str(manquantes)),
        ("Règle de comptage", "Une limite est « officielle chiffrée » seulement si sa vérification commence par « officielle » et qu'elle a un chiffre."),
        ("Règle de contenu", "Une valeur absente de la doc n'est jamais déduite d'une autre source."),
    ]
    ecrire_lignes(ws, 2, lignes)


def main():
    donnees = json.loads(DATA.read_text(encoding="utf-8"))
    sha = version_depot()
    wb = Workbook()
    feuille_tableau_de_bord(wb, donnees, sha)
    feuille_institutions(wb, donnees)
    feuille_limites(wb, donnees)
    feuille_entetes(wb, donnees)
    feuille_blocages(wb, donnees)
    feuille_sources(wb, donnees)
    feuille_web(wb, donnees)
    feuille_preuves(wb, donnees)
    feuille_journal(wb, donnees, sha)
    wb.save(OUT)
    manquantes = sum(1 for d in donnees for _, _, e in preuves_verifiees(d)[2] if not e)
    print(f"écrit : {OUT} ({len(donnees)} lignes, commit {sha}, preuves manquantes : {manquantes})")


if __name__ == "__main__":
    try:
        main()
    except ImportError:
        sys.exit("openpyxl manquant : /Users/marcel/.venvs/veille/bin/python scripts/build_benchmark.py")
