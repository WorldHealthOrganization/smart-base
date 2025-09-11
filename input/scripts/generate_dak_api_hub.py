#!/usr/bin/env python3
"""
DAK API Documentation Hub Generator

This script post-processes the IG-generated HTML files to inject DAK API content.
It works by:
1. Detecting existing JSON schemas (ValueSet and Logical Model schemas)
2. Creating minimal OpenAPI 3.0 wrappers for each JSON schema
3. Generating schema documentation content
4. Post-processing the dak-api.html file to replace content after "publish-box"
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
import yaml
import re
from typing import Dict, List, Optional, Any, Tuple
from pathlib import Path
from urllib.parse import urlparse
from bs4 import BeautifulSoup


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
        
        for file in os.listdir(output_dir):
            if file.endswith('.jsonld') and file.startswith('ValueSet-'):
                file_path = os.path.join(output_dir, file)
                jsonld_files.append(file_path)
        
        self.logger.info(f"Found {len(jsonld_files)} JSON-LD vocabulary files")
        
        return jsonld_files


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
    
    def create_enumeration_wrapper(self, enum_schema_path: str, schema_type: str, output_dir: str) -> Optional[str]:
        """
        Create an OpenAPI 3.0 wrapper for an enumeration schema.
        
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
                "openapi": "3.0.3",
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
                        "EnumerationResponse": enum_schema
                    }
                }
            }
            
            # Save OpenAPI wrapper
            if schema_type == 'valueset':
                wrapper_filename = "ValueSets-enumeration.openapi.yaml"
            else:
                wrapper_filename = "LogicalModels-enumeration.openapi.yaml"
                
            wrapper_path = os.path.join(output_dir, wrapper_filename)
            
            with open(wrapper_path, 'w', encoding='utf-8') as f:
                yaml.dump(openapi_spec, f, default_flow_style=False, sort_keys=False)
            
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
            content: HTML content to inject after the publish-box
            
        Returns:
            The new HTML content as a string
        """
        try:
            with open(template_html_path, 'r', encoding='utf-8') as f:
                template_html = f.read()
            
            soup = BeautifulSoup(template_html, 'html.parser')
            
            # Update the title
            title_tag = soup.find('title')
            if title_tag:
                # Extract the suffix from existing title (e.g., " - SMART Base v0.2.0")
                current_title = title_tag.get_text()
                if ' - ' in current_title:
                    suffix = ' - ' + current_title.split(' - ', 1)[1]
                else:
                    suffix = ''
                title_tag.string = title + suffix
            
            # Find the publish-box and replace content after it
            publish_box = soup.find(id='publish-box')
            if publish_box:
                # Find the parent container that holds the content
                content_container = publish_box.find_parent()
                if content_container:
                    # Remove all siblings after the publish-box
                    for sibling in list(publish_box.next_siblings):
                        if hasattr(sibling, 'extract'):
                            sibling.extract()
                    
                    # Add the new content
                    new_content_soup = BeautifulSoup(content, 'html.parser')
                    for element in new_content_soup:
                        if hasattr(element, 'name'):  # Only add tag elements
                            content_container.append(element)
            
            return str(soup)
            
        except Exception as e:
            self.logger.error(f"Error creating HTML template: {e}")
            return ""
    
    def inject_content_after_publish_box(self, html_file_path: str, content: str) -> bool:
        """
        Inject content into an HTML file after the publish-box div.
        
        Args:
            html_file_path: Path to the HTML file to modify
            content: HTML content to inject
            
        Returns:
            True if successful, False otherwise
        """
        try:
            with open(html_file_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Find the publish-box
            publish_box = soup.find(id='publish-box')
            if not publish_box:
                self.logger.warning(f"No publish-box found in {html_file_path}")
                return False
            
            # Find the parent container that holds the content
            content_container = publish_box.find_parent()
            if not content_container:
                self.logger.warning(f"No content container found for publish-box in {html_file_path}")
                return False
            
            # Remove all siblings after the publish-box
            for sibling in list(publish_box.next_siblings):
                if hasattr(sibling, 'extract'):
                    sibling.extract()
            
            # Add the new content
            new_content_soup = BeautifulSoup(content, 'html.parser')
            for element in new_content_soup:
                if hasattr(element, 'name'):  # Only add tag elements
                    content_container.append(element)
            
            # Write the modified HTML back to the file
            with open(html_file_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            
            self.logger.info(f"Successfully injected content into {html_file_path}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error injecting content into {html_file_path}: {e}")
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
                    
                    # Look for anchor patterns like id="CDHIv1-2.461.462" or similar
                    import re
                    # Pattern to find id attributes that likely correspond to codes
                    anchor_pattern = rf'id="({re.escape(codesystem_id)}-[^"]+)"'
                    matches = re.findall(anchor_pattern, html_content)
                    
                    for match in matches:
                        # Extract the code part after the codesystem ID
                        if '-' in match:
                            code_part = match.split('-', 1)[1]
                            anchor_map[code_part] = match
                
                self.logger.info(f"Found {len(anchor_map)} anchor mappings for CodeSystem {codesystem_id}")
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
        <p><strong>Schema ID:</strong> <a href="{schema_id}" target="_blank">{schema_id}</a></p>
        <p><strong>FHIR Page:</strong> <a href="{fhir_url}">View full FHIR definition</a></p>
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
            
            # Show full schema as collapsible JSON
            schema_json_str = json.dumps(schema_data, indent=2)
            html_content += f"""
    <div class="schema-json">
        <details>
            <summary>Full Schema (JSON)</summary>
            <pre><code class="language-json">{schema_json_str}</code></pre>
        </details>
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

