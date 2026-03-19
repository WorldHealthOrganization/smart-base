#!/usr/bin/env python3
"""Inject CI build info (commit SHA + branch) into every HTML page in output/.

Strategy
--------
The IG Publisher (with -auto-ig-build) already generates a ``<div id="publish-box">``
near the top of every page.  This script appends commit and branch information
to that existing box rather than adding a second, separate element.

If the publish-box is not found the script falls back to inserting a new
banner just before ``<div id="segment-content">`` (the main content area),
then to just after ``<body>`` as a last resort.

The injection is idempotent: a previously injected block (identified by the
``smart-ci-extra`` marker attribute) is replaced on re-runs.

Skips
-----
- Non-HTML files
- Files inside asset directories (assets/, css/, js/ …)
- HTML fragments that have no ``<body>`` tag

Environment variables
---------------------
GITHUB_REPOSITORY   ``owner/repo`` — always set by GitHub Actions.
GH_SHA              Full git commit SHA.
BRANCH_NAME         Full branch name (e.g. ``feat/my-feature``).
BRANCH_DIR          Last path component of the branch name.
IS_DEFAULT_BRANCH   ``true`` when building the default branch.
IG_VERSION          IG version; falls back to reading sushi-config.yaml.
"""

import html
import os
import re
import sys
from pathlib import Path

import yaml  # PyYAML — already required by other scripts in this repo


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _read_env(name: str) -> str:
    return os.environ.get(name, "").strip()


def _short_sha(sha: str) -> str:
    return sha[:8] if len(sha) >= 8 else sha


def _read_version(root: Path) -> str:
    """Read IG version from sushi-config.yaml or dak.json."""
    sushi = root / "sushi-config.yaml"
    if sushi.exists():
        try:
            cfg = yaml.safe_load(sushi.read_text(encoding="utf-8"))
            if isinstance(cfg, dict) and cfg.get("version"):
                return str(cfg["version"])
        except Exception:
            pass
    try:
        import json
        dak = root / "dak.json"
        if dak.exists():
            d = json.loads(dak.read_text(encoding="utf-8"))
            if d.get("version"):
                return str(d["version"])
    except Exception:
        pass
    return ""


# ---------------------------------------------------------------------------
# Build the extra-info HTML snippet
# ---------------------------------------------------------------------------

_MARKER_ATTR = 'data-smart-ci-extra="1"'


def _build_extra_html(
    version: str,
    sha: str,
    branch_name: str,
    branch_dir: str,
    repo: str,
    is_default: bool,
) -> str:
    """Return a small <span> (or <p>) with commit SHA and optional branch."""
    parts = []

    if sha and repo:
        short    = html.escape(_short_sha(sha))
        sha_esc  = html.escape(sha)
        repo_esc = html.escape(repo)
        url      = f"https://github.com/{repo_esc}/commit/{sha_esc}"
        parts.append(f'Built from commit <a href="{url}"><code>{short}</code></a>.')
    elif sha:
        parts.append(f'Built from commit <code>{html.escape(_short_sha(sha))}</code>.')

    if not is_default and branch_name and branch_name not in ("main", "master"):
        name_esc = html.escape(branch_name)
        if repo:
            repo_esc  = html.escape(repo)
            bname_url = html.escape(branch_name)
            branch_url = f"https://github.com/{repo_esc}/tree/{bname_url}"
            parts.append(
                f'Branch: <a href="{html.escape(branch_url)}"><code>{name_esc}</code></a>.'
            )
        else:
            parts.append(f'Branch: <code>{name_esc}</code>.')

    if not parts:
        return ""

    inner = " &nbsp; ".join(parts)
    return (
        f'<p {_MARKER_ATTR} style="margin:.4rem 0 0 0;font-size:.9em;">'
        f'{inner}'
        f'</p>'
    )


# ---------------------------------------------------------------------------
# Build a standalone banner (fallback when no publish-box found)
# ---------------------------------------------------------------------------

_BANNER_ID   = "smart-ci-build-banner"
_BANNER_STYLE = (
    "background:#fff3cd;color:#664d03;border-bottom:1px solid #ffda6a;"
    "padding:.5rem 1rem;font-size:.9rem;"
)


def _build_standalone_banner(
    version: str,
    sha: str,
    branch_name: str,
    branch_dir: str,
    repo: str,
    is_default: bool,
) -> str:
    extra = _build_extra_html(version, sha, branch_name, branch_dir, repo, is_default)
    if not extra:
        return ""
    ver_part = f" for version <strong>{html.escape(version)}</strong>" if version else ""
    return (
        f'<div id="{_BANNER_ID}" style="{_BANNER_STYLE}">'
        f'<p style="margin:0;">CI build{ver_part}. {extra.replace(_MARKER_ATTR, "").strip()}</p>'
        f'</div>'
    )


