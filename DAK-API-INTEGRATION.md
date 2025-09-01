# DAK API Link Integration Approaches

This document outlines the different ways to add a `dak-api.html` link to the FHIR IG footer/navigation.

## Current Implementation

The repository now includes **multiple approaches** for integrating the DAK API link:

### 1. Menu Navigation Link (Already Existed)
**Location**: `sushi-config.yaml` lines 62-64
```yaml
menu:
  Home: index.html 
  Downloads: downloads.html
  Indices:
    Artifact Index: artifacts.html
    DAK API: dak-api.html
```
**Pros**: 
- Standard FHIR IG navigation approach
- Integrated with IG menu system
- No template customization required

**Cons**:
- May not be as prominent as footer link
- Requires dak-api.html to exist during build

### 2. Footer Link (Newly Added)
**Location**: `local-template/package/includes/_append.fragment-footer.html`
```html
<div style="text-align: center; margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #dee2e6;">
    <p style="color: #6c757d; font-size: 0.9rem;">
        <a href="dak-api.html" style="color: #0066cc; text-decoration: none;">📋 DAK API Documentation Hub</a>
    </p>
</div>
```
**Pros**:
- Appears on every page footer
- More prominent and visible
- Consistent with footer placement request

**Cons**:
- Requires local template activation
- Custom template maintenance

### 3. Page Configuration (Newly Added)
**Location**: `sushi-config.yaml` pages section
```yaml
pages:
  # ... other pages ...
  dak-api.html:
    title: DAK API Documentation Hub
```
**Pros**:
- Ensures page is properly included in IG
- Provides proper page metadata
- Integrates with IG page management

**Cons**:
- Requires file to exist during build

### 4. Build Integration (Newly Added)
**Location**: `build-with-dak-api.sh`
```bash
# Generate DAK API documentation hub
python3 input/scripts/generate_dak_api_hub.py output
```
**Pros**:
- Ensures dak-api.html is generated before IG build
- Automated as part of build process
- Prevents broken links

**Cons**:
- Requires build process modification

## Template Configuration Changes

To enable the footer link approach, the template configuration was changed:

**File**: `ig.ini`
```ini
# Changed from:
# template = who.template.root#current
# To:
template = #local-template
```

This activates the local template which includes the footer fragment.

## Recommended Approach

**Use all approaches together** for maximum compatibility:

1. **Menu link** - for standard navigation
2. **Footer link** - for prominence and accessibility  
3. **Page configuration** - for proper IG integration
4. **Build integration** - for automated generation

## Alternative Approaches Not Implemented

### 5. Template Override
Could override the entire footer template instead of using fragment append.

### 6. CSS-based Injection
Could use CSS content injection to add the link.

### 7. JavaScript-based Addition
Could use client-side JavaScript to add the link dynamically.

### 8. WHO Template Extension
Could extend the WHO template to include the link in their base template.

## Build Instructions

To build the IG with DAK API integration:

```bash
# Option 1: Use the integrated build script
./build-with-dak-api.sh

# Option 2: Manual steps
mkdir -p output
python3 input/scripts/generate_dak_api_hub.py output
./_genonce.sh
```

## Testing the Implementation

1. Ensure `dak-api.html` is generated in the output directory
2. Check that the menu link appears in the "Indices" section
3. Check that the footer link appears at the bottom of each page
4. Verify both links navigate to the correct API documentation hub