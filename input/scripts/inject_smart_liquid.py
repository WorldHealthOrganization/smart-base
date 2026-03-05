#!/usr/bin/env python3
"""
Inject '{% include smart.liquid %}' into DAK IG markdown pages.

This script scans all markdown files under input/pagecontent/**/*.md and
ensures that '{% include smart.liquid %}' is present at the top of each file
(after any YAML front-matter block).  The operation is idempotent: if the
include directive is already present anywhere in the file it is not duplicated.

Only runs when dak.json is present in the IG root (DAK IG detection).

Usage:
    python inject_smart_liquid.py [ig_root]

Defaults:
    ig_root = .  (repository root)

Author: SMART Guidelines Team
"""

import os
import re
import stat
import sys
from pathlib import Path
from typing import List, Tuple

# The Liquid include directive to inject
_INCLUDE_DIRECTIVE = "{% include smart.liquid %}"

# Pattern that matches a YAML front-matter block at the very start of a file.
# Front-matter starts with '---' on its own line and ends with '---' or '...'
# on its own line.
_FRONTMATTER_RE = re.compile(
    r'\A(---[ \t]*\r?\n.*?\n(?:---|\.\.\.)[ \t]*\r?\n)',
    re.DOTALL,
)


def _already_has_include(content: str) -> bool:
    """Return True if the include directive is already present in the file."""
    return _INCLUDE_DIRECTIVE in content


def _inject(content: str) -> Tuple[str, bool]:
    """
    Inject _INCLUDE_DIRECTIVE into *content* if not already present.

    Returns (new_content, was_modified).
    Preserves YAML front-matter by inserting the directive after the
    front-matter block (or at the very start if there is none).
    """
    if _already_has_include(content):
        return content, False

    m = _FRONTMATTER_RE.match(content)
    if m:
        frontmatter = m.group(1)
        rest = content[m.end():]
        # Ensure exactly one blank line between the include and the rest
        rest_stripped = rest.lstrip('\n')
        separator = "\n\n" if rest_stripped else "\n"
        new_content = frontmatter + _INCLUDE_DIRECTIVE + separator + rest_stripped
    else:
        new_content = _INCLUDE_DIRECTIVE + "\n\n" + content

    return new_content, True


def find_markdown_files(pagecontent_dir: Path) -> List[Path]:
    """Return a sorted list of all .md files under pagecontent_dir."""
    return sorted(pagecontent_dir.rglob("*.md"))


def process_file(md_path: Path) -> bool:
    """
    Inject the include directive into a single markdown file if needed.
    Returns True if the file was modified, None if the file could not be written.
    """
    content = md_path.read_text(encoding='utf-8')
    new_content, modified = _inject(content)
    if modified:
        # First attempt: write directly (works on most writable files).
        try:
            md_path.write_text(new_content, encoding='utf-8')
        except PermissionError:
            # Fallback: try to temporarily grant owner-write permission.
            # This handles the case where the IG Publisher leaves files
            # read-only but we still own them.
            original_mode = md_path.stat().st_mode
            try:
                os.chmod(md_path, original_mode | stat.S_IWUSR)
            except OSError:
                # We don't own the file and cannot change its permissions;
                # skip it with a warning rather than crashing.
                print(f"  ⚠️  Cannot write (no permission): {md_path}")
                return False
            try:
                md_path.write_text(new_content, encoding='utf-8')
            finally:
                os.chmod(md_path, original_mode)
    return modified


def main() -> int:
    ig_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")

    # DAK IG check
    dak_json_path = ig_root / "dak.json"
    if not dak_json_path.exists():
        print("ℹ️  dak.json not found – this is not a DAK IG. Skipping smart.liquid injection.")
        return 0

    print(f"✅ DAK IG detected (dak.json found at {dak_json_path})")

    pagecontent_dir = ig_root / "input" / "pagecontent"
    if not pagecontent_dir.is_dir():
        print(f"⚠️  pagecontent directory not found: {pagecontent_dir}. Nothing to inject.")
        return 0

    md_files = find_markdown_files(pagecontent_dir)
    print(f"📂 Found {len(md_files)} markdown file(s) in {pagecontent_dir}")

    injected: List[Path] = []
    skipped: List[Path] = []

    for md_path in md_files:
        # Never inject into smart.liquid.md itself (it renders the variables)
        if md_path.name == "smart.liquid.md":
            skipped.append(md_path)
            continue
        modified = process_file(md_path)
        if modified:
            injected.append(md_path)
            print(f"  ✏️  Injected include into: {md_path.relative_to(ig_root)}")
        else:
            skipped.append(md_path)
            print(f"  ✔️  Already has include:    {md_path.relative_to(ig_root)}")

    print(f"\n✅ Injection complete: {len(injected)} file(s) modified, "
          f"{len(skipped)} file(s) already up-to-date.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
