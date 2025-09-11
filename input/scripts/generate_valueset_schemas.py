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


def extract_valueset_id_from_entry(entry: Dict[str, Any]) -> str:
    """
    Extract the ValueSet ID from a Bundle entry and its resource.
    
    Args:
        entry: Bundle entry containing a ValueSet resource
        
    Returns:
        ValueSet ID or 'unknown' if cannot be determined
    """
    valueset_resource = entry.get('resource', {})
    
    # Try different sources for the ID in order of preference
    
    # 1. Direct 'id' field in resource
    if 'id' in valueset_resource and valueset_resource['id'] != 'unknown':
        return valueset_resource['id']
    
    # 2. Extract from resource 'url' field (canonical URL)
    if 'url' in valueset_resource:
        url = valueset_resource['url']
        # Extract the last part of the URL after the last '/'
        if '/' in url:
            return url.split('/')[-1]
    
    # 3. Extract from Bundle entry 'fullUrl' field
    if 'fullUrl' in entry:
        full_url = entry['fullUrl']
        # Extract the last part of the URL after the last '/'
        if '/' in full_url:
            return full_url.split('/')[-1]
    
    # 4. Use 'name' field if available
    if 'name' in valueset_resource and valueset_resource['name']:
        return valueset_resource['name']
    
    # 5. Extract from title if it's in a recognizable format
    if 'title' in valueset_resource:
        title = valueset_resource['title']
        # If title contains common patterns, try to extract ID
        # This is a fallback for cases where title might contain the logical name
        words = title.replace(' ', '').replace('-', '').replace('_', '')
        if words and not words.lower().startswith('unknown'):
            return words
    
    return 'unknown'


def extract_valueset_id(valueset_resource: Dict[str, Any]) -> str:
    """
    Extract the ValueSet ID from various possible sources.
    (Legacy function - kept for backwards compatibility)
    
    Args:
        valueset_resource: FHIR ValueSet resource
        
    Returns:
        ValueSet ID or 'unknown' if cannot be determined
    """
    # Try different sources for the ID in order of preference
    
    # 1. Direct 'id' field
    if 'id' in valueset_resource and valueset_resource['id'] != 'unknown':
        return valueset_resource['id']
    
    # 2. Extract from 'url' field (canonical URL)
    if 'url' in valueset_resource:
        url = valueset_resource['url']
        # Extract the last part of the URL after the last '/'
        if '/' in url:
            return url.split('/')[-1]
    
    # 3. Use 'name' field if available
    if 'name' in valueset_resource and valueset_resource['name']:
        return valueset_resource['name']
    
    # 4. Extract from title if it's in a recognizable format
    if 'title' in valueset_resource:
        title = valueset_resource['title']
        # If title contains common patterns, try to extract ID
        # This is a fallback for cases where title might contain the logical name
        words = title.replace(' ', '').replace('-', '').replace('_', '')
        if words and not words.lower().startswith('unknown'):
            return words
    
    return 'unknown'


def extract_valueset_codes(valueset_resource: Dict[str, Any], valueset_id: str = None) -> List[str]:
    """
    Extract codes from a ValueSet resource's expansion.
    
    Args:
        valueset_resource: FHIR ValueSet resource with expansion
        valueset_id: Optional ValueSet ID for logging (if not provided, will be extracted)
        
    Returns:
        List of codes from the expansion
    """
    logger = logging.getLogger(__name__)
    codes = []
    
    if valueset_id is None:
        valueset_id = extract_valueset_id(valueset_resource)
    
    # Check if resource has expansion
    if 'expansion' not in valueset_resource:
        logger.warning(f"ValueSet {valueset_id} has no expansion")
        return codes
    
    expansion = valueset_resource['expansion']
    
    # Check if expansion has contains
    if 'contains' not in expansion:
        logger.warning(f"ValueSet {valueset_id} expansion has no contains")
        return codes
    
    # Extract codes from contains array
    for item in expansion['contains']:
        if 'code' in item:
            codes.append(item['code'])
    
    logger.info(f"Extracted {len(codes)} codes from ValueSet {valueset_id}")
    return codes


