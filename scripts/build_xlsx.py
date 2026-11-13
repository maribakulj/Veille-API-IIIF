"""Régénère docs/veille_iiif.xlsx et docs/veille_iiif.csv à partir des fiches et des données de veille.

Les fichiers de docs/ sont des sorties : ne pas les modifier à la main.
"""
import csv
import datetime
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fiches import CLASSES, charger  # noqa: E402
from openpyxl import Workbook  # noqa: E402
from openpyxl.styles import Alignment, Font, PatternFill  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENTETE = PatternFill('solid', fgColor='1F3A5F')
POLICE_ENTETE = Font(bold=True, color='FFFFFF')
RENVOI = Alignment(wrap_text=True, vertical='top')

COLONNES = [
    ('ID', 'id', 12), ('Institution', 'institution', 34), ('Pays', 'pays', 14),
    ('Classe', 'classe', 24), ('Verdict', 'statut', 40), ('Débit IIIF', 'debit_iiif', 50),
    ('Statut quota', 'statut_quota', 40), ('Image API', 'iiif_image', 44),
    ('Presentation API', 'iiif_presentation', 44), ('Accès', 'acces', 40),
    ('Moissonnage', 'moissonnage', 40), ('Vérifié le', 'verifie_le', 12),
    ('Nb sources', '_nb', 10), ('Sources surveillées', '_surv', 12),
    ('Conflits', '_conf', 40), ('Lacunes', 'lacunes', 40),
]


def texte(v):
    if v is None:
        return ''
    if isinstance(v, list):
        return ' ; '.join(str(x) for x in v)
    return str(v)


def ligne_institution(fm):
    out = []
    for _, cle, _ in COLONNES:
        if cle == '_nb':
            out.append(len(fm.get('sources') or []))
        elif cle == '_surv':
            out.append(sum(1 for s in fm.get('sources') or [] if s.get('surveiller')))
        elif cle == '_conf':
            out.append(texte(fm.get('conflits')))
        else:
            out.append(texte(fm.get(cle)))
    return out


def entete(ws, valeurs):
    ws.append(valeurs)
    for c in ws[ws.max_row]:
        c.fill = ENTETE
        c.font = POLICE_ENTETE
        c.alignment = Alignment(wrap_text=True, vertical='center')


def main():
    donnees = os.path.join(ROOT, 'data')
    fiches = [fm for _, fm in charger(os.path.join(ROOT, 'institutions'))]
    etat = json.load(open(os.path.join(donnees, 'state.json'), encoding='utf-8')) \
        if os.path.exists(os.path.join(donnees, 'state.json')) else {}
    hist = []
    chemin_hist = os.path.join(donnees, 'historique.jsonl')
    if os.path.exists(chemin_hist):
        with open(chemin_hist, encoding='utf-8') as fh:
            hist = [json.loads(l) for l in fh if l.strip()]

    wb = Workbook()
    n = len(fiches)
    fin_inst = n + 1

    # --- Institutions ---
    wi = wb.active
    wi.title = 'Institutions'
    entete(wi, [c[0] for c in COLONNES])
    for fm in fiches:
        wi.append(ligne_institution(fm))
    for col, (_, _, largeur) in enumerate(COLONNES, 1):
        wi.column_dimensions[wi.cell(1, col).column_letter].width = largeur
    for row in wi.iter_rows(min_row=2):
        for c in row:
            c.alignment = RENVOI
    wi.freeze_panes = 'C2'
    wi.auto_filter.ref = f'A1:{wi.cell(1, len(COLONNES)).column_letter}{fin_inst}'

    # --- Sources ---
    ws = wb.create_sheet('Sources')
    entete(ws, ['ID', 'Institution', 'URL', 'Note', 'Surveillée', 'Dernier statut',
                'Dernière vérification', 'Empreinte (début)', 'Dernier changement'])
    nb_src = 0
    for fm in fiches:
        for s in fm.get('sources') or []:
            nb_src += 1
            url = str(s.get('url', ''))
            e = etat.get(url, {})
            ws.append([fm['id'], fm.get('institution', ''), url, s.get('note', ''),
                       'oui' if s.get('surveiller') else 'non', e.get('statut', 'non vérifiée'),
                       e.get('verifie_le', ''), (e.get('empreinte') or '')[:12], e.get('modifie_le', '')])
            cell = ws.cell(ws.max_row, 3)
            if url.startswith(('http://', 'https://')):
                cell.hyperlink = url
                cell.font = Font(color='1F4E9A', underline='single')
    for col, largeur in zip('ABCDEFGHI', [12, 34, 60, 40, 12, 18, 22, 18, 22]):
        ws.column_dimensions[col].width = largeur
    ws.freeze_panes = 'A2'
    ws.auto_filter.ref = f'A1:I{max(2, nb_src + 1)}'

    # --- Changements ---
    wc = wb.create_sheet('Changements')
    entete(wc, ['Date', 'ID', 'Institution', 'URL', 'Empreinte précédente', 'Nouvelle empreinte'])
    for ch in hist:
        wc.append([ch.get('date', ''), ch.get('id', ''), ch.get('institution', ''), ch.get('url', ''),
                   (ch.get('precedente') or '')[:12], (ch.get('nouvelle') or '')[:12]])
    for col, largeur in zip('ABCDEF', [22, 12, 34, 60, 22, 22]):
        wc.column_dimensions[col].width = largeur
    fin_chg = max(2, len(hist) + 1)

    # --- Synthèse (formules : se recalculent quand Excel ouvre le fichier) ---
    wsyn = wb.create_sheet('Synthèse', 0)
    wsyn['A1'] = 'Veille API IIIF : synthèse'
    wsyn['A1'].font = Font(bold=True, size=14)
    wsyn['A2'] = ('Fichier généré par scripts/build_xlsx.py à partir des fiches institutions/. '
                  'Ne pas le modifier à la main ; modifier les fiches puis relancer le script.')
    wsyn['A2'].alignment = RENVOI
    wsyn['A3'] = f'Généré le {datetime.date.today().isoformat()}'
    wsyn.append([])
    entete(wsyn, ['Indicateur', 'Valeur'])
    wsyn.append(['Fiches institutions', f'=COUNTA(Institutions!A2:A{fin_inst})'])
    for classe in CLASSES:
        wsyn.append([f'Classe : {classe}', f'=COUNTIF(Institutions!D2:D{fin_inst},"{classe}")'])
    wsyn.append(['Sources répertoriées', f'=COUNTA(Sources!C2:C{max(2, nb_src + 1)})'])
    wsyn.append(['Sources surveillées', f'=COUNTIF(Sources!E2:E{max(2, nb_src + 1)},"oui")'])
    wsyn.append(['Changements détectés (historique)', f'=COUNTA(Changements!A2:A{fin_chg})'])
    wsyn.column_dimensions['A'].width = 44
    wsyn.column_dimensions['B'].width = 16

    sortie = os.path.join(ROOT, 'docs')
    os.makedirs(sortie, exist_ok=True)
    wb.save(os.path.join(sortie, 'veille_iiif.xlsx'))

    with open(os.path.join(sortie, 'veille_iiif.csv'), 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.writer(fh)
        w.writerow([c[0] for c in COLONNES])
        for fm in fiches:
            w.writerow(ligne_institution(fm))
    print(f'docs/veille_iiif.xlsx et .csv : {n} institutions, {nb_src} sources, {len(hist)} changement(s)')


if __name__ == '__main__':
    main()
