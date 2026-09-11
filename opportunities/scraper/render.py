"""
Render the opportunities dataset as a scannable markdown table for the
repository README. Replaces the section between the marker comments.
"""
import json
import logging
from pathlib import Path

log = logging.getLogger(__name__)

MARK_START = "<!-- BEGIN_OPPORTUNITIES -->"
MARK_END = "<!-- END_OPPORTUNITIES -->"

CATEGORY_ORDER = [
    "jobs", "internship", "hackathon", "scholarship",
    "research", "fellowship", "open_source", "other",
]

CATEGORY_LABELS = {
    "jobs": "💼 Jobs",
    "internship": "🎓 Internships",
    "hackathon": "🏆 Hackathons and competitions",
    "scholarship": "🎓 Scholarships",
    "research": "🔬 Research programs",
    "fellowship": "🧑‍💻 Fellowships",
    "open_source": "🌐 Open source programs",
    "other": "📚 Other",
}

REGION_ORDER = {"India": 0, "International": 1, "Global": 2}


def _clean(value: str, limit: int = 40) -> str:
    value = (value or "").replace("|", "/").replace("\n", " ").strip()
    if len(value) > limit:
        return value[: limit - 1].rstrip() + "…"
    return value


def _sorted(opportunities: list[dict]) -> list[dict]:
    def key(o):
        region = REGION_ORDER.get(o.get("region", ""), 3)
        return (
            CATEGORY_ORDER.index(o.get("category")) if o.get("category") in CATEGORY_ORDER else 99,
            region,
            o.get("organization", "").lower(),
            o.get("title", "").lower(),
        )

    return sorted(opportunities, key=key)


def render_section(opportunities: list[dict]) -> str:
    lines = []
    buckets: dict[str, list[dict]] = {}
    for o in _sorted(opportunities):
        buckets.setdefault(o.get("category", "other"), []).append(o)

    for category in CATEGORY_ORDER:
        rows = buckets.get(category)
        if not rows:
            continue
        header = f"#### {CATEGORY_LABELS.get(category, category)} ({len(rows)})"
        lines.append(header)
        lines.append("")
        lines.append("| Role | Organization | Location | Areas | Apply |")
        lines.append("|---|---|---|---|---|")
        for o in rows:
            title = _clean(o.get("title"))
            org = _clean(o.get("organization"))
            loc = _clean(o.get("location"))
            url = o.get("official_url") or "#"
            areas = ", ".join((o.get("areas") or [])[:3]) or "—"
            lines.append(f"| {title} | {org} | {loc} | {areas} | [Apply]({url}) |")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def render_readme(readme_path: str | Path, section_content: str) -> None:
    readme_path = Path(readme_path)
    text = readme_path.read_text(encoding="utf-8")
    if MARK_START not in text or MARK_END not in text:
        raise ValueError(f"{readme_path} missing {MARK_START} / {MARK_END} markers")
    head, _, _ = text.partition(MARK_START)
    _, _, tail = text.partition(MARK_END)
    rebuilt = head + MARK_START + "\n" + section_content + MARK_END + tail
    readme_path.write_text(rebuilt, encoding="utf-8")


def render_from_json(data_path: str | Path, readme_path: str | Path) -> dict:
    with open(data_path) as f:
        data = json.load(f)
    opportunities = data.get("opportunities", [])
    section = render_section(opportunities)
    render_readme(readme_path, section)
    log.info("Rendered %d opportunities into %s", len(opportunities), readme_path)
    return data