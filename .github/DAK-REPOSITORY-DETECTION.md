# DAK Repository Detection Guide

## Overview

This document provides guidance for tools and applications that need to identify WHO SMART Guidelines DAK (Digital Adaptation Kit) repositories programmatically.

## Recommended Detection Method

To detect whether a GitHub repository is a WHO SMART Guidelines DAK repository, external tools should use the following approach to **completely eliminate 404 errors**:

### Method 1: Use the DAK Repository List (RECOMMENDED - No 404s!)

**Fetch the curated list of WHO DAK repositories:**
```javascript
// Fetch the list once - NO 404 errors!
const response = await fetch(
  'https://worldhealthorganization.github.io/smart-base/dak-repositories.json'
);
const data = await response.json();

// Check if a repo is in the list
function isDAKRepository(owner, repo) {
  return data.repositories.some(
    r => r.owner === owner && r.name === repo
  );
}
```

**Benefits:**
- ✅ **Zero 404 errors** - Only one request needed
- ✅ **Fast** - Check against in-memory list
- ✅ **Reliable** - Curated and maintained by WHO
- ✅ **Complete** - Includes metadata (title, URLs, etc.)

### Method 2: Check for `dak.json` (If list unavailable)

If the curated list is unavailable, check for `dak.json` in the repository root:

**API Check:**
```
GET https://api.github.com/repos/{owner}/{repo}/contents/dak.json
```

### Handling Expected 404 Responses

When scanning multiple repositories to identify DAK repositories, 404 responses are expected and normal for non-DAK repositories. Applications should handle these gracefully:

```javascript
// Example: Graceful 404 handling in JavaScript
async function isDAKRepository(owner, repo) {
  try {
    const response = await fetch(
      `https://api.github.com/repos/${owner}/${repo}/contents/dak.json`,
      {
        headers: {
          'Accept': 'application/vnd.github.v3+json',
          // Include auth token if available to avoid rate limiting
        }
      }
    );
    
    if (response.status === 404) {
      // This is expected - repository is not a DAK repository
      return false;
    }
    
    if (!response.ok) {
      console.warn(`Unexpected response checking ${owner}/${repo}: ${response.status}`);
      return false;
    }
    
    return true;
  } catch (error) {
    // Network errors or other issues
    console.error(`Error checking ${owner}/${repo}:`, error.message);
    return false;
  }
}
```

### Suppressing Console Errors

Browser DevTools will show 404 errors for API calls even when they're handled correctly. To prevent these from appearing in the console during repository scanning:

1. **Use Fetch with proper error handling** (as shown above)
2. **Filter console messages** in browser DevTools
3. **Consider caching** DAK repository lists to minimize repeated checks
4. **Use the GitHub GraphQL API** which can batch queries and may generate cleaner error handling

## Alternative: Batch Detection

For scanning multiple repositories, consider using GitHub's search API or maintaining a curated list of known DAK repositories:

### GitHub Search API

```javascript
// Search for repositories with dak.json files
const query = 'filename:dak.json user:WorldHealthOrganization';
const response = await fetch(
  `https://api.github.com/search/code?q=${encodeURIComponent(query)}`
);
```

### Curated Repository List

Maintain a cached list of known DAK repositories updated periodically:

```json
{
  "dak_repositories": [
    "WorldHealthOrganization/smart-base",
    "WorldHealthOrganization/smart-immunizations",
    "WorldHealthOrganization/smart-anc",
    "WorldHealthOrganization/smart-hiv"
  ],
  "last_updated": "2025-10-11T21:00:00Z"
}
```

## Why Not Use `sushi-config.yaml`?

While `sushi-config.yaml` is present in all WHO SMART Guidelines repositories (including DAK repositories), it is also present in many non-DAK FHIR Implementation Guide repositories. Using it as a detection mechanism would:

1. Generate false positives for non-DAK FHIR IGs
2. Not distinguish DAK repositories from other FHIR IGs
3. Provide less specific information than `dak.json`

## `dak.json` Structure

The `dak.json` file contains structured metadata about the DAK:

```json
{
  "resourceType": "DAK",
  "resourceDefinition": "http://smart.who.int/base/StructureDefinition/DAK",
  "id": "smart.who.int.example",
  "name": "ExampleGuideline",
  "title": "WHO SMART Guidelines - Example",
  "version": "1.0.0",
  "status": "draft",
  "publicationUrl": "https://smart.who.int/example",
  "previewUrl": "https://WorldHealthOrganization.github.io/smart-example",
  "canonicalUrl": "https://smart.who.int/example"
}
```

## Rate Limiting Considerations

When scanning multiple repositories:

1. **Use authenticated requests** to get 5,000 requests/hour instead of 60
2. **Implement exponential backoff** for rate limit errors
3. **Cache results** to avoid repeated checks
4. **Consider using conditional requests** with `If-Modified-Since` headers

## Example Implementation

Complete example for a repository scanner with **zero 404 errors**:

```javascript
class DAKRepositoryScanner {
  constructor(githubToken) {
    this.token = githubToken;
    this.dakListUrl = 'https://worldhealthorganization.github.io/smart-base/dak-repositories.json';
    this.dakList = null;
  }

