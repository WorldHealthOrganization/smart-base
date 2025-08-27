#!/usr/bin/env python3
"""
FHIR ValueSet JSON Schema Generator

This script processes the expansions.json file output by the FHIR IG publisher
and generates JSON schemas for each ValueSet that enumerate all valid codes
using the JSON Schema enum constraint.

The script is intended to be run after the IG publisher finishes processing
to create schemas that can be used for validation of data against the
expanded ValueSets.

Usage:
    python generate_valueset_schemas.py [expansions_json_path] [output_dir]

Author: SMART Guidelines Team
"""

import json
import os
import sys
import logging
from typing import Dict, List, Optional, Any
from pathlib import Path


def setup_logging() -> logging.Logger:
    """Configure logging for the script."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger(__name__)


def load_expansions_json(file_path: str) -> Optional[Dict[str, Any]]:
    """
    Load and parse the expansions.json file.
    
    Args:
        file_path: Path to the expansions.json file
        
    Returns:
        Parsed JSON data or None if failed to load
    """
    logger = logging.getLogger(__name__)
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        logger.info(f"Successfully loaded expansions.json from {file_path}")
        return data
    
    except FileNotFoundError:
        logger.error(f"Expansions file not found: {file_path}")
        return None
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in expansions file: {e}")
        return None
    except Exception as e:
        logger.error(f"Error loading expansions file: {e}")
        return None


def extract_valueset_codes(valueset_resource: Dict[str, Any]) -> List[str]:
    """
    Extract codes from a ValueSet resource's expansion.
    
    Args:
        valueset_resource: FHIR ValueSet resource with expansion
        
    Returns:
        List of codes from the expansion
    """
    logger = logging.getLogger(__name__)
    codes = []
    
    # Check if resource has expansion
    if 'expansion' not in valueset_resource:
        logger.warning(f"ValueSet {valueset_resource.get('id', 'unknown')} has no expansion")
        return codes
    
    expansion = valueset_resource['expansion']
    
    # Check if expansion has contains
    if 'contains' not in expansion:
        logger.warning(f"ValueSet {valueset_resource.get('id', 'unknown')} expansion has no contains")
        return codes
    
    # Extract codes from contains array
    for item in expansion['contains']:
        if 'code' in item:
            codes.append(item['code'])
    
    logger.info(f"Extracted {len(codes)} codes from ValueSet {valueset_resource.get('id', 'unknown')}")
    return codes


def generate_json_schema(valueset_resource: Dict[str, Any], codes: List[str]) -> Dict[str, Any]:
    """
    Generate a JSON schema for a ValueSet using enum constraints.
    
    Args:
        valueset_resource: FHIR ValueSet resource
        codes: List of valid codes for the enum
        
    Returns:
        JSON schema dictionary
    """
    valueset_id = valueset_resource.get('id', 'unknown')
    valueset_title = valueset_resource.get('title', valueset_resource.get('name', 'Unknown ValueSet'))
    valueset_url = valueset_resource.get('url', '')
    
    schema = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": f"{valueset_url}/schema" if valueset_url else f"#{valueset_id}-schema",
        "title": f"{valueset_title} Schema",
        "description": f"JSON Schema for {valueset_title} ValueSet codes. Generated from FHIR expansions.",
        "type": "string",
        "enum": codes
    }
    
    # Add metadata if available
    if valueset_url:
        schema["fhir:valueSet"] = valueset_url
    
    if 'version' in valueset_resource:
        schema["fhir:version"] = valueset_resource['version']
    
    if 'expansion' in valueset_resource and 'timestamp' in valueset_resource['expansion']:
        schema["fhir:expansionTimestamp"] = valueset_resource['expansion']['timestamp']
    
    return schema


def save_schema(schema: Dict[str, Any], output_dir: str, valueset_id: str) -> Optional[str]:
    """
    Save a JSON schema to a file.
    
    Args:
        schema: JSON schema dictionary
        output_dir: Directory to save schema files
        valueset_id: ValueSet ID for filename
        
    Returns:
        Filepath if saved successfully, None otherwise
    """
    logger = logging.getLogger(__name__)
    
    try:
        # Ensure output directory exists
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        # Create filename
        filename = f"{valueset_id}.schema.json"
        filepath = os.path.join(output_dir, filename)
        
        # Save schema
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(schema, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Saved schema for ValueSet {valueset_id} to {filepath}")
        return filepath
        
    except Exception as e:
        logger.error(f"Error saving schema for ValueSet {valueset_id}: {e}")
        return None


def generate_index_html(schema_files: List[str], output_dir: str) -> bool:
    """
    Generate an index.html file listing all generated schemas.
    
    Args:
        schema_files: List of schema file paths
        output_dir: Directory where schemas are saved
        
    Returns:
        True if index generated successfully, False otherwise
    """
    logger = logging.getLogger(__name__)
    
    try:
        # Create schemas subdirectory for index (inside the output directory)
        index_dir = os.path.join(output_dir, "schemas")
        Path(index_dir).mkdir(parents=True, exist_ok=True)
        
        index_path = os.path.join(index_dir, "index.html")
        
        # Generate HTML content
        html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FHIR ValueSet JSON Schemas</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        h1 { color: #333; }
        ul { list-style-type: none; padding: 0; }
        li { margin: 10px 0; }
        a { text-decoration: none; color: #0066cc; }
        a:hover { text-decoration: underline; }
        .schema-link { display: block; padding: 8px; background: #f5f5f5; border-radius: 4px; }
        .generated-info { color: #666; font-size: 0.9em; margin-top: 20px; }
    </style>
</head>
<body>
    <h1>FHIR ValueSet JSON Schemas</h1>
    <p>This page contains links to all generated JSON schemas for FHIR ValueSets.</p>
    
    <ul>
"""
        
        # Add links for each schema file
        for file_path in sorted(schema_files):
            filename = os.path.basename(file_path)
            # Create relative path from schemas/ to parent directory where schemas are stored
            relative_path = f"../{filename}"
            valueset_name = filename.replace('.schema.json', '')
            
            html_content += f'        <li><a href="{relative_path}" class="schema-link">{valueset_name}.schema.json</a></li>\n'
        
        html_content += """    </ul>
    
    <div class="generated-info">
        <p><em>Generated automatically by the FHIR ValueSet JSON Schema Generator</em></p>
    </div>
</body>
</html>"""
        
        # Save index file
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        logger.info(f"Generated index.html with {len(schema_files)} schema links at {index_path}")
        return True
        
    except Exception as e:
        logger.error(f"Error generating index.html: {e}")
        return False


