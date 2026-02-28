import yaml
import sys
import os
import json
import glob
import re
from datetime import datetime
from typing import Dict, List, Any, Optional


# FSH parsing regex patterns
LOGICAL_PATTERN = r'^Logical:\s+(\S+)'
VALUESET_PATTERN = r'^ValueSet:\s+(\S+)'
TITLE_PATTERN = r'^Title:\s*"([^"]+)"'
DESCRIPTION_PATTERN = r'^Description:\s*"([^"]+)"'


class QAReporter:
    """Handles QA reporting for pre-processing and post-processing steps."""
    
    def __init__(self, phase: str = "preprocessing"):
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
        """Finalize the QA report with summary statistics."""
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
        return self.report
    
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

def create_dak_api_md_if_needed(qa_reporter: QAReporter):
    """Create dak-api.md file with proper content if it doesn't exist."""
    dak_api_path = 'input/pagecontent/dak-api.md'
    qa_reporter.add_file_expected(dak_api_path)
    
    # Check if the file already exists
    if os.path.exists(dak_api_path):
        # Verify it has the required DAK_API_CONTENT marker
        try:
            with open(dak_api_path, 'r') as f:
                content = f.read()
            if '<!-- DAK_API_CONTENT -->' in content:
                print(f"dak-api.md already exists with proper content")
                qa_reporter.add_success("dak-api.md already exists with proper content marker")
                qa_reporter.add_file_processed(dak_api_path, "exists_valid")
                return True
            else:
                print(f"dak-api.md exists but missing DAK_API_CONTENT marker, updating...")
                qa_reporter.add_warning("dak-api.md exists but missing DAK_API_CONTENT marker, updating")
        except Exception as e:
            print(f"Error reading existing dak-api.md: {e}")
            qa_reporter.add_error(f"Error reading existing dak-api.md: {e}")
    else:
        print(f"dak-api.md does not exist, creating...")
        qa_reporter.add_warning("dak-api.md does not exist, creating new file")
    
    # Create the directories if they don't exist
    try:
        os.makedirs(os.path.dirname(dak_api_path), exist_ok=True)
        qa_reporter.add_success(f"Created directory structure for {dak_api_path}")
    except Exception as e:
        qa_reporter.add_error(f"Failed to create directory structure: {e}")
        return False
    
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
        qa_reporter.add_success("Successfully created dak-api.md with DAK_API_CONTENT marker")
        qa_reporter.add_file_processed(dak_api_path, "created")
        return True
    except Exception as e:
        print(f"Error creating dak-api.md: {e}")
        qa_reporter.add_error(f"Error creating dak-api.md: {e}")
        return False