def extract_valueset_codes_with_display(valueset_resource: Dict[str, Any], valueset_id: str = None) -> List[Dict[str, str]]:
    """
    Extract codes with their display values and system URIs from a ValueSet resource's expansion.
    
    Args:
        valueset_resource: FHIR ValueSet resource with expansion
        valueset_id: Optional ValueSet ID for logging (if not provided, will be extracted)
        
    Returns:
        List of dictionaries containing 'code', 'display', and 'system' keys
    """
    logger = logging.getLogger(__name__)
    codes_with_display = []
    
    if valueset_id is None:
        valueset_id = extract_valueset_id(valueset_resource)
    
    # Check if resource has expansion
    if 'expansion' not in valueset_resource:
        logger.warning(f"ValueSet {valueset_id} has no expansion")
        return codes_with_display
    
    expansion = valueset_resource['expansion']
    
    # Check if expansion has contains
    if 'contains' not in expansion:
        logger.warning(f"ValueSet {valueset_id} expansion has no contains")
        return codes_with_display
    
    # Extract codes, displays, and systems from contains array
    for item in expansion['contains']:
        if 'code' in item:
            code_entry = {'code': item['code']}
            if 'display' in item and item['display'].strip():
                code_entry['display'] = item['display']
            else:
                # Fallback to code if no display is available or display is empty
                code_entry['display'] = item['code']
            
            # Include system URI if available
            if 'system' in item:
                code_entry['system'] = item['system']
            
            codes_with_display.append(code_entry)
    
    logger.info(f"Extracted {len(codes_with_display)} codes with displays and systems from ValueSet {valueset_id}")
    return codes_with_display


def generate_json_schema(valueset_resource: Dict[str, Any], codes_with_display: List[Dict[str, str]]) -> Dict[str, Any]:
    """
    Generate a JSON schema for a ValueSet using enum constraints with IRI-formatted values that match JSON-LD format.
    
    Args:
        valueset_resource: FHIR ValueSet resource
        codes_with_display: List of dictionaries with 'code', 'display', and optionally 'system' keys
        
    Returns:
        JSON schema dictionary
    """
    valueset_id = extract_valueset_id(valueset_resource)
    valueset_title = valueset_resource.get('title', valueset_resource.get('name', 'Unknown ValueSet'))
    valueset_url = valueset_resource.get('url', '')
    
    # Construct schema $id based on ValueSet canonical URL pattern
    if valueset_url:
        # Extract base URL from canonical URL
        # e.g., http://smart.who.int/base/ValueSet/DecisionTableActions -> http://smart.who.int/base
        if '/ValueSet/' in valueset_url:
            base_url = valueset_url.split('/ValueSet/')[0]
            schema_id = f"{base_url}/ValueSet-{valueset_id}.schema.json"
        else:
            # Fallback if URL doesn't follow expected pattern
            schema_id = f"{valueset_url}-{valueset_id}.schema.json"
    else:
        schema_id = f"#ValueSet-{valueset_id}-schema"
    
    # Use absolute URLs for file references
    if valueset_url and '/ValueSet/' in valueset_url:
        base_url = valueset_url.split('/ValueSet/')[0]
        display_reference = f"{base_url}/ValueSet-{valueset_id}.displays.json"
    else:
        display_reference = f"ValueSet-{valueset_id}.displays.json"
    
    # Generate IRI-formatted enum values that match JSON-LD format
    enum_values = []
    for item in codes_with_display:
        code = item['code']
        system = item.get('system', '')
        
        # Generate canonical IRI for the code using same logic as JSON-LD
        enum_iri = generate_canonical_iri(code, valueset_url, system)
        enum_values.append(enum_iri)
    
    schema = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": schema_id,
        "title": f"{valueset_title} Schema",
        "description": f"JSON Schema for {valueset_title} ValueSet codes. Generated from FHIR expansions using IRI format.",
        "type": "string",
        "enum": enum_values
    }
    
    # Add narrative that reflects the IRI format (system URIs are embedded, no separate system file needed)
    narrative_text = f"This schema validates IRI-formatted codes for the {valueset_title} ValueSet. "
    narrative_text += f"Each enum value includes the system URI in the format {{systemuri}}#{{code}} to match JSON-LD enumeration IRIs. "
    narrative_text += f"Display values are available at {display_reference}. "
    narrative_text += f"For a complete listing of all ValueSets, see artifacts.html#terminology-value-sets."
    schema["narrative"] = narrative_text
    
    # References to display file (no system file needed since system URIs are embedded in enum values)
    schema["fhir:displays"] = display_reference
    
    # Add metadata if available
    if valueset_url:
        schema["fhir:valueSet"] = valueset_url
    
    if 'version' in valueset_resource:
        schema["fhir:version"] = valueset_resource['version']
    
    if 'expansion' in valueset_resource and 'timestamp' in valueset_resource['expansion']:
        schema["fhir:expansionTimestamp"] = valueset_resource['expansion']['timestamp']
    
    return schema


