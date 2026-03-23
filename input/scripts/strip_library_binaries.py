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


# ---------------------------------------------------------------------------
# JSON processing
# ---------------------------------------------------------------------------

def _is_elm(entry: dict) -> bool:
    """Return True if a content entry is an ELM payload."""
    return entry.get("contentType", "") in _ELM_CONTENT_TYPES


def strip_library_json(output_dir: Path) -> int:
    """Strip ELM base64 data from Library-*.json files.

    Returns the number of files modified.
    """
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

        contents = resource.get("content")
        if not isinstance(contents, list):
            continue

        changed = False
        for entry in contents:
            if _is_elm(entry) and entry.get("data"):
                entry["data"] = ""
                changed = True

        if changed:
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

_FHIR_NS = "http://hl7.org/fhir"
_NS = {"f": _FHIR_NS}


def strip_library_xml(output_dir: Path) -> int:
    """Strip ELM base64 data from Library-*.xml files.

    Returns the number of files modified.
    """
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

        changed = False
        for content_el in root.findall("f:content", _NS):
            ct_el = content_el.find("f:contentType", _NS)
            if ct_el is None:
                continue
            ct_value = ct_el.get("value", "")
            if ct_value not in _ELM_CONTENT_TYPES:
                continue
            data_el = content_el.find("f:data", _NS)
            if data_el is not None and data_el.get("value"):
                data_el.set("value", "")
                changed = True

        if changed:
            # Preserve the XML declaration and namespace prefixes as written
            # by the IG Publisher.  ElementTree cannot round-trip perfectly,
            # so fall back to a regex-based approach on the raw text instead.
            raw = fpath.read_text(encoding="utf-8")
            new_raw = _strip_elm_data_in_raw_xml(raw)
            if new_raw != raw:
                fpath.write_text(new_raw, encoding="utf-8")
                modified += 1
                logger.info("Stripped ELM data from %s", fpath.name)

    return modified


# Regex for raw FHIR XML: match <contentType value="application/elm+…"/>
# followed (non-greedy) by <data value="…base64…"/> and clear the value.
_RAW_XML_ELM_DATA_RE = re.compile(
    r'(<contentType\s+value="application/elm\+(?:json|xml)"\s*/>'
    r'.*?'
    r'<data\s+value=")[A-Za-z0-9+/=]+(")',
    re.DOTALL,
)


def _strip_elm_data_in_raw_xml(raw: str) -> str:
    """Replace ELM base64 data values with empty strings in raw FHIR XML."""
    return _RAW_XML_ELM_DATA_RE.sub(r"\1\2", raw)


# ---------------------------------------------------------------------------
# TTL (Turtle/RDF) processing
# ---------------------------------------------------------------------------

# In the Turtle serialisation the IG Publisher renders content entries as e.g.:
#   fhir:contentType [ fhir:v "application/elm+json" ] ;
#   fhir:data [ fhir:v "eyJ…base64…"^^xsd:base64Binary ]
_TTL_ELM_DATA_RE = re.compile(
    r'(fhir:contentType\s+\[\s*fhir:v\s+"application/elm\+(?:json|xml)"\s*\]'
    r'.*?'
    r'fhir:data\s+\[\s*fhir:v\s+")[A-Za-z0-9+/=]+(")',
    re.DOTALL,
)


def strip_library_ttl(output_dir: Path) -> int:
    """Strip ELM base64 data from Library-*.ttl files.

    Returns the number of files modified.
    """
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

# In the JSON view the IG Publisher renders:
#   "contentType" : "application/elm+json",
#   "data" : "eyJ…very long base64…"
# We match the contentType line, optional whitespace/lines, then the data line
# and replace just the base64 value with an empty string.
_JSON_ELM_DATA_RE = re.compile(
    r'("contentType"\s*:\s*"application/elm\+(?:json|xml)"'  # contentType line
    r'.*?'                                                    # anything between
    r'"data"\s*:\s*)"[A-Za-z0-9+/=]+"',                      # data value
    re.DOTALL,
)

# In the XML view the IG Publisher renders:
#   <contentType value="application/elm+json"/>
#   <data value="eyJ…very long base64…"/>
_XML_ELM_DATA_RE = re.compile(
    r'(&lt;contentType\s+value=(?:&quot;|")application/elm\+(?:json|xml)(?:&quot;|")\s*/&gt;'
    r'.*?'
    r'&lt;data\s+value=(?:&quot;|"))[A-Za-z0-9+/=]+((?:&quot;|")\s*/&gt;)',
    re.DOTALL,
)


def strip_library_html(output_dir: Path) -> int:
    """Strip ELM base64 data from Library-*.html files.

    Returns the number of files modified.
    """
    modified = 0
    for fpath in sorted(output_dir.glob("Library-*.html")):
        try:
            html = fpath.read_text(encoding="utf-8")
        except OSError as exc:
            logger.warning("Skipping %s: %s", fpath.name, exc)
            continue

        new_html = html

        # Strip from JSON representation
        new_html = _JSON_ELM_DATA_RE.sub(r'\1""', new_html)

        # Strip from XML representation
        new_html = _XML_ELM_DATA_RE.sub(r"\1\2", new_html)

        if new_html != html:
            fpath.write_text(new_html, encoding="utf-8")
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
