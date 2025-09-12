# DAK API Link Integration

This document outlines how the DAK API link has been integrated into the FHIR IG.

## Current Implementation

The DAK API link is integrated using a **simplified, reliable approach** that avoids custom template complexity:

### 1. Menu Navigation Link
**Location**: `sushi-config.yaml` under menu > Indices
```yaml
menu:
  Home: index.html 
  Downloads: downloads.html
  Indices:
    Artifact Index: artifacts.html
    DAK API: dak-api.html
```
**Benefits**: 
- Standard FHIR IG navigation approach
- Integrated with IG menu system
- No template customization required
- Reliable and maintainable

### 2. Page Configuration
**Location**: `sushi-config.yaml` pages section
```yaml
pages:
  dak-api.html:
    title: DAK API Documentation Hub
```
**Benefits**:
- Ensures proper IG integration
- Provides metadata for the page
- Standard FHIR IG approach

### 3. Build Integration
**Location**: `build-with-dak-api.sh`
```bash
# Generate DAK API documentation hub
python3 input/scripts/generate_dak_api_hub.py output
```
**Benefits**:
- Ensures `dak-api.html` exists before IG build
- Prevents broken links during build process
- Automated generation of API documentation hub

## Template Configuration

The implementation uses the standard WHO template:
```ini
template = who.template.root#current
```

This avoids the complexity and potential build issues of custom template modifications while still providing reliable access to the DAK API documentation.

## Usage

Users can access the DAK API documentation through:

1. **Main Navigation**: Indices → DAK API 
2. **Direct URL**: `{ig-base-url}/dak-api.html`

## Build Process

```bash
# Build IG with DAK API integration
./build-with-dak-api.sh

# Or manually run IG build first, then post-process
./_genonce.sh
python3 input/scripts/generate_dak_api_hub.py output
```

## Architecture Decision

This simplified approach was chosen over footer template modifications because:

- **Reliability**: Uses standard WHO template without custom dependencies
- **Maintainability**: No custom template files to maintain
- **Build Stability**: Avoids template dependency issues
- **User Access**: Menu navigation provides clear, discoverable access
