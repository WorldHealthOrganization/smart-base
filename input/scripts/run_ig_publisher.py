#!/usr/bin/env python3
"""
FHIR IG Publisher Runner with automatic .pot file commit

This script is a companion to the WHO SMART Guidelines DAK extraction pipeline.
After the main extraction pipeline has generated FSH/CQL/page-content files,
this script:

  1. Invokes the FHIR IG Publisher (``java -jar publisher.jar -ig .``) as a
     subprocess so that SUSHI and the publisher can compile the generated
     resources into a complete FHIR Implementation Guide.

  2. Detects any new or modified Gettext ``.pot`` translation-template files
     that were produced by the run — both from the IG Publisher's own i18n
     output and from directories tracked by ``extract_translations.py``.

  3. Stages and commits those ``.pot`` files to the local git repository so
     that translation-template updates are never accidentally omitted from
     version control.

Error handling:
  - If the IG Publisher exits with a non-zero return code the script stops
    immediately and does **not** commit any partial artefacts.
  - If ``git`` is not available the commit step is skipped with a warning.

Usage::

    python run_ig_publisher.py [options]

Options::

    --ig-root DIR          Repository root (default: current directory)
    --publisher-jar PATH   Explicit path to publisher.jar
                           (default: auto-detected from input-cache/ or ../)
    --tx URL               Terminology server URL; use ``n/a`` for offline mode
    --skip-commit          Run publisher and detect .pot files but do not commit
    --commit-message MSG   Custom git commit message for the .pot update
    --help / -h            Print this help

Author: WHO SMART Guidelines Team
"""

import argparse
import datetime
import glob as glob_module
import logging
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import List, Optional

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Publisher jar discovery
# ---------------------------------------------------------------------------

#: Paths (relative to ig_root) that are checked for publisher.jar in order.
_PUBLISHER_JAR_SEARCH_PATHS: List[str] = [
    "input-cache/publisher.jar",
    "../publisher.jar",
    "publisher.jar",
]


def find_publisher_jar(
    ig_root: str,
    explicit_path: Optional[str] = None,
) -> Optional[str]:
    """Locate the FHIR IG Publisher jar file.

    Mirrors the search order used by ``_genonce.sh``:

    * ``input-cache/publisher.jar``  (preferred)
    * ``../publisher.jar``           (fallback used in some CI setups)

    An *explicit_path* (relative or absolute) always takes precedence.

    Args:
        ig_root:       Repository root directory.
        explicit_path: Optional caller-supplied path to the jar.

    Returns:
        Absolute path string if found, or ``None`` otherwise.
    """
    if explicit_path:
        candidate = Path(explicit_path)
        if not candidate.is_absolute():
            candidate = Path(ig_root) / explicit_path
        if candidate.exists():
            logger.info(f"Using explicitly specified publisher jar: {candidate}")
            return str(candidate)
        logger.error(f"Specified publisher jar not found: {explicit_path}")
        return None

    for rel in _PUBLISHER_JAR_SEARCH_PATHS:
        candidate = Path(ig_root) / rel
        if candidate.exists():
            logger.info(f"Found publisher jar at: {candidate}")
            return str(candidate)

    return None


# ---------------------------------------------------------------------------
# IG Publisher invocation
# ---------------------------------------------------------------------------


