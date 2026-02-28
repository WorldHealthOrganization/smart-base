#!/usr/bin/env python3
"""
WHO SMART Guidelines — Translated Image Reference Updater

After the FHIR IG Publisher runs it creates language-specific HTML pages
(e.g. output/fr/index.html) by mirroring translated narrative pages from
input/pages/<lang>/.  Those HTML pages still reference images using the
same paths as the English pages, e.g.:

    <img src="../diagram1.svg">   ← English version

inject_translations.py placed translated diagram copies under the language
sub-directory of each source type, and the IG Publisher (or a preceding copy
step) made those available at:

    output/<lang>/diagram1.svg   ← translated version

This script performs a final postprocessing pass over every translated HTML
page and rewrites image/source/object references so that, when a translated
version of an image exists in the same language output directory, the
reference is updated to point to it.

If no translated version exists the reference is left unchanged so the page
gracefully falls back to the English image.

Affected reference attributes:
  - <img src="...">
  - <source src="..."> / <source srcset="...">
  - <object data="...">
  - SVG <image href="..."> / <image xlink:href="...">

Usage:
    python update_translated_image_refs.py [options]

Options:
    --output-dir DIR     IG Publisher output directory (default: output)
    --ig-root DIR        Repository root (default: current directory)
    --dry-run            Show changes without writing files
    --lang LANG          Only process a specific language (e.g. fr)
    --help / -h          Print this help

Author: WHO SMART Guidelines Team
"""

import argparse
import logging
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

# ---------------------------------------------------------------------------
# Optional lxml import for robust HTML parsing (graceful fallback omitted
# because lxml is already a declared dependency in requirements.txt).
# ---------------------------------------------------------------------------
try:
    import lxml.etree as ET
    from lxml import html as lxml_html
    _HAVE_LXML = True
except ImportError:  # pragma: no cover
    _HAVE_LXML = False


# ---------------------------------------------------------------------------
# Image-bearing HTML attributes we rewrite
# ---------------------------------------------------------------------------

# (tag_name_or_None, attribute_name)
# None for tag_name means "any tag".
_IMAGE_ATTRS: List[Tuple[Optional[str], str]] = [
    ("img",    "src"),
    ("source", "src"),
    ("source", "srcset"),   # srcset may contain multiple URLs; handled separately
    ("object", "data"),
    ("image",  "href"),                  # SVG <image>
    ("image",  "{http://www.w3.org/1999/xlink}href"),  # SVG xlink:href
]

# Image file extensions we care about
_IMAGE_EXTENSIONS: Set[str] = {
    ".svg", ".png", ".jpg", ".jpeg", ".gif", ".webp",
}

