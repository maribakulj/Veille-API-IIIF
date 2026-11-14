#!/usr/bin/env python3
"""Tests sans réseau du registre de rattrapage documentaire."""
import contextlib
import csv
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from etat_reverifications import agregger_constats, main, normalize_url  # noqa: E402


class RapprochementTests(unittest.TestCase):
    def test_constats_multiples_cible_confirmee_mais_acces_bloque(self):
        constats = [
            {
                "statut_doc_2026_11_14": "BLOCAGE_ACCES",
                "source_preuve": "https://example.org/collection",
                "reste_a_verifier": "Accès JSON non vérifié",
            },
            {
                "statut_doc_2026_11_14": "LIEN_OFFICIEL_CIBLE_CONFIRME",
                "source_preuve": "https://example.org/page-officielle",
                "reste_a_verifier": "Politique d'accès inconnue",
            },
        ]
        resultat = agregger_constats(constats, "Ancien contrôle")
        self.assertEqual(resultat["nombre_constats"], 2)
        self.assertIn("BLOCAGE_ACCES", resultat["statut_revision"])
        self.assertIn("LIEN_OFFICIEL_CIBLE_CONFIRME", resultat["statut_revision"])
        self.assertIn("Accès JSON non vérifié", resultat["reste_a_verifier"])
        self.assertIn("Politique d'accès inconnue", resultat["reste_a_verifier"])
        self.assertEqual(resultat["verification_http_independante"],
                         "NON_ETABLIE_PAR_LE_REGISTRE")

    def test_aucune_observation_ne_signifie_aucune_cloture(self):
        resultat = agregger_constats([], "Contrôler les entêtes")
        self.assertEqual(resultat["nombre_constats"], 0)
        self.assertEqual(resultat["statut_revision"], "NON_REEXAMINE_DANS_REGISTRE")
        self.assertEqual(resultat["reste_a_verifier"], "Contrôler les entêtes")

    def test_url_conserve_chemin_et_requete(self):
        self.assertEqual(normalize_url(" HTTPS://EXAMPLE.ORG/Manifest?ID=AbC "),
                         "https://example.org/Manifest?ID=AbC")

    def test_rapprochement_ecrit_une_ligne_par_item_sans_effacer_les_blocages(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            d = root / "institutions" / "cultural-japan"
            d.mkdir(parents=True)
            target = "https://app.cultural.jp/iiif-collection/collection.json"
            data = {
                "a_verifier_manuellement": [
                    {"url": target, "pourquoi": "accès bloqué",
                     "a_chercher": "Lire le JSON"},
                    {"url": target, "pourquoi": "doublon", "a_chercher": "Confirmer"},
                    {"url": "mailto:contact@example.org", "pourquoi": "contact",
                     "a_chercher": "Demander un quota"},
                ]
            }
            (d / "data.json").write_text(json.dumps(data), encoding="utf-8")
            (root / "data").mkdir()
            ledger = root / "data" / "reverifications-chatgpt-2026-11-14.csv"
            fields = ["slug", "url_initiale", "statut_doc_2026_11_14",
                      "source_preuve", "reste_a_verifier"]
            with ledger.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=fields)
                writer.writeheader()
                writer.writerows([
                    {"slug": "cultural-japan", "url_initiale": target,
                     "statut_doc_2026_11_14": "BLOCAGE_ACCES",
                     "source_preuve": "https://example.org/lecture",
                     "reste_a_verifier": "JSON non récupéré"},
                    {"slug": "cultural-japan", "url_initiale": target,
                     "statut_doc_2026_11_14": "LIEN_OFFICIEL_CIBLE_CONFIRME",
                     "source_preuve": "https://cultural.jp/en",
                     "reste_a_verifier": "HTTP non établi"},
                    {"slug": "autre-dossier", "url_initiale": "https://example.org/autre",
                     "statut_doc_2026_11_14": "DOCUMENT_LU",
                     "source_preuve": "https://example.org/autre",
                     "reste_a_verifier": "Aucun"},
                ])
            output = io.StringIO()
            with patch.object(sys, "argv", [
                    "etat_reverifications.py", "--root", str(root),
                    "--out", "data/etat-reverifications.csv"]), (
                    contextlib.redirect_stdout(output)):
                main()
            summary = json.loads(output.getvalue())
            self.assertEqual(summary["lignes_manuelles"], 3)
            self.assertEqual(summary["lignes_avec_constat_ledger"], 2)
            self.assertEqual(summary["lignes_avec_plusieurs_constats"], 2)
            self.assertEqual(summary["observations_supplementaires_hors_liste"], 1)
            with (root / "data" / "etat-reverifications.csv").open(
                    encoding="utf-8", newline="") as handle:
                rows = list(csv.DictReader(handle))
            self.assertEqual(len(rows), 3)
            self.assertEqual(rows[0]["nombre_constats"], "2")
            self.assertIn("BLOCAGE_ACCES", rows[0]["statut_revision"])
            self.assertIn("LIEN_OFFICIEL_CIBLE_CONFIRME", rows[1]["statut_revision"])
            self.assertEqual(rows[0]["signal_doublon"], "DOUBLON_DANS_INSTITUTION")
            self.assertEqual(rows[2]["categorie_preliminaire"],
                             "CONTACT_OU_ACTION_HUMAINE")


if __name__ == "__main__":
    unittest.main()
