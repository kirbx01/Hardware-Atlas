"""
Normalization: strip raw description text, validate required fields,
lowercase regions, mark last_verified from fetch time.
"""
import re
from datetime import datetime, timezone

STRIP_TAGS = re.compile(r"<[^>]+>")
MULTI_SPACE = re.compile(r"\s+")


def _strip_html(text: str | None) -> str:
    if not text:
        return ""
    clean = STRIP_TAGS.sub(" ", text)
    return MULTI_SPACE.sub(" ", clean).strip()


def normalize_record(rec: dict) -> dict:
    rec["title"] = (rec.get("title") or "").strip()
    rec["organization"] = (rec.get("organization") or "").strip()
    rec["location"] = (rec.get("location") or "").strip()
    rec["official_url"] = (rec.get("official_url") or "").strip()
    rec["application_url"] = (rec.get("application_url") or "").strip() or None
    rec["source"] = (rec.get("source") or "").strip()
    rec["source_id"] = (rec.get("source_id") or "").strip()

    raw_desc = rec.pop("_description", "") or ""
    rec["_text"] = _strip_html(raw_desc)

    if not rec.get("last_verified"):
        rec["last_verified"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    if not rec.get("status"):
        rec["status"] = "unknown"

    if rec.get("remote") is None:
        loc_lower = rec.get("location", "").lower()
        if any(kw in loc_lower for kw in ["remote", "worldwide", "anywhere"]):
            rec["remote"] = True

    for field in ("deadline", "start_date", "end_date"):
        val = rec.get(field)
        if val and isinstance(val, str) and not val.endswith("Z"):
            rec[field] = val.rstrip("Z") + "Z"

    return rec


def normalize_all(records: list[dict]) -> list[dict]:
    return [normalize_record(r) for r in records if _is_valid_minimal(r)]


def _is_valid_minimal(rec: dict) -> bool:
    if not rec.get("title"):
        return False
    if not rec.get("organization"):
        return False
    if not rec.get("official_url"):
        return False
    return True
