"""Veille des sources : télécharge les pages marquées surveiller, compare une empreinte du texte à la précédente.

Un changement d'empreinte signale qu'une page a bougé ; il ne dit pas quelle valeur a changé.
Les pages dynamiques (horodatages, jetons) peuvent provoquer de fausses alertes.
"""
import datetime
import hashlib
import html as htmllib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fiches import charger  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = 'veille-api-iiif/1.0 (veille de documentation publique)'
MIN_TEXTE = 50


def extraire_texte(corps):
    corps = re.sub(r'(?is)<(script|style|noscript)\b.*?</\1>', ' ', corps)
    corps = re.sub(r'(?s)<!--.*?-->', ' ', corps)
    texte = htmllib.unescape(re.sub(r'(?s)<[^>]+>', ' ', corps))
    return re.sub(r'\s+', ' ', texte).strip()


def empreinte(texte):
    return hashlib.sha256(texte.encode('utf-8')).hexdigest()


def cibles(dirpath):
    vus, res = set(), []
    for _, fm in charger(dirpath):
        for s in fm.get('sources') or []:
            url = str(s.get('url', ''))
            if s.get('surveiller') and url.startswith(('http://', 'https://')) and url not in vus:
                vus.add(url)
                res.append({'id': fm['id'], 'institution': fm.get('institution', ''), 'url': url})
    return res


def verifier(cibles_, etat, recuperer, maintenant):
    """Met à jour `etat` (url -> dict) et renvoie la liste des changements constatés."""
    changements = []
    for c in cibles_:
        url = c['url']
        prec = etat.get(url, {})
        try:
            texte = extraire_texte(recuperer(url))
            if len(texte) < MIN_TEXTE:
                raise ValueError('contenu trop court')
        except Exception as exc:  # une page en erreur ne doit pas casser la veille
            etat[url] = {**prec, 'statut': f'erreur: {type(exc).__name__}', 'verifie_le': maintenant}
            continue
        h = empreinte(texte)
        nouveau = {'empreinte': h, 'statut': 'ok', 'verifie_le': maintenant,
                   'modifie_le': prec.get('modifie_le')}
        if prec.get('empreinte') and prec['empreinte'] != h:
            nouveau['modifie_le'] = maintenant
            changements.append({'date': maintenant, 'id': c['id'], 'institution': c['institution'],
                                'url': url, 'precedente': prec['empreinte'], 'nouvelle': h})
        etat[url] = nouveau
    return changements


def recuperer_http(url):
    import requests
    rep = requests.get(url, headers={'User-Agent': UA}, timeout=30, allow_redirects=True)
    rep.raise_for_status()
    return rep.text


def main():
    chemin_etat = os.path.join(ROOT, 'data', 'state.json')
    chemin_hist = os.path.join(ROOT, 'data', 'historique.jsonl')
    chemin_run = os.path.join(ROOT, 'data', 'changements.json')
    etat = json.load(open(chemin_etat, encoding='utf-8')) if os.path.exists(chemin_etat) else {}
    maintenant = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
    liste = cibles(os.path.join(ROOT, 'institutions'))
    changements = verifier(liste, etat, recuperer_http, maintenant)
    with open(chemin_etat, 'w', encoding='utf-8') as fh:
        json.dump(etat, fh, ensure_ascii=False, indent=1, sort_keys=True)
    with open(chemin_hist, 'a', encoding='utf-8') as fh:
        for ch in changements:
            fh.write(json.dumps(ch, ensure_ascii=False) + '\n')
    ok = sum(1 for v in etat.values() if v.get('statut') == 'ok')
    with open(chemin_run, 'w', encoding='utf-8') as fh:
        json.dump({'dernier_run': maintenant, 'pages': len(liste), 'ok': ok,
                   'erreurs': len(liste) - ok, 'changements': changements},
                  fh, ensure_ascii=False, indent=1)
    print(f'{len(liste)} pages, {ok} lues, {len(liste) - ok} en erreur, {len(changements)} changement(s)')


if __name__ == '__main__':
    main()
