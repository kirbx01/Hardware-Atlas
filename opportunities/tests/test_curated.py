"""
End-to-end checks for curated opportunities in scraper/curated.json.
Curated entries must survive the full pipeline and stay within the
validated schema. At least one entry per curated category is expected,
so category coverage does not regress silently.
"""
import json
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from scraper.normalize import normalize_all
from scraper.classify import classify_all
from scraper.deduplicate import deduplicate
from scraper.validate import validate, VALID_CATEGORIES

HERE = os.path.dirname(__file__)
CURATED = os.path.join(HERE, "..", "scraper", "curated.json")
DATA = os.path.join(HERE, "..", "data", "opportunities.json")

CURATED_CATEGORIES = {
    "internship": "internship",
    "hackathon": "hackathon",
    "research": "research",
    "fellowship": "fellowship",
    "open_source": "open_source",
    "other": "other",
}


class TestCuratedRecords(unittest.TestCase):
    def setUp(self):
        with open(CURATED) as f:
            self.curated = json.load(f)

    def _pipeline(self):
        return deduplicate(classify_all(normalize_all(self.curated)))

    def test_curated_records_survive_pipeline(self):
        processed = self._pipeline()
        errors = validate(processed)
        self.assertEqual(errors, [])
        self.assertEqual(len(processed), len(self.curated))

    def test_every_curated_record_has_required_fields(self):
        for rec in self.curated:
            self.assertTrue(rec.get("title"), "missing title")
            self.assertTrue(rec.get("organization"), "missing organization")
            self.assertTrue(rec.get("official_url", "").startswith("https://"))
            self.assertEqual(rec.get("source"), "curated")
            self.assertTrue(rec.get("source_id"), "missing source_id")
            self.assertIn(rec.get("region"), {"India", "International", "Global"})
            self.assertIn(rec.get("category"), VALID_CATEGORIES)

    def test_curated_area_taxonomy_valid(self):
        from scraper.config import AREAS
        valid = set(AREAS)
        for rec in self.curated:
            for area in rec.get("areas", []):
                self.assertIn(area, valid, f"unknown area {area!r} in {rec['source_id']}")

    def test_curated_categories_covered(self):
        used = {rec.get("category") for rec in self.curated}
        for expected in CURATED_CATEGORIES:
            self.assertIn(expected, used, f"no curated entry uses category {expected!r}")

    def test_urls_live_after_pipeline(self):
        for rec in self._pipeline():
            for field in ("official_url", "application_url"):
                url = rec.get(field)
                if url:
                    self.assertTrue(url.startswith("http"), f"bad {field} in {rec['source_id']}")


class TestPublishedData(unittest.TestCase):
    def test_published_data_passes_validation(self):
        with open(DATA) as f:
            data = json.load(f)
        self.assertEqual(data["opportunity_count"], len(data["opportunities"]))
        errors = validate(data["opportunities"])
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()