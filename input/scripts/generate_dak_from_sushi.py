#!/usr/bin/env python3
"""
Generate the DAK section of index.config.json from sushi-config.yaml

This script processes an existing FHIR Implementation Guide sushi-config.yaml file
and writes the corresponding `contentTypes.dak` section of index.config.json,
which is the DAK indicator.
It uses only the Python standard library and YAML parsing to avoid dependency on SUSHI.

Usage:
    python generate_dak_from_sushi.py [path_to_sushi_config] [repo_root]
    
If no paths are provided, it looks for sushi-config.yaml in the current directory
and writes it into ./index.config.json (or <root>/index.config.json).
"""

import json
import os
import sys
import yaml
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List, Optional


def load_sushi_config(config_path: Path) -> Dict[str, Any]:
    """Load and parse the sushi-config.yaml file."""
    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Error: sushi-config.yaml not found at {config_path}")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        sys.exit(1)


def convert_publisher(sushi_publisher: Any) -> Dict[str, str]:
    """Convert publisher information from sushi config to DAK format."""
    if isinstance(sushi_publisher, dict):
        return {
            "name": sushi_publisher.get("name", ""),
            "url": sushi_publisher.get("url", ""),
            **({"email": sushi_publisher["email"]} if sushi_publisher.get("email") else {})
        }
    elif isinstance(sushi_publisher, str):
        return {"name": sushi_publisher}
    else:
        return {"name": ""}


def generate_publication_url(repo_name: str, canonical_url: str) -> str:
    """Generate publication URL based on repository ownership and name."""
    # Check if this is a WorldHealthOrganization repository
    if os.getenv('GITHUB_REPOSITORY', '').startswith('WorldHealthOrganization/'):
        # Extract stub by removing 'smart-' prefix if present
        stub = repo_name
        if stub.startswith('smart-'):
            stub = stub[6:]  # Remove 'smart-' prefix
        return f"https://smart.who.int/{stub}"
    else:
        # For non-WHO repositories, use canonical URL or default pattern
        if canonical_url:
            return canonical_url
        # Fallback to GitHub Pages pattern
        github_repo = os.getenv('GITHUB_REPOSITORY', '')
        if github_repo:
            return f"https://{github_repo.split('/')[0]}.github.io/{github_repo.split('/')[1]}"
        return canonical_url or ""


def generate_preview_url(repo_name: str) -> str:
    """Generate preview URL for current CI build."""
    github_repo = os.getenv('GITHUB_REPOSITORY', '')
    if github_repo:
        profile, repo = github_repo.split('/')
        return f"https://{profile}.github.io/{repo}"
    # Fallback for local development
    return f"https://worldhealthorganization.github.io/{repo_name}"


def is_release_branch() -> bool:
    """Check if current branch is a release branch (prefixed with 'release-')."""
    branch_name = os.getenv('GITHUB_REF_NAME', os.getenv('BRANCH_NAME', ''))
    return branch_name.startswith('release-')


def generate_dak_json(sushi_config: Dict[str, Any]) -> Dict[str, Any]:
    """Generate the DAK declaration from sushi-config.yaml."""
    
    # Extract repository information
    repo_id = sushi_config.get("id", "")
    repo_name = repo_id.split('.')[-1] if '.' in repo_id else repo_id
    canonical_url = sushi_config.get("canonical", "")
    
    # Generate URLs based on branch type and repository ownership
    if is_release_branch():
        # For release branches, use publication URL for canonical references
        publication_url = generate_publication_url(repo_name, canonical_url)
        preview_url = generate_preview_url(repo_name)
        # Use publication URL as canonical URL for release branches
        effective_canonical = publication_url
    else:
        # For non-release branches, use preview URL
        publication_url = generate_publication_url(repo_name, canonical_url)
        preview_url = generate_preview_url(repo_name)
        # Use preview URL as canonical URL for development branches
        effective_canonical = preview_url
    
    # Core DAK identity (mapped from sushi config)
    dak = {
        "resourceType": "DAK",
        "resourceDefinition": "http://smart.who.int/base/StructureDefinition/DAK",
        "id": repo_id,
        "name": sushi_config.get("name", ""),
        "title": sushi_config.get("title", ""),
        "description": sushi_config.get("description", ""),
        "version": sushi_config.get("version", "0.1.0"),
        "status": sushi_config.get("status", "draft"),
        "publicationUrl": publication_url,
        "previewUrl": preview_url,
        "canonicalUrl": effective_canonical,
        "license": sushi_config.get("license", "CC0-1.0"),
        "copyrightYear": sushi_config.get("copyrightYear", str(datetime.now().year)),
        "publisher": convert_publisher(sushi_config.get("publisher", {}))
    }
    
    return dak


def check_smart_base_dependency(sushi_config: Dict[str, Any]) -> bool:
    """Check if this repository should generate DAK configuration."""
    
    # Check if this is the smart-base repository
    repo_id = sushi_config.get('id', '')
    is_smart_base_repo = repo_id == 'smart.who.int.base'
    
    if is_smart_base_repo:
        print(f"This is the smart-base repository (id: {repo_id})")
        return True
    
    # Check if smart-base is listed as a dependency
    dependencies = sushi_config.get('dependencies', {})
    
    # Check for various possible smart-base dependency names
    smart_base_patterns = [
        'smart-base',
        'smart.who.int.base',
        'who.smart.base',
        'smart.base'
    ]
    
    for dep_name in dependencies.keys():
        for pattern in smart_base_patterns:
            if pattern in dep_name.lower():
                print(f"Found smart-base dependency: {dep_name}")
                return True
    
    print("This is not the smart-base repository and smart-base is not listed as a dependency. Skipping DAK generation.")
    return False


def main():
    """Process command line arguments and write the DAK section."""
    
    # Parse command line arguments
    if len(sys.argv) > 1:
        sushi_path = Path(sys.argv[1])
    else:
        sushi_path = Path("sushi-config.yaml")
    
    # The DAK declaration is the `dak` section of the root index.config.json
    # (owner, 2026-10-24; it was dak.json). An optional second argument names
    # the repository root that holds the index.
    from dak_index import dak_index_path, read_dak_section, write_dak_section
    repo_root = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(".")
    output_path = dak_index_path(repo_root)

    # Check if sushi config exists
    if not sushi_path.exists():
        print(f"Error: {sushi_path} does not exist")
        sys.exit(1)

    # Check if the DAK section already exists
    if read_dak_section(repo_root) is not None:
        print(f"DAK configuration already exists in {output_path} (contentTypes.dak), skipping generation")
        return

    print(f"Reading sushi configuration from: {sushi_path}")
    
    # Load and check dependencies
    sushi_config = load_sushi_config(sushi_path)
    
    # Check if we should generate DAK configuration
    if not check_smart_base_dependency(sushi_config):
        return
    
    # Generate DAK configuration
    dak_config = generate_dak_json(sushi_config)
    
    # Write output
    try:
        write_dak_section(dak_config, repo_root)
        print(f"Successfully generated DAK configuration: {output_path} (contentTypes.dak)")
        print(f"DAK ID: {dak_config['id']}")
        print(f"DAK Title: {dak_config['title']}")
        print(f"Publication URL: {dak_config['publicationUrl']}")
        print(f"Preview URL: {dak_config['previewUrl']}")
        print(f"Canonical URL: {dak_config['canonicalUrl']}")
        print(f"Is Release Branch: {is_release_branch()}")
    except (IOError, ValueError) as e:
        print(f"Error writing output file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()