#!/usr/bin/env python3
"""Empêcher l'amalgame quota HTTP / robots / pagination / droits dans Excel."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from classification_limites import categorie, seuil_debit_explicitement_identifie


class TestsClassificationLimites(unittest.TestCase):
    def test_debit_requetes_identifie(self):
        lim = {"nature": "Limite de débit (anonyme)",
               "valeur": "60 requêtes", "fenetre": "par minute"}
        self.assertTrue(seuil_debit_explicitement_identifie(lim))
        self.assertIn("Seuil de débit", categorie(lim))

    def test_crawl_delay_ne_compte_pas_comme_quota_api(self):
        lim = {"nature": "Crawl-delay robots.txt",
               "valeur": "30 s", "fenetre": "entre requêtes"}
        self.assertFalse(seuil_debit_explicitement_identifie(lim))
        self.assertIn("robots.txt", categorie(lim))

    def test_pagination_ou_pixels_sont_differents(self):
        for nature, valeur in (
            ("Taille maximale d'une image", "1200 pixels"),
            ("Plafond de résultats de recherche", "100 résultats"),
            ("Pagination (pas un quota)", "limit=500"),
        ):
            with self.subTest(nature=nature):
                lim = {"nature": nature, "valeur": valeur,
                       "fenetre": "par requête"}
                self.assertFalse(seuil_debit_explicitement_identifie(lim))
                self.assertIn("Pagination", categorie(lim))

    def test_recommandations_non_contractuelles(self):
        lim = {"nature": "Indicatif de débit (« best practice »)",
               "valeur": "3000 appels", "fenetre": "par jour"}
        self.assertFalse(seuil_debit_explicitement_identifie(lim))
        self.assertIn("Recommandation", categorie(lim))

    def test_quota_maptiler_hors_iiif_ne_compte_pas(self):
        lim = {"nature": "Quota gratuit non commercial (couches de cartes MapTiler, hors IIIF)",
               "valeur": "100 000", "fenetre": "par mois"}
        self.assertFalse(seuil_debit_explicitement_identifie(lim))
        self.assertIn("hors IIIF", categorie(lim))

    def test_seuil_sans_fenetre_ne_passe_pas(self):
        lim = {"nature": "Limite de débit LibraryCloud",
               "valeur": "300", "fenetre": "–"}
        self.assertFalse(seuil_debit_explicitement_identifie(lim))


if __name__ == "__main__":
    unittest.main()
