#!/usr/bin/env python3
"""
SMART Guidelines Translation Extraction Script

Extracts translatable strings from visual and architectural diagram sources
into Gettext .pot template files for Weblate-based localisation.

Targeted source types (aligned with the L3 Authoring SOP):
  - PlantUML  (.plantuml)  in input/images-source/
  - Custom SVG (.svg)      in input/images/
  - ArchiMate  (.archimate) in input/archimate/
  - UML diagrams (.svg/.xml) in input/diagrams/

Each .pot file records:
  - #. Source: <relative-path>:<line>   — exact file/line location
  - #. URL: <canonical-page-url>        — published page for Weblate context

Usage:
    python extract_translations.py [options]

Options:
    --ig-root DIR          Repository root (default: current directory)
    --canonical URL        IG canonical base URL
                           (default: http://smart.who.int/base)
    --output-dir DIR       Override a single output directory for all .pot
                           files (useful for testing)
    --help / -h            Print this help
"""

import argparse
import datetime
import glob as glob_module
import logging
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Optional lxml import (graceful fallback to stdlib xml.etree)
# ---------------------------------------------------------------------------
try:
    import lxml.etree as ET
    _HAVE_LXML = True
except ImportError:  # pragma: no cover
    import xml.etree.ElementTree as ET  # type: ignore
    _HAVE_LXML = False

# ---------------------------------------------------------------------------
# PlantUML syntax exclusion list
# Words/patterns that must NOT be extracted as translatable text.
# ---------------------------------------------------------------------------
PLANTUML_KEYWORDS: frozenset = frozenset([
    # diagram-type declarations
    "startuml", "enduml",
    "startmindmap", "endmindmap",
    "startgantt", "endgantt",
    "startsalt", "endsalt",
    "startwbs", "endwbs",
    "startjson", "endjson",
    "startyaml", "endyaml",
    # layout / style
    "skinparam", "hide", "show", "left", "right", "center",
    "top", "bottom", "up", "down",
    "horizontal", "vertical", "together",
    "newpage", "autonumber", "autoactivate",
    # element keywords
    "participant", "actor", "boundary", "control", "entity",
    "database", "collections", "queue", "component", "interface",
    "package", "node", "cloud", "frame", "rectangle",
    "class", "abstract", "enum", "annotation",
    "usecase", "state", "object", "artifact",
    "folder", "file", "hexagon", "agent", "stack",
    "card", "label", "map", "storage",
    # relation keywords
    "as", "with", "of", "is", "in", "extends", "implements",
    # note / grouping keywords
    "note", "end", "ref", "over", "across",
    "group", "box", "alt", "else", "opt", "loop",
    "par", "break", "critical", "neg",
    "legend", "endlegend",
    # colour / style
    "order", "activate", "deactivate", "destroy", "create",
    "return", "autonumber", "delay", "divider", "space",
    # misc
    "title", "header", "footer", "caption",
    "mainframe", "allow_mixing",
    "!include", "!theme", "!pragma",
    "sprite",
])

# Regex patterns for lines that are purely PlantUML directives (never extract)
_PLANTUML_DIRECTIVE_RE = re.compile(
    r"""^\s*(?:
        @\w+                          |  # @startuml / @enduml etc.
        '.*                           |  # single-quote comment
        /\*|\*/                       |  # block comment delimiters
        skinparam\b                   |  # skinparam block
        \!(?:include|theme|pragma)\b  |  # pre-processor directives
        \#[0-9A-Fa-f]{3,8}\b         |  # inline colour
        [\-\~\.=<>#\[\]\{\}]{2,}        # arrow / box drawing chars
    )""",
    re.VERBOSE,
)

# Pattern to extract a quoted label from a PlantUML declaration line.
# Captures content inside double-quotes (handles escaped quotes).
_QUOTED_LABEL_RE = re.compile(r'"((?:[^"\\]|\\.)+)"')

# Pattern to extract unquoted labels that follow certain keywords, e.g.:
#   title My Title
#   header Some Header
#   footer Some Footer
_UNQUOTED_KEYWORD_LABEL_RE = re.compile(
    r"^\s*(?:title|header|footer|caption)\s+(.+)$", re.IGNORECASE
)

