# Solution Summary: Nicer Error Handling in Repo Scan

## Issue Description
When scanning repositories to check if they're DAK repositories, 404 errors appear in browser console:
```
112.b763af0b.chunk.js:1 GET https://api.github.com/repos/litlfred/sushi/contents/sushi-config.yaml 404 (Not Found)
```

These 404s are **expected** (most repos are not DAK repos) but the console errors are noisy.

## Root Cause
External tools were checking for `sushi-config.yaml` to identify DAK repositories. However:
- ❌ `sushi-config.yaml` exists in ALL FHIR Implementation Guides (not just DAK repos)
- ❌ Causes false positives
- ❌ Generates many 404s for non-FHIR repos
- ❌ Creates noisy console output

## Solution Provided

### 1. DAK Repository List (Completely Eliminates 404s!)

**Created `input/pagecontent/dak-repositories.json`** - A curated JSON file with all WHO DAK repositories:

```javascript
// Fetch once - NO 404 errors!
const response = await fetch(
  'https://worldhealthorganization.github.io/smart-base/dak-repositories.json'
);
const data = await response.json();

// Check in-memory - no API calls needed!
function isDAKRepository(owner, repo) {
  return data.repositories.some(
    r => r.owner === owner && r.name === repo
  );
}
```

**Benefits:**
- ✅ **Zero 404 errors** - One request for entire organization
- ✅ **Instant checks** - In-memory lookup, no API calls
- ✅ **Complete metadata** - Titles, URLs, descriptions included

### 2. Comprehensive Detection Guide

Created `.github/DAK-REPOSITORY-DETECTION.md` with:
- ✅ Primary method: Fetch DAK repository list (NO 404s!)
- ✅ Fallback method: Check for `dak.json` with proper error handling
- ✅ Production-ready JavaScript and Python code examples
- ✅ Console error suppression techniques
- ✅ Rate limiting and caching strategies

### 3. Better Detection Method
**Old approach (generates 404s):**
```javascript
// Check for sushi-config.yaml - generates many 404s
GET /repos/{owner}/{repo}/contents/sushi-config.yaml
```

**New approach (RECOMMENDED - zero 404s):**
```javascript
// Method 1: Use curated list (NO 404s!)
const list = await fetch('https://worldhealthorganization.github.io/smart-base/dak-repositories.json');
const data = await list.json();
const isDak = data.repositories.some(r => r.name === 'smart-base');

// Method 2 (fallback): Check dak.json with error handling
const response = await fetch('/repos/WHO/smart-base/contents/dak.json');
if (response.status === 404) return false; // No console error
```

### 4. Marker File
Added `.dak-repository` lightweight marker for even more efficient scanning using HEAD requests.

### 5. Documentation Updates
- Updated README.md
- Updated index.md
- Added clear guidance on how to detect DAK repos properly

## How This Solves the Problem

### Before (Problematic):
1. Tool scans 100 GitHub repos
2. Checks each for `sushi-config.yaml`
3. Gets 404s for 90+ repos (expected)
4. **Console filled with red error messages** ❌
5. Still unclear which are DAK repos (sushi-config exists in non-DAK FHIR IGs too)

### After (Solution):
1. Tool fetches DAK repository list ONCE
2. Checks repos against in-memory list
3. **Zero 404 errors!** ✅
4. **Clean console output** ✅
5. Instant lookups, no API rate limiting
6. Clear identification of DAK repos only

## Code Example: Zero 404 Errors

```javascript
async function scanForDAKRepos() {
  // Fetch list once - NO 404s!
  const response = await fetch(
    'https://worldhealthorganization.github.io/smart-base/dak-repositories.json'
  );
  const data = await response.json();
  
  // Check against in-memory list - NO API calls, NO 404s!
  function isDAKRepository(owner, repo) {
    return data.repositories.some(
      r => r.owner === owner && r.name === repo
    );
  }
  
  // Example: Check if smart-base is a DAK repo
  const isDak = isDAKRepository('WorldHealthOrganization', 'smart-base');
  console.log('Is DAK:', isDak); // true, no 404 errors!
}
```

## Code Example: Fallback with Proper 404 Handling

If the list is unavailable, fall back to individual checks:

```javascript
async function isDAKRepository(owner, repo) {
  try {
    const response = await fetch(
      `https://api.github.com/repos/${owner}/${repo}/contents/dak.json`,
      {
        headers: {
          'Accept': 'application/vnd.github.v3+json',
        }
      }
    );
    
    if (response.status === 404) {
      // This is EXPECTED - repository is not a DAK repository
      // No need to log as error
      return false;
    }
    
    if (!response.ok) {
      console.warn(`Unexpected response for ${owner}/${repo}: ${response.status}`);
      return false;
    }
    
    return true;
  } catch (error) {
    // Only log actual errors, not expected 404s
    console.error(`Error checking ${owner}/${repo}:`, error.message);
    return false;
  }
}
```

## Additional Optimizations Provided

### 1. Batch Detection with Search API
Instead of checking repos one by one:
```javascript
// Find all DAK repos in organization at once
const query = 'filename:dak.json user:WorldHealthOrganization';
const response = await fetch(
  `https://api.github.com/search/code?q=${encodeURIComponent(query)}`
);
```

### 2. Caching
```javascript
class DAKRepositoryScanner {
  constructor(githubToken) {
    this.cache = new Map();
  }
  
  async checkRepository(owner, repo) {
    const cacheKey = `${owner}/${repo}`;
    if (this.cache.has(cacheKey)) {
      return this.cache.get(cacheKey);
    }
    // ... check and cache result
  }
}
```

### 3. Curated List
Maintain a list of known DAK repositories to minimize scanning:
```json
{
  "dak_repositories": [
    "WorldHealthOrganization/smart-base",
    "WorldHealthOrganization/smart-immunizations",
    "WorldHealthOrganization/smart-anc",
    "WorldHealthOrganization/smart-hiv"
  ]
}
```

## Benefits of This Solution

1. **Cleaner Console**: 404s handled gracefully, no error spam
2. **Better Performance**: Check DAK-specific file, use caching
3. **Accurate Detection**: `dak.json` is unique to DAK repos
4. **Production Ready**: Complete code examples in JavaScript and Python
5. **Best Practices**: Rate limiting, authentication, batch operations
6. **Documentation**: Comprehensive guide for developers

## For External Tool Developers

If you're developing a tool that scans WHO repositories:

1. **Read the guide**: `.github/DAK-REPOSITORY-DETECTION.md`
2. **Use `dak.json`**: Primary indicator for DAK repos
3. **Handle 404s**: They're expected, not errors
4. **Implement caching**: Minimize API calls
5. **Use authentication**: Avoid rate limits
6. **Consider batch API**: Search API or curated lists

## Questions?

See the full guide at:
https://github.com/WorldHealthOrganization/smart-base/blob/main/.github/DAK-REPOSITORY-DETECTION.md

Or file an issue at:
https://github.com/WorldHealthOrganization/smart-base/issues
