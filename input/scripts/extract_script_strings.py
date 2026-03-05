#!/usr/bin/env python3
"""
extract_script_strings.py — Extract translatable strings from Python scripts.

Scans all Python source files under input/scripts/ (and optionally any
user-specified directory) for gettext-marked strings (_(), gettext(),
ngettext()) using Babel's extraction machinery, and writes a Gettext .pot
file to input/scripts/translations/scripts.pot.

This .pot file is then picked up by the translation pipeline as a component
named "scripts-scripts".

Usage:
    python extract_script_strings.py [--scripts-dir DIR]
                                     [--output FILE]
                                     [--canonical-url URL]

Exit codes:
    0  .pot file written (even if 0 strings found)
    1  Fatal error
"""

import argparse
import datetime
import logging
import sys
from pathlib import Path
from typing import List, Optional

try:
    from babel.messages.extract import extract_from_dir, DEFAULT_MAPPING
    from babel.messages.pofile import write_po
    from babel.messages.catalog import Catalog
except ImportError:
    sys.exit(
        "ERROR: 'babel' package is required.\n"
        "  Install with: pip install Babel>=2.10.0"
    )

logger = logging.getLogger(__name__)

# Extraction method map — Python files only
_EXTRACTION_MAP = [("**.py", "python")]

# Keywords recognised as i18n markers
_KEYWORDS = {
    "_": None,
    "gettext": None,
    "ngettext": (1, 2),
    "ugettext": None,
    "pgettext": ((1, "c"), 2),
    "npgettext": ((1, "c"), 2, 3),
}


def extract_po_template(
    scripts_dir: Path,
    output_path: Path,
    canonical_url: str = "",
    project: str = "SMART Base Scripts",
    version: str = "0.1",
) -> int:
    """
    Extract all _()-marked strings from Python files under *scripts_dir*
    and write them to *output_path* as a Gettext .pot file.

    Returns 0 on success, 1 on error.
    """
    if not scripts_dir.is_dir():
        logger.error("Scripts directory %s does not exist", scripts_dir)
        return 1

    catalog = Catalog(
        project=project,
        version=version,
        copyright_holder="WHO",
        charset="utf-8",
    )

    # Extract messages
    count = 0
    for filename, lineno, message, comments, context in extract_from_dir(
        str(scripts_dir),
        method_map=_EXTRACTION_MAP,
        keywords=_KEYWORDS,
        comment_tags=("NOTE:", "TRANSLATORS:"),
        strip_comment_tags=True,
        options_map=None,
    ):
        locations = [(filename, lineno)]
        auto_comments: List[str] = list(comments)
        if canonical_url:
            auto_comments.append(f"URL: {canonical_url}")
        catalog.add(
            message,
            string="",
            locations=locations,
            auto_comments=auto_comments,
            context=context or None,
        )
        count += 1

    logger.info("Extracted %d message(s) from %s", count, scripts_dir)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("wb") as fh:
        write_po(fh, catalog, include_lineno=True, sort_by_file=True)

    logger.info("Written .pot file to %s", output_path)
    return 0


def _parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="extract_script_strings.py",
        description="Extract translatable strings from Python scripts into a .pot file",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--scripts-dir",
        default="input/scripts",
        help="Directory containing Python scripts (default: input/scripts)",
    )
    parser.add_argument(
        "--output",
        default="input/scripts/translations/scripts.pot",
        help="Output .pot file path (default: input/scripts/translations/scripts.pot)",
    )
    parser.add_argument(
        "--canonical-url",
        default="",
        help="IG canonical base URL for context comments",
    )
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Repository root directory (default: .)",
    )
    return parser.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> int:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%H:%M:%S",
    )
    args = _parse_args(argv)

    repo_root = Path(args.repo_root).resolve()
    scripts_dir = (repo_root / args.scripts_dir).resolve()
    output_path = Path(args.output)
    if not output_path.is_absolute():
        output_path = repo_root / output_path

    return extract_po_template(
        scripts_dir=scripts_dir,
        output_path=output_path,
        canonical_url=args.canonical_url,
    )


if __name__ == "__main__":
    sys.exit(main())
