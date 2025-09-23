#!/usr/bin/env python3
"""
DAK URL Utilities

Shared utilities for generating publication and preview URLs for DAK-enabled repositories.
These utilities are used by PR comment scripts and other build tools to determine
the appropriate URLs based on repository configuration and branch context.
"""

import json
import os
from pathlib import Path
from typing import Dict, Any, Optional, Tuple


def load_dak_config(dak_path: Path = None) -> Optional[Dict[str, Any]]:
    """Load dak.json configuration if it exists."""
    if dak_path is None:
        dak_path = Path("dak.json")
    
    if not dak_path.exists():
        return None
    
    try:
        with open(dak_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        return None


def generate_dak_publication_url(repo_name: str, canonical_url: str = "") -> str:
    """Generate publication URL based on repository ownership and name."""
    # Check if this is a WorldHealthOrganization repository
    github_repo = os.getenv('GITHUB_REPOSITORY', '')
    if github_repo.startswith('WorldHealthOrganization/'):
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
        if github_repo:
            profile, repo = github_repo.split('/')
            return f"https://{profile}.github.io/{repo}"
        return canonical_url or ""


def generate_dak_preview_url(repo_name: str = "") -> str:
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


def get_deployment_urls(branch: str, repository: str = "") -> Tuple[str, str]:
    """
    Get appropriate deployment URLs based on DAK configuration and branch context.
    
    Returns:
        Tuple[str, str]: (deployment_url, base_url) where:
        - deployment_url: The URL for the specific branch deployment
        - base_url: The base URL for the repository
    """
    # Load DAK configuration if available
    dak_config = load_dak_config()
    
    if dak_config:
        # Use DAK-specific URL logic
        repo_name = repository.split('/')[-1] if repository else ""
        
        if is_release_branch():
            # For release branches, use publication URL as base
            base_url = dak_config.get('publicationUrl', generate_dak_publication_url(repo_name))
        else:
            # For non-release branches, use preview URL as base
            base_url = dak_config.get('previewUrl', generate_dak_preview_url(repo_name))
        
        # Generate branch-specific URL
        if branch == 'main':
            deployment_url = base_url
        else:
            # Extract branch suffix for URL
            branch_for_url = branch.split('/')[-1] if '/' in branch else branch
            deployment_url = f"{base_url.rstrip('/')}/branches/{branch_for_url}"
    else:
        # Fallback to GitHub Pages pattern for non-DAK repositories
        github_repo = repository or os.getenv('GITHUB_REPOSITORY', '')
        if github_repo:
            profile, repo = github_repo.split('/')
            base_url = f"https://{profile}.github.io/{repo}"
        else:
            base_url = "https://worldhealthorganization.github.io/smart-base"
        
        if branch == 'main':
            deployment_url = f"{base_url}/"
        else:
            branch_for_url = branch.split('/')[-1] if '/' in branch else branch
            deployment_url = f"{base_url}/branches/{branch_for_url}/"
    
    return deployment_url, base_url


def get_canonical_url_for_branch(branch: str, repository: str = "") -> str:
    """Get the canonical URL that should be used for the given branch."""
    dak_config = load_dak_config()
    
    if dak_config:
        if is_release_branch():
            return dak_config.get('publicationUrl', dak_config.get('canonicalUrl', ''))
        else:
            return dak_config.get('previewUrl', dak_config.get('canonicalUrl', ''))
    else:
        # Fallback for non-DAK repositories
        deployment_url, _ = get_deployment_urls(branch, repository)
        return deployment_url