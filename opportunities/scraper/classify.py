"""
Keyword-based classification of opportunities into Hardware Atlas areas,
categories, and regions. Rules are transparent and readable.
"""
import re
from .config import AREAS, INDIA_KEYWORDS, REMOTE_KEYWORDS

_ESCAPED_INDIA = [re.escape(kw) for kw in INDIA_KEYWORDS]
_ESCAPED_REMOTE = [re.escape(kw) for kw in REMOTE_KEYWORDS]

INDIA_RE = re.compile(r"\b(?:" + "|".join(_ESCAPED_INDIA) + r")\b", re.IGNORECASE)
REMOTE_RE = re.compile(r"\b(?:" + "|".join(_ESCAPED_REMOTE) + r")\b", re.IGNORECASE)

AREA_RULES = {
    "Embedded": r"embedded|firmware|microcontroller|mcu|rtos|bare.?metal|arm cortex|stm32|esp32|freertos|zephyr|micropython",
    "FPGA": r"fpga|xilinx|vivado|intel quartus|altera|lattice|altera quartus",
    "RTL": r"\brtl\b|verilog|systemverilog|vhdl|\bhdl\b|cocotb|synthesis|uvm|verification",
    "ASIC": r"asic|tape.?out|gdsii|place.?and.?route|pdk|sky130|openlane|magic vlsi",
    "VLSI": r"vlsi|digital ic|analog ic|custom silicon|chip design",
    "Semiconductor": r"semiconductor|silicon|wafer|fab|fabrication|process.?node|foundry",
    "Electronics": r"electronics|circuit|analog|transistor|op.?amp|filter|amplifier|schematic|oscilloscope|multimeter",
    "Hardware": r"\bhardware\b|pcb|schematic|board.?design|kicad|altium|eagle|orcad|layout|gerber|silkscreen",
    "Robotics": r"robot|robotics|actuator|motion.?control|servo|manipulator|drone|uav|ugv",
    "DSP": r"\bdsp\b|signal.?processing|fft|filter.?design|dsp processor|digital signal|matlab|octave",
    "EDA": r"\beda\b|cadence|synopsys|mentor|siemens.?eda|vcs|xcelium|questa|design.?compiler|innovus|icc2|calibre|design.?compiler",
    "Computer Architecture": r"cpu|microarchitect|risc.?v|arm|processor|datapath|cache|pipeline|out.of.order|branch.?predict",
    "Low-level Systems": r"linux.?kernel|device.?driver|bootloader|bare.?metal|u-boot|coreboot|bios|uefi",
    "Edge AI": r"edge.?ai|tinyml|on.?device|ml.?accelerator|npu|neural.?network|inference|tensor",
    "Automotive": r"automotive|autosar|iso.?26262|can.?bus|lin\b|vehicle",
    "Power Electronics": r"power.?electronics|converter|inverter|dc.?dc|pwm|motor.?drive|smps",
}

COMPILED_AREA_RULES = {
    area: re.compile(pattern, re.IGNORECASE)
    for area, pattern in AREA_RULES.items()
}

TECH_TITLE_RE = re.compile(
    r"\b(engineer|engineering|developer|development|technician|technologist|"
    r"intern|internship|scientist|researcher|architect|designer|design|"
    r"principal|staff|senior|junior|lead|director|manager|research|specialist|"
    r"embedded|firmware|hardware|fpga|rtl|vlsi|asic|silicon|semiconductor|"
    r"electronics|electronic|robotics|robotic|pcb|processor|cpu|gpu|chip|"
    r"analog|digital|power|automotive|signal|systems|system|computer)\b",
    re.IGNORECASE,
)


def classify_areas(text: str, title: str = "", team: str = "") -> list[str]:
    combined = f"{title} {team} {text}"
    matched = []
    for area, regex in COMPILED_AREA_RULES.items():
        if regex.search(combined):
            matched.append(area)
    return matched


def classify_category(text: str, title: str = "", employment_type: str = "") -> str:
    combined = f"{title} {text}".lower()
    if "hackathon" in combined:
        return "hackathon"
    if "scholarship" in combined or "bursary" in combined:
        return "scholarship"
    if "fellowship" in combined:
        return "fellowship"
    if "research" in title.lower() or "postdoc" in combined or "research scientist" in combined:
        return "research"
    if "open source" in combined and ("program" in combined or "internship" in combined or "gsoc" in combined):
        return "open_source"
    if "intern" in combined or "intern" in employment_type.lower():
        return "internship"
    return "jobs"


def classify_region(location: str, remote: bool | None = None) -> str:
    """India wins when the location mentions an Indian city (even if it also
    says remote, e.g. "India (Remote)"). Otherwise a remote location is
    Global, and everything else is International. Word-boundary matching
    avoids "in" in "AustIN" or "SINGapore" flipping roles to India."""
    loc = (location or "")
    if INDIA_RE.search(loc):
        return "India"
    if REMOTE_RE.search(loc):
        return "Global"
    return "International"


def classify_student_level(text: str) -> str | None:
    combined = text.lower()
    if "ph.d" in combined or "phd" in combined:
        return "phd"
    if "master" in combined or "m.s." in combined or "ms " in combined:
        return "grad"
    if "bachelor" in combined or "b.e." in combined or "b.tech" in combined:
        return "undergrad"
    return None


def classify_all(records: list[dict]) -> list[dict]:
    for rec in records:
        text = rec.get("_text", "")
        title = rec.get("title", "")
        team = rec.get("_team", "")
        if not rec.get("areas"):
            rec["areas"] = classify_areas(text, title, team)
        if not rec.get("category") or rec["category"] == "jobs":
            rec["category"] = classify_category(text, title, rec.get("type", ""))
        if not rec.get("region"):
            rec["region"] = classify_region(rec.get("location", ""), rec.get("remote"))
        if not rec.get("student_level"):
            rec["student_level"] = classify_student_level(text)
    return records


def is_hardware_relevant(rec: dict) -> bool:
    """A record is kept if its title/team clearly matches an area, or if
    the description matches an area and the title contains a technical word.
    This filters out roles like planners or recruiters at chip companies
    whose descriptions merely mention hardware keywords. Curated records
    are hand-verified with intentional areas and always pass."""
    if not rec.get("areas"):
        return False
    if rec.get("source") == "curated":
        return True
    title = rec.get("title", "")
    team = rec.get("_team", "")
    if classify_areas("", title, team):
        return True
    return bool(TECH_TITLE_RE.search(f"{title} {team}"))
