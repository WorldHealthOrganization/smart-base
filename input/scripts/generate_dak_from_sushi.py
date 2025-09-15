#!/usr/bin/env python3
"""
Generate dak.json from sushi-config.yaml

This script processes an existing FHIR Implementation Guide sushi-config.yaml file
and generates a corresponding dak.json file that serves as the primary DAK indicator.
It uses only the Python standard library and YAML parsing to avoid dependency on SUSHI.

Usage:
    python generate_dak_from_sushi.py [path_to_sushi_config] [output_path]
    
If no paths are provided, it looks for sushi-config.yaml in the current directory
and outputs dak.json to the current directory.
"""

import json
import sys
import yaml
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List, Optional


def load_sushi_config(config_path: Path) -> Dict[str, Any]:
    """Load and parse the sushi-config.yaml file."""
    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Error: sushi-config.yaml not found at {config_path}")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        sys.exit(1)


def convert_publisher(sushi_publisher: Any) -> Dict[str, str]:
    """Convert publisher information from sushi config to DAK format."""
    if isinstance(sushi_publisher, dict):
        return {
            "name": sushi_publisher.get("name", ""),
            "url": sushi_publisher.get("url", ""),
            **({"email": sushi_publisher["email"]} if sushi_publisher.get("email") else {})
        }
    elif isinstance(sushi_publisher, str):
        return {"name": sushi_publisher}
    else:
        return {"name": ""}


def convert_dependencies(sushi_deps: Dict[str, Any]) -> List[Dict[str, str]]:
    """Convert dependencies from sushi config to DAK format."""
    dependencies = []
    
    # Default reasons for common dependencies
    default_reasons = {
        "hl7.terminology": "Required terminology definitions",
        "hl7.fhir.uv.extensions.r4": "Standard FHIR extensions for R4",
        "hl7.fhir.uv.extensions.r5": "Standard FHIR extensions for R5"
    }
    
    for dep_id, dep_info in sushi_deps.items():
        if isinstance(dep_info, dict):
            dep_name = dep_info.get("id", dep_id)
            reason = dep_info.get("reason", default_reasons.get(dep_name, ""))
            dependencies.append({
                "id": dep_name,
                "version": dep_info.get("version", ""),
                "reason": reason
            })
        elif isinstance(dep_info, str):
            reason = default_reasons.get(dep_id, "")
            dependencies.append({
                "id": dep_id,
                "version": dep_info,
                "reason": reason
            })
    return dependencies


def convert_pages(sushi_pages: Dict[str, Any]) -> List[Dict[str, str]]:
    """Convert pages from sushi config to DAK format."""
    pages = []
    for filename, page_info in sushi_pages.items():
        if isinstance(page_info, dict):
            pages.append({
                "filename": filename,
                "title": page_info.get("title", filename)
            })
        else:
            pages.append({
                "filename": filename,
                "title": str(page_info) if page_info else filename
            })
    return pages


def convert_menu(sushi_menu: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Convert menu structure from sushi config to DAK format."""
    menu = []
    for title, url_or_submenu in sushi_menu.items():
        if isinstance(url_or_submenu, str):
            menu.append({
                "title": title,
                "url": url_or_submenu
            })
        elif isinstance(url_or_submenu, dict):
            menu_item = {
                "title": title,
                "url": "#",
                "subItems": []
            }
            for sub_title, sub_url in url_or_submenu.items():
                menu_item["subItems"].append({
                    "title": sub_title,
                    "url": sub_url
                })
            menu.append(menu_item)
    return menu


def convert_jurisdiction(jurisdiction_list: Optional[List[str]]) -> List[Dict[str, Any]]:
    """Convert jurisdiction from sushi config to DAK format."""
    if not jurisdiction_list:
        return [{
            "coding": [{
                "system": "urn:iso:std:iso:3166",
                "code": "001",
                "display": "World"
            }]
        }]
    
    jurisdictions = []
    for j in jurisdiction_list:
        # Parse jurisdiction strings like "urn:iso:std:iso:3166#US"
        if "#" in j:
            system, code = j.split("#", 1)
            jurisdictions.append({
                "coding": [{
                    "system": system,
                    "code": code
                }]
            })
        else:
            jurisdictions.append({
                "coding": [{
                    "system": "urn:iso:std:iso:3166",
                    "code": j
                }]
            })
    return jurisdictions


def generate_dak_json(sushi_config: Dict[str, Any]) -> Dict[str, Any]:
    """Generate dak.json structure from sushi-config.yaml."""
    
    # Core DAK identity (mapped from sushi config)
    dak = {
        "resourceType": "DAK",
        "resourceDefinition": "http://smart.who.int/base/StructureDefinition/DAK",
        "id": sushi_config.get("id", ""),
        "name": sushi_config.get("name", ""),
        "title": sushi_config.get("title", ""),
        "description": sushi_config.get("description", ""),
        "version": sushi_config.get("version", "0.1.0"),
        "status": sushi_config.get("status", "draft"),
        "publicationUrl": sushi_config.get("canonical", ""),
        "license": sushi_config.get("license", "CC0-1.0"),
        "copyrightYear": sushi_config.get("copyrightYear", str(datetime.now().year)),
        "publisher": convert_publisher(sushi_config.get("publisher", {})),
        "experimental": sushi_config.get("experimental", False),
        "useContext": sushi_config.get("useContext", []),
        "jurisdiction": convert_jurisdiction(sushi_config.get("jurisdiction")),
        "fhirVersion": sushi_config.get("fhirVersion", "4.0.1"),
    }
    
    # Dependencies
    if sushi_config.get("dependencies"):
        dak["dependencies"] = convert_dependencies(sushi_config["dependencies"])
    else:
        dak["dependencies"] = []
    
    # Additional metadata
    dak.update({
        "releaseLabel": sushi_config.get("releaseLabel", "ci-build"),
        "date": datetime.now().strftime("%Y-%m-%d"),
        "contact": sushi_config.get("contact", [])
    })
    
    return dak


def main():
    """Main function to process command line arguments and generate dak.json."""
    
    # Parse command line arguments
    if len(sys.argv) > 1:
        sushi_path = Path(sys.argv[1])
    else:
        sushi_path = Path("sushi-config.yaml")
    
    if len(sys.argv) > 2:
        output_path = Path(sys.argv[2])
    else:
        output_path = Path("dak.json")
    
    # Check if sushi config exists
    if not sushi_path.exists():
        print(f"Error: {sushi_path} does not exist")
        sys.exit(1)
    
    print(f"Reading sushi configuration from: {sushi_path}")
    
    # Load and convert
    sushi_config = load_sushi_config(sushi_path)
    dak_config = generate_dak_json(sushi_config)
    
    # Write output
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            json.dump(dak_config, file, indent=2, ensure_ascii=False)
        print(f"Successfully generated DAK configuration: {output_path}")
        print(f"DAK ID: {dak_config['id']}")
        print(f"DAK Title: {dak_config['title']}")
        print(f"Publication URL: {dak_config['publicationUrl']}")
    except IOError as e:
        print(f"Error writing output file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()