details {{
    margin: 1rem 0;
    border: 1px solid #dee2e6;
    border-radius: 4px;
    padding: 0;
}}

details summary {{
    background: #f8f9fa;
    padding: 0.75rem;
    cursor: pointer;
    border-bottom: 1px solid #dee2e6;
    font-weight: 500;
}}

details[open] summary {{
    border-bottom: 1px solid #dee2e6;
}}

details pre {{
    margin: 1rem;
    background: #f8f9fa;
    border: 1px solid #e9ecef;
    border-radius: 4px;
    padding: 1rem;
    overflow-x: auto;
}}
</style>

<hr>

<p><em>This documentation is automatically generated from the schema definition.</em></p>
"""
            
            return html_content
            
        except Exception as e:
            self.logger.error(f"Error generating schema documentation for {schema_path}: {e}")
            return ""
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
                    
                    # Look for anchor patterns like id="CDHIv1-2.461.462" or similar
                    import re
                    # Pattern to find id attributes that likely correspond to codes
                    anchor_pattern = rf'id="({re.escape(codesystem_id)}-[^"]+)"'
                    matches = re.findall(anchor_pattern, html_content)
                    
                    for match in matches:
                        # Extract the code part after the codesystem ID
                        if '-' in match:
                            code_part = match.split('-', 1)[1]
                            anchor_map[code_part] = match
                
                self.logger.info(f"Found {len(anchor_map)} anchor mappings for CodeSystem {codesystem_id}")
        except Exception as e:
            self.logger.warning(f"Could not load CodeSystem anchors for {codesystem_url}: {e}")
        
        return anchor_map
    
    def generate_redoc_html(self, openapi_path: str, output_dir: str, title: str = None, schema_type: str = None) -> Optional[str]:
        """
        Generate a markdown file for an OpenAPI specification that integrates with the IG template.
        
        Args:
            openapi_path: Path to the OpenAPI spec file
            output_dir: Directory to save the markdown file
            title: Optional title for the page
            schema_type: Optional schema type ('valueset' or 'logical_model')
            
        Returns:
            Path to the generated markdown file, or None if failed
        """
        try:
            openapi_filename = os.path.basename(openapi_path)
            spec_name = openapi_filename.replace('.openapi.yaml', '').replace('.yaml', '').replace('.yml', '').replace('.json', '')
            
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
                if openapi_path.endswith('.json'):
                    spec_data = json.load(f)
                else:
                    spec_data = yaml.safe_load(f)
            
            # Create pagecontent directory path
            pagecontent_dir = os.path.join(os.path.dirname(output_dir), "input", "pagecontent")
            if not os.path.exists(pagecontent_dir):
                # Fallback: try to find pagecontent relative to current location
                pagecontent_dir = os.path.join(os.getcwd(), "input", "pagecontent")
            
            if not os.path.exists(pagecontent_dir):
                # Generate in output directory as fallback
                pagecontent_dir = output_dir
            
            # Generate markdown content for IG integration
            markdown_content = f"""# {title}

