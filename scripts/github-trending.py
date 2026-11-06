#!/usr/bin/env python3
"""Fetch GitHub trending repositories and print formatted output."""

import json
import urllib.request
import urllib.error
import html.parser
import sys
from datetime import datetime, timezone

TRENDING_URL = "https://github.com/trending"
USER_AGENT = "Mozilla/5.0 (Hermes-Secretary/1.0)"


class TrendingParser(html.parser.HTMLParser):
    """Parse GitHub trending page HTML."""

    def __init__(self):
        super().__init__()
        self.repos = []
        # State machine
        self._in_article = False
        self._in_h2 = False
        self._in_repo_link = False
        self._in_desc_p = False
        self._skip_next_desc = False
        # Buffer for accumulating repo name across inner tags
        self._name_parts = []
        self._desc_parts = []
        self._current = {}

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "article":
            if self._repos_finalized():
                return
            self._in_article = True
            self._current = {}
            self._name_parts = []
            self._desc_parts = []
            self._in_h2 = False
            self._in_repo_link = False
            self._in_desc_p = False
            return

        if not self._in_article:
            return

        if tag == "h2":
            self._in_h2 = True
        elif tag == "a" and self._in_h2 and a.get("href", "").count("/") >= 2:
            self._in_repo_link = True
        elif tag == "p" and self._is_description_container():
            self._in_desc_p = True
            self._desc_parts = []
        elif tag == "span" and self._in_article:
            cls = a.get("class", "")
            if "d-inline-block" in cls or ("float-right" in cls):
                self._current["stars_today_area"] = True

    def _is_description_container(self):
        return self._in_article and not self._in_h2 and not self._in_repo_link

    def handle_endtag(self, tag):
        if tag == "article" and self._in_article:
            self._finalize_current()
            self._in_article = False
            return

        if not self._in_article:
            return

        if tag == "h2":
            if self._name_parts:
                self._current["name_raw"] = "".join(self._name_parts).strip()
            self._in_h2 = False
            self._in_repo_link = False
        elif tag == "a":
            self._in_repo_link = False
        elif tag == "p" and self._in_desc_p:
            desc = "".join(self._desc_parts).strip()
            if desc:
                self._current["description"] = desc
            self._in_desc_p = False

    def handle_data(self, data):
        if not self._in_article:
            return
        if self._in_h2 and self._in_repo_link:
            s = data.strip()
            if s:
                self._name_parts.append(s)
        elif self._in_desc_p:
            s = data.strip()
            if s:
                self._desc_parts.append(s)

    def _clean_name(self, raw):
        """Normalize 'owner / repo' or 'owner/repo' to 'owner/repo'."""
        if not raw:
            return ""
        s = raw.replace("\u00a0", " ").strip()
        parts = [p.strip() for p in s.split("/")]
        if len(parts) >= 2 and parts[0] and parts[1]:
            return f"{parts[0]}/{parts[1]}"
        # Try splitting on whitespace
        import re
        m = re.match(r'(\S+)\s*/\s*(\S+)', s)
        if m:
            return f"{m.group(1)}/{m.group(2)}"
        return s

    def _finalize_current(self):
        raw = self._current.get("name_raw", "")
        name = self._clean_name(raw)
        if not name or "/" not in name:
            return
        self._current["name"] = name
        if "description" not in self._current:
            self._current["description"] = ""
        self.repos.append(self._current)

    def _repos_finalized(self):
        return False


def fetch_trending(language="", since="daily"):
    url = TRENDING_URL
    params = []
    if language:
        url += f"/{language}"
    if since:
        params.append(("since", since))
    if params:
        url += "?" + "&".join(f"{k}={v}" for k, v in params)

    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            html_data = resp.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        print(f"HTTP error {e.code}: {e.reason}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"URL error: {e.reason}", file=sys.stderr)
        sys.exit(1)

    parser = TrendingParser()
    parser.feed(html_data)
    return parser.repos


def format_output(repos, since="daily"):
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        f"# GitHub Trending ({since})",
        f"Fetched: {now}",
        "",
    ]
    if not repos:
        lines.append("_No repositories found. GitHub may have changed its page structure._")
        lines.append("")
        return "\n".join(lines)

    for i, repo in enumerate(repos, 1):
        name = repo.get("name", "unknown/unknown")
        desc = repo.get("description", "") or ""
        lines.append(f"## {i}. {name}")
        if desc:
            lines.append(f"   {desc}")
        lines.append(f"   https://github.com/{name}")
        lines.append("")

    return "\n".join(lines)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Fetch GitHub trending repositories")
    parser.add_argument("--language", "-l", default="", help="Language filter")
    parser.add_argument(
        "--since", "-s", default="daily", choices=["daily", "weekly", "monthly"],
        help="Time range"
    )
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    repos = fetch_trending(args.language, args.since)

    if args.json:
        print(json.dumps(repos, indent=2))
    else:
        print(format_output(repos, args.since))
