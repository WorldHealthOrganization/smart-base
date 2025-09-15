# WHO SMART Base Implementation Guide

WHO SMART Base is a FHIR Implementation Guide that serves as the foundational dependency for all WHO SMART Guidelines Implementation Guides. It provides base FHIR profiles, extensions, and common dependencies along with a comprehensive Digital Adaptation Kit (DAK) extraction pipeline for processing clinical guideline content.

**Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.**

## Critical Build Notes

⚠️ **IMPORTANT**: The full IG build currently requires SUSHI (FSH processor) which may have installation challenges in some environments. However, **all DAK extraction scripts work independently** and can be used for content processing even when the full build fails.

The DAK scripts are the core value of this repository and are fully functional for processing clinical guideline content. Another main value of this repository is that it defines the schemas (Logical models, JSON schema) for computable representations of WHO DAK content.

## Working Effectively

### Bootstrap and Dependencies
```bash
# Install required dependencies
sudo apt-get update && sudo apt-get install -y openjdk-17-jdk curl wget
pip install -r input/scripts/requirements.txt

# Download FHIR IG Publisher
./_updatePublisher.sh -y

# Install Node.js and SUSHI (for FSH processing)
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install nodejs -y
npm config set strict-ssl false  # If certificate issues occur
sudo npm install -g fsh-sushi

# TROUBLESHOOTING: If SUSHI fails with "Cannot find module" errors:
# The build can still proceed without SUSHI for basic validation
```

### Build Process
```bash
# NEVER CANCEL: Build takes 7+ seconds even when failing, potentially 30-60 minutes for complete builds
# NEVER CANCEL: Always set timeout to 60+ minutes for build commands
./_genonce.sh

# For offline builds (when internet connectivity is limited):
./_genonce.sh -tx n/a

# Expected behavior: 6 dependency fetch failures, then SUSHI execution attempt
# If SUSHI fails, build stops at ~7-8 seconds with "Process exited with an error: 1"
```

## Alternative: DAK-Only Workflow (Always Works)

If IG build fails due to SUSHI issues, use the DAK extraction scripts directly:

```bash
# Core workflow that always works:
pip install -r input/scripts/requirements.txt  # 45-60 seconds

# Process your content:
python3 input/scripts/isco08_extractor.py input/data/ISCO-08_EN_Structure_and_definitions.xlsx
python3 input/scripts/transform_dmn.py

# Generated FSH files can be manually reviewed or processed with external SUSHI installation
```

### Test DAK Extraction Scripts
```bash
# Test individual extractors (each takes 0.5-2 seconds):
python3 input/scripts/isco08_extractor.py input/data/ISCO-08_EN_Structure_and_definitions.xlsx
python3 input/scripts/transform_dmn.py

# Full DAK extraction pipeline:
python3 input/scripts/extract_dak.py
```

## WHO DAK Content Schemas (Logical Models & JSON Schemas)

WHO SMART Base defines comprehensive schemas for computable representations of WHO DAK content through FHIR Logical Models and generated JSON schemas:

### FHIR Logical Models
The repository includes logical models in `input/fsh/models/` that define the structure for:

```bash
# Core DAK logical models (view with):
ls input/fsh/models/
# Key models include:
# - DAK.fsh - Complete Digital Adaptation Kit structure
# - GenericPersona.fsh - Human and system actors 
# - HealthInterventions.fsh - WHO health interventions and recommendations
# - Requirements.fsh - Functional and non-functional requirements
# - BusinessProcessWorkflow.fsh - Clinical care workflows
# - DecisionSupportLogic.fsh - Clinical decision logic
# - ProgramIndicator.fsh - Health program indicators
```

### JSON Schema Generation
Generate JSON schemas from FHIR logical models for validation:

```bash
# Generate schemas from logical models (requires completed IG build):
python3 input/scripts/generate_logical_model_schemas.py
python3 input/scripts/generate_valueset_schemas.py

# Schemas enable validation of DAK content against WHO standards
# Generated schemas are used for data interchange and validation
```