def generate_display_file(valueset_resource: Dict[str, Any], codes_with_display: List[Dict[str, str]]) -> Dict[str, Any]:
    """
    Generate a display file for a ValueSet containing only display values for translation support.
    
    Args:
        valueset_resource: FHIR ValueSet resource
        codes_with_display: List of dictionaries with 'code', 'display', and optionally 'system' keys
        
    Returns:
        Display file dictionary
    """
    valueset_id = extract_valueset_id(valueset_resource)
    valueset_title = valueset_resource.get('title', valueset_resource.get('name', 'Unknown ValueSet'))
    valueset_url = valueset_resource.get('url', '')
    
    # Construct display file $id based on ValueSet canonical URL pattern
    if valueset_url:
        if '/ValueSet/' in valueset_url:
            base_url = valueset_url.split('/ValueSet/')[0]
            display_id = f"{base_url}/ValueSet-{valueset_id}.displays.json"
        else:
            display_id = f"{valueset_url}-{valueset_id}.displays.json"
    else:
        display_id = f"#ValueSet-{valueset_id}-displays"
    
    # Extract displays with multilingual structure support using IRI format to match schema enum values
    displays = {}
    
    for item in codes_with_display:
        code = item['code']
        display = item['display']
        system = item.get('system', '')
        
        # Generate canonical IRI for the code using same logic as JSON schema enum values
        code_iri = generate_canonical_iri(code, valueset_url, system)
        
        # Structure displays to support multiple languages
        # For now, use 'en' as the default language since FHIR expansions typically contain English text
        # This structure allows for easy addition of other languages later
        displays[code_iri] = {
            "en": display
        }
    
    display_file = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": display_id,
        "title": f"{valueset_title} Display Values",
        "description": f"Display values for {valueset_title} ValueSet codes. Generated from FHIR expansions.",
        "type": "object",
        "properties": {
            "fhir:displays": {
                "type": "object",
                "description": "Multilingual display values for ValueSet codes using IRI format to match JSON schema enum values",
                "patternProperties": {
                    "^https?://.*": {
                        "type": "object",
                        "description": "Display values for a specific IRI-formatted code by language",
                        "properties": {
                            "en": {
                                "type": "string",
                                "description": "English display value"
                            }
                        },
                        "patternProperties": {
                            "^[a-z]{2}(-[A-Z]{2})?$": {
                                "type": "string",
                                "description": "Display value in the specified language (ISO 639-1 code)"
                            }
                        },
                        "additionalProperties": False
                    }
                },
                "additionalProperties": False
            }
        },
        "required": ["fhir:displays"],
        "additionalProperties": True,
        "fhir:displays": displays
    }
    
    # Add metadata if available
    if valueset_url:
        display_file["fhir:valueSet"] = valueset_url
    
    if 'version' in valueset_resource:
        display_file["fhir:version"] = valueset_resource['version']
    
    if 'expansion' in valueset_resource and 'timestamp' in valueset_resource['expansion']:
        display_file["fhir:expansionTimestamp"] = valueset_resource['expansion']['timestamp']
    
    return display_file