def run_ig_publisher(
    ig_root: str,
    publisher_jar: str,
    tx: Optional[str] = None,
    extra_args: Optional[List[str]] = None,
) -> bool:
    """Invoke the FHIR IG Publisher as a child process.

    The publisher is run with ``-ig .`` so it reads ``ig.ini`` /
    ``sushi-config.yaml`` from *ig_root*.

    Args:
        ig_root:        Working directory (repository root).
        publisher_jar:  Absolute path to ``publisher.jar``.
        tx:             Optional terminology server URL.  Pass ``"n/a"`` to
                        disable external terminology lookups.
        extra_args:     Additional flags forwarded verbatim to the publisher.

    Returns:
        ``True`` if the publisher exited with code 0, ``False`` otherwise.
    """
    cmd: List[str] = ["java", "-jar", publisher_jar, "-ig", "."]
    if tx:
        cmd += ["-tx", tx]
    if extra_args:
        cmd.extend(extra_args)

    logger.info(f"Running IG Publisher: {' '.join(cmd)}")
    logger.info(f"Working directory  : {ig_root}")

    try:
        result = subprocess.run(
            cmd,
            cwd=ig_root,
            check=False,          # inspect returncode ourselves
            capture_output=False,  # let stdout/stderr flow to the terminal
        )
    except FileNotFoundError:
        logger.error(
            "'java' executable not found. "
            "Ensure Java is installed and available on PATH."
        )
        return False
    except Exception as exc:  # pragma: no cover
        logger.exception(f"Unexpected error invoking IG Publisher: {exc}")
        return False

    if result.returncode != 0:
        logger.error(
            f"IG Publisher exited with non-zero return code: {result.returncode}"
        )
        return False

    logger.info("IG Publisher completed successfully.")
    return True


# ---------------------------------------------------------------------------
# .pot file discovery
# ---------------------------------------------------------------------------

#: Repository-relative directories that may contain .pot translation files
#: produced by ``extract_translations.py``.
#: Note: the IG Publisher ``output/`` directory is excluded here because it is
#: listed in ``.gitignore`` and its contents cannot be committed to the source
#: branch.
_POT_SEARCH_DIRS: List[str] = [
    "input/fsh/translations",
    "input/images-source/translations",
    "input/images/translations",
    "input/archimate/translations",
    "input/diagrams/translations",
]


# git status --porcelain line layout: "XY <path>"
_GIT_STATUS_MIN_LINE_LEN: int = 3
_GIT_STATUS_PATH_START: int = 3


def find_changed_pot_files(ig_root: str) -> List[str]:
    """Detect new or modified ``.pot`` files using ``git status``.

    Uses ``git status --porcelain`` so that only files that actually differ
    from the current index/HEAD are returned.

    Args:
        ig_root: Repository root directory.

    Returns:
        List of repository-relative paths (as reported by git) for every
        ``.pot`` file that is new, modified, or staged.  Empty list on error.
    """
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=ig_root,
            capture_output=True,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError as exc:
        logger.warning(f"'git status' failed: {exc}")
        return []
    except FileNotFoundError:
        logger.warning("'git' executable not found; skipping git-status detection.")
        return []

    changed: List[str] = []
    for line in result.stdout.splitlines():
        # git status --porcelain format: "XY <path>" (path starts at col 3)
        if len(line) >= _GIT_STATUS_MIN_LINE_LEN and line[2] == " ":
            filepath = line[_GIT_STATUS_PATH_START:].strip()
            if filepath.endswith(".pot"):
                changed.append(filepath)

    return changed


def find_pot_files_in_dirs(ig_root: str) -> List[str]:
    """Find all ``.pot`` files under the known translation output directories.

    This supplements git-status-based detection for freshly initialised
    repositories where new files might be untracked.

    Args:
        ig_root: Repository root directory.

    Returns:
        Repository-relative paths for every ``.pot`` file found.
    """
    found: List[str] = []
    for search_dir in _POT_SEARCH_DIRS:
        abs_dir = os.path.join(ig_root, search_dir)
        pattern = os.path.join(abs_dir, "**", "*.pot")
        for pot_file in glob_module.glob(pattern, recursive=True):
            rel = os.path.relpath(pot_file, ig_root)
            found.append(rel)
    return found


# ---------------------------------------------------------------------------
# git staging and commit
# ---------------------------------------------------------------------------