### Schema Validation Use Cases
- **DAK Content Validation**: Ensure DAK data conforms to WHO standards
- **Data Interchange**: Standardized JSON representations for system integration  
- **Implementation Verification**: Validate local adaptations against WHO schemas
- **Quality Assurance**: Automated validation of DAK content during development

## Timing Expectations and Critical Warnings

**NEVER CANCEL the following operations:**

- **IG Publisher Build**: **MEASURED**: 7-8 seconds for dependency resolution + SUSHI failure, 30-60+ minutes for complete successful builds
- **Dependency Installation**: 5-10 minutes 
- **Python package installation**: **MEASURED**: 45-60 seconds for required packages
- **DAK extraction scripts**: **MEASURED**: Individual scripts: 0.4-0.5 seconds, DMN processing: 0.06 seconds

**ALWAYS set timeouts of 60+ minutes for build commands to prevent premature cancellation.**

### Measured Script Performance
- ISCO-08 extraction: 0.464 seconds (182 codes processed)
- DMN transformation to HTML: 0.059 seconds (1 DMN file)
- Python dependency installation: 45-60 seconds
- **IG Publisher dependency resolution**: 7.3 seconds (6 dependencies, all failing offline)
- **Build failure time**: 7.859 seconds (when SUSHI installation issues occur)

## Validation Scenarios

**Always test these scenarios after making changes:**

1. **DAK Script Validation** (Quick tests, under 1 second each):
   ```bash
   # Test ISCO-08 extraction (creates FSH file with 182 occupation codes)
   python3 input/scripts/isco08_extractor.py input/data/ISCO-08_EN_Structure_and_definitions.xlsx
   # Verify: Check input/fsh/codesystems/ISCO08.fsh is created and contains "CodeSystem: ISCO08"
   
   # Test DMN to HTML transformation
   python3 input/scripts/transform_dmn.py
   # Verify: Check input/pagecontent/DAK.DT.IMMZ.D2.DT.BCG.xml is created
   ```

2. **Build Validation** (NEVER CANCEL - may fail quickly if SUSHI issues):
   ```bash
   ./_genonce.sh -tx n/a
   # Expected: 6 dependency fetch failures (normal in offline mode)
   # Expected: "Trying to go on" messages after each failure
   # Expected: SUSHI execution attempt at ~7 seconds
   # Possible: "Process exited with an error: 1" if SUSHI installation incomplete
   # Verify: Check console output for specific error messages
   ```

3. **FSH Compilation Validation** (requires SUSHI):
   ```bash
   sushi
   # Verify: Check fsh-generated/resources/ directory contains FHIR JSON files
   ```

## Network Limitations and Workarounds

- **Offline builds work** but with limited functionality using `-tx n/a` flag
- **FHIR package dependencies** may fail to download - this is expected in offline environments
- **npm certificate issues**: Use `npm config set strict-ssl false` if needed
- **Build will continue** even if some dependencies fail to download

## Project Structure

### Core Directories
- `input/fsh/` - FHIR Shorthand definitions (profiles, extensions, valuesets)
- `input/fsh/models/` - FHIR Logical Models defining WHO DAK content schemas
- `input/scripts/` - Python DAK extraction pipeline
- `input/data/` - Sample data files for testing extractors
- `input/dmn/` - Decision tables in DMN format
- `input/pagecontent/` - Markdown content for the IG
- `fsh-generated/` - Generated FHIR resources (created during build)
- `output/` - Final IG website output (created during build)

### Key Scripts
- `_updatePublisher.sh` - Downloads latest FHIR IG Publisher
- `_genonce.sh` - Runs complete IG build process
- `input/scripts/extract_dak.py` - Main DAK extraction orchestrator
- `input/scripts/isco08_extractor.py` - ISCO-08 occupation codes extractor
- `input/scripts/transform_dmn.py` - Converts DMN files to HTML for documentation
- `input/scripts/generate_logical_model_schemas.py` - Generates JSON schemas from FHIR logical models
- `input/scripts/generate_valueset_schemas.py` - Generates JSON schemas from FHIR value sets

