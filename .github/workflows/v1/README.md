# v1 Workflow - ghbuild.yml (Semi-Stable)

This is the original comprehensive workflow that includes all DAK features. It provides WHO/non-WHO repository detection and enables DAK features automatically for WHO repositories.

## Features

- ✅ Core FHIR IG build functionality
- ✅ WHO/non-WHO repository detection
- ✅ Automatic DAK feature enablement for WHO repos
- ✅ Manual override controls for all features
- ✅ DMN questionnaire generation
- ✅ DMN file transformation to HTML
- ✅ ValueSet JSON schema generation
- ✅ Logical model JSON schema generation
- ✅ DAK API documentation hub
- ✅ JSON-LD vocabulary generation

## Usage

```yaml
name: Build FHIR IG
on: [push, pull_request]

jobs:
  build:
    uses: WorldHealthOrganization/smart-base/.github/workflows/v1-ghbuild.yml@main
    with:
      tx: "https://tx.fhir.org"  # Optional custom terminology server
      # Manual overrides (optional):
      generate_dmn_questionnaires: true
      transform_dmn_files: true
      generate_valueset_schemas: true
      generate_logical_model_schemas: true
      generate_dak_api_hub: true
      generate_jsonld_vocabularies: true
    secrets: inherit
```

## Automatic Behavior

- **WHO repositories**: All DAK features enabled by default
- **Non-WHO repositories**: All DAK features disabled by default
- **Manual triggers**: Can override defaults using workflow inputs

## Manual Override

You can explicitly enable/disable any feature regardless of repository owner:

```yaml
jobs:
  build:
    uses: WorldHealthOrganization/smart-base/.github/workflows/v1-ghbuild.yml@main
    with:
      generate_dmn_questionnaires: false  # Force disable even for WHO repos
      generate_valueset_schemas: true     # Force enable even for non-WHO repos
```

## Migration from Main

If you're currently using the main `ghbuild.yml`, no changes are needed. The main workflow now calls this v1 workflow for backward compatibility.

## When to Use v1

- You want the "batteries included" approach
- You're a WHO repository wanting all features automatically
- You need the most stable and tested workflow
- You want to minimize configuration

## When to Consider v2

- You need faster builds (core FHIR only)
- You want explicit control over which features run
- You want to separate DAK processing from core build
- You're experimenting with new features

## Support

This is the **semi-stable** version with the following support guarantees:

- ✅ Interface changes require 30-day notice
- ✅ Bug fixes applied promptly  
- ✅ New features added cautiously
- ✅ Backward compatibility maintained

## Troubleshooting

### Common Issues

1. **Build failures on non-WHO repos with DAK features**: DAK features are disabled by default for non-WHO repositories. Enable them explicitly if needed.

2. **Missing DAK features on WHO repos**: Check that repository owner is exactly "WorldHealthOrganization".

3. **Manual triggers not working**: Ensure you're using `workflow_dispatch` trigger and setting inputs correctly.

### Getting Help

- Check the main [README](../readme.md) for general setup
- Review [VERSIONING.md](../VERSIONING.md) for migration guidance
- Open an issue for bugs or feature requests