def process_expansions(expansions_data: Dict[str, Any], output_dir: str) -> int:
    """
    Process the expansions data and generate schemas for all ValueSets.
    
    Args:
        expansions_data: Parsed expansions.json data
        output_dir: Directory to save schema files
        
    Returns:
        Number of schemas successfully generated
    """
    logger = logging.getLogger(__name__)
    
    # Check if it's a Bundle
    if expansions_data.get('resourceType') != 'Bundle':
        logger.error("Expansions data is not a FHIR Bundle")
        return 0
    
    # Check if Bundle has entries
    if 'entry' not in expansions_data:
        logger.warning("Bundle has no entries")
        return 0
    
    schemas_generated = 0
    schema_files = []
    
    # Process each entry
    for entry in expansions_data['entry']:
        if 'resource' not in entry:
            logger.warning("Bundle entry has no resource")
            continue
            
        resource = entry['resource']
        
        # Check if it's a ValueSet
        if resource.get('resourceType') != 'ValueSet':
            logger.debug(f"Skipping non-ValueSet resource: {resource.get('resourceType')}")
            continue
        
        valueset_id = resource.get('id', 'unknown')
        logger.info(f"Processing ValueSet: {valueset_id}")
        
        # Extract codes from expansion
        codes = extract_valueset_codes(resource)
        
        if not codes:
            logger.warning(f"No codes found for ValueSet {valueset_id}, skipping schema generation")
            continue
        
        # Generate schema
        schema = generate_json_schema(resource, codes)
        
        # Save schema
        schema_path = save_schema(schema, output_dir, valueset_id)
        if schema_path:
            schemas_generated += 1
            schema_files.append(schema_path)
    
    # Generate index.html
    if schema_files:
        generate_index_html(schema_files, output_dir)
    
    logger.info(f"Generated {schemas_generated} ValueSet schemas")
    return schemas_generated


def main():
    """Main entry point for the script."""
    logger = setup_logging()
    
    # Parse command line arguments
    if len(sys.argv) < 2:
        # Default paths
        expansions_path = "output/expansions.json"
        output_dir = "output"  # Changed to output schemas directly to output/ directory
    elif len(sys.argv) == 2:
        expansions_path = sys.argv[1]
        output_dir = "output"  # Changed default
    else:
        expansions_path = sys.argv[1]
        output_dir = sys.argv[2]
    
    logger.info(f"Processing expansions from: {expansions_path}")
    logger.info(f"Output directory: {output_dir}")
    
    # Load expansions.json
    expansions_data = load_expansions_json(expansions_path)
    if not expansions_data:
        logger.error("Failed to load expansions data")
        sys.exit(1)
    
    # Process expansions and generate schemas
    schemas_count = process_expansions(expansions_data, output_dir)
    
    if schemas_count > 0:
        logger.info(f"Successfully generated {schemas_count} ValueSet schemas in {output_dir}")
        sys.exit(0)
    else:
        logger.error("No schemas were generated")
        sys.exit(1)


if __name__ == "__main__":
    main()