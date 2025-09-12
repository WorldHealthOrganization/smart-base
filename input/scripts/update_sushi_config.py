import yaml
import sys
import os

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