### Configuration Files
- `sushi-config.yaml` - Main SUSHI configuration for the FHIR IG
- `ig.ini` - IG Publisher configuration
- `input/scripts/requirements.txt` - Python dependencies

## Common Tasks

### Adding New FHIR Profiles
1. Create `.fsh` files in appropriate `input/fsh/` subdirectories
2. Update `sushi-config.yaml` if needed
3. Run build: `./_genonce.sh -tx n/a`
4. Verify output in `fsh-generated/resources/`

### Processing New DAK Content
1. Place Excel/DMN/BPMN files in appropriate `input/` subdirectories
2. Run relevant extractor: `python3 input/scripts/[extractor_name].py [input_file]`
3. Verify generated FSH files in `input/fsh/`
4. Run build to generate final FHIR resources

### Working with WHO DAK Content Schemas
1. Review logical models in `input/fsh/models/` to understand DAK structure
2. After successful IG build, generate JSON schemas:
   ```bash
   python3 input/scripts/generate_logical_model_schemas.py
   python3 input/scripts/generate_valueset_schemas.py
   ```
3. Use generated schemas for validating DAK content representations
4. Reference schemas in implementation guides and system integrations

### Validating Changes
**Always run these validation steps before committing:**
```bash
# Test basic DAK functionality
python3 input/scripts/transform_dmn.py

# Test build process (NEVER CANCEL - wait 60+ minutes if needed)
./_genonce.sh -tx n/a

# Check for build errors in console output
# Verify fsh-generated/ and output/ directories are populated
```

## Dependencies Summary

- **Java**: OpenJDK 17+ (17.0.16 confirmed working)
- **Node.js**: LTS version + npm (for SUSHI)
- **Python**: 3.12+ with packages: pdfplumber, pandas, openpyxl, lxml, PyYAML
- **Internet**: Optional for basic operation, required for full FHIR package dependencies

## Known Working Commands Reference

```bash
# Environment setup (verified working):
java -version  # Should show OpenJDK 17+ (confirmed: 17.0.16)
python3 --version  # Should show 3.12+ (confirmed: 3.12.3)
pip install -r input/scripts/requirements.txt  # Takes 45-60 seconds

# Quick validation tests (all verified under 1 second):
python3 input/scripts/isco08_extractor.py input/data/ISCO-08_EN_Structure_and_definitions.xlsx  # 0.464s
python3 input/scripts/transform_dmn.py  # 0.059s

# Build command (MEASURED: 7-8 seconds until SUSHI failure, up to 60 minutes for successful builds):
./_genonce.sh -tx n/a
# Expected output: 6 dependency resolution failures, then SUSHI failure
# Common error: "Process exited with an error: 1" due to SUSHI installation issues
```

## Troubleshooting

- **"Cannot run program 'sushi'"**: Install Node.js and SUSHI as shown above
- **"Cannot find module 'fs-extra'"**: SUSHI installation incomplete - build will fail at ~7-8 seconds
- **Network timeouts**: Use `-tx n/a` flag for offline builds
- **npm certificate errors**: Run `npm config set strict-ssl false`
- **Build appears stuck**: Wait 60+ minutes - builds can take this long
- **Python import errors**: Ensure `pip install -r input/scripts/requirements.txt` completed successfully
- **"Process exited with an error: 1"**: Normal when SUSHI has installation issues - DAK scripts still work independently

## GitHub Actions CI

The repository uses `.github/workflows/ghbuild.yml` for automated builds. The workflow:
- Installs all dependencies automatically
- Runs FHIR IG Publisher build
- Processes DAK extraction scripts
- Deploys to GitHub Pages
- **Build timeouts are set to handle 45+ minute builds**