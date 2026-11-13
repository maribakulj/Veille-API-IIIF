"""Tests hors réseau : lecture des fiches, validation, empreintes et logique de veille."""
import os
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))

import check_sources  # noqa: E402
import validate  # noqa: E402
from fiches import classe_de, parse_fiche  # noqa: E402


class TestFiches(unittest.TestCase):
    def test_en_tete_lu(self):
        fm = parse_fiche('---\nid: GLAM-001\nstatut: "CHIFFRE TROUVÉ (page officielle)"\n---\n\n# Titre\n')
        self.assertEqual(fm['id'], 'GLAM-001')
        self.assertEqual(classe_de(fm['statut']), 'chiffre publié')

    def test_en_tete_absent_refuse(self):
        with self.assertRaises(ValueError):
            parse_fiche('# pas de front matter')

    def test_classes(self):
        self.assertEqual(classe_de('PAS DE DÉBIT IIIF CHIFFRÉ (x)'), 'pas de débit IIIF chiffré')
        self.assertEqual(classe_de('NON TROUVÉ APRÈS RECHERCHE'), 'non trouvé après recherche')
        self.assertEqual(classe_de('autre chose'), 'à classer')

    def test_depot_valide(self):
        n, erreurs = validate.valider(os.path.join(ROOT, 'institutions'))
        self.assertEqual(n, 84)
        self.assertEqual(erreurs, [])


class TestVeille(unittest.TestCase):
    def test_extraction_texte(self):
        html = '<html><script>var x=1;</script><p>Limite &amp; quota</p><!-- c --></html>'
        self.assertEqual(check_sources.extraire_texte(html), 'Limite & quota')

    def test_cycle_baseline_changement_erreur(self):
        texte = 'Page officielle de la bibliothèque avec suffisamment de texte pour passer le seuil minimal. ' * 2
        cible = [{'id': 'GLAM-999', 'institution': 'Test', 'url': 'https://exemple.test/doc'}]
        etat = {}

        def ok_v1(url):
            return f'<p>{texte}</p>'

        def ok_v2(url):
            return f'<p>{texte} Nouvelle limite : 10 requêtes par minute.</p>'

        def panne(url):
            raise OSError('réseau indisponible')

        ch = check_sources.verifier(cible, etat, ok_v1, '2026-11-13T00:00:00+00:00')
        self.assertEqual(ch, [], 'la première lecture sert de référence, sans alerte')
        ch = check_sources.verifier(cible, etat, ok_v2, '2026-11-14T00:00:00+00:00')
        self.assertEqual(len(ch), 1)
        empreinte_avant = etat['https://exemple.test/doc']['empreinte']
        ch = check_sources.verifier(cible, etat, panne, '2026-11-15T00:00:00+00:00')
        self.assertEqual(ch, [])
        self.assertEqual(etat['https://exemple.test/doc']['empreinte'], empreinte_avant,
                         'une erreur réseau ne remplace pas la dernière empreinte connue')
        self.assertTrue(etat['https://exemple.test/doc']['statut'].startswith('erreur'))


if __name__ == '__main__':
    unittest.main()
