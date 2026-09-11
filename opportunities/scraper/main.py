#!/usr/bin/env python3
"""
Hardware Atlas opportunity scraper.

Usage:
    python -m opportunities.scraper.main [--output FILE] [--offline]

Fetches published job postings from public ATS APIs, classifies them
into Hardware Atlas areas, and writes the combined list to a JSON file.
"""
import argparse
import json
import logging
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT.parent))

from opportunities.scraper.normalize import normalize_all
from opportunities.scraper.classify import classify_all, is_hardware_relevant
from opportunities.scraper.deduplicate import deduplicate
from opportunities.scraper.validate import validate
from opportunities.scraper.sources import greenhouse, lever, ashby

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
log = logging.getLogger(__name__)

DEFAULT_OUTPUT = ROOT / "data" / "opportunities.json"


def _load_curated() -> list[dict]:
    curated_path = ROOT / "scraper" / "curated.json"
    if not curated_path.exists():
        return []
    with open(curated_path) as f:
        return json.load(f)


def fetch_all() -> list[dict]:
    records = []
    records.extend(greenhouse.fetch_all())
    records.extend(lever.fetch_all())
    records.extend(ashby.fetch_all())
    return records


def pipeline(records: list[dict]) -> dict:
    normalized = normalize_all(records)
    classified = classify_all(normalized)
    hardware_only = [r for r in classified if is_hardware_relevant(r)]
    deduped = deduplicate(hardware_only)
    errors = validate(deduped)
    if errors:
        for e in errors[:20]:
            log.warning("Validation: %s", e)
        if len(errors) > 20:
            log.warning("... and %d more validation warnings", len(errors) - 20)

    final = []
    for rec in deduped:
        rec.pop("_text", None)
        rec.pop("_team", None)
        rec.pop("_updated_at", None)
        rec.pop("_id", None)
        final.append(rec)

    return {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "opportunity_count": len(final),
        "opportunities": final,
    }


def main():
    parser = argparse.ArgumentParser(description="Hardware Atlas opportunity scraper")
    parser.add_argument("--output", "-o", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--offline", action="store_true")
    parser.add_argument("--no-render", action="store_true")
    args = parser.parse_args()

    log.info("Fetching opportunities from ATS sources...")
    if args.offline:
        log.info("Offline mode: loading cached data only")
        curated = _load_curated()
        cached_path = ROOT / "data" / "opportunities.json"
        if cached_path.exists():
            with open(cached_path) as f:
                existing = json.load(f)
            records = existing.get("opportunities", [])
        else:
            records = []
        records.extend(curated)
    else:
        records = fetch_all()
        records.extend(_load_curated())

    log.info("Raw records before pipeline: %d", len(records))
    result = pipeline(records)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    log.info("Wrote %d opportunities to %s", result["opportunity_count"], output_path)

    if not args.no_render:
        try:
            from opportunities.scraper.render import render_from_json
            repo_root = ROOT.parent
            render_from_json(output_path, repo_root / "README.md")
        except Exception as exc:
            log.error("Failed to render README: %s", exc)


if __name__ == "__main__":
    main()
