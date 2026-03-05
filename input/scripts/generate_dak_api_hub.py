#!/usr/bin/env python3
"""
DAK API Documentation Hub Generator

This script post-processes the IG-generated HTML files to inject DAK API content.
It works by:
1. Detecting existing JSON schemas (ValueSet and Logical Model schemas)
2. Creating minimal OpenAPI 3.0 wrappers for each JSON schema
3. Generating schema documentation content
4. Post-processing the dak-api.html file to replace content at the "DAK_API_CONTENT" comment marker
5. Creating individual schema documentation pages using dak-api.html as template

The script is designed to work with a single IG publisher run, post-processing
the generated HTML files instead of creating markdown that requires a second run.

Usage:
    python generate_dak_api_hub.py [output_dir] [openapi_dir]

Author: SMART Guidelines Team
"""

import json
import os
import sys
import logging
import re
import html as html_module
from typing import Dict, List, Optional, Any, Tuple, Union
from pathlib import Path
from urllib.parse import urlparse
from datetime import datetime

# Minimum code-block content size (in characters) to trigger dynamic source loading.
# Static pre-formatted blocks smaller than this threshold are left as-is to avoid
# replacing small illustrative code snippets with fetch-based loaders.
_MIN_SOURCE_SIZE_FOR_DYNAMIC_LOADING = 500

# Fallback FHIR R4 property name → documentation URL mapping used when the IG Publisher
# does not embed <a href> links in the JSON format pages.  Covers the most common
# top-level properties of StructureDefinition, ElementDefinition, and base Resource.
# The extracted link_map (when non-empty) takes precedence over these defaults.
_FHIR_R4_JSON_FALLBACK_LINKS: Dict[str, str] = {
    # ---- Resource base (all FHIR R4 resources) ----
    'resourceType':     'http://hl7.org/fhir/R4/resource.html#Resource.resourceType',
    'id':               'http://hl7.org/fhir/R4/datatypes.html#id',
    'meta':             'http://hl7.org/fhir/R4/resource.html#Resource.meta',
    'implicitRules':    'http://hl7.org/fhir/R4/resource.html#Resource.implicitRules',
    'language':         'http://hl7.org/fhir/R4/resource.html#Resource.language',
    # ---- DomainResource ----
    'text':             'http://hl7.org/fhir/R4/domainresource.html#DomainResource.text',
    'contained':        'http://hl7.org/fhir/R4/domainresource.html#DomainResource.contained',
    'extension':        'http://hl7.org/fhir/R4/domainresource.html#DomainResource.extension',
    'modifierExtension':'http://hl7.org/fhir/R4/domainresource.html#DomainResource.modifierExtension',
    # ---- StructureDefinition ----
    'url':              'http://hl7.org/fhir/R4/structuredefinition.html#StructureDefinition.url',
    'identifier':       'http://hl7.org/fhir/R4/structuredefinition.html#StructureDefinition.identifier',
    'version':          'http://hl7.org/fhir/R4/structuredefinition.html#StructureDefinition.version',
    'name':             'http://hl7.org/fhir/R4/structuredefinition.html#StructureDefinition.name',
    'title':            'http://hl7.org/fhir/R4/structuredefinition.html#StructureDefinition.title',
    'status':           'http://hl7.org/fhir/R4/structuredefinition.html#StructureDefinition.status',
    'experimental':     'http://hl7.org/fhir/R4/structuredefinition.html#StructureDefinition.experimental',
    'date':             'http://hl7.org/fhir/R4/structuredefinition.html#StructureDefinition.date',
    'publisher':        'http://hl7.org/fhir/R4/structuredefinition.html#StructureDefinition.publisher',
    'contact':          'http://hl7.org/fhir/R4/structuredefinition.html#StructureDefinition.contact',
    'description':      'http://hl7.org/fhir/R4/structuredefinition.html#StructureDefinition.description',
    'useContext':       'http://hl7.org/fhir/R4/structuredefinition.html#StructureDefinition.useContext',
    'jurisdiction':     'http://hl7.org/fhir/R4/structuredefinition.html#StructureDefinition.jurisdiction',
    'purpose':          'http://hl7.org/fhir/R4/structuredefinition.html#StructureDefinition.purpose',
    'copyright':        'http://hl7.org/fhir/R4/structuredefinition.html#StructureDefinition.copyright',
    'keyword':          'http://hl7.org/fhir/R4/structuredefinition.html#StructureDefinition.keyword',
    'fhirVersion':      'http://hl7.org/fhir/R4/structuredefinition.html#StructureDefinition.fhirVersion',
    'kind':             'http://hl7.org/fhir/R4/structuredefinition.html#StructureDefinition.kind',
    'abstract':         'http://hl7.org/fhir/R4/structuredefinition.html#StructureDefinition.abstract',
    'type':             'http://hl7.org/fhir/R4/structuredefinition.html#StructureDefinition.type',
    'baseDefinition':   'http://hl7.org/fhir/R4/structuredefinition.html#StructureDefinition.baseDefinition',
    'derivation':       'http://hl7.org/fhir/R4/structuredefinition.html#StructureDefinition.derivation',
    'snapshot':         'http://hl7.org/fhir/R4/structuredefinition.html#StructureDefinition.snapshot',
    'differential':     'http://hl7.org/fhir/R4/structuredefinition.html#StructureDefinition.differential',
    'element':          'http://hl7.org/fhir/R4/elementdefinition.html',
    # ---- ElementDefinition ----
    'path':             'http://hl7.org/fhir/R4/elementdefinition.html#ElementDefinition.path',
    'sliceName':        'http://hl7.org/fhir/R4/elementdefinition.html#ElementDefinition.sliceName',
    'min':              'http://hl7.org/fhir/R4/elementdefinition.html#ElementDefinition.min',
    'max':              'http://hl7.org/fhir/R4/elementdefinition.html#ElementDefinition.max',
    'base':             'http://hl7.org/fhir/R4/elementdefinition.html#ElementDefinition.base',
    'short':            'http://hl7.org/fhir/R4/elementdefinition.html#ElementDefinition.short',
    'definition':       'http://hl7.org/fhir/R4/elementdefinition.html#ElementDefinition.definition',
    'comment':          'http://hl7.org/fhir/R4/elementdefinition.html#ElementDefinition.comment',
    'requirements':     'http://hl7.org/fhir/R4/elementdefinition.html#ElementDefinition.requirements',
    'alias':            'http://hl7.org/fhir/R4/elementdefinition.html#ElementDefinition.alias',
    'mustSupport':      'http://hl7.org/fhir/R4/elementdefinition.html#ElementDefinition.mustSupport',
    'isModifier':       'http://hl7.org/fhir/R4/elementdefinition.html#ElementDefinition.isModifier',
    'isModifierReason': 'http://hl7.org/fhir/R4/elementdefinition.html#ElementDefinition.isModifierReason',
    'isSummary':        'http://hl7.org/fhir/R4/elementdefinition.html#ElementDefinition.isSummary',
    'binding':          'http://hl7.org/fhir/R4/elementdefinition.html#ElementDefinition.binding',
    'constraint':       'http://hl7.org/fhir/R4/elementdefinition.html#ElementDefinition.constraint',
    'mapping':          'http://hl7.org/fhir/R4/elementdefinition.html#ElementDefinition.mapping',
    # ---- Common FHIR datatypes ----
    'system':           'http://hl7.org/fhir/R4/datatypes.html#Coding.system',
    'code':             'http://hl7.org/fhir/R4/datatypes.html#code',
    'display':          'http://hl7.org/fhir/R4/datatypes.html#Coding.display',
    'value':            'http://hl7.org/fhir/R4/datatypes.html#id',
    'valueSet':         'http://hl7.org/fhir/R4/elementdefinition.html#ElementDefinition.binding.valueSet',
    'strength':         'http://hl7.org/fhir/R4/elementdefinition.html#ElementDefinition.binding.strength',
}


