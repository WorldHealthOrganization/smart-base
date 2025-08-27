#!/usr/bin/env python3
"""
ISCO-08 Extractor for SMART Guidelines

This module extracts ISCO-08 (International Standard Classification of Occupations 2008)
codes from XML source files and generates FHIR CodeSystem definitions.

The extractor processes the official ILO ISCO-08 classification structure and converts
it into a FHIR-compatible CodeSystem for use in clinical decision support implementations.

Author: SMART Guidelines Team
"""

import xml.etree.ElementTree as ET
import os
import sys
from typing import Dict, List, Tuple


class ISCO08Extractor:
    """
    Extractor for ISCO-08 classification codes.
    
    This extractor processes ISCO-08 XML source files and generates FHIR CodeSystem
    definitions for use in SMART Guidelines implementations.
    """

    def __init__(self):
        self.codes = {}
        self.output_path = "input/fsh/codesystems"
        
    def extract_from_xml(self, xml_file_path: str) -> bool:
        """
        Extract ISCO-08 codes from XML file.
        
        Args:
            xml_file_path: Path to the ISCO-08 XML source file
            
        Returns:
            bool: True if extraction successful, False otherwise
        """
        try:
            tree = ET.parse(xml_file_path)
            root = tree.getroot()
            
            # Extract major groups (1-digit codes)
            for major_group in root.findall('major_group'):
                code = major_group.get('code')
                title = major_group.get('title')
                definition_elem = major_group.find('definition')
                definition = definition_elem.text if definition_elem is not None else title
                
                self.codes[code] = {
                    'display': title,
                    'definition': definition
                }
                
                # Extract sub-major groups (2-digit codes)
                for sub_major in major_group.findall('sub_major_group'):
                    sub_code = sub_major.get('code')
                    sub_title = sub_major.get('title')
                    sub_definition_elem = sub_major.find('definition')
                    sub_definition = sub_definition_elem.text if sub_definition_elem is not None else sub_title
                    
                    self.codes[sub_code] = {
                        'display': sub_title,
                        'definition': sub_definition
                    }
                    
                    # Extract minor groups (3-digit codes)
                    for minor in sub_major.findall('minor_group'):
                        minor_code = minor.get('code')
                        minor_title = minor.get('title')
                        minor_definition_elem = minor.find('definition')
                        minor_definition = minor_definition_elem.text if minor_definition_elem is not None else minor_title
                        
                        self.codes[minor_code] = {
                            'display': minor_title,
                            'definition': minor_definition
                        }
                        
                        # Extract unit groups (4-digit codes)
                        for unit in minor.findall('unit_group'):
                            unit_code = unit.get('code')
                            unit_title = unit.get('title')
                            unit_definition_elem = unit.find('definition')
                            unit_definition = unit_definition_elem.text if unit_definition_elem is not None else unit_title
                            
                            self.codes[unit_code] = {
                                'display': unit_title,
                                'definition': unit_definition
                            }
                            
            return True
            
        except ET.ParseError as e:
            print(f"Error parsing XML file {xml_file_path}: {e}")
            return False
        except Exception as e:
            print(f"Error processing XML file {xml_file_path}: {e}")
            return False

    def escape_string(self, text: str) -> str:
        """
        Escape special characters for FHIR FSH format.
        
        Args:
            text: Text to escape
            
        Returns:
            str: Escaped text
        """
        if not text:
            return ""
        return text.replace('"', '\\"').replace('\\', '\\\\')

    def generate_codesystem_fsh(self) -> str:
        """
        Generate FHIR CodeSystem in FSH format.
        
        Returns:
            str: FSH content for the CodeSystem
        """
        fsh_content = []
        
        # CodeSystem header
        fsh_content.append("CodeSystem: ISCO08")
        fsh_content.append("Id: ISCO08")
        fsh_content.append("Title: \"International Standard Classification of Occupations 2008\"")
        fsh_content.append("Description: \"ISCO-08 codes from the International Labour Organization official classification\"")
        fsh_content.append("* ^url = \"http://www.ilo.org/public/english/bureau/stat/isco/isco08/\"")
        fsh_content.append("* ^status = #active")
        fsh_content.append("* ^experimental = false")
        fsh_content.append("* ^caseSensitive = true")
        fsh_content.append("* ^content = #complete")
        fsh_content.append("* ^copyright = \"© International Labour Organization 2008\"")
        fsh_content.append("")
        
        # Add properties
        fsh_content.append("* ^property[+].code = #definition")
        fsh_content.append("* ^property[=].type = #string")
        fsh_content.append("* ^property[=].description = \"Definition of the ISCO-08 code\"")
        fsh_content.append("")
        
        # Sort codes by numeric value for logical ordering
        sorted_codes = sorted(self.codes.items(), key=lambda x: int(x[0]))
        
        # Add concepts
        for code, data in sorted_codes:
            escaped_display = self.escape_string(data['display'])
            escaped_definition = self.escape_string(data['definition'])
            
            fsh_content.append(f"* #{code} \"{escaped_display}\"")
            if data['definition'] != data['display']:
                fsh_content.append(f"  * ^property[=].code = #definition")
                fsh_content.append(f"  * ^property[=].valueString = \"{escaped_definition}\"")
        
        return "\n".join(fsh_content)

    def save_codesystem(self, output_file: str = None) -> bool:
        """
        Save the generated CodeSystem to a file.
        
        Args:
            output_file: Optional output file path. If not provided, uses default path.
            
        Returns:
            bool: True if save successful, False otherwise
        """
        if not output_file:
            os.makedirs(self.output_path, exist_ok=True)
            output_file = os.path.join(self.output_path, "ISCO08.fsh")
        
        try:
            fsh_content = self.generate_codesystem_fsh()
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(fsh_content)
            print(f"ISCO-08 CodeSystem saved to {output_file}")
            return True
        except Exception as e:
            print(f"Error saving CodeSystem to {output_file}: {e}")
            return False

    def extract_and_generate(self, xml_file_path: str, output_file: str = None) -> bool:
        """
        Main method to extract ISCO-08 codes and generate FHIR CodeSystem.
        
        Args:
            xml_file_path: Path to the ISCO-08 XML source file
            output_file: Optional output file path
            
        Returns:
            bool: True if successful, False otherwise
        """
        print(f"Extracting ISCO-08 codes from {xml_file_path}")
        
        if not os.path.exists(xml_file_path):
            print(f"Error: Source file {xml_file_path} does not exist")
            return False
            
        if not self.extract_from_xml(xml_file_path):
            print("Failed to extract codes from XML file")
            return False
            
        print(f"Extracted {len(self.codes)} ISCO-08 codes")
        
        if not self.save_codesystem(output_file):
            print("Failed to save CodeSystem")
            return False
            
        return True


def main():
    """Main entry point for the ISCO-08 extractor script."""
    if len(sys.argv) < 2:
        print("Usage: python isco08_extractor.py <xml_file_path> [output_file]")
        print("Example: python isco08_extractor.py input/data/isco08.xml")
        sys.exit(1)
    
    xml_file_path = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    extractor = ISCO08Extractor()
    
    if extractor.extract_and_generate(xml_file_path, output_file):
        print("ISCO-08 extraction completed successfully")
        sys.exit(0)
    else:
        print("ISCO-08 extraction failed")
        sys.exit(1)


if __name__ == "__main__":
    main()