<!-- This content is automatically generated from {openapi_filename} -->

"""
            
            # Add API info
            info = spec_data.get('info', {})
            markdown_content += f"""## API Information

**{info.get('title', 'API')}**

{info.get('description', 'No description available')}

**Version:** {info.get('version', 'Unknown')}

"""
            
            # Add endpoints
            paths = spec_data.get('paths', {})
            if paths:
                markdown_content += """## Endpoints

"""
                
                for path, methods in paths.items():
                    for method, operation in methods.items():
                        markdown_content += f"""### {method.upper()} {path}

**{operation.get('summary', 'No summary')}**

{operation.get('description', 'No description available')}

"""
            
            # Add schema information
            components = spec_data.get('components', {})
            schemas = components.get('schemas', {})
            if schemas:
                markdown_content += """## Schema Definition

"""
                
                for schema_name, schema_def in schemas.items():
                    schema_id = schema_def.get('$id', '')
                    
                    markdown_content += f"""### {schema_name}

**Description:** {schema_def.get('description', 'No description')}

**Type:** {schema_def.get('type', 'unknown')}

"""
                    
                    # Add schema ID as link if available
                    if schema_id:
                        # Convert schema ID to corresponding FHIR page (use relative URL)
                        # Extract filename from absolute URL and replace extension
                        if '/' in schema_id:
                            filename = schema_id.split('/')[-1]
                        else:
                            filename = schema_id
                        
                        # Determine the correct FHIR page link based on schema type
                        # Individual schemas should link to their specific HTML pages
                        # Only enumeration endpoints should link to artifacts.html sections
                        if filename == 'ValueSets.schema.json':
                            fhir_url = "artifacts.html#terminology-value-sets"
                        elif filename == 'LogicalModels.schema.json':
                            fhir_url = "artifacts.html#structures-logical-models"
                        else:
                            # Individual schemas link to their specific HTML files
                            fhir_url = filename.replace('.schema.json', '.html')
                        
                        markdown_content += f"""**Schema ID:** [{schema_id}]({schema_id})

**FHIR Page:** [View full FHIR definition]({fhir_url})

"""
                    
                    # Handle enum values for ValueSets
                    if 'enum' in schema_def:
                        # Sort enum values alphabetically and truncate after 40 entries
                        enum_values = sorted(schema_def['enum'])
                        displayed_values = enum_values[:40]
                        truncated = len(enum_values) > 40
                        
                        # Check if we can link to CodeSystem definitions
                        codesystem_anchors = {}
                        if schema_type == 'valueset' and schema_id:
                            # Try to load system mapping to find CodeSystem
                            try:
                                if '/' in schema_id:
                                    base_url = '/'.join(schema_id.split('/')[:-1])
                                    system_filename = f"{schema_name}.system.json"
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
                                self.logger.warning(f"Could not load system mappings for {schema_name}: {e}")
                        
                        markdown_content += """**Allowed values:**

<div class="enum-values">
"""
                        for enum_value in displayed_values:
                            if enum_value in codesystem_anchors:
                                # Create link to CodeSystem anchor
                                anchor = codesystem_anchors[enum_value]
                                codesystem_id = anchor.split('-')[0]
                                link_url = f"CodeSystem-{codesystem_id}.html#{anchor}"
                                markdown_content += f'<span class="enum-value"><a href="{link_url}" title="View definition in CodeSystem">{enum_value}</a></span>\n'
                            else:
                                markdown_content += f'<span class="enum-value">{enum_value}</span>\n'
                        
                        if truncated:
                            remaining_count = len(enum_values) - 40
                            markdown_content += f'<div class="enum-truncated">... and {remaining_count} more values</div>\n'
                        
                        markdown_content += """</div>

