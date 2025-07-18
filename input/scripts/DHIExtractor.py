"""
DHIExtractor.py

Extracts classifications and interventions from text files, generating code systems,
value sets, and concept maps for digital health interventions.

Usage:
    - find_files() returns the set of input files needed for extraction.
    - extract_to_resources(inputfile_name, resources) processes the file and populates resources.
    - extract_categories and extract_interventions parse and process data files.

Key Variables:
    - cdhi_id, cdhsc_id, cm_id: Identifiers for code systems and concept maps.
    - interventions: dict mapping codes to interventions.
    - parent_map: dict mapping child codes to parent codes for hierarchy.
    - resources: dict structure for storing extracted artifacts.
"""

import os
from typing import List, Dict, Any

import installer

def find_files() -> List[str]:
    """
    Returns a list of input files required for extraction.

    Returns:
        List[str]: List of file paths.
    """
    return ['input/data/system_categories.txt', 'input/data/dhi_v1.txt']

def extract_to_resources(inputfile_name: str, resources: Dict[str, Any]) -> None:
    """
    Processes the given input file and extracts its contents into the provided resources dict.

    Args:
        inputfile_name (str): Path to the input file.
        resources (dict): Dictionary to store extracted code systems, value sets, and concept maps.
    """
    if inputfile_name == 'input/data/system_categories.txt':
        extract_categories(inputfile_name, resources)
    if inputfile_name == 'input/data/dhi_v1.txt':
        extract_interventions(inputfile_name, resources)

def extract_categories(filename: str, resources: Dict[str, Any]) -> None:
    """
    Parses system categories from a file and adds them as code systems and value sets.

    Args:
        filename (str): Path to the system categories file.
        resources (dict): Dictionary to store extracted artifacts.
    """
    cdhsc_id = 'CDSCv1'
    print("System Categories")
    interventions: Dict[str, str] = {}
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split(' ', 1)
            if len(parts) < 2:
                continue
            code = parts[0].strip().rstrip('.')
            intervention = parts[1].strip()
            print(f"\t{intervention} = {code}")
            interventions[code] = intervention
    installer.generate_cs_and_vs_from_dict(
        cdhsc_id,
        'Classification of Digital Health System Categories v1',
        interventions,
        resources
    )

def extract_interventions(filename: str, resources: Dict[str, Any]) -> None:
    """
    Parses interventions from a file, builds a hierarchy map, and adds them as code systems,
    value sets, and concept maps representing hierarchy.

    Args:
        filename (str): Path to the interventions file.
        resources (dict): Dictionary to store extracted artifacts.
    """
    cdhi_id = 'CDHIv1'
    cm_id = "CDHIv1Hierarchy"
    print("Interventions")
    interventions: Dict[str, str] = {}
    parent_map: Dict[str, str] = {}

    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split(' ', 1)
            if len(parts) < 2:
                continue
            codes = parts[0].strip().split('.')
            code = ".".join(codes)
            parent_code = ".".join(codes[:-1])
            intervention = parts[1].strip()
            print(f"\t{intervention} = {code}")
            interventions[code] = intervention
            if parent_code:
                parent_map[code] = parent_code

    installer.generate_cs_and_vs_from_dict(
        cdhi_id,
        'Classification of Digital Health Interventions v1',
        interventions,
        resources
    )

    if parent_map:
        title = "Hierarchy of the Classification of Digital Health Interventions v1"
        cm = f"Instance: {cm_id}\n"
        cm += "InstanceOf: ConceptMap\n"
        cm += f'Description: "Mapping to represent hierarchy within {title}."\n'
        cm += "Usage: #definition\n"
        cm += f'* name = "{cm_id}"\n'
        cm += f'* title = "{title}"\n'
        cm += "* status = #active\n"
        cm += "* experimental = false\n"
        cm += f"* sourceCanonical = Canonical({cdhi_id})\n"
        cm += f"* targetCanonical = Canonical({cdhi_id})\n"
        cm += "* group[+]\n"
        cm += f"  * source = Canonical({cdhi_id})\n"
        cm += f"  * target = Canonical({cdhi_id})\n"
        for code, parent_code in parent_map.items():
            cm += f"  * insert ElementMap({code}, {parent_code}, narrower)\n"
        resources.setdefault('conceptmaps', {})[cm_id] = cm