"""Lecture des fiches institutions : en-tête YAML (données) et corps Markdown (notes)."""
import glob
import os
import re

import yaml

FRONT = re.compile(r'\A---\n(.*?)\n---\n', re.S)

CLASSES = [
    'chiffre publié',
    'pas de débit IIIF chiffré',
    'règle sans chiffre',
    'chiffre à confirmer',
    'doc lue, sans chiffre',
    'non trouvé après recherche',
]

# Préfixe du verdict -> classe. L'ordre compte : le premier préfixe reconnu gagne.
PREFIXES = [
    ('CHIFFRE TROUVÉ', 'chiffre publié'),
    ('PAS DE DÉBIT IIIF', 'pas de débit IIIF chiffré'),
    ('PARTIEL', 'règle sans chiffre'),
    ('CHIFFRE À CONFIRMER', 'chiffre à confirmer'),
    ('DOC LUE', 'doc lue, sans chiffre'),
    ('NON TROUVÉ', 'non trouvé après recherche'),
]

REQUIRED = ['id', 'institution', 'pays', 'statut', 'classe', 'verifie_le']
ID_RE = re.compile(r'^GLAM-\d{3}$')


def classe_de(statut):
    for prefixe, classe in PREFIXES:
        if str(statut).startswith(prefixe):
            return classe
    return 'à classer'


def parse_fiche(texte):
    m = FRONT.match(texte)
    if not m:
        raise ValueError('en-tête YAML absent')
    return yaml.safe_load(m.group(1)) or {}


def charger(dirpath):
    """Itère (chemin, en-tête) sur les fiches, triées par nom. Ignore les fichiers commençant par '_'."""
    for path in sorted(glob.glob(os.path.join(dirpath, '*.md'))):
        nom = os.path.basename(path)
        if nom.startswith('_'):
            continue
        with open(path, encoding='utf-8') as fh:
            yield path, parse_fiche(fh.read())
