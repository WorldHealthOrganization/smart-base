#!/usr/bin/env python3
"""Upload large IG Publisher output files as GitHub Release binary assets.

This script:
1. Reads the IG version from sushi-config.yaml
2. Finds large binary artifacts in the output directory
3. Determines the next available semver tag (appending .N if needed)
4. Creates a GitHub Release and uploads the assets
5. Removes the uploaded files from the output directory so they
   don't bloat the gh-pages deployment

Requires:
  - GITHUB_TOKEN environment variable
  - GITHUB_REPOSITORY environment variable (owner/repo)
  - PyYAML and requests Python packages

Usage:
  python3 create_package_release.py [--output-dir ./output] [--dry-run]
"""

import argparse
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

import requests
import yaml

# Files to extract as release assets (matched by name in output/)
RELEASE_ASSET_PATTERNS = [
    "package.db",
    "package.tgz",
    "package.r4.tgz",
    "package.r4b.tgz",
    "ai.zip",
]

# MIME types for upload
MIME_TYPES = {
    ".db": "application/x-sqlite3",
    ".tgz": "application/gzip",
    ".zip": "application/zip",
}


def read_ig_version(repo_root: Path) -> str:
    """Read the version field from sushi-config.yaml."""
    config_path = repo_root / "sushi-config.yaml"
    if not config_path.exists():
        raise FileNotFoundError(f"sushi-config.yaml not found at {config_path}")
    with open(config_path) as f:
        config = yaml.safe_load(f)
    version = config.get("version")
    if not version:
        raise ValueError("No 'version' field found in sushi-config.yaml")
    version = str(version)
    # Validate semver format to prevent tag injection
    if not re.match(r"^\d+\.\d+\.\d+(-[a-zA-Z0-9.]+)?$", version):
        raise ValueError(f"Invalid semver version in sushi-config.yaml: {version!r}")
    return version


def get_existing_tags(token: str, repo: str, version_prefix: str) -> list[str]:
    """List existing tags that start with the given version prefix."""
    tags = []
    url = f"https://api.github.com/repos/{repo}/tags"
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github+json"}
    page = 1
    while True:
        resp = requests.get(url, headers=headers, params={"per_page": 100, "page": page})
        resp.raise_for_status()
        batch = resp.json()
        if not batch:
            break
        for tag in batch:
            name = tag["name"]
            # Match vX.Y.Z or vX.Y.Z.N
            bare = name.lstrip("v")
            if bare == version_prefix or bare.startswith(version_prefix + "."):
                tags.append(bare)
        page += 1
    return tags


def next_release_version(base_version: str, existing_tags: list[str]) -> str:
    """Determine the next release version.

    If vX.Y.Z doesn't exist yet, use X.Y.Z.
    If it does, find the highest X.Y.Z.N and return X.Y.Z.(N+1).
    """
    if base_version not in existing_tags:
        return base_version

    # Find highest .N suffix
    max_n = 0
    pattern = re.compile(re.escape(base_version) + r"\.(\d+)$")
    for tag in existing_tags:
        m = pattern.match(tag)
        if m:
            max_n = max(max_n, int(m.group(1)))

    return f"{base_version}.{max_n + 1}"


def find_release_assets(output_dir: Path) -> list[Path]:
    """Find files in output_dir matching RELEASE_ASSET_PATTERNS."""
    assets = []
    for pattern in RELEASE_ASSET_PATTERNS:
        candidate = output_dir / pattern
        if candidate.exists() and candidate.is_file():
            assets.append(candidate)
    return assets


def create_release(token: str, repo: str, tag: str, name: str, body: str, commitish: str) -> dict:
    """Create a GitHub Release."""
    url = f"https://api.github.com/repos/{repo}/releases"
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github+json"}
    data = {
        "tag_name": f"v{tag}",
        "target_commitish": commitish,
        "name": name,
        "body": body,
        "draft": False,
        "prerelease": False,
    }
    resp = requests.post(url, headers=headers, json=data)
    resp.raise_for_status()
    return resp.json()