# Arrow message: A -> B : some text   (extract "some text")
_ARROW_MESSAGE_RE = re.compile(r":\s*([^:\n]+)\s*$")

# Multi-line note block pattern
_NOTE_START_RE = re.compile(
    r"^\s*note\s+(?:left|right|over[\w\s,]*|across|as\s+\w+)\s*$", re.IGNORECASE
)
_NOTE_END_RE = re.compile(r"^\s*end\s+note\s*$", re.IGNORECASE)
_INLINE_NOTE_RE = re.compile(
    r"^\s*note\s+(?:left|right|over|across)[^:]*:\s*(.+)$", re.IGNORECASE
)

# Legend block
_LEGEND_START_RE = re.compile(r"^\s*legend\s*(?:left|right|center)?\s*$", re.IGNORECASE)
_LEGEND_END_RE = re.compile(r"^\s*end\s*legend\s*$", re.IGNORECASE)


# ---------------------------------------------------------------------------
# POT file helpers
# ---------------------------------------------------------------------------

POT_HEADER = """\
# WHO SMART Guidelines Translation Template
# Copyright (C) {year} World Health Organization
# This file is distributed under the CC-BY-SA-3.0-IGO license.
#
#, fuzzy
msgid ""
msgstr ""
"Project-Id-Version: WHO SMART Guidelines\\n"
"POT-Creation-Date: {timestamp}\\n"
"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\\n"
"Last-Translator: FULL NAME <EMAIL@ADDRESS>\\n"
"Language-Team: LANGUAGE <LL@li.org>\\n"
"Language: \\n"
"MIME-Version: 1.0\\n"
"Content-Type: text/plain; charset=UTF-8\\n"
"Content-Transfer-Encoding: 8bit\\n"
"Plural-Forms: nplurals=6; plural=(n==1 ? 0 : n==2 ? 1 : n>=3 && n<=10 ? 2 : n>=11 && n<=99 ? 3 : 4);\\n"

"""


def _escape_pot(text: str) -> str:
    """Escape a string for inclusion in a msgid / msgstr value."""
    text = text.replace("\\", "\\\\")
    text = text.replace('"', '\\"')
    text = text.replace("\n", "\\n\"\n\"")
    return text


def _make_context_url(canonical: str, source_rel: str) -> str:
    """
    Derive the published URL for a source diagram file.

    PlantUML files in input/images-source/foo.plantuml are rendered to
    output/foo.svg, accessible at <canonical>/foo.svg.
    SVGs in input/images/foo.svg are accessible at <canonical>/foo.svg.
    ArchiMate files have no direct published equivalent; link to the IG root.
    """
    canonical = canonical.rstrip("/")
    source_path = Path(source_rel)
    stem = source_path.stem
    suffix = source_path.suffix.lower()

    if suffix == ".plantuml":
        return f"{canonical}/{stem}.svg"
    elif suffix == ".svg":
        return f"{canonical}/{stem}.svg"
    elif suffix in (".archimate", ".xml"):
        return f"{canonical}/"
    return f"{canonical}/"


# ---------------------------------------------------------------------------
# Entry dataclass (named tuple) for a single translatable string
# ---------------------------------------------------------------------------

class TranslationEntry:
    """Represents a single extractable translatable string."""

    __slots__ = ("source_file", "line_number", "text", "context_url")

    def __init__(self, source_file: str, line_number: int, text: str, context_url: str):
        self.source_file = source_file
        self.line_number = line_number
        self.text = text.strip()
        self.context_url = context_url


# ---------------------------------------------------------------------------
# PlantUML extractor
# ---------------------------------------------------------------------------

def _is_plantuml_keyword_only(text: str) -> bool:
    """Return True if a candidate label is a bare PlantUML keyword."""
    words = re.split(r"[\s_\-]+", text.strip().lower())
    return all(w in PLANTUML_KEYWORDS or not w for w in words)


