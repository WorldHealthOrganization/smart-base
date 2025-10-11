# DAK Repository Detection Guide

## Overview

This document provides guidance for tools and applications that need to identify WHO SMART Guidelines DAK (Digital Adaptation Kit) repositories programmatically.

## Recommended Detection Method

To detect whether a GitHub repository is a WHO SMART Guidelines DAK repository, external tools should use the following approach to minimize unnecessary API calls and avoid 404 errors:

### Primary Indicator: `dak.json`

The presence of a `dak.json` file in the repository root is the definitive indicator of a DAK repository. This file contains DAK-specific metadata and configuration.

**Recommended API Check:**
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

Complete example for a repository scanner with proper error handling:

```javascript
class DAKRepositoryScanner {
  constructor(githubToken) {
    this.token = githubToken;
    this.cache = new Map();
  }

  async checkRepository(owner, repo) {
    const cacheKey = `${owner}/${repo}`;
    
    // Check cache first
    if (this.cache.has(cacheKey)) {
      return this.cache.get(cacheKey);
    }

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

      const isDAK = response.ok;
      
      // Cache the result
      this.cache.set(cacheKey, isDAK);
      
      return isDAK;
    } catch (error) {
      // Log only unexpected errors, not 404s
      if (error.status !== 404) {
        console.error(`Error scanning ${cacheKey}:`, error);
      }
      return false;
    }
  }

  async scanOrganization(org) {
    // Get all repos for the organization
    const repos = await this.getOrgRepos(org);
    
    // Check each repo (with rate limiting)
    const results = [];
    for (const repo of repos) {
      const isDAK = await this.checkRepository(org, repo.name);
      if (isDAK) {
        results.push(repo);
      }
      
      // Small delay to avoid rate limiting
      await new Promise(resolve => setTimeout(resolve, 100));
    }
    
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

// Usage
const scanner = new DAKRepositoryScanner(process.env.GITHUB_TOKEN);
const dakRepos = await scanner.scanOrganization('WorldHealthOrganization');
console.log('Found DAK repositories:', dakRepos.map(r => r.name));
```

## Python Example

For Python applications:

```python
import requests
from typing import List, Dict

class DAKRepositoryScanner:
    def __init__(self, github_token: str = None):
        self.token = github_token
        self.cache = {}
        self.session = requests.Session()
        if github_token:
            self.session.headers.update({
                'Authorization': f'token {github_token}'
            })

    def is_dak_repository(self, owner: str, repo: str) -> bool:
        """Check if a repository contains a dak.json file."""
        cache_key = f"{owner}/{repo}"
        
        if cache_key in self.cache:
            return self.cache[cache_key]

        url = f"https://api.github.com/repos/{owner}/{repo}/contents/dak.json"
        
        try:
            response = self.session.get(url)
            is_dak = response.status_code == 200
            self.cache[cache_key] = is_dak
            return is_dak
        except requests.RequestException as e:
            # Only log unexpected errors
            if hasattr(e, 'response') and e.response.status_code != 404:
                print(f"Error checking {cache_key}: {e}")
            return False

    def scan_organization(self, org: str) -> List[Dict]:
        """Scan all repositories in an organization for DAK repositories."""
        url = f"https://api.github.com/orgs/{org}/repos"
        dak_repos = []
        
        try:
            response = self.session.get(url, params={'per_page': 100})
            response.raise_for_status()
            repos = response.json()
            
            for repo in repos:
                if self.is_dak_repository(org, repo['name']):
                    dak_repos.append(repo)
        except requests.RequestException as e:
            print(f"Error scanning organization {org}: {e}")
        
        return dak_repos

# Usage
scanner = DAKRepositoryScanner(github_token='your_token_here')
dak_repos = scanner.scan_organization('WorldHealthOrganization')
print(f"Found {len(dak_repos)} DAK repositories")
for repo in dak_repos:
    print(f"  - {repo['name']}")
```

## Summary

- ✅ **DO** check for `dak.json` to identify DAK repositories
- ✅ **DO** handle 404 responses gracefully (they're expected for non-DAK repos)
- ✅ **DO** use authenticated requests to avoid rate limiting
- ✅ **DO** cache results to minimize API calls
- ❌ **DON'T** rely on `sushi-config.yaml` alone for DAK detection
- ❌ **DON'T** treat 404 responses as errors during repository scanning
- ❌ **DON'T** scan repositories repeatedly without caching

## Questions?

For questions about DAK repository detection or this guide, please file an issue in the [smart-base repository](https://github.com/WorldHealthOrganization/smart-base/issues).
