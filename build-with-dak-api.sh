#!/bin/bash

# SMART Base IG Build Script
# This script runs IG publisher first, then post-processes with DAK API hub

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
    echo "Warning: _genonce.sh not found. Please run IG publisher manually first."
    exit 1
fi

# Post-process with DAK API documentation hub
echo "Post-processing with DAK API documentation hub..."
python3 input/scripts/generate_dak_api_hub.py output

echo "DAK API hub post-processing completed."
echo "Build process completed."