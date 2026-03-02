#!/usr/bin/env python3
"""
Stamp deployment metadata into an HTML file's <head> section.

Each call adds one <meta name="deploy-log"> tag recording a named step
(e.g. checkout, ig-build, postprocessing, pre-deploy) together with the
commit SHA, branch and timestamp.  Tags accumulate across builds: on the
first call per build pass --prev-html to carry forward entries from the
previously deployed file.

Usage:
    python stamp_deploy_metadata.py <html_file> \\
        --step <step_name> \\
        --commit <full_commit_sha> \\
        --branch <branch_name> \\
        [--timestamp <iso8601>]  \\   # defaults to UTC now
        [--prev-html <path>]          # previous deployment's index.html

Meta tag format:
    <meta name="deploy-log"
          content="step=<step>; commit=<short_sha>; branch=<branch>; ts=<iso8601>">
"""

import argparse
import os
import re
import sys
from datetime import datetime, timezone


# ── helpers ───────────────────────────────────────────────────────────────────

_TAG_RE = re.compile(
    r'<meta\s+name="deploy-log"\s+content="[^"]*"\s*/?>',
    re.IGNORECASE,
)

_BLOCK_RE = re.compile(
    r'[ \t]*<!-- deploy-log-start -->.*?<!-- deploy-log-end -->\n?',
    re.DOTALL | re.IGNORECASE,
)


def extract_log_tags(html: str) -> list:
    """Return all deploy-log meta tags found in *html* (in document order)."""
    return _TAG_RE.findall(html)


def _sanitise(value: str) -> str:
    """Strip characters that would break the meta content attribute value."""
    return re.sub(r'[;"<>]', '', value)


def build_meta_tag(step: str, commit_sha: str, branch: str, ts: str) -> str:
    short = commit_sha[:8] if len(commit_sha) >= 8 else commit_sha
    return (
        '<meta name="deploy-log" content="'
        f'step={_sanitise(step)}; '
        f'commit={short}; '
        f'branch={_sanitise(branch)}; '
        f'ts={_sanitise(ts)}">'
    )


# ── injection ─────────────────────────────────────────────────────────────────

def inject(html_file: str, new_tag: str, prev_html: str | None = None) -> None:
    """
    Read *html_file*, remove any existing deploy-log block, then re-insert
    a block containing:
      - entries from *prev_html* that are not already in *html_file*
      - entries already in *html_file*  (current build's earlier stamps)
      - *new_tag*
    Write the result back to *html_file*.
    """
    with open(html_file, 'r', encoding='utf-8') as fh:
        content = fh.read()

    current_tags = extract_log_tags(content)

    prev_tags: list[str] = []
    if prev_html and os.path.exists(prev_html):
        try:
            with open(prev_html, 'r', encoding='utf-8') as fh:
                prev_tags = extract_log_tags(fh.read())
            print(f"Preserved {len(prev_tags)} deploy-log entries from previous build")
        except Exception as exc:
            print(f"Warning: could not read previous HTML ({prev_html}): {exc}",
                  file=sys.stderr)

    # Ordered, deduplicated: prev history → current build steps → new step
    seen: set[str] = set()
    all_tags: list[str] = []
    for tag in prev_tags + current_tags + [new_tag]:
        if tag not in seen:
            seen.add(tag)
            all_tags.append(tag)

    # Remove old block (and any stray tags not wrapped in it)
    content = _BLOCK_RE.sub('', content)
    content = re.sub(r'[ \t]*<meta\s+name="deploy-log"[^>]*>\n?', '',
                     content, flags=re.IGNORECASE)

    # Build the new block
    indent = '    '
    lines = [f'{indent}<!-- deploy-log-start -->']
    for tag in all_tags:
        lines.append(f'{indent}{tag}')
    lines.append(f'{indent}<!-- deploy-log-end -->')
    block = '\n'.join(lines) + '\n'

    # Insert just before </head>
    m = re.search(r'([ \t]*</head>)', content, re.IGNORECASE)
    if m:
        pos = m.start()
        content = content[:pos] + block + content[pos:]
    else:
        content += '\n' + block

    with open(html_file, 'w', encoding='utf-8') as fh:
        fh.write(content)


# ── CLI ───────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description='Stamp a deployment-step entry into an HTML file <head>.'
    )
    parser.add_argument('html_file', help='Path to the HTML file (e.g. output/index.html)')
    parser.add_argument('--step',      required=True,
                        help='Step name, e.g. checkout, ig-build, postprocessing, pre-deploy')
    parser.add_argument('--commit',    required=True, help='Full git commit SHA')
    parser.add_argument('--branch',    required=True, help='Branch / BRANCH_DIR value')
    parser.add_argument('--timestamp', default=None,
                        help='ISO-8601 UTC timestamp; omit to use current time')
    parser.add_argument('--prev-html', default=None, dest='prev_html',
                        help='Previously deployed index.html (for cross-build log accumulation)')
    args = parser.parse_args()

    if not os.path.exists(args.html_file):
        print(f"Note: {args.html_file} not found – skipping stamp (IG build may have failed)",
              file=sys.stderr)
        sys.exit(0)

    ts = args.timestamp or datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    tag = build_meta_tag(args.step, args.commit, args.branch, ts)

    try:
        inject(args.html_file, tag, args.prev_html)
        print(f"Stamped: {tag}")
    except Exception as exc:
        print(f"Error stamping deploy metadata: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