"""
                    
                    # Handle object properties for Logical Models
                    if 'properties' in schema_def:
                        markdown_content += """**Properties:**

"""
                        for prop_name, prop_def in schema_def['properties'].items():
                            prop_type = prop_def.get('type', 'unknown')
                            
                            markdown_content += f"""- **{prop_name}** ({prop_type}): {prop_def.get('description', 'No description')}
"""
                        
                        # Show required fields
                        required = schema_def.get('required', [])
                        if required:
                            markdown_content += f"""
**Required fields:** {', '.join(required)}

"""
                    
                    # Show full schema as collapsible JSON
                    schema_json_str = json.dumps(schema_def, indent=2)
                    markdown_content += f"""<details>
<summary>Full Schema (JSON)</summary>

```json
{schema_json_str}
```

</details>

"""
            
            # Add styling that integrates with IG theme
            markdown_content += """
<style>
/* Schema documentation styling that integrates with IG theme */
.enum-values {
  background-color: #e7f3ff;
  border: 1px solid #b8daff;
  border-radius: 4px;
  padding: 1rem;
  margin: 1rem 0;
}

.enum-value {
  display: inline-block;
  background-color: #00477d;
  color: white;
  padding: 0.2rem 0.5rem;
  border-radius: 3px;
  margin: 0.2rem;
  font-size: 0.9rem;
  text-decoration: none;
}

.enum-value a {
  color: white;
  text-decoration: none;
}

.enum-value:hover, .enum-value a:hover {
  background-color: #0070A1;
  color: white;
  text-decoration: none;
}

.enum-truncated {
  margin-top: 0.5rem;
  font-style: italic;
  color: #6c757d;
}

details {
  margin: 1rem 0;
  border: 1px solid #dee2e6;
  border-radius: 4px;
  padding: 0;
}

details summary {
  background: #f8f9fa;
  padding: 0.75rem;
  cursor: pointer;
  border-bottom: 1px solid #dee2e6;
  font-weight: 500;
}

details[open] summary {
  border-bottom: 1px solid #dee2e6;
}

details pre {
  margin: 1rem;
  background: #f8f9fa;
  border: 1px solid #e9ecef;
  border-radius: 4px;
  padding: 1rem;
  overflow-x: auto;
}
</style>

---

*This documentation is automatically generated from the OpenAPI specification.*
"""
            
            # Save markdown file
            md_filename = f"{spec_name}.md"
            md_path = os.path.join(pagecontent_dir, md_filename)
            
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            
            self.logger.info(f"Generated schema documentation markdown: {md_path}")
            
            # Return the corresponding HTML filename that will be generated by the IG build
            html_filename = f"{spec_name}.html"
            return html_filename
            
        except Exception as e:
            self.logger.error(f"Error generating markdown for {openapi_path}: {e}")
            return None


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
    
    def generate_hub_html_content(self, schema_docs: Dict[str, List[Dict]], openapi_docs: List[Dict], enumeration_docs: List[Dict] = None, jsonld_docs: List[Dict] = None) -> str:
        """
        Generate HTML content for the DAK API hub page.
        
        Args:
            schema_docs: Dictionary with schema documentation info
            openapi_docs: List of OpenAPI documentation info
            enumeration_docs: List of enumeration endpoint documentation info
            jsonld_docs: List of JSON-LD vocabulary documentation info
            
        Returns:
            HTML content as a string
        """
        if enumeration_docs is None:
            enumeration_docs = []
        if jsonld_docs is None:
            jsonld_docs = []
        
        # Start building the HTML content
        html_content = """
<div class="dak-api-hub">
    <h2>DAK API Documentation Hub</h2>
    
    <p>This page provides comprehensive documentation for all available DAK (Data Access Kit) API endpoints and schemas. 
    The DAK API provides structured access to ValueSet enumerations and Logical Model definitions used throughout this implementation guide.</p>
"""
        
        # Add API Enumeration Endpoints section
        if enumeration_docs:
            html_content += """
    <h3>API Enumeration Endpoints</h3>
    
    <p>These endpoints provide lists of all available schemas of each type:</p>
    
    <div class="enumeration-endpoints">
