"""
Shared HTTP fetcher for ATS source adapters.
"""
import json
import logging
import urllib.error
import urllib.request
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any, Callable, Optional

log = logging.getLogger(__name__)

DEFAULT_TIMEOUT = 15
RETRY_ATTEMPTS = 2
RETRY_DELAY = 1.0
USER_AGENT = "HardwareAtlas-OpportunityBot/1.0 (https://github.com/kirbx01/Hardware-Atlas)"


def fetch_json(
    url: str,
    *,
    params: Optional[dict[str, str]] = None,
    timeout: int = DEFAULT_TIMEOUT,
    header_override: Optional[dict[str, str]] = None,
) -> Any:
    if params:
        qs = "&".join(f"{k}={v}" for k, v in params.items())
        url = f"{url}?{qs}"
    headers = {"User-Agent": USER_AGENT, "Accept": "application/json"}
    if header_override:
        headers.update(header_override)
    req = urllib.request.Request(url, headers=headers)
    for attempt in range(RETRY_ATTEMPTS):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            if exc.code == 429 and attempt < RETRY_ATTEMPTS - 1:
                log.warning("Rate limited on %s, retrying in %.1fs", url, RETRY_DELAY)
                time.sleep(RETRY_DELAY * (attempt + 1))
                continue
            log.error("HTTP %d fetching %s", exc.code, url)
            raise
        except urllib.error.URLError as exc:
            log.error("Network error fetching %s: %s", url, exc.reason)
            raise
    return None


def parse_timestamp(ts) -> Optional[str]:
    if not ts:
        return None
    if isinstance(ts, (int, float)):
        try:
            import datetime as _dt
            return _dt.datetime.fromtimestamp(ts / 1000, tz=_dt.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
        except (OSError, ValueError):
            return None
    if isinstance(ts, str):
        return ts.rstrip("Z").rstrip("+00:00")[:19] + "Z"
    return None


def parallel_map(fn: Callable, items: list, max_workers: int = 4) -> list:
    """Run fn over items in parallel, preserving input order of results."""
    if len(items) <= 1:
        return [fn(item) for item in items]
    results: dict[int, Any] = {}
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = {pool.submit(fn, item): idx for idx, item in enumerate(items)}
        for future in as_completed(futures):
            results[futures[future]] = future.result()
    return [results[i] for i in range(len(items))]
