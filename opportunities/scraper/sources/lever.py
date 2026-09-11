"""
Lever Postings adapter.
Docs: https://github.com/lever/postings-api
Public GET: https://api.lever.co/v0/postings/{site}?mode=json&limit=100
No auth required for published postings.
"""
import logging
import urllib.parse
from typing import Any

from .base import fetch_json, parse_timestamp, parallel_map
from ..config import LEVER_BOOTSTRAP

log = logging.getLogger(__name__)

GLOBAL_BASE = "https://api.lever.co/v0/postings"
EU_BASE = "https://api.eu.lever.co/v0/postings"
PAGE_SIZE = 100


def _fetch_postings(slug: str, base: str = GLOBAL_BASE) -> list[dict[str, Any]]:
    all_postings = []
    skip = 0
    while True:
        url = f"{base}/{urllib.parse.quote(slug)}"
        params = {"mode": "json", "skip": str(skip), "limit": str(PAGE_SIZE)}
        try:
            data = fetch_json(url, params=params)
        except Exception as exc:
            log.error("Failed to fetch Lever board %s from %s: %s", slug, base, exc)
            break
        if not isinstance(data, list) or len(data) == 0:
            break
        all_postings.extend(data)
        if len(data) < PAGE_SIZE:
            break
        skip += PAGE_SIZE
    return all_postings


def _fetch_with_fallback(slug: str) -> list[dict[str, Any]]:
    postings = _fetch_postings(slug, GLOBAL_BASE)
    if not postings:
        try:
            postings = _fetch_postings(slug, EU_BASE)
        except Exception:
            pass
    return postings


def normalize(posting: dict, slug: str, org_name: str) -> dict[str, Any]:
    cats = posting.get("categories", {})
    loc = cats.get("location", "") or ""
    team = cats.get("team", "") or ""
    commitment = cats.get("commitment", "") or ""
    workplace = posting.get("workplaceType", "") or ""
    desc = posting.get("descriptionPlain", "") or posting.get("description", "") or ""

    etype = "full_time"
    lower_commitment = commitment.lower()
    if "intern" in lower_commitment or "intern" in (cats.get("department") or "").lower():
        etype = "internship"
    elif "contract" in lower_commitment:
        etype = "contract"

    return {
        "title": posting.get("text", ""),
        "organization": org_name,
        "category": "jobs",
        "areas": [],
        "region": "",
        "location": loc,
        "type": etype,
        "eligibility": None,
        "official_url": posting.get("hostedUrl", ""),
        "application_url": posting.get("applyUrl") or posting.get("hostedUrl", ""),
        "deadline": None,
        "start_date": None,
        "end_date": None,
        "status": "open",
        "recurring": False,
        "series": None,
        "edition": None,
        "remote": workplace.lower() == "remote" if workplace else None,
        "student_level": None,
        "degree_requirements": None,
        "field_requirements": None,
        "source": f"lever:{slug}",
        "source_id": posting.get("id", ""),
        "last_verified": None,
        "_description": desc,
        "_updated_at": parse_timestamp(posting.get("createdAt")),
        "_team": team,
    }


def fetch_all(bootstrap: list[dict] | None = None) -> list[dict[str, Any]]:
    bootstrap = bootstrap or LEVER_BOOTSTRAP
    results = []

    def _company(entry):
        slug, name = entry["slug"], entry["name"]
        postings = _fetch_with_fallback(slug)
        log.info("Lever %s: %d postings", slug, len(postings))
        return [normalize(p, slug, name) for p in postings]

    for co_result in parallel_map(_company, bootstrap):
        results.extend(co_result)
    return results
