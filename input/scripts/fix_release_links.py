#!/usr/bin/env python3
"""Fix hardcoded GitHub release links in IG Publisher HTML output.

The downloads.md template contains hardcoded release links pointing to
WorldHealthOrganization/smart-base.  When downstream IGs build using the
shared ghbuild.yml workflow, these links need to point to the actual
repository instead.

This postprocessing script scans output/*.html and replaces any
hardcoded smart-base release URLs with the correct repository URL
derived from the GITHUB_REPOSITORY environment variable.

Environment variables
---------------------
GITHUB_REPOSITORY   ``owner/repo`` — set automatically by GitHub Actions.

Usage:
    python3 fix_release_links.py [output_dir]
"""

import os
import re
import sys
from pathlib import Path

# The hardcoded base URL pattern to replace (owner/repo part only)
_DEFAULT_REPO = "WorldHealthOrganization/smart-base"


def fix_release_links(output_dir: Path, actual_repo: str) -> int:
    """Replace hardcoded smart-base release URLs with the actual repo.

    Returns the number of files modified.
    """
    if actual_repo == _DEFAULT_REPO:
        print(f"ℹ️  Building {_DEFAULT_REPO} itself — no link replacement needed.")
        return 0

    if not output_dir.is_dir():
        print(f"⚠️  Output directory not found: {output_dir}")
        return 0

    # Pattern matches GitHub URLs containing the hardcoded repo
    pattern = re.compile(
        re.escape(f"https://github.com/{_DEFAULT_REPO}")
    )
    replacement = f"https://github.com/{actual_repo}"

    html_files = sorted(output_dir.rglob("*.html"))
    modified = 0

    for path in html_files:
        try:
            content = path.read_text(encoding="utf-8", errors="replace")
            new_content = pattern.sub(replacement, content)
            if new_content != content:
                path.write_text(new_content, encoding="utf-8")
                modified += 1
        except Exception as exc:
            print(f"⚠️  Could not process {path}: {exc}", file=sys.stderr)

    return modified


def main() -> int:
    output_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("output")
    repo = os.environ.get("GITHUB_REPOSITORY", "").strip()

    if not repo:
        print("ℹ️  GITHUB_REPOSITORY not set — skipping release link replacement.")
        return 0

    modified = fix_release_links(output_dir, repo)
    print(f"✅ Release links: replaced smart-base URLs in {modified} file(s) "
          f"with {repo}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
