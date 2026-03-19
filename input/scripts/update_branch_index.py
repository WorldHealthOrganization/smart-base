#!/usr/bin/env python3
"""Update README.md and generate output/history.html with feature branch build links.

Runs as part of the GitHub Pages build process to keep the repository README
and the CI history page in sync with the current set of deployed feature branches.

Actions performed
-----------------
1. Fetch the list of deployed feature branch directories from the gh-pages branch
   via the GitHub REST API.
2. Generate ``output/history.html`` — a CI-build history page listing all
   feature branch builds (deployed as part of the regular CI output).
3. Update the ``## Publication`` section of ``README.md``, replacing the block
   between ``<!-- CI_BUILD_LINKS_START -->`` and ``<!-- CI_BUILD_LINKS_END -->``
   with current build URLs and a sorted table of feature branch links.
   README.md is only written when its content actually changes (idempotent).

Environment variables
---------------------
GITHUB_REPOSITORY   ``owner/repo`` — always set by GitHub Actions.
GITHUB_TOKEN        Workflow token — optional, reduces API rate-limit risk.
README_UPDATE       Set to ``false`` to skip the README.md update step.

Usage
-----
python3 input/scripts/update_branch_index.py
"""

import html
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _read_env(name: str) -> str:
    return os.environ.get(name, "").strip()


def _github_api(path: str, token: str = "") -> "list | dict | None":
    """Call the GitHub REST API and return parsed JSON, or None on error."""
    url = f"https://api.github.com/{path.lstrip('/')}"
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    try:
        req = Request(url, headers=headers)
        with urlopen(req, timeout=30) as resp:
            return json.loads(resp.read())
    except HTTPError as exc:
        if exc.code == 404:
            # gh-pages branch or branches/ directory not yet created
            print(f"ℹ️  GitHub API 404 (not yet deployed?): {url}")
            return None
        print(f"⚠️  GitHub API HTTP {exc.code}: {url}", file=sys.stderr)
        return None
    except URLError as exc:
        print(f"⚠️  GitHub API network error: {exc}", file=sys.stderr)
        return None


def _fetch_deployed_branches(repo: str, token: str) -> "list[str]":
    """Return sorted list of branch directory names deployed under gh-pages/branches/."""
    data = _github_api(f"repos/{repo}/contents/branches?ref=gh-pages", token)
    if not data or not isinstance(data, list):
        return []
    return sorted(
        item["name"]
        for item in data
        if isinstance(item, dict) and item.get("type") == "dir"
    )


def _load_dak_json(root: Path) -> dict:
    dak_path = root / "dak.json"
    if dak_path.exists():
        try:
            return json.loads(dak_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, IOError):
            pass
    return {}


# ---------------------------------------------------------------------------
# history.html
# ---------------------------------------------------------------------------

_HISTORY_HTML = """\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Branch Builds &mdash; {title_escaped}</title>
  <style>
    body {{
      font-family: system-ui, -apple-system, sans-serif;
      max-width: 960px;
      margin: 2rem auto;
      padding: 0 1rem;
      color: #333;
    }}
    h1 {{ font-size: 1.6rem; margin-bottom: .25rem; }}
    h2 {{ font-size: 1.2rem; margin-top: 2rem; }}
    a {{ color: #0069c2; }}
    table {{ border-collapse: collapse; width: 100%; margin-top: 1rem; }}
    th, td {{ text-align: left; padding: .45rem .75rem; border: 1px solid #ddd; }}
    th {{ background: #f4f4f4; font-weight: 600; }}
    tr:nth-child(even) td {{ background: #fafafa; }}
    .meta {{ color: #666; font-size: .85rem; margin-top: 2rem; }}
  </style>
</head>
<body>
  <h1>Branch Builds &mdash; {title_escaped}</h1>
  <h2>Main builds</h2>
  <table>
    <tr><th>Build type</th><th>URL</th></tr>
    <tr>
      <td>Continuous (CI) build</td>
      <td><a href="{ci_url_escaped}">{ci_url_escaped}</a></td>
    </tr>
    <tr>
      <td>Published build</td>
      <td><a href="{pub_url_escaped}">{pub_url_escaped}</a></td>
    </tr>
  </table>
  <h2>Feature branch builds</h2>
  {branch_block}
  <p class="meta">Generated: {timestamp}</p>
</body>
</html>
"""

_NO_BRANCHES_HTML = "<p><em>No feature branches deployed yet.</em></p>"


def _branch_table_html(branches: "list[str]", ci_base: str) -> str:
    if not branches:
        return _NO_BRANCHES_HTML
    rows = []
    for name in branches:
        url = f"{ci_base.rstrip('/')}/branches/{name}/"
        name_esc = html.escape(name)
        url_esc = html.escape(url)
        rows.append(
            f"    <tr><td><code>{name_esc}</code></td>"
            f'<td><a href="{url_esc}">{url_esc}</a></td></tr>'
        )
    header = "    <tr><th>Branch</th><th>Build URL</th></tr>"
    return "<table>\n" + header + "\n" + "\n".join(rows) + "\n  </table>"


