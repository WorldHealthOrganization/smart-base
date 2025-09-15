# v2 Workflows (Experimental)

Version 2 provides a modular approach with two separate workflows:

- **`ghbuild.yml`**: Core FHIR IG build only
- **`dakbuild.yml`**: DAK features + calls ghbuild

## ghbuild.yml - Core FHIR Build

A streamlined workflow focused solely on building FHIR Implementation Guides.

### Features

- ✅ Core FHIR IG build functionality
- ✅ GitHub Pages deployment
- ✅ PR comments with build status
- ✅ Branch-based deployments
- ❌ No DAK-specific features

### Usage

```yaml
name: Build FHIR IG
on: [push, pull_request]

jobs:
  build:
    uses: WorldHealthOrganization/smart-base/.github/workflows/v2/ghbuild.yml@main
    with:
      tx: "https://tx.fhir.org"  # Optional custom terminology server
    secrets: inherit
```

### When to Use

- You only need standard FHIR IG building
- You want faster build times
- You're not using DAK features
- You prefer explicit control over what runs

## dakbuild.yml - DAK Features + Core Build

A comprehensive workflow that includes DAK features and calls the core ghbuild workflow.

### Features

- ✅ All DAK features with fine-grained control
- ✅ DMN questionnaire generation  
- ✅ DMN file transformation to HTML
- ✅ ValueSet JSON schema generation
- ✅ Logical model JSON schema generation
- ✅ DAK API documentation hub
- ✅ JSON-LD vocabulary generation
- ✅ Calls v2/ghbuild.yml for core build
- ✅ Modular pre/post-processing architecture

### Usage

```yaml
name: Build FHIR IG with DAK
on: [push, pull_request]

jobs:
  dak-build:
    uses: WorldHealthOrganization/smart-base/.github/workflows/v2/dakbuild.yml@main
    with:
      tx: "https://tx.fhir.org"
      # All DAK features default to true, but can be controlled:
      generate_dmn_questionnaires: true
      transform_dmn_files: true
      generate_valueset_schemas: true
      generate_logical_model_schemas: true
      generate_dak_api_hub: true
      generate_jsonld_vocabularies: true
    secrets: inherit
```

### Architecture

The DAK workflow uses a three-job architecture:

1. **`dak-preprocess`**: DMN processing, configuration setup
2. **`call-ghbuild`**: Calls v2/ghbuild.yml for core FHIR build
3. **`dak-postprocess`**: Schema generation, API documentation

### When to Use

- You need DAK features
- You want explicit control over each feature
- You're experimenting with new DAK capabilities
- You prefer modular architecture

## Key Differences from v1

| Aspect | v1 | v2 |
|--------|----|----|
| Architecture | Monolithic | Modular (separate workflows) |
| DAK Features | Auto-enabled for WHO repos | Explicit control, default enabled |
| Repository Detection | Automatic WHO/non-WHO | Manual configuration |
| Stability | Semi-stable | Experimental |
| Build Speed | Slower (all features) | Faster (ghbuild only) |
| Configuration | Minimal | Explicit |

## Migration from v1

### From v1 to v2/ghbuild (Core Only)

**Before (v1)**:
```yaml
jobs:
  build:
    uses: WorldHealthOrganization/smart-base/.github/workflows/v1/ghbuild.yml@main
```

**After (v2/ghbuild)**:
```yaml
jobs:
  build:
    uses: WorldHealthOrganization/smart-base/.github/workflows/v2/ghbuild.yml@main
```

### From v1 to v2/dakbuild (With DAK Features)

**Before (v1)**:
```yaml
jobs:
  build:
    uses: WorldHealthOrganization/smart-base/.github/workflows/v1/ghbuild.yml@main
    with:
      generate_dmn_questionnaires: true
```

**After (v2/dakbuild)**:
```yaml
jobs:
  dak-build:
    uses: WorldHealthOrganization/smart-base/.github/workflows/v2/dakbuild.yml@main
    with:
      generate_dmn_questionnaires: true
      # Note: Other features default to true, but can be explicitly controlled
```

## Experimental Status

⚠️ **Important**: v2 workflows are **experimental** and may have breaking changes without notice.

### What This Means

- ❌ No stability guarantees
- ❌ Breaking changes allowed without notice  
- ❌ Not recommended for production use
- ✅ Rapid iteration and feedback collection
- ✅ Testing new features and approaches

### Using v2 Safely

1. **Pin to specific commits** for reproducibility:
   ```yaml
   uses: WorldHealthOrganization/smart-base/.github/workflows/v2/ghbuild.yml@abc123
   ```

2. **Test thoroughly** before adopting

3. **Monitor** for breaking changes

4. **Provide feedback** to help stabilize features

## Known Limitations

### dakbuild.yml Current Limitations

- ⚠️ Post-processing jobs need full IG output coordination (simplified in current implementation)
- ⚠️ Artifact sharing between jobs needs refinement
- ⚠️ Error handling needs improvement

### Planned Improvements

- Better artifact coordination between pre/post processing jobs
- Enhanced error handling and recovery
- Performance optimizations
- Additional DAK features

## Feedback and Contributions

Since v2 is experimental, your feedback is crucial:

- 🐛 **Report issues**: Use GitHub Issues for bugs
- 💡 **Feature requests**: Discuss in GitHub Discussions  
- 🧪 **Testing**: Try v2 workflows and share experiences
- 📝 **Documentation**: Help improve docs and examples

## Support

v2 workflows have **active development** support:

- ✅ Active feature development
- ✅ Community feedback incorporated
- ✅ Regular updates and improvements
- ❌ No backward compatibility guarantees
- ❌ Interface may change without notice

For production use, consider [v1](../v1/) until v2 stabilizes.