def generate_system_file(valueset_resource: Dict[str, Any], codes_with_display: List[Dict[str, str]]) -> Dict[str, Any]:
    """
    Generate a system file for a ValueSet containing code to system URI mappings.
    
    Args:
        valueset_resource: FHIR ValueSet resource
        codes_with_display: List of dictionaries with 'code', 'display', and optionally 'system' keys
        
    Returns:
        System file dictionary
    """
    valueset_id = extract_valueset_id(valueset_resource)
    valueset_title = valueset_resource.get('title', valueset_resource.get('name', 'Unknown ValueSet'))
    valueset_url = valueset_resource.get('url', '')
    
    # Construct system file $id based on ValueSet canonical URL pattern
    if valueset_url:
        if '/ValueSet/' in valueset_url:
            base_url = valueset_url.split('/ValueSet/')[0]
            system_id = f"{base_url}/ValueSet-{valueset_id}.system.json"
        else:
            system_id = f"{valueset_url}-{valueset_id}.system.json"
    else:
        system_id = f"#ValueSet-{valueset_id}-system"
    
    # Extract system URIs mapping
    systems = {}
    
    for item in codes_with_display:
        code = item['code']
        system = item.get('system', '')
        
        if system:
            systems[code] = system
    
    system_file = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": system_id,
        "title": f"{valueset_title} System URIs",
        "description": f"System URI mappings for {valueset_title} ValueSet codes. Generated from FHIR expansions.",
        "type": "object",
        "properties": {
            "fhir:systems": {
                "type": "object",
                "description": "Mapping of ValueSet codes to their corresponding system URIs",
                "patternProperties": {
                    "^[a-zA-Z0-9._-]+$": {
                        "type": "string",
                        "format": "uri",
                        "description": "System URI for the corresponding code"
                    }
                },
                "additionalProperties": False
            }
        },
        "required": ["fhir:systems"],
        "additionalProperties": True,
        "fhir:systems": systems
    }
    
    # Add metadata if available
    if valueset_url:
        system_file["fhir:valueSet"] = valueset_url
    
    if 'version' in valueset_resource:
        system_file["fhir:version"] = valueset_resource['version']
    
    if 'expansion' in valueset_resource and 'timestamp' in valueset_resource['expansion']:
        system_file["fhir:expansionTimestamp"] = valueset_resource['expansion']['timestamp']
    
    return system_file


def generate_canonical_iri(code: str, valueset_url: str, system_uri: str = None) -> str:
    """
    Generate a canonical IRI for a code using a deterministic pattern.
    
    Args:
        code: The code value
        valueset_url: The ValueSet canonical URL
        system_uri: Optional system URI for the code
        
    Returns:
        Canonical IRI for the code
    """
    # If we have a system URI, use it as the base
    if system_uri:
        # Ensure system URI ends with # or / for fragment/path appending
        if not system_uri.endswith(('#', '/')):
            return f"{system_uri}#{code}"
        else:
            return f"{system_uri}{code}"
    
    # Fall back to using ValueSet URL as base
    if valueset_url:
        # Use the base URL from the ValueSet canonical URL
        if '/ValueSet/' in valueset_url:
            base_url = valueset_url.split('/ValueSet/')[0]
            return f"{base_url}/CodeSystem/{code}"
        else:
            # Fallback pattern
            return f"{valueset_url}#{code}"
    
    # Final fallback
    return f"http://example.com/codes#{code}"


