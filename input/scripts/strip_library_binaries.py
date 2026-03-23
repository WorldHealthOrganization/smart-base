#!/usr/bin/env python3
"""
WHO SMART Guidelines — Extract ELM Binary Data from Library Resources

Postprocessing step that extracts base64-encoded ELM data from FHIR Library
resource files produced by the IG Publisher, writes the decoded content to
standalone files, and replaces the inline ``data`` with a relative ``url``
reference to the extracted file.

Library resources contain a ``content`` array whose entries carry a
``data`` field with base64-encoded payloads.  ELM payloads
(application/elm+json, application/elm+xml) are large and not needed
inline.  CQL source (text/cql) is kept as-is.

For each ELM content entry the script:
  1. Decodes the base64 ``data`` payload.
  2. Writes it to a file next to the Library resource
     (e.g. ``Library-Foo.elm``).
  3. Removes the ``data`` field and adds a ``url`` field with a relative
     reference to the extracted file.

This script modifies:
  - **JSON files** (Library-*.json): extracts data, replaces with ``url``.
  - **XML files**  (Library-*.xml):  replaces ``<data>`` with ``<url>``.
  - **TTL files**  (Library-*.ttl):  replaces base64 literal with url.
  - **HTML files** (Library-*.html): updates the rendered representations.

Usage:
    python strip_library_binaries.py [output_dir]

Defaults:
    output_dir = ./output

Author: SMART Guidelines Team
"""

import base64
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

# Content types whose data should be extracted.
_ELM_CONTENT_TYPES = {
    "application/elm+json",
    "application/elm+xml",
}

_FHIR_NS = "http://hl7.org/fhir"
_XHTML_NS = "http://www.w3.org/1999/xhtml"


def _is_elm(entry: dict) -> bool:
    """Return True if a content entry is an ELM payload."""
    return entry.get("contentType", "") in _ELM_CONTENT_TYPES


def _elm_filename(library_stem: str) -> str:
    """Return the extracted ELM filename for a Library resource.

    E.g. Library-Foo -> Library-Foo.elm
    """
    return library_stem + ".elm"


def _extract_and_replace_elm_in_dict(
    resource: dict, output_dir: Path, library_stem: str
) -> bool:
    """Extract ELM data to files and replace ``data`` with ``url``.

    Returns True if anything was changed.
    """
    contents = resource.get("content")
    if not isinstance(contents, list):
        return False
    changed = False
    for entry in contents:
        if not _is_elm(entry) or not entry.get("data"):
            continue
        elm_file = _elm_filename(library_stem)
        elm_path = output_dir / elm_file
        # Only extract once per Library (first ELM entry wins).
        if not elm_path.exists():
            try:
                decoded = base64.b64decode(entry["data"])
            except Exception as exc:
                logger.warning(
                    "Could not decode base64 data for %s in %s: %s",
                    entry["contentType"],
                    library_stem,
                    exc,
                )
                continue
            elm_path.write_bytes(decoded)
            logger.info("Extracted %s -> %s", entry["contentType"], elm_file)
        # Replace data with a relative url reference.
        del entry["data"]
        entry["url"] = elm_file
        changed = True
    return changed


def _replace_elm_data_with_url_in_dict(
    resource: dict, library_stem: str
) -> bool:
    """Replace ``data`` with ``url`` on ELM content entries (no file I/O).

    Used for embedded representations (HTML) where we don't need to
    extract again — the JSON pass already wrote the files.
    """
    contents = resource.get("content")
    if not isinstance(contents, list):
        return False
    changed = False
    for entry in contents:
        if not _is_elm(entry):
            continue
        elm_file = _elm_filename(library_stem)
        if entry.get("data"):
            del entry["data"]
            entry["url"] = elm_file
            changed = True
        elif not entry.get("url"):
            entry["url"] = elm_file
            changed = True
    return changed


