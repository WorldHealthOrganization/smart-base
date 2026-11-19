#!/usr/bin/env python3
"""
Round-trip a Markdown page through extract_translations.py and
inject_translations.py, beside this file, and check that inline code spans and
links survive translation.

The page holds inline code, an inline link, a reference link, code inside link
text, a table, a list item, a standalone image and plain prose. It is
extracted to a .pot, "translated" by upper-casing every word outside the
placeholders, written as a .po, and injected. Every code span and every link
target must come back, in place, around the translated text; a translation
that drops a placeholder must leave the source sentence and log it; and a
segment with no code or links must keep the msgid it always had.

Run: python3 input/scripts/translation_placeholders.test.py
"""

from __future__ import annotations

import importlib.util
import logging
import os
import re
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))


def _load(name: str):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, f"{name}.py"))
    module = importlib.util.module_from_spec(spec)
    sys.path.insert(0, HERE)
    try:
        spec.loader.exec_module(module)
    finally:
        sys.path.remove(HERE)
    return module


EXT = _load("extract_translations")
INJ = _load("inject_translations")

PAGE = """\
### The `Consent` resource

Set `Consent.status` to `active`; see [the `Consent` profile](StructureDefinition-Consent.html) and the [WHO guide][who].

| State | Values |
|---|---|
| `Consent.status` (FHIR R4) | `proposed`, `active`, `inactive` (withdrawn or expired): [PHW Consent Kind](ValueSet-PHWConsentKind.html) |

- A list item naming `OPTIN` and [opt-in rules](rules.html#opt-in).

![Consent flow diagram](consent-flow.svg)

Plain prose with no code and no links stays as it was.

Dropped placeholder: `keep-me` must survive.

[who]: https://www.who.int/publications
"""

PLACEHOLDER = re.compile(r"(\{code\d+\}|</?a\d+>)")
CODE_SPAN = re.compile(r"`[^`]+`")
LINK_TARGET = re.compile(r"\]((?:\([^)]*\))|(?:\[[^\]]*\]))")


def fake_translate(msgid: str) -> str:
    """Upper-case the text outside the placeholders."""
    return "".join(p if PLACEHOLDER.fullmatch(p) else p.upper() for p in PLACEHOLDER.split(msgid))


def pot_to_po(pot: str, translate) -> str:
    """Fill every msgstr of a .pot with translate(msgid)."""
    out: list[str] = []
    msgid: str | None = None
    for line in pot.splitlines():
        m = re.match(r'^msgid "(.*)"$', line)
        if m:
            msgid = INJ._unescape_po(m.group(1))
        if line == 'msgstr ""' and msgid:
            line = f'msgstr "{EXT._escape_pot(translate(msgid))}"'
            msgid = None
        out.append(line)
    return "\n".join(out) + "\n"


class _Capture(logging.Handler):
    def __init__(self) -> None:
        super().__init__(logging.WARNING)
        self.messages: list[str] = []

    def emit(self, record: logging.LogRecord) -> None:
        self.messages.append(record.getMessage())


