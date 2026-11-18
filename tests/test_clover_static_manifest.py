"""Tester un vrai fichier JSON statique, sans inférer d'accès live aux images."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JSON_PATH = ROOT / "institutions/northwestern-university-libraries/sources/lectures-2026-11-18/clover-tagging-manifest-static.json"


class TestCloverExample(unittest.TestCase):
    def test_static_manifest_is_iiif_presentation_3(self):
        data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
        self.assertEqual(data["@context"], "http://iiif.io/api/presentation/3/context.json")
        self.assertEqual(data["type"], "Manifest")
        self.assertEqual(len(data["items"]), 1)
        self.assertEqual(data["id"], "https://clover.iiif.library.northwestern.edu/mocks/tagging/manifest.json")

    def test_document_refers_to_actual_image_host_not_auth_guarantee(self):
        data = json.loads(JSON_PATH.read_text(encoding="utf-8"))
        serialized = json.dumps(data)
        self.assertIn("https://iiif.dc.library.northwestern.edu/iiif/3/bcb98b9f-4c44-4fd0-bfa9-673fb904a2b1", serialized)
        self.assertNotEqual(data["id"].split("/")[2], "iiif.dc.library.northwestern.edu")


if __name__ == "__main__":
    unittest.main()
