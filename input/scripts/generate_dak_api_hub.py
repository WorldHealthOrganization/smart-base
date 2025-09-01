#!/usr/bin/env python3
"""
DAK API Documentation Hub Generator

This script generates a unified API documentation hub (dak-api.html) that provides 
browsable documentation for all JSON schemas and OpenAPI specifications in a 
WHO SMART Guideline Digital Adaptation Kit (DAK).

The script:
1. Detects existing JSON schemas (ValueSet and Logical Model schemas)
2. Creates minimal OpenAPI 3.0 wrappers for each JSON schema
3. Generates ReDoc HTML files for each schema
4. Detects any existing OpenAPI/Swagger files
5. Creates the unified dak-api.html hub page

Usage:
    python generate_dak_api_hub.py [output_dir] [openapi_dir]

Author: SMART Guidelines Team
"""

import json
import os
import sys
import logging
import yaml
import re
from typing import Dict, List, Optional, Any, Tuple
from pathlib import Path
from urllib.parse import urlparse


def setup_logging() -> logging.Logger:
    """Configure logging for the script."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger(__name__)


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
        
        for file in os.listdir(output_dir):
            if file.endswith('.schema.json'):
                file_path = os.path.join(output_dir, file)
                
                if file.startswith('ValueSet-'):
                    schemas['valueset'].append(file_path)
                elif not file.startswith('ValueSet-') and not file.startswith('CodeSystem-'):
                    # Assume logical model if not ValueSet or CodeSystem
                    schemas['logical_model'].append(file_path)
                else:
                    schemas['other'].append(file_path)
        
        self.logger.info(f"Found {len(schemas['valueset'])} ValueSet schemas")
        self.logger.info(f"Found {len(schemas['logical_model'])} Logical Model schemas")
        self.logger.info(f"Found {len(schemas['other'])} other schemas")
        
        return schemas


class OpenAPIDetector:
    """Detects existing OpenAPI/Swagger files."""
    
    def __init__(self, logger: logging.Logger):
        self.logger = logger
    
    def find_openapi_files(self, openapi_dir: str) -> List[str]:
        """Find OpenAPI/Swagger files in the given directory."""
        openapi_files = []
        
        if not os.path.exists(openapi_dir):
            self.logger.info(f"OpenAPI directory does not exist: {openapi_dir}")
            return openapi_files
        
        for root, dirs, files in os.walk(openapi_dir):
            for file in files:
                if file.endswith(('.yaml', '.yml', '.json')) and (
                    'openapi' in file.lower() or 'swagger' in file.lower()
                ):
                    openapi_files.append(os.path.join(root, file))
        
        self.logger.info(f"Found {len(openapi_files)} OpenAPI/Swagger files")
        return openapi_files


class OpenAPIWrapper:
    """Creates OpenAPI 3.0 wrappers for JSON schemas."""
    
    def __init__(self, logger: logging.Logger, canonical_base: str = "http://smart.who.int/base"):
        self.logger = logger
        self.canonical_base = canonical_base
    
    def create_wrapper_for_schema(self, schema_path: str, schema_type: str, output_dir: str) -> Optional[str]:
        """
        Create an OpenAPI 3.0 wrapper for a JSON schema.
        
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
                "openapi": "3.0.3",
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
                        schema_name: schema
                    }
                }
            }
            
            # Save OpenAPI wrapper
            wrapper_filename = f"{schema_name}.openapi.yaml"
            wrapper_path = os.path.join(output_dir, wrapper_filename)
            
            with open(wrapper_path, 'w', encoding='utf-8') as f:
                yaml.dump(openapi_spec, f, default_flow_style=False, sort_keys=False)
            
            self.logger.info(f"Created OpenAPI wrapper: {wrapper_path}")
            return wrapper_path
            
        except Exception as e:
            self.logger.error(f"Error creating OpenAPI wrapper for {schema_path}: {e}")
            return None