def generate_jsonld_vocabulary(valueset_resource: Dict[str, Any], codes_with_display: List[Dict[str, str]]) -> Dict[str, Any]:
    """
    Generate a JSON-LD vocabulary for a ValueSet that defines an Enumeration class,
    declares each code as a member of that Enumeration, and creates a property
    whose allowed range is that Enumeration.
    
    Args:
        valueset_resource: FHIR ValueSet resource
        codes_with_display: List of dictionaries with 'code', 'display', and optionally 'system' keys
        
    Returns:
        JSON-LD vocabulary dictionary
    """
    valueset_id = extract_valueset_id(valueset_resource)
    valueset_title = valueset_resource.get('title', valueset_resource.get('name', 'Unknown ValueSet'))
    valueset_description = valueset_resource.get('description', f"Allowed values for the {valueset_title} enumeration.")
    valueset_url = valueset_resource.get('url', '')
    valueset_version = valueset_resource.get('version', '')
    valueset_date = None
    valueset_publisher = valueset_resource.get('publisher', 'World Health Organization')
    
    # Extract date from expansion timestamp if available
    if 'expansion' in valueset_resource and 'timestamp' in valueset_resource['expansion']:
        valueset_date = valueset_resource['expansion']['timestamp']
    elif 'date' in valueset_resource:
        valueset_date = valueset_resource['date']
    
    # Determine base vocabulary IRI
    if valueset_url:
        if '/ValueSet/' in valueset_url:
            base_url = valueset_url.split('/ValueSet/')[0]
            vocab_base = f"{base_url}/vocab"
        else:
            vocab_base = f"{valueset_url}/vocab"
    else:
        vocab_base = "http://example.com/vocab"
    
    # Create enumeration class IRI
    enumeration_class_iri = f"{vocab_base}#{valueset_id}Enumeration"
    property_iri = f"{vocab_base}#{valueset_id.lower()}"
    
    # JSON-LD context
    context = {
        "@vocab": f"{vocab_base}#",
        "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "schema": "https://schema.org/",
        "fhir": "http://hl7.org/fhir/",
        "id": "@id",
        "type": "@type",
        "name": "rdfs:label",
        "comment": "rdfs:comment",
        "version": "schema:version",
        "date": "schema:dateCreated",
        "publisher": "schema:publisher"
    }
    
    # Start building the @graph
    graph = []
    
    # 1. Define the Enumeration class
    enumeration_class = {
        "id": enumeration_class_iri,
        "type": "schema:Enumeration",
        "name": f"{valueset_title} Enumeration",
        "comment": valueset_description
    }
    
    # Add metadata if available
    if valueset_version:
        enumeration_class["version"] = valueset_version
    if valueset_date:
        enumeration_class["date"] = valueset_date
    if valueset_publisher:
        enumeration_class["publisher"] = valueset_publisher
    if valueset_url:
        enumeration_class["fhir:valueSet"] = valueset_url
    
    graph.append(enumeration_class)
    
    # 2. Declare each code as a member (instance) of the Enumeration
    for item in codes_with_display:
        code = item['code']
        display = item['display']
        system = item.get('system', '')
        
        # Generate canonical IRI for the code
        code_iri = generate_canonical_iri(code, valueset_url, system)
        
        code_instance = {
            "id": code_iri,
            "type": enumeration_class_iri,
            "name": display,
            "fhir:code": code
        }
        
        # Add system information if available
        if system:
            code_instance["fhir:system"] = system
        
        graph.append(code_instance)
    
    # 3. Declare a property whose allowed range is the Enumeration
    property_definition = {
        "id": property_iri,
        "type": "rdf:Property",
        "name": valueset_id.lower(),
        "comment": f"Property for selecting a value from the {valueset_title} enumeration.",
        "schema:rangeIncludes": {"id": enumeration_class_iri}
    }
    
    # Add domain information if this is a specific use case
    # For now, we'll leave the domain open as this is a general enumeration
    
    graph.append(property_definition)
    
    # Create the complete JSON-LD document
    jsonld_vocab = {
        "@context": context,
        "@graph": graph
    }
    
    return jsonld_vocab


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
        
        # Create filename with ValueSet- prefix
        filename = f"ValueSet-{valueset_id}.schema.json"
        filepath = os.path.join(output_dir, filename)
        
        # Save schema
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(schema, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Saved schema for ValueSet {valueset_id} to {filepath}")
        return filepath
        
    except Exception as e:
        logger.error(f"Error saving schema for ValueSet {valueset_id}: {e}")
        return None


def save_display_file(display_file: Dict[str, Any], output_dir: str, valueset_id: str) -> Optional[str]:
    """
    Save a display file to a file.
    
    Args:
        display_file: Display file dictionary
        output_dir: Directory to save display files
        valueset_id: ValueSet ID for filename
        
    Returns:
        Filepath if saved successfully, None otherwise
    """
    logger = logging.getLogger(__name__)
    
    try:
        # Ensure output directory exists
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        # Create filename with ValueSet- prefix
        filename = f"ValueSet-{valueset_id}.displays.json"
        filepath = os.path.join(output_dir, filename)
        
        # Save display file
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(display_file, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Saved display file for ValueSet {valueset_id} to {filepath}")
        return filepath
        
    except Exception as e:
        logger.error(f"Error saving display file for ValueSet {valueset_id}: {e}")
        return None


def save_system_file(system_file: Dict[str, Any], output_dir: str, valueset_id: str) -> Optional[str]:
    """
    Save a system file to a file.
    
    Args:
        system_file: System file dictionary
        output_dir: Directory to save system files
        valueset_id: ValueSet ID for filename
        
    Returns:
        Filepath if saved successfully, None otherwise
    """
    logger = logging.getLogger(__name__)
    
    try:
        # Ensure output directory exists
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        # Create filename with ValueSet- prefix
        filename = f"ValueSet-{valueset_id}.system.json"
        filepath = os.path.join(output_dir, filename)
        
        # Save system file
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(system_file, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Saved system file for ValueSet {valueset_id} to {filepath}")
        return filepath
        
    except Exception as e:
        logger.error(f"Error saving system file for ValueSet {valueset_id}: {e}")
        return None


def save_jsonld_vocabulary(jsonld_vocab: Dict[str, Any], output_dir: str, valueset_id: str) -> Optional[str]:
    """
    Save a JSON-LD vocabulary file.
    
    Args:
        jsonld_vocab: JSON-LD vocabulary dictionary
        output_dir: Directory to save JSON-LD files
        valueset_id: ValueSet ID for filename
        
    Returns:
        Filepath if saved successfully, None otherwise
    """
    logger = logging.getLogger(__name__)
    
    try:
        # Ensure output directory exists
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        # Create filename with ValueSet- prefix and .jsonld extension
        filename = f"ValueSet-{valueset_id}.jsonld"
        filepath = os.path.join(output_dir, filename)
        
        # Save JSON-LD vocabulary
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(jsonld_vocab, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Saved JSON-LD vocabulary for ValueSet {valueset_id} to {filepath}")
        return filepath
        
    except Exception as e:
        logger.error(f"Error saving JSON-LD vocabulary for ValueSet {valueset_id}: {e}")
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
        # Ensure output directory exists
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        index_path = os.path.join(output_dir, "index.html")
        
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
            # Schema files are now in the same directory as index.html
            valueset_name = filename.replace('.schema.json', '')
            
            html_content += f'        <li><a href="{filename}" class="schema-link">{valueset_name}.schema.json</a></li>\n'
        
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
        
        valueset_id = extract_valueset_id_from_entry(entry)
        logger.info(f"Processing ValueSet: {valueset_id}")
        
        # Extract codes with displays from expansion
        codes_with_display = extract_valueset_codes_with_display(resource, valueset_id)
        
        if not codes_with_display:
            logger.warning(f"No codes found for ValueSet {valueset_id}, skipping schema generation")
            continue
        
        # Generate schema
        schema = generate_json_schema(resource, codes_with_display)
        
        # Generate display file
        display_file = generate_display_file(resource, codes_with_display)
        
        # System file no longer needed - system URIs are embedded in schema enum values
        # to match JSON-LD IRI format as requested
        # system_file = generate_system_file(resource, codes_with_display)
        
        # Generate JSON-LD vocabulary (skipped - now handled by separate script)
        # jsonld_vocab = generate_jsonld_vocabulary(resource, codes_with_display)
        
        # Save schema
        schema_path = save_schema(schema, output_dir, valueset_id)
        if schema_path:
            schema_files.append(schema_path)
        
        # Save display file
        display_path = save_display_file(display_file, output_dir, valueset_id)
        
        # System file no longer generated - system URIs are embedded in schema enum values
        # system_path = save_system_file(system_file, output_dir, valueset_id)
        
        # Save JSON-LD vocabulary (skipped - now handled by separate script)
        # jsonld_path = save_jsonld_vocabulary(jsonld_vocab, output_dir, valueset_id)
        
        # Count as successful if schema and display files are saved
        if schema_path and display_path:
            schemas_generated += 1
    

    
    logger.info(f"Generated {schemas_generated} ValueSet schemas")
    return schemas_generated


def main():
    """Main entry point for the script."""
    logger = setup_logging()
    
    # Parse command line arguments
    if len(sys.argv) < 2:
        # Default paths
        expansions_path = "output/expansions.json"
        output_dir = "output"  # Schemas will be saved directly to output/ directory
    elif len(sys.argv) == 2:
        expansions_path = sys.argv[1]
        output_dir = "output"  # Schemas will be saved directly to output/ directory
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