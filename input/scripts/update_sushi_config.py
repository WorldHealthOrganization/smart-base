import yaml
import sys
import os
import json
import glob

def create_dak_api_md_if_needed():
    """Create dak-api.md file with proper content if it doesn't exist."""
    dak_api_path = 'input/pagecontent/dak-api.md'
    
    # Check if the file already exists
    if os.path.exists(dak_api_path):
        # Verify it has the required DAK_API_CONTENT marker
        try:
            with open(dak_api_path, 'r') as f:
                content = f.read()
            if '<!-- DAK_API_CONTENT -->' in content:
                print(f"dak-api.md already exists with proper content")
                return True
            else:
                print(f"dak-api.md exists but missing DAK_API_CONTENT marker, updating...")
        except Exception as e:
            print(f"Error reading existing dak-api.md: {e}")
    else:
        print(f"dak-api.md does not exist, creating...")
    
    # Create the directories if they don't exist
    os.makedirs(os.path.dirname(dak_api_path), exist_ok=True)
    
    # Create the dak-api.md content with the required marker
    dak_api_content = """# DAK API Documentation Hub

This page provides access to Data Access Kit (DAK) API documentation and schemas.

{: .no_toc}

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

<!-- DAK_API_CONTENT -->
"""
    
    try:
        with open(dak_api_path, 'w') as f:
            f.write(dak_api_content)
        print(f"Successfully created dak-api.md with DAK_API_CONTENT marker")
        return True
    except Exception as e:
        print(f"Error creating dak-api.md: {e}")
        return False

def scan_for_valuesets_and_create_placeholders():
    """
    Scan for ValueSet resources from fsh-generated and input/resources directories
    and create placeholder markdown files for the IG publisher to process.
    
    This runs after sushi but before the IG publisher.
    """
    try:
        valuesets = []
        logical_models = []
        
        # Scan fsh-generated directory (created by sushi)
        fsh_generated_dir = 'fsh-generated/resources'
        if os.path.exists(fsh_generated_dir):
            print(f"Scanning {fsh_generated_dir} for FHIR resources...")
            fhir_files = glob.glob(os.path.join(fsh_generated_dir, '*.json'))
            for fhir_file in fhir_files:
                try:
                    with open(fhir_file, 'r', encoding='utf-8') as f:
                        resource = json.load(f)
                    
                    resource_type = resource.get('resourceType', '')
                    resource_id = resource.get('id', '')
                    
                    if resource_type == 'ValueSet' and resource_id:
                        valuesets.append({
                            'id': resource_id,
                            'name': resource.get('name', resource_id),
                            'title': resource.get('title', resource_id),
                            'source_file': fhir_file
                        })
                        print(f"  Found ValueSet: {resource_id}")
                    elif resource_type == 'StructureDefinition' and resource_id:
                        kind = resource.get('kind', '')
                        if kind == 'logical':
                            logical_models.append({
                                'id': resource_id,
                                'name': resource.get('name', resource_id),
                                'title': resource.get('title', resource_id),
                                'source_file': fhir_file
                            })
                            print(f"  Found Logical Model: {resource_id}")
                            
                except Exception as e:
                    print(f"  Warning: Error reading {fhir_file}: {e}")
        
        # Scan input/resources directory (static FHIR resources)
        input_resources_dir = 'input/resources'
        if os.path.exists(input_resources_dir):
            print(f"Scanning {input_resources_dir} for FHIR resources...")
            fhir_files = glob.glob(os.path.join(input_resources_dir, '*.json'))
            for fhir_file in fhir_files:
                try:
                    with open(fhir_file, 'r', encoding='utf-8') as f:
                        resource = json.load(f)
                    
                    resource_type = resource.get('resourceType', '')
                    resource_id = resource.get('id', '')
                    
                    if resource_type == 'ValueSet' and resource_id:
                        # Check if already found in fsh-generated
                        if not any(vs['id'] == resource_id for vs in valuesets):
                            valuesets.append({
                                'id': resource_id,
                                'name': resource.get('name', resource_id),
                                'title': resource.get('title', resource_id),
                                'source_file': fhir_file
                            })
                            print(f"  Found ValueSet: {resource_id}")
                    elif resource_type == 'StructureDefinition' and resource_id:
                        kind = resource.get('kind', '')
                        if kind == 'logical':
                            # Check if already found in fsh-generated
                            if not any(lm['id'] == resource_id for lm in logical_models):
                                logical_models.append({
                                    'id': resource_id,
                                    'name': resource.get('name', resource_id),
                                    'title': resource.get('title', resource_id),
                                    'source_file': fhir_file
                                })
                                print(f"  Found Logical Model: {resource_id}")
                            
                except Exception as e:
                    print(f"  Warning: Error reading {fhir_file}: {e}")
        
        # Create placeholder markdown files for all found resources
        pagecontent_dir = 'input/pagecontent'
        os.makedirs(pagecontent_dir, exist_ok=True)
        
        created_files = []
        
        # Create placeholder files for ValueSets
        for valueset in valuesets:
            md_filename = f"ValueSet-{valueset['id']}.md"
            md_path = os.path.join(pagecontent_dir, md_filename)
            
            # Only create if doesn't exist or is empty placeholder
            should_create = True
            if os.path.exists(md_path):
                try:
                    with open(md_path, 'r', encoding='utf-8') as f:
                        existing_content = f.read().strip()
                    # Only recreate if it's empty or contains our placeholder marker
                    if existing_content and '<!-- DAK_API_PLACEHOLDER -->' not in existing_content:
                        should_create = False
                        print(f"  Skipping {md_filename} - already exists with content")
                except Exception:
                    pass
            
            if should_create:
                placeholder_content = f"""# {valueset['title']}

<!-- DAK_API_PLACEHOLDER: ValueSet-{valueset['id']} -->

{valueset.get('description', 'ValueSet documentation will be generated during post-processing.')}

---

*This content will be automatically updated during the DAK API documentation generation process.*
"""
                try:
                    with open(md_path, 'w', encoding='utf-8') as f:
                        f.write(placeholder_content)
                    created_files.append(md_filename)
                    print(f"  Created placeholder: {md_filename}")
                except Exception as e:
                    print(f"  Error creating {md_filename}: {e}")
        
        # Create placeholder files for Logical Models
        for logical_model in logical_models:
            md_filename = f"StructureDefinition-{logical_model['id']}.md"
            md_path = os.path.join(pagecontent_dir, md_filename)
            
            # Only create if doesn't exist or is empty placeholder
            should_create = True
            if os.path.exists(md_path):
                try:
                    with open(md_path, 'r', encoding='utf-8') as f:
                        existing_content = f.read().strip()
                    # Only recreate if it's empty or contains our placeholder marker
                    if existing_content and '<!-- DAK_API_PLACEHOLDER -->' not in existing_content:
                        should_create = False
                        print(f"  Skipping {md_filename} - already exists with content")
                except Exception:
                    pass
            
            if should_create:
                placeholder_content = f"""# {logical_model['title']}

<!-- DAK_API_PLACEHOLDER: StructureDefinition-{logical_model['id']} -->

{logical_model.get('description', 'Logical Model documentation will be generated during post-processing.')}

---

*This content will be automatically updated during the DAK API documentation generation process.*
"""
                try:
                    with open(md_path, 'w', encoding='utf-8') as f:
                        f.write(placeholder_content)
                    created_files.append(md_filename)
                    print(f"  Created placeholder: {md_filename}")
                except Exception as e:
                    print(f"  Error creating {md_filename}: {e}")
        
        print(f"Placeholder generation completed:")
        print(f"  Found {len(valuesets)} ValueSets")
        print(f"  Found {len(logical_models)} Logical Models")
        print(f"  Created {len(created_files)} placeholder files")
        
        return len(created_files) > 0
        
    except Exception as e:
        print(f"Error during valueset scanning and placeholder creation: {e}")
        return False