def _replace_elm_data_with_url_in_xml(
    root: ET.Element, library_stem: str
) -> bool:
    """Replace ``data`` with ``url`` on ELM content entries in XML.

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
        elm_file = _elm_filename(library_stem)
        data_el = content_el.find("f:data", ns)
        if data_el is not None:
            content_el.remove(data_el)
        # Add or update the url element.
        url_el = content_el.find("f:url", ns)
        if url_el is None:
            url_el = ET.SubElement(content_el, f"{{{_FHIR_NS}}}url")
        url_el.set("value", elm_file)
        changed = True
    return changed


# ---------------------------------------------------------------------------
# JSON processing
# ---------------------------------------------------------------------------


def strip_library_json(output_dir: Path) -> int:
    """Extract ELM data from Library-*.json files and replace with url."""
    modified = 0
    for fpath in sorted(output_dir.glob("Library-*.json")):
        # Skip extracted .elm files that happen to end in .json.
        if fpath.suffixes == [".elm", ".json"]:
            continue
        try:
            raw = fpath.read_text(encoding="utf-8")
            resource = json.loads(raw)
        except (json.JSONDecodeError, OSError) as exc:
            logger.warning("Skipping %s: %s", fpath.name, exc)
            continue

        if resource.get("resourceType") != "Library":
            continue

        if _extract_and_replace_elm_in_dict(resource, output_dir, fpath.stem):
            fpath.write_text(
                json.dumps(resource, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
            modified += 1
            logger.info("Updated %s with url references", fpath.name)

    return modified


# ---------------------------------------------------------------------------
# XML processing
# ---------------------------------------------------------------------------

# Register namespaces so ElementTree preserves them on write-back.
ET.register_namespace("", _FHIR_NS)
ET.register_namespace("xhtml", _XHTML_NS)


def strip_library_xml(output_dir: Path) -> int:
    """Replace ELM data with url references in Library-*.xml files."""
    modified = 0
    for fpath in sorted(output_dir.glob("Library-*.xml")):
        if fpath.suffixes == [".elm", ".xml"]:
            continue
        try:
            tree = ET.parse(fpath)  # noqa: S314
        except ET.ParseError as exc:
            logger.warning("Skipping %s: %s", fpath.name, exc)
            continue

        root = tree.getroot()
        if root.tag != f"{{{_FHIR_NS}}}Library":
            continue

        if _replace_elm_data_with_url_in_xml(root, fpath.stem):
            tree.write(fpath, encoding="unicode", xml_declaration=True)
            modified += 1
            logger.info("Updated %s with url references", fpath.name)

    return modified


# ---------------------------------------------------------------------------
# TTL (Turtle/RDF) processing
# ---------------------------------------------------------------------------

# No Turtle parser in the standard library.  We use a targeted regex that
# matches the IG Publisher's predictable serialisation of content entries:
#
#   fhir:contentType [ fhir:v "application/elm+json" ] ;
#   fhir:data [ fhir:v "eyJ…base64…"^^xsd:base64Binary ]
#
# We replace the fhir:data line with a fhir:url line.
_TTL_ELM_BLOCK_RE = re.compile(
    r"(fhir:contentType\s+\[\s*fhir:v\s+"
    r'"application/elm\+(json|xml)"\s*\]'
    r".*?)"
    r'fhir:data\s+\[\s*fhir:v\s+"[A-Za-z0-9+/=]+"(?:\^\^xsd:base64Binary)?\s*\]',
    re.DOTALL,
)


def _ttl_elm_replacer(match: re.Match, library_stem: str) -> str:
    """Replace fhir:data with fhir:url in a TTL ELM block."""
    prefix = match.group(1)
    elm_file = _elm_filename(library_stem)
    return f'{prefix}fhir:url [ fhir:v "{elm_file}" ]'


def strip_library_ttl(output_dir: Path) -> int:
    """Replace ELM data with url references in Library-*.ttl files."""
    modified = 0
    for fpath in sorted(output_dir.glob("Library-*.ttl")):
        try:
            raw = fpath.read_text(encoding="utf-8")
        except OSError as exc:
            logger.warning("Skipping %s: %s", fpath.name, exc)
            continue

        new_raw = _TTL_ELM_BLOCK_RE.sub(
            lambda m: _ttl_elm_replacer(m, fpath.stem), raw
        )
        if new_raw != raw:
            fpath.write_text(new_raw, encoding="utf-8")
            modified += 1
            logger.info("Updated %s with url references", fpath.name)

    return modified


# ---------------------------------------------------------------------------
# HTML processing
# ---------------------------------------------------------------------------

# The IG Publisher embeds the full resource representation inside
# <pre class="json"><code>…</code></pre> and
# <pre class="xml"><code>…</code></pre> blocks.
# We locate each block, extract and unescape the text content, parse it
# with the proper parser (json / XML), update ELM references, and write
# it back.

_PRE_CODE_RE = re.compile(
    r'(<pre\s+class="(json|xml|rdf)"\s*>\s*<code[^>]*>)'
    r"(.*?)"
    r"(</code>\s*</pre>)",
    re.DOTALL,
)


def _make_html_code_block_replacer(library_stem: str):
    """Return a callback for _PRE_CODE_RE that replaces ELM data with url."""

    def _replace(match: re.Match) -> str:
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
            if not _replace_elm_data_with_url_in_dict(resource, library_stem):
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
            if not _replace_elm_data_with_url_in_xml(root, library_stem):
                return match.group(0)
            new_body = ET.tostring(root, encoding="unicode")
            return prefix + html.escape(new_body, quote=False) + suffix

        if lang == "rdf":
            new_body = _TTL_ELM_BLOCK_RE.sub(
                lambda m: _ttl_elm_replacer(m, library_stem), body
            )
            if new_body == body:
                return match.group(0)
            return prefix + html.escape(new_body, quote=False) + suffix

        return match.group(0)

    return _replace


def _elm_viewer_snippet(elm_file: str) -> str:
    """Return an HTML/JS snippet that loads and displays an extracted .elm file."""
    return f"""<div class="elm-viewer" style="margin:1em 0">