"""
            for enum_doc in enumeration_docs:
                html_content += f"""
        <div class="endpoint-card">
            <h4><a href="{enum_doc['html_file']}">{enum_doc['title']}</a></h4>
            <p>{enum_doc['description']}</p>
        </div>
"""
            html_content += """
    </div>
"""
        
        # Add ValueSet Schemas section
        if schema_docs['valueset']:
            html_content += f"""
    <h3>ValueSet Schemas ({len(schema_docs['valueset'])} available)</h3>
    
    <p>JSON Schema definitions for FHIR ValueSets, providing structured enumeration of allowed code values:</p>
    
    <div class="schema-grid">
"""
            for schema_doc in schema_docs['valueset']:
                html_content += f"""
        <div class="schema-card">
            <h4><a href="{schema_doc['html_file']}">{schema_doc['title']}</a></h4>
            <p>{schema_doc['description']}</p>
        </div>
"""
            html_content += """
    </div>
"""
        
        # Add Logical Model Schemas section
        if schema_docs['logical_model']:
            html_content += f"""
    <h3>Logical Model Schemas ({len(schema_docs['logical_model'])} available)</h3>
    
    <p>JSON Schema definitions for FHIR Logical Models, defining structured data elements and their relationships:</p>
    
    <div class="schema-grid">
"""
            for schema_doc in schema_docs['logical_model']:
                html_content += f"""
        <div class="schema-card">
            <h4><a href="{schema_doc['html_file']}">{schema_doc['title']}</a></h4>
            <p>{schema_doc['description']}</p>
        </div>
"""
            html_content += """
    </div>
"""
        
        # Add JSON-LD Vocabularies section
        if jsonld_docs:
            html_content += f"""
    <h3>JSON-LD Vocabularies ({len(jsonld_docs)} available)</h3>
    
    <p>Semantic web vocabularies that define enumeration classes and properties for ValueSet codes. 
    Each vocabulary follows the JSON-LD 1.1 specification and provides:</p>
    
    <div class="schema-grid">
"""
            for jsonld_doc in jsonld_docs:
                html_content += f"""
        <div class="schema-card">
            <h4><a href="{jsonld_doc['filename']}">{jsonld_doc['title']}</a></h4>
            <p>{jsonld_doc['description']}</p>
        </div>
"""
            html_content += """
    </div>
"""
        
        # Add OpenAPI Documentation section (if any)
        if openapi_docs:
            html_content += f"""
    <h3>OpenAPI Documentation ({len(openapi_docs)} available)</h3>
    
    <p>Interactive API documentation for REST endpoints:</p>
    
    <div class="api-grid">
"""
            for api_doc in openapi_docs:
                html_content += f"""
        <div class="api-card">
            <h4><a href="{api_doc['html_file']}">{api_doc['title']}</a></h4>
            <p>{api_doc['description']}</p>
        </div>
"""
            html_content += """
    </div>
"""
        
        # Add usage information
        html_content += """
    <h3>Using the DAK API</h3>
    
    <div class="usage-info">
        <h4>Schema Validation</h4>
        <p>Each JSON Schema can be used to validate data structures in your applications. 
        The schemas follow the JSON Schema Draft 2020-12 specification and include:</p>
        <ul>
            <li>Type definitions and constraints</li>
            <li>Property descriptions and examples</li>
            <li>Required field specifications</li>
            <li>Enumeration values with links to definitions</li>
        </ul>
        
        <h4>JSON-LD Semantic Integration</h4>
        <p>The JSON-LD vocabularies provide semantic web integration for ValueSet enumerations. Each vocabulary includes:</p>
        <ul>
            <li>Enumeration class definitions with schema.org compatibility</li>
            <li>Individual code instances with canonical IRIs</li>
            <li>Property definitions with range constraints</li>
            <li>FHIR metadata integration (system URIs, ValueSet references)</li>
        </ul>
        
        <h4>Integration with FHIR</h4>
        <p>All schemas are derived from the FHIR definitions in this implementation guide. 
        Each schema page includes links to the corresponding FHIR resource definitions for complete context.</p>
        
        <h4>API Endpoints</h4>
        <p>The enumeration endpoints provide machine-readable lists of all available schemas, 
        making it easy to discover and integrate with the available data structures programmatically.</p>
    </div>
