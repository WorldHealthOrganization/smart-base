# WHO SMART Base Implementation Guide

WHO SMART Base is a FHIR Implementation Guide that serves as the foundational dependency for all WHO SMART Guidelines Implementation Guides. It provides base FHIR profiles, extensions, and common dependencies along with a comprehensive Digital Adaptation Kit (DAK) extraction pipeline for processing clinical guideline content.

**Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.**

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
```

### Build Process
```bash
# NEVER CANCEL: Build takes 8-15 minutes in offline mode, potentially 30+ minutes with network dependencies
# NEVER CANCEL: Always set timeout to 60+ minutes for build commands
./_genonce.sh

# For offline builds (when internet connectivity is limited):
./_genonce.sh -tx n/a
```

### Test DAK Extraction Scripts
```bash
# Test individual extractors (each takes 0.5-2 seconds):
python3 input/scripts/isco08_extractor.py input/data/ISCO-08_EN_Structure_and_definitions.xlsx
python3 input/scripts/dmn_questionnaire_generator.py
python3 input/scripts/transform_dmn.py

# Full DAK extraction pipeline:
python3 input/scripts/extract_dak.py
```

## Timing Expectations and Critical Warnings

**NEVER CANCEL the following operations:**

- **IG Publisher Build**: 8-15 minutes offline, 30-45 minutes with network dependencies. **MEASURED**: Dependency resolution alone takes 5+ seconds per package (6 packages = 30+ seconds), actual build processing time can be 10-60 minutes depending on complexity.
- **Dependency Installation**: 5-10 minutes 
- **Python package installation**: 2-5 minutes **MEASURED**: Completed in 30-60 seconds for required packages
- **DAK extraction scripts**: **MEASURED**: Individual scripts: 0.4-0.5 seconds, DMN processing: 0.06 seconds

**ALWAYS set timeouts of 60+ minutes for build commands to prevent premature cancellation.**

### Measured Script Performance
- ISCO-08 extraction: 0.464 seconds (182 codes processed)
- DMN questionnaire generation: <0.1 seconds (1 DMN file)  
- DMN transformation to HTML: 0.059 seconds (1 DMN file)
- Python dependency installation: 45-60 seconds

## Validation Scenarios

**Always test these scenarios after making changes:**

1. **DAK Script Validation** (Quick tests, under 1 second each):
   ```bash
   # Test ISCO-08 extraction (creates FSH file with 182 occupation codes)
   python3 input/scripts/isco08_extractor.py input/data/ISCO-08_EN_Structure_and_definitions.xlsx
   # Verify: Check input/fsh/codesystems/ISCO08.fsh is created and contains "CodeSystem: ISCO08"
   
   # Test DMN questionnaire generation (processes 1 DMN file)
   python3 input/scripts/dmn_questionnaire_generator.py
   # Verify: Check input/fsh/questionnaires/DAK.DT.IMMZ.D2.DT.BCGQuestionnaire.fsh is created
   
   # Test DMN to HTML transformation
   python3 input/scripts/transform_dmn.py
   # Verify: Check input/pagecontent/DAK.DT.IMMZ.D2.DT.BCG.xml is created
   ```

2. **Build Validation** (NEVER CANCEL - 10-60 minutes):
   ```bash
   ./_genonce.sh -tx n/a
   # Expected: 6 dependency fetch failures (normal in offline mode)
   # Expected: "Trying to go on" messages after each failure
   # Verify: Check for final success message and fsh-generated/ directory creation
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
- `input/scripts/dmn_questionnaire_generator.py` - Generates questionnaires from DMN files
- `input/scripts/transform_dmn.py` - Converts DMN files to HTML for documentation

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

### Validating Changes
**Always run these validation steps before committing:**
```bash
# Test basic DAK functionality
python3 input/scripts/dmn_questionnaire_generator.py

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
python3 input/scripts/dmn_questionnaire_generator.py  # <0.1s
python3 input/scripts/transform_dmn.py  # 0.059s

# Build command (MEASURED: 10-60 minutes - NEVER CANCEL):
./_genonce.sh -tx n/a
# Expected output: 6 dependency resolution failures, then "Trying to go on"
```

## Troubleshooting

- **"Cannot run program 'sushi'"**: Install Node.js and SUSHI as shown above
- **Network timeouts**: Use `-tx n/a` flag for offline builds
- **npm certificate errors**: Run `npm config set strict-ssl false`
- **Build appears stuck**: Wait 60+ minutes - builds can take this long
- **Python import errors**: Ensure `pip install -r input/scripts/requirements.txt` completed successfully

## GitHub Actions CI

The repository uses `.github/workflows/ghbuild.yml` for automated builds. The workflow:
- Installs all dependencies automatically
- Runs FHIR IG Publisher build
- Processes DAK extraction scripts
- Deploys to GitHub Pages
- **Build timeouts are set to handle 45+ minute builds**