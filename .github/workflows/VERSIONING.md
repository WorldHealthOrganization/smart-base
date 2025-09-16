# GitHub Workflow Versioning Guide

This document describes the versioning strategy for GitHub workflows in the smart-base repository and provides best practices for using the versioned workflow.

## Overview

The smart-base repository provides a **single versioned workflow** that supports both stable v1 compatibility and v2 DAK features through hybrid commit SHA and branch reference versioning.

## Workflow Versioning Strategy

### Hybrid Versioning Approach

The repository uses **hybrid versioning** combining commit SHAs for stability and branch references for latest features:

- **Stable Production (Recommended)**: `@14b3859` - Immutable commit reference for v1 functionality
- **Latest Development**: `@main` - Dynamic branch reference for latest features
- **Future Versions**: Specific commit SHAs for v2, v2.1, etc. when released

### Single Workflow with Conditional Features

**Location**: `.github/workflows/ghbuild.yml`

**Features**:
- Complete FHIR IG build functionality (always enabled)
- Conditional DAK features via `do_dak: true` parameter:
  - DMN questionnaire generation
  - DMN file transformation to HTML  
  - ValueSet and logical model JSON schema generation
  - DAK API documentation hub
  - JSON-LD vocabulary generation
- Self-contained: Downloads DAK scripts when needed
- Validates `dak.json` presence before enabling DAK features

## Usage Examples

### Standard FHIR IG Build (Recommended - Stable)
```yaml
jobs:
  build:
    uses: WorldHealthOrganization/smart-base/.github/workflows/ghbuild.yml@14b3859
    with:
      tx: "https://tx.fhir.org"  # optional
```

### DAK-Enhanced Build (Recommended - Stable)
```yaml
jobs:
  dak-build:
    uses: WorldHealthOrganization/smart-base/.github/workflows/ghbuild.yml@14b3859
    with:
      do_dak: true
      tx: "https://tx.fhir.org"  # optional
```

### Latest Development Features
```yaml
jobs:
  build:
    uses: WorldHealthOrganization/smart-base/.github/workflows/ghbuild.yml@main
    with:
      do_dak: true  # optional - enable DAK features
```

## Best Practices for Workflow Versioning

### 1. Version Reference Strategy

#### For Production Use (Recommended)
```yaml
# Use stable commit SHA for production
uses: WorldHealthOrganization/smart-base/.github/workflows/ghbuild.yml@14b3859
```

#### For Development/Testing
```yaml
# Use latest for testing new features  
uses: WorldHealthOrganization/smart-base/.github/workflows/ghbuild.yml@main
```

#### Future Versions
```yaml
# Use specific commit SHAs for v2+ when released
uses: WorldHealthOrganization/smart-base/.github/workflows/ghbuild.yml@abc1234
```

### 2. Stability Guarantees

#### Commit SHA References (Production)
- **Immutable**: Never changes once tagged
- **Stable**: Guaranteed consistent behavior
- **Secure**: GitHub recommended for production use

#### Branch References (Development)  
- **Dynamic**: Updates with latest features
- **Testing**: Good for validating new capabilities
- **Flexible**: Easy to get latest improvements

### 3. DAK Feature Usage

DAK features are enabled conditionally via the `do_dak` parameter:

```yaml
# Standard FHIR IG build
uses: WorldHealthOrganization/smart-base/.github/workflows/ghbuild.yml@14b3859

# With DAK features enabled
uses: WorldHealthOrganization/smart-base/.github/workflows/ghbuild.yml@14b3859
with:
  do_dak: true
```

DAK features require `dak.json` in the repository root and include:
- DMN questionnaire generation
- DMN to HTML transformation
- JSON schema generation
- DAK API hub creation
- JSON-LD vocabulary generation

## Support Matrix

| Reference | Status | Use Case | Stability |
|-----------|--------|----------|-----------|
| `@14b3859` | Stable | Production repositories | Immutable v1 implementation |
| `@main` | Development | Testing new features | Latest development version |
| `@abc1234` | Future | v2+ releases | Immutable future versions |

## Getting Help

- **Documentation**: Check this versioning guide and workflow README
- **Issues**: Report bugs via GitHub Issues
- **Discussions**: Ask questions in GitHub Discussions
- **Examples**: See workflow README for usage examples

## Contributing

When contributing to the workflow:

1. **Test** changes with multiple repository types
2. **Validate** both standard and DAK-enabled scenarios  
3. **Document** interface changes
4. **Follow** hybrid versioning guidelines
5. **Ensure** backward compatibility