def setup_logging() -> logging.Logger:
    """Configure logging for the script."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger(__name__)


class QAReporter:
    """Handles QA reporting for post-processing steps and merging with FHIR IG publisher QA."""
    
    def __init__(self, phase: str = "postprocessing"):
        self.phase = phase
        self.timestamp = datetime.now().isoformat()
        self.report = {
            "phase": phase,
            "timestamp": self.timestamp,
            "status": "running",
            "summary": {},
            "details": {
                "successes": [],
                "warnings": [],
                "errors": [],
                "files_processed": [],
                "files_expected": [],
                "files_missing": []
            }
        }
        # Store existing IG publisher QA data if present
        self.ig_publisher_qa = None
    
    def load_existing_ig_qa(self, qa_file_path: str):
        """Load existing FHIR IG publisher QA file to preserve its structure."""
        try:
            if os.path.exists(qa_file_path):
                with open(qa_file_path, 'r', encoding='utf-8') as f:
                    self.ig_publisher_qa = json.load(f)
                print(f"Loaded existing IG publisher QA file: {qa_file_path}")
                return True
            else:
                print(f"No existing IG publisher QA file found at: {qa_file_path}")
                return False
        except Exception as e:
            print(f"Error loading existing IG publisher QA file: {e}")
            return False
    
    def add_success(self, message: str, details: Optional[Dict] = None):
        """Add a success entry to the QA report."""
        entry = {"message": message, "timestamp": datetime.now().isoformat()}
        if details:
            entry["details"] = details
        self.report["details"]["successes"].append(entry)
    
    def add_warning(self, message: str, details: Optional[Dict] = None):
        """Add a warning entry to the QA report."""
        entry = {"message": message, "timestamp": datetime.now().isoformat()}
        if details:
            entry["details"] = details
        self.report["details"]["warnings"].append(entry)
    
    def add_error(self, message: str, details: Optional[Dict] = None):
        """Add an error entry to the QA report."""
        entry = {"message": message, "timestamp": datetime.now().isoformat()}
        if details:
            entry["details"] = details
        self.report["details"]["errors"].append(entry)
    
    def add_file_processed(self, file_path: str, status: str = "success", details: Optional[Dict] = None):
        """Record a file that was processed."""
        entry = {
            "file": file_path,
            "status": status,
            "timestamp": datetime.now().isoformat()
        }
        if details:
            entry["details"] = details
        self.report["details"]["files_processed"].append(entry)
    
    def add_file_expected(self, file_path: str, found: bool = False):
        """Record a file that was expected."""
        self.report["details"]["files_expected"].append(file_path)
        if not found:
            self.report["details"]["files_missing"].append(file_path)
    
    def finalize_report(self, status: str = "completed"):
        """Finalize the QA report with summary statistics and merge with IG publisher QA if available."""
        self.report["status"] = status
        self.report["summary"] = {
            "total_successes": len(self.report["details"]["successes"]),
            "total_warnings": len(self.report["details"]["warnings"]),
            "total_errors": len(self.report["details"]["errors"]),
            "files_processed_count": len(self.report["details"]["files_processed"]),
            "files_expected_count": len(self.report["details"]["files_expected"]),
            "files_missing_count": len(self.report["details"]["files_missing"]),
            "completion_timestamp": datetime.now().isoformat()
        }
        
        # If we have IG publisher QA data, merge it with our report
        if self.ig_publisher_qa:
            return self.merge_with_ig_publisher_qa()
        
        return self.report
    
    def merge_with_ig_publisher_qa(self):
        """Merge our QA report with the existing FHIR IG publisher QA structure."""
        try:
            # Create a merged report that preserves the IG publisher structure
            merged_report = dict(self.ig_publisher_qa)
            
            # Add our component reports as a new section
            if "dak_api_processing" not in merged_report:
                merged_report["dak_api_processing"] = {}
            
            # Include any stored preprocessing reports
            preprocessing_reports = {}
            if hasattr(self, '_stored_preprocessing_reports'):
                for i, report in enumerate(self._stored_preprocessing_reports):
                    component_name = report.get("component", report.get("phase", f"component_{i}"))
                    preprocessing_reports[component_name] = report
            
            # Add our preprocessing and postprocessing reports
            merged_report["dak_api_processing"] = {
                "preprocessing_reports": preprocessing_reports,
                "postprocessing": self.report,
                "summary": {
                    "total_dak_api_successes": self.report["summary"]["total_successes"],
                    "total_dak_api_warnings": self.report["summary"]["total_warnings"], 
                    "total_dak_api_errors": self.report["summary"]["total_errors"],
                    "dak_api_completion_timestamp": self.report["summary"]["completion_timestamp"]
                }
            }
            
            return merged_report
            
        except Exception as e:
            print(f"Error merging with IG publisher QA: {e}")
            # Fall back to our report only
            return self.report
    
    def merge_preprocessing_report(self, preprocessing_report: Dict):
        """Merge a preprocessing report into this post-processing report."""
        if "details" in preprocessing_report:
            # Add preprocessing entries with a prefix
            component_name = preprocessing_report.get("component", preprocessing_report.get("phase", "Unknown"))
            
            for success in preprocessing_report["details"].get("successes", []):
                self.add_success(f"[{component_name}] {success['message']}", success.get("details"))
            
            for warning in preprocessing_report["details"].get("warnings", []):
                self.add_warning(f"[{component_name}] {warning['message']}", warning.get("details"))
            
            for error in preprocessing_report["details"].get("errors", []):
                self.add_error(f"[{component_name}] {error['message']}", error.get("details"))
            
            for file_proc in preprocessing_report["details"].get("files_processed", []):
                self.add_file_processed(f"[{component_name}] {file_proc['file']}", file_proc.get("status", "unknown"), file_proc.get("details"))
            
            # Merge schemas_generated if available (for component reports)
            for schema in preprocessing_report["details"].get("schemas_generated", []):
                schema_with_component = dict(schema)
                schema_with_component["component"] = component_name
                self.add_success(f"[{component_name}] Generated schema", schema_with_component)
        
        # Store preprocessing report in the final merged structure
        if self.ig_publisher_qa and "dak_api_processing" in self.ig_publisher_qa:
            self.ig_publisher_qa["dak_api_processing"]["preprocessing"] = preprocessing_report
        else:
            # Store for later merging
            if not hasattr(self, '_stored_preprocessing_reports'):
                self._stored_preprocessing_reports = []
            self._stored_preprocessing_reports.append(preprocessing_report)
    
    def save_to_file(self, output_path: str):
        """Save QA report to a JSON file."""
        try:
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(self.report, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error saving QA report to {output_path}: {e}")
            return False


class SchemaDetector:
    """Detects and categorizes schema files in the output directory."""
    
    def __init__(self, logger: logging.Logger):
        self.logger = logger
    
    def find_schema_files(self, output_dir: str) -> Dict[str, List[str]]:
        """
        Find all schema files in the output directory.
        
        Returns:
            Dictionary with categories 'valueset' and 'logical_model' 
            containing lists of schema file paths
        """
        schemas = {
            'valueset': [],
            'logical_model': [],
            'other': []
        }
        
        if not os.path.exists(output_dir):
            self.logger.warning(f"Output directory does not exist: {output_dir}")
            return schemas
        
        self.logger.info(f"Scanning directory for schema files: {output_dir}")
        all_files = os.listdir(output_dir)
        schema_count = 0
        
        for file in all_files:
            if file.endswith('.schema.json'):
                schema_count += 1
                file_path = os.path.join(output_dir, file)
                self.logger.info(f"Found schema file: {file}")
                
                if file.startswith('ValueSet-'):
                    schemas['valueset'].append(file_path)
                    self.logger.info(f"  -> Categorized as ValueSet schema")
                elif file in ['ValueSets.schema.json', 'LogicalModels.schema.json']:
                    # These are enumeration schemas, categorize appropriately
                    if file == 'ValueSets.schema.json':
                        schemas['valueset'].append(file_path) 
                        self.logger.info(f"  -> Categorized as ValueSet enumeration schema")
                    else:
                        schemas['logical_model'].append(file_path)
                        self.logger.info(f"  -> Categorized as Logical Model enumeration schema")
                elif not file.startswith('ValueSet-') and not file.startswith('CodeSystem-'):
                    # Assume logical model if not ValueSet or CodeSystem
                    schemas['logical_model'].append(file_path)
                    self.logger.info(f"  -> Categorized as Logical Model schema")
                else:
                    schemas['other'].append(file_path)
                    self.logger.info(f"  -> Categorized as other schema")
        
        self.logger.info(f"Schema detection summary:")
        self.logger.info(f"  Total schema files found: {schema_count}")
        self.logger.info(f"  ValueSet schemas: {len(schemas['valueset'])}")
        self.logger.info(f"  Logical Model schemas: {len(schemas['logical_model'])}")
        self.logger.info(f"  Other schemas: {len(schemas['other'])}")
        
        if schema_count == 0:
            self.logger.warning(f"No .schema.json files found in {output_dir}")
            self.logger.info(f"Directory contents: {', '.join(all_files)}")
        
        return schemas
    
    def find_jsonld_files(self, output_dir: str) -> List[str]:
        """
        Find all JSON-LD vocabulary files in the output directory.
        
        Returns:
            List of JSON-LD file paths
        """
        jsonld_files = []
        
        if not os.path.exists(output_dir):
            self.logger.warning(f"Output directory does not exist: {output_dir}")
            return jsonld_files
        
        self.logger.info(f"Scanning directory for JSON-LD files: {output_dir}")
        all_files = os.listdir(output_dir)
        jsonld_count = 0
        
        for file in all_files:
            if file.endswith('.jsonld'):
                jsonld_count += 1
                file_path = os.path.join(output_dir, file)
                self.logger.info(f"Found JSON-LD file: {file}")
                
                if file.startswith('ValueSet-'):
                    jsonld_files.append(file_path)
                    self.logger.info(f"  -> Added ValueSet JSON-LD vocabulary")
                else:
                    self.logger.info(f"  -> Skipped non-ValueSet JSON-LD file")
        
        self.logger.info(f"JSON-LD detection summary:")
        self.logger.info(f"  Total JSON-LD files found: {jsonld_count}")
        self.logger.info(f"  ValueSet JSON-LD vocabularies: {len(jsonld_files)}")
        
        if jsonld_count == 0:
            self.logger.info(f"No .jsonld files found in {output_dir}")
        
        return jsonld_files


class OpenAPIDetector:
    """Detects existing OpenAPI/Swagger files."""
    
    def __init__(self, logger: logging.Logger):
        self.logger = logger
    
    def find_openapi_files(self, openapi_dir: str) -> List[str]:
        """Find OpenAPI/Swagger files in the given directory, including generated .openapi.json files."""
        openapi_files = []
        
        if not os.path.exists(openapi_dir):
            self.logger.info(f"OpenAPI directory does not exist: {openapi_dir}")
            return openapi_files
        
        self.logger.info(f"Scanning for OpenAPI files in: {openapi_dir}")
        
        for root, dirs, files in os.walk(openapi_dir):
            for file in files:
                # Include OpenAPI/Swagger files with more lenient matching for existing files
                # Exclude index.html as it's handled separately for content extraction
                if (file.endswith(('.json', '.yaml', '.yml')) and 
                    file.lower() != 'index.html' and
                    ('openapi' in file.lower() or 'swagger' in file.lower() or 
                     'api' in file.lower() or  # More lenient for existing API files
                     file.endswith('.openapi.json') or file.endswith('.openapi.yaml'))):
                    full_path = os.path.join(root, file)
                    openapi_files.append(full_path)
                    self.logger.info(f"Found OpenAPI file: {file}")
        
        self.logger.info(f"Found {len(openapi_files)} OpenAPI/Swagger files total")
        return openapi_files
    
    def find_existing_html_content(self, openapi_dir: str) -> Optional[str]:
        """Find and extract content from existing index.html in OpenAPI directory."""
        index_html_path = os.path.join(openapi_dir, "index.html")
        
        if not os.path.exists(index_html_path):
            self.logger.info(f"No existing index.html found in: {openapi_dir}")
            return None
        
        try:
            from bs4 import BeautifulSoup
            
            self.logger.info(f"Found existing OpenAPI HTML content at: {index_html_path}")
            with open(index_html_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            # Parse the HTML using BeautifulSoup
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Extract the body content
            body = soup.find('body')
            if not body:
                self.logger.warning("No <body> tag found in existing index.html")
                return None
            
            # Remove script tags and other non-content elements
            for script in body.find_all(['script', 'noscript']):
                script.decompose()
            
            # Look for the main content container
            # Try common container patterns
            content_container = (
                body.find('div', class_=lambda x: x and 'container' in x.lower()) or
                body.find('div', class_=lambda x: x and 'content' in x.lower()) or
                body.find('main') or
                body.find('div', id=lambda x: x and 'content' in x.lower()) or
                body
            )
            
            if content_container:
                # Get the inner HTML content
                extracted_content = str(content_container)
                
                # If we got the whole body, remove the body tags
                if content_container == body:
                    # Remove body tag but keep its content
                    extracted_content = extracted_content.replace('<body>', '').replace('</body>', '')
                    # Clean up any attributes from body tag
                    if extracted_content.startswith('<body '):
                        end_tag = extracted_content.find('>')
                        if end_tag != -1:
                            extracted_content = extracted_content[end_tag + 1:]
                
                self.logger.info(f"Extracted {len(extracted_content)} characters of HTML content from existing index.html")
                return extracted_content.strip()
            else:
                self.logger.warning("Could not find suitable content container in existing index.html")
                return None
                
        except ImportError:
            self.logger.error("BeautifulSoup not available. Please install beautifulsoup4: pip install beautifulsoup4")
            return None
        except Exception as e:
            self.logger.error(f"Error parsing existing HTML content: {e}")
            return None



class OpenAPIWrapper:
    """Creates OpenAPI 3.1 wrappers for JSON schemas."""

    # Filename of the generated base schema (produced by
    # generate_logical_model_schemas.py from the FHIRSchemaBase FSH Logical
    # Model).  All generated logical model schemas reference this file via
    # ``allOf`` to inherit the shared FHIR metadata properties.
    FHIR_SCHEMA_BASE_FILENAME = "StructureDefinition-FHIRSchemaBase.schema.json"

    def __init__(self, logger: logging.Logger, canonical_base: str = "http://smart.who.int/base"):
        self.logger = logger
        self.canonical_base = canonical_base

    def sanitize_schema_for_openapi(self, schema: Any) -> Any:
        """
        Adapt a JSON Schema document for use inside an OpenAPI 3.1
        ``components/schemas`` entry.

        OpenAPI 3.1 is fully aligned with JSON Schema 2020-12, so standard
        keywords such as ``$schema``, ``$id``, and ``const`` are kept as-is.

        Schemas generated by ``generate_logical_model_schemas.py`` already
        contain an ``allOf`` composition that references the generated
        ``StructureDefinition-FHIRSchemaBase.schema.json`` file (produced from
        the ``FHIRSchemaBase`` FSH Logical Model), so this method simply
        returns the schema unchanged.

        Args:
            schema: A JSON-Schema-compatible dict (or any nested value).

        Returns:
            The same dict (or value) unmodified — valid as-is inside an
            OpenAPI 3.1 ``components/schemas`` entry.
        """
        return schema

    def create_wrapper_for_schema(self, schema_path: str, schema_type: str, output_dir: str) -> Optional[str]:
        """
        Create an OpenAPI 3.1 wrapper for a JSON schema.
        
        Args:
            schema_path: Path to the JSON schema file
            schema_type: Type of schema ('valueset' or 'logical_model')
            output_dir: Directory to save the OpenAPI wrapper
            
        Returns:
            Path to the generated OpenAPI wrapper file, or None if failed
        """
        try:
            # Load the schema
            with open(schema_path, 'r', encoding='utf-8') as f:
                schema = json.load(f)
            
            schema_filename = os.path.basename(schema_path)
            schema_name = schema_filename.replace('.schema.json', '')
            
            # Determine the endpoint path and description
            if schema_type == 'valueset':
                endpoint_path = f"/{schema_filename}"
                summary = f"JSON Schema definition for the enumeration {schema_name}"
                description = f"This endpoint serves the JSON Schema definition for the enumeration {schema_name}."
                media_type = "application/schema+json"
            else:  # logical_model
                endpoint_path = f"/{schema_filename}"
                summary = f"JSON Schema definition for the Logical Model {schema_name}"
                description = f"This endpoint serves the JSON Schema definition for the Logical Model {schema_name}."
                media_type = "application/schema+json"
            
            # Create OpenAPI wrapper
            openapi_spec = {
                "openapi": "3.1.0",
                "info": {
                    "title": f"{schema.get('title', schema_name)} API",
                    "description": schema.get('description', f"API for {schema_name} schema"),
                    "version": "1.0.0"
                },
                "paths": {
                    endpoint_path: {
                        "get": {
                            "summary": summary,
                            "description": description,
                            "responses": {
                                "200": {
                                    "description": f"The JSON Schema for {schema_name}",
                                    "content": {
                                        media_type: {
                                            "schema": {
                                                "$ref": f"./{schema_filename}"
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "components": {
                    "schemas": {
                        schema_name: self.sanitize_schema_for_openapi(schema),
                    }
                }
            }
            
            # Save OpenAPI wrapper
            wrapper_filename = f"{schema_name}.openapi.json"
            wrapper_path = os.path.join(output_dir, wrapper_filename)
            
            with open(wrapper_path, 'w', encoding='utf-8') as f:
                json.dump(openapi_spec, f, indent=2, ensure_ascii=False)
            
            self.logger.info(f"Created OpenAPI wrapper: {wrapper_path}")
            return wrapper_path
            
        except Exception as e:
            self.logger.error(f"Error creating OpenAPI wrapper for {schema_path}: {e}")
            return None
    
    def create_enumeration_wrapper(self, enum_schema_path: str, schema_type: str, output_dir: str) -> Optional[str]:
        """
        Create an OpenAPI 3.1 wrapper for an enumeration schema.
        
        Args:
            enum_schema_path: Path to the enumeration schema file
            schema_type: Type of schema ('valueset' or 'logical_model')
            output_dir: Directory to save the OpenAPI wrapper
            
        Returns:
            Path to the generated OpenAPI wrapper file, or None if failed
        """
        try:
            # Load the enumeration schema
            with open(enum_schema_path, 'r', encoding='utf-8') as f:
                enum_schema = json.load(f)
            
            enum_filename = os.path.basename(enum_schema_path)
            
            # Determine the endpoint details
            if schema_type == 'valueset':
                endpoint_path = "/ValueSets.schema.json"
                api_title = "ValueSets Enumeration API"
                api_description = "API endpoint providing an enumeration of all available ValueSet schemas"
                summary = "Get enumeration of all ValueSet schemas"
                description = "Returns a list of all available ValueSet schemas with metadata"
            else:  # logical_model
                endpoint_path = "/LogicalModels.schema.json"
                api_title = "LogicalModels Enumeration API"
                api_description = "API endpoint providing an enumeration of all available Logical Model schemas"
                summary = "Get enumeration of all Logical Model schemas"
                description = "Returns a list of all available Logical Model schemas with metadata"
            
            # Create OpenAPI wrapper for the enumeration
            openapi_spec = {
                "openapi": "3.1.0",
                "info": {
                    "title": api_title,
                    "description": api_description,
                    "version": "1.0.0"
                },
                "paths": {
                    endpoint_path: {
                        "get": {
                            "summary": summary,
                            "description": description,
                            "responses": {
                                "200": {
                                    "description": f"Successfully retrieved {schema_type} enumeration",
                                    "content": {
                                        "application/json": {
                                            "schema": {
                                                "$ref": f"#/components/schemas/EnumerationResponse"
                                            },
                                            "example": enum_schema.get('example', {})
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "components": {
                    "schemas": {
                        "EnumerationResponse": self.sanitize_schema_for_openapi(enum_schema),
                    }
                }
            }
            
            # Save OpenAPI wrapper
            if schema_type == 'valueset':
                wrapper_filename = "ValueSets-enumeration.openapi.json"
            else:
                wrapper_filename = "LogicalModels-enumeration.openapi.json"
                
            wrapper_path = os.path.join(output_dir, wrapper_filename)
            
            with open(wrapper_path, 'w', encoding='utf-8') as f:
                json.dump(openapi_spec, f, indent=2, ensure_ascii=False)
            
            self.logger.info(f"Created enumeration OpenAPI wrapper: {wrapper_path}")
            return wrapper_path
            
        except Exception as e:
            self.logger.error(f"Error creating enumeration OpenAPI wrapper for {enum_schema_path}: {e}")
            return None


class HTMLProcessor:
    """Post-processes HTML files to inject DAK API content."""
    
    def __init__(self, logger: logging.Logger, output_dir: str):
        self.logger = logger
        self.output_dir = output_dir
    
    def create_html_template_from_existing(self, template_html_path: str, title: str, content: str) -> str:
        """
        Create a new HTML file using an existing file as template.
        
        Args:
            template_html_path: Path to the template HTML file (e.g., dak-api.html)
            title: Title for the new page
            content: HTML content to inject at the DAK_API_CONTENT marker
            
        Returns:
            The new HTML content as a string
        """
        try:
            with open(template_html_path, 'r', encoding='utf-8') as f:
                template_html = f.read()
            
            # Update the title
            import re
            title_pattern = r'<title>([^<]*)</title>'
            match = re.search(title_pattern, template_html)
            if match:
                current_title = match.group(1)
                # Preserve any suffix from the original title
                if ' - ' in current_title:
                    suffix = ' - ' + current_title.split(' - ', 1)[1]
                else:
                    suffix = ''
                new_title = title + suffix
                template_html = re.sub(title_pattern, f'<title>{new_title}</title>', template_html)
            
            # Replace the DAK_API_CONTENT comment marker with actual content
            comment_marker = '<!-- DAK_API_CONTENT -->'
            if comment_marker in template_html:
                template_html = template_html.replace(comment_marker, content)
            else:
                self.logger.warning(f"DAK_API_CONTENT marker not found in template")
            
            return template_html
            
        except Exception as e:
            self.logger.error(f"Error creating HTML template: {e}")
            return ""
    
    def inject_content_at_comment_marker(self, html_file_path: str, content: str) -> bool:
        """
        Inject content into an HTML file at the DAK_API_CONTENT comment marker.
        
        Args:
            html_file_path: Path to the HTML file to modify
            content: HTML content to inject
            
        Returns:
            True if successful, False otherwise
        """
        try:
            self.logger.info(f"🔍 Starting content injection into: {html_file_path}")
            self.logger.info(f"📏 Content to inject length: {len(content)} characters")
            
            if not os.path.exists(html_file_path):
                self.logger.error(f"❌ HTML file does not exist: {html_file_path}")
                return False
            
            with open(html_file_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            self.logger.info(f"📖 Read HTML file, original length: {len(html_content)} characters")
            
            # Look for the DAK_API_CONTENT comment marker
            comment_marker = '<!-- DAK_API_CONTENT -->'
            hub_start_marker = '<!-- DAK_API_HUB_START -->'
            hub_end_marker = '<!-- DAK_API_HUB_END -->'
            
            if comment_marker in html_content:
                self.logger.info(f"✅ Found DAK_API_CONTENT comment marker")
                # Replace the comment marker with the actual content
                new_html_content = html_content.replace(comment_marker, content)
                replaced_existing = False
            elif hub_start_marker in html_content and hub_end_marker in html_content:
                self.logger.info(f"✅ Found DAK_API_HUB start/end markers — replacing previously injected content")
                start_idx = html_content.index(hub_start_marker)
                end_idx = html_content.index(hub_end_marker) + len(hub_end_marker)
                if start_idx >= end_idx - len(hub_end_marker):
                    self.logger.error(f"❌ DAK_API_HUB markers are in wrong order or overlapping in {html_file_path}")
                    return False
                new_html_content = html_content[:start_idx] + content + html_content[end_idx:]
                replaced_existing = True
            elif '<div class="dak-api-hub">' in html_content:
                # Legacy fallback: content was injected by an old script version that didn't add markers.
                # Replace from the hub div up to (and including) the standard hub footer paragraph.
                self.logger.info(f"✅ Found legacy dak-api-hub div — replacing old hub content without markers")
                hub_div_marker = '<div class="dak-api-hub">'
                start_idx = html_content.index(hub_div_marker)
                legacy_end_text = '<p><em>This documentation hub is automatically generated from the available schema and API definitions.</em></p>'
                end_marker_pos = html_content.find(legacy_end_text, start_idx)
                if end_marker_pos != -1:
                    end_idx = end_marker_pos + len(legacy_end_text)
                else:
                    # Backstop: replace up to the inner-wrapper comment that follows the content section
                    inner_wrapper_pos = html_content.find('<!-- /inner-wrapper -->', start_idx)
                    if inner_wrapper_pos == -1:
                        self.logger.error(f"❌ Cannot find end of legacy dak-api-hub content in {html_file_path}")
                        return False
                    end_idx = inner_wrapper_pos
                new_html_content = html_content[:start_idx] + content + html_content[end_idx:]
                replaced_existing = True
            else:
                self.logger.error(f"❌ DAK_API_CONTENT comment marker not found in {html_file_path}")
                self.logger.info("Available content sample for debugging:")
                # Show a sample to help debug
                sample_content = html_content[:1000] if len(html_content) > 1000 else html_content
                self.logger.info(f"Sample content: {sample_content}")
                return False
            
            self.logger.info(f"📏 Content replacement: original={len(html_content)}, new={len(new_html_content)}")
            
            # Write the modified HTML back to the file
            with open(html_file_path, 'w', encoding='utf-8') as f:
                f.write(new_html_content)
            
            size_increase = len(new_html_content) - len(html_content)
            self.logger.info(f"💾 Successfully wrote modified HTML back to {html_file_path}")
            self.logger.info(f"📏 Final HTML file size: {len(new_html_content)} characters (increased by {size_increase})")
            
            if size_increase > 100:  # If we added substantial content
                self.logger.info(f"✅ Content injection appears successful (substantial size increase)")
                return True
            elif replaced_existing:
                self.logger.info(f"✅ Content replacement successful (replaced existing hub content, size change: {size_increase})")
                return True
            else:
                self.logger.warning(f"⚠️  Content injection may have failed (minimal size increase: {size_increase})")
                return False
            
        except Exception as e:
            self.logger.error(f"❌ Error injecting content into {html_file_path}: {e}")
            import traceback
            self.logger.error(f"🔍 Traceback: {traceback.format_exc()}")
            return False
class SchemaDocumentationRenderer:
    """Generates HTML documentation content for schemas."""
    
    def __init__(self, logger: logging.Logger):
        self.logger = logger
    
    def get_codesystem_anchors(self, codesystem_url: str, output_dir: str) -> Dict[str, str]:
        """
        Attempt to find anchor mappings for codes in a CodeSystem HTML file.
        
        Args:
            codesystem_url: The canonical URL of the CodeSystem
            output_dir: Directory where HTML files are located
            
        Returns:
            Dictionary mapping codes to their anchor names
        """
        anchor_map = {}
        
        try:
            # Extract CodeSystem ID from URL
            if '/CodeSystem/' in codesystem_url:
                codesystem_id = codesystem_url.split('/CodeSystem/')[-1]
                html_filename = f"CodeSystem-{codesystem_id}.html"
                html_path = os.path.join(output_dir, html_filename)
                
                if os.path.exists(html_path):
                    with open(html_path, 'r', encoding='utf-8') as f:
                        html_content = f.read()
                    
                    # Look for anchor patterns in code definition tables
                    # Pattern 1: id="CodeSystem-ID-code" (simple case)
                    # Pattern 2: id="ID-code" (common IG Publisher pattern)
                    # Pattern 3: code-specific patterns based on the actual HTML structure
                    import re
                    
                    # Try different anchor patterns that might be used by IG Publisher
                    patterns = [
                        rf'id="({codesystem_id}-[^"]+)"',  # CodeSystem-ID-code
                        rf'id="([^"]*-[0-9.]+[^"]*)"',     # Any ID with numeric codes
                        rf'<tr[^>]*id="([^"]*{codesystem_id}[^"]*)"',  # Table rows with CodeSystem ID
                        rf'<a[^>]*name="([^"]*)"[^>]*>.*?{re.escape(codesystem_id)}'  # Named anchors
                    ]
                    
                    for pattern in patterns:
                        matches = re.findall(pattern, html_content, re.IGNORECASE)
                        for match in matches:
                            # Extract potential code from the match
                            if codesystem_id in match:
                                # Split by the codesystem ID and take the part after it
                                parts = match.split(codesystem_id, 1)
                                if len(parts) > 1 and parts[1]:
                                    code_part = parts[1].lstrip('-_.')
                                    if code_part:
                                        anchor_map[code_part] = match
                            else:
                                # For patterns that don't include the codesystem ID
                                # Try to extract numeric codes
                                code_match = re.search(r'[0-9]+(?:\.[0-9]+)*', match)
                                if code_match:
                                    code = code_match.group()
                                    anchor_map[code] = match
                    
                    # If we still don't have anchors, try a more generic approach
                    if not anchor_map:
                        # Look for any table cells or elements that might contain codes
                        td_pattern = r'<td[^>]*>([0-9]+(?:\.[0-9]+)*)</td>'
                        code_matches = re.findall(td_pattern, html_content)
                        for code in code_matches:
                            # Create a best-guess anchor
                            anchor_map[code] = f"{codesystem_id}-{code}"
                
                self.logger.info(f"Found {len(anchor_map)} anchor mappings for CodeSystem {codesystem_id}")
                if anchor_map:
                    # Log a few examples for debugging
                    sample_mappings = list(anchor_map.items())[:3]
                    self.logger.info(f"Sample mappings: {sample_mappings}")
                    
        except Exception as e:
            self.logger.warning(f"Could not load CodeSystem anchors for {codesystem_url}: {e}")
        
        return anchor_map
    
    def generate_schema_documentation_html(self, schema_path: str, schema_type: str, output_dir: str) -> str:
        """
        Generate HTML documentation content for a schema.
        
        Args:
            schema_path: Path to the schema file
            schema_type: Type of schema ('valueset' or 'logical_model')
            output_dir: Output directory for reference files
            
        Returns:
            HTML content as a string
        """
        try:
            schema_filename = os.path.basename(schema_path)
            spec_name = schema_filename.replace('.schema.json', '')
            
            # Load the schema
            with open(schema_path, 'r', encoding='utf-8') as f:
                schema_data = json.load(f)
            
            title = schema_data.get('title', f"{spec_name} Schema Documentation")
            
            # Generate HTML content
            html_content = f"""
