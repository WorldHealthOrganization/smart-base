import yaml
import sys

def update_sushi_config():
    config_updated = False
    
    try:
        with open('sushi-config.yaml', 'r') as f:
            config = yaml.safe_load(f)
        
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