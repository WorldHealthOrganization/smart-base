"""
Strip ELM binary data from Library resources — post-build processing.

Extracts base64-encoded ELM payloads (application/elm+json,
application/elm+xml) from Library resource files produced by the IG
Publisher, writes the decoded content to standalone files, and replaces
inline ``data`` with ``url`` references.  Also injects an interactive
ELM viewer into Library HTML pages.

This action wraps ``input/scripts/strip_library_binaries.py`` so it
can be invoked as a skill command.

Environment variables:
    DAK_IG_ROOT   — IG root directory (default: current directory)
"""

import os
import sys
from pathlib import Path

_SKILLS_ROOT = Path(__file__).resolve().parent.parent.parent
if str(_SKILLS_ROOT) not in sys.path:
    sys.path.insert(0, str(_SKILLS_ROOT))

from common.ig_errors import error, info, format_issues, has_errors


def main() -> None:
    ig_root = Path(os.environ.get("DAK_IG_ROOT", "."))
    output_dir = ig_root / "output"

    if not output_dir.is_dir():
        print(format_issues([error(
            "ELM-001",
            f"Output directory does not exist: {output_dir}. "
            "Run the IG Publisher build first.",
        )]))
        sys.exit(1)

    # Import the strip script from input/scripts/
    script_path = ig_root / "input" / "scripts" / "strip_library_binaries.py"
    if not script_path.is_file():
        print(format_issues([error(
            "ELM-002",
            f"strip_library_binaries.py not found at {script_path}",
        )]))
        sys.exit(1)

    # Import and run the script's processing functions directly.
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "strip_library_binaries", str(script_path)
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    print("📦 Extracting ELM binary data from Library resources...")

    json_count = module.strip_library_json(output_dir)
    xml_count = module.strip_library_xml(output_dir)
    ttl_count = module.strip_library_ttl(output_dir)
    html_count = module.strip_library_html(output_dir)

    total = json_count + xml_count + ttl_count + html_count
    issues = [info(
        "ELM-100",
        f"Processed {total} file(s): "
        f"{json_count} JSON, {xml_count} XML, "
        f"{ttl_count} TTL, {html_count} HTML",
    )]
    print(format_issues(issues))

    if total > 0:
        print(f"✅ ELM binary data extracted from {total} Library file(s).")
    else:
        print("ℹ️  No Library resources with ELM data found.")


if __name__ == "__main__":
    main()
