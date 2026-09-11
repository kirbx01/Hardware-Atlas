import sys, os, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from scraper.deduplicate import deduplicate


class TestDeduplicate(unittest.TestCase):
    def _make(self, source, source_id, title="Engineer", org="Org", url=None):
        return {
            "source": source,
            "source_id": source_id,
            "title": title,
            "organization": org,
            "official_url": url or f"https://{source}/{source_id}",
            "location": "San Jose, CA",
            "recurring": False,
            "series": None,
            "edition": None,
        }

    def test_dedup_by_stable_id(self):
        a = self._make("lever:acme", "123", title="FPGA Eng")
        b = self._make("lever:acme", "123", title="FPGA Eng")
        result = deduplicate([a, b])
        self.assertEqual(len(result), 1)

    def test_keeps_different_sources(self):
        a = self._make("lever:acme", "123", title="FPGA Eng")
        b = self._make("greenhouse:acme", "123", title="FPGA Eng")
        result = deduplicate([a, b])
        self.assertEqual(len(result), 2)

    def test_keeps_different_titles(self):
        a = self._make("lever:acme", "123", title="FPGA Eng")
        b = self._make("lever:acme", "123", title="ASIC Eng")
        result = deduplicate([a, b])
        self.assertEqual(len(result), 1)

    def test_fuzzy_dedup(self):
        a = self._make("greenhouse:acme", "111", title="FPGA Engineer", org="Acme Corp", url="https://acme.com/jobs/1")
        b = self._make("lever:acme", "222", title="FPGA Engineer", org="Acme Corp", url="https://acme.com/jobs/1")
        result = deduplicate([a, b])
        self.assertEqual(len(result), 1)

    def test_keeps_different_editions(self):
        a = self._make("curated", "gsoc-2025", title="GSOC", org="Google", url="https://example.com")
        a.update(recurring=True, series="Google Summer of Code", edition=2025)
        b = self._make("curated", "gsoc-2026", title="GSOC", org="Google", url="https://example.com")
        b.update(recurring=True, series="Google Summer of Code", edition=2026)
        result = deduplicate([a, b])
        self.assertEqual(len(result), 2)

    def test_preserves_order(self):
        a = self._make("lever:acme", "1")
        b = self._make("lever:acme", "2")
        c = self._make("lever:acme", "3")
        result = deduplicate([a, b, c])
        ids = [r["source_id"] for r in result]
        self.assertEqual(ids, ["1", "2", "3"])


if __name__ == "__main__":
    unittest.main()