# ---------------------------------------------------------------------------
# Injection helpers
# ---------------------------------------------------------------------------

# Matches the previously injected extra-info paragraph so we can replace it.
_PREV_EXTRA_RE = re.compile(
    r'<p\s+' + re.escape(_MARKER_ATTR) + r'[^>]*>.*?</p>',
    re.DOTALL | re.IGNORECASE,
)

# Matches the previously injected standalone banner.
_PREV_BANNER_RE = re.compile(
    rf'<div\s+id="{re.escape(_BANNER_ID)}"[^>]*>.*?</div>',
    re.DOTALL | re.IGNORECASE,
)

# Matches <div id="publish-box"> … first </div>  (publish-box has no nested divs).
_PUBLISH_BOX_RE = re.compile(
    r'(<div\s[^>]*\bid=["\']publish-box["\'][^>]*>)'   # group 1: opening tag
    r'(.*?)'                                             # group 2: content
    r'(</div>)',                                          # group 3: closing tag
    re.DOTALL | re.IGNORECASE,
)

# Matches the opening of segment-content for the fallback insertion.
_SEGMENT_CONTENT_RE = re.compile(
    r'(<div\s[^>]*\bid=["\']segment-content["\'][^>]*>)',
    re.IGNORECASE,
)

# Final fallback: just after <body …>
_BODY_RE = re.compile(r'(<body[^>]*>)', re.IGNORECASE)


def _remove_previous(content: str) -> str:
    content = _PREV_EXTRA_RE.sub("", content)
    content = _PREV_BANNER_RE.sub("", content)
    return content


def _inject(content: str, extra_html: str, banner_html: str) -> str:
    """Inject build info into *content* using the best available location."""
    content = _remove_previous(content)

    # ── Strategy 1: append extra-info inside the existing publish-box ──────
    m = _PUBLISH_BOX_RE.search(content)
    if m and extra_html:
        new_box = m.group(1) + m.group(2) + "\n" + extra_html + "\n" + m.group(3)
        return content[: m.start()] + new_box + content[m.end() :]

    # ── Strategy 2: insert standalone banner before segment-content ─────────
    if banner_html:
        m2 = _SEGMENT_CONTENT_RE.search(content)
        if m2:
            return content[: m2.start()] + banner_html + "\n" + content[m2.start() :]

    # ── Strategy 3: insert after <body> ─────────────────────────────────────
    if banner_html:
        m3 = _BODY_RE.search(content)
        if m3:
            pos = m3.end()
            return content[:pos] + "\n" + banner_html + "\n" + content[pos:]

    return content  # nothing matched — leave file unchanged


# ---------------------------------------------------------------------------
# File filtering
# ---------------------------------------------------------------------------

_SKIP_DIRS = frozenset({
    "assets", "css", "js", "img", "images",
    "fonts", "scripts", "vendor", "node_modules",
})


def _is_page(path: Path) -> bool:
    if path.suffix.lower() != ".html":
        return False
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
    root       = Path(".")
    output_dir = root / "output"

    if not output_dir.is_dir():
        print(
            "⚠️  output/ not found — skipping banner injection. "
            "Run after the IG Publisher has produced ./output/",
            file=sys.stderr,
        )
        sys.exit(0)

    repo        = _read_env("GITHUB_REPOSITORY")
    sha         = _read_env("GH_SHA")
    branch_name = _read_env("BRANCH_NAME")
    branch_dir  = _read_env("BRANCH_DIR")
    is_default  = _read_env("IS_DEFAULT_BRANCH").lower() == "true"
    version     = _read_env("IG_VERSION") or _read_version(root)

    extra_html  = _build_extra_html(version, sha, branch_name, branch_dir, repo, is_default)
    banner_html = _build_standalone_banner(version, sha, branch_name, branch_dir, repo, is_default)

    if not extra_html and not banner_html:
        print("ℹ️  No build context available (GH_SHA not set?) — skipping banner injection.")
        return

    html_files = sorted(p for p in output_dir.rglob("*.html") if _is_page(p))

    modified = 0
    skipped  = 0
    for path in html_files:
        try:
            original = path.read_text(encoding="utf-8", errors="replace")
            if not _has_body(original):
                skipped += 1
                continue
            updated = _inject(original, extra_html, banner_html)
            if updated != original:
                path.write_text(updated, encoding="utf-8")
                modified += 1
        except Exception as exc:
            print(f"⚠️  Could not process {path}: {exc}", file=sys.stderr)

    total = len(html_files)
    print(
        f"✅ CI build info injected into {modified}/{total} HTML pages "
        f"({skipped} skipped — no <body> tag)."
    )


if __name__ == "__main__":
    main()