def extract_plantuml(file_path: str, canonical: str) -> List[TranslationEntry]:
    """
    Extract translatable strings from a PlantUML source file.

    Args:
        file_path: Relative path to the .plantuml file
        canonical: IG canonical base URL

    Returns:
        List of TranslationEntry objects
    """
    entries: List[TranslationEntry] = []
    context_url = _make_context_url(canonical, file_path)

    try:
        with open(file_path, "r", encoding="utf-8") as fh:
            lines = fh.readlines()
    except OSError as exc:
        logging.getLogger(__name__).warning(f"Cannot read {file_path}: {exc}")
        return entries

    in_note = False
    in_legend = False
    block_lines: List[Tuple[int, str]] = []

    for lineno, raw_line in enumerate(lines, start=1):
        line = raw_line.rstrip("\n")

        # Skip pure directive / comment lines
        if _PLANTUML_DIRECTIVE_RE.match(line):
            continue

        # --- Multi-line note block ---
        if _NOTE_START_RE.match(line):
            in_note = True
            block_lines = []
            continue
        if in_note:
            if _NOTE_END_RE.match(line):
                in_note = False
                combined = "\n".join(l for _, l in block_lines if l.strip())
                if combined.strip():
                    entries.append(TranslationEntry(file_path, block_lines[0][0] if block_lines else lineno, combined, context_url))
                block_lines = []
            else:
                block_lines.append((lineno, line.strip()))
            continue

        # --- Legend block ---
        if _LEGEND_START_RE.match(line):
            in_legend = True
            block_lines = []
            continue
        if in_legend:
            if _LEGEND_END_RE.match(line):
                in_legend = False
                combined = "\n".join(l for _, l in block_lines if l.strip())
                if combined.strip():
                    entries.append(TranslationEntry(file_path, block_lines[0][0] if block_lines else lineno, combined, context_url))
                block_lines = []
            else:
                block_lines.append((lineno, line.strip()))
            continue

        # --- Inline note ---
        m = _INLINE_NOTE_RE.match(line)
        if m:
            text = m.group(1).strip()
            if text and not _is_plantuml_keyword_only(text):
                entries.append(TranslationEntry(file_path, lineno, text, context_url))
            continue

        # --- Unquoted keyword labels (title, header, footer, caption) ---
        m = _UNQUOTED_KEYWORD_LABEL_RE.match(line)
        if m:
            text = m.group(1).strip()
            if text and not _is_plantuml_keyword_only(text):
                entries.append(TranslationEntry(file_path, lineno, text, context_url))

        # --- Quoted labels ---
        for m in _QUOTED_LABEL_RE.finditer(line):
            text = m.group(1).strip()
            # Skip if it looks like a URL, color, or pure keyword
            if text and not _is_plantuml_keyword_only(text) and not text.startswith("#") and "://" not in text:
                entries.append(TranslationEntry(file_path, lineno, text, context_url))

        # --- Arrow messages (after ":" at end of line) ---
        # Only when line contains an arrow operator.
        # Skip if the message is a quoted string — the quoted-label pass
        # above already extracted it to avoid duplicates.
        # (Plain string check avoids false-positive HTML-comment-filter warnings.)
        if any(op in line for op in ("->", "<-", "->>", "<<-")):
            m = _ARROW_MESSAGE_RE.search(line)
            if m:
                text = m.group(1).strip()
                # If the arrow message is quoted, it was already captured above
                if text.startswith('"') and text.endswith('"'):
                    pass  # already extracted by _QUOTED_LABEL_RE
                elif text and not _is_plantuml_keyword_only(text) and not text.startswith("#"):
                    entries.append(TranslationEntry(file_path, lineno, text, context_url))

    return entries


# ---------------------------------------------------------------------------
# SVG extractor
# ---------------------------------------------------------------------------

# SVG namespace
_SVG_NS = "http://www.w3.org/2000/svg"

# Text-bearing SVG element tags (with/without namespace)
_SVG_TEXT_TAGS = {
    f"{{{_SVG_NS}}}text",
    f"{{{_SVG_NS}}}tspan",
    f"{{{_SVG_NS}}}title",
    f"{{{_SVG_NS}}}desc",
    "text", "tspan", "title", "desc",
}


def _get_text_content(element) -> str:
    """Recursively collect all text from an XML element."""
    parts = []
    if element.text:
        parts.append(element.text.strip())
    for child in element:
        parts.append(_get_text_content(child))
        if child.tail:
            parts.append(child.tail.strip())
    return " ".join(p for p in parts if p)


