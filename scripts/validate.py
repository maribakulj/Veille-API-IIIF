"""Vérifie la cohérence des fiches. Sort avec un code d'erreur s'il y a des problèmes."""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fiches import CLASSES, ID_RE, REQUIRED, charger, classe_de  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def valider(dirpath):
    erreurs, ids, n = [], set(), 0
    for path, fm in charger(dirpath):
        n += 1
        nom = os.path.basename(path)
        for cle in REQUIRED:
            if fm.get(cle) in (None, '', []):
                erreurs.append(f'{nom} : champ requis absent ou vide : {cle}')
        gid = str(fm.get('id', ''))
        if not ID_RE.match(gid):
            erreurs.append(f'{nom} : identifiant mal formé : {gid!r}')
        elif not nom.startswith(gid + '-'):
            erreurs.append(f'{nom} : le nom de fichier doit commencer par {gid}-')
        if gid in ids:
            erreurs.append(f'{nom} : identifiant en double : {gid}')
        ids.add(gid)
        if fm.get('classe') not in CLASSES:
            erreurs.append(f'{nom} : classe inconnue : {fm.get("classe")!r}')
        elif fm.get('classe') != classe_de(fm.get('statut', '')):
            erreurs.append(f'{nom} : classe incohérente avec le statut')
        if not re.match(r'^\d{4}-\d{2}-\d{2}$', str(fm.get('verifie_le', ''))):
            erreurs.append(f'{nom} : verifie_le doit être au format AAAA-MM-JJ')
        if not fm.get('sources') and not fm.get('sources_sans_url'):
            erreurs.append(f'{nom} : aucune source, ni URL ni explication (sources_sans_url)')
        for s in fm.get('sources') or []:
            if not isinstance(s, dict) or not str(s.get('url', '')).startswith(('http://', 'https://')):
                erreurs.append(f'{nom} : source sans URL http(s) : {s!r}')
            elif not isinstance(s.get('surveiller', False), bool):
                erreurs.append(f'{nom} : surveiller doit être true ou false : {s.get("url")}')
    return n, erreurs


if __name__ == '__main__':
    n, erreurs = valider(os.path.join(ROOT, 'institutions'))
    print(f'{n} fiches vérifiées, {len(erreurs)} erreur(s)')
    for e in erreurs:
        print('ERREUR', e)
    sys.exit(1 if erreurs or n == 0 else 0)