def parse_fsh_file_for_logical_model(fsh_file: str, qa_reporter: QAReporter) -> Optional[Dict[str, str]]:
    """
    Parse a FSH file to extract Logical Model information.
    
    Returns a dictionary with 'id', 'name', 'title', and 'description' if found, None otherwise.
    """
    try:
        with open(fsh_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Look for Logical: declaration
        logical_match = re.search(LOGICAL_PATTERN, content, re.MULTILINE)
        if not logical_match:
            return None
        
        model_id = logical_match.group(1)
        
        # Extract title
        title_match = re.search(TITLE_PATTERN, content, re.MULTILINE)
        title = title_match.group(1) if title_match else model_id
        
        # Extract description
        desc_match = re.search(DESCRIPTION_PATTERN, content, re.MULTILINE)
        description = desc_match.group(1) if desc_match else ""
        
        return {
            'id': model_id,
            'name': model_id,
            'title': title,
            'description': description,
            'source_file': fsh_file
        }
    except Exception as e:
        qa_reporter.add_warning(f"Error parsing FSH file {fsh_file}: {e}")
        return None

def parse_fsh_file_for_valueset(fsh_file: str, qa_reporter: QAReporter) -> Optional[Dict[str, str]]:
    """
    Parse a FSH file to extract ValueSet information.
    
    Returns a dictionary with 'id', 'name', 'title', and 'description' if found, None otherwise.
    """
    try:
        with open(fsh_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Look for ValueSet: declaration
        valueset_match = re.search(VALUESET_PATTERN, content, re.MULTILINE)
        if not valueset_match:
            return None
        
        valueset_id = valueset_match.group(1)
        
        # Extract title
        title_match = re.search(TITLE_PATTERN, content, re.MULTILINE)
        title = title_match.group(1) if title_match else valueset_id
        
        # Extract description
        desc_match = re.search(DESCRIPTION_PATTERN, content, re.MULTILINE)
        description = desc_match.group(1) if desc_match else ""
        
        return {
            'id': valueset_id,
            'name': valueset_id,
            'title': title,
            'description': description,
            'source_file': fsh_file
        }
    except Exception as e:
        qa_reporter.add_warning(f"Error parsing FSH file {fsh_file}: {e}")
        return None

def scan_for_valuesets_and_create_placeholders(qa_reporter: QAReporter):
    """
    Scan for ValueSet and Logical Model resources from multiple directories:
    - fsh-generated/resources (JSON files created by SUSHI)
    - input/resources (static JSON FHIR resources)
    - input/fsh/models (FSH files defining Logical Models)
    - input/fsh/valuesets (FSH files defining ValueSets)
    - input/models (JSON StructureDefinition files)
    - input/vocabulary (JSON ValueSet files)
    
    Creates placeholder markdown files for the IG publisher to process.
    This runs after sushi but before the IG publisher.
    """
    try:
        valuesets = []
        logical_models = []
        
        # Scan fsh-generated directory (created by sushi)
        fsh_generated_dir = 'fsh-generated/resources'
        qa_reporter.add_file_expected(fsh_generated_dir)
        
        if os.path.exists(fsh_generated_dir):
            print(f"Scanning {fsh_generated_dir} for FHIR resources...")
            qa_reporter.add_success(f"Found directory: {fsh_generated_dir}")
            fhir_files = glob.glob(os.path.join(fsh_generated_dir, '*.json'))
            qa_reporter.add_success(f"Found {len(fhir_files)} JSON files in {fsh_generated_dir}")
            
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
                        qa_reporter.add_success(f"Found ValueSet: {resource_id}", 
                                               {"source_file": fhir_file, "title": resource.get('title', resource_id)})
                        qa_reporter.add_file_processed(fhir_file, "valueset_detected")
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
                            qa_reporter.add_success(f"Found Logical Model: {resource_id}",
                                                   {"source_file": fhir_file, "title": resource.get('title', resource_id)})
                            qa_reporter.add_file_processed(fhir_file, "logical_model_detected")
                    else:
                        qa_reporter.add_file_processed(fhir_file, "other_resource")
                            
                except Exception as e:
                    print(f"  Warning: Error reading {fhir_file}: {e}")
                    qa_reporter.add_warning(f"Error reading {fhir_file}: {e}")
                    qa_reporter.add_file_processed(fhir_file, "error")
        else:
            qa_reporter.add_warning(f"Directory not found: {fsh_generated_dir}")
        
        # Scan input/resources directory (static FHIR resources)
        input_resources_dir = 'input/resources'
        qa_reporter.add_file_expected(input_resources_dir)
        
        if os.path.exists(input_resources_dir):
            print(f"Scanning {input_resources_dir} for FHIR resources...")
            qa_reporter.add_success(f"Found directory: {input_resources_dir}")
            fhir_files = glob.glob(os.path.join(input_resources_dir, '*.json'))
            qa_reporter.add_success(f"Found {len(fhir_files)} JSON files in {input_resources_dir}")
            
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
                            qa_reporter.add_success(f"Found ValueSet (input/resources): {resource_id}",
                                                   {"source_file": fhir_file, "title": resource.get('title', resource_id)})
                            qa_reporter.add_file_processed(fhir_file, "valueset_detected")
                        else:
                            qa_reporter.add_warning(f"Duplicate ValueSet {resource_id} found in input/resources (already in fsh-generated)")
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
                                qa_reporter.add_success(f"Found Logical Model (input/resources): {resource_id}",
                                                       {"source_file": fhir_file, "title": resource.get('title', resource_id)})
                                qa_reporter.add_file_processed(fhir_file, "logical_model_detected")
                            else:
                                qa_reporter.add_warning(f"Duplicate Logical Model {resource_id} found in input/resources (already in fsh-generated)")
                    else:
                        qa_reporter.add_file_processed(fhir_file, "other_resource")
                            
                except Exception as e:
                    print(f"  Warning: Error reading {fhir_file}: {e}")
                    qa_reporter.add_warning(f"Error reading {fhir_file}: {e}")
                    qa_reporter.add_file_processed(fhir_file, "error")
        else:
            qa_reporter.add_warning(f"Directory not found: {input_resources_dir}")
        
        # Scan input/fsh/models directory for FSH files defining Logical Models
        input_fsh_models_dir = 'input/fsh/models'
        qa_reporter.add_file_expected(input_fsh_models_dir)
        
        if os.path.exists(input_fsh_models_dir):
            print(f"Scanning {input_fsh_models_dir} for FSH Logical Models...")
            qa_reporter.add_success(f"Found directory: {input_fsh_models_dir}")
            fsh_files = glob.glob(os.path.join(input_fsh_models_dir, '*.fsh'))
            qa_reporter.add_success(f"Found {len(fsh_files)} FSH files in {input_fsh_models_dir}")
            
            for fsh_file in fsh_files:
                logical_model = parse_fsh_file_for_logical_model(fsh_file, qa_reporter)
                if logical_model:
                    # Check if already found
                    if not any(lm['id'] == logical_model['id'] for lm in logical_models):
                        logical_models.append(logical_model)
                        print(f"  Found Logical Model from FSH: {logical_model['id']}")
                        qa_reporter.add_success(f"Found Logical Model from FSH: {logical_model['id']}",
                                               {"source_file": fsh_file, "title": logical_model['title']})
                        qa_reporter.add_file_processed(fsh_file, "logical_model_detected")
                    else:
                        qa_reporter.add_warning(f"Duplicate Logical Model {logical_model['id']} found in {input_fsh_models_dir}")
                else:
                    qa_reporter.add_file_processed(fsh_file, "not_logical_model")
        else:
            qa_reporter.add_warning(f"Directory not found: {input_fsh_models_dir}")
        
        # Scan input/fsh/valuesets directory for FSH files defining ValueSets
        input_fsh_valuesets_dir = 'input/fsh/valuesets'
        qa_reporter.add_file_expected(input_fsh_valuesets_dir)
        
        if os.path.exists(input_fsh_valuesets_dir):
            print(f"Scanning {input_fsh_valuesets_dir} for FSH ValueSets...")
            qa_reporter.add_success(f"Found directory: {input_fsh_valuesets_dir}")
            fsh_files = glob.glob(os.path.join(input_fsh_valuesets_dir, '*.fsh'))
            qa_reporter.add_success(f"Found {len(fsh_files)} FSH files in {input_fsh_valuesets_dir}")
            
            for fsh_file in fsh_files:
                valueset = parse_fsh_file_for_valueset(fsh_file, qa_reporter)
                if valueset:
                    # Check if already found
                    if not any(vs['id'] == valueset['id'] for vs in valuesets):
                        valuesets.append(valueset)
                        print(f"  Found ValueSet from FSH: {valueset['id']}")
                        qa_reporter.add_success(f"Found ValueSet from FSH: {valueset['id']}",
                                               {"source_file": fsh_file, "title": valueset['title']})
                        qa_reporter.add_file_processed(fsh_file, "valueset_detected")
                    else:
                        qa_reporter.add_warning(f"Duplicate ValueSet {valueset['id']} found in {input_fsh_valuesets_dir}")
                else:
                    qa_reporter.add_file_processed(fsh_file, "not_valueset")
        else:
            qa_reporter.add_warning(f"Directory not found: {input_fsh_valuesets_dir}")
        
        # Scan input/models directory for JSON StructureDefinition files
        input_models_dir = 'input/models'
        qa_reporter.add_file_expected(input_models_dir)
        
        if os.path.exists(input_models_dir):
            print(f"Scanning {input_models_dir} for JSON StructureDefinition files...")
            qa_reporter.add_success(f"Found directory: {input_models_dir}")
            json_files = glob.glob(os.path.join(input_models_dir, '*.json'))
            qa_reporter.add_success(f"Found {len(json_files)} JSON files in {input_models_dir}")
            
            for json_file in json_files:
                try:
                    with open(json_file, 'r', encoding='utf-8') as f:
                        resource = json.load(f)
                    
                    resource_type = resource.get('resourceType', '')
                    resource_id = resource.get('id', '')
                    
                    if resource_type == 'StructureDefinition' and resource_id:
                        kind = resource.get('kind', '')
                        if kind == 'logical':
                            # Check if already found
                            if not any(lm['id'] == resource_id for lm in logical_models):
                                logical_models.append({
                                    'id': resource_id,
                                    'name': resource.get('name', resource_id),
                                    'title': resource.get('title', resource_id),
                                    'source_file': json_file
                                })
                                print(f"  Found Logical Model from JSON: {resource_id}")
                                qa_reporter.add_success(f"Found Logical Model from JSON (input/models): {resource_id}",
                                                       {"source_file": json_file, "title": resource.get('title', resource_id)})
                                qa_reporter.add_file_processed(json_file, "logical_model_detected")
                            else:
                                qa_reporter.add_warning(f"Duplicate Logical Model {resource_id} found in {input_models_dir}")
                    else:
                        qa_reporter.add_file_processed(json_file, "other_resource")
                except Exception as e:
                    print(f"  Warning: Error reading {json_file}: {e}")
                    qa_reporter.add_warning(f"Error reading {json_file}: {e}")
                    qa_reporter.add_file_processed(json_file, "error")
        else:
            qa_reporter.add_warning(f"Directory not found: {input_models_dir}")
        
        # Scan input/vocabulary directory for JSON ValueSet files
        input_vocabulary_dir = 'input/vocabulary'
        qa_reporter.add_file_expected(input_vocabulary_dir)
        
        if os.path.exists(input_vocabulary_dir):
            print(f"Scanning {input_vocabulary_dir} for JSON ValueSet files...")
            qa_reporter.add_success(f"Found directory: {input_vocabulary_dir}")
            json_files = glob.glob(os.path.join(input_vocabulary_dir, '*.json'))
            qa_reporter.add_success(f"Found {len(json_files)} JSON files in {input_vocabulary_dir}")
            
            for json_file in json_files:
                try:
                    with open(json_file, 'r', encoding='utf-8') as f:
                        resource = json.load(f)
                    
                    resource_type = resource.get('resourceType', '')
                    resource_id = resource.get('id', '')
                    
                    if resource_type == 'ValueSet' and resource_id:
                        # Check if already found
                        if not any(vs['id'] == resource_id for vs in valuesets):
                            valuesets.append({
                                'id': resource_id,
                                'name': resource.get('name', resource_id),
                                'title': resource.get('title', resource_id),
                                'source_file': json_file
                            })
                            print(f"  Found ValueSet from JSON: {resource_id}")
                            qa_reporter.add_success(f"Found ValueSet from JSON (input/vocabulary): {resource_id}",
                                                   {"source_file": json_file, "title": resource.get('title', resource_id)})
                            qa_reporter.add_file_processed(json_file, "valueset_detected")
                        else:
                            qa_reporter.add_warning(f"Duplicate ValueSet {resource_id} found in {input_vocabulary_dir}")
                    else:
                        qa_reporter.add_file_processed(json_file, "other_resource")
                except Exception as e:
                    print(f"  Warning: Error reading {json_file}: {e}")
                    qa_reporter.add_warning(f"Error reading {json_file}: {e}")
                    qa_reporter.add_file_processed(json_file, "error")
        else:
            qa_reporter.add_warning(f"Directory not found: {input_vocabulary_dir}")
        
        # Create placeholder markdown files for all found resources
        pagecontent_dir = 'input/pagecontent'
        try:
            os.makedirs(pagecontent_dir, exist_ok=True)
            qa_reporter.add_success(f"Ensured directory exists: {pagecontent_dir}")
        except Exception as e:
            qa_reporter.add_error(f"Failed to create directory {pagecontent_dir}: {e}")
            return False
        
        created_files = []
        
        # Create placeholder files for ValueSets
        for valueset in valuesets:
            md_filename = f"ValueSet-{valueset['id']}.md"
            md_path = os.path.join(pagecontent_dir, md_filename)
            qa_reporter.add_file_expected(md_path)
            
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
                        qa_reporter.add_warning(f"Skipping {md_filename} - already exists with content")
                        qa_reporter.add_file_processed(md_path, "skipped_existing")
                except Exception as e:
                    qa_reporter.add_warning(f"Error checking existing file {md_path}: {e}")
            
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
                    qa_reporter.add_success(f"Created placeholder: {md_filename}")
                    qa_reporter.add_file_processed(md_path, "created")
                except Exception as e:
                    print(f"  Error creating {md_filename}: {e}")
                    qa_reporter.add_error(f"Error creating {md_filename}: {e}")
        
        # Create placeholder files for Logical Models
        for logical_model in logical_models:
            md_filename = f"StructureDefinition-{logical_model['id']}.md"
            md_path = os.path.join(pagecontent_dir, md_filename)
            qa_reporter.add_file_expected(md_path)
            
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
                        qa_reporter.add_warning(f"Skipping {md_filename} - already exists with content")
                        qa_reporter.add_file_processed(md_path, "skipped_existing")
                except Exception as e:
                    qa_reporter.add_warning(f"Error checking existing file {md_path}: {e}")
            
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
                    qa_reporter.add_success(f"Created placeholder: {md_filename}")
                    qa_reporter.add_file_processed(md_path, "created")
                except Exception as e:
                    print(f"  Error creating {md_filename}: {e}")
                    qa_reporter.add_error(f"Error creating {md_filename}: {e}")
        
        print(f"Placeholder generation completed:")
        print(f"  Found {len(valuesets)} ValueSets")
        print(f"  Found {len(logical_models)} Logical Models")
        print(f"  Created {len(created_files)} placeholder files")
        
        qa_reporter.add_success("Placeholder generation completed", {
            "valuesets_found": len(valuesets),
            "logical_models_found": len(logical_models),
            "placeholder_files_created": len(created_files)
        })
        
        return len(created_files) > 0
        
    except Exception as e:
        print(f"Error during valueset scanning and placeholder creation: {e}")
        qa_reporter.add_error(f"Error during valueset scanning and placeholder creation: {e}")
        return False

def update_sushi_config(qa_reporter: QAReporter):
    config_updated = False
    sushi_config_path = 'sushi-config.yaml'
    qa_reporter.add_file_expected(sushi_config_path)
    
    try:
        with open(sushi_config_path, 'r') as f:
            config = yaml.safe_load(f)
        qa_reporter.add_success("Successfully loaded sushi-config.yaml")
        qa_reporter.add_file_processed(sushi_config_path, "loaded")
        
        # Check if this is the smart-base repository or if smart-base is listed as a dependency
        repo_id = config.get('id', '')
        is_smart_base_repo = repo_id == 'smart.who.int.base'
        
        smart_base_found = is_smart_base_repo
        
        if is_smart_base_repo:
            print(f"This is the smart-base repository (id: {repo_id})")
            qa_reporter.add_success(f"Detected smart-base repository (id: {repo_id})")
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
                        qa_reporter.add_success(f"Found smart-base dependency: {dep_name}")
                        break
                if smart_base_found:
                    break
        
        if not smart_base_found:
            print("This is not the smart-base repository and smart-base is not listed as a dependency. Skipping DAK API configuration.")
            qa_reporter.add_warning("This is not the smart-base repository and smart-base is not listed as a dependency. Skipping DAK API configuration.")
            return False
        
        # Create dak-api.md if needed before processing sushi config
        if not create_dak_api_md_if_needed(qa_reporter):
            print("Failed to create dak-api.md, but continuing with sushi-config processing...")
            qa_reporter.add_warning("Failed to create dak-api.md, but continuing with sushi-config processing")
        
        # Scan for valuesets and logical models, create placeholder markdown files
        # This ensures the IG publisher will process these files into HTML
        scan_for_valuesets_and_create_placeholders(qa_reporter)
        
        # Ensure pages section exists
        if 'pages' not in config:
            config['pages'] = {}
            qa_reporter.add_success("Created pages section in sushi-config.yaml")
        
        # Check if dak-api.md is registered in pages
        if 'dak-api.md' not in config['pages']:
            config['pages']['dak-api.md'] = {'title': 'DAK API Documentation Hub'}
            config_updated = True
            print("Added dak-api.md to pages section")
            qa_reporter.add_success("Added dak-api.md to pages section")
        else:
            qa_reporter.add_success("dak-api.md already exists in pages section")
        
        # Ensure menu section exists
        if 'menu' not in config:
            config['menu'] = {}
            qa_reporter.add_success("Created menu section in sushi-config.yaml")
        
        # Ensure Indices subsection exists under menu
        if 'Indices' not in config['menu']:
            config['menu']['Indices'] = {}
            qa_reporter.add_success("Created Indices subsection in menu")
        
        # Check if DAK API is registered in menu -> Indices
        if 'DAK API' not in config['menu']['Indices']:
            config['menu']['Indices']['DAK API'] = 'dak-api.html'
            config_updated = True
            print("Added DAK API to menu Indices section")
            qa_reporter.add_success("Added DAK API to menu Indices section")
        else:
            qa_reporter.add_success("DAK API already exists in menu Indices section")
        
        # Write back the updated config if changes were made
        if config_updated:
            with open(sushi_config_path, 'w') as f:
                yaml.dump(config, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
            print("sushi-config.yaml updated successfully")
            qa_reporter.add_success("sushi-config.yaml updated successfully")
            qa_reporter.add_file_processed(sushi_config_path, "updated")
            return True
        else:
            print("sushi-config.yaml already contains required DAK API entries")
            qa_reporter.add_success("sushi-config.yaml already contains required DAK API entries")
            qa_reporter.add_file_processed(sushi_config_path, "no_changes_needed")
            return False
            
    except Exception as e:
        print(f"Error updating sushi-config.yaml: {e}")
        qa_reporter.add_error(f"Error updating sushi-config.yaml: {e}")
        return False

if __name__ == "__main__":
    # Initialize QA reporter for preprocessing
    qa_reporter = QAReporter("preprocessing")
    qa_reporter.add_success("Starting update_sushi_config.py preprocessing")
    
    try:
        success = update_sushi_config(qa_reporter)
        if success:
            qa_reporter.add_success("update_sushi_config completed successfully")
        else:
            qa_reporter.add_warning("update_sushi_config completed but no changes were made")
        
        # Finalize the QA report
        qa_report = qa_reporter.finalize_report("completed")
        
        # Save the preprocessing QA report to a location that won't be overwritten by IG publisher
        # Using a different filename and location to avoid conflicts
        preprocessing_qa_path = "input/temp/qa_preprocessing.json"
        if qa_reporter.save_to_file(preprocessing_qa_path):
            print(f"QA report saved to {preprocessing_qa_path}")
        else:
            print("Failed to save QA report")
            
        # Also save to the /tmp location for backward compatibility
        temp_qa_path = "/tmp/qa_preprocessing.json"
        qa_reporter.save_to_file(temp_qa_path)
        
        # Return exit code based on whether there were any errors
        # Note: We don't fail on warnings, only on errors
        exit_code = 0 if len(qa_report["details"]["errors"]) == 0 else 1
        sys.exit(exit_code)
        
    except Exception as e:
        qa_reporter.add_error(f"Unexpected error in main: {e}")
        qa_report = qa_reporter.finalize_report("failed")
        
        # Try to save the error report to both locations
        preprocessing_qa_path = "input/temp/qa_preprocessing.json"
        qa_reporter.save_to_file(preprocessing_qa_path)
        temp_qa_path = "/tmp/qa_preprocessing.json"
        qa_reporter.save_to_file(temp_qa_path)
        
        print(f"Fatal error: {e}")
        sys.exit(1)