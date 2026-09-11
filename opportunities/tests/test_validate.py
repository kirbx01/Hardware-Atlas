import sys, os, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from scraper.validate import validate


class TestValidate(unittest.TestCase):
    def _make(self, **overrides):
        base = {
            "title": "Test Job",
            "organization": "Test Org",
            "category": "jobs",
            "region": "International",
            "official_url": "https://example.com/job",
            "application_url": "",
            "areas": ["FPGA"],
            "status": "open",
        }
        base.update(overrides)
        return base

    def test_valid_record_passes(self):
        errors = validate([self._make()])
        self.assertEqual(errors, [])

    def test_missing_title(self):
        errors = validate([self._make(title="")])
        self.assertTrue(any("title" in e for e in errors))

    def test_missing_organization(self):
        errors = validate([self._make(organization="")])
        self.assertTrue(any("organization" in e for e in errors))

    def test_missing_url(self):
        errors = validate([self._make(official_url="")])
        self.assertTrue(any("official_url" in e for e in errors))

    def test_invalid_url(self):
        errors = validate([self._make(official_url="not-a-url")])
        self.assertTrue(any("invalid official_url" in e for e in errors))

    def test_invalid_category(self):
        errors = validate([self._make(category="bogus")])
        self.assertTrue(any("invalid category" in e for e in errors))

    def test_invalid_region(self):
        errors = validate([self._make(region="Mars")])
        self.assertTrue(any("invalid region" in e for e in errors))

    def test_invalid_application_url(self):
        errors = validate([self._make(application_url="ftp://bad")])
        self.assertTrue(any("invalid application_url" in e for e in errors))

    def test_areas_must_be_list(self):
        errors = validate([self._make(areas="FPGA")])
        self.assertTrue(any("areas is not a list" in e for e in errors))

    def test_valid_optional_fields(self):
        rec = self._make(application_url="https://example.com/apply", status="unknown")
        errors = validate([rec])
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
