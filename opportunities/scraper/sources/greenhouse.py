"""
Greenhouse Job Board adapter.
Docs: https://developers.greenhouse.io/job-board.html
Public GET: https://boards-api.greenhouse.io/v1/boards/{board_token}/jobs?content=true
No auth required for read.
"""
import logging
import urllib.parse
from typing import Any

from .base import fetch_json, parse_timestamp, parallel_map
from ..config import GREENHOUSE_BOOTSTRAP

log = logging.getLogger(__name__)

BASE = "https://boards-api.greenhouse.io/v1/boards"


def _fetch_board(slug: str) -> list[dict[str, Any]]:
    url = f"{BASE}/{urllib.parse.quote(slug)}/jobs?content=true"
    try:
        data = fetch_json(url)
    except Exception as exc:
        log.error("Failed to fetch Greenhouse board %s: %s", slug, exc)
        return []
    return data.get("jobs", []) if isinstance(data, dict) else []


def _extract_description(job: dict) -> str:
    content = job.get("content", "")
    if isinstance(content, str):
        return content
    return ""


def _location_str(job: dict) -> str:
    loc = job.get("location", {})
    if isinstance(loc, dict):
        return loc.get("name", "") or ""
    return str(loc)


def normalize(job: dict, slug: str, org_name: str) -> dict[str, Any]:
    desc = _extract_description(job)
    return {
        "title": job.get("title", ""),
        "organization": org_name,
        "category": "jobs",
        "areas": [],
        "region": "",
        "location": _location_str(job),
        "type": _employment_type(job),
        "eligibility": None,
        "official_url": job.get("absolute_url", ""),
        "application_url": job.get("absolute_url", ""),
        "deadline": None,
        "start_date": None,
        "end_date": None,
        "status": "open",
        "recurring": False,
        "series": None,
        "edition": None,
        "remote": None,
        "student_level": None,
        "degree_requirements": None,
        "field_requirements": None,
        "source": f"greenhouse:{slug}",
        "source_id": str(job.get("id", "")),
        "last_verified": None,
        "_description": desc,
        "_updated_at": parse_timestamp(job.get("updated_at")),
    }


def _employment_type(job: dict) -> str:
    dept_names = " ".join(
        d.get("name", "") for d in job.get("departments", []) if isinstance(d, dict)
    )
    lower = dept_names.lower()
    if "intern" in lower:
        return "internship"
    return "full_time"


def fetch_all(bootstrap: list[dict] | None = None) -> list[dict[str, Any]]:
    bootstrap = bootstrap or GREENHOUSE_BOOTSTRAP
    results = []

    def _board(entry):
        slug, name = entry["slug"], entry["name"]
        jobs = _fetch_board(slug)
        log.info("Greenhouse %s: %d jobs", slug, len(jobs))
        return [normalize(job, slug, name) for job in jobs]

    for board_result in parallel_map(_board, bootstrap):
        results.extend(board_result)
    return results