class ReDocRenderer:
    """Generates self-contained HTML files for OpenAPI specifications and JSON schemas."""
    
    def __init__(self, logger: logging.Logger):
        self.logger = logger
    
    def generate_redoc_html(self, openapi_path: str, output_dir: str, title: str = None) -> Optional[str]:
        """
        Generate a self-contained HTML file for an OpenAPI specification.
        
        Args:
            openapi_path: Path to the OpenAPI spec file
            output_dir: Directory to save the HTML file
            title: Optional title for the HTML page
            
        Returns:
            Path to the generated HTML file, or None if failed
        """
        try:
            openapi_filename = os.path.basename(openapi_path)
            spec_name = openapi_filename.replace('.openapi.yaml', '').replace('.yaml', '').replace('.yml', '').replace('.json', '')
            
            if title is None:
                title = f"{spec_name} API Documentation"
            
            # Load the OpenAPI spec
            with open(openapi_path, 'r', encoding='utf-8') as f:
                if openapi_path.endswith('.json'):
                    spec_data = json.load(f)
                else:
                    spec_data = yaml.safe_load(f)
            
            # Generate self-contained HTML with embedded spec
            html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    
    <style>
        body {{
            margin: 0;
            padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background-color: #fafafa;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }}
        
        .header {{
            background: linear-gradient(135deg, #0066cc 0%, #004a99 100%);
            color: white;
            padding: 2rem 0;
            margin: -2rem -2rem 2rem -2rem;
            text-align: center;
        }}
        
        .header h1 {{
            margin: 0;
            font-size: 2rem;
            font-weight: 400;
        }}
        
        .header p {{
            margin: 0.5rem 0 0 0;
            opacity: 0.9;
        }}
        
        .section {{
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 2rem;
            overflow: hidden;
        }}
        
        .section-header {{
            background-color: #f8f9fa;
            padding: 1rem 1.5rem;
            border-bottom: 1px solid #dee2e6;
        }}
        
        .section-header h2 {{
            margin: 0;
            color: #0066cc;
            font-size: 1.3rem;
        }}
        
        .section-content {{
            padding: 1.5rem;
        }}
        
        .endpoint {{
            border: 1px solid #e9ecef;
            border-radius: 4px;
            margin-bottom: 1rem;
            overflow: hidden;
        }}
        
        .endpoint-header {{
            background-color: #28a745;
            color: white;
            padding: 0.5rem 1rem;
            font-weight: 500;
            font-family: monospace;
        }}
        
        .endpoint-content {{
            padding: 1rem;
        }}
        
        .schema-display {{
            background-color: #f8f9fa;
            border: 1px solid #e9ecef;
            border-radius: 4px;
            padding: 1rem;
            font-family: monospace;
            white-space: pre-wrap;
            overflow-x: auto;
            max-height: 400px;
            overflow-y: auto;
        }}
        
        .property {{
            margin-bottom: 0.5rem;
        }}
        
        .property-name {{
            font-weight: 600;
            color: #0066cc;
        }}
        
        .property-type {{
            color: #6f42c1;
            font-family: monospace;
        }}
        
        .property-description {{
            color: #666;
            margin-top: 0.25rem;
        }}
        
        .enum-values {{
            background-color: #e7f3ff;
            border: 1px solid #b8daff;
            border-radius: 4px;
            padding: 0.5rem;
            margin-top: 0.5rem;
        }}
        
        .enum-value {{
            display: inline-block;
            background-color: #0066cc;
            color: white;
            padding: 0.2rem 0.5rem;
            border-radius: 3px;
            margin: 0.2rem;
            font-family: monospace;
            font-size: 0.9rem;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{title}</h1>
            <p>Generated from: {openapi_filename}</p>
        </div>
"""
            
            # Add API info
            info = spec_data.get('info', {})
            html_content += f"""
        <div class="section">
            <div class="section-header">
                <h2>API Information</h2>
            </div>
            <div class="section-content">
                <h3>{info.get('title', 'API')}</h3>
                <p>{info.get('description', 'No description available')}</p>
                <p><strong>Version:</strong> {info.get('version', 'Unknown')}</p>
            </div>
        </div>
"""
            
            # Add endpoints
            paths = spec_data.get('paths', {})
            if paths:
                html_content += """
        <div class="section">
            <div class="section-header">
                <h2>Endpoints</h2>
            </div>
            <div class="section-content">
"""
                
                for path, methods in paths.items():
                    for method, operation in methods.items():
                        html_content += f"""
                <div class="endpoint">
                    <div class="endpoint-header">
                        {method.upper()} {path}
                    </div>
                    <div class="endpoint-content">
                        <h4>{operation.get('summary', 'No summary')}</h4>
                        <p>{operation.get('description', 'No description available')}</p>
                    </div>
                </div>
"""
                
                html_content += """
            </div>
        </div>
"""
            
            # Add schema information
            components = spec_data.get('components', {})
            schemas = components.get('schemas', {})
            if schemas:
                html_content += """
        <div class="section">
            <div class="section-header">
                <h2>Schema Definition</h2>
            </div>
            <div class="section-content">
"""
                
                for schema_name, schema_def in schemas.items():
                    html_content += f"""
                <h3>{schema_name}</h3>
                <p><strong>Description:</strong> {schema_def.get('description', 'No description')}</p>
                <p><strong>Type:</strong> <span class="property-type">{schema_def.get('type', 'unknown')}</span></p>
"""
                    
                    # Handle enum values for ValueSets
                    if 'enum' in schema_def:
                        html_content += """
                <div class="enum-values">
                    <strong>Allowed values:</strong><br>
"""
                        for enum_value in schema_def['enum']:
                            html_content += f'                    <span class="enum-value">{enum_value}</span>\n'
                        html_content += """
                </div>
"""
                    
                    # Handle object properties for Logical Models
                    if 'properties' in schema_def:
                        html_content += """
                <h4>Properties:</h4>
"""
                        for prop_name, prop_def in schema_def['properties'].items():
                            html_content += f"""
                <div class="property">
                    <span class="property-name">{prop_name}</span>
                    <span class="property-type">({prop_def.get('type', 'unknown')})</span>
                    <div class="property-description">{prop_def.get('description', 'No description')}</div>
                </div>
"""
                        
                        # Show required fields
                        required = schema_def.get('required', [])
                        if required:
                            html_content += f"""
                <p><strong>Required fields:</strong> {', '.join(required)}</p>
"""
                    
                    # Show full schema as JSON
                    html_content += f"""
                <h4>Full Schema:</h4>
                <div class="schema-display">{json.dumps(schema_def, indent=2)}</div>
"""
                
                html_content += """
            </div>
        </div>
"""
            
            html_content += """
    </div>
</body>
</html>"""
            
            # Save HTML file
            html_filename = f"{spec_name}.openapi.html"
            html_path = os.path.join(output_dir, html_filename)
            
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            self.logger.info(f"Generated self-contained HTML: {html_path}")
            return html_path
            
        except Exception as e:
            self.logger.error(f"Error generating HTML for {openapi_path}: {e}")
            return None


class DAKApiHubGenerator:
    """Generates the unified DAK API documentation hub."""
    
    def __init__(self, logger: logging.Logger):
        self.logger = logger
    
    def generate_hub(self, output_dir: str, schema_docs: Dict[str, List[Dict]], openapi_docs: List[Dict]) -> bool:
        """
        Generate the unified dak-api.html hub page.
        
        Args:
            output_dir: Directory to save the hub file
            schema_docs: Dictionary with schema documentation info
            openapi_docs: List of OpenAPI documentation info
            
        Returns:
            True if successful, False otherwise
        """
        try:
            hub_path = os.path.join(output_dir, "dak-api.html")
            
            # Generate HTML content
            html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DAK API Documentation Hub</title>
    <style>
        /* FHIR IG-inspired styling */
        body { 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            margin: 0; 
            padding: 0;
            background-color: #f8f9fa;
            color: #333;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }
        
        .header {
            background: linear-gradient(135deg, #0066cc 0%, #004a99 100%);
            color: white;
            padding: 2rem 0;
            margin-bottom: 2rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        
        .header h1 { 
            margin: 0;
            font-size: 2.5rem;
            font-weight: 300;
            text-align: center;
        }
        
        .header p {
            margin: 0.5rem 0 0 0;
            font-size: 1.1rem;
            text-align: center;
            opacity: 0.9;
        }
        
        .section {
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 2rem;
            overflow: hidden;
        }
        
        .section-header {
            background-color: #e9ecef;
            padding: 1rem 1.5rem;
            border-bottom: 1px solid #dee2e6;
        }
        
        .section-header h2 { 
            margin: 0;
            color: #0066cc; 
            font-size: 1.5rem;
            font-weight: 500;
        }
        
        .section-content {
            padding: 1.5rem;
        }
        
        .doc-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1rem;
        }
        
        .doc-card {
            border: 1px solid #dee2e6;
            border-radius: 6px;
            padding: 1rem;
            background: #f8f9fa;
            transition: all 0.2s ease;
        }
        
        .doc-card:hover {
            border-color: #0066cc;
            background: white;
            box-shadow: 0 2px 8px rgba(0,102,204,0.1);
        }
        
        .doc-card h3 {
            margin: 0 0 0.5rem 0;
            color: #0066cc;
            font-size: 1.1rem;
        }
        
        .doc-card p {
            margin: 0 0 1rem 0;
            color: #6c757d;
            font-size: 0.9rem;
            line-height: 1.4;
        }
        
        .doc-card a {
            display: inline-block;
            color: #0066cc;
            text-decoration: none;
            font-weight: 500;
            padding: 0.5rem 1rem;
            border: 1px solid #0066cc;
            border-radius: 4px;
            transition: all 0.2s ease;
        }
        
        .doc-card a:hover {
            background-color: #0066cc;
            color: white;
        }
        
        .schema-type {
            display: inline-block;
            background-color: #28a745;
            color: white;
            padding: 0.2rem 0.5rem;
            border-radius: 3px;
            font-size: 0.75rem;
            font-weight: 500;
            text-transform: uppercase;
            margin-bottom: 0.5rem;
        }
        
        .schema-type.valueset {
            background-color: #17a2b8;
        }
        
        .schema-type.logical-model {
            background-color: #6f42c1;
        }
        
        .schema-type.openapi {
            background-color: #fd7e14;
        }
        
        .no-content {
            text-align: center;
            color: #6c757d;
            font-style: italic;
            padding: 2rem;
        }
        
        .footer {
            text-align: center;
            color: #6c757d;
            font-size: 0.9rem;
            margin-top: 3rem;
            padding-top: 2rem;
            border-top: 1px solid #dee2e6;
        }
    </style>
</head>
<body>
    <div class="header">
        <div class="container">
            <h1>DAK API Documentation Hub</h1>
            <p>WHO SMART Guideline Digital Adaptation Kit - API and Schema Documentation</p>
        </div>
    </div>
    
    <div class="container">
"""
            
            # Add ValueSet schemas section
            if schema_docs.get('valueset'):
                html_content += """
        <div class="section">
            <div class="section-header">
                <h2>ValueSet Schemas</h2>
            </div>
            <div class="section-content">
                <div class="doc-grid">
"""
                for doc in schema_docs['valueset']:
                    html_content += f"""
                    <div class="doc-card">
                        <div class="schema-type valueset">ValueSet</div>
                        <h3>{doc['title']}</h3>
                        <p>{doc['description']}</p>
                        <a href="{doc['html_file']}" target="_blank">View Documentation</a>
                    </div>
"""
                html_content += """
                </div>
            </div>
        </div>
"""
            
            # Add Logical Model schemas section
            if schema_docs.get('logical_model'):
                html_content += """
        <div class="section">
            <div class="section-header">
                <h2>Logical Model Schemas</h2>
            </div>
            <div class="section-content">
                <div class="doc-grid">
"""
                for doc in schema_docs['logical_model']:
                    html_content += f"""
                    <div class="doc-card">
                        <div class="schema-type logical-model">Logical Model</div>
                        <h3>{doc['title']}</h3>
                        <p>{doc['description']}</p>
                        <a href="{doc['html_file']}" target="_blank">View Documentation</a>
                    </div>
"""
                html_content += """
                </div>
            </div>
        </div>
"""
            
            # Add OpenAPI specifications section
            if openapi_docs:
                html_content += """
        <div class="section">
            <div class="section-header">
                <h2>OpenAPI Specifications</h2>
            </div>
            <div class="section-content">
                <div class="doc-grid">
"""
                for doc in openapi_docs:
                    html_content += f"""
                    <div class="doc-card">
                        <div class="schema-type openapi">OpenAPI</div>
                        <h3>{doc['title']}</h3>
                        <p>{doc['description']}</p>
                        <a href="{doc['html_file']}" target="_blank">View Documentation</a>
                    </div>
"""
                html_content += """
                </div>
            </div>
        </div>
"""
            
            # Add empty state if no documentation
            if not schema_docs.get('valueset') and not schema_docs.get('logical_model') and not openapi_docs:
                html_content += """
        <div class="section">
            <div class="section-content">
                <div class="no-content">
                    <p>No API documentation found. Run the schema generation scripts first to generate documentation.</p>
                </div>
            </div>
        </div>
"""
            
            html_content += """
        <div class="footer">
            <p>Generated automatically by the DAK API Documentation Hub Generator</p>
        </div>
    </div>
</body>
</html>"""
            
            # Save hub file
            with open(hub_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            self.logger.info(f"Generated DAK API hub: {hub_path}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error generating DAK API hub: {e}")
            return False


def main():
    """Main entry point for the script."""
    logger = setup_logging()
    
    # Parse command line arguments
    if len(sys.argv) == 1:
        output_dir = "output"
        openapi_dir = "input/images/openapi"
    elif len(sys.argv) == 2:
        output_dir = sys.argv[1]
        openapi_dir = "input/images/openapi"
    else:
        output_dir = sys.argv[1]
        openapi_dir = sys.argv[2]
    
    logger.info(f"Output directory: {output_dir}")
    logger.info(f"OpenAPI directory: {openapi_dir}")
    
    # Initialize components
    schema_detector = SchemaDetector(logger)
    openapi_detector = OpenAPIDetector(logger)
    openapi_wrapper = OpenAPIWrapper(logger)
    redoc_renderer = ReDocRenderer(logger)
    hub_generator = DAKApiHubGenerator(logger)
    
    # Find schema files
    schemas = schema_detector.find_schema_files(output_dir)
    
    # Find existing OpenAPI files
    openapi_files = openapi_detector.find_openapi_files(openapi_dir)
    
    # Generate OpenAPI wrappers and ReDoc HTML for schemas
    schema_docs = {
        'valueset': [],
        'logical_model': []
    }
    
    # Process ValueSet schemas
    for schema_path in schemas['valueset']:
        try:
            # Load schema to get metadata
            with open(schema_path, 'r', encoding='utf-8') as f:
                schema = json.load(f)
            
            # Create OpenAPI wrapper
            wrapper_path = openapi_wrapper.create_wrapper_for_schema(schema_path, 'valueset', output_dir)
            if wrapper_path:
                # Generate ReDoc HTML
                html_path = redoc_renderer.generate_redoc_html(wrapper_path, output_dir, 
                                                             f"{schema.get('title', 'ValueSet')} Documentation")
                if html_path:
                    schema_docs['valueset'].append({
                        'title': schema.get('title', os.path.basename(schema_path)),
                        'description': schema.get('description', 'ValueSet schema documentation'),
                        'html_file': os.path.basename(html_path)
                    })
        except Exception as e:
            logger.error(f"Error processing ValueSet schema {schema_path}: {e}")
    
    # Process Logical Model schemas
    for schema_path in schemas['logical_model']:
        try:
            # Load schema to get metadata
            with open(schema_path, 'r', encoding='utf-8') as f:
                schema = json.load(f)
            
            # Create OpenAPI wrapper
            wrapper_path = openapi_wrapper.create_wrapper_for_schema(schema_path, 'logical_model', output_dir)
            if wrapper_path:
                # Generate ReDoc HTML
                html_path = redoc_renderer.generate_redoc_html(wrapper_path, output_dir,
                                                             f"{schema.get('title', 'Logical Model')} Documentation")
                if html_path:
                    schema_docs['logical_model'].append({
                        'title': schema.get('title', os.path.basename(schema_path)),
                        'description': schema.get('description', 'Logical Model schema documentation'),
                        'html_file': os.path.basename(html_path)
                    })
        except Exception as e:
            logger.error(f"Error processing Logical Model schema {schema_path}: {e}")
    
    # Process existing OpenAPI files
    openapi_docs = []
    for openapi_path in openapi_files:
        try:
            # Generate ReDoc HTML for existing OpenAPI files
            html_path = redoc_renderer.generate_redoc_html(openapi_path, output_dir)
            if html_path:
                openapi_docs.append({
                    'title': f"{os.path.basename(openapi_path)} API",
                    'description': f"API documentation from {os.path.basename(openapi_path)}",
                    'html_file': os.path.basename(html_path)
                })
        except Exception as e:
            logger.error(f"Error processing OpenAPI file {openapi_path}: {e}")
    
    # Generate the unified hub
    success = hub_generator.generate_hub(output_dir, schema_docs, openapi_docs)
    
    if success:
        total_docs = len(schema_docs['valueset']) + len(schema_docs['logical_model']) + len(openapi_docs)
        logger.info(f"Successfully generated DAK API hub with {total_docs} documentation pages")
        sys.exit(0)
    else:
        logger.error("Failed to generate DAK API hub")
        sys.exit(1)


if __name__ == "__main__":
    main()