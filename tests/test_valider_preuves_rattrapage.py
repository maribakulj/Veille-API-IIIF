#!/usr/bin/env python3
"""Tests du lien entre data.json, rapport de lecture et fiche institutionnelle."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from valider_preuves_rattrapage import verifier  # noqa: E402

RAPPORT = "VERIFICATIONS-CHATGPT-2026-11-15-Q-PREUVES.md"
URL = "https://exemple.org/iiif/id/info.json"


class TestPreuvesRattrapage(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.folder = self.root / "institutions" / "exemple"
        self.folder.mkdir(parents=True)
        self.d = {"web": [{"url": URL, "preuve": RAPPORT,
                           "date": "2026-11-15",
                           "citation": "Un JSON extrait, copie datée."}]}
        (self.folder / "data.json").write_text(
            json.dumps(self.d), encoding="utf-8")
        (self.folder / "fiche.md").write_text(
            f"Voir [{RAPPORT}](../../{RAPPORT}).", encoding="utf-8")
        (self.root / RAPPORT).write_text(
            f"# Rapport\n\nURL vérifiée : {URL}\n", encoding="utf-8")

    def test_chaine_validee(self):
        count, errors = verifier(self.root)
        self.assertEqual(count, 1)
        self.assertEqual(errors, [])

    def test_url_non_presente_dans_rapport_rejetee(self):
        (self.root / RAPPORT).write_text("# Pas de preuve", encoding="utf-8")
        _, errors = verifier(self.root)
        self.assertTrue(any("URL absente" in x for x in errors))

    def test_preuve_hors_fiche_rejetee(self):
        (self.folder / "fiche.md").write_text("# Aucun lien", encoding="utf-8")
        _, errors = verifier(self.root)
        self.assertTrue(any("non cité dans fiche" in x for x in errors))

    def test_date_manquante_rejetee(self):
        self.d["web"][0]["date"] = ""
        (self.folder / "data.json").write_text(
            json.dumps(self.d), encoding="utf-8")
        _, errors = verifier(self.root)
        self.assertTrue(any("date de consultation" in x for x in errors))


if __name__ == "__main__":
    unittest.main()