def upload_asset(token: str, upload_url: str, filepath: Path) -> dict:
    """Upload a file as a release asset."""
    # upload_url has {?name,label} suffix — strip it
    upload_url = upload_url.split("{")[0]
    suffix = filepath.suffix
    content_type = MIME_TYPES.get(suffix, "application/octet-stream")
    headers = {
        "Authorization": f"token {token}",
        "Content-Type": content_type,
        "Accept": "application/vnd.github+json",
    }
    with open(filepath, "rb") as f:
        resp = requests.post(
            upload_url,
            headers=headers,
            params={"name": filepath.name},
            data=f,
        )
    resp.raise_for_status()
    return resp.json()


def main():
    parser = argparse.ArgumentParser(description="Create GitHub Release with IG package assets")
    parser.add_argument("--output-dir", default="./output", help="IG Publisher output directory")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done without creating a release")
    args = parser.parse_args()

    token = os.environ.get("GITHUB_TOKEN", "")
    repo = os.environ.get("GITHUB_REPOSITORY", "")
    commitish = os.environ.get("GITHUB_SHA", "HEAD")
    branch_name = os.environ.get("BRANCH_NAME", "unknown")

    if not token and not args.dry_run:
        print("ERROR: GITHUB_TOKEN is required", file=sys.stderr)
        sys.exit(1)
    if not repo and not args.dry_run:
        print("ERROR: GITHUB_REPOSITORY is required", file=sys.stderr)
        sys.exit(1)

    repo_root = Path(".")
    output_dir = Path(args.output_dir)

    # 1. Read IG version
    ig_version = read_ig_version(repo_root)
    print(f"IG version from sushi-config.yaml: {ig_version}")

    # 2. Find assets
    assets = find_release_assets(output_dir)
    if not assets:
        print("No release assets found in output directory — skipping release creation")
        return

    print(f"Found {len(assets)} release asset(s):")
    for a in assets:
        size_mb = a.stat().st_size / (1024 * 1024)
        flag = " ⚠️  (>=100 MB — would be stripped from gh-pages)" if size_mb >= 100 else ""
        print(f"  {a.name} ({size_mb:.1f} MB){flag}")

    # 3. Determine next version tag
    if not args.dry_run:
        existing = get_existing_tags(token, repo, ig_version)
    else:
        existing = []
    release_version = next_release_version(ig_version, existing)
    print(f"Release version: v{release_version}")

    if args.dry_run:
        print("DRY RUN — would create release and upload assets, then remove from output/")
        return

    # 4. Create release
    release_name = f"FHIR Package v{release_version}"
    body_lines = [
        f"Automated FHIR package release for IG version **{ig_version}**.",
        f"",
        f"Branch: `{branch_name}`",
        f"Commit: `{commitish[:12]}`",
        f"",
        f"### Assets",
    ]
    for a in assets:
        size_mb = a.stat().st_size / (1024 * 1024)
        body_lines.append(f"- **{a.name}** ({size_mb:.1f} MB)")

    body = "\n".join(body_lines)

    print(f"Creating release: {release_name}")
    release = create_release(token, repo, release_version, release_name, body, commitish)
    upload_url = release["upload_url"]
    release_html_url = release["html_url"]
    print(f"Release created: {release_html_url}")

    # 5. Upload assets
    for asset_path in assets:
        print(f"Uploading {asset_path.name}...")
        result = upload_asset(token, upload_url, asset_path)
        print(f"  Uploaded: {result['browser_download_url']}")

    # 6. Remove uploaded files from output dir
    for asset_path in assets:
        print(f"Removing {asset_path.name} from output directory")
        asset_path.unlink()

    print(f"\nRelease complete: {release_html_url}")

    # Export release URL for downstream steps
    github_output = os.environ.get("GITHUB_OUTPUT", "")
    if github_output:
        with open(github_output, "a") as f:
            f.write(f"release_url={release_html_url}\n")
            f.write(f"release_version=v{release_version}\n")


if __name__ == "__main__":
    main()