def extract_svg(file_path: str, canonical: str) -> List[TranslationEntry]:
    """
    Extract translatable text from a custom SVG file.

    Args:
        file_path: Relative path to the .svg file
        canonical: IG canonical base URL

    Returns:
        List of TranslationEntry objects
    """
    entries: List[TranslationEntry] = []
    context_url = _make_context_url(canonical, file_path)

    try:
        if _HAVE_LXML:
            parser = ET.XMLParser(recover=True)
            tree = ET.parse(file_path, parser)
        else:
            tree = ET.parse(file_path)
        root = tree.getroot()
    except Exception as exc:
        logging.getLogger(__name__).warning(f"Cannot parse SVG {file_path}: {exc}")
        return entries

    # Walk all elements and collect text-bearing ones
    for element in root.iter():
        tag = element.tag
        if tag not in _SVG_TEXT_TAGS:
            continue

        # Try to get an approximate line number from lxml
        lineno = getattr(element, "sourceline", 0) or 0
        text = _get_text_content(element).strip()
        if text:
            entries.append(TranslationEntry(file_path, lineno, text, context_url))

    return entries


# ---------------------------------------------------------------------------
# ArchiMate extractor
# ---------------------------------------------------------------------------

def extract_archimate(file_path: str, canonical: str) -> List[TranslationEntry]:
    """
    Extract translatable strings from an ArchiMate Open Exchange XML file.

    ArchiMate Open Exchange Format is XML-based.  Translatable content lives in:
      - <name> element text
      - <documentation> element text
      - <label> element text (inside <labelExpression>)

    Args:
        file_path: Relative path to the .archimate file
        canonical: IG canonical base URL

    Returns:
        List of TranslationEntry objects
    """
    entries: List[TranslationEntry] = []
    context_url = _make_context_url(canonical, file_path)

    try:
        if _HAVE_LXML:
            parser = ET.XMLParser(recover=True)
            tree = ET.parse(file_path, parser)
        else:
            tree = ET.parse(file_path)
        root = tree.getroot()
    except Exception as exc:
        logging.getLogger(__name__).warning(f"Cannot parse ArchiMate {file_path}: {exc}")
        return entries

    _TARGET_LOCAL_NAMES = {"name", "documentation", "label", "content", "value"}

    for element in root.iter():
        # Strip namespace to get local name
        tag = element.tag
        if "}" in tag:
            tag = tag.split("}", 1)[1]
        if tag.lower() not in _TARGET_LOCAL_NAMES:
            continue

        lineno = getattr(element, "sourceline", 0) or 0
        text = (element.text or "").strip()
        if text:
            entries.append(TranslationEntry(file_path, lineno, text, context_url))

    return entries


# ---------------------------------------------------------------------------
# POT writer
# ---------------------------------------------------------------------------

