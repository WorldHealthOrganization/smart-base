"""
FSH (FHIR Shorthand) utility helpers for DAK skill actions.

Provides helpers for reading, validating, and generating small FSH snippets
used by BPMN import and DAK authoring skills.
"""

import re
from pathlib import Path
from typing import Optional


def fsh_id_safe(raw_id: str) -> str:
    """Sanitize a string to a valid FSH instance identifier.

    FSH identifiers allow ``[A-Za-z0-9\\-\\.]``.  Characters outside that
    set are replaced with ``-``.
    """
    return re.sub(r"[^A-Za-z0-9.\-]", "-", raw_id)


def actor_fsh_path(ig_root: str, bare_id: str) -> Path:
    """Return the expected path for an ActorDefinition FSH file.

    Convention from ``bpmn2fhirfsh.xsl``:
        ``input/fsh/actors/ActorDefinition-DAK.<bare_id>.fsh``
    """
    return Path(ig_root) / "input" / "fsh" / "actors" / f"ActorDefinition-DAK.{bare_id}.fsh"


def instance_exists(ig_root: str, bare_id: str) -> bool:
    """Check whether an ActorDefinition FSH file exists for *bare_id*."""
    return actor_fsh_path(ig_root, bare_id).is_file()


def read_fsh_instance_id(fsh_path: Path) -> Optional[str]:
    """Extract the ``Instance:`` identifier from a FSH file, if present."""
    if not fsh_path.is_file():
        return None
    text = fsh_path.read_text(encoding="utf-8")
    match = re.search(r"^Instance:\s*(\S+)", text, re.MULTILINE)
    return match.group(1) if match else None
