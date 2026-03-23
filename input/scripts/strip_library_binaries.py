#!/usr/bin/env python3
"""
WHO SMART Guidelines — Strip Binary Data from Library Resources

Temporary postprocessing step that removes base64-encoded binary data
from FHIR Library resource JSON files produced by the IG Publisher.

Library resources contain a ``content`` array whose entries carry a
``data`` field with base64-encoded payloads (CQL source, compiled ELM,
etc.).  These payloads can be very large and are not needed in the
published output.  This script replaces every ``data`` value with an
empty string so the structural metadata (contentType, url, …) is
preserved while the bulk binary payload is removed.

Usage:
    python strip_library_binaries.py [output_dir]

Defaults:
    output_dir = ./output

Author: SMART Guidelines Team
"""

import json
import logging
import os
import sys
from pathlib import Path


def setup_logging() -> logging.Logger:
    """Configure logging for the script."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    return logging.getLogger(__name__)


logger = setup_logging()


def strip_library_binary_data(output_dir: str) -> int:
    """Strip base64 data from Library JSON files in *output_dir*.

    Returns the number of files modified.
    """
    output_path = Path(output_dir)
    if not output_path.is_dir():
        logger.error("Output directory does not exist: %s", output_dir)
        return 0

    modified_count = 0

    for fpath in sorted(output_path.glob("Library-*.json")):
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
            if "data" in entry and entry["data"]:
                entry["data"] = ""
                changed = True

        if changed:
            fpath.write_text(
                json.dumps(resource, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
            modified_count += 1
            logger.info("Stripped binary data from %s", fpath.name)

    return modified_count


def main() -> None:
    output_dir = sys.argv[1] if len(sys.argv) > 1 else "output"
    logger.info("Stripping binary data from Library resources in %s", output_dir)
    count = strip_library_binary_data(output_dir)
    logger.info("Done — %d Library file(s) modified", count)


if __name__ == "__main__":
    main()
