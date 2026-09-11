"""
Validate the generated opportunities list.
Checks required fields, URL format, allowed values.
"""
import re

URL_RE = re.compile(r"^https?://")

VALID_CATEGORIES = {
    "jobs", "internship", "hackathon", "scholarship",
    "research", "fellowship", "open_source", "other",
}
VALID_REGIONS = {"India", "International", "Global"}
VALID_STATUSES = {"open", "unknown", "closed"}


def validate(records: list[dict]) -> list[str]:
    errors = []
    for i, rec in enumerate(records):
        prefix = f"record[{i}]"
        if not rec.get("title"):
            errors.append(f"{prefix}: missing title")
        if not rec.get("organization"):
            errors.append(f"{prefix}: missing organization")
        if not rec.get("official_url"):
            errors.append(f"{prefix}: missing official_url")
        elif not URL_RE.match(rec.get("official_url", "")):
            errors.append(f"{prefix}: invalid official_url: {rec['official_url']}")
        if rec.get("application_url") and not URL_RE.match(rec["application_url"]):
            errors.append(f"{prefix}: invalid application_url: {rec['application_url']}")
        cat = rec.get("category", "")
        if cat and cat not in VALID_CATEGORIES:
            errors.append(f"{prefix}: invalid category: {cat}")
        region = rec.get("region", "")
        if region and region not in VALID_REGIONS:
            errors.append(f"{prefix}: invalid region: {region}")
        status = rec.get("status", "")
        if status and status not in VALID_STATUSES:
            errors.append(f"{prefix}: invalid status: {status}")
        areas = rec.get("areas", [])
        if not isinstance(areas, list):
            errors.append(f"{prefix}: areas is not a list")
    return errors
