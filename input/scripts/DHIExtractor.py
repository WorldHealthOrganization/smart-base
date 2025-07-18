"""
DHI (Digital Health Interventions) Extractor Module
This module extracts classifications and interventions from text files to generate
FHIR CodeSystems, ValueSets, and ConceptMaps for digital health interventions.
The script processes two primary data files:
1. system_categories.txt - Contains system categories (A-Z format)
2. dhi_v1.txt - Contains hierarchical digital health interventions (numerical codes)
The extracted data is used to generate:
- FHIR CodeSystems for both classifications and interventions
- FHIR ValueSets for both data sets
- FHIR ConceptMaps to represent hierarchical relationships
Usage:
    The extractor is typically instantiated and run as part of a larger
    data processing pipeline that generates FHIR resources from DAK artifacts.
Example:
    extractor = DHIExtractor(installer_instance)
    extractor.extract()
"""
from typing import List, Dict, Any
import installer
from extractor import extractor
class DHIExtractor(extractor):
    """
    Digital Health Interventions extractor for processing classification and intervention data.
    This class extends the base extractor to handle DHI-specific data processing,
    generating FHIR CodeSystems, ValueSets, and ConceptMaps from text-based
    classification files.
    Attributes:
        Standard attributes inherited from the extractor base class.
    """
    def find_files(self) -> List[str]:
        """
        Identify the input files to be processed by this extractor.
        Returns:
            List[str]: List of file paths containing DHI classification data.
                      Includes system categories and interventions files.
        """
        return ['input/data/system_categories.txt', 'input/data/dhi_v1.txt']
    def extract_to_resources(self, inputfile_name: str, resources: Dict[str, Any]) -> None:
        """
        Route file processing based on input filename.
        Determines which extraction method to use based on the input file name
        and delegates to the appropriate processing function.
        Args:
            inputfile_name (str): Path to the input file being processed
            resources (Dict[str, Any]): Dictionary to store generated FHIR resources
                                      organized by resource type (codesystems, valuesets, etc.)
        """
        if inputfile_name == 'input/data/system_categories.txt':
            self.extract_classifications(inputfile_name, resources)
        if inputfile_name == 'input/data/dhi_v1.txt':
            self.extract_interventions(inputfile_name, resources)
    def extract_classifications(self, filename: str, resources: Dict[str, Any]) -> None:
        """
        Extract system classifications from the system categories file.
        Processes system_categories.txt which contains system categories in format:
        "A. Category Name" where A-Z are the classification codes.
        Args:
            filename (str): Path to the system categories input file
            resources (Dict[str, Any]): Dictionary to store generated FHIR resources
        """
        # CodeSystem and ValueSet identifiers for Digital Health System Categories
        cdhsc_id = 'CDSCv1'
        print("System Categories")
        categories: Dict[str, str] = {}
        for line in open(filename, 'r'):
            parts = line.strip().split(' ', 1)
            if len(parts) < 2:
                continue
            # Extract code (letter) and remove trailing period if present
            code = parts[0].strip().rstrip(".")
            category = parts[1].strip()
            print("\t" + category + ' = ' + code)
            categories[code] = category
        # Generate CodeSystem and ValueSet from the extracted categories
        self.installer.generate_cs_and_vs_from_dict(
            cdhsc_id, 
            'Classification of Digital Health System Categories v1', 
            categories, 
            resources
        )
    def extract_interventions(self, filename: str, resources: Dict[str, Any]) -> None:
        """
        Extract digital health interventions from the interventions file.
        Processes dhi_v1.txt which contains hierarchical interventions in format:
        "1.1.2 Intervention Name" where numerical codes represent hierarchy.
        Also generates a ConceptMap to represent the hierarchical relationships
        between intervention codes.
        Args:
            filename (str): Path to the interventions input file  
            resources (Dict[str, Any]): Dictionary to store generated FHIR resources
        """
        # Resource identifiers
        cdhi_id = 'CDHIv1'  # CodeSystem for Digital Health Interventions
        cm_id = "CDHIv1Hierarchy"  # ConceptMap for hierarchy
        print("Interventions")
        interventions: Dict[str, str] = {}
        parent_map: Dict[str, str] = {}  # Maps child code to parent code
        for line in open(filename, 'r'):
            parts = line.strip().split(' ', 1)
            if len(parts) < 2:
                continue
            # Parse hierarchical code structure (e.g., "1.1.2" -> ["1", "1", "2"])
            codes = parts[0].strip().split('.')
            code = ".".join(codes)
            parent_code = ".".join(codes[:-1])  # Parent is all but last element
            intervention = parts[1].strip()
            print("\t" + intervention + ' = ' + code)
            interventions[code] = intervention
            # Map child to parent for hierarchy (only if parent exists)
            if parent_code:
                parent_map[code] = parent_code
        # Generate CodeSystem and ValueSet from the extracted interventions        
        self.installer.generate_cs_and_vs_from_dict(
            cdhi_id, 
            'Classification of Digital Health Interventions v1', 
            interventions, 
            resources
        )
        # Generate ConceptMap for hierarchical relationships if any exist
        if len(parent_map) > 0: 
            title = "Hierarchy of the Classification of Digital Health Interventions v1"
            cm = "Instance:  " + self.escape(cm_id) + '\n'
            cm += "InstanceOf:   ConceptMap\n"
            cm += "Description:  \"Mapping to represent hierarchy within " + title + ".\"\n"
            cm += "Usage:        #definition\n"
            cm += "* name = \"" + self.escape(cm_id) + "\"\n"
            cm += "* title = \"" + self.escape(title) + "\"\n"
            cm += "* status = #active\n"
            cm += "* experimental = false\n"
            cm += "* sourceCanonical = Canonical(" + cdhi_id + ")\n"
            cm += "* targetCanonical = Canonical(" + cdhi_id + ")\n"
            cm += "* group[+]\n"
            cm += "  * source = Canonical(" + cdhi_id + ")\n"
            cm += "  * target = Canonical(" + cdhi_id + ")\n"
            # Add mapping entries for each parent-child relationship
            for code, parent_code in parent_map.items():
                cm += "  * insert ElementMap( " + code + ", " + parent_code + ", narrower)\n"
            resources['conceptmaps'][cm_id] = cm