  async loadDAKList() {
    if (this.dakList) {
      return this.dakList;
    }

    try {
      const response = await fetch(this.dakListUrl);
      if (!response.ok) {
        throw new Error(`Failed to fetch DAK list: ${response.status}`);
      }
      const data = await response.json();
      this.dakList = new Set(
        data.repositories.map(r => `${r.owner}/${r.name}`)
      );
      return this.dakList;
    } catch (error) {
      console.warn('Could not load DAK repository list, falling back to individual checks:', error.message);
      this.dakList = new Set(); // Empty set to prevent repeated failures
      return this.dakList;
    }
  }

  async checkRepository(owner, repo) {
    // Try to use the curated list first (NO 404s!)
    await this.loadDAKList();
    
    const repoKey = `${owner}/${repo}`;
    if (this.dakList.has(repoKey)) {
      return true;
    }
    
    // If list is empty (failed to load), fall back to API check
    if (this.dakList.size === 0) {
      return this.checkRepositoryViaAPI(owner, repo);
    }
    
    // Repository not in list
    return false;
  }

  async checkRepositoryViaAPI(owner, repo) {
    // Fallback method - only used if list fails to load
    try {
      const response = await fetch(
        `https://api.github.com/repos/${owner}/${repo}/contents/dak.json`,
        {
          headers: {
            'Accept': 'application/vnd.github.v3+json',
            ...(this.token && { 'Authorization': `token ${this.token}` })
          }
        }
      );

      // Handle 404 silently - expected for non-DAK repos
      if (response.status === 404) {
        return false;
      }

      return response.ok;
    } catch (error) {
      // Only log unexpected errors
      console.error(`Error checking ${owner}/${repo}:`, error.message);
      return false;
    }
  }

  async scanOrganization(org) {
    // Load the list once
    await this.loadDAKList();
    
    // Get all repos for the organization
    const repos = await this.getOrgRepos(org);
    
    // Filter using the in-memory list (NO API calls, NO 404s!)
    const results = repos.filter(repo => {
      const repoKey = `${org}/${repo.name}`;
      return this.dakList.has(repoKey);
    });
    
    return results;
  }

  async getOrgRepos(org) {
    const response = await fetch(
      `https://api.github.com/orgs/${org}/repos?per_page=100`,
      {
        headers: {
          'Accept': 'application/vnd.github.v3+json',
          ...(this.token && { 'Authorization': `token ${this.token}` })
        }
      }
    );

    return await response.json();
  }
}

// Usage - completely eliminates 404 errors!
const scanner = new DAKRepositoryScanner(process.env.GITHUB_TOKEN);

// Scan organization - uses cached list, NO 404s
const dakRepos = await scanner.scanOrganization('WorldHealthOrganization');
console.log('Found DAK repositories:', dakRepos.map(r => r.name));

// Check individual repo - uses cached list if available
const isDak = await scanner.checkRepository('WorldHealthOrganization', 'smart-base');
console.log('Is DAK repository:', isDak);
```

## Python Example

For Python applications with **zero 404 errors**:

```python
import requests
from typing import List, Dict, Set