def generate_history_html(
    output_dir: Path,
    branches: "list[str]",
    ci_base: str,
    pub_url: str,
    title: str,
) -> None:
    """Write output/history.html with a table of all feature branch builds."""
    output_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    content = _HISTORY_HTML.format(
        title_escaped=html.escape(title),
        ci_url_escaped=html.escape(ci_base),
        pub_url_escaped=html.escape(pub_url),
        branch_block=_branch_table_html(branches, ci_base),
        timestamp=ts,
    )
    dest = output_dir / "history.html"
    dest.write_text(content, encoding="utf-8")
    print(f"✅ Wrote {dest}")


# ---------------------------------------------------------------------------
# README.md
# ---------------------------------------------------------------------------

# Matches the auto-managed block inside ## Publication, demarcated by comment markers.
_MARKERS_RE = re.compile(
    r"<!-- CI_BUILD_LINKS_START -->.*?<!-- CI_BUILD_LINKS_END -->",
    re.DOTALL,
)


def _branch_table_md(branches: "list[str]", ci_base: str) -> str:
    if not branches:
        return "_No feature branches deployed yet._\n"
    lines = ["| Branch | Build |", "|--------|-------|"]
    for name in branches:
        url = f"{ci_base.rstrip('/')}/branches/{name}/"
        lines.append(f"| `{name}` | [{url}]({url}) |")
    return "\n".join(lines) + "\n"


def _build_marker_block(branches: "list[str]", ci_url: str, pub_url: str) -> str:
    branch_md = _branch_table_md(branches, ci_url)
    return (
        "<!-- CI_BUILD_LINKS_START -->\n"
        f"Continuous Build: [{ci_url}]({ci_url})  \n"
        f"Published: [{pub_url}]({pub_url})\n\n"
        "### Feature Branch Builds\n"
        f"{branch_md}"
        "<!-- CI_BUILD_LINKS_END -->"
    )


def update_readme(
    readme_path: Path,
    branches: "list[str]",
    ci_url: str,
    pub_url: str,
) -> bool:
    """Replace the marker block in README.md.  Return True if the file changed."""
    if not readme_path.exists():
        print(f"⚠️  README.md not found at {readme_path}", file=sys.stderr)
        return False

    original = readme_path.read_text(encoding="utf-8")

    if "<!-- CI_BUILD_LINKS_START -->" not in original:
        print(
            "⚠️  README.md does not contain CI_BUILD_LINKS markers — skipping update.\n"
            "    Add <!-- CI_BUILD_LINKS_START --> and <!-- CI_BUILD_LINKS_END --> markers\n"
            "    inside the ## Publication section to enable automatic updates.",
            file=sys.stderr,
        )
        return False

    new_block = _build_marker_block(branches, ci_url, pub_url)
    updated = _MARKERS_RE.sub(new_block, original, count=1)

    if updated == original:
        print("ℹ️  README.md Publication links are already up-to-date.")
        return False

    readme_path.write_text(updated, encoding="utf-8")
    print("✅ Updated README.md Publication section with current branch build links.")
    return True


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    repo = _read_env("GITHUB_REPOSITORY")
    token = _read_env("GITHUB_TOKEN")
    skip_readme = _read_env("README_UPDATE").lower() == "false"

    root = Path(".")
    dak = _load_dak_json(root)

    # Determine display title
    title = dak.get("title") or (repo.split("/")[-1] if repo else "IG")

    # Determine CI (GitHub Pages preview) and published URLs from dak.json,
    # falling back to the standard GitHub Pages URL pattern.
    if repo:
        owner, repo_name = repo.split("/", 1)
        ci_base = dak.get("previewUrl") or f"https://{owner}.github.io/{repo_name}"
        pub_url = dak.get("publicationUrl") or ci_base
    else:
        ci_base = "https://worldhealthorganization.github.io/smart-base"
        pub_url = ci_base

    # Ensure ci_base ends with a slash for consistent URL construction
    ci_base = ci_base.rstrip("/")

    # Fetch deployed feature branches from gh-pages/branches/
    branches: "list[str]" = []
    if repo:
        branches = _fetch_deployed_branches(repo, token)
        if branches:
            print(f"Found {len(branches)} deployed branch(es): {', '.join(branches)}")
        else:
            print("No feature branches found on gh-pages yet.")

    # 1. Generate output/history.html (deployed as part of every CI build)
    output_dir = root / "output"
    if output_dir.is_dir():
        generate_history_html(output_dir, branches, ci_base, pub_url, title)
    else:
        print(
            "⚠️  output/ directory not found — skipping history.html generation.\n"
            "    (Run this script after the IG Publisher has produced ./output/)",
            file=sys.stderr,
        )

    # 2. Update README.md (only when the markers are present and content changed)
    if not skip_readme:
        changed = update_readme(root / "README.md", branches, ci_base, pub_url)
        # Signal to the caller whether the file was modified so the workflow
        # can decide whether to commit.
        if changed:
            print("README_CHANGED=true")
        else:
            print("README_CHANGED=false")
    else:
        print("ℹ️  README_UPDATE=false — skipping README.md update.")


if __name__ == "__main__":
    main()
