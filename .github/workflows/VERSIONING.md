# GitHub Workflow Versioning Guide

This document describes the versioning strategy for GitHub workflows in the smart-base repository and provides best practices for managing community versions of GitHub workflows.

## Overview

The smart-base repository provides versioned GitHub workflows to support different use cases:

- **v1 (Stable)**: The original `ghbuild.yml` with all DAK features included (semi-stable)
- **v2 (Experimental)**: Split workflows for modular usage

## Workflow Versions

### Version 1 (v1) - Semi-Stable

**Location**: `.github/workflows/v1-ghbuild.yml`

**Features**:
- Complete FHIR IG build functionality
- WHO/non-WHO repository detection
- Optional DAK features based on repository owner:
  - DMN questionnaire generation
  - DMN file transformation to HTML
  - ValueSet JSON schema generation
  - Logical model JSON schema generation
  - DAK API documentation hub
  - JSON-LD vocabulary generation

**Usage**:
```yaml
jobs:
  build:
    uses: WorldHealthOrganization/smart-base/.github/workflows/v1-ghbuild.yml@main
    with:
      tx: "https://tx.fhir.org"  # optional
      generate_dmn_questionnaires: true  # optional
      # ... other DAK feature flags
```

### Version 2 (v2) - Experimental

Version 2 splits the monolithic workflow into two focused workflows:

#### v2-ghbuild.yml - Core FHIR Build

**Location**: `.github/workflows/v2-ghbuild.yml`

**Features**:
- Core FHIR IG build functionality only
- No DAK-specific features
- Faster execution for standard FHIR builds
- Suitable for non-WHO repositories and basic builds

**Usage**:
```yaml
jobs:
  build:
    uses: WorldHealthOrganization/smart-base/.github/workflows/v2-ghbuild.yml@main
    with:
      tx: "https://tx.fhir.org"  # optional
```

#### v2-dakbuild.yml - DAK Features + Core Build

**Location**: `.github/workflows/v2-dakbuild.yml`

**Features**:
- All DAK-specific features
- Calls v2-ghbuild.yml for core FHIR build
- Modular architecture with pre-processing and post-processing jobs
- Fine-grained control over DAK features

**Usage**:
```yaml
jobs:
  dak-build:
    uses: WorldHealthOrganization/smart-base/.github/workflows/v2-dakbuild.yml@main
    with:
      tx: "https://tx.fhir.org"  # optional
      generate_dmn_questionnaires: true
      transform_dmn_files: true
      generate_valueset_schemas: true
      generate_logical_model_schemas: true
      generate_dak_api_hub: true
      generate_jsonld_vocabularies: true
```

### Main ghbuild.yml - Backward Compatibility

**Location**: `.github/workflows/ghbuild.yml`

This is a wrapper that calls the v1 workflow to maintain backward compatibility for existing projects.

## Migration Guide

### From Main ghbuild.yml to v2

#### For Standard FHIR Builds (No DAK Features)

**Before**:
```yaml
jobs:
  build:
    uses: WorldHealthOrganization/smart-base/.github/workflows/ghbuild.yml@main
```

**After**:
```yaml
jobs:
  build:
    uses: WorldHealthOrganization/smart-base/.github/workflows/v2-ghbuild.yml@main
```

#### For DAK-Enhanced Builds

**Before**:
```yaml
jobs:
  build:
    uses: WorldHealthOrganization/smart-base/.github/workflows/ghbuild.yml@main
    with:
      generate_dmn_questionnaires: true
      # ... other DAK flags
```

**After**:
```yaml
jobs:
  dak-build:
    uses: WorldHealthOrganization/smart-base/.github/workflows/v2-dakbuild.yml@main
    with:
      generate_dmn_questionnaires: true
      # ... other DAK flags
```

## Best Practices for Community Workflow Versioning

### 1. Semantic Versioning for Workflows

- **Major versions** (v1, v2): Breaking changes in interface or behavior
- **Minor versions** (v1.1, v1.2): New features, backward compatible
- **Patch versions** (v1.1.1): Bug fixes, no interface changes

### 2. Version Directory Structure

```
.github/workflows/
├── v1/
│   ├── ghbuild.yml
│   └── README.md
├── v2/
│   ├── ghbuild.yml
│   ├── dakbuild.yml
│   └── README.md
├── ghbuild.yml          # Backward compatibility wrapper
└── VERSIONING.md        # This file
```

### 3. Backward Compatibility Strategy

- **Never delete** previous major versions
- **Maintain** existing interfaces in stable versions
- **Document** deprecation timeline clearly
- **Provide** clear migration paths

### 4. Stability Guarantees

#### v1 (Semi-Stable)
- Interface changes require 30-day notice
- Bug fixes allowed without notice
- Feature additions may be added cautiously

#### v2 (Experimental)
- Breaking changes allowed without notice
- Rapid iteration and feedback collection
- Not recommended for production use

### 5. Release Communication

#### For Breaking Changes
1. **Announce** in repository discussions
2. **Document** in CHANGELOG.md
3. **Provide** migration guide
4. **Give** adequate notice period

#### For New Features
1. **Document** in workflow README
2. **Add** usage examples
3. **Test** with pilot projects

### 6. Testing Strategy

#### Pre-Release Testing
- Test with multiple repository types
- Validate both WHO and non-WHO scenarios
- Check backward compatibility
- Test error conditions

#### Community Testing
- Beta testing with selected repositories
- Feedback collection period
- Issue tracking and resolution

### 7. Version Pinning Recommendations

#### For Production Use
```yaml
# Pin to specific version
uses: WorldHealthOrganization/smart-base/.github/workflows/v1-ghbuild.yml@v1.2.1

# Or pin to major version for stability
uses: WorldHealthOrganization/smart-base/.github/workflows/v1-ghbuild.yml@v1
```

#### For Development/Testing
```yaml
# Use latest for testing new features
uses: WorldHealthOrganization/smart-base/.github/workflows/v2-ghbuild.yml@main

# Or use specific branch for testing
uses: WorldHealthOrganization/smart-base/.github/workflows/v2-ghbuild.yml@feature/new-capability
```

### 8. Documentation Standards

Each version should include:
- **README.md**: Usage instructions and examples
- **CHANGELOG.md**: Version history and breaking changes
- **Input/Output specification**: Clear interface documentation
- **Migration guides**: When moving between versions

### 9. Community Feedback

- **GitHub Discussions**: For design discussions
- **Issues**: For bug reports and feature requests
- **Pull Requests**: For community contributions
- **Beta testing**: Opt-in testing program

### 10. Deprecation Process

1. **Announce** deprecation with timeline
2. **Mark** as deprecated in documentation
3. **Provide** migration path
4. **Maintain** for announced period
5. **Archive** but keep available for reference

## Support Matrix

| Version | Status | Support Level | Use Case |
|---------|--------|---------------|----------|
| v1 | Semi-Stable | Bug fixes + Critical features | Production WHO repositories |
| v2 | Experimental | Active development | Testing and feedback |
| main (wrapper) | Stable | Redirects to v1 | Backward compatibility |

## Getting Help

- **Documentation**: Check version-specific README files
- **Issues**: Report bugs via GitHub Issues
- **Discussions**: Ask questions in GitHub Discussions
- **Migration**: Follow migration guides in this document

## Contributing

When contributing to workflows:

1. **Target** the appropriate version branch
2. **Test** changes with multiple repository types
3. **Document** interface changes
4. **Update** version-specific README
5. **Follow** semantic versioning guidelines