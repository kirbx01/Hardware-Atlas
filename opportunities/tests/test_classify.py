import sys, os, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from scraper.classify import classify_areas, classify_category, classify_region


class TestAreaClassification(unittest.TestCase):
    def test_fpga_keywords(self):
        areas = classify_areas("Design and verify FPGA systems using Vivado", "FPGA Engineer")
        self.assertIn("FPGA", areas)

    def test_rtl_keywords(self):
        areas = classify_areas("RTL verification with SystemVerilog UVM", "RTL Verification")
        self.assertIn("RTL", areas)

    def test_embedded_keywords(self):
        areas = classify_areas("Develop firmware on ARM Cortex-M microcontrollers", "Embedded Engineer")
        self.assertIn("Embedded", areas)

    def test_no_match(self):
        areas = classify_areas("Cloud software platform", "Software Engineer")
        self.assertEqual(areas, [])

    def test_multiple_areas(self):
        areas = classify_areas(
            "ASIC design RTL synthesis and verification using SystemVerilog UVM Cadence EDA tools",
            "ASIC Verification Engineer"
        )
        self.assertIn("ASIC", areas)
        self.assertIn("RTL", areas)
        self.assertIn("EDA", areas)

    def test_robotics_keywords(self):
        areas = classify_areas("Build robotic actuator control firmware", "Robotics Firmware")
        self.assertIn("Robotics", areas)

    def test_hardware_keywords(self):
        areas = classify_areas("PCB layout in KiCad and schematic review", "Hardware Engineer")
        self.assertIn("Hardware", areas)

    def test_automotive_keywords(self):
        areas = classify_areas("AUTOSAR BSW integration ISO 26262 functional safety", "Automotive SW")
        self.assertIn("Automotive", areas)

    def test_dsp_keywords(self):
        areas = classify_areas("DSP algorithm optimization FFT implementation", "DSP Engineer")
        self.assertIn("DSP", areas)

    def test_edge_ai_keywords(self):
        areas = classify_areas("TinyML inference on microcontroller edge device", "Edge AI Engineer")
        self.assertIn("Edge AI", areas)


class TestCategoryClassification(unittest.TestCase):
    def test_hackathon(self):
        self.assertEqual(classify_category("Annual embedded hackathon", "Hackathon"), "hackathon")

    def test_scholarship(self):
        self.assertEqual(classify_category("VLSI scholarship program", "Scholarship"), "scholarship")

    def test_fellowship(self):
        self.assertEqual(classify_category("RISC-V research fellowship", "Fellowship"), "fellowship")

    def test_intern_from_title(self):
        self.assertEqual(classify_category("Firmware intern", "Summer Intern"), "internship")

    def test_research(self):
        cat = classify_category("Research scientist position", "Research Scientist")
        self.assertEqual(cat, "research")

    def test_open_source(self):
        cat = classify_category("Open source program internship", "OSS Intern")
        self.assertEqual(cat, "open_source")

    def test_default_jobs(self):
        self.assertEqual(classify_category("FPGA Design Engineer", "FPGA Engineer"), "jobs")


class TestRegionClassification(unittest.TestCase):
    def test_india(self):
        self.assertEqual(classify_region("Bangalore, India"), "India")

    def test_bangalore(self):
        self.assertEqual(classify_region("Bangalore"), "India")

    def test_remote(self):
        self.assertEqual(classify_region("Remote"), "Global")

    def test_international(self):
        self.assertEqual(classify_region("San Jose, CA"), "International")

    def test_global(self):
        self.assertEqual(classify_region("Worldwide"), "Global")

    def test_india_wins_over_remote(self):
        self.assertEqual(classify_region("India (Remote)"), "India")

    def test_no_in_substring_bug(self):
        self.assertEqual(classify_region("Austin, TX"), "International")
        self.assertEqual(classify_region("Singapore"), "International")
        self.assertEqual(classify_region("Berlin, Germany"), "International")

    def test_in_code(self):
        self.assertEqual(classify_region("Bengaluru, IND"), "India")

    def test_hyderabad(self):
        self.assertEqual(classify_region("Hyderabad"), "India")


if __name__ == "__main__":
    unittest.main()