<h4>ELM Content</h4>
<p>ELM binary data has been extracted to
<a href="{elm_file}">{elm_file}</a>.</p>
<button type="button" onclick="loadElm(this, '{elm_file}')"
  style="cursor:pointer;padding:4px 12px">View ELM</button>
<pre class="elm-content" style="display:none;max-height:400px;overflow:auto;
border:1px solid #ccc;padding:8px;margin-top:6px;background:#f8f8f8"><code></code></pre>
</div>
<script>
function loadElm(btn, url) {{
  var pre = btn.nextElementSibling;
  if (pre.style.display !== 'none') {{
    pre.style.display = 'none';
    btn.textContent = 'View ELM';
    return;
  }}
  var code = pre.querySelector('code');
  if (code.textContent) {{
    pre.style.display = '';
    btn.textContent = 'Hide ELM';
    return;
  }}
  btn.textContent = 'Loading\u2026';
  fetch(url)
    .then(function(r) {{ return r.text(); }})
    .then(function(text) {{
      try {{ text = JSON.stringify(JSON.parse(text), null, 2); }} catch(e) {{}}
      code.textContent = text;
      pre.style.display = '';
      btn.textContent = 'Hide ELM';
    }})
    .catch(function(err) {{
      code.textContent = 'Failed to load: ' + err;
      pre.style.display = '';
      btn.textContent = 'View ELM';
    }});
}}
</script>"""


# Regex to find the first <pre class="json"> block — we inject the viewer
# right before it so it appears alongside the resource representations.
_FIRST_PRE_JSON_RE = re.compile(
    r'<pre\s+class="json"\s*>', re.IGNORECASE
)


def strip_library_html(output_dir: Path) -> int:
    """Update ELM references in Library-*.html files."""
    modified = 0
    for fpath in sorted(output_dir.glob("Library-*.html")):
        try:
            raw = fpath.read_text(encoding="utf-8")
        except OSError as exc:
            logger.warning("Skipping %s: %s", fpath.name, exc)
            continue

        # Derive the library stem from the HTML filename.
        library_stem = fpath.stem

        replacer = _make_html_code_block_replacer(library_stem)
        new_raw = _PRE_CODE_RE.sub(replacer, raw)
        if new_raw != raw:
            # Inject the ELM viewer widget before the first JSON code block.
            elm_file = _elm_filename(library_stem)
            snippet = _elm_viewer_snippet(elm_file)
            m = _FIRST_PRE_JSON_RE.search(new_raw)
            if m:
                new_raw = new_raw[: m.start()] + snippet + "\n" + new_raw[m.start() :]
            fpath.write_text(new_raw, encoding="utf-8")
            modified += 1
            logger.info("Updated %s with url references and ELM viewer", fpath.name)

    return modified


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    output_dir = Path(sys.argv[1] if len(sys.argv) > 1 else "output")
    if not output_dir.is_dir():
        logger.error("Output directory does not exist: %s", output_dir)
        sys.exit(1)

    logger.info(
        "Extracting ELM binary data from Library resources in %s", output_dir
    )
    # JSON pass runs first — it extracts the actual .elm files.
    json_count = strip_library_json(output_dir)
    # Remaining passes just update references (files already extracted).
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
