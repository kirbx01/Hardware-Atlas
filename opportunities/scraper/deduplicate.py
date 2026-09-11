"""
Deduplication using stable source IDs and a fuzzy fallback.
Different yearly editions of the same series are kept separate.
"""
import hashlib
import re


def _stable_id(rec: dict) -> str:
    sid = rec.get("source_id", "")
    source = rec.get("source", "")
    if sid and source:
        return f"{source}:{sid}"
    parts = [
        rec.get("source", ""),
        rec.get("organization", ""),
        rec.get("title", ""),
        rec.get("location", ""),
        rec.get("official_url", ""),
    ]
    raw = "|".join(p.lower().strip() for p in parts)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:32]


def _normalize_for_fuzzy(rec: dict) -> str:
    title = re.sub(r"[^a-z0-9]+", " ", rec.get("title", "").lower()).strip()
    org = re.sub(r"[^a-z0-9]+", " ", rec.get("organization", "").lower()).strip()
    loc = re.sub(r"[^a-z0-9]+", " ", rec.get("location", "").lower()).strip()
    url = (rec.get("official_url") or "").lower().rstrip("/")
    return f"{org}|{title}|{loc}|{url}"


def deduplicate(records: list[dict]) -> list[dict]:
    seen_ids: dict[str, dict] = {}
    seen_fuzzy: dict[str, dict] = {}

    for rec in records:
        rec["_id"] = _stable_id(rec)
        sid = rec["_id"]
        if sid in seen_ids:
            continue
        fuzzy_key = _normalize_for_fuzzy(rec)
        if fuzzy_key in seen_fuzzy:
            existing = seen_fuzzy[fuzzy_key]
            if not _different_editions(rec, existing):
                continue
        seen_ids[sid] = rec
        seen_fuzzy[fuzzy_key] = rec

    return list(seen_ids.values())


def _different_editions(a: dict, b: dict) -> bool:
    if a.get("recurring") and b.get("recurring"):
        a_series = (a.get("series") or "").lower()
        b_series = (b.get("series") or "").lower()
        if a_series and b_series and a_series == b_series:
            return a.get("edition") != b.get("edition")
    return False
