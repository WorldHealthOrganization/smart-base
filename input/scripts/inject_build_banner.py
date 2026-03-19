#!/usr/bin/env python3
"""Inject a CI build info banner into every HTML page in output/.

The banner appears near the top of each page and shows:
  - That this is the continuous CI build (not the published version)
  - The IG version number
  - The short git commit SHA (linked to GitHub)
  - The feature branch name, when building a non-default branch

The script is idempotent: it will not double-inject a banner it already added.
It skips non-page files (assets, CSS, JS, images, etc.).

Environment variables
---------------------
GITHUB_REPOSITORY   ``owner/repo`` — always set by GitHub Actions.
GH_SHA              Full git commit SHA.
BRANCH_NAME         Full branch name (e.g. ``feat/my-feature``).
BRANCH_DIR          Last path component of the branch (used as the directory name).
IS_DEFAULT_BRANCH   ``true`` when building the default branch.
IG_VERSION          IG version string; falls back to reading sushi-config.yaml.
"""

import html
import os
import re
import sys
from pathlib import Path

import yaml  # PyYAML — already required by other scripts


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _read_env(name: str) -> str:
    return os.environ.get(name, "").strip()


def _short_sha(sha: str) -> str:
    return sha[:8] if len(sha) >= 8 else sha


def _read_version(root: Path) -> str:
    """Read the IG version from sushi-config.yaml or dak.json."""
    sushi = root / "sushi-config.yaml"
    if sushi.exists():
        try:
            cfg = yaml.safe_load(sushi.read_text(encoding="utf-8"))
            if isinstance(cfg, dict) and cfg.get("version"):
                return str(cfg["version"])
        except Exception:
            pass
    dak = root / "dak.json"
    if dak.exists():
        try:
            import json
            d = json.loads(dak.read_text(encoding="utf-8"))
            if d.get("version"):
                return str(d["version"])
        except Exception:
            pass
    return ""


# ---------------------------------------------------------------------------
# Banner HTML
# ---------------------------------------------------------------------------

_BANNER_ID = "smart-ci-build-banner"

_BANNER_STYLE = (
    "background:#fff3cd;color:#664d03;border:1px solid #ffda6a;"
    "padding:.5rem 1rem;margin:0;font-size:.9rem;"
    "display:flex;align-items:center;flex-wrap:wrap;gap:.35rem;"
)

_COMMIT_LINK_STYLE = "color:#664d03;font-weight:bold;"


def _build_banner_html(
    version: str,
    sha: str,
    branch_name: str,
    branch_dir: str,
    repo: str,
    is_default: bool,
) -> str:
    """Return the full banner <div> HTML string."""
    parts = []

    # Version line
    if version:
        ver_esc = html.escape(version)
        parts.append(
            f"This is the continuous&nbsp;CI&nbsp;build for version&nbsp;<strong>{ver_esc}</strong>."
        )
    else:
        parts.append("This is the continuous&nbsp;CI&nbsp;build.")

    # Commit link
    if sha and repo:
        short = html.escape(_short_sha(sha))
        sha_esc = html.escape(sha)
        repo_esc = html.escape(repo)
        commit_url = f"https://github.com/{repo_esc}/commit/{sha_esc}"
        parts.append(
            f'Built from commit&nbsp;<a href="{commit_url}" style="{_COMMIT_LINK_STYLE}">'
            f"<code>{short}</code></a>."
        )
    elif sha:
        short = html.escape(_short_sha(sha))
        parts.append(f"Built from commit&nbsp;<code>{short}</code>.")

    # Branch info (for feature branches only)
    if not is_default and branch_name and branch_name not in ("main", "master"):
        name_esc = html.escape(branch_name)
        branch_url = ""
        if repo:
            repo_esc = html.escape(repo)
            dir_esc = html.escape(branch_dir or branch_name.split("/")[-1])
            branch_url = (
                f"https://github.com/{repo_esc}/tree/{html.escape(branch_name)}"
            )
        if branch_url:
            parts.append(
                f'Feature branch:&nbsp;<a href="{html.escape(branch_url)}" '
                f'style="{_COMMIT_LINK_STYLE}"><code>{name_esc}</code></a>.'
            )
        else:
            parts.append(f"Feature branch:&nbsp;<code>{name_esc}</code>.")

    inner = " ".join(parts)
    return (
        f'<div id="{_BANNER_ID}" style="{_BANNER_STYLE}">'
        f"{inner}"
        f"</div>"
    )


