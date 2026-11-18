"""Test sans réseau de la copie IIIF NPM réellement enregistrée le 18/11/2026.

Ce test valide la syntaxe et la provenance locale ; il ne vérifie ni
les en-têtes HTTP, ni la fraîcheur du service, ni un quota réseau.
"""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = ROOT / "institutions/national-palace-museum-taiwan/sources/lectures-2026-11-18/info-K1F000001N000000000PAA-indexed.json"


class NationalPalaceMuseumSnapshot(unittest.TestCase):
    def test_snapshot_est_json_iiif_image_2(self):
        data = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
        self.assertEqual(data["@context"], "http://iiif.io/api/image/2/context.json")
        self.assertEqual(data["@id"], "https://iiifod.npm.gov.tw/iiif/2/K1F%2FK1F000001N000000000PAA")
        self.assertEqual((data["width"], data["height"]), (3055, 2291))
        self.assertEqual((data["tiles"][0]["width"], data["tiles"][0]["height"]), (512, 512))
        self.assertEqual(data["tiles"][0]["scaleFactors"], [1, 2, 4, 8, 16, 32])
        self.assertEqual(data["profile"][0], "http://iiif.io/api/image/2/level2.json")

    def test_max_area_est_une_surface_et_non_un_quota(self):
        data = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
        self.assertEqual(data["profile"][1]["maxArea"], data["width"] * data["height"])
        self.assertNotIn("rateLimit", data)


if __name__ == "__main__":
    unittest.main()