<div class="schema-documentation">
    <h2>{title}</h2>
    
    <div class="schema-info">
        <p><strong>Schema File:</strong> {schema_filename}</p>
        <p><strong>Description:</strong> {schema_data.get('description', 'No description available')}</p>
        <p><strong>Type:</strong> {schema_data.get('type', 'unknown')}</p>
    </div>
"""
            
            # Add schema ID as link if available
            schema_id = schema_data.get('$id', '')
            if schema_id:
                # Determine the correct FHIR page link based on schema type
                if schema_filename == 'ValueSets.schema.json':
                    fhir_url = "artifacts.html#terminology-value-sets"
                elif schema_filename == 'LogicalModels.schema.json':
                    fhir_url = "artifacts.html#structures-logical-models"
                else:
                    # Individual schemas link to their specific HTML files
                    fhir_url = schema_filename.replace('.schema.json', '.html')
                
                html_content += f"""
    <div class="schema-links">
        <p><strong>Schema ID:</strong> <a href="{schema_id}">{schema_id}</a></p>
    </div>
"""
            
            # Handle enum values for ValueSets
            if 'enum' in schema_data:
                # Sort enum values alphabetically and truncate after 40 entries
                enum_values = sorted(schema_data['enum'])
                displayed_values = enum_values[:40]
                truncated = len(enum_values) > 40
                
                # Check if we can link to CodeSystem definitions
                codesystem_anchors = {}
                if schema_type == 'valueset' and schema_id:
                    # Try to load system mapping to find CodeSystem
                    try:
                        if '/' in schema_id:
                            base_url = '/'.join(schema_id.split('/')[:-1])
                            system_filename = f"{spec_name}.system.json"
                            system_path = os.path.join(output_dir, system_filename)
                            
                            if os.path.exists(system_path):
                                with open(system_path, 'r', encoding='utf-8') as f:
                                    system_data = json.load(f)
                                
                                # Get system URIs for codes
                                fhir_systems = system_data.get('fhir:systems', {})
                                if fhir_systems:
                                    # Check if any system is from the same IG
                                    for code, system_uri in fhir_systems.items():
                                        if system_uri and base_url in system_uri:
                                            # This is a local CodeSystem, try to get anchors
                                            codesystem_anchors = self.get_codesystem_anchors(system_uri, output_dir)
                                            break
                    except Exception as e:
                        self.logger.warning(f"Could not load system mappings for {spec_name}: {e}")
                
                html_content += """
    <div class="allowed-values">
        <h3>Allowed Values</h3>
        <div class="enum-values">
"""
                for enum_value in displayed_values:
                    if enum_value in codesystem_anchors:
                        # Create link to CodeSystem anchor
                        anchor = codesystem_anchors[enum_value]
                        codesystem_id = anchor.split('-')[0]
                        link_url = f"CodeSystem-{codesystem_id}.html#{anchor}"
                        html_content += f'            <span class="enum-value"><a href="{link_url}" title="View definition in CodeSystem">{enum_value}</a></span>\n'
                    else:
                        html_content += f'            <span class="enum-value">{enum_value}</span>\n'
                
                if truncated:
                    remaining_count = len(enum_values) - 40
                    html_content += f'            <div class="enum-truncated">... and {remaining_count} more values</div>\n'
                
                html_content += """        </div>
    </div>
"""
            
            # Handle object properties for Logical Models
            if 'properties' in schema_data:
                html_content += """
    <div class="schema-properties">
        <h3>Properties</h3>
        <ul>
"""
                for prop_name, prop_def in schema_data['properties'].items():
                    prop_type = prop_def.get('type', 'unknown')
                    html_content += f'            <li><strong>{prop_name}</strong> ({prop_type}): {prop_def.get("description", "No description")}</li>\n'
                
                html_content += """        </ul>
"""
                
                # Show required fields
                required = schema_data.get('required', [])
                if required:
                    html_content += f"""
        <p><strong>Required fields:</strong> {', '.join(required)}</p>
"""
                
                html_content += """    </div>
"""
            
            # Link to the schema file rather than embedding pre-formatted JSON.
            # The JSON Schema tab (for logical model pages) loads the file lazily;
            # here we provide a direct download link for other page types.
            html_content += f"""
    <div class="schema-json">
        <p><a href="{schema_filename}" target="_blank" class="schema-link">&#128196; Download full JSON schema ({schema_filename})</a></p>
    </div>
</div>

<style>
/* Schema documentation styling that integrates with IG theme */
.schema-documentation {{
    margin: 1rem 0;
}}

.schema-info, .schema-links, .allowed-values, .schema-properties, .schema-json {{
    margin: 1.5rem 0;
}}

.enum-values {{
    background-color: #e7f3ff;
    border: 1px solid #b8daff;
    border-radius: 4px;
    padding: 1rem;
    margin: 1rem 0;
}}

.enum-value {{
    display: inline-block;
    background-color: #00477d;
    color: white;
    padding: 0.2rem 0.5rem;
    border-radius: 3px;
    margin: 0.2rem;
    font-size: 0.9rem;
    text-decoration: none;
}}

.enum-value a {{
    color: white;
    text-decoration: none;
}}

.enum-value:hover, .enum-value a:hover {{
    background-color: #0070A1;
    color: white;
    text-decoration: none;
}}

.enum-truncated {{
    margin-top: 0.5rem;
    font-style: italic;
    color: #6c757d;
}}

.schema-link {{
    display: inline-block;
    background-color: #17a2b8;
    color: white;
    padding: 0.25rem 0.5rem;
    border-radius: 3px;
    text-decoration: none;
    font-size: 0.8rem;
    font-weight: 500;
    transition: background-color 0.2s ease;
}}

.schema-link:hover {{
    background-color: #138496;
    color: white;
    text-decoration: none;
}}
</style>

<hr>

