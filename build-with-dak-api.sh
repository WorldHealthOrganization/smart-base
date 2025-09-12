#!/bin/bash

# SMART Base IG Build Script
# This script ensures the DAK API hub is generated before the IG build

set -e

echo "=== SMART Base IG Build ==="

# Ensure output directory exists
mkdir -p output

# Ensure dak-api.md exists before generating DAK API hub
touch input/pagecontent/dak-api.md

# Generate DAK API documentation hub
echo "Generating DAK API documentation hub..."
python3 input/scripts/generate_dak_api_hub.py output

echo "DAK API hub generated successfully at output/dak-api.html"

# Run the standard IG build process
echo "Starting IG build process..."
if [ -f "_genonce.sh" ]; then
    ./_genonce.sh
else
    echo "Warning: _genonce.sh not found. Run this manually after the script completes."
fi

echo "Build process completed."