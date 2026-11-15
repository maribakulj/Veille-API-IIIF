#!/usr/bin/env python3
"""Tests unitaires sans réseau du triage des interventions humaines."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from triage_interventions import generate, qualifier  # noqa: E402


def item(url, status="", duplicate="", read="CONTENU_NON_DEMONTRE_PAR_REPRISE_O"):
    return {"institution": "test", "rang": "1", "url": url,
            "statut_revision": status, "signal_doublon": duplicate,
            "lecture_documentaire": read, "preuve": ""}


class TriageTests(unittest.TestCase):
    def test_contact_est_decision_et_pas_navigation(self):
        r = qualifier(item("mailto:bndigital@bnportugal.gov.pt"))
        self.assertEqual(r["classe"], "DEMANDE_INSTITUTIONNELLE")
        self.assertEqual(r["intervention_utilisateur"], "OUI_SI_NECESSAIRE")

    def test_controle_json_nexige_pas_navigation_humaine(self):
        r = qualifier(item("https://a.example/iiif/2/image/info.json", "BLOCAGE_ACCES"))
        self.assertEqual(r["classe"], "SERVICE_TECHNIQUE_A_VERIFIER")
        self.assertEqual(r["intervention_utilisateur"], "NON_PAR_DEFAUT")

    def test_robots_est_distinct_du_quota(self):
        r = qualifier(item("https://a.example/robots.txt", "DEFI_WAF"))
        self.assertEqual(r["classe"], "ROBOTS_OU_POLITIQUE_CRAWL")

    def test_vieux_lien_404_na_pas_besoin_de_nouveau_lecteur(self):
        r = qualifier(item("https://a.example/ancienne", "ANCIENNE_URL_404"))
        self.assertEqual(r["classe"], "LIEN_HISTORIQUE_OU_DEPLACE")

    def test_pdf_partiel_reste_a_inspecter(self):
        r = qualifier(item("https://a.example/conference.pdf", "PDF_DIAPOS_ANALYSE_PARTIELLE"))
        self.assertEqual(r["classe"], "PIECE_PDF_OU_ARCHIVE")

    def test_un_meme_hote_en_plusieurs_dossiers_ne_justifie_pas_repetition(self):
        r = qualifier(item("https://a.example/", "DEFI_403",
                           "REFERENCE_INTER_INSTITUTIONS"))
        self.assertEqual(r["classe"], "REFERENCE_PARTAGEE")

    def test_lu_est_exclu_et_non_lu_conserve(self):
        all_rows = [
            item("https://a.example/iiif/manifest", "WAF"),
            item("https://a.example/iiif/manifest",
                 read="TEXTE_RECUPERE_COPIE_DATEE"),
        ]
        rows, summary = generate(all_rows)
        self.assertEqual(len(rows), 1)
        self.assertEqual(summary["entrees_non_lues"], 1)
        self.assertEqual(rows[0]["preuve_http_actuelle"],
                         "NON_ETABLIE_PAR_CE_TRIAGE")

    def test_info_json_301_reste_un_service_a_lire(self):
        r = qualifier(item("https://example.org/iiif/2/a/info.json",
                           "REDIRECTION_AUTOREFFERENTIELLE_SANS_JSON_U"))
        self.assertEqual(r["classe"], "SERVICE_TECHNIQUE_A_VERIFIER")

    def test_doc_termes_remplacee_ne_demande_pas_nouvelle_lecture_humaine(self):
        r = qualifier(item(
            "https://www.qdl.qa/en/copyright-and-ethical-terms-reuse",
            "CONDITIONS_NON_EXTRAITES_520_2026_11_14"))
        self.assertEqual(r["classe"], "SUBSTITUT_OFFICIEL_LU")
        self.assertIn("/copyright-ethical-terms-reuse", r["action"])

    def test_collection_json_hors_chemin_iiif_est_technique(self):
        r = qualifier(item("https://app.cultural.jp/iiif-collection/collection.json",
                           "JSON_NON_EXTRAIT_2026_11_14"))
        self.assertEqual(r["classe"], "SERVICE_TECHNIQUE_A_VERIFIER")

    def test_authentification_na_pas_ete_effectuee(self):
        r = qualifier(item("https://web.library.yale.edu/lit/servicecatalog/164929"))
        self.assertEqual(r["classe"], "AUTORISATION_COMPTE")
        self.assertEqual(r["intervention_utilisateur"], "OUI_SI_NECESSAIRE")


if __name__ == "__main__":
    unittest.main()
