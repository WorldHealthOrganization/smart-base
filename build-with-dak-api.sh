#!/bin/bash

# SMART Base IG Build Script
# This script runs the IG build first, then post-processes with DAK API hub

set -e

echo "=== SMART Base IG Build ==="

# Ensure output directory exists
mkdir -p output

# Ensure dak-api.md exists before IG publisher runs
touch input/pagecontent/dak-api.md

# Run the standard IG build process first
echo "Starting IG build process..."
if [ -f "_genonce.sh" ]; then
    ./_genonce.sh
else
    echo "Error: _genonce.sh not found. Cannot proceed with IG build."
    exit 1
fi

# Post-process: Generate DAK API documentation hub
echo "Post-processing DAK API documentation into generated HTML files..."
python3 input/scripts/generate_dak_api_hub.py output

echo "DAK API hub post-processing completed successfully."
echo "Build process completed."