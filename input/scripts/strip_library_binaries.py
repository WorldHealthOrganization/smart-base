#!/usr/bin/env python3
"""
WHO SMART Guidelines — Strip ELM Binary Data from Library Resources

Temporary postprocessing step that removes base64-encoded ELM data from
FHIR Library resource files produced by the IG Publisher.

Library resources contain a ``content`` array whose entries carry a
``data`` field with base64-encoded payloads.  ELM payloads
(application/elm+json, application/elm+xml) are large and not needed in
the published site.  CQL source (text/cql) is kept.

This script modifies:
  - **JSON files** (Library-*.json): clears ``content[].data`` for ELM entries.
  - **XML files**  (Library-*.xml):  clears ``<data value="…"/>`` for ELM entries.
  - **TTL files**  (Library-*.ttl):  clears base64 literals for ELM entries.
  - **HTML files** (Library-*.html): strips the long base64 strings from
    the rendered JSON and XML representations embedded in the page.

Usage:
    python strip_library_binaries.py [output_dir]

Defaults:
    output_dir = ./output

Author: SMART Guidelines Team
"""

import html
import json
import logging
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def setup_logging() -> logging.Logger:
    """Configure logging for the script."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    return logging.getLogger(__name__)


logger = setup_logging()

# Content types whose data should be stripped.
_ELM_CONTENT_TYPES = {
    "application/elm+json",
    "application/elm+xml",
}

_FHIR_NS = "http://hl7.org/fhir"
_XHTML_NS = "http://www.w3.org/1999/xhtml"


def _is_elm(entry: dict) -> bool:
    """Return True if a content entry is an ELM payload."""
    return entry.get("contentType", "") in _ELM_CONTENT_TYPES


def _strip_elm_from_dict(resource: dict) -> bool:
    """Clear ``data`` on ELM content entries in a Library dict.

    Returns True if anything was changed.
    """
    contents = resource.get("content")
    if not isinstance(contents, list):
        return False
    changed = False
    for entry in contents:
        if _is_elm(entry) and entry.get("data"):
            entry["data"] = ""
            changed = True
    return changed


def _strip_elm_from_xml_tree(root: ET.Element) -> bool:
    """Clear ``data`` on ELM content entries in a parsed FHIR XML tree.

    Returns True if anything was changed.
    """
    ns = {"f": _FHIR_NS}
    changed = False
    for content_el in root.findall("f:content", ns):
        ct_el = content_el.find("f:contentType", ns)
        if ct_el is None:
            continue
        if ct_el.get("value", "") not in _ELM_CONTENT_TYPES:
            continue
        data_el = content_el.find("f:data", ns)
        if data_el is not None and data_el.get("value"):
            data_el.set("value", "")
            changed = True
    return changed


# ---------------------------------------------------------------------------
# JSON processing
# ---------------------------------------------------------------------------


def strip_library_json(output_dir: Path) -> int:
    """Strip ELM base64 data from Library-*.json files."""
    modified = 0
    for fpath in sorted(output_dir.glob("Library-*.json")):
        try:
            raw = fpath.read_text(encoding="utf-8")
            resource = json.loads(raw)
        except (json.JSONDecodeError, OSError) as exc:
            logger.warning("Skipping %s: %s", fpath.name, exc)
            continue

        if resource.get("resourceType") != "Library":
            continue

        if _strip_elm_from_dict(resource):
            fpath.write_text(
                json.dumps(resource, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
            modified += 1
            logger.info("Stripped ELM data from %s", fpath.name)

    return modified


# ---------------------------------------------------------------------------
# XML processing
# ---------------------------------------------------------------------------

# Register namespaces so ElementTree preserves them on write-back.
ET.register_namespace("", _FHIR_NS)
ET.register_namespace("xhtml", _XHTML_NS)


def strip_library_xml(output_dir: Path) -> int:
    """Strip ELM base64 data from Library-*.xml files."""
    modified = 0
    for fpath in sorted(output_dir.glob("Library-*.xml")):
        try:
            tree = ET.parse(fpath)  # noqa: S314
        except ET.ParseError as exc:
            logger.warning("Skipping %s: %s", fpath.name, exc)
            continue

        root = tree.getroot()
        if root.tag != f"{{{_FHIR_NS}}}Library":
            continue

        if _strip_elm_from_xml_tree(root):
            tree.write(fpath, encoding="unicode", xml_declaration=True)
            modified += 1
            logger.info("Stripped ELM data from %s", fpath.name)

    return modified


# ---------------------------------------------------------------------------
# TTL (Turtle/RDF) processing
# ---------------------------------------------------------------------------

# No Turtle parser in the standard library.  We use a targeted regex that
# matches the IG Publisher's predictable serialisation of content entries:
#
#   fhir:contentType [ fhir:v "application/elm+json" ] ;
#   fhir:data [ fhir:v "eyJ…base64…"^^xsd:base64Binary ]
_TTL_ELM_DATA_RE = re.compile(
    r"(fhir:contentType\s+\[\s*fhir:v\s+"
    r'"application/elm\+(?:json|xml)"\s*\]'
    r".*?"
    r'fhir:data\s+\[\s*fhir:v\s+")[A-Za-z0-9+/=]+(")',
    re.DOTALL,
)


def strip_library_ttl(output_dir: Path) -> int:
    """Strip ELM base64 data from Library-*.ttl files."""
    modified = 0
    for fpath in sorted(output_dir.glob("Library-*.ttl")):
        try:
            raw = fpath.read_text(encoding="utf-8")
        except OSError as exc:
            logger.warning("Skipping %s: %s", fpath.name, exc)
            continue

        new_raw = _TTL_ELM_DATA_RE.sub(r"\1\2", raw)
        if new_raw != raw:
            fpath.write_text(new_raw, encoding="utf-8")
            modified += 1
            logger.info("Stripped ELM data from %s", fpath.name)

    return modified


# ---------------------------------------------------------------------------
# HTML processing
# ---------------------------------------------------------------------------

# The IG Publisher embeds the full resource representation inside
# <pre class="json"><code>…</code></pre> and
# <pre class="xml"><code>…</code></pre> blocks.
# We locate each block, extract and unescape the text content, parse it
# with the proper parser (json / XML), strip ELM data, and write it back.

_PRE_CODE_RE = re.compile(
    r'(<pre\s+class="(json|xml|rdf)"\s*>\s*<code[^>]*>)'
    r"(.*?)"
    r"(</code>\s*</pre>)",
    re.DOTALL,
)


def _replace_html_code_block(match: re.Match) -> str:
    """Callback for _PRE_CODE_RE: parse the embedded content and strip ELM."""
    prefix = match.group(1)
    lang = match.group(2)
    encoded_body = match.group(3)
    suffix = match.group(4)

    body = html.unescape(encoded_body)

    if lang == "json":
        try:
            resource = json.loads(body)
        except (json.JSONDecodeError, ValueError):
            return match.group(0)
        if resource.get("resourceType") != "Library":
            return match.group(0)
        if not _strip_elm_from_dict(resource):
            return match.group(0)
        new_body = json.dumps(resource, indent=2, ensure_ascii=False)
        return prefix + html.escape(new_body, quote=False) + suffix

    if lang == "xml":
        try:
            root = ET.fromstring(body)  # noqa: S314
        except ET.ParseError:
            return match.group(0)
        if root.tag != f"{{{_FHIR_NS}}}Library":
            return match.group(0)
        if not _strip_elm_from_xml_tree(root):
            return match.group(0)
        new_body = ET.tostring(root, encoding="unicode")
        return prefix + html.escape(new_body, quote=False) + suffix

    if lang == "rdf":
        new_body = _TTL_ELM_DATA_RE.sub(r"\1\2", body)
        if new_body == body:
            return match.group(0)
        return prefix + html.escape(new_body, quote=False) + suffix

    return match.group(0)


def strip_library_html(output_dir: Path) -> int:
    """Strip ELM base64 data from Library-*.html files."""
    modified = 0
    for fpath in sorted(output_dir.glob("Library-*.html")):
        try:
            raw = fpath.read_text(encoding="utf-8")
        except OSError as exc:
            logger.warning("Skipping %s: %s", fpath.name, exc)
            continue

        new_raw = _PRE_CODE_RE.sub(_replace_html_code_block, raw)
        if new_raw != raw:
            fpath.write_text(new_raw, encoding="utf-8")
            modified += 1
            logger.info("Stripped ELM data from %s", fpath.name)

    return modified


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    output_dir = Path(sys.argv[1] if len(sys.argv) > 1 else "output")
    if not output_dir.is_dir():
        logger.error("Output directory does not exist: %s", output_dir)
        sys.exit(1)

    logger.info("Stripping ELM binary data from Library resources in %s", output_dir)
    json_count = strip_library_json(output_dir)
    xml_count = strip_library_xml(output_dir)
    ttl_count = strip_library_ttl(output_dir)
    html_count = strip_library_html(output_dir)
    logger.info(
        "Done — %d JSON, %d XML, %d TTL, %d HTML file(s) modified",
        json_count,
        xml_count,
        ttl_count,
        html_count,
    )


if __name__ == "__main__":
    main()
