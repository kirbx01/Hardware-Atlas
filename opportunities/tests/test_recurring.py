import sys, os, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from scraper.deduplicate import deduplicate


class TestRecurringEditions(unittest.TestCase):
    def test_same_series_different_editions_are_kept(self):
        a = {
            "source": "curated", "source_id": "gsoc-2025", "title": "GSOC",
            "organization": "Google", "official_url": "https://example.com",
            "location": "Remote", "recurring": True, "series": "Google Summer of Code", "edition": 2025,
        }
        b = {
            "source": "curated", "source_id": "gsoc-2026", "title": "GSOC",
            "organization": "Google", "official_url": "https://example.com",
            "location": "Remote", "recurring": True, "series": "Google Summer of Code", "edition": 2026,
        }
        result = deduplicate([a, b])
        self.assertEqual(len(result), 2)
        editions = {r["edition"] for r in result}
        self.assertEqual(editions, {2025, 2026})

    def test_non_recurring_series_are_deduped(self):
        a = {
            "source": "greenhouse:acme", "source_id": "111", "title": "FPGA Eng",
            "organization": "Acme", "official_url": "https://acme.com/1",
            "location": "San Jose", "recurring": False, "series": None, "edition": None,
        }
        b = {
            "source": "lever:acme", "source_id": "222", "title": "FPGA Eng",
            "organization": "Acme", "official_url": "https://acme.com/1",
            "location": "San Jose", "recurring": False, "series": None, "edition": None,
        }
        result = deduplicate([a, b])
        self.assertEqual(len(result), 1)

    def test_missing_edition_not_confused_with_different(self):
        a = {
            "source": "curated", "source_id": "f1", "title": "Fellowship",
            "organization": "X", "official_url": "https://x.com",
            "location": "Global", "recurring": True, "series": "X Fellowship", "edition": None,
        }
        b = {
            "source": "curated", "source_id": "f2", "title": "Fellowship",
            "organization": "X", "official_url": "https://x.com",
            "location": "Global", "recurring": True, "series": "X Fellowship", "edition": None,
        }
        result = deduplicate([a, b])
        self.assertEqual(len(result), 1)


if __name__ == "__main__":
    unittest.main()
