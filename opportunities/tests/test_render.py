import sys, os, unittest, tempfile, pathlib
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from scraper.render import render_section, render_readme, MARK_START, MARK_END


class TestRender(unittest.TestCase):
    def _opps(self):
        return [
            {"title": "FPGA Engineer", "organization": "Acme", "location": "San Jose, CA",
             "areas": ["FPGA", "RTL"], "category": "jobs", "region": "International",
             "official_url": "https://acme.com/fpga"},
            {"title": "VLSI Intern", "organization": "Acme", "location": "Bangalore, India",
             "areas": ["ASIC", "VLSI"], "category": "internship", "region": "India",
             "official_url": "https://acme.com/intern"},
        ]

    def test_renders_table_with_apply_link(self):
        section = render_section(self._opps())
        self.assertIn("| Role | Organization | Location | Areas | Apply |", section)
        self.assertIn("[Apply](https://acme.com/fpga)", section)
        self.assertIn("#### 💼 Jobs (1)", section)
        self.assertIn("#### 🎓 Internships (1)", section)

    def test_sorted_by_category_and_region(self):
        section = render_section(self._opps())
        jobs = section.index("#### 💼 Jobs")
        interns = section.index("#### 🎓 Internships")
        self.assertLess(jobs, interns)

    def test_empty_renders_without_tables(self):
        section = render_section([])
        self.assertNotIn("| Role |", section)
        self.assertEqual(section.strip(), "")

    def test_escaping(self):
        opps = [{"title": "FW | Tooling", "organization": "A|B", "location": "X; Y",
                 "areas": ["Embedded"], "category": "jobs", "region": "Global",
                 "official_url": "https://x.com"}]
        section = render_section(opps)
        self.assertIn("FW / Tooling", section)
        self.assertIn("A/B", section)

    def test_render_readme_replaces_between_markers(self):
        readme = "Head\n" + MARK_START + "old" + MARK_END + "\nTail\n"
        with tempfile.TemporaryDirectory() as tmp:
            path = pathlib.Path(tmp) / "README.md"
            path.write_text(readme)
            render_readme(path, "new-table\n")
            result = path.read_text()
        self.assertIn("Head\n" + MARK_START + "\nnew-table\n" + MARK_END, result)
        self.assertIn("Tail\n", result)
        self.assertNotIn("old", result)

    def test_render_readme_missing_markers_raises(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = pathlib.Path(tmp) / "README.md"
            path.write_text("no markers here")
            with self.assertRaises(ValueError):
                render_readme(path, "x")


if __name__ == "__main__":
    unittest.main()