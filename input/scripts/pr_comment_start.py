#!/usr/bin/env python3
"""
PR Comment Script - Deployment Started

Safely posts a PR comment when deployment starts, with proper input validation
and sanitization to prevent injection attacks.

Usage:
    python pr_comment_start.py <pr_number> <repository> <run_id> <sha> <branch> <github_token>
"""

import os
import sys
import json
import re
import requests
from urllib.parse import quote

# Try to import DAK URL utilities, fallback to inline implementation if not available
try:
    from dak_url_utils import get_deployment_urls
    DAK_UTILS_AVAILABLE = True
except ImportError:
    DAK_UTILS_AVAILABLE = False


def sanitize_input(value: str) -> str:
    """Sanitize input to prevent injection attacks."""
    if not value:
        return ""
    
    # Remove any potentially dangerous characters
    # Allow only alphanumeric, hyphens, dots, underscores, and forward slashes for branch names
    sanitized = re.sub(r'[^a-zA-Z0-9\-\._/]', '', str(value))
    
    # Limit length to prevent extremely long inputs
    return sanitized[:200]


def validate_pr_number(pr_number: str) -> int:
    """Validate and convert PR number to integer."""
    try:
        pr_num = int(pr_number)
        if pr_num <= 0 or pr_num > 999999:  # Reasonable bounds
            raise ValueError("PR number out of bounds")
        return pr_num
    except (ValueError, TypeError):
        raise ValueError(f"Invalid PR number: {pr_number}")


def validate_run_id(run_id: str) -> int:
    """Validate and convert run ID to integer."""
    try:
        run_num = int(run_id)
        if run_num <= 0:
            raise ValueError("Run ID must be positive")
        return run_num
    except (ValueError, TypeError):
        raise ValueError(f"Invalid run ID: {run_id}")


def generate_deployment_url(branch: str) -> str:
    """Generate deployment URL with proper sanitization."""
    branch = sanitize_input(branch)
    repository = os.getenv('GITHUB_REPOSITORY', 'WorldHealthOrganization/smart-base')
    
    # Use DAK-aware URL generation if available
    if DAK_UTILS_AVAILABLE:
        try:
            deployment_url, _ = get_deployment_urls(branch, repository)
            return deployment_url
        except Exception:
            # Fallback to default implementation if DAK utils fail
            pass
    
    # Default GitHub Pages implementation
    if branch == 'main':
        return f'https://{repository.split("/")[0].lower()}.github.io/{repository.split("/")[1]}/'
    else:
        # Extract branch suffix after last slash for URL
        branch_for_url = branch.split('/')[-1] if '/' in branch else branch
        branch_for_url = sanitize_input(branch_for_url)
        # URL encode the branch name for safety
        branch_encoded = quote(branch_for_url, safe='')
        profile = repository.split('/')[0].lower()
        repo = repository.split('/')[1]
        return f'https://{profile}.github.io/{repo}/branches/{branch_encoded}/'


def post_pr_comment(pr_number: int, repository: str, run_id: int, sha: str, branch: str, github_token: str) -> str:
    """Post initial PR comment and return comment ID."""
    
    # Sanitize all inputs
    repository = sanitize_input(repository)
    sha = sanitize_input(sha)[:7]  # Limit to 7 chars for display
    branch = sanitize_input(branch)
    
    # Generate URLs
    deployment_url = generate_deployment_url(branch)
    build_log_url = f'https://github.com/{repository}/actions/runs/{run_id}'
    
    # Create comment content
    comment_body = f"""## 🚀 Deployment Started

**Branch:** `{branch}`  
**Commit:** `{sha}`  
**Expected URL:** {deployment_url}

[`🔍 View Build Log`]({build_log_url})

---
*This comment will be updated when the deployment completes.*"""
    
    # Post comment via GitHub API
    url = f'https://api.github.com/repos/{repository}/issues/{pr_number}/comments'
    
    headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/vnd.github.v3+json',
        'User-Agent': 'WHO-SMART-Base-PR-Commenter/1.0'
    }
    
    data = {
        'body': comment_body
    }
    
    try:
        response = requests.post(url, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        
        comment_data = response.json()
        comment_id = str(comment_data['id'])
        
        # Save comment ID for later updates
        os.makedirs('/tmp', exist_ok=True)
        with open('/tmp/comment_id.txt', 'w') as f:
            f.write(comment_id)
        
        print(f"Successfully posted PR comment. Comment ID: {comment_id}")
        return comment_id
        
    except requests.exceptions.RequestException as e:
        print(f"Error posting PR comment: {e}")
        sys.exit(1)


def main():
    """Main function."""
    if len(sys.argv) != 7:
        print("Usage: python pr_comment_start.py <pr_number> <repository> <run_id> <sha> <branch> <github_token>")
        sys.exit(1)
    
    try:
        pr_number = validate_pr_number(sys.argv[1])
        repository = sys.argv[2]
        run_id = validate_run_id(sys.argv[3])
        sha = sys.argv[4]
        branch = sys.argv[5]
        github_token = sys.argv[6]
        
        # Validate required inputs
        if not all([repository, sha, branch, github_token]):
            raise ValueError("All parameters are required")
        
        # Validate repository format (owner/repo)
        if '/' not in repository or len(repository.split('/')) != 2:
            raise ValueError("Repository must be in format 'owner/repo'")
        
        post_pr_comment(pr_number, repository, run_id, sha, branch, github_token)
        
    except ValueError as e:
        print(f"Invalid input: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()