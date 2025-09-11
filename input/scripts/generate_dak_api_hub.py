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


class ReDocRenderer:
    """Generates self-contained HTML files for OpenAPI specifications and JSON schemas."""
    
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
    
    def generate_hub(self, output_dir: str, schema_docs: Dict[str, List[Dict]], openapi_docs: List[Dict], enumeration_docs: List[Dict] = None) -> bool:
        """
        Generate the unified DAK API documentation by updating the dak-api.md file.
        
        Args:
            output_dir: Directory to save the hub file
            schema_docs: Dictionary with schema documentation info
            openapi_docs: List of OpenAPI documentation info
            enumeration_docs: List of enumeration endpoint documentation info
            
        Returns:
            True if successful, False otherwise
        """
        try:
            if enumeration_docs is None:
                enumeration_docs = []
            
            # Update dak-api.md instead of creating standalone HTML
            pagecontent_dir = os.path.join(os.path.dirname(output_dir), "input", "pagecontent")
            if not os.path.exists(pagecontent_dir):
                # Fallback: try to find pagecontent relative to current location
                pagecontent_dir = os.path.join(os.getcwd(), "input", "pagecontent")
            
            if not os.path.exists(pagecontent_dir):
                self.logger.error(f"Could not find pagecontent directory. Tried: {pagecontent_dir}")
                return False
                
            dak_api_md_path = os.path.join(pagecontent_dir, "dak-api.md")
            
            
            # Generate Markdown content for IG integration
            markdown_content = """# DAK API Documentation Hub

<!-- This content is automatically generated by the DAK API Documentation Hub Generator -->

This Digital Adaptation Kit (DAK) API documentation provides programmatic access to the ValueSet schemas and Logical Model schemas defined in this implementation guide.

<div class="dak-api-content">
"""
            
            # Add enumeration endpoints section
            if enumeration_docs:
                # Sort enumeration docs alphabetically by title
                sorted_enumeration_docs = sorted(enumeration_docs, key=lambda x: x['title'])
                markdown_content += """
## API Enumeration Endpoints

These endpoints provide dynamic lists of all available schemas in this implementation guide.

<div class="card-grid">
"""
                for doc in sorted_enumeration_docs:
                    # Determine type label and description
                    if doc.get('type') == 'enumeration-valueset':
                        type_label = "ValueSets Enumeration"
                        icon = "📋"
                    elif doc.get('type') == 'enumeration-logicalmodel':
                        type_label = "LogicalModels Enumeration"
                        icon = "🏗️"
                    else:
                        type_label = "Enumeration"
                        icon = "📊"
                    
                    markdown_content += f"""
<div class="api-card enumeration">
  <div class="card-header">
    <span class="card-icon">{icon}</span>
    <span class="card-type">{type_label}</span>
  </div>
  <h3><a href="{doc['html_file']}">{doc['title']}</a></h3>
  <p>{doc['description']}</p>
  <div class="card-actions">
    <a href="{doc['html_file']}" class="btn btn-primary">View API Documentation</a>
  </div>
</div>
"""
                markdown_content += """
</div>
"""
            
            # Add ValueSet schemas section
            if schema_docs.get('valueset'):
                # Sort ValueSet schemas alphabetically by title
                sorted_valueset_docs = sorted(schema_docs['valueset'], key=lambda x: x['title'])
                markdown_content += """
## ValueSet Schemas

Individual ValueSet schemas provide enumerated code lists for specific value domains.

<div class="card-grid">
"""
                for doc in sorted_valueset_docs:
                    markdown_content += f"""
<div class="api-card valueset">
  <div class="card-header">
    <span class="card-icon">🎯</span>
    <span class="card-type">ValueSet</span>
  </div>
  <h3><a href="{doc['html_file']}">{doc['title']}</a></h3>
  <p>{doc['description']}</p>
  <div class="card-actions">
    <a href="{doc['html_file']}" class="btn btn-primary">View Schema Documentation</a>
  </div>
</div>
"""
                markdown_content += """
</div>
"""
            
            # Add Logical Model schemas section
            if schema_docs.get('logical_model'):
                # Sort Logical Model schemas alphabetically by title
                sorted_logical_model_docs = sorted(schema_docs['logical_model'], key=lambda x: x['title'])
                markdown_content += """
## Logical Model Schemas

Logical Model schemas define the structure and constraints for data models used in this implementation guide.

<div class="card-grid">
"""
                for doc in sorted_logical_model_docs:
                    markdown_content += f"""
<div class="api-card logical-model">
  <div class="card-header">
    <span class="card-icon">🏗️</span>
    <span class="card-type">Logical Model</span>
  </div>
  <h3><a href="{doc['html_file']}">{doc['title']}</a></h3>
  <p>{doc['description']}</p>
  <div class="card-actions">
    <a href="{doc['html_file']}" class="btn btn-primary">View Schema Documentation</a>
  </div>
</div>
"""
                markdown_content += """
</div>
"""
            
            # Add OpenAPI specifications section
            if openapi_docs:
                # Sort OpenAPI docs alphabetically by title
                sorted_openapi_docs = sorted(openapi_docs, key=lambda x: x['title'])
                markdown_content += """
## OpenAPI Specifications

Additional API specifications beyond the core ValueSet and Logical Model schemas.

<div class="card-grid">
"""
                for doc in sorted_openapi_docs:
                    markdown_content += f"""
<div class="api-card openapi">
  <div class="card-header">
    <span class="card-icon">⚙️</span>
    <span class="card-type">OpenAPI</span>
  </div>
  <h3><a href="{doc['html_file']}">{doc['title']}</a></h3>
  <p>{doc['description']}</p>
  <div class="card-actions">
    <a href="{doc['html_file']}" class="btn btn-primary">View API Documentation</a>
  </div>
</div>
"""
                markdown_content += """
</div>
"""
            
            # Add empty state if no documentation
            if not schema_docs.get('valueset') and not schema_docs.get('logical_model') and not openapi_docs and not enumeration_docs:
                markdown_content += """
## No API Documentation Available

No API documentation found. Run the schema generation scripts first to generate documentation:

1. `Generate ValueSet JSON Schemas`
2. `Generate Logical Model JSON Schemas` 
3. `Generate DAK API Documentation Hub`

These scripts are part of the GitHub workflow build process.
"""
            
            markdown_content += """
</div>

<style>
/* DAK API Styling that integrates with IG theme */
.dak-api-content {
  margin-top: 1rem;
}

.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
  margin: 1.5rem 0;
}

.api-card {
  border: 1px solid #dee2e6;
  border-radius: 8px;
  background: #fff;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  transition: all 0.2s ease;
  overflow: hidden;
}

.api-card:hover {
  border-color: #00477d;
  box-shadow: 0 4px 12px rgba(0,71,125,0.15);
  transform: translateY(-2px);
}

.card-header {
  display: flex;
  align-items: center;
  padding: 1rem;
  background: #f8f9fa;
  border-bottom: 1px solid #dee2e6;
}

.card-icon {
  font-size: 1.5rem;
  margin-right: 0.75rem;
}

.card-type {
  background: #00477d;
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 4px;
  font-size: 0.875rem;
  font-weight: 500;
  text-transform: uppercase;
}

.api-card.enumeration .card-type {
  background: #607d8b;
}

.api-card.valueset .card-type {
  background: #17a2b8;
}

.api-card.logical-model .card-type {
  background: #6f42c1;
}

.api-card.openapi .card-type {
  background: #fd7e14;
}

.api-card h3 {
  margin: 1rem 1rem 0.5rem 1rem;
  font-size: 1.25rem;
  font-weight: 600;
}

.api-card h3 a {
  color: #00477d;
  text-decoration: none;
}

.api-card h3 a:hover {
  text-decoration: underline;
}

.api-card p {
  margin: 0 1rem 1rem 1rem;
  color: #6c757d;
  line-height: 1.5;
}

.card-actions {
  padding: 1rem;
  border-top: 1px solid #f1f3f4;
  background: #fafbfc;
}

.btn {
  display: inline-block;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  text-decoration: none;
  font-weight: 500;
  transition: all 0.2s ease;
  border: 1px solid transparent;
}

.btn-primary {
  background-color: #00477d;
  color: white;
  border-color: #00477d;
}

.btn-primary:hover {
  background-color: #003a68;
  border-color: #003a68;
  color: white;
  text-decoration: none;
}

/* Responsive design */
@media (max-width: 768px) {
  .card-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }
}
</style>

---

*This documentation is automatically generated from the schemas and specifications defined in this implementation guide.*
"""
            
            # Save markdown content to dak-api.md
            with open(dak_api_md_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            
            self.logger.info(f"Updated DAK API markdown: {dak_api_md_path}")
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
                                                             f"{schema.get('title', 'ValueSet')} Documentation", 'valueset')
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
                                                             f"{schema.get('title', 'Logical Model')} Documentation", 'logical_model')
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
    
    # Create enumeration endpoints for ValueSets and LogicalModels
    enumeration_docs = []
    
    # Create ValueSets enumeration endpoint if we have ValueSet schemas
    if schemas['valueset']:
        valueset_enum_path = hub_generator.create_enumeration_schema('valueset', schemas['valueset'], output_dir)
        if valueset_enum_path:
            # Create OpenAPI wrapper for ValueSets enumeration
            valueset_enum_wrapper = openapi_wrapper.create_enumeration_wrapper(valueset_enum_path, 'valueset', output_dir)
            if valueset_enum_wrapper:
                # Generate ReDoc HTML for ValueSets enumeration
                valueset_enum_html = redoc_renderer.generate_redoc_html(valueset_enum_wrapper, output_dir,
                                                                       "ValueSets Enumeration API Documentation", 'valueset')
                if valueset_enum_html:
                    enumeration_docs.append({
                        'title': 'ValueSets.schema.json',
                        'description': 'Enumeration of all available ValueSet schemas',
                        'html_file': os.path.basename(valueset_enum_html),
                        'type': 'enumeration-valueset'
                    })
    
    # Create LogicalModels enumeration endpoint if we have LogicalModel schemas  
    if schemas['logical_model']:
        logicalmodel_enum_path = hub_generator.create_enumeration_schema('logical_model', schemas['logical_model'], output_dir)
        if logicalmodel_enum_path:
            # Create OpenAPI wrapper for LogicalModels enumeration
            logicalmodel_enum_wrapper = openapi_wrapper.create_enumeration_wrapper(logicalmodel_enum_path, 'logical_model', output_dir)
            if logicalmodel_enum_wrapper:
                # Generate ReDoc HTML for LogicalModels enumeration
                logicalmodel_enum_html = redoc_renderer.generate_redoc_html(logicalmodel_enum_wrapper, output_dir,
                                                                           "LogicalModels Enumeration API Documentation", 'logical_model')
                if logicalmodel_enum_html:
                    enumeration_docs.append({
                        'title': 'LogicalModels.schema.json',
                        'description': 'Enumeration of all available Logical Model schemas',
                        'html_file': os.path.basename(logicalmodel_enum_html),
                        'type': 'enumeration-logicalmodel'
                    })
    
    # Generate the unified hub
    success = hub_generator.generate_hub(output_dir, schema_docs, openapi_docs, enumeration_docs)
    
    if success:
        total_docs = len(schema_docs['valueset']) + len(schema_docs['logical_model']) + len(openapi_docs) + len(enumeration_docs)
        logger.info(f"Successfully generated DAK API hub with {total_docs} documentation pages")
        sys.exit(0)
    else:
        logger.error("Failed to generate DAK API hub")
        sys.exit(1)


if __name__ == "__main__":
    main()