# BCP-47 language codes for the six UN languages plus common variants.
# We use this to recognise language sub-directories in the output tree.
_KNOWN_LANG_CODES: Set[str] = {
    "ar", "zh", "en", "fr", "ru", "es",
    "ar-SA", "zh-CN", "zh-TW", "fr-FR", "es-ES", "ru-RU",
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _is_image_path(path: str) -> bool:
    """Return True if the path looks like a diagram / image file."""
    return Path(path).suffix.lower() in _IMAGE_EXTENSIONS


def _resolve_ref(ref: str, page_path: Path, output_root: Path) -> Optional[Path]:
    """
    Resolve an image reference found in an HTML page to an absolute filesystem
    path inside the output directory.

    Returns None if the reference is external (http/https/data) or cannot
    be resolved within the output tree.
    """
    ref = ref.strip()
    if not ref or ref.startswith(("http://", "https://", "data:", "//")):
        return None
    if ref.startswith("/"):
        # Absolute path relative to site root — resolve against output_root
        candidate = output_root / ref.lstrip("/")
    else:
        candidate = page_path.parent / ref
    try:
        resolved = candidate.resolve()
        output_resolved = output_root.resolve()
        # Only accept paths inside the output tree
        resolved.relative_to(output_resolved)
        return resolved
    except (ValueError, OSError):
        return None


def _find_translated_image(
    original_resolved: Path,
    lang_dir: Path,
    output_root: Path,
) -> Optional[Path]:
    """
    Given the resolved path of an image reference, look for a translated
    version in the language output directory.

    We match by filename only (basename), so
      output/diagram1.svg  →  output/fr/diagram1.svg
    """
    basename = original_resolved.name
    candidate = lang_dir / basename
    if candidate.exists():
        return candidate
    return None


def _make_relative_ref(target: Path, page_path: Path) -> str:
    """Compute a relative URL from an HTML page to a target file."""
    try:
        return os.path.relpath(str(target), str(page_path.parent))
    except ValueError:
        # On Windows, relpath can fail across drives; fall back to basename.
        return target.name


def _rewrite_srcset(srcset: str, lang_dir: Path, page_path: Path, output_root: Path) -> Tuple[str, bool]:
    """
    Rewrite a srcset attribute value, replacing each URL that has a
    translated version with the translated path.

    Returns (new_srcset, changed).
    """
    parts = [p.strip() for p in srcset.split(",") if p.strip()]
    changed = False
    new_parts = []
    for part in parts:
        tokens = part.split()
        if not tokens:
            new_parts.append(part)
            continue
        url = tokens[0]
        descriptor = " ".join(tokens[1:])
        if _is_image_path(url):
            resolved = _resolve_ref(url, page_path, output_root)
            if resolved:
                translated = _find_translated_image(resolved, lang_dir, output_root)
                if translated:
                    new_url = _make_relative_ref(translated, page_path)
                    url = new_url
                    changed = True
        new_parts.append((url + " " + descriptor).strip() if descriptor else url)
    return ", ".join(new_parts), changed


# ---------------------------------------------------------------------------
# Core per-file processing
# ---------------------------------------------------------------------------

def process_html_file(
    html_path: Path,
    lang_dir: Path,
    output_root: Path,
    dry_run: bool,
    logger: logging.Logger,
) -> int:
    """
    Rewrite image references in a single translated HTML file.

    Returns the number of references updated.
    """
    if not _HAVE_LXML:
        logger.error("lxml is required for HTML processing. Install with: pip install lxml")
        return 0

    try:
        with open(html_path, "rb") as fh:
            raw = fh.read()
    except OSError as exc:
        logger.warning(f"Cannot read {html_path}: {exc}")
        return 0

    try:
        tree = lxml_html.fromstring(raw)
    except Exception as exc:
        logger.warning(f"Cannot parse HTML {html_path}: {exc}")
        return 0

    updates = 0

    for element in tree.iter():
        tag = element.tag
        if not isinstance(tag, str):
            continue
        # Normalise tag to local name (strip namespace)
        local_tag = tag.split("}")[-1].lower() if "}" in tag else tag.lower()

        for attr_tag, attr_name in _IMAGE_ATTRS:
            if attr_tag is not None and local_tag != attr_tag:
                continue

            value = element.get(attr_name)
            if not value:
                continue

            # srcset needs special comma-separated handling
            if attr_name == "srcset":
                new_val, changed = _rewrite_srcset(value, lang_dir, html_path, output_root)
                if changed:
                    if not dry_run:
                        element.set(attr_name, new_val)
                    logger.info(f"  {html_path.name}: {attr_name} {value!r} → {new_val!r}")
                    updates += 1
                continue

            if not _is_image_path(value):
                continue

            resolved = _resolve_ref(value, html_path, output_root)
            if resolved is None:
                continue

            translated = _find_translated_image(resolved, lang_dir, output_root)
            if translated is None:
                continue

            new_val = _make_relative_ref(translated, html_path)
            if new_val == value:
                continue

            if not dry_run:
                element.set(attr_name, new_val)
            logger.info(f"  {html_path.name}: {attr_name} {value!r} → {new_val!r}")
            updates += 1

    if updates > 0 and not dry_run:
        try:
            updated_bytes = lxml_html.tostring(
                tree,
                encoding="unicode",
                doctype="<!DOCTYPE html>",
            ).encode("utf-8")
            with open(html_path, "wb") as fh:
                fh.write(updated_bytes)
        except Exception as exc:
            logger.error(f"Failed to write {html_path}: {exc}")

    return updates


# ---------------------------------------------------------------------------
# Language directory discovery
# ---------------------------------------------------------------------------

def _find_lang_dirs(output_root: Path, lang_filter: Optional[str]) -> List[Tuple[str, Path]]:
    """
    Find language sub-directories inside the IG Publisher output directory.

    A directory is considered a language directory if:
      - Its name matches a known BCP-47 language code, OR
      - Its name is a two-letter lowercase code and it contains .html files

    Returns list of (lang_code, path) tuples.
    """
    results: List[Tuple[str, Path]] = []
    if not output_root.is_dir():
        return results

    for entry in sorted(output_root.iterdir()):
        if not entry.is_dir():
            continue
        name = entry.name
        if lang_filter and name != lang_filter:
            continue
        # Accept known language codes or any 2-letter lowercase directory
        # that contains HTML files (avoids picking up unrelated directories)
        is_known = name in _KNOWN_LANG_CODES
        is_two_letter = re.match(r'^[a-z]{2}$', name) is not None
        has_html = any(entry.glob("*.html"))
        if is_known or (is_two_letter and has_html):
            results.append((name, entry))

    return results


# ---------------------------------------------------------------------------
# Main orchestrator
# ---------------------------------------------------------------------------

def run(
    output_root: Path,
    lang_filter: Optional[str],
    dry_run: bool,
    logger: logging.Logger,
) -> int:
    """
    Process all translated HTML pages in the output directory.

    Returns total number of image references updated.
    """
    lang_dirs = _find_lang_dirs(output_root, lang_filter)
    if not lang_dirs:
        logger.info("No language sub-directories found in output — nothing to update")
        return 0

    total_updates = 0
    for lang, lang_dir in lang_dirs:
        html_files = sorted(lang_dir.glob("*.html"))
        if not html_files:
            logger.debug(f"No HTML files in {lang_dir}, skipping")
            continue

        logger.info(f"Processing {len(html_files)} HTML file(s) for language '{lang}'")
        for html_file in html_files:
            n = process_html_file(html_file, lang_dir, output_root, dry_run, logger)
            total_updates += n

    return total_updates


def main() -> int:
    """Entry point."""
    parser = argparse.ArgumentParser(
        description="Update image references in translated IG Publisher HTML output",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("output"),
        help="IG Publisher output directory (default: output)",
    )
    parser.add_argument(
        "--ig-root",
        type=Path,
        default=Path("."),
        help="Repository root directory (default: current directory)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be changed without writing files",
    )
    parser.add_argument(
        "--lang",
        default=None,
        help="Only process a specific language code (e.g. fr)",
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    logger = logging.getLogger(__name__)

    output_root = (args.ig_root / args.output_dir).resolve()

    if not output_root.exists():
        logger.info(f"Output directory {output_root} does not exist — nothing to update")
        return 0

    logger.info(
        f"Updating translated image references in {output_root}"
        + (" [dry-run]" if args.dry_run else "")
    )

    total = run(output_root, args.lang, args.dry_run, logger)
    logger.info(
        f"Done: {total} image reference(s) "
        + ("would be " if args.dry_run else "")
        + "updated"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