def update_sushi_config():
    config_updated = False
    
    try:
        with open('sushi-config.yaml', 'r') as f:
            config = yaml.safe_load(f)
        
        # Check if this is the smart-base repository or if smart-base is listed as a dependency
        repo_id = config.get('id', '')
        is_smart_base_repo = repo_id == 'smart.who.int.base'
        
        smart_base_found = is_smart_base_repo
        
        if is_smart_base_repo:
            print(f"This is the smart-base repository (id: {repo_id})")
        else:
            # Check if smart-base is listed as a dependency
            dependencies = config.get('dependencies', {})
            
            # Check for various possible smart-base dependency names
            smart_base_patterns = [
                'smart-base',
                'smart.who.int.base',
                'who.smart.base',
                'smart.base'
            ]
            
            for dep_name in dependencies.keys():
                for pattern in smart_base_patterns:
                    if pattern in dep_name.lower():
                        smart_base_found = True
                        print(f"Found smart-base dependency: {dep_name}")
                        break
                if smart_base_found:
                    break
        
        if not smart_base_found:
            print("This is not the smart-base repository and smart-base is not listed as a dependency. Skipping DAK API configuration.")
            return False
        
        # Create dak-api.md if needed before processing sushi config
        if not create_dak_api_md_if_needed():
            print("Failed to create dak-api.md, but continuing with sushi-config processing...")
        
        # Scan for valuesets and logical models, create placeholder markdown files
        # This ensures the IG publisher will process these files into HTML
        scan_for_valuesets_and_create_placeholders()
        
        # Ensure pages section exists
        if 'pages' not in config:
            config['pages'] = {}
        
        # Check if dak-api.md is registered in pages
        if 'dak-api.md' not in config['pages']:
            config['pages']['dak-api.md'] = {'title': 'DAK API Documentation Hub'}
            config_updated = True
            print("Added dak-api.md to pages section")
        
        # Ensure menu section exists
        if 'menu' not in config:
            config['menu'] = {}
        
        # Ensure Indices subsection exists under menu
        if 'Indices' not in config['menu']:
            config['menu']['Indices'] = {}
        
        # Check if DAK API is registered in menu -> Indices
        if 'DAK API' not in config['menu']['Indices']:
            config['menu']['Indices']['DAK API'] = 'dak-api.html'
            config_updated = True
            print("Added DAK API to menu Indices section")
        
        # Write back the updated config if changes were made
        if config_updated:
            with open('sushi-config.yaml', 'w') as f:
                yaml.dump(config, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
            print("sushi-config.yaml updated successfully")
            return True
        else:
            print("sushi-config.yaml already contains required DAK API entries")
            return False
            
    except Exception as e:
        print(f"Error updating sushi-config.yaml: {e}")
        return False

if __name__ == "__main__":
    sys.exit(0 if update_sushi_config() else 1)