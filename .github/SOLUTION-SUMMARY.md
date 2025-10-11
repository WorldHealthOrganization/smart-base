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

### 1. Comprehensive Detection Guide
Created `.github/DAK-REPOSITORY-DETECTION.md` with:
- ✅ Best practices for identifying DAK repositories
- ✅ Production-ready JavaScript and Python code examples
- ✅ Proper 404 error handling patterns
- ✅ Console error suppression techniques
- ✅ Rate limiting and caching strategies

### 2. Better Detection Method
**Old approach (problematic):**
```javascript
// Check for sushi-config.yaml - generates many 404s
GET /repos/{owner}/{repo}/contents/sushi-config.yaml
```

**New approach (recommended):**
```javascript
// Check for dak.json - specific to DAK repos only
GET /repos/{owner}/{repo}/contents/dak.json

// Handle 404 gracefully
if (response.status === 404) {
  // Expected - not a DAK repository
  return false;
}
```

### 3. Marker File
Added `.dak-repository` lightweight marker for even more efficient scanning using HEAD requests.

### 4. Documentation Updates
- Updated README.md
- Updated index.md
- Added clear guidance on how to detect DAK repos properly

## How This Solves the Problem

### Before (Problematic):
1. Tool scans 100 GitHub repos
2. Checks each for `sushi-config.yaml`
3. Gets 404s for 90+ repos (expected)
4. Console filled with red error messages
5. Still unclear which are DAK repos (sushi-config exists in non-DAK FHIR IGs too)

### After (Solution):
1. Tool scans repos checking for `dak.json` (DAK-specific)
2. Implements proper 404 handling from guide
3. 404s are handled silently (expected for non-DAK repos)
4. Console stays clean
5. Clear identification of DAK repos only

## Code Example: Proper 404 Handling

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