<p><em>This documentation is automatically generated from the schema definition.</em></p>
"""
            
            return html_content
            
        except Exception as e:
            self.logger.error(f"Error generating schema documentation for {schema_path}: {e}")
            return ""
    
    def _find_closing_div(self, html: str, start: int) -> int:
        """
        Find the position after the closing </div> of a div starting at `start`.

        Counts div nesting depth to handle nested elements correctly.

        Args:
            html: HTML string to search
            start: Position of the opening <div tag

        Returns:
            Position after the matching </div>, or -1 if not found
        """
        depth = 0
        i = start
        n = len(html)
        while i < n:
            j = html.find('<', i)
            if j == -1:
                break
            # Opening div
            if j + 4 <= n and html[j:j+4].lower() == '<div' and (j + 4 >= n or html[j+4] in ' \t\n\r>/'):
                end_tag = html.find('>', j)
                if end_tag == -1:
                    break
                if end_tag > 0 and html[end_tag - 1] == '/':
                    # Self-closing <div/> – no depth change
                    i = end_tag + 1
                else:
                    depth += 1
                    i = end_tag + 1
            # Closing div
            elif html[j:j+6].lower() == '</div>':
                depth -= 1
                if depth == 0:
                    return j + 6
                i = j + 6
            else:
                i = j + 1
        return -1

    def _generate_schema_tab_pane_html(self, schema_filename: str, tab_id: str,
                                        language: str = 'json') -> str:
        """
        Generate the HTML for a content tab pane that lazily loads a source file
        via JavaScript and applies client-side syntax highlighting.

        Cross-domain / CORS note
        ------------------------
        The ``fetch()`` call uses a *relative* URL (same directory as the HTML
        page), so it is always same-origin regardless of whether the site is
        deployed to github.io, smart.who.int, or any other domain.  There is no
        cross-origin request and therefore no CORS error is possible.

        Syntax-highlighter strategy
        ---------------------------
        Syntax highlighting is provided exclusively by **Prism.js**, which is
        already bundled by the FHIR IG Publisher's standard template
        (hl7.fhir.template / who.template.root).  No CDN request is made, so
        there are no Content Security Policy (CSP) concerns regardless of the
        deployment domain.

        ``Prism.highlightElement(el)`` is called when ``window.Prism`` is
        available and the requested language grammar is registered.  Languages
        not registered in Prism (``Prism.languages[language]`` is falsy, e.g.
        ``cql``) fall through to plain formatted text — no silent failure.

        Other options considered and rejected:

        - **highlight.js** — requires an external CDN request; may be blocked
          by strict CSP on domains such as smart.who.int.
        - **CodeMirror** — full interactive editor, 6× heavier; designed for
          editing not read-only display.

        If Prism is unavailable the JSON is still pretty-printed via
        ``JSON.stringify(d, null, 2)`` — fully readable, just without colours.

        Args:
            schema_filename: Relative URL of the source file to load.
                             Must be same-origin (relative path).
            tab_id: Unique ID for the tab / pane element
            language: Prism language identifier (default: 'json')

        Returns:
            HTML string for the tab pane
        """
        return (
            # ── Tab pane ────────────────────────────────────────────────────────
            f'<div role="tabpanel" class="tab-pane" id="{tab_id}">\n'
            f'<div class="schema-tab-content" style="padding:1rem;">\n'
            f'<h3>JSON Schema</h3>\n'
            f'<p><a href="{schema_filename}" target="_blank" '
            f'class="btn btn-sm btn-outline-secondary">'
            f'&#128196; Download {schema_filename}</a></p>\n'
            f'<pre style="margin:0;padding:0;background:transparent;border:none;">'
            f'<code id="{tab_id}-display" class="language-{language}" '
            f'style="border-radius:4px;max-height:600px;overflow-y:auto;'
            f'font-size:0.85em;display:block;">Loading schema&#8230;</code>'
            f'</pre>\n'
            f'</div>\n'
            # ── Load + highlight on tab activation ───────────────────────────────
            # fetch() uses a relative URL → always same-origin → no CORS issue.
            # Syntax highlighting uses Prism.js only (no CDN dependency).
            # Unregistered languages fall through to plain text gracefully.
            f'<script>\n'
            f'(function(){{\n'
            f'  function loadSchema(){{\n'
            f'    var el=document.getElementById("{tab_id}-display");\n'
            f'    if(!el||el.dataset.loaded)return;\n'
            f'    el.dataset.loaded="1";\n'
            f'    fetch("{schema_filename}")\n'
            f'      .then(function(r){{return r.json();}})\n'
            f'      .then(function(d){{\n'
            f'        var txt=JSON.stringify(d,null,2);\n'
            f'        el.textContent=txt;\n'
            f'        if(window.Prism&&Prism.languages["{language}"]){{\n'
            f'          setTimeout(function(){{el.innerHTML=Prism.highlight(txt,Prism.languages["{language}"],"{language}");}},0);\n'
            f'        }}\n'
            f'      }})\n'
            f'      .catch(function(e){{\n'
            f'        el.textContent="Error loading schema: "+e.message;\n'
            f'      }});\n'
            f'  }}\n'
            f'  var link=document.getElementById("{tab_id}-head");\n'
            f'  if(link){{\n'
            f'    link.addEventListener("shown.bs.tab",loadSchema);\n'
            f'    if(link.classList.contains("active")){{loadSchema();}}\n'
            f'  }}else{{\n'
            f'    document.addEventListener("DOMContentLoaded",loadSchema);\n'
            f'  }}\n'
            f'}})();\n'
            f'</script>\n'
            f'</div>'
        )

    def _inject_schema_as_new_tab(self, html_content: str, schema_filename: str,
                                   spec_name: str) -> Optional[str]:
        """
        Add a JSON Schema tab to the FHIR IG publisher's nav-tabs navigation.

        The FHIR IG publisher uses Bootstrap Nav as *inter-page* navigation —
        each tab is a link to a separate HTML page (e.g.
        StructureDefinition-DAK-definitions.html, StructureDefinition-DAK.profile.xml.html).
        There is NO tab-content / tab-pane structure on these pages.

        This method adds a ``<li>`` linking to
        ``{spec_name}.schema.json.html`` which is a companion page generated
        by ``_generate_schema_view_page()``.

        Args:
            html_content: Full HTML of the StructureDefinition page
            schema_filename: Basename of the schema file
                             (e.g. 'StructureDefinition-DAK.schema.json')
            spec_name: Resource name (e.g. 'StructureDefinition-DAK')

        Returns:
            Updated HTML string, or None if the nav-tabs <ul> was not found
        """
        try:
            schema_page = f'{spec_name}.schema.json.html'

            # Guard: skip if already injected
            if schema_page in html_content:
                self.logger.info(
                    f'JSON Schema tab already present in {spec_name}.html – skipping'
                )
                return html_content

            nav_tabs_re = re.compile(
                r'(<ul[^>]*class="[^"]*(?:nav-tabs|fhir-nav-tabs)[^"]*"[^>]*>)(.*?)(</ul>)',
                re.DOTALL | re.IGNORECASE,
            )
            nav_match = nav_tabs_re.search(html_content)
            if not nav_match:
                self.logger.warning(
                    f'nav-tabs <ul> not found in {spec_name}.html – skipping tab injection'
                )
                return None

            new_li = (
                f'\n<li role="presentation">'
                f'<a href="{schema_page}">JSON Schema</a>'
                f'</li>\n'
            )
            updated_nav = (
                nav_match.group(1) + nav_match.group(2) + new_li + nav_match.group(3)
            )
            html_content = (
                html_content[:nav_match.start()]
                + updated_nav
                + html_content[nav_match.end():]
            )
            self.logger.info(f'Added JSON Schema tab link to {spec_name}.html')
            return html_content

        except Exception as exc:
            self.logger.error(f'Error adding schema tab for {spec_name}: {exc}')
            return None

    def _inject_schema_tab_into_sibling_pages(
        self, spec_name: str, schema_filename: str, output_dir: str
    ) -> int:
        """
        Inject the JSON Schema tab into all sibling pages of a StructureDefinition.

        The FHIR IG Publisher generates separate pages for each format view, e.g.
        ``StructureDefinition-DAK-mappings.html``,
        ``StructureDefinition-DAK.profile.json.html``.  Each page has its own copy
        of the nav-tabs bar, so the JSON Schema tab must be added to every one of
        them so that it is visible regardless of which tab the user is on.

        The main content page (``{spec_name}.html``) and the generated schema view
        page (``{spec_name}.schema.json.html``) are excluded — the former is handled
        by the caller and the latter is the destination of the new tab.

        Args:
            spec_name:        Resource name (e.g. ``StructureDefinition-DAK``)
            schema_filename:  Basename of the schema file
            output_dir:       Directory produced by the FHIR IG Publisher

        Returns:
            Number of sibling pages updated.
        """
        schema_page = f'{spec_name}.schema.json.html'
        main_page = f'{spec_name}.html'
        count = 0

        try:
            html_files = [f for f in os.listdir(output_dir) if f.endswith('.html')]
        except OSError as e:
            self.logger.warning(f'Cannot list {output_dir} for sibling injection: {e}')
            return 0

        for html_file in html_files:
            # Only process pages that belong to this spec (same name prefix)
            if not (html_file.startswith(f'{spec_name}-')
                    or html_file.startswith(f'{spec_name}.')):
                continue
            # Skip the main content page and the schema view page we are generating
            if html_file in (main_page, schema_page):
                continue

            html_path = os.path.join(output_dir, html_file)
            try:
                with open(html_path, 'r', encoding='utf-8', errors='replace') as f:
                    html_content = f.read()

                updated = self._inject_schema_as_new_tab(
                    html_content, schema_filename, spec_name
                )
                if updated is not None and updated != html_content:
                    with open(html_path, 'w', encoding='utf-8') as f:
                        f.write(updated)
                    count += 1
                    self.logger.info(
                        f'Added JSON Schema tab to sibling page: {html_file}'
                    )
            except Exception as e:
                self.logger.warning(
                    f'Could not inject schema tab into {html_file}: {e}'
                )

        return count

    def _generate_schema_view_page(self, html_content: str, schema_filename: str,
                                    spec_name: str, output_dir: str) -> Optional[str]:
        """
        Generate a standalone ``{spec_name}.schema.json.html`` page.

        The page reuses the head / header / nav-tabs from the original
        StructureDefinition page, makes the JSON Schema tab the active tab
        (Content tab becomes a normal link back to the original page), and
        shows the schema content via a same-origin fetch + Prism.js highlight.

        Args:
            html_content: Full HTML of the StructureDefinition page **after**
                          ``_inject_schema_as_new_tab`` has already added the
                          JSON Schema ``<li>`` to the nav-tabs.
            schema_filename: Basename of the ``.schema.json`` file
            spec_name: Resource name (e.g. ``StructureDefinition-DAK``)
            output_dir: Directory where the new HTML file will be written

        Returns:
            Filename of the generated page, or None on failure
        """
        try:
            schema_page = f'{spec_name}.schema.json.html'
            schema_page_path = os.path.join(output_dir, schema_page)

            # ── Locate nav-tabs in the (already modified) html_content ────────
            nav_tabs_re = re.compile(
                r'(<ul[^>]*class="[^"]*(?:nav-tabs|fhir-nav-tabs)[^"]*"[^>]*>)(.*?)(</ul>)',
                re.DOTALL | re.IGNORECASE,
            )
            nav_match = nav_tabs_re.search(html_content)
            if not nav_match:
                self.logger.warning(
                    f'Cannot generate schema view page: nav-tabs not found in {spec_name}.html'
                )
                return None

            # ── Transform nav-tabs for the schema view page ───────────────────
            # 1. Remove active class from Content tab; change href="#" → "{spec_name}.html"
            # 2. Make JSON Schema tab active; change its href to "#"
            nav_section = html_content[nav_match.start():nav_match.end()]

            # Content tab — flexible match for whitespace/attribute variations
            # Matches: <li class="active"> ... <a href="#">Content</a> ... </li>
            nav_section = re.sub(
                r'<li[^>]*class="active"[^>]*>\s*<a[^>]*href="#"[^>]*>(\s*Content\s*)</a>\s*</li>',
                f'<li>\n    <a href="{spec_name}.html">Content</a>\n  </li>',
                nav_section,
                flags=re.DOTALL | re.IGNORECASE,
            )
            # JSON Schema tab link → active (flexible whitespace)
            nav_section = re.sub(
                r'<li[^>]*>\s*<a[^>]*href="'
                + re.escape(schema_page)
                + r'"[^>]*>\s*JSON Schema\s*</a>\s*</li>',
                '<li role="presentation" class="active"><a href="#">JSON Schema</a></li>',
                nav_section,
                flags=re.DOTALL | re.IGNORECASE,
            )

            header_html = html_content[:nav_match.start()] + nav_section

            # ── Extract footer (inner-wrapper end → end of file) ──────────────
            # The FHIR IG Publisher wraps content in:
            #   segment-content > container > row > inner-wrapper > col-12 > nav-tabs
            # We need to close col-12, inner-wrapper, row, container before the
            # segment-content closing comment.  Anchoring on <!-- /inner-wrapper -->
            # (the first occurrence after the nav tabs) lets us pick up all four
            # closing </div> tags reliably without hardcoding their count.
            footer_re = re.compile(
                r'</div>\s*<!--\s*/inner-wrapper\s*-->', re.IGNORECASE
            )
            footer_match = footer_re.search(html_content, nav_match.end())
            footer_html = (
                '\n</div>\n' + html_content[footer_match.start():]
                if footer_match
                else '\n</div>\n</div>\n</div>\n</div>\n</div>'
            )

            # ── Generate schema content for the standalone page ───────────────
            safe_id = re.sub(r'[^a-zA-Z0-9]', '-', spec_name).lower()
            safe_id = re.sub(r'-+', '-', safe_id).strip('-')
            tab_id = f'dak-json-schema-{safe_id}'

            schema_body = (
                f'<div style="padding:1rem;">\n'
                f'<h2>JSON Schema</h2>\n'
                f'<p><a href="{schema_filename}">Raw JSON Schema</a>'
                f' | <a href="{schema_filename}" download>Download</a></p>\n'
                f'<pre style="background:#f5f5f5;padding:1rem;border-radius:4px;">'
                f'<code id="{tab_id}-display" class="language-json" '
                f'style="font-size:0.85em;white-space:pre-wrap;display:block;">'
                f'Loading schema&#8230;</code></pre>\n'
                f'</div>\n'
                f'<script>\n'
                f'(function(){{\n'
                # Map JSON Schema "type" values to hl7.org/fhir/R4 spec URLs.
                # "number" is JSON Schema's representation of FHIR's decimal type.
                f'  var FHIR_TYPE_LINKS={{\n'
                f'    "string":"http://hl7.org/fhir/R4/datatypes.html#string",\n'
                f'    "boolean":"http://hl7.org/fhir/R4/datatypes.html#boolean",\n'
                f'    "integer":"http://hl7.org/fhir/R4/datatypes.html#integer",\n'
                f'    "number":"http://hl7.org/fhir/R4/datatypes.html#decimal"\n'
                f'  }};\n'
                # After Prism highlights the JSON, post-process the innerHTML to
                # add <a href> links around FHIR type names and absolute $ref URLs.
                # Prism marks property keys as <span class="token property"> and
                # string values as <span class="token string">, separated by a
                # <span class="token operator">:</span> element.  The pattern must
                # bridge that operator span: property</span><span…>…</span> value.
                f'  function addFhirLinks(el){{\n'
                f'    var html=el.innerHTML;\n'
                # Link FHIR primitive type values under "type" keys.
                # Matches HTML like:
                #   <span class="token property">&quot;type&quot;</span>
                #   <span class="token operator">:</span> 
                #   <span class="token string">&quot;string&quot;</span>
                f'    Object.keys(FHIR_TYPE_LINKS).forEach(function(t){{\n'
                f'      var url=FHIR_TYPE_LINKS[t];\n'
                f'      html=html.replace(\n'
                f'        new RegExp(\n'
                f'          \'(<span class="token property">&quot;type&quot;</span><span[^>]*>[^<]*</span>[^<]*)\'\n'
                f'          +\'(<span class="token string">&quot;\'+t+\'&quot;</span>)\',\n'
                f'          \'g\'\n'
                f'        ),\n'
                f'        \'$1<a href="\'+url+\'" target="_blank" rel="noopener noreferrer">$2</a>\'\n'
                f'      );\n'
                f'    }});\n'
                # Link absolute hl7.org/fhir $ref values.
                # Matches HTML like:
                #   <span class="token property">&quot;$ref&quot;</span>
                #   <span class="token operator">:</span> 
                #   <span class="token string">&quot;http://hl7.org/fhir/...&quot;</span>
                f'    html=html.replace(\n'
                f'      /(<span class="token property">&quot;\\$ref&quot;<\\/span><span[^>]*>[^<]*<\\/span>[^<]*)(<span class="token string">&quot;(http:\\/\\/hl7\\.org\\/fhir[^&"]*?)&quot;<\\/span>)/g,\n'
                f'      function(m,pre,span,href){{\n'
                f'        return pre+\'<a href="\'+href+\'" target="_blank" rel="noopener noreferrer">\'+span+\'</a>\';\n'
                f'      }}\n'
                f'    );\n'
                f'    el.innerHTML=html;\n'
                f'  }}\n'
                f'  function loadSchema(){{\n'
                f'    var el=document.getElementById("{tab_id}-display");\n'
                f'    if(!el)return;\n'
                f'    fetch("{schema_filename}")\n'
                f'      .then(function(r){{return r.json();}})\n'
                f'      .then(function(d){{\n'
                f'        var txt=JSON.stringify(d,null,2);\n'
                f'        el.textContent=txt;\n'
                f'        if(window.Prism&&Prism.languages.json){{\n'
                f'          setTimeout(function(){{\n'
                f'            el.innerHTML=Prism.highlight(txt,Prism.languages.json,"json");\n'
                f'            addFhirLinks(el);\n'
                f'          }},0);\n'
                f'        }}\n'
                f'      }})\n'
                f'      .catch(function(e){{\n'
                f'        el.textContent="Error loading {schema_filename}: "+e.message;\n'
                f'      }});\n'
                f'  }}\n'
                f'  document.addEventListener("DOMContentLoaded",loadSchema);\n'
                f'}})();\n'
                f'</script>\n'
            )

            full_page = header_html + '\n\n' + schema_body + '\n\n' + footer_html

            with open(schema_page_path, 'w', encoding='utf-8') as f:
                f.write(full_page)

            self.logger.info(f'Generated schema view page: {schema_page_path}')
            return schema_page

        except Exception as exc:
            self.logger.error(
                f'Error generating schema view page for {spec_name}: {exc}'
            )
            return None

    def _find_injection_point(self, html_content: str, schema_type: str) -> Optional[int]:
        """
        Find the appropriate injection point in FHIR IG generated HTML content.
        
        For StructureDefinition pages: after "Formal Views of Profile Content"
        For ValueSet pages: after "Expansion" section (last IG publisher content)
        
        Args:
            html_content: The HTML content to search
            schema_type: Type of schema ('valueset', 'logical_model', etc.)
            
        Returns:
            Index position for injection, or None if not found
        """
        try:
            # For logical models (StructureDefinition pages), look for "Formal Views" section
            if schema_type == 'logical_model':
                # Look for the end of the "Formal Views of Profile Content" section
                formal_views_patterns = [
                    r'<h3[^>]*>Formal Views of Profile Content</h3>.*?</div>\s*</div>',
                    r'<h2[^>]*>Formal Views of Profile Content</h2>.*?</div>\s*</div>',
                    r'<h3[^>]*>Formal Views</h3>.*?</div>\s*</div>',
                    r'<h2[^>]*>Formal Views</h2>.*?</div>\s*</div>'
                ]
                
                for pattern in formal_views_patterns:
                    import re
                    match = re.search(pattern, html_content, re.DOTALL | re.IGNORECASE)
                    if match:
                        self.logger.info(f"Found 'Formal Views' section for injection point")
                        return match.end()
            
            # For ValueSet pages, look for "Expansion" section
            elif schema_type == 'valueset':
                # Look for the end of the "Expansion" section
                expansion_patterns = [
                    r'<h3[^>]*>Expansion</h3>.*?</div>\s*</div>',
                    r'<h2[^>]*>Expansion</h2>.*?</div>\s*</div>',
                    r'<h4[^>]*>Expansion</h4>.*?</div>\s*</div>'
                ]
                
                for pattern in expansion_patterns:
                    import re
                    match = re.search(pattern, html_content, re.DOTALL | re.IGNORECASE)
                    if match:
                        self.logger.info(f"Found 'Expansion' section for injection point")
                        return match.end()
            
            # Fallback: look for common FHIR IG content structures
            fallback_patterns = [
                # Look for the end of main content div
                r'<div[^>]*class="[^"]*col-12[^"]*"[^>]*>.*?</div>\s*(?=<div[^>]*class="[^"]*col-12[^"]*"|$)',
                # Look for navigation or footer sections to inject before
                r'(?=<div[^>]*class="[^"]*nav[^"]*")',
                r'(?=<footer)',
                # Generic fallback
                r'</main>',
                r'</body>'
            ]
            
            for pattern in fallback_patterns:
                import re
                match = re.search(pattern, html_content, re.DOTALL | re.IGNORECASE)
                if match:
                    self.logger.info(f"Using fallback injection point")
                    return match.start() if pattern.startswith('(?=') else match.end()
            
            self.logger.warning("No suitable injection point found")
            return None
            
        except Exception as e:
            self.logger.error(f"Error finding injection point: {e}")
            return None
    
    def _remove_dak_api_content_block(self, html_content: str) -> str:
        """
        Remove any pre-existing ``<div class="dak-api-content">…</div>`` block
        and the inline ``<style>`` / disclaimer ``<p>`` that the old generator
        always appended immediately after the closing ``</div>``.

        Previous builds may have injected a dak-api-content block (including
        Schema Definition sections) whose HTML is now stale.  The IG Publisher
        sometimes reuses cached output pages, so the block can persist even after
        the generating code has been updated.  This method strips it so the page
        starts clean before any new content is written.

        Args:
            html_content: Raw HTML string.

        Returns:
            HTML with the dak-api-content block (and its trailing style/disclaimer)
            removed.  Returns the input unchanged if no dak-api-content block is
            found.
        """
        # Find the start of the dak-api-content div
        open_tag_re = re.compile(r'<div\b[^>]*\bclass="dak-api-content"[^>]*>', re.IGNORECASE)
        m = open_tag_re.search(html_content)
        if not m:
            return html_content

        start = m.start()
        pos = m.end()
        depth = 1  # We are inside one <div>

        # Walk forward counting open/close <div> tags to find the matching </div>
        tag_re = re.compile(r'<(/?)div\b', re.IGNORECASE)
        for tag_m in tag_re.finditer(html_content, pos):
            if tag_m.group(1):  # closing tag </div>
                depth -= 1
                if depth == 0:
                    # Advance past the '>' that closes the </div> tag
                    close_gt = html_content.find('>', tag_m.end())
                    end = close_gt + 1 if close_gt != -1 else tag_m.end()
                    break
            else:  # opening tag <div>
                depth += 1
        else:
            # Never found the matching close tag — leave content unchanged
            self.logger.warning('Could not find matching </div> for dak-api-content block')
            return html_content

        # Also consume optional trailing artifacts that the old _generate_html_content
        # always appended immediately after the closing </div>:
        #   - an inline <style>…</style> block
        #   - a <p><em>…</em></p> disclaimer paragraph
        # Skip leading whitespace then check for each artifact in order.
        scan = end
        # Skip whitespace
        while scan < len(html_content) and html_content[scan] in ' \t\r\n':
            scan += 1
        # Remove <style>...</style> if immediately following
        if html_content[scan:scan+7].lower() == '<style>':
            style_end = html_content.lower().find('</style>', scan)
            if style_end != -1:
                end = style_end + len('</style>')
                # Skip whitespace again
                while end < len(html_content) and html_content[end] in ' \t\r\n':
                    end += 1
            scan = end
        # Remove <p><em>...</em></p> disclaimer if immediately following
        if html_content[scan:scan+7].lower() == '<p><em>':
            p_end = html_content.lower().find('</p>', scan)
            if p_end != -1:
                end = p_end + len('</p>')

        result = html_content[:start] + html_content[end:]
        self.logger.info('Removed pre-existing dak-api-content block')
        return result

    def inject_into_html(self, openapi_path: str, output_dir: str, title: str = None, schema_type: str = None) -> Optional[str]:
        """
        Inject OpenAPI content into an existing HTML file that was generated by the IG publisher.
        
        This replaces the old generate_redoc_html approach by working with already-generated HTML files.
        
        Args:
            openapi_path: Path to the OpenAPI spec file
            output_dir: Directory containing the generated HTML files
            title: Optional title for the page
            schema_type: Optional schema type ('valueset' or 'logical_model')
            
        Returns:
            Path to the updated HTML file, or None if failed
        """
        try:
            openapi_filename = os.path.basename(openapi_path)
            spec_name = openapi_filename.replace('.openapi.json', '').replace('.openapi.yaml', '').replace('.yaml', '').replace('.yml', '').replace('.json', '')
            
            # Determine schema type if not provided
            if schema_type is None:
                if spec_name.startswith('ValueSet-'):
                    schema_type = 'valueset'
                elif spec_name.startswith('LogicalModel-') or spec_name.startswith('StructureDefinition-'):
                    schema_type = 'logical_model'
                else:
                    schema_type = 'unknown'
            
            if title is None:
                title = f"{spec_name} API Documentation"
            
            # Load the OpenAPI spec
            with open(openapi_path, 'r', encoding='utf-8') as f:
                spec_data = json.load(f)
            
            # Find the corresponding HTML file in the output directory
            html_filename = f"{spec_name}.html"
            html_path = os.path.join(output_dir, html_filename)
            
            if not os.path.exists(html_path):
                self.logger.warning(f"HTML file not found: {html_path}. IG publisher may not have processed the placeholder.")
                return None
            
            # Read the existing HTML file
            with open(html_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            # Check for the placeholder marker
            placeholder_marker = f'<!-- DAK_API_PLACEHOLDER: {spec_name} -->'

            # For logical model pages, always inject a JSON Schema tab pointing to
            # {spec_name}.schema.json.  The schema is generated by
            # generate_logical_model_schemas.py (which runs before this script in
            # the CI pipeline) so it will be present at deployment time.
            # Never fall back to the raw FHIR .json StructureDefinition file.
            if schema_type == 'logical_model':
                # Remove any pre-existing dak-api-content block (from previous CI
                # runs where the old generator injected Schema Definition content).
                # The IG Publisher sometimes reuses cached HTML, so the block can
                # persist across builds even after the generator was updated.
                html_content = self._remove_dak_api_content_block(html_content)
                # Clear the placeholder marker if present (it may have been
                # preserved by the IG Publisher or be absent if the page was cached).
                if placeholder_marker in html_content:
                    html_content = html_content.replace(placeholder_marker, '')

                schema_filename = f'{spec_name}.schema.json'
                updated_html = self._inject_schema_as_new_tab(
                    html_content, schema_filename, spec_name
                )
                if updated_html is not None:
                    html_content = updated_html
                    self.logger.info(
                        f'Injected JSON Schema tab into {html_path}'
                    )
                    # Generate the companion schema view page
                    self._generate_schema_view_page(
                        html_content, schema_filename, spec_name, output_dir
                    )
                    # Propagate the JSON Schema tab to all sibling pages
                    # (Mappings, XML, JSON, TTL, Definitions, etc.) so it
                    # appears on every tab, not just Content.
                    self._inject_schema_tab_into_sibling_pages(
                        spec_name, schema_filename, output_dir
                    )
                else:
                    self.logger.warning(
                        f'Tab injection failed for {spec_name}; no schema tab added'
                    )
                with open(html_path, 'w', encoding='utf-8') as f:
                    f.write(html_content)
                return html_filename

            # Strip any pre-existing dak-api-content block (from a previous CI
            # build where the old generator included Schema Definition sections).
            # This is needed when the IG Publisher reuses cached HTML pages.
            html_content = self._remove_dak_api_content_block(html_content)

            if placeholder_marker not in html_content:
                self.logger.warning(f"Placeholder marker not found in {html_path}. Searching for appropriate FHIR IG content section.")
                # Find the appropriate injection point based on content type
                injection_point = self._find_injection_point(html_content, schema_type)
                if injection_point is None:
                    self.logger.error(f"No suitable injection point found in {html_path}")
                    return None
            else:
                injection_point = html_content.find(placeholder_marker)
            
            # Generate the documentation content (HTML instead of markdown)
            doc_content = self._generate_html_content(spec_data, openapi_filename, schema_type)
            
            # Inject the content
            if placeholder_marker in html_content:
                # Replace the placeholder with actual content
                updated_html = html_content.replace(placeholder_marker, doc_content)
            else:
                # Insert at the injection point
                updated_html = html_content[:injection_point] + doc_content + html_content[injection_point:]
            
            # Write the updated HTML file
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(updated_html)
            
            self.logger.info(f"Injected OpenAPI content into HTML file: {html_path}")
            return html_filename
            
        except Exception as e:
            self.logger.error(f"Error injecting content into HTML for {openapi_path}: {e}")
            return None

    def _generate_html_content(self, spec_data: dict, openapi_filename: str, schema_type: str) -> str:
        """
        Generate HTML content for OpenAPI documentation.
        
        Args:
            spec_data: Parsed OpenAPI specification
            openapi_filename: Name of the OpenAPI file
            schema_type: Type of schema ('valueset', 'logical_model', etc.)
            
        Returns:
            HTML content string
        """
        html_content = f"""
<!-- OpenAPI Documentation Content -->
<div class="dak-api-content">
"""
        
        # Add API info
        info = spec_data.get('info', {})
        html_content += f"""
<div class="api-info">
<h2>API Information</h2>
<div class="card">
<div class="card-body">
<h5 class="card-title">{info.get('title', 'API')}</h5>
<p class="card-text">{info.get('description', 'No description available')}</p>
<p><strong>Version:</strong> {info.get('version', 'Unknown')}</p>
</div>
</div>
</div>
"""
        
        # Add endpoints
        paths = spec_data.get('paths', {})
        if paths:
            html_content += """
<div class="api-endpoints">
<h2>Endpoints</h2>
"""
            
            for path, methods in paths.items():
                for method, operation in methods.items():
                    html_content += f"""
<div class="endpoint-card">
<h3><span class="badge badge-{method.lower()}">{method.upper()}</span> {path}</h3>
<h4>{operation.get('summary', 'No summary')}</h4>
<p>{operation.get('description', 'No description available')}</p>
</div>
"""
            
            html_content += """
</div>
"""
        
        # Schema Definition section is intentionally omitted for all resource types
        # to avoid duplicate content — schema information is accessible via dedicated
        # schema tabs or schema view pages generated elsewhere in the pipeline.
        
        # Add styling that integrates with IG theme
        html_content += """
</div>

<style>
/* DAK API documentation styling that integrates with IG theme */
.dak-api-content {
  margin: 1rem 0;
}

.api-info .card, .endpoint-card {
  background-color: #f8f9fa;
  border: 1px solid #dee2e6;
  border-radius: 0.375rem;
  padding: 1rem;
  margin: 1rem 0;
}

.endpoint-card h3 {
  color: #00477d;
  margin-top: 0;
}