# ---------------------------------------------------------------------------
# HTML injection
# ---------------------------------------------------------------------------

# Matches a previously injected banner so we can replace it on re-runs.
_EXISTING_BANNER_RE = re.compile(
    rf'<div\s+id="{re.escape(_BANNER_ID)}"[^>]*>.*?</div>',
    re.DOTALL | re.IGNORECASE,
)

# Candidate insertion points, tried in order.
_INSERT_AFTER_PATTERNS = [
    # After the IG Publisher's own CI-build notice (if present)
    re.compile(r'(<p\s+id="publish-box"[^>]*>.*?</p>)', re.DOTALL | re.IGNORECASE),
    re.compile(r'(<div\s+[^>]*class="[^"]*hl7-igpack-notice[^"]*"[^>]*>.*?</div>)',
               re.DOTALL | re.IGNORECASE),
    # Before the main content container
    re.compile(r'(<div\s+id="segment-content"[^>]*>)', re.IGNORECASE),
    # Generic fallback: just after <body>
    re.compile(r'(<body[^>]*>)', re.IGNORECASE),
]


def _inject_banner(content: str, banner: str) -> str:
    """Return *content* with *banner* injected at the best available location."""
    # Remove any previously injected banner first
    content = _EXISTING_BANNER_RE.sub("", content, count=1)

    for pattern in _INSERT_AFTER_PATTERNS:
        m = pattern.search(content)
        if m:
            pos = m.end()
            return content[:pos] + "\n" + banner + "\n" + content[pos:]

    # Absolute fallback: prepend before </body>
    end_body = re.search(r'</body>', content, re.IGNORECASE)
    if end_body:
        pos = end_body.start()
        return content[:pos] + banner + "\n" + content[pos:]

    return content  # give up if no reasonable location found


# ---------------------------------------------------------------------------
# File filtering
# ---------------------------------------------------------------------------

# Subdirectory names under output/ that contain non-page files.
_SKIP_DIRS = frozenset({
    "assets", "css", "js", "img", "images", "fonts",
    "scripts", "vendor", "node_modules",
})

# File names that are not standalone IG pages.
_SKIP_FILES = frozenset({
    "searchindex.js", "searchindex.json",
})


def _is_page(path: Path) -> bool:
    """Return True if *path* looks like an IG content page."""
    if path.suffix.lower() != ".html":
        return False
    if path.name in _SKIP_FILES:
        return False
    # Skip files inside known asset directories
    for part in path.parts:
        if part in _SKIP_DIRS:
            return False
    return True


def _has_body(content: str) -> bool:
    return bool(re.search(r"<body", content, re.IGNORECASE))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    root = Path(".")
    output_dir = root / "output"

    if not output_dir.is_dir():
        print(
            "⚠️  output/ directory not found — skipping banner injection.\n"
            "    Run this script after the IG Publisher has produced ./output/",
            file=sys.stderr,
        )
        sys.exit(0)

    repo = _read_env("GITHUB_REPOSITORY")
    sha = _read_env("GH_SHA")
    branch_name = _read_env("BRANCH_NAME")
    branch_dir = _read_env("BRANCH_DIR")
    is_default = _read_env("IS_DEFAULT_BRANCH").lower() == "true"

    # Read version from sushi-config.yaml / dak.json
    version = _read_env("IG_VERSION") or _read_version(root)

    banner = _build_banner_html(version, sha, branch_name, branch_dir, repo, is_default)

    html_files = [p for p in output_dir.rglob("*.html") if _is_page(p)]
    html_files.sort()

    modified = 0
    skipped = 0
    for path in html_files:
        try:
            original = path.read_text(encoding="utf-8", errors="replace")
            if not _has_body(original):
                skipped += 1
                continue
            updated = _inject_banner(original, banner)
            if updated != original:
                path.write_text(updated, encoding="utf-8")
                modified += 1
        except Exception as exc:
            print(f"⚠️  Could not process {path}: {exc}", file=sys.stderr)

    total = len(html_files)
    print(
        f"✅ CI build banner injected into {modified}/{total} HTML pages "
        f"({skipped} non-page files skipped)."
    )


if __name__ == "__main__":
    main()
