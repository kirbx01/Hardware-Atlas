import sys, os, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from scraper.normalize import normalize_all
from scraper.classify import classify_all, classify_areas, is_hardware_relevant
from scraper.deduplicate import deduplicate
from scraper.validate import validate


class TestPipeline(unittest.TestCase):
    def test_empty_input(self):
        result = deduplicate([])
        self.assertEqual(len(result), 0)

    def test_invalid_records_filtered(self):
        records = [
            {"title": "", "organization": "X", "official_url": "https://x.com"},
            {"title": "Good", "organization": "X", "official_url": "https://x.com"},
        ]
        self.assertEqual(len(normalize_all(records)), 1)

def test_full_pipeline(self):
        records = [
            {
                "title": "FPGA Design Engineer", "organization": "Acme",
                "official_url": "https://acme.com/fpga", "location": "Bangalore, India",
                "_description": "RTL design using SystemVerilog and Vivado, PCB layout.",
                "category": "jobs", "type": "full_time",
            },
            {
                "title": "FPGA Design Engineer", "organization": "Acme",
                "official_url": "https://acme.com/fpga", "location": "Bangalore, India",
                "_description": "RTL design using SystemVerilog and Vivado, PCB layout.",
                "category": "jobs", "type": "full_time",
            },
            {
                "title": "Cloud Software Engineer", "organization": "Acme",
                "official_url": "https://acme.com/cloud", "location": "San Jose, CA",
                "_description": "AWS infrastructure and backend services.",
                "category": "jobs", "type": "full_time",
            },
        ]
        normalized = normalize_all(records)
        classified = classify_all(normalized)
        deduped = deduplicate(classified)
        errors = validate(deduped)
        self.assertEqual(len(deduped), 1)
        self.assertEqual(deduped[0]["title"], "FPGA Design Engineer")
        self.assertIn("FPGA", deduped[0]["areas"])
        self.assertIn("RTL", deduped[0]["areas"])
        self.assertEqual(deduped[0]["region"], "India")
        self.assertTrue(deduped[0]["official_url"].startswith("https://"))
        self.assertEqual(errors, [])


class TestJsonOutput(unittest.TestCase):
    def test_output_structure(self):
        import json
        data_path = os.path.join(os.path.dirname(__file__), "..", "data", "opportunities.json")
        with open(data_path) as f:
            data = json.load(f)
        self.assertIn("generated_at", data)
        self.assertIn("opportunity_count", data)
        self.assertIn("opportunities", data)
        self.assertIsInstance(data["opportunities"], list)


class TestPipelineFilter(unittest.TestCase):
    def test_full_pipeline_filters_non_hardware(self):
        from scraper.main import pipeline
        records = [
            {"title": "FPGA Eng", "organization": "Acme", "official_url": "https://x.com/fpga",
             "location": "San Jose", "_description": "RTL and FPGA design", "source": "greenhouse:t", "source_id": "1"},
            {"title": "Backend SWE", "organization": "Acme", "official_url": "https://x.com/be",
             "location": "San Jose", "_description": "AWS microservices Java", "source": "greenhouse:t", "source_id": "2"},
        ]
        result = pipeline(records)
        self.assertEqual(result["opportunity_count"], 1)
        self.assertEqual(result["opportunities"][0]["title"], "FPGA Eng")


class TestRelevance(unittest.TestCase):
    def _rec(self, title, desc="", team=""):
        return {"title": title, "_team": team, "_text": desc}

    def test_technical_word_required_for_desc_only_match(self):
        rec = self._rec("Demand Planner", "Supports semiconductor chip supply planning for automotive and AI products.")
        rec["areas"] = classify_areas(rec["_text"], rec["title"])
        self.assertFalse(is_hardware_relevant(rec))

    def test_engineer_title_keeps_desc_match(self):
        rec = self._rec("Demand Planning Engineer", "Semiconductor chip supply planning for automotive and AI products.")
        rec["areas"] = classify_areas(rec["_text"], rec["title"])
        self.assertTrue(is_hardware_relevant(rec))

    def test_title_team_match_always_kept(self):
        rec = self._rec("Strategic Partner", "Generalist role", team="FPGA Engineering")
        rec["areas"] = classify_areas("", rec["title"], team="FPGA Engineering")
        self.assertTrue(is_hardware_relevant(rec))

    def test_no_areas_dropped(self):
        rec = self._rec("Software Engineer", "AWS microservices and Kubernetes.")
        rec["areas"] = []
        self.assertFalse(is_hardware_relevant(rec))

    def test_design_verification_engineer_kept(self):
        rec = self._rec("Design Verification Engineer", "UVM testbenches, coverage closure, waveform debugging.")
        rec["areas"] = classify_areas(rec["_text"], rec["title"])
        self.assertTrue(is_hardware_relevant(rec))

    def test_hardware_word_title_kept(self):
        rec = self._rec("Firmware", "C and RTOS for sensor nodes.")
        rec["areas"] = classify_areas(rec["_text"], rec["title"])
        self.assertTrue(is_hardware_relevant(rec))


if __name__ == "__main__":
    unittest.main()