</div>

<style>
/* DAK API Hub styling that integrates with IG theme */
.dak-api-hub {
    margin: 1rem 0;
}

.enumeration-endpoints, .schema-grid, .api-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1rem;
    margin: 1rem 0;
}

.endpoint-card, .schema-card, .api-card {
    border: 1px solid #dee2e6;
    border-radius: 4px;
    padding: 1rem;
    background: #f8f9fa;
    transition: box-shadow 0.2s ease;
}

.endpoint-card:hover, .schema-card:hover, .api-card:hover {
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.endpoint-card h4, .schema-card h4, .api-card h4 {
    margin: 0 0 0.5rem 0;
    color: #00477d;
}

.endpoint-card h4 a, .schema-card h4 a, .api-card h4 a {
    color: #00477d;
    text-decoration: none;
}

.endpoint-card h4 a:hover, .schema-card h4 a:hover, .api-card h4 a:hover {
    color: #0070A1;
    text-decoration: underline;
}

.endpoint-card p, .schema-card p, .api-card p {
    margin: 0;
    color: #6c757d;
    font-size: 0.9rem;
}

.usage-info {
    background: #e7f3ff;
    border: 1px solid #b8daff;
    border-radius: 4px;
    padding: 1.5rem;
    margin: 1.5rem 0;
}

.usage-info h4 {
    color: #00477d;
    margin-top: 1rem;
}

.usage-info h4:first-child {
    margin-top: 0;
}

.usage-info ul {
    margin: 0.5rem 0;
}

.usage-info li {
    margin: 0.25rem 0;
}
</style>

<hr>

<p><em>This documentation hub is automatically generated from the available schema and API definitions.</em></p>
"""
        
        return html_content
    
    def post_process_dak_api_html(self, output_dir: str, schema_docs: Dict[str, List[Dict]], openapi_docs: List[Dict], enumeration_docs: List[Dict] = None, jsonld_docs: List[Dict] = None) -> bool:
        """
        Post-process the dak-api.html file to inject DAK API content.
        
        Args:
            output_dir: Directory containing the generated HTML files
            schema_docs: Dictionary with schema documentation info
            openapi_docs: List of OpenAPI documentation info
            enumeration_docs: List of enumeration endpoint documentation info
            jsonld_docs: List of JSON-LD vocabulary documentation info
            
        Returns:
            True if successful, False otherwise
        """
        try:
            if enumeration_docs is None:
                enumeration_docs = []
            if jsonld_docs is None:
                jsonld_docs = []
            
            # Check if dak-api.html exists
            dak_api_html_path = os.path.join(output_dir, "dak-api.html")
            if not os.path.exists(dak_api_html_path):
                self.logger.error(f"dak-api.html not found at {dak_api_html_path}")
                return False
            
            # Generate the HTML content for the hub
            hub_content = self.generate_hub_html_content(schema_docs, openapi_docs, enumeration_docs, jsonld_docs)
            
            # Create HTML processor to inject content
            html_processor = HTMLProcessor(self.logger, output_dir)
            
            # Inject content into dak-api.html
            success = html_processor.inject_content_after_publish_box(dak_api_html_path, hub_content)
            
            if success:
                self.logger.info(f"Successfully post-processed DAK API hub: {dak_api_html_path}")
            
            return success
            
        except Exception as e:
            self.logger.error(f"Error post-processing DAK API hub: {e}")
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
    schema_doc_renderer = SchemaDocumentationRenderer(logger)
    hub_generator = DAKApiHubGenerator(logger)
    html_processor = HTMLProcessor(logger, output_dir)
    
    # Find schema files
    schemas = schema_detector.find_schema_files(output_dir)
    
    # Find JSON-LD vocabulary files
    jsonld_files = schema_detector.find_jsonld_files(output_dir)
    
    # Find existing OpenAPI files
    openapi_files = openapi_detector.find_openapi_files(openapi_dir)
    
    # Generate schema documentation
    schema_docs = {
        'valueset': [],
        'logical_model': []
    }
    
    # Check if dak-api.html exists (required as template)
    dak_api_html_path = os.path.join(output_dir, "dak-api.html")
    if not os.path.exists(dak_api_html_path):
        logger.error(f"dak-api.html not found at {dak_api_html_path}. Make sure the IG publisher ran first with a placeholder dak-api.md file.")
        sys.exit(1)
    
    # Process ValueSet schemas
    for schema_path in schemas['valueset']:
        try:
            # Load schema to get metadata
            with open(schema_path, 'r', encoding='utf-8') as f:
                schema = json.load(f)
            
            schema_filename = os.path.basename(schema_path)
            schema_name = schema_filename.replace('.schema.json', '')
            
            # Generate schema documentation content
            doc_content = schema_doc_renderer.generate_schema_documentation_html(schema_path, 'valueset', output_dir)
            
            if doc_content:
                # Create individual HTML file using dak-api.html as template
                html_filename = f"{schema_name}.html"
                html_path = os.path.join(output_dir, html_filename)
                
                # Create HTML content using template
                title = schema.get('title', f"{schema_name} Schema Documentation")
                html_content = html_processor.create_html_template_from_existing(dak_api_html_path, title, doc_content)
                
                if html_content:
                    # Save the individual schema HTML file
                    with open(html_path, 'w', encoding='utf-8') as f:
                        f.write(html_content)
                    
                    logger.info(f"Created ValueSet schema HTML: {html_path}")
                    
                    schema_docs['valueset'].append({
                        'title': title,
                        'description': schema.get('description', 'ValueSet schema documentation'),
                        'html_file': html_filename
                    })
                
        except Exception as e:
            logger.error(f"Error processing ValueSet schema {schema_path}: {e}")
    
    # Process Logical Model schemas
    for schema_path in schemas['logical_model']:
        try:
            # Load schema to get metadata
            with open(schema_path, 'r', encoding='utf-8') as f:
                schema = json.load(f)
            
            schema_filename = os.path.basename(schema_path)
            schema_name = schema_filename.replace('.schema.json', '')
            
            # Generate schema documentation content
            doc_content = schema_doc_renderer.generate_schema_documentation_html(schema_path, 'logical_model', output_dir)
            
            if doc_content:
                # Create individual HTML file using dak-api.html as template
                html_filename = f"{schema_name}.html"
                html_path = os.path.join(output_dir, html_filename)
                
                # Create HTML content using template
                title = schema.get('title', f"{schema_name} Schema Documentation")
                html_content = html_processor.create_html_template_from_existing(dak_api_html_path, title, doc_content)
                
                if html_content:
                    # Save the individual schema HTML file
                    with open(html_path, 'w', encoding='utf-8') as f:
                        f.write(html_content)
                    
                    logger.info(f"Created Logical Model schema HTML: {html_path}")
                    
                    schema_docs['logical_model'].append({
                        'title': title,
                        'description': schema.get('description', 'Logical Model schema documentation'),
                        'html_file': html_filename
                    })
                
        except Exception as e:
            logger.error(f"Error processing Logical Model schema {schema_path}: {e}")
    
    # Process existing OpenAPI files (if any)
    openapi_docs = []
    for openapi_path in openapi_files:
        try:
            # For now, just note them - could add OpenAPI documentation generation here
            openapi_filename = os.path.basename(openapi_path)
            openapi_docs.append({
                'title': f"{openapi_filename} API",
                'description': f"API documentation from {openapi_filename}",
                'html_file': f"{openapi_filename}.html"  # Would need to create this
            })
        except Exception as e:
            logger.error(f"Error processing OpenAPI file {openapi_path}: {e}")
    
    # Create enumeration endpoints for ValueSets and LogicalModels
    enumeration_docs = []
    
    # Create ValueSets enumeration endpoint if we have ValueSet schemas
    if schemas['valueset']:
        valueset_enum_path = hub_generator.create_enumeration_schema('valueset', schemas['valueset'], output_dir)
        if valueset_enum_path:
            # Generate enumeration documentation content
            doc_content = schema_doc_renderer.generate_schema_documentation_html(valueset_enum_path, 'valueset', output_dir)
            
            if doc_content:
                # Create enumeration HTML file
                html_filename = "ValueSets-enumeration.html"
                html_path = os.path.join(output_dir, html_filename)
                
                title = "ValueSets Enumeration API Documentation"
                html_content = html_processor.create_html_template_from_existing(dak_api_html_path, title, doc_content)
                
                if html_content:
                    with open(html_path, 'w', encoding='utf-8') as f:
                        f.write(html_content)
                    
                    logger.info(f"Created ValueSets enumeration HTML: {html_path}")
                    
                    enumeration_docs.append({
                        'title': 'ValueSets.schema.json',
                        'description': 'Enumeration of all available ValueSet schemas',
                        'html_file': html_filename,
                        'type': 'enumeration-valueset'
                    })
    
    # Create LogicalModels enumeration endpoint if we have LogicalModel schemas  
    if schemas['logical_model']:
        logicalmodel_enum_path = hub_generator.create_enumeration_schema('logical_model', schemas['logical_model'], output_dir)
        if logicalmodel_enum_path:
            # Generate enumeration documentation content
            doc_content = schema_doc_renderer.generate_schema_documentation_html(logicalmodel_enum_path, 'logical_model', output_dir)
            
            if doc_content:
                # Create enumeration HTML file
                html_filename = "LogicalModels-enumeration.html"
                html_path = os.path.join(output_dir, html_filename)
                
                title = "LogicalModels Enumeration API Documentation"
                html_content = html_processor.create_html_template_from_existing(dak_api_html_path, title, doc_content)
                
                if html_content:
                    with open(html_path, 'w', encoding='utf-8') as f:
                        f.write(html_content)
                    
                    logger.info(f"Created LogicalModels enumeration HTML: {html_path}")
                    
                    enumeration_docs.append({
                        'title': 'LogicalModels.schema.json',
                        'description': 'Enumeration of all available Logical Model schemas',
                        'html_file': html_filename,
                        'type': 'enumeration-logicalmodel'
                    })
    
    # Process JSON-LD vocabulary files
    jsonld_docs = []
    for jsonld_path in jsonld_files:
        try:
            # Load JSON-LD vocabulary to get metadata
            with open(jsonld_path, 'r', encoding='utf-8') as f:
                jsonld_vocab = json.load(f)
            
            jsonld_filename = os.path.basename(jsonld_path)
            
            # Extract title and description from the enumeration class in the @graph
            title = jsonld_filename
            description = "JSON-LD vocabulary for ValueSet enumeration"
            
            if '@graph' in jsonld_vocab and isinstance(jsonld_vocab['@graph'], list):
                for item in jsonld_vocab['@graph']:
                    if isinstance(item, dict) and item.get('type') == 'schema:Enumeration':
                        if 'name' in item:
                            title = f"{item['name']} JSON-LD Vocabulary"
                        if 'comment' in item:
                            description = item['comment']
                        break
            
            jsonld_docs.append({
                'title': title,
                'description': description,
                'filename': jsonld_filename
            })
            
            logger.info(f"Added JSON-LD vocabulary to documentation: {jsonld_filename}")
            
        except Exception as e:
            logger.error(f"Error processing JSON-LD vocabulary {jsonld_path}: {e}")
    
    # Post-process the DAK API hub
    success = hub_generator.post_process_dak_api_html(output_dir, schema_docs, openapi_docs, enumeration_docs, jsonld_docs)
    
    if success:
        total_docs = len(schema_docs['valueset']) + len(schema_docs['logical_model']) + len(openapi_docs) + len(enumeration_docs) + len(jsonld_docs)
        logger.info(f"Successfully post-processed DAK API hub with {total_docs} documentation pages")
        sys.exit(0)
    else:
        logger.error("Failed to post-process DAK API hub")
        sys.exit(1)


if __name__ == "__main__":
    main()