def git_stage_and_commit(
    ig_root: str,
    files: List[str],
    commit_message: str,
) -> bool:
    """Stage *files* and create a git commit.

    Args:
        ig_root:        Repository root directory (used as git working dir).
        files:          Repository-relative paths to stage.
        commit_message: Message for the new commit.

    Returns:
        ``True`` if the commit was created (or there was nothing to commit),
        ``False`` if a git command failed.
    """
    if not files:
        logger.info("No .pot files to commit.")
        return True

    # Stage the files
    try:
        subprocess.run(
            ["git", "add", "--"] + files,
            cwd=ig_root,
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError as exc:
        logger.error(f"'git add' failed: {exc.stderr.strip()}")
        return False
    except FileNotFoundError:
        logger.error("'git' executable not found; cannot commit .pot files.")
        return False

    # Check whether anything was actually staged
    try:
        diff_result = subprocess.run(
            ["git", "diff", "--cached", "--quiet"],
            cwd=ig_root,
            check=False,
            capture_output=True,
        )
    except FileNotFoundError:
        logger.error("'git' executable not found; cannot verify staged changes.")
        return False

    if diff_result.returncode == 0:
        logger.info("No staged changes detected in .pot files — nothing to commit.")
        return True

    # Create the commit
    try:
        subprocess.run(
            ["git", "commit", "-m", commit_message],
            cwd=ig_root,
            check=True,
            capture_output=True,
            text=True,
        )
        logger.info(f"Committed .pot file updates with message: {commit_message!r}")
        return True
    except subprocess.CalledProcessError as exc:
        logger.error(f"'git commit' failed: {exc.stderr.strip()}")
        return False


# ---------------------------------------------------------------------------
# Translation extraction (post-publisher)
# ---------------------------------------------------------------------------


def _run_extract_translations(ig_root: str) -> None:
    """Run ``extract_translations.py`` to regenerate ``.pot`` files.

    Called automatically after the IG Publisher succeeds so that the
    translation templates reflect the latest diagram sources.  Failures are
    logged as warnings rather than errors — missing diagram sources should not
    block the commit of whatever ``.pot`` files are already present.

    Args:
        ig_root: Repository root directory.
    """
    script_path = os.path.join(ig_root, "input", "scripts", "extract_translations.py")
    if not os.path.exists(script_path):
        logger.warning(
            f"extract_translations.py not found at {script_path}; "
            "skipping translation template regeneration."
        )
        return

    # Derive canonical URL from sushi-config.yaml if present
    canonical = _read_canonical_from_sushi(ig_root)

    cmd: List[str] = [
        sys.executable,
        script_path,
        "--ig-root", ig_root,
    ]
    if canonical:
        cmd += ["--canonical", canonical]

    logger.info(f"Regenerating .pot files via extract_translations.py: {' '.join(cmd)}")
    try:
        result = subprocess.run(cmd, cwd=ig_root, check=False)
        if result.returncode != 0:
            logger.warning(
                f"extract_translations.py exited with code {result.returncode}; "
                "some .pot files may be missing or outdated."
            )
        else:
            logger.info("extract_translations.py completed successfully.")
    except Exception as exc:
        logger.warning(f"Could not run extract_translations.py: {exc}")


def _read_canonical_from_sushi(ig_root: str) -> Optional[str]:
    """Parse the ``canonical`` field from ``sushi-config.yaml``.

    Args:
        ig_root: Repository root directory.

    Returns:
        The canonical URL string, or ``None`` if it cannot be read.
    """
    config_path = os.path.join(ig_root, "sushi-config.yaml")
    if not os.path.exists(config_path):
        return None
    try:
        # Use a simple regex to extract the top-level ``canonical:`` field
        # without requiring PyYAML as an additional import.
        with open(config_path, "r", encoding="utf-8") as fh:
            for line in fh:
                m = re.match(r"^canonical\s*:\s*(.+)$", line)
                if m:
                    return m.group(1).strip().strip("'\"")
    except Exception as exc:
        logger.debug(f"Could not read canonical from sushi-config.yaml: {exc}")
    return None


# ---------------------------------------------------------------------------
# Full pipeline orchestrator
# ---------------------------------------------------------------------------


def run_publisher_and_commit_pot(
    ig_root: str,
    publisher_jar: Optional[str] = None,
    tx: Optional[str] = None,
    skip_commit: bool = False,
    commit_message: Optional[str] = None,
) -> bool:
    """Run the IG Publisher and automatically commit any updated .pot files.

    This is the high-level entry point used both by the CLI and by
    ``extract_dak.py`` when ``--run-publisher`` is supplied.

    Workflow:

    1. Locate ``publisher.jar`` (abort early if not found).
    2. Invoke the IG Publisher — on failure stop here so no partial artefacts
       are committed.
    3. Collect all new/modified ``.pot`` files from the output directories.
    4. Stage and commit them (unless *skip_commit* is ``True``).

    Args:
        ig_root:        Repository root directory.
        publisher_jar:  Optional explicit path to ``publisher.jar``.
        tx:             Optional terminology server URL.
        skip_commit:    When ``True`` the function still runs the publisher and
                        reports what it found, but does not create a git commit.
        commit_message: Custom commit message; a sensible default is used when
                        ``None``.

    Returns:
        ``True`` on success, ``False`` if the publisher failed or a git
        operation failed.
    """
    # 1. Locate publisher jar
    jar_path = find_publisher_jar(ig_root, publisher_jar)
    if not jar_path:
        logger.error(
            "FHIR IG Publisher jar not found. "
            "Run _updatePublisher.sh to download it, or supply --publisher-jar."
        )
        return False

    # 2. Run IG Publisher — abort on failure to avoid partial commits
    if not run_ig_publisher(ig_root, jar_path, tx=tx):
        logger.error(
            "IG Publisher failed. "
            "Aborting .pot file commit to avoid committing incomplete templates."
        )
        return False

    # 2b. Run extract_translations.py to regenerate .pot files from diagram sources
    _run_extract_translations(ig_root)

    if skip_commit:
        logger.info("--skip-commit specified; skipping .pot detection and commit.")
        return True

    # 3. Detect changed / new .pot files
    changed = find_changed_pot_files(ig_root)
    all_in_dirs = find_pot_files_in_dirs(ig_root)
    # Merge, deduplicate, preserve insertion order
    unique_paths: dict = {}
    for path in changed + all_in_dirs:
        unique_paths[path] = None
    all_pot_paths: List[str] = list(unique_paths.keys())

    if not all_pot_paths:
        logger.info("No .pot files found after IG Publisher run; nothing to commit.")
        return True

    logger.info(
        f"Detected {len(all_pot_paths)} .pot file(s) to stage: {all_pot_paths}"
    )

    # 4. Commit
    if commit_message is None:
        timestamp = datetime.datetime.now(datetime.timezone.utc).strftime(
            "%Y-%m-%d %H:%M UTC"
        )
        commit_message = (
            f"chore: update translation templates (.pot) [{timestamp}]\n\n"
            "Regenerated by run_ig_publisher.py after IG Publisher run."
        )

    return git_stage_and_commit(ig_root, all_pot_paths, commit_message)


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------


def main() -> int:
    """Command-line entry point."""
    parser = argparse.ArgumentParser(
        description=(
            "Run the FHIR IG Publisher and automatically commit any updated "
            ".pot translation-template files."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--ig-root",
        default=".",
        help="Repository root directory (default: current directory)",
    )
    parser.add_argument(
        "--publisher-jar",
        default=None,
        metavar="PATH",
        help=(
            "Explicit path to publisher.jar. "
            "Defaults to auto-detection in input-cache/ and ../"
        ),
    )
    parser.add_argument(
        "--tx",
        default=None,
        metavar="URL",
        help="Terminology server URL. Use 'n/a' to disable external lookups.",
    )
    parser.add_argument(
        "--skip-commit",
        action="store_true",
        default=False,
        help=(
            "Run the publisher and report detected .pot files "
            "but do not create a git commit."
        ),
    )
    parser.add_argument(
        "--commit-message",
        default=None,
        metavar="MSG",
        help="Custom git commit message for the .pot file update commit.",
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    ig_root = os.path.abspath(args.ig_root)
    logger.info(f"IG root: {ig_root}")

    success = run_publisher_and_commit_pot(
        ig_root=ig_root,
        publisher_jar=args.publisher_jar,
        tx=args.tx,
        skip_commit=args.skip_commit,
        commit_message=args.commit_message,
    )

    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