.badge-get { background-color: #28a745; }
.badge-post { background-color: #007bff; }
.badge-put { background-color: #ffc107; color: #212529; }
.badge-delete { background-color: #dc3545; }
.badge-patch { background-color: #6f42c1; }
</style>

<p><em>This documentation is automatically generated from the OpenAPI specification.</em></p>
"""
        
        return html_content

    def _build_fhir_restore_js(self, link_map: dict, lang: str) -> str:
        """Return JavaScript (with {{ }} doubled for .format()-safety) that re-applies
        FHIR documentation links on Prism-highlighted source content.

        The FHIR IG Publisher embeds ``<a href>`` links around property/element names in
        the static ``<pre>`` blocks.  After dynamic loading fetches the raw source file
        those links are absent.  This snippet runs inside the ``setTimeout`` after
        ``Prism.highlight()`` to restore them by scanning the highlighted HTML for the
        known token spans produced by Prism for each source format.

        For JSON format pages the FHIR IG Publisher sometimes does not embed ``<a href>``
        links in the raw JSON source.  In those cases ``link_map`` is empty and a static
        fallback map of common FHIR R4 property names is used instead so that users still
        see FHIR documentation links on dynamically-loaded JSON views.

        Args:
            link_map: Mapping of ``{text: url}`` extracted from the static HTML block.
            lang: Prism language name ('json', 'xml', 'turtle').

        Returns:
            JavaScript code with ``{`` and ``}`` doubled so it is safe to embed inside
            a ``.format()`` template.  Returns empty string when link_map is empty and
            no fallback is applicable, or lang is unsupported.
        """
        # For JSON, merge extracted links with the static fallback map.
        # The extracted links (from the IG Publisher static HTML) take priority;
        # fallback covers properties the IG Publisher does not link in JSON views.
        if lang == 'json':
            effective_map = dict(_FHIR_R4_JSON_FALLBACK_LINKS)
            effective_map.update(link_map)  # extracted links override fallback
        else:
            effective_map = link_map

        if not effective_map:
            return ''

        links_json = json.dumps(effective_map)

        if lang == 'json':
            # Prism JSON: property keys → <span class="token property">&quot;key&quot;</span>
            # Note: Prism.highlight() encodes " as &quot; in its HTML output, so
            # el.innerHTML contains &quot; around property names, not plain ".
            # The regex matches either &quot; or " to handle both Prism versions.
            js = (
                'var FL=' + links_json + ';'
                'el.innerHTML=el.innerHTML.replace('
                '/(<span class="token property">)(?:&quot;|")([A-Za-z0-9_$@-]+)(?:&quot;|")(<\\/span>)/g,'
                "function(m,o,k,c){return FL[k]?o+'&quot;<a href=\"'+FL[k]+'\">'+(k)+'</a>&quot;'+c:m;});"
            )
        elif lang == 'xml':
            # Prism markup: element names follow the &lt;[/] punctuation span;
            # attribute names are in attr-name spans.
            js = (
                'var FL=' + links_json + ';'
                'el.innerHTML=el.innerHTML.replace('
                '/(<span class="token punctuation">&lt;\\/?<\\/span>)([A-Za-z][A-Za-z0-9._:-]*)/g,'
                "function(m,lt,nm){return FL[nm]?lt+'<a href=\"'+FL[nm]+'\">'+(nm)+'</a>':m;}"
                ').replace('
                '/(<span class="token attr-name">)([A-Za-z][A-Za-z0-9._:-]*)(<\\/span>)/g,'
                "function(m,p,n,s){return FL[n]?p+'<a href=\"'+FL[n]+'\">'+(n)+'</a>'+s:m;});"
            )
        elif lang == 'turtle':
            # Turtle: scan all Prism span text for matching FHIR predicate names
            # (e.g. fhir:id, fhir:text).  Keys shorter than 3 chars are skipped to
            # avoid false positives on punctuation tokens.
            js = (
                'var FL=' + links_json + ';'
                'el.innerHTML=el.innerHTML.replace('
                '/(<span[^>]*>)([^<]+)(<\\/span>)/g,'
                "function(m,p,t,s){var k=t.trim();return(FL[k]&&k.length>2)?p+'<a href=\"'+FL[k]+'\">'+(t)+'</a>'+s:m;});"
            )
        else:
            return ''

        # Double { and } so this JS survives being embedded inside a .format() template.
        return js.replace('{', '{{').replace('}', '}}')

    def _replace_lang_source(self, html: str, lang: str, label: str, src_file: str,
                             allow_classless: bool = False) -> str:
        """
        Replace one language's static pre-formatted source block with a dynamic loader.

        The FHIR IG Publisher embeds full source code in ``<pre class="LANG">`` blocks
        at publication time (and sometimes in ``<pre><code>`` blocks without a class on
        format-specific pages).  This replaces those blocks with a tiny ``<code>`` element
        plus a ``<script>`` that fetches the raw source file on-demand and applies
        Prism.js syntax highlighting.

        For CQL (Library resource pages), ``Raw CQL | Download CQL`` links are prepended
        to each replaced block because the IG Publisher does not generate these links for
        CQL the way it does for JSON / XML.  Prism.js does not ship a CQL grammar, so the
        content is displayed as plain pre-formatted text (the fetch and display still work
        correctly; only syntax colouring is absent).

        Args:
            html: Full HTML content of the page
            lang: Source language / class name ('json', 'xml', 'turtle', 'cql')
            label: Human-readable label ('JSON', 'XML', 'TTL', 'CQL')
            src_file: Relative URL of the raw source file to fetch (same directory)
            allow_classless: When True, also replace ``<pre>`` blocks that have no
                ``class`` attribute (used for format-specific pages where the language
                is known from the page name, e.g. ``StructureDefinition-DAK.profile.xml.html``).

        Returns:
            Updated HTML string
        """
        # Match <pre> opening tags whose class contains the language word.
        # <pre> cannot be nested in HTML, so the first </pre> after each opening
        # tag is always its matching close.
        pre_open_re = re.compile(
            r'<pre\b([^>]*?\bclass="[^"]*?\b' + re.escape(lang) + r'\b[^"]*?"[^>]*)>',
            re.IGNORECASE
        )
        # For format-specific pages (allow_classless=True), also match <pre> tags that
        # have no class attribute at all (the FHIR IG Publisher sometimes omits the class
        # on per-format view pages like StructureDefinition-Foo.profile.xml.html).
        classless_pre_re = re.compile(
            r'<pre\b(?![^>]*\bclass=)[^>]*>',
            re.IGNORECASE
        ) if allow_classless else None
        close_tag = '</pre>'
        close_tag_lower = close_tag.lower()

        parts: List[str] = []
        pos = 0
        occurrence = 0

        while pos < len(html):
            m = pre_open_re.search(html, pos)
            # Also check the classless pattern when enabled; use whichever match comes first.
            if classless_pre_re:
                m2 = classless_pre_re.search(html, pos)
                if m2 and (m is None or m2.start() < m.start()):
                    m = m2
            if not m:
                break

            body_start = m.end()
            close_pos = html.lower().find(close_tag_lower, body_start)
            if close_pos < 0:
                break  # malformed HTML; stop processing

            pre_content = html[body_start:close_pos]

            # Only replace blocks that contain a <code> element with substantial content.
            code_match = re.search(r'<code([^>]*)>([\s\S]*?)</code>', pre_content, re.IGNORECASE)
            if not code_match or len(code_match.group(2).strip()) < _MIN_SOURCE_SIZE_FOR_DYNAMIC_LOADING:
                # Keep this block unchanged; preserve everything from pos through </pre>
                parts.append(html[pos:close_pos + len(close_tag)])
                pos = close_pos + len(close_tag)
                continue

            # Everything before this <pre>
            parts.append(html[pos:m.start()])

            # Build a stable, unique element ID: lang + sanitized filename + occurrence index
            occurrence += 1
            safe_name = re.sub(r'[^a-z0-9]', '-', src_file.lower())
            el_id = 'dyn-{}-{}-{}'.format(lang, safe_name, occurrence)

            # Extract FHIR documentation links from the static source block so they
            # can be restored after Prism re-highlights the dynamically fetched content.
            # The IG Publisher embeds <a href="URL">text</a> around property/element names.
            # Only hl7.org/fhir URLs are included; the anchor text must be plain (no tags).
            # Use \s before href so the pattern matches href in any attribute position.
            _href_re = re.compile(r'<a\b[^>]*\shref="([^"]+)"[^>]*>([^<]+)</a>')
            link_map: Dict[str, str] = {}
            for lm in _href_re.finditer(code_match.group(2)):
                url, text = lm.group(1), lm.group(2).strip()
                # Accept canonical FHIR spec URLs (http or https) to avoid injecting
                # arbitrary content.
                if text and re.search(r'https?://hl7\.org/fhir/', url):
                    link_map[text] = url
            fhir_restore = self._build_fhir_restore_js(link_map, lang)

            # Fetch body differs by format: JSON gets pretty-printed via JSON.stringify.
            # Content is fetched asynchronously via fetch().then(); once received the raw
            # text is shown immediately, then Prism.highlight() (synchronous, no Web Worker)
            # is deferred via setTimeout(fn,0) so it doesn't block the UI.
            # We avoid Prism.highlightElement() which spawns a Web Worker and throws
            # "Cannot read properties of undefined (reading 'payload')" on some pages.
            # fhir_restore (already {{ }}-escaped) runs inside the same setTimeout to
            # re-apply FHIR documentation links after highlighting.
            if lang == 'json':
                fetch_body = (
                    'fetch("{f}").then(function(r){{return r.json();}}).then(function(d){{'
                    'var txt=JSON.stringify(d,null,2);'
                    'el.textContent=txt;'
                    'if(window.Prism&&Prism.languages.json)'
                    '{{setTimeout(function(){{el.innerHTML=Prism.highlight(txt,Prism.languages.json,"json");'
                    + fhir_restore +
                    '}},0);}}'
                    '}})'
                ).format(f=src_file)
            else:
                # For XML, fall back to Prism.languages.markup when Prism.languages.xml
                # is not registered (some Prism.js builds only register the grammar as
                # 'markup').  For turtle the language name matches the FHIR IG Publisher's
                # registered name so no fallback is needed.
                if lang == 'xml':
                    grammar_expr = '(Prism.languages["{l}"]||Prism.languages.markup)'.format(l=lang)
                else:
                    grammar_expr = 'Prism.languages["{l}"]'.format(l=lang)
                fetch_body = (
                    'fetch("{f}").then(function(r){{return r.text();}}).then(function(t){{'
                    'el.textContent=t;'
                    'var _g={g};'
                    'if(window.Prism&&_g)'
                    '{{setTimeout(function(){{el.innerHTML=Prism.highlight(t,_g,"{l}");'
                    + fhir_restore +
                    '}},0);}}'
                    '}})'
                ).format(f=src_file, l=lang, g=grammar_expr)

            # For CQL, the IG Publisher does not generate raw/download links the way it
            # does for JSON and XML.  Prepend them here so users can access the raw file.
            raw_download_prefix = ''
            if lang == 'cql':
                raw_download_prefix = (
                    '<p><a href="' + src_file + '">Raw CQL</a>'
                    ' | <a href="' + src_file + '" download>Download CQL</a></p>\n'
                )

            loader = (
                raw_download_prefix +
                '<pre class="{l}"><code id="{id}" class="language-{l}" style="display:block;">'
                'Loading {label} source&#8230;</code></pre>'
                '<script>(function(){{'
                'var el=document.getElementById("{id}");if(!el)return;'
                'function loadSrc(){{if(el.dataset.loaded)return;el.dataset.loaded="1";'
                '{fb}'
                '.catch(function(e){{el.textContent="Could not load {label}: "+e.message;}});'
                '}}'
                # Activate on Bootstrap tab-shown event
                'document.addEventListener("shown.bs.tab",function(e){{'
                'var h=e.target&&(e.target.getAttribute("href")||e.target.getAttribute("data-bs-target")||"");'
                'if(h==="#{l}"||h.startsWith("#{l}-"))loadSrc();'
                '}});'
                # Load immediately on standalone format pages (no .tab-pane parent),
                # or if the containing tab-pane is already active on page load.
                'function checkActive(){{var p=el.closest&&el.closest(".tab-pane");'
                'if(!p||p.classList.contains("active")||p.classList.contains("show"))loadSrc();}}'
                'if(document.readyState!=="loading")checkActive();'
                'else document.addEventListener("DOMContentLoaded",checkActive);'
                '}})()</script>'
            ).format(l=lang, id=el_id, label=label, fb=fetch_body)

            parts.append(loader)
            pos = close_pos + len(close_tag)

        parts.append(html[pos:])
        return ''.join(parts)

    def replace_static_source_with_dynamic_loading(self, output_dir: str) -> int:
        """
        Replace large static pre-formatted source code in JSON / XML / TTL / CQL tabs with
        dynamic Prism.js loaders across all FHIR resource HTML pages.

        The FHIR IG Publisher embeds the full resource source in ``<pre class="json">``
        / ``<pre class="xml">`` / ``<pre class="turtle">`` blocks at publication time,
        which inflates every page significantly.  This method removes that embedded
        content and replaces it with a small JavaScript snippet that fetches the
        corresponding raw source file (already present in the output directory) on
        demand, then applies Prism.js syntax highlighting — zero CDN requests, zero
        build step.

        For Library resource pages the IG Publisher embeds CQL content as
        ``<pre><code class="language-cql">`` (no class on the outer ``<pre>``).
        This method normalises that pattern to ``<pre class="cql"><code …>`` before
        replacement and prepends ``Raw CQL | Download CQL`` links (the IG Publisher
        does not generate these links for CQL the way it does for JSON / XML).

        Args:
            output_dir: Directory produced by the FHIR IG Publisher

        Returns:
            Number of HTML files modified
        """
        # Each tuple is (prism_class, label, file_ext).
        # prism_class: CSS class on <pre> and Prism language name used in the loader JS.
        # file_ext: actual source file extension (.json / .xml / .ttl / .cql).
        # Note: the FHIR IG Publisher uses class="turtle" (not "ttl") on TTL <pre> blocks.
        FORMATS = [
            ('json', 'JSON', 'json'),
            ('xml',  'XML',  'xml'),
            ('turtle', 'TTL', 'ttl'),  # IG Publisher: <pre class="turtle">, source file *.ttl
            ('cql', 'CQL', 'cql'),     # Library CQL source; raw/download links are injected
        ]

        modified = 0
        try:
            html_files = sorted(f for f in os.listdir(output_dir) if f.endswith('.html'))
        except OSError as e:
            self.logger.error(f'Cannot list output dir {output_dir}: {e}')
            return 0

        for html_file in html_files:
            base_name = html_file[:-5]  # strip .html
            html_path = os.path.join(output_dir, html_file)

            # The FHIR IG Publisher creates dedicated per-format view pages named
            # "Foo.profile.{ext}.html" whose raw source file is "Foo.{ext}" (not
            # "Foo.profile.{ext}.{ext}").  Detect that pattern and remap the source
            # file name accordingly; fall back to the generic "{base_name}.{ext}" for
            # all other pages (e.g. pages that embed multiple formats inline).
            def _src_for_ext(file_ext: str) -> str:
                suffix = f'.profile.{file_ext}'
                if base_name.endswith(suffix):
                    return base_name[:-len(suffix)] + '.' + file_ext
                return f'{base_name}.{file_ext}'

            src_exists = {
                file_ext: os.path.exists(os.path.join(output_dir, _src_for_ext(file_ext)))
                for _, _, file_ext in FORMATS
            }
            if not any(src_exists.values()):
                continue

            try:
                with open(html_path, 'r', encoding='utf-8', errors='replace') as f:
                    html = f.read()

                original = html
                for prism_class, label, file_ext in FORMATS:
                    if src_exists[file_ext]:
                        # On format-specific pages (e.g. Foo.profile.xml.html), the FHIR IG
                        # Publisher sometimes emits <pre><code> blocks without a class
                        # attribute. Pass allow_classless=True so those are also replaced.
                        is_format_page = base_name.endswith(f'.profile.{file_ext}')
                        if prism_class == 'cql':
                            # The FHIR IG Publisher renders Library CQL content as:
                            #   <pre><code class="language-cql">...</code></pre>
                            # rather than <pre class="cql"><code>...</code></pre>.
                            # Normalise to the latter form so _replace_lang_source can
                            # detect and replace the block with a dynamic fetch loader.
                            html = re.sub(
                                r'<pre\b([^>]*?)>(\s*<code\b[^>]*\bclass="[^"]*\blanguage-cql\b)',
                                lambda m: (
                                    '<pre class="cql">'
                                    if not re.search(r'\bclass=', m.group(1), re.IGNORECASE)
                                    else '<pre' + m.group(1) + '>'
                                ) + m.group(2),
                                html,
                                flags=re.IGNORECASE,
                            )
                        html = self._replace_lang_source(
                            html, prism_class, label, _src_for_ext(file_ext),
                            allow_classless=is_format_page
                        )

                if html != original:
                    with open(html_path, 'w', encoding='utf-8') as f:
                        f.write(html)
                    modified += 1
                    self.logger.info(f'Dynamic source loading applied to {html_file}')

            except Exception as e:
                self.logger.warning(f'Could not process {html_file}: {e}')

        self.logger.info(
            f'Dynamic source loading: {modified}/{len(html_files)} HTML files modified'
        )
        return modified


class DAKApiHubGenerator:
    """Generates the unified DAK API documentation hub."""
    
    def __init__(self, logger: logging.Logger):
        self.logger = logger
    
    def create_enumeration_schema(self, schema_type: str, schema_files: List[str], output_dir: str) -> Optional[str]:
        """
        Create an enumeration schema file that lists all schemas of a given type.
        
        Args:
            schema_type: Type of schema ('valueset' or 'logical_model')  
            schema_files: List of schema file paths
            output_dir: Directory to save the enumeration schema
            
        Returns:
            Path to the generated enumeration schema file, or None if failed
        """
        try:
            # Create enumeration data by reading each schema file
            schemas_list = []
            
            for schema_path in schema_files:
                try:
                    with open(schema_path, 'r', encoding='utf-8') as f:
                        schema = json.load(f)
                    
                    schema_filename = os.path.basename(schema_path)
                    schema_entry = {
                        "filename": schema_filename,
                        "id": schema.get('$id', ''),
                        "title": schema.get('title', schema_filename),
                        "description": schema.get('description', ''),
                        "url": f"./{schema_filename}"
                    }
                    
                    # Add type-specific metadata
                    if schema_type == 'valueset':
                        if 'fhir:valueSet' in schema:
                            schema_entry['valueSetUrl'] = schema['fhir:valueSet']
                        if 'enum' in schema:
                            schema_entry['codeCount'] = len(schema['enum'])
                    elif schema_type == 'logical_model':
                        if 'fhir:logicalModel' in schema:
                            schema_entry['logicalModelUrl'] = schema['fhir:logicalModel']
                        if 'properties' in schema:
                            schema_entry['propertyCount'] = len(schema['properties'])
                    
                    schemas_list.append(schema_entry)
                    
                except Exception as e:
                    self.logger.warning(f"Error reading schema {schema_path}: {e}")
                    continue
            
            # Create the enumeration schema
            if schema_type == 'valueset':
                enum_filename = "ValueSets.schema.json"
                enum_title = "ValueSet Enumeration Schema"
                enum_description = "JSON Schema defining the structure of the ValueSet enumeration endpoint response"
            else:  # logical_model
                enum_filename = "LogicalModels.schema.json"
                enum_title = "Logical Model Enumeration Schema"  
                enum_description = "JSON Schema defining the structure of the Logical Model enumeration endpoint response"
            
            enumeration_schema = {
                "$schema": "https://json-schema.org/draft/2020-12/schema",
                "$id": f"#/{enum_filename}",
                "title": enum_title,
                "description": enum_description,
                "type": "object",
                "properties": {
                    "type": {
                        "type": "string",
                        "const": schema_type,
                        "description": f"The type of schemas enumerated ({schema_type})"
                    },
                    "count": {
                        "type": "integer",
                        "description": "Total number of schemas available"
                    },
                    "schemas": {
                        "type": "array",
                        "description": "Array of available schemas",
                        "items": {
                            "type": "object",
                            "properties": {
                                "filename": {
                                    "type": "string",
                                    "description": "Schema filename"
                                },
                                "id": {
                                    "type": "string",
                                    "description": "Schema $id"
                                },
                                "title": {
                                    "type": "string", 
                                    "description": "Schema title"
                                },
                                "description": {
                                    "type": "string",
                                    "description": "Schema description"
                                },
                                "url": {
                                    "type": "string",
                                    "description": "Relative URL to the schema file"
                                }
                            },
                            "required": ["filename", "title", "url"]
                        }
                    }
                },
                "required": ["type", "count", "schemas"],
                "example": {
                    "type": schema_type,
                    "count": len(schemas_list),
                    "schemas": schemas_list
                }
            }
            
            # Add type-specific properties to schema items
            if schema_type == 'valueset':
                enumeration_schema["properties"]["schemas"]["items"]["properties"]["valueSetUrl"] = {
                    "type": "string",
                    "description": "FHIR canonical URL of the ValueSet"
                }
                enumeration_schema["properties"]["schemas"]["items"]["properties"]["codeCount"] = {
                    "type": "integer", 
                    "description": "Number of codes in the ValueSet"
                }
            elif schema_type == 'logical_model':
                enumeration_schema["properties"]["schemas"]["items"]["properties"]["logicalModelUrl"] = {
                    "type": "string",
                    "description": "FHIR canonical URL of the Logical Model"
                }
                enumeration_schema["properties"]["schemas"]["items"]["properties"]["propertyCount"] = {
                    "type": "integer",
                    "description": "Number of properties in the Logical Model"  
                }
            
            # Save enumeration schema
            enum_path = os.path.join(output_dir, enum_filename)
            with open(enum_path, 'w', encoding='utf-8') as f:
                json.dump(enumeration_schema, f, indent=2, ensure_ascii=False)
            
            self.logger.info(f"Created enumeration schema: {enum_path}")
            return enum_path
            
        except Exception as e:
            self.logger.error(f"Error creating enumeration schema for {schema_type}: {e}")
            return None
    
    def generate_hub_html_content(self, schema_docs: Dict[str, List[Dict]], openapi_docs: List[Dict], enumeration_docs: List[Dict] = None, jsonld_docs: List[Dict] = None, existing_openapi_html_content: Optional[str] = None) -> str:
        """
        Generate HTML content for the DAK API hub page.
        
        Args:
            schema_docs: Dictionary with schema documentation info
            openapi_docs: List of OpenAPI documentation info
            enumeration_docs: List of enumeration endpoint documentation info
            jsonld_docs: List of JSON-LD vocabulary documentation info
            existing_openapi_html_content: Existing HTML content from input/images/openapi/index.html
            
        Returns:
            HTML content as a string
        """
        if enumeration_docs is None:
            enumeration_docs = []
        if jsonld_docs is None:
            jsonld_docs = []
        
        # Start building the HTML content (wrapped with markers so re-runs can replace it)
        html_content = """<!-- DAK_API_HUB_START -->
<div class="dak-api-hub">
    <p>This page provides access to all available DAK (Data Access Kit) API endpoints and schemas.
    The DAK API provides structured access to ValueSet enumerations and Logical Model definitions used throughout this implementation guide.</p>

    <h2>OpenAPI Documentation</h2>

    <p>Interactive Swagger UI documentation for all generated schemas and external API specifications is available in the OpenAPI documentation hub:
    <a href="openapi/index.html">View OpenAPI Documentation</a></p>

    <h2>Using the DAK API</h2>
    
    <div class="usage-info">
        <h3>Schema Validation</h3>
        <p>Each JSON Schema can be used to validate data structures in your applications. 
        The schemas follow the JSON Schema Draft 2020-12 specification and include:</p>
        <ul>
            <li>Type definitions and constraints</li>
            <li>Property descriptions and examples</li>
            <li>Required field specifications</li>
            <li>Enumeration values with links to definitions</li>
        </ul>
        
        <h3>JSON-LD Semantic Integration</h3>
        <p>The JSON-LD vocabularies provide semantic web integration for ValueSet enumerations. Each vocabulary includes:</p>
        <ul>
            <li>Enumeration class definitions with schema.org compatibility</li>
            <li>Individual code instances with canonical IRIs</li>
            <li>Property definitions with range constraints</li>
            <li>FHIR metadata integration (system URIs, ValueSet references)</li>
        </ul>
        
        <h3>Integration with FHIR</h3>
        <p>All schemas are derived from the FHIR definitions in this implementation guide. 
        Each schema page includes links to the corresponding FHIR resource definitions for complete context.</p>
        
        <h3>API Endpoints</h3>
        <p>The enumeration endpoints provide machine-readable lists of all available schemas, 
        making it easy to discover and integrate with the available data structures programmatically.</p>
    </div>
"""
        
        # Add Logical Models section with cards
        if schema_docs.get('logical_model'):
            html_content += """
    <h2>Logical Models</h2>
    
    <p>The following logical models define the structure for computable representations of WHO DAK content:</p>
    
    <div class="schema-grid">
"""
            for schema_doc in schema_docs['logical_model']:
                schema_links = ""
                html_file = html_module.escape(schema_doc.get('html_file', '#'))
                schema_file = html_module.escape(schema_doc.get('schema_file', ''))
                openapi_file = html_module.escape(schema_doc.get('openapi_file', ''))
                title = html_module.escape(schema_doc.get('title', 'Untitled'))
                description = html_module.escape(schema_doc.get('description', ''))
                if schema_doc.get('html_file'):
                    schema_links += f'<a href="{html_file}" class="schema-link fhir-link">FHIR Definition</a>'
                if schema_doc.get('schema_file'):
                    schema_links += f'<a href="{schema_file}" class="schema-link">JSON Schema</a>'
                if schema_doc.get('openapi_file'):
                    schema_links += f'<a href="{openapi_file}" class="schema-link">OpenAPI</a>'
                html_content += f"""
        <div class="schema-card">
            <h4><a href="{html_file}">{title}</a></h4>
            <p>{description}</p>
            <div class="schema-links">{schema_links}</div>
        </div>
"""
            html_content += """
    </div>
"""

        # Add API Endpoints section
        if enumeration_docs:
            html_content += """
    <h2>API Endpoints</h2>
    
    <p>These endpoints provide lists of all available schemas and vocabularies of each type:</p>
    
    <div class="enumeration-endpoints">
"""
            # Add schema enumeration endpoints with proper endpoint listings
            for enum_doc in enumeration_docs:
                if enum_doc['type'] == 'enumeration-valueset':
                    # List ValueSet schemas in this enumeration
                    valueset_list = ""
                    for schema_doc in schema_docs['valueset']:
                        schema_name = schema_doc['schema_file'].replace('.schema.json', '')
                        valueset_list += f"""
                    <li><a href="{schema_doc['schema_file']}">{schema_name}.schema.json</a> - JSON Schema for {schema_doc['title']}</li>"""
                        # Add JSON-LD if available
                        if schema_doc.get('jsonld_file'):
                            jsonld_name = schema_doc['jsonld_file'].replace('.jsonld', '')
                            valueset_list += f"""
                    <li><a href="{schema_doc['jsonld_file']}">{jsonld_name}.jsonld</a> - JSON-LD vocabulary for {schema_doc['title']}</li>"""
                    
                    html_content += f"""
        <div class="endpoint-card">
            <h4><a href="{enum_doc['html_file']}">{enum_doc['title']}</a></h4>
            <p>{enum_doc['description']}</p>
            <div class="endpoint-list">
                <h5>Available Endpoints:</h5>
                <ul>{valueset_list}
                </ul>
            </div>
        </div>
"""
                elif enum_doc['type'] == 'enumeration-logicalmodel':
                    # List LogicalModel schemas in this enumeration
                    logicalmodel_list = ""
                    for schema_doc in schema_docs['logical_model']:
                        schema_name = schema_doc['schema_file'].replace('.schema.json', '')
                        logicalmodel_list += f"""
                    <li><a href="{schema_doc['schema_file']}">{schema_name}.schema.json</a> - JSON Schema for {schema_doc['title']}</li>"""
                    
                    html_content += f"""
        <div class="endpoint-card">
            <h4><a href="{enum_doc['html_file']}">{enum_doc['title']}</a></h4>
            <p>{enum_doc['description']}</p>
            <div class="endpoint-list">
                <h5>Available Endpoints:</h5>
                <ul>{logicalmodel_list}
                </ul>
            </div>
        </div>
"""
            
            html_content += """
    </div>
"""
        
        html_content += """
</div>

<style>
/* DAK API Hub styling that integrates with IG theme */
.dak-api-hub {
    margin: 1rem 0;
}

.enumeration-endpoints, .schema-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1rem;
    margin: 1rem 0;
}

.endpoint-card, .schema-card {
    border: 1px solid #dee2e6;
    border-radius: 4px;
    padding: 1rem;
    background: #f8f9fa;
    transition: box-shadow 0.2s ease;
}

.endpoint-card:hover, .schema-card:hover {
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.endpoint-card h4, .schema-card h4 {
    margin: 0 0 0.5rem 0;
    color: #00477d;
}

.endpoint-card h4 a, .schema-card h4 a {
    color: #00477d;
    text-decoration: none;
}

.endpoint-card h4 a:hover, .schema-card h4 a:hover {
    color: #0070A1;
    text-decoration: underline;
}

.endpoint-card p, .schema-card p {
    margin: 0 0 0.5rem 0;
    color: #6c757d;
    font-size: 0.9rem;
}

.endpoint-list {
    margin-top: 1rem;
    padding-top: 1rem;
    border-top: 1px solid #dee2e6;
}

.endpoint-list h5 {
    margin: 0 0 0.5rem 0;
    color: #00477d;
    font-size: 0.9rem;
    font-weight: 600;
}

.endpoint-list ul {
    margin: 0;
    padding-left: 1.2rem;
    list-style-type: disc;
}

.endpoint-list li {
    margin: 0.25rem 0;
    font-size: 0.85rem;
    line-height: 1.4;
}

.endpoint-list a {
    color: #17a2b8;
    text-decoration: none;
    font-family: monospace;
    font-weight: 500;
}

.endpoint-list a:hover {
    color: #138496;
    text-decoration: underline;
}

.schema-links {
    margin: 0.75rem 0 0 0;
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
}

.schema-link {
    display: inline-block;
    background-color: #17a2b8;
    color: white;
    padding: 0.25rem 0.5rem;
    border-radius: 3px;
    text-decoration: none;
    font-size: 0.8rem;
    font-weight: 500;
    transition: background-color 0.2s ease;
}

.schema-link:hover {
    background-color: #138496;
    color: white;
    text-decoration: none;
}

.schema-link.fhir-link {
    background-color: #28a745;
}

.schema-link.fhir-link:hover {
    background-color: #218838;
}

.usage-info {
    background: #e7f3ff;
    border: 1px solid #b8daff;
    border-radius: 4px;
    padding: 1.5rem;
    margin: 1.5rem 0;
}

.usage-info h3 {
    color: #00477d;
    margin-top: 1rem;
}

.usage-info h3:first-child {
    margin-top: 0;
}

.usage-info ul {
    margin: 0.5rem 0;
}

.usage-info li {
    margin: 0.25rem 0;
}

/* JSON-LD specific styling */
.jsonld-list {
    margin: 0.75rem 0 0 0;
    padding: 0.75rem;
    background: #fff;
    border: 1px solid #e1ecf4;
    border-radius: 4px;
}

.jsonld-item {
    display: flex;
    flex-direction: column;
    margin: 0.5rem 0;
    padding: 0.5rem;
    border-left: 3px solid #17a2b8;
    background: #f8f9fa;
}

.jsonld-item:last-child {
    margin-bottom: 0;
}

.jsonld-link {
    font-weight: 600;
    color: #17a2b8;
    text-decoration: none;
    margin-bottom: 0.25rem;
}

.jsonld-link:hover {
    color: #138496;
    text-decoration: underline;
}

.jsonld-description {
    font-size: 0.85rem;
    color: #6c757d;
    font-style: italic;
}
</style>

<hr>

<p><em>This documentation hub is automatically generated from the available schema and API definitions.</em></p>
<!-- DAK_API_HUB_END -->
"""
        
        return html_content

    def _generate_swagger_ui_html(self, swagger_urls: List[Dict], existing_content: Optional[str] = None) -> str:
        """
        Generate a self-contained Swagger UI HTML page.

        Args:
            swagger_urls: List of {'url': ..., 'name': ...} dicts for Swagger UI.
            existing_content: Optional HTML content to display above the Swagger UI.

        Returns:
            Complete HTML page as a string.
        """
        urls_json = json.dumps(swagger_urls, indent=2)

        existing_section = ""
        if existing_content:
            existing_section = f"""
  <div class="existing-api-content">
    {existing_content}
  </div>
  <hr>
"""

        if swagger_urls:
            first_url = swagger_urls[0]['url']
            swagger_section = f"""
  <div id="definition-selector-bar">
    <label for="definition-select">Select a definition:</label>
    <select id="definition-select" onchange="switchDefinition(this.value)">
    </select>
  </div>
  <div id="swagger-ui"></div>
  <script src="https://unpkg.com/swagger-ui-dist@5.11.0/swagger-ui-bundle.js"></script>
  <script>
  var swaggerUrls = {urls_json};
  var ui;
  window.onload = function() {{
    var select = document.getElementById('definition-select');
    swaggerUrls.forEach(function(item, idx) {{
      var opt = document.createElement('option');
      opt.value = item.url;
      opt.textContent = item.name;
      select.appendChild(opt);
    }});
    ui = SwaggerUIBundle({{
      url: "{first_url}",
      dom_id: '#swagger-ui',
      presets: [SwaggerUIBundle.presets.apis],
      layout: "BaseLayout"
    }});
  }};
  function switchDefinition(url) {{
    ui.specActions.updateUrl(url);
    ui.specActions.download(url);
  }}
  </script>
"""
        else:
            swagger_section = """
  <p><em>No API specifications available. Add OpenAPI specification files to the
  <code>input/openapi</code> directory or generate schemas through the DAK pipeline.</em></p>
"""

        return f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <title>OpenAPI Documentation - SMART Base</title>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css"
          href="https://unpkg.com/swagger-ui-dist@5.11.0/swagger-ui.css">
    <style>
      body {{ margin: 0; padding: 0; font-family: Arial, Helvetica, sans-serif; }}
      /* WHO-styled header bar */
      .who-header {{
        background-color: #00477d;
        color: #ffffff;
        padding: 0.6rem 1.5rem;
        display: flex;
        align-items: center;
        gap: 1.5rem;
        font-size: 1rem;
        font-weight: 600;
        letter-spacing: 0.01em;
      }}
      .who-header a.home-link {{
        color: #ffffff;
        text-decoration: none;
        font-size: 0.9rem;
        font-weight: 600;
        border: 1px solid rgba(255,255,255,0.6);
        padding: 0.25rem 0.75rem;
        border-radius: 3px;
        transition: background-color 0.2s ease;
      }}
      .who-header a.home-link:hover {{
        background-color: rgba(255,255,255,0.15);
        text-decoration: none;
      }}
      .who-header .header-title {{
        flex: 1;
      }}
      /* Definition selector bar below the header */
      #definition-selector-bar {{
        background-color: #0070a1;
        color: #ffffff;
        padding: 0.5rem 1.5rem;
        display: flex;
        align-items: center;
        gap: 0.75rem;
        font-size: 0.9rem;
        flex-wrap: wrap;
      }}
      #definition-selector-bar label {{
        font-weight: 600;
        white-space: nowrap;
      }}
      #definition-select {{
        font-size: 0.9rem;
        padding: 0.25rem 0.5rem;
        border-radius: 3px;
        border: 1px solid rgba(255,255,255,0.6);
        background-color: #ffffff;
        color: #00477d;
        min-width: 200px;
        max-width: 100%;
        flex: 1;
      }}
      /* Hide Swagger UI topbar entirely */
      .swagger-ui .topbar {{
        display: none;
      }}
      .existing-api-content {{ padding: 1rem 2rem; }}
    </style>
  </head>
  <body>
  <div class="who-header">
    <a href="../index.html" class="home-link">&#8962; Home</a>
    <span class="header-title">SMART Base &mdash; OpenAPI Documentation</span>
  </div>
{existing_section}{swagger_section}
  </body>
</html>"""

    def generate_openapi_index_html(self, output_dir: str,
                                    openapi_input_dirs: Union[str, List[str]],
                                    schema_docs: Dict[str, List[Dict]],
                                    existing_openapi_html_content: Optional[str] = None) -> Optional[str]:
        """
        Generate output/openapi/index.html with Swagger UI, combining:
          1. Generated schema OpenAPI specs from the output directory.
          2. External OpenAPI specs copied from each directory in openapi_input_dirs (if present).
          3. Optional existing HTML content extracted from the first index.html found.

        Args:
            output_dir: IG output directory.
            openapi_input_dirs: One or more source directories for external OpenAPI specs
                                (e.g. ``input/openapi``, ``input/images/openapi``).
                                Accepts either a single string or a list of strings.
                                Directories that do not exist are silently skipped.
            schema_docs: Dictionary with schema documentation info.
            existing_openapi_html_content: Existing HTML content from an index.html found in
                                           one of the input directories.

        Returns:
            Path to the generated index.html, or None if generation failed.
        """
        import shutil

        # Normalise to a list so the rest of the code is uniform
        if isinstance(openapi_input_dirs, str):
            openapi_input_dirs = [openapi_input_dirs]

        try:
            openapi_output_dir = os.path.join(output_dir, "openapi")
            os.makedirs(openapi_output_dir, exist_ok=True)
            self.logger.info(f"Created output OpenAPI directory: {openapi_output_dir}")

            swagger_urls: List[Dict] = []

            # Add generated schema OpenAPI specs (parent output dir, referenced with ../)
            for schema_doc in schema_docs.get('valueset', []):
                if schema_doc.get('openapi_file'):
                    swagger_urls.append({
                        'url': f"../{schema_doc['openapi_file']}",
                        'name': schema_doc['title']
                    })

            for schema_doc in schema_docs.get('logical_model', []):
                if schema_doc.get('openapi_file'):
                    swagger_urls.append({
                        'url': f"../{schema_doc['openapi_file']}",
                        'name': schema_doc['title']
                    })

            # Copy external OpenAPI files from each input directory and add to the spec list.
            # Files are de-duplicated by filename (first directory wins).
            # All OpenAPI spec files and their supporting assets (e.g. referenced schemas) are
            # copied so that relative references within the specs continue to resolve correctly.
            seen_filenames: set = set()
            for openapi_input_dir in openapi_input_dirs:
                if not os.path.exists(openapi_input_dir):
                    self.logger.info(f"No external OpenAPI directory found at: {openapi_input_dir}")
                    continue
                self.logger.info(f"Scanning external OpenAPI directory: {openapi_input_dir}")
                for filename in sorted(os.listdir(openapi_input_dir)):
                    src_path = os.path.join(openapi_input_dir, filename)
                    if not os.path.isfile(src_path) or filename.lower() == 'index.html':
                        continue
                    # Only copy recognised spec and asset file types
                    ext = os.path.splitext(filename)[1].lower()
                    if ext not in ('.json', '.yaml', '.yml', '.png', '.svg', '.css', '.js'):
                        self.logger.debug(f"Skipping non-asset file: {filename}")
                        continue
                    if filename in seen_filenames:
                        self.logger.debug(f"Skipping duplicate file (already copied): {filename}")
                        continue
                    seen_filenames.add(filename)
                    dst_path = os.path.join(openapi_output_dir, filename)
                    shutil.copy2(src_path, dst_path)
                    self.logger.info(f"Copied external OpenAPI file: {filename}")
                    if ext in ('.json', '.yaml', '.yml'):
                        spec_name = os.path.splitext(filename)[0]
                        swagger_urls.append({'url': f"./{filename}", 'name': spec_name})

            html = self._generate_swagger_ui_html(swagger_urls, existing_openapi_html_content)

            index_path = os.path.join(openapi_output_dir, "index.html")
            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(html)

            self.logger.info(f"Generated OpenAPI index at: {index_path}")
            return index_path

        except Exception as e:
            self.logger.error(f"Error generating OpenAPI index HTML: {e}")
            import traceback
            self.logger.error(traceback.format_exc())
            return None

    def post_process_dak_api_html(self, output_dir: str, schema_docs: Dict[str, List[Dict]], openapi_docs: List[Dict], enumeration_docs: List[Dict] = None, jsonld_docs: List[Dict] = None, existing_openapi_html_content: Optional[str] = None) -> bool:
        """
        Post-process the dak-api.html file to inject DAK API content.
        
        Args:
            output_dir: Directory containing the generated HTML files
            schema_docs: Dictionary with schema documentation info
            openapi_docs: List of OpenAPI documentation info
            enumeration_docs: List of enumeration endpoint documentation info
            jsonld_docs: List of JSON-LD vocabulary documentation info
            existing_openapi_html_content: Existing HTML content from input/images/openapi/index.html
            
        Returns:
            True if successful, False otherwise
        """
        try:
            self.logger.info("Starting DAK API hub post-processing...")
            
            if enumeration_docs is None:
                enumeration_docs = []
            if jsonld_docs is None:
                jsonld_docs = []
            
            self.logger.info(f"Content to include in hub:")
            self.logger.info(f"  ValueSet schemas: {len(schema_docs['valueset'])}")
            self.logger.info(f"  Logical Model schemas: {len(schema_docs['logical_model'])}")
            self.logger.info(f"  Enumeration endpoints: {len(enumeration_docs)}")
            self.logger.info(f"  JSON-LD vocabularies: {len(jsonld_docs)}")
            self.logger.info(f"  OpenAPI docs: {len(openapi_docs)}")
            
            # Check if dak-api.html exists
            dak_api_html_path = os.path.join(output_dir, "dak-api.html")
            if not os.path.exists(dak_api_html_path):
                self.logger.error(f"dak-api.html not found at {dak_api_html_path}")
                return False
            
            self.logger.info(f"Found dak-api.html template at: {dak_api_html_path}")
            
            # Generate the HTML content for the hub
            self.logger.info("Generating hub HTML content...")
            hub_content = self.generate_hub_html_content(schema_docs, openapi_docs, enumeration_docs, jsonld_docs, existing_openapi_html_content)
            self.logger.info(f"Generated hub content length: {len(hub_content)} characters")
            
            if len(hub_content) < 100:
                self.logger.warning("Generated hub content seems very short, this might indicate an issue")
                self.logger.info(f"Hub content preview: {hub_content[:200]}...")
            
            # Create HTML processor to inject content
            self.logger.info("Creating HTML processor for content injection...")
            html_processor = HTMLProcessor(self.logger, output_dir)
            
            # Inject content into dak-api.html
            self.logger.info("Injecting content into dak-api.html...")
            success = html_processor.inject_content_at_comment_marker(dak_api_html_path, hub_content)
            
            if success:
                self.logger.info(f"✅ Successfully post-processed DAK API hub: {dak_api_html_path}")
                # Verify the final file
                final_size = os.path.getsize(dak_api_html_path)
                self.logger.info(f"Final dak-api.html file size: {final_size} bytes")
            else:
                self.logger.error("❌ Failed to inject content into dak-api.html")
            
            return success
            
        except Exception as e:
            self.logger.error(f"Error post-processing DAK API hub: {e}")
            import traceback
            self.logger.error(f"Traceback: {traceback.format_exc()}")
            return False


def main():
    """Main entry point for the script."""
    logger = setup_logging()
    
    # Parse command line arguments first
    if len(sys.argv) == 1:
        output_dir = "output"
        openapi_dir = "input/openapi"  # Optional: externally defined APIs (e.g. smart-trust IG)
    elif len(sys.argv) == 2:
        output_dir = sys.argv[1]
        openapi_dir = "input/openapi"  # Optional: externally defined APIs (e.g. smart-trust IG)
    else:
        output_dir = sys.argv[1]
        openapi_dir = sys.argv[2]
    
    logger.info(f"Output directory: {output_dir}")
    logger.info(f"OpenAPI directory: {openapi_dir}")
    
    # Initialize QA reporter for post-processing
    qa_reporter = QAReporter("postprocessing")
    qa_reporter.add_success("Starting generate_dak_api_hub.py post-processing")
    qa_reporter.add_success(f"Configured directories - Output: {output_dir}, OpenAPI: {openapi_dir}")
    
    # Load existing FHIR IG publisher QA file if it exists
    qa_output_path = os.path.join(output_dir, "qa.json")
    if qa_reporter.load_existing_ig_qa(qa_output_path):
        qa_reporter.add_success("Loaded existing FHIR IG publisher QA file for merging")
    else:
        qa_reporter.add_warning("No existing FHIR IG publisher QA file found - will create new one")
    
    # Check for and merge preprocessing QA report from protected location first
    preprocessing_qa_path = "input/temp/qa_preprocessing.json"
    if os.path.exists(preprocessing_qa_path):
        try:
            with open(preprocessing_qa_path, 'r', encoding='utf-8') as f:
                preprocessing_report = json.load(f)
            qa_reporter.merge_preprocessing_report(preprocessing_report)
            qa_reporter.add_success("Merged preprocessing QA report from input/temp/")
            logger.info("Successfully merged preprocessing QA report from input/temp/")
        except Exception as e:
            qa_reporter.add_warning(f"Failed to merge preprocessing QA report from input/temp/: {e}")
            logger.warning(f"Failed to merge preprocessing QA report from input/temp/: {e}")
    else:
        # Fallback to /tmp location
        temp_qa_path = "/tmp/qa_preprocessing.json"
        if os.path.exists(temp_qa_path):
            try:
                with open(temp_qa_path, 'r', encoding='utf-8') as f:
                    preprocessing_report = json.load(f)
                qa_reporter.merge_preprocessing_report(preprocessing_report)
                qa_reporter.add_success("Merged preprocessing QA report from /tmp/")
                logger.info("Successfully merged preprocessing QA report from /tmp/")
            except Exception as e:
                qa_reporter.add_warning(f"Failed to merge preprocessing QA report from /tmp/: {e}")
                logger.warning(f"Failed to merge preprocessing QA report from /tmp/: {e}")
        else:
            qa_reporter.add_warning("No preprocessing QA report found in either input/temp/ or /tmp/")
            logger.warning("No preprocessing QA report found in either input/temp/ or /tmp/")
    
    # Check for and merge component QA reports from both locations
    component_qa_files = [
        ("input/temp/qa_valueset_schemas.json", "/tmp/qa_valueset_schemas.json", "ValueSet schema generation"),
        ("input/temp/qa_logical_model_schemas.json", "/tmp/qa_logical_model_schemas.json", "Logical Model schema generation"), 
        ("input/temp/qa_jsonld_vocabularies.json", "/tmp/qa_jsonld_vocabularies.json", "JSON-LD vocabulary generation")
    ]
    
    for protected_path, temp_path, component_name in component_qa_files:
        # Try protected location first
        qa_file_path = protected_path if os.path.exists(protected_path) else temp_path
        
        if os.path.exists(qa_file_path):
            try:
                with open(qa_file_path, 'r', encoding='utf-8') as f:
                    component_report = json.load(f)
                qa_reporter.merge_preprocessing_report(component_report)
                qa_reporter.add_success(f"Merged {component_name} QA report from {qa_file_path}")
                logger.info(f"Successfully merged {component_name} QA report from {qa_file_path}")
            except Exception as e:
                qa_reporter.add_warning(f"Failed to merge {component_name} QA report: {e}")
                logger.warning(f"Failed to merge {component_name} QA report: {e}")
        else:
            qa_reporter.add_warning(f"No {component_name} QA report found")
            logger.info(f"No {component_name} QA report found at {protected_path} or {temp_path}")
    
    # Check if output directory exists and has content
    qa_reporter.add_file_expected(output_dir)
    if os.path.exists(output_dir):
        logger.info(f"Output directory exists with {len(os.listdir(output_dir))} items")
        qa_reporter.add_success(f"Output directory exists with {len(os.listdir(output_dir))} items")
        # Log a few sample files to help debugging
        all_files = os.listdir(output_dir)
        sample_files = all_files[:10]  # Show first 10 files
        logger.info(f"Sample files in output directory: {sample_files}")
        qa_reporter.add_success("Output directory contents sampled", {"sample_files": sample_files})
    else:
        logger.error(f"Output directory does not exist: {output_dir}")
        qa_reporter.add_error(f"Output directory does not exist: {output_dir}")
        
        # Save QA report even on failure
        qa_report = qa_reporter.finalize_report("failed")
        qa_output_path = os.path.join("output", "qa.json")  # Fallback location
        try:
            os.makedirs(os.path.dirname(qa_output_path), exist_ok=True)
            qa_reporter.save_to_file(qa_output_path)
        except:
            pass  # Don't fail if we can't save QA report
        
        sys.exit(1)
    
    # Initialize components
    logger.info("Initializing DAK API components...")
    qa_reporter.add_success("Initializing DAK API components")
    
    try:
        schema_detector = SchemaDetector(logger)
        openapi_detector = OpenAPIDetector(logger)
        openapi_wrapper = OpenAPIWrapper(logger)
        schema_doc_renderer = SchemaDocumentationRenderer(logger)
        hub_generator = DAKApiHubGenerator(logger)
        html_processor = HTMLProcessor(logger, output_dir)
        logger.info("Components initialized successfully")
        qa_reporter.add_success("All components initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize components: {e}")
        qa_reporter.add_error(f"Failed to initialize components: {e}")
        
        # Save QA report even on failure
        qa_report = qa_reporter.finalize_report("failed")
        qa_output_path = os.path.join(output_dir, "qa.json")
        qa_reporter.save_to_file(qa_output_path)
        sys.exit(1)
    
    # Find schema files
    logger.info("=== SCHEMA FILE DETECTION PHASE ===")
    qa_reporter.add_success("Starting schema file detection phase")
    
    try:
        schemas = schema_detector.find_schema_files(output_dir)
        logger.info(f"Schema detection completed - ValueSet: {len(schemas['valueset'])}, LogicalModel: {len(schemas['logical_model'])}, Other: {len(schemas['other'])}")
        qa_reporter.add_success("Schema detection completed", {
            "valueset_schemas": len(schemas['valueset']),
            "logical_model_schemas": len(schemas['logical_model']),
            "other_schemas": len(schemas['other'])
        })
        
        # Record found schema files
        for schema_path in schemas['valueset']:
            qa_reporter.add_file_processed(schema_path, "valueset_schema_detected")
        for schema_path in schemas['logical_model']:
            qa_reporter.add_file_processed(schema_path, "logical_model_schema_detected")
        for schema_path in schemas['other']:
            qa_reporter.add_file_processed(schema_path, "other_schema_detected")
            
    except Exception as e:
        logger.error(f"Schema detection failed: {e}")
        qa_reporter.add_error(f"Schema detection failed: {e}")
        schemas = {'valueset': [], 'logical_model': [], 'other': []}
    
    # Find JSON-LD vocabulary files
    logger.info("=== JSON-LD FILE DETECTION PHASE ===")
    jsonld_files = schema_detector.find_jsonld_files(output_dir)
    logger.info(f"JSON-LD detection completed - found {len(jsonld_files)} files")
    
    # Find existing OpenAPI files
    logger.info("=== OPENAPI FILE DETECTION PHASE ===")
    openapi_files = openapi_detector.find_openapi_files(openapi_dir)
    logger.info(f"OpenAPI detection completed - found {len(openapi_files)} files in source directory")

    # Also check the legacy input/images/openapi location
    legacy_openapi_dir = "input/images/openapi"
    legacy_openapi_files = openapi_detector.find_openapi_files(legacy_openapi_dir)
    logger.info(f"Found {len(legacy_openapi_files)} existing OpenAPI files in legacy directory")
    
    # Also check for OpenAPI files in output directory (copied by IG publisher)
    output_openapi_dir = os.path.join(output_dir, "images", "openapi")
    output_openapi_files = openapi_detector.find_openapi_files(output_openapi_dir)
    logger.info(f"Found {len(output_openapi_files)} existing OpenAPI files in output directory")
    
    # Extract existing HTML content from OpenAPI documentation
    # Check all candidate directories in priority order; use the first one found.
    logger.info("=== EXISTING OPENAPI HTML CONTENT DETECTION ===")
    existing_openapi_html_content = None
    for _html_dir in [openapi_dir, legacy_openapi_dir, output_openapi_dir]:
        existing_openapi_html_content = openapi_detector.find_existing_html_content(_html_dir)
        if existing_openapi_html_content:
            logger.info(f"Found existing OpenAPI HTML content in: {_html_dir}")
            break
    if not existing_openapi_html_content:
        logger.info("No existing OpenAPI HTML content found")
    
    # Generate schema documentation
    logger.info("=== SCHEMA DOCUMENTATION GENERATION PHASE ===")
    schema_docs = {
        'valueset': [],
        'logical_model': []
    }
    
    # Check if dak-api.html exists (required as template)
    dak_api_html_path = os.path.join(output_dir, "dak-api.html")
    logger.info(f"Checking for dak-api.html template at: {dak_api_html_path}")
    
    # Log some debug information about the output directory
    logger.info(f"Current working directory: {os.getcwd()}")
    logger.info(f"Output directory absolute path: {os.path.abspath(output_dir)}")
    if os.path.exists(output_dir):
        all_files = os.listdir(output_dir)
        html_files = [f for f in all_files if f.endswith('.html')]
        logger.info(f"Total files in output directory: {len(all_files)}")
        logger.info(f"HTML files in output directory: {len(html_files)} found")
        if len(html_files) > 0:
            logger.info(f"Sample HTML files: {html_files[:5]}")  # Show first 5
        if 'dak-api.html' in all_files:
            logger.info("✅ Found dak-api.html in directory listing")
        else:
            logger.warning("⚠️ dak-api.html NOT found in directory listing")
            logger.info(f"Files containing 'dak': {[f for f in all_files if 'dak' in f.lower()]}")
    else:
        logger.error(f"❌ Output directory does not exist: {output_dir}")
    
    # Continue processing even if dak-api.html is not found initially
    # The IG publisher might have generated it in a different location or named it differently
    if not os.path.exists(dak_api_html_path):
        logger.warning(f"⚠️ dak-api.html not found at expected location: {dak_api_html_path}")
        
        # Try to find dak-api.html in the output directory with different approaches
        found_dak_api = False
        if os.path.exists(output_dir):
            all_files = os.listdir(output_dir)
            for file in all_files:
                if file == 'dak-api.html':
                    found_dak_api = True
                    dak_api_html_path = os.path.join(output_dir, file)
                    logger.info(f"✅ Found dak-api.html at: {dak_api_html_path}")
                    break
        
        if not found_dak_api:
            logger.error(f"❌ Cannot find dak-api.html in output directory. Available HTML files:")
            if os.path.exists(output_dir):
                html_files = [f for f in os.listdir(output_dir) if f.endswith('.html')]
                for html_file in html_files[:10]:  # Show first 10
                    logger.error(f"  - {html_file}")
            logger.error("Make sure the IG publisher ran first and created dak-api.html from the dak-api.md placeholder.")
            logger.error("Exiting with error code 1")
            sys.exit(1)
    else:
        logger.info("✅ dak-api.html template found successfully")
    
    # Get file size for debugging
    if os.path.exists(dak_api_html_path):
        template_size = os.path.getsize(dak_api_html_path)
        logger.info(f"Template file size: {template_size} bytes")
        
        # Check if the file has the DAK_API_CONTENT comment marker for injection
        try:
            with open(dak_api_html_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
            if '<!-- DAK_API_CONTENT -->' in html_content:
                logger.info("✅ Found DAK_API_CONTENT comment marker in dak-api.html for content injection")
            else:
                logger.warning("⚠️ No DAK_API_CONTENT comment marker found in dak-api.html - content injection may fail")
                # Log a sample of the content to help debug
                sample_content = html_content[:500] if len(html_content) > 500 else html_content
                logger.info(f"Sample content from dak-api.html: {sample_content}")
        except Exception as e:
            logger.error(f"Error reading dak-api.html for validation: {e}")
    else:
        logger.error(f"dak-api.html path does not exist: {dak_api_html_path}")
    
    # Process ValueSet schemas (collect metadata and generate OpenAPI wrappers)
    logger.info(f"Processing {len(schemas['valueset'])} ValueSet schemas...")
    for i, schema_path in enumerate(schemas['valueset'], 1):
        logger.info(f"Processing ValueSet schema {i}/{len(schemas['valueset'])}: {schema_path}")
        try:
            # Load schema to get metadata
            with open(schema_path, 'r', encoding='utf-8') as f:
                schema = json.load(f)
            
            schema_filename = os.path.basename(schema_path)
            schema_name = schema_filename.replace('.schema.json', '')
            logger.info(f"  Schema name: {schema_name}")
            logger.info(f"  Schema title: {schema.get('title', 'No title')}")
            
            # Generate OpenAPI wrapper for this ValueSet schema
            openapi_wrapper_path = openapi_wrapper.create_wrapper_for_schema(schema_path, 'valueset', output_dir)
            if openapi_wrapper_path:
                logger.info(f"  ✅ Created OpenAPI wrapper: {openapi_wrapper_path}")
            else:
                logger.warning(f"  ⚠️ Failed to create OpenAPI wrapper for {schema_name}")
            
            # Collect metadata for the hub documentation
            title = schema.get('title', f"{schema_name} Schema Documentation")
            
            # Individual schemas should link to their IG-generated HTML files
            html_filename = f"{schema_name}.html"
            
            # Collect additional file references
            schema_filename = os.path.basename(schema_path)
            displays_filename = f"{schema_name}.displays.json"
            openapi_filename = f"{schema_name}.openapi.json"
            jsonld_filename = f"{schema_name}.jsonld"
            
            # Check if additional files exist
            displays_path = os.path.join(output_dir, displays_filename)
            openapi_path = os.path.join(output_dir, openapi_filename)
            jsonld_path = os.path.join(output_dir, jsonld_filename)
            
            schema_doc_entry = {
                'title': title,
                'description': schema.get('description', 'ValueSet schema documentation'),
                'html_file': html_filename,
                'schema_file': schema_filename
            }
            
            # Add displays file if it exists
            if os.path.exists(displays_path):
                schema_doc_entry['displays_file'] = displays_filename
                logger.info(f"  Found displays file: {displays_filename}")
            
            # Add OpenAPI file if it exists
            if os.path.exists(openapi_path):
                schema_doc_entry['openapi_file'] = openapi_filename
                logger.info(f"  Found OpenAPI file: {openapi_filename}")
                
            # Add JSON-LD file if it exists  
            if os.path.exists(jsonld_path):
                schema_doc_entry['jsonld_file'] = jsonld_filename
                logger.info(f"  Found JSON-LD file: {jsonld_filename}")
            
            schema_docs['valueset'].append(schema_doc_entry)
            
            logger.info(f"  ✅ Added ValueSet schema to hub documentation: {schema_name}")
                
        except Exception as e:
            logger.error(f"  ❌ Error processing ValueSet schema {schema_path}: {e}")
            import traceback
            logger.error(f"  Traceback: {traceback.format_exc()}")
    
    # Process Logical Model schemas (collect metadata and generate OpenAPI wrappers)
    logger.info(f"Processing {len(schemas['logical_model'])} Logical Model schemas...")
    for i, schema_path in enumerate(schemas['logical_model'], 1):
        logger.info(f"Processing Logical Model schema {i}/{len(schemas['logical_model'])}: {schema_path}")
        try:
            # Load schema to get metadata
            with open(schema_path, 'r', encoding='utf-8') as f:
                schema = json.load(f)
            
            schema_filename = os.path.basename(schema_path)
            schema_name = schema_filename.replace('.schema.json', '')
            logger.info(f"  Schema name: {schema_name}")
            logger.info(f"  Schema title: {schema.get('title', 'No title')}")
            
            # Generate OpenAPI wrapper for this Logical Model schema
            openapi_wrapper_path = openapi_wrapper.create_wrapper_for_schema(schema_path, 'logical_model', output_dir)
            if openapi_wrapper_path:
                logger.info(f"  ✅ Created OpenAPI wrapper: {openapi_wrapper_path}")
            else:
                logger.warning(f"  ⚠️ Failed to create OpenAPI wrapper for {schema_name}")
            
            # Collect metadata for the hub documentation
            title = schema.get('title', f"{schema_name} Schema Documentation")
            
            # Individual schemas should link to their IG-generated HTML files
            html_filename = f"{schema_name}.html"
            
            # Collect additional file references
            schema_filename = os.path.basename(schema_path)
            displays_filename = f"{schema_name}.displays.json"
            openapi_filename = f"{schema_name}.openapi.json"
            
            # Check if additional files exist
            displays_path = os.path.join(output_dir, displays_filename)
            openapi_path = os.path.join(output_dir, openapi_filename)
            
            schema_doc_entry = {
                'title': title,
                'description': schema.get('description', 'Logical Model schema documentation'),
                'html_file': html_filename,
                'schema_file': schema_filename
            }
            
            # Add displays file if it exists
            if os.path.exists(displays_path):
                schema_doc_entry['displays_file'] = displays_filename
                logger.info(f"  Found displays file: {displays_filename}")
            
            # Add OpenAPI file if it exists
            if os.path.exists(openapi_path):
                schema_doc_entry['openapi_file'] = openapi_filename
                logger.info(f"  Found OpenAPI file: {openapi_filename}")
            
            schema_docs['logical_model'].append(schema_doc_entry)
            
            logger.info(f"  ✅ Added Logical Model schema to hub documentation: {schema_name}")
                
        except Exception as e:
            logger.error(f"  ❌ Error processing Logical Model schema {schema_path}: {e}")
            import traceback
            logger.error(f"  Traceback: {traceback.format_exc()}")
    
    # Initialize OpenAPI docs list (will be populated after generation)
    openapi_docs = []
    
    # Create enumeration endpoints for ValueSets and LogicalModels
    logger.info("=== ENUMERATION ENDPOINT CREATION PHASE ===")
    enumeration_docs = []
    
    # Create ValueSets enumeration endpoint if we have ValueSet schemas
    if schemas['valueset']:
        logger.info(f"Creating ValueSets enumeration endpoint for {len(schemas['valueset'])} schemas...")
        valueset_enum_path = hub_generator.create_enumeration_schema('valueset', schemas['valueset'], output_dir)
        if valueset_enum_path:
            logger.info(f"Created ValueSets enumeration schema: {valueset_enum_path}")
            
            # Create OpenAPI wrapper for the enumeration endpoint
            enum_openapi_path = openapi_wrapper.create_enumeration_wrapper(valueset_enum_path, 'valueset', output_dir)
            if enum_openapi_path:
                logger.info(f"✅ Created ValueSets enumeration OpenAPI wrapper: {enum_openapi_path}")
            else:
                logger.warning("⚠️ Failed to create ValueSets enumeration OpenAPI wrapper")
            
            # Add to enumeration docs (IG publisher should create the HTML)
            enumeration_docs.append({
                'title': 'ValueSets.schema.json',
                'description': 'Enumeration of all available ValueSet schemas',
                'html_file': 'ValueSets-enumeration.html',  # This should be created by IG publisher
                'type': 'enumeration-valueset'
            })
            logger.info(f"✅ Added ValueSets enumeration to hub documentation")
        else:
            logger.error("❌ Failed to create ValueSets enumeration schema")
    else:
        logger.info("No ValueSet schemas found, skipping ValueSets enumeration endpoint")
    
    # Create LogicalModels enumeration endpoint if we have LogicalModel schemas  
    if schemas['logical_model']:
        logger.info(f"Creating LogicalModels enumeration endpoint for {len(schemas['logical_model'])} schemas...")
        logicalmodel_enum_path = hub_generator.create_enumeration_schema('logical_model', schemas['logical_model'], output_dir)
        if logicalmodel_enum_path:
            logger.info(f"Created LogicalModels enumeration schema: {logicalmodel_enum_path}")
            
            # Create OpenAPI wrapper for the enumeration endpoint
            enum_openapi_path = openapi_wrapper.create_enumeration_wrapper(logicalmodel_enum_path, 'logical_model', output_dir)
            if enum_openapi_path:
                logger.info(f"✅ Created LogicalModels enumeration OpenAPI wrapper: {enum_openapi_path}")
            else:
                logger.warning("⚠️ Failed to create LogicalModels enumeration OpenAPI wrapper")
            
            # Add to enumeration docs (IG publisher should create the HTML)
            enumeration_docs.append({
                'title': 'LogicalModels.schema.json',
                'description': 'Enumeration of all available Logical Model schemas',
                'html_file': 'LogicalModels-enumeration.html',  # This should be created by IG publisher
                'type': 'enumeration-logicalmodel'
            })
            logger.info(f"✅ Added LogicalModels enumeration to hub documentation")
        else:
            logger.error("❌ Failed to create LogicalModels enumeration schema")
    else:
        logger.info("No Logical Model schemas found, skipping LogicalModels enumeration endpoint")
    
    # Process JSON-LD vocabulary files
    logger.info("=== JSON-LD VOCABULARY PROCESSING PHASE ===")
    jsonld_docs = []
    logger.info(f"Processing {len(jsonld_files)} JSON-LD vocabulary files...")
    for i, jsonld_path in enumerate(jsonld_files, 1):
        logger.info(f"Processing JSON-LD vocabulary {i}/{len(jsonld_files)}: {jsonld_path}")
        try:
            # Load JSON-LD vocabulary to get metadata
            with open(jsonld_path, 'r', encoding='utf-8') as f:
                jsonld_vocab = json.load(f)
            
            jsonld_filename = os.path.basename(jsonld_path)
            logger.info(f"  Filename: {jsonld_filename}")
            
            # Extract title and description from the enumeration class in the @graph
            title = jsonld_filename
            description = "JSON-LD vocabulary for ValueSet enumeration"
            
            if '@graph' in jsonld_vocab and isinstance(jsonld_vocab['@graph'], list):
                logger.info(f"  Found @graph with {len(jsonld_vocab['@graph'])} items")
                for item in jsonld_vocab['@graph']:
                    if isinstance(item, dict) and item.get('type') == 'schema:Enumeration':
                        logger.info(f"  Found enumeration class: {item.get('id', 'no ID')}")
                        if 'name' in item:
                            title = f"{item['name']} JSON-LD Vocabulary"
                            logger.info(f"  Updated title to: {title}")
                        if 'comment' in item:
                            description = item['comment']
                            logger.info(f"  Updated description to: {description}")
                        break
            
            jsonld_docs.append({
                'title': title,
                'description': description,
                'filename': jsonld_filename
            })
            
            logger.info(f"  ✅ Added JSON-LD vocabulary to documentation: {jsonld_filename}")
            
        except Exception as e:
            logger.error(f"  ❌ Error processing JSON-LD vocabulary {jsonld_path}: {e}")
            import traceback
            logger.error(f"  Traceback: {traceback.format_exc()}")
    
    # Process all OpenAPI files (existing + generated) for OpenAPI documentation section
    logger.info("=== OPENAPI DOCUMENTATION COLLECTION PHASE ===")
    
    # Re-scan for all OpenAPI files now that generated wrappers exist
    generated_openapi_files = openapi_detector.find_openapi_files(output_dir)
    logger.info(f"Found {len(generated_openapi_files)} generated OpenAPI files in output directory")
    
    # Combine and deduplicate OpenAPI files by filename
    all_openapi_files = []
    seen_filenames = set()
    
    # Add generated files first (they take priority)
    for file_path in generated_openapi_files:
        filename = os.path.basename(file_path)
        if filename not in seen_filenames:
            all_openapi_files.append(file_path)
            seen_filenames.add(filename)
    
    # Add existing files from source directory if not already seen
    if openapi_files:
        for file_path in openapi_files:
            filename = os.path.basename(file_path)
            if filename not in seen_filenames:
                all_openapi_files.append(file_path)
                seen_filenames.add(filename)
        logger.info(f"Added {len([f for f in openapi_files if os.path.basename(f) not in seen_filenames])} new existing OpenAPI files from source")
    
    # Add existing files from output directory (copied by IG publisher) if not already seen
    if output_openapi_files:
        for file_path in output_openapi_files:
            filename = os.path.basename(file_path)
            if filename not in seen_filenames:
                all_openapi_files.append(file_path)
                seen_filenames.add(filename)
        logger.info(f"Added {len([f for f in output_openapi_files if os.path.basename(f) not in seen_filenames])} existing OpenAPI files from output")
    
    logger.info(f"Total unique OpenAPI files: {len(all_openapi_files)}")
    
    # Process all unique OpenAPI files for documentation
    for openapi_path in all_openapi_files:
        try:
            openapi_filename = os.path.basename(openapi_path)
            logger.info(f"Processing OpenAPI file: {openapi_filename}")
            
            # Determine the correct relative path based on file location
            if "images/openapi" in openapi_path:
                relative_path = f"images/openapi/{openapi_filename}"
            else:
                relative_path = openapi_filename
            
            # Create cleaner title from filename
            clean_name = openapi_filename.replace('.openapi.json', '').replace('.openapi.yaml', '').replace('.yaml', '').replace('.json', '')
            
            # Generate individual OpenAPI documentation by injecting into existing HTML
            logger.info(f"  Injecting OpenAPI documentation content for: {clean_name}")
            openapi_html_filename = schema_doc_renderer.inject_into_html(openapi_path, output_dir, f"{clean_name} API Documentation")
            if openapi_html_filename:
                logger.info(f"  ✅ Generated OpenAPI documentation: {openapi_html_filename}")
            else:
                logger.warning(f"  ⚠️ Failed to generate OpenAPI documentation for {clean_name}")
            
            openapi_docs.append({
                'title': f"{clean_name} API",
                'description': f"OpenAPI specification for {clean_name}",
                'file_path': relative_path,  # Direct link to JSON/YAML file
                'filename': openapi_filename,
                'html_file': openapi_html_filename if openapi_html_filename else None
            })
            
            logger.info(f"  ✅ Added to OpenAPI documentation: {clean_name}")
            
        except Exception as e:
            logger.error(f"  ❌ Error processing OpenAPI file {openapi_path}: {e}")
    
    logger.info(f"OpenAPI documentation collection completed - {len(openapi_docs)} unique files documented")
    
    # Log summary before hub generation
    logger.info("=== DOCUMENTATION SUMMARY ===")
    logger.info(f"ValueSet schema docs: {len(schema_docs['valueset'])}")
    logger.info(f"Logical Model schema docs: {len(schema_docs['logical_model'])}")
    logger.info(f"Enumeration endpoints: {len(enumeration_docs)}")
    logger.info(f"JSON-LD vocabularies: {len(jsonld_docs)}")
    logger.info(f"OpenAPI docs: {len(openapi_docs)}")
    
    qa_reporter.add_success("Documentation summary completed", {
        "valueset_schema_docs": len(schema_docs['valueset']),
        "logical_model_schema_docs": len(schema_docs['logical_model']),
        "enumeration_endpoints": len(enumeration_docs),
        "jsonld_vocabularies": len(jsonld_docs),
        "openapi_docs": len(openapi_docs)
    })
    
    total_content_items = len(schema_docs['valueset']) + len(schema_docs['logical_model']) + len(enumeration_docs) + len(jsonld_docs) + len(openapi_docs)
    if total_content_items == 0:
        logger.warning("⚠️ No content items found to document! The DAK API hub will be empty.")
        qa_reporter.add_warning("No content items found to document! The DAK API hub will be empty.")
    else:
        logger.info(f"Total content items to include in hub: {total_content_items}")
        qa_reporter.add_success(f"Total content items to include in hub: {total_content_items}")
    
    # Replace static pre-formatted source in all FHIR resource HTML pages with dynamic loaders
    logger.info("=== DYNAMIC SOURCE LOADING PHASE ===")
    try:
        dynamic_count = schema_doc_renderer.replace_static_source_with_dynamic_loading(output_dir)
        qa_reporter.add_success(f"Dynamic source loading applied to {dynamic_count} HTML files")
    except Exception as e:
        logger.warning(f"Dynamic source loading phase failed (non-fatal): {e}")

    # Post-process the DAK API hub
    logger.info("=== DAK API HUB POST-PROCESSING PHASE ===")
    qa_reporter.add_success("Starting DAK API hub post-processing phase")
    
    try:
        success = hub_generator.post_process_dak_api_html(output_dir, schema_docs, openapi_docs, enumeration_docs, jsonld_docs, existing_openapi_html_content)
        
        if success:
            total_docs = len(schema_docs['valueset']) + len(schema_docs['logical_model']) + len(openapi_docs) + len(enumeration_docs) + len(jsonld_docs)
            logger.info(f"🎉 Successfully post-processed DAK API hub with {total_docs} documentation pages")
            logger.info("=== FINAL SUMMARY ===")
            logger.info(f"✅ ValueSet schema pages: {len(schema_docs['valueset'])}")
            logger.info(f"✅ Logical Model schema pages: {len(schema_docs['logical_model'])}")
            logger.info(f"✅ Enumeration endpoint pages: {len(enumeration_docs)}")
            logger.info(f"✅ JSON-LD vocabulary references: {len(jsonld_docs)}")
            logger.info(f"✅ OpenAPI documentation pages: {len(openapi_docs)}")
            logger.info(f"✅ Total documentation pages: {total_docs}")
            
            qa_reporter.add_success("DAK API hub post-processing completed successfully", {
                "total_documentation_pages": total_docs,
                "valueset_pages": len(schema_docs['valueset']),
                "logical_model_pages": len(schema_docs['logical_model']),
                "enumeration_pages": len(enumeration_docs),
                "jsonld_references": len(jsonld_docs),
                "openapi_pages": len(openapi_docs)
            })
        else:
            logger.error("❌ Failed to post-process DAK API hub")
            qa_reporter.add_error("Failed to post-process DAK API hub - check detailed logs for specific errors")
            
    except Exception as e:
        logger.error(f"❌ Exception during DAK API hub post-processing: {e}")
        qa_reporter.add_error(f"Exception during DAK API hub post-processing: {e}")
        success = False

    # Generate unified OpenAPI documentation index (output/openapi/index.html)
    logger.info("=== OPENAPI INDEX GENERATION PHASE ===")
    try:
        openapi_index_path = hub_generator.generate_openapi_index_html(
            output_dir, [openapi_dir, legacy_openapi_dir], schema_docs, existing_openapi_html_content
        )
        if openapi_index_path:
            logger.info(f"✅ Generated OpenAPI index: {openapi_index_path}")
            qa_reporter.add_success(f"Generated OpenAPI index: {openapi_index_path}")
        else:
            logger.warning("⚠️ OpenAPI index generation failed or produced no output")
            qa_reporter.add_warning("OpenAPI index generation failed or produced no output")
    except Exception as e:
        logger.warning(f"⚠️ Exception during OpenAPI index generation: {e}")
        qa_reporter.add_warning(f"Exception during OpenAPI index generation: {e}")
    
    # Always generate and save QA report, regardless of success/failure
    qa_status = "completed" if success else "completed_with_errors"
    qa_report = qa_reporter.finalize_report(qa_status)
    
    # Save final merged QA report to output directory
    # This will either merge with existing IG publisher QA or create a new comprehensive report
    qa_output_path = os.path.join(output_dir, "qa.json")
    if qa_reporter.save_to_file(qa_output_path):
        logger.info(f"Final merged QA report saved to {qa_output_path}")
        qa_reporter.add_success(f"Final merged QA report saved to {qa_output_path}")
        
        # Log details about the merged report structure
        if qa_reporter.ig_publisher_qa:
            logger.info("QA report successfully merged with existing FHIR IG publisher QA file")
        else:
            logger.info("QA report created as new comprehensive DAK API QA file")
    else:
        logger.warning(f"Failed to save QA report to {qa_output_path}")
        
        # Try to save to backup location if main save fails
        backup_qa_path = os.path.join(output_dir, "dak-api-qa.json")
        if qa_reporter.save_to_file(backup_qa_path):
            logger.info(f"QA report saved to backup location: {backup_qa_path}")
        else:
            logger.error("Failed to save QA report to any location")
    
    # Log final QA summary (using qa_reporter.report which has the most up-to-date summary)
    logger.info("=== QA REPORT SUMMARY ===")
    logger.info(f"Total successes: {len(qa_reporter.report['details']['successes'])}")
    logger.info(f"Total warnings: {len(qa_reporter.report['details']['warnings'])}")
    logger.info(f"Total errors: {len(qa_reporter.report['details']['errors'])}")
    logger.info(f"Files processed: {len(qa_reporter.report['details']['files_processed'])}")
    logger.info(f"Files expected: {len(qa_reporter.report['details']['files_expected'])}")
    logger.info(f"Files missing: {len(qa_reporter.report['details']['files_missing'])}")
    
    # Exit with success code (0) regardless of errors - QA report contains all details
    # This prevents the workflow from failing while still providing comprehensive error reporting
    if success:
        logger.info("✅ DAK API documentation generation completed successfully")
    else:
        logger.warning("⚠️ DAK API documentation generation completed with errors - see QA report for details")
    
    logger.info("Exiting with success code 0 - check qa.json for detailed status")
    sys.exit(0)


if __name__ == "__main__":
    main()