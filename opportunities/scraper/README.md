# Opportunities scraper

Fetches public job postings from documented ATS APIs, merges curated records, classifies them into Hardware Atlas areas, and writes `../data/opportunities.json`.

Python only, standard library. No dependencies beyond the interpreter.

## Pipeline

```
ATS sources ──▶ normalize ──▶ classify ──▶ deduplicate ──▶ validate ──▶ opportunities.json
```

### Sources

Three ATS adapters, each using the vendor's documented public read API. No authentication required for any of them.

| Source | Endpoint | Docs |
|---|---|---|
| Greenhouse | `boards-api.greenhouse.io/v1/boards/{slug}/jobs` | developers.greenhouse.io/job-board.html |
| Lever | `api.lever.co/v0/postings/{site}?mode=json` | github.com/lever/postings-api |
| Ashby | `api.ashbyhq.com/posting-api/job-board/{board}` | developers.ashbyhq.com |

Company slugs live in `config.py`. Adding a company means adding its ATS slug to the right bootstrap list.

Curated records for scholarships, fellowships, hackathons, and open source programs live in `curated.json` because those programs do not expose reliable public JSON. They carry `"source": "curated"`.

### Fetching

Each board is fetched in parallel (thread pool, no added dependencies) once per company, and vendor-specific fields are converted into the shared normalized record shape. The HTTP helper in `sources/base.py` handles timeouts, a few retries for rate limits, and a stable user agent. One failing company does not sink the run; its error is logged and the rest continue.

### Normalization

`normalize.py` strips HTML out of descriptions, trims fields, drops records missing a title, organization, or official URL, and stamps `last_verified`.

### Classification

`classify.py` contains keyword rules, one readable regex per Hardware Atlas area. A role can match several areas, and the keywords are plain enough for contributors to improve. Category and region are derived the same way.

### Relevance filtering

Raw jobs from a chip company include adjacent roles like recruiters and demand planners whose descriptions merely mention hardware words. `is_hardware_relevant` keeps a record only if the title or team clearly matches an area, or if the description matches an area and the title contains a technical word such as engineer, developer, intern, or scientist. The exact list lives in `TECH_TITLE_RE` in `classify.py`. Tune it there, not in the pipeline.

### Deduplication

`deduplicate.py` uses a stable ID from `source` plus `source_id` where available. Cross-source duplicates are caught with a fuzzy key built from organization, title, location, and URL. Different editions of the same recurring series are never merged.

### Validation

`validate.py` checks required fields, URL format, and allowed values for category, region, and status. Warnings are logged but the run completes; a corrupted record is dropped by earlier stages, not silently published.

### Publication

`main.py` runs the whole pipeline and writes `../data/opportunities.json`. Run it locally with:

```bash
python opportunities/scraper/main.py
```

Offline reproduction (no network):

```bash
python opportunities/scraper/main.py --offline
```

## GitHub Actions

`.github/workflows/update-opportunities.yml` runs the pipeline on a schedule (twice weekly, Monday and Thursday) and on manual dispatch. It installs nothing beyond the standard library, runs the scraper, validates the JSON, runs the test suite, and commits `opportunities.json` only when it differs from the committed copy. No changes, no commit, no push.

## Tests

`tests/` uses fixtures in `tests/fixtures/`, one per ATS. It never hits a live website.

```bash
python -m unittest discover -s opportunities/tests -v
```

Tests cover normalization, classification, deduplication, recurring editions, invalid records, and JSON output shape.

## Additions to consider

These adapters are candidates for later; each is a documented public endpoint but none made the first cut because the companies were not hand-verified:

- SmartRecruiters: `api.smartrecruiters.com/v1/companies/{id}/postings`, public but tier-dependent per company
- Workday APIs require per-company OAuth flow and do not fit a shared-credentialless scraper

The bootstrap lists in `config.py` are deliberately small and hand-verified. A board whose slug no longer resolves is removed or replaced, as happened with the MatX Greenhouse board. Adding a company means reproducing its careers page URL in the config: `boards.greenhouse.io/<slug>`, `jobs.lever.co/<site>`, or `jobs.ashbyhq.com/<board>`.