def write_pot(
    entries: List[TranslationEntry],
    output_path: str,
    canonical: str,
) -> None:
    """
    Write a Gettext .pot template file from a list of TranslationEntry objects.

    Duplicate msgids are deduplicated while merging their source comments.

    Args:
        entries: List of extracted translation entries
        output_path: Path to the output .pot file
        canonical: IG canonical base URL (for header comments)
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Deduplicate: map msgid -> list of (source_file, line, context_url)
    deduped: Dict[str, List[Tuple[str, int, str]]] = {}
    for entry in entries:
        key = entry.text
        if key not in deduped:
            deduped[key] = []
        deduped[key].append((entry.source_file, entry.line_number, entry.context_url))

    now = datetime.datetime.now(datetime.timezone.utc)
    timestamp = now.strftime("%Y-%m-%d %H:%M+0000")
    year = now.year

    with open(output_path, "w", encoding="utf-8") as fh:
        fh.write(POT_HEADER.format(year=year, timestamp=timestamp))

        for msgid, locations in sorted(deduped.items(), key=lambda kv: kv[0].lower()):
            # Write source/location comments
            seen_urls: set = set()
            for src_file, lineno, ctx_url in locations:
                fh.write(f"#. Source: {src_file}:{lineno}\n")
                if ctx_url not in seen_urls:
                    fh.write(f"#. URL: {ctx_url}\n")
                    seen_urls.add(ctx_url)

            # Standard gettext file:line reference
            for src_file, lineno, _ in locations:
                fh.write(f"#: {src_file}:{lineno}\n")

            escaped = _escape_pot(msgid)
            fh.write(f'msgid "{escaped}"\n')
            fh.write('msgstr ""\n\n')

    logger = logging.getLogger(__name__)
    logger.info(f"Wrote {len(deduped)} unique msgids to {output_path}")


# ---------------------------------------------------------------------------
# Main orchestrator
# ---------------------------------------------------------------------------

def collect_entries(
    ig_root: str,
    canonical: str,
) -> Dict[str, List[TranslationEntry]]:
    """
    Scan all diagram source directories and return per-component entry lists.

    Returns:
        Dict mapping output .pot path -> list of TranslationEntry
    """
    result: Dict[str, List[TranslationEntry]] = {}

    # Helper: scan a directory for source files and collect entries.
    # Returns None when the directory does not exist or contains no matching
    # files so the caller can skip writing an empty .pot for that component.
    def _scan(
        src_dir: str,
        patterns: List[str],
        extractor_fn,
    ) -> Optional[List[TranslationEntry]]:
        if not os.path.isdir(src_dir):
            return None
        found: List[TranslationEntry] = []
        for pat in patterns:
            for fpath in sorted(glob_module.glob(os.path.join(src_dir, pat))):
                rel = os.path.relpath(fpath, ig_root)
                found.extend(extractor_fn(rel, canonical))
        return found if found else None

    # --- PlantUML in input/images-source/ ---
    plantuml_dir = os.path.join(ig_root, "input", "images-source")
    plantuml_entries = _scan(plantuml_dir, ["*.plantuml"], extract_plantuml)
    if plantuml_entries is not None:
        result[os.path.join(plantuml_dir, "translations", "diagrams.pot")] = plantuml_entries

    # --- Custom SVG in input/images/ ---
    images_dir = os.path.join(ig_root, "input", "images")
    svg_entries = _scan(images_dir, ["*.svg"], extract_svg)
    if svg_entries is not None:
        result[os.path.join(images_dir, "translations", "images.pot")] = svg_entries

    # --- ArchiMate in input/archimate/ ---
    archimate_dir = os.path.join(ig_root, "input", "archimate")
    archimate_entries = _scan(archimate_dir, ["*.archimate"], extract_archimate)
    if archimate_entries is not None:
        result[os.path.join(archimate_dir, "translations", "models.pot")] = archimate_entries

    # --- UML diagrams in input/diagrams/ (SVG and XML) ---
    diagrams_dir = os.path.join(ig_root, "input", "diagrams")
    diagrams_entries = _scan(diagrams_dir, ["*.svg", "*.xml"], extract_svg)
    if diagrams_entries is not None:
        result[os.path.join(diagrams_dir, "translations", "diagrams.pot")] = diagrams_entries

    return result


def main() -> int:
    """Entry point."""
    parser = argparse.ArgumentParser(
        description="Extract translatable strings from SMART diagram sources into .pot files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--ig-root",
        default=".",
        help="Repository root directory (default: current directory)",
    )
    parser.add_argument(
        "--canonical",
        default="http://smart.who.int/base",
        help="IG canonical base URL (default: http://smart.who.int/base)",
    )
    parser.add_argument(
        "--output-dir",
        default=None,
        help="Override output directory for all .pot files (useful for testing)",
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    logger = logging.getLogger(__name__)

    ig_root = os.path.abspath(args.ig_root)
    canonical = args.canonical.rstrip("/")

    logger.info(f"Extracting translations from {ig_root} (canonical: {canonical})")

    per_component = collect_entries(ig_root, canonical)

    if not per_component:
        logger.info("No diagram source files found — nothing to extract")
        return 0

    total_written = 0
    for pot_path, entries in per_component.items():
        if args.output_dir:
            pot_path = os.path.join(args.output_dir, os.path.basename(pot_path))
        write_pot(entries, pot_path, canonical)
        total_written += 1

    logger.info(f"Extraction complete: {total_written} .pot file(s) written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