def main() -> int:
    failures: list[str] = []

    def expect(label: str, cond: bool, detail: object = "") -> None:
        if not cond:
            failures.append(f"{label} {detail}".rstrip())

    capture = _Capture()
    logging.getLogger(INJ.__name__).addHandler(capture)

    with tempfile.TemporaryDirectory() as tmp:
        src = os.path.join(tmp, "consent.md")
        with open(src, "w", encoding="utf-8") as fh:
            fh.write(PAGE)

        entries = EXT.extract_markdown(src, "http://example.org/ig")
        msgids = {e.text for e in entries}
        pot_path = os.path.join(tmp, "translations", "consent.pot")
        EXT.write_pot(entries, pot_path, "http://example.org/ig")

        # --- Extraction ---
        expect("heading keeps its code span", "The {code0} resource" in msgids, msgids)
        expect(
            "inline code, code in link text, inline and reference links",
            "Set {code0} to {code1}; see <a0>the {code2} profile</a0> and the <a1>WHO guide</a1>." in msgids,
            msgids,
        )
        expect(
            "table cell keeps codes and link",
            "{code0}, {code1}, {code2} (withdrawn or expired): <a0>PHW Consent Kind</a0>" in msgids,
            msgids,
        )
        expect("a cell of only code is not offered", "{code0} (FHIR R4)" in msgids and "{code0}" not in msgids, msgids)
        expect("list item", "A list item naming {code0} and <a0>opt-in rules</a0>." in msgids, msgids)
        expect("image keeps alt text only", "Consent flow diagram" in msgids, msgids)
        expect(
            "prose without code or links: msgid unchanged",
            "Plain prose with no code and no links stays as it was." in msgids,
            msgids,
        )
        expect("reference-link definition is not prose", not any("who.int" in m for m in msgids), msgids)
        expect("no msgid has an empty slot", not any(re.search(r"(^|\s),|\(\s*\)", m) for m in msgids), msgids)

        # --- Translation: one msgid loses its placeholder ---
        with open(pot_path, encoding="utf-8") as fh:
            pot = fh.read()

        def translate(msgid: str) -> str:
            if msgid.startswith("Dropped placeholder"):
                return "PLACEHOLDER LOST: MUST SURVIVE."
            return fake_translate(msgid)

        po_path = os.path.join(tmp, "translations", "fr.po")
        with open(po_path, "w", encoding="utf-8") as fh:
            fh.write(pot_to_po(pot, translate))
        translations = INJ.parse_po_file(po_path)
        expect("every msgid is translated", set(translations) == msgids, set(msgids) - set(translations))

        # --- Injection ---
        out = os.path.join(tmp, "fr", "consent.md")
        expect("injector writes the page", INJ.inject_markdown(src, translations, out))
        with open(out, encoding="utf-8") as fh:
            got = fh.read()
        lines = got.splitlines()

        expect("heading", "### THE `Consent` RESOURCE" in lines, got)
        expect(
            "paragraph: codes and both links in place",
            "SET `Consent.status` TO `active`; SEE [THE `Consent` PROFILE](StructureDefinition-Consent.html)"
            " AND THE [WHO GUIDE][who]." in lines,
            got,
        )
        expect(
            "table row",
            "| `Consent.status` (FHIR R4) | `proposed`, `active`, `inactive` (WITHDRAWN OR EXPIRED):"
            " [PHW CONSENT KIND](ValueSet-PHWConsentKind.html) |" in lines,
            got,
        )
        expect("list item", "- A LIST ITEM NAMING `OPTIN` AND [OPT-IN RULES](rules.html#opt-in)." in lines, got)
        expect("standalone image keeps its source", "![CONSENT FLOW DIAGRAM](consent-flow.svg)" in lines, got)
        expect("plain prose translated", "PLAIN PROSE WITH NO CODE AND NO LINKS STAYS AS IT WAS." in lines, got)
        expect(
            "lost placeholder: source sentence kept",
            "Dropped placeholder: `keep-me` must survive." in lines,
            got,
        )
        expect(
            "lost placeholder: logged",
            any("keep-me" not in m and "Dropped placeholder: {code0}" in m for m in capture.messages),
            capture.messages,
        )
        expect("reference definition kept", "[who]: https://www.who.int/publications" in lines, got)

        # Every code span and link target of the source is in the output, as often.
        for label, pattern in (("code span", CODE_SPAN), ("link target", LINK_TARGET)):
            want = sorted(pattern.findall(PAGE))
            have = sorted(pattern.findall(got))
            expect(f"every {label} survives", want == have, (want, have))

    # --- Extractor and injector derive the same msgid ---
    for raw in (
        "Set `a_b` and *it* to [x `y`](z.html) or [r][ref], {{ site.data_x }}.",
        "No code, **bold**, _italic_, <b>html</b>, {{ count }} items.",
    ):
        expect("extractor and injector agree", EXT._clean_markdown_text(raw) == INJ._clean_md_for_lookup(raw), raw)

    if failures:
        for f in failures:
            print(f"FAIL {f}", file=sys.stderr)
        return 1
    print("ok: inline code, inline and reference links, code in link text round-trip")
    return 0


if __name__ == "__main__":
    sys.exit(main())
