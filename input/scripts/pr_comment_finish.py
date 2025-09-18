#!/usr/bin/env python3
"""
PR Comment Script - Deployment Finished

Safely updates a PR comment when deployment finishes, with proper input validation
and sanitization to prevent injection attacks.

Usage:
    python pr_comment_finish.py <pr_number> <repository> <run_id> <sha> <branch> <job_status> <github_token>
"""

import os
import sys
import json
import re
import requests
from urllib.parse import quote


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


def validate_job_status(status: str) -> str:
    """Validate job status is one of expected values."""
    status = sanitize_input(status).lower()
    valid_statuses = ['success', 'failure', 'cancelled', 'skipped']
    
    if status not in valid_statuses:
        # Default to failure for unknown statuses
        return 'failure'
    
    return status


def generate_deployment_url(branch: str) -> str:
    """Generate deployment URL with proper sanitization."""
    branch = sanitize_input(branch)
    
    if branch == 'main':
        return 'https://worldhealthorganization.github.io/smart-base/'
    else:
        # Extract branch suffix after last slash for URL
        branch_for_url = branch.split('/')[-1] if '/' in branch else branch
        branch_for_url = sanitize_input(branch_for_url)
        # URL encode the branch name for safety
        branch_encoded = quote(branch_for_url, safe='')
        return f'https://worldhealthorganization.github.io/smart-base/branches/{branch_encoded}/'


def update_pr_comment(pr_number: int, repository: str, run_id: int, sha: str, branch: str, job_status: str, github_token: str):
    """Update existing PR comment or create new one with final status."""
    
    # Sanitize all inputs
    repository = sanitize_input(repository)
    sha = sanitize_input(sha)[:7]  # Limit to 7 chars for display
    branch = sanitize_input(branch)
    job_status = validate_job_status(job_status)
    
    # Generate URLs
    deployment_url = generate_deployment_url(branch)
    build_log_url = f'https://github.com/{repository}/actions/runs/{run_id}'
    
    # Create comment content based on status
    if job_status == 'success':
        comment_icon = '✅'
        status_text = 'Deployment Successful'
        action_button = f'[`🌐 Open Preview`]({deployment_url})'
        
        comment_body = f"""## {comment_icon} {status_text}

**Branch:** `{branch}`  
**Commit:** `{sha}`  
**Deployed to:** {deployment_url}

{action_button}  
[`🔍 View Build Log`]({build_log_url})

---
*Deployment completed successfully! The site is now live at the URL above.*"""
    
    else:
        comment_icon = '❌'
        status_text = 'Deployment Failed'
        action_button = f'[`🔍 View Build Log`]({build_log_url})'
        
        comment_body = f"""## {comment_icon} {status_text}

**Branch:** `{branch}`  
**Commit:** `{sha}`  

{action_button}

---
*Deployment failed. Please check the build log for details.*"""
    
    headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/vnd.github.v3+json',
        'User-Agent': 'WHO-SMART-Base-PR-Commenter/1.0'
    }
    
    # Try to update existing comment first
    comment_updated = False
    comment_id_file = '/tmp/comment_id.txt'
    
    if os.path.exists(comment_id_file):
        try:
            with open(comment_id_file, 'r') as f:
                comment_id = f.read().strip()
            
            # Validate comment ID is numeric
            if comment_id.isdigit():
                update_url = f'https://api.github.com/repos/{repository}/issues/comments/{comment_id}'
                
                data = {'body': comment_body}
                response = requests.patch(update_url, headers=headers, json=data, timeout=30)
                
                if response.status_code == 200:
                    comment_updated = True
                    print(f"Successfully updated existing comment {comment_id}")
                else:
                    print(f"Failed to update comment {comment_id}: {response.status_code}")
            
        except Exception as e:
            print(f"Failed to update existing comment: {e}")
    
    # If update failed, create new comment
    if not comment_updated:
        try:
            create_url = f'https://api.github.com/repos/{repository}/issues/{pr_number}/comments'
            data = {'body': comment_body}
            
            response = requests.post(create_url, headers=headers, json=data, timeout=30)
            response.raise_for_status()
            
            print("Successfully created new comment")
            
        except requests.exceptions.RequestException as e:
            print(f"Error creating new PR comment: {e}")
            sys.exit(1)


def main():
    """Main function."""
    if len(sys.argv) != 8:
        print("Usage: python pr_comment_finish.py <pr_number> <repository> <run_id> <sha> <branch> <job_status> <github_token>")
        sys.exit(1)
    
    try:
        pr_number = validate_pr_number(sys.argv[1])
        repository = sys.argv[2]
        run_id = validate_run_id(sys.argv[3])
        sha = sys.argv[4]
        branch = sys.argv[5]
        job_status = sys.argv[6]
        github_token = sys.argv[7]
        
        # Validate required inputs
        if not all([repository, sha, branch, job_status, github_token]):
            raise ValueError("All parameters are required")
        
        # Validate repository format (owner/repo)
        if '/' not in repository or len(repository.split('/')) != 2:
            raise ValueError("Repository must be in format 'owner/repo'")
        
        update_pr_comment(pr_number, repository, run_id, sha, branch, job_status, github_token)
        
    except ValueError as e:
        print(f"Invalid input: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()