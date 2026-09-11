import sys, os, unittest, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from scraper.normalize import normalize_record, normalize_all

FIXTURE_DIR = os.path.join(os.path.dirname(__file__), "fixtures")


class TestNormalizeRecord(unittest.TestCase):
    def test_strips_html_description(self):
        rec = {"title": "Test", "organization": "Org", "official_url": "https://example.com", "_description": "<p>Hello <b>world</b></p>"}
        norm = normalize_record(rec)
        self.assertEqual(norm["_text"], "Hello world")
        self.assertNotIn("<", norm["_text"])

    def test_sets_last_verified(self):
        rec = {"title": "Test", "organization": "Org", "official_url": "https://example.com"}
        norm = normalize_record(rec)
        self.assertIn("T", norm["last_verified"])

    def test_rejects_missing_title(self):
        result = normalize_all([{"title": "", "organization": "Org", "official_url": "https://x"}])
        self.assertEqual(len(result), 0)

    def test_rejects_missing_org(self):
        result = normalize_all([{"title": "T", "organization": "", "official_url": "https://x"}])
        self.assertEqual(len(result), 0)

    def test_rejects_missing_url(self):
        result = normalize_all([{"title": "T", "organization": "O", "official_url": ""}])
        self.assertEqual(len(result), 0)

    def test_preserves_valid(self):
        rec = {"title": "T", "organization": "O", "official_url": "https://example.com"}
        result = normalize_all([rec])
        self.assertEqual(len(result), 1)

    def test_remote_detection_from_location(self):
        rec = {"title": "T", "organization": "O", "official_url": "https://example.com", "location": "Remote"}
        norm = normalize_record(rec)
        self.assertTrue(norm["remote"])

    def test_empty_description(self):
        rec = {"title": "T", "organization": "O", "official_url": "https://example.com", "_description": None}
        norm = normalize_record(rec)
        self.assertEqual(norm["_text"], "")


class TestNormalizeGreenhouse(unittest.TestCase):
    def test_normalizes_sample(self):
        with open(os.path.join(FIXTURE_DIR, "greenhouse_sample.json")) as f:
            jobs = json.load(f)
        from scraper.sources.greenhouse import normalize
        results = [normalize(j, "samsungsemiconductor", "Samsung Semiconductor") for j in jobs]
        results = normalize_all(results)
        self.assertEqual(len(results), 3)
        self.assertEqual(results[0]["category"], "jobs")


class TestNormalizeLever(unittest.TestCase):
    def test_normalizes_sample(self):
        with open(os.path.join(FIXTURE_DIR, "lever_sample.json")) as f:
            postings = json.load(f)
        from scraper.sources.lever import normalize
        results = [normalize(p, "shieldai", "Shield AI") for p in postings]
        results = normalize_all(results)
        self.assertEqual(len(results), 3)


class TestNormalizeAshby(unittest.TestCase):
    def test_filters_unlisted(self):
        with open(os.path.join(FIXTURE_DIR, "ashby_sample.json")) as f:
            data = json.load(f)
        from scraper.sources.ashby import normalize
        listed = [j for j in data["jobs"] if j.get("isListed", True)]
        results = [normalize(j, "sensmore", "Sensmore") for j in listed]
        results = normalize_all(results)
        self.assertEqual(len(results), 2)


if __name__ == "__main__":
    unittest.main()