class DAKRepositoryScanner:
    def __init__(self, github_token: str = None):
        self.token = github_token
        self.dak_list_url = 'https://worldhealthorganization.github.io/smart-base/dak-repositories.json'
        self.dak_list: Set[str] = None
        self.session = requests.Session()
        if github_token:
            self.session.headers.update({
                'Authorization': f'token {github_token}'
            })

    def load_dak_list(self) -> Set[str]:
        """Load the curated DAK repository list (eliminates 404s)."""
        if self.dak_list is not None:
            return self.dak_list

        try:
            response = self.session.get(self.dak_list_url)
            response.raise_for_status()
            data = response.json()
            self.dak_list = set(
                f"{repo['owner']}/{repo['name']}" 
                for repo in data['repositories']
            )
            return self.dak_list
        except requests.RequestException as e:
            print(f"Could not load DAK repository list: {e}")
            self.dak_list = set()  # Empty set to prevent repeated failures
            return self.dak_list

    def is_dak_repository(self, owner: str, repo: str) -> bool:
        """Check if a repository is a DAK repository (no 404s!)."""
        # Load list if not already loaded
        self.load_dak_list()
        
        repo_key = f"{owner}/{repo}"
        
        # Check against in-memory list first
        if self.dak_list and repo_key in self.dak_list:
            return True
        
        # If list is empty (failed to load), fall back to API check
        if len(self.dak_list) == 0:
            return self._check_via_api(owner, repo)
        
        return False

    def _check_via_api(self, owner: str, repo: str) -> bool:
        """Fallback method - only used if list fails to load."""
        url = f"https://api.github.com/repos/{owner}/{repo}/contents/dak.json"
        
        try:
            response = self.session.get(url)
            # Handle 404 silently - expected for non-DAK repos
            if response.status_code == 404:
                return False
            return response.status_code == 200
        except requests.RequestException as e:
            print(f"Error checking {owner}/{repo}: {e}")
            return False

    def scan_organization(self, org: str) -> List[Dict]:
        """Scan all repositories in an organization (no 404s!)."""
        # Load list once
        self.load_dak_list()
        
        url = f"https://api.github.com/orgs/{org}/repos"
        dak_repos = []
        
        try:
            response = self.session.get(url, params={'per_page': 100})
            response.raise_for_status()
            repos = response.json()
            
            # Filter using in-memory list (NO API calls, NO 404s!)
            for repo in repos:
                repo_key = f"{org}/{repo['name']}"
                if self.dak_list and repo_key in self.dak_list:
                    dak_repos.append(repo)
        except requests.RequestException as e:
            print(f"Error scanning organization {org}: {e}")
        
        return dak_repos

# Usage - completely eliminates 404 errors!
scanner = DAKRepositoryScanner(github_token='your_token_here')

# Scan organization - uses cached list, NO 404s
dak_repos = scanner.scan_organization('WorldHealthOrganization')
print(f"Found {len(dak_repos)} DAK repositories")
for repo in dak_repos:
    print(f"  - {repo['name']}")

# Check individual repo - uses cached list if available
is_dak = scanner.is_dak_repository('WorldHealthOrganization', 'smart-base')
print(f"Is DAK repository: {is_dak}")
```

## Summary

- ✅ **DO** fetch the DAK repository list from `dak-repositories.json` (eliminates ALL 404s)
- ✅ **DO** check against the in-memory list instead of making individual API calls
- ✅ **DO** fall back to checking `dak.json` if the list is unavailable
- ✅ **DO** handle 404 responses gracefully when using fallback method
- ✅ **DO** use authenticated requests to avoid rate limiting
- ❌ **DON'T** check each repository individually if you can use the curated list
- ❌ **DON'T** rely on `sushi-config.yaml` alone for DAK detection
- ❌ **DON'T** treat 404 responses as errors during repository scanning

## Questions?

For questions about DAK repository detection or this guide, please file an issue in the [smart-base repository](https://github.com/WorldHealthOrganization/smart-base/issues).
