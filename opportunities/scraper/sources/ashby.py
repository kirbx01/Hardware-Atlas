"""
Ashby Job Board adapter.
Docs: https://developers.ashbyhq.com/docs/public-job-posting-api
Public GET: https://api.ashbyhq.com/posting-api/job-board/{board_name}
No auth required.
"""
import logging
import urllib.parse
from typing import Any

from .base import fetch_json, parallel_map
from ..config import ASHBY_BOOTSTRAP

log = logging.getLogger(__name__)

BASE = "https://api.ashbyhq.com/posting-api/job-board"


def _fetch_board(slug: str) -> list[dict[str, Any]]:
    url = f"{BASE}/{urllib.parse.quote(slug)}"
    try:
        data = fetch_json(url, params={"includeCompensation": "true"})
    except Exception as exc:
        log.error("Failed to fetch Ashby board %s: %s", slug, exc)
        return []
    if not isinstance(data, dict):
        return []
    return data.get("jobs", [])


def normalize(job: dict, slug: str, org_name: str) -> dict[str, Any]:
    is_remote = job.get("isRemote", False)
    workplace = job.get("workplaceType", "") or ""
    location = job.get("location", "") or ""
    emp_type = (job.get("employmentType") or "").lower()

    etype = "full_time"
    if "intern" in emp_type:
        etype = "internship"
    elif "contract" in emp_type:
        etype = "contract"
    elif "temporary" in emp_type:
        etype = "contract"

    url = job.get("jobUrl") or job.get("applyUrl") or ""
    return {
        "title": job.get("title", ""),
        "organization": org_name,
        "category": "jobs",
        "areas": [],
        "region": "",
        "location": location,
        "type": etype,
        "eligibility": None,
        "official_url": url,
        "application_url": job.get("applyUrl") or url,
        "deadline": None,
        "start_date": None,
        "end_date": None,
        "status": "open",
        "recurring": False,
        "series": None,
        "edition": None,
        "remote": is_remote if isinstance(is_remote, bool) else None,
        "student_level": None,
        "degree_requirements": None,
        "field_requirements": None,
        "source": f"ashby:{slug}",
        "source_id": url.rsplit("/", 1)[-1] if "/" in url else "",
        "last_verified": None,
        "_description": job.get("descriptionPlain", "") or job.get("descriptionHtml", "") or "",
        "_updated_at": job.get("publishedAt"),
    }


def fetch_all(bootstrap: list[dict] | None = None) -> list[dict[str, Any]]:
    bootstrap = bootstrap or ASHBY_BOOTSTRAP
    results = []

    def _board(entry):
        slug, name = entry["slug"], entry["name"]
        jobs = _fetch_board(slug)
        log.info("Ashby %s: %d jobs", slug, len(jobs))
        return [
            normalize(job, slug, name)
            for job in jobs
            if job.get("isListed", True)
        ]

    for board_result in parallel_map(_board, bootstrap):
        results.extend(board_result)
    return results
