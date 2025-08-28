#!/usr/bin/env python3
"""
ISCO-08 Extractor for SMART Guidelines

This module extracts ISCO-08 (International Standard Classification of Occupations 2008)
codes from Excel source files and generates FHIR CodeSystem definitions.

The extractor processes the official ILO ISCO-08 Excel file with columns:
- "ISCO 08 Code": The official ISCO-08 code
- "Title EN": English title/display name 
- "Definition": Official definition of the occupation

Source: https://webapps.ilo.org/ilostat-files/ISCO/newdocs-08-2021/ISCO-08/ISCO-08%20EN%20Structure%20and%20definitions.xlsx

Author: SMART Guidelines Team
"""

import pandas as pd
import os
import sys
from typing import Dict, List, Tuple


class ISCO08Extractor:
    """
    Extractor for ISCO-08 classification codes.
    
    This extractor processes ISCO-08 Excel source files and generates FHIR CodeSystem
    definitions for use in SMART Guidelines implementations.
    """

    def __init__(self):
        self.codes = {}
        self.output_path = "input/fsh/codesystems"
        
    def extract_from_excel(self, excel_file_path: str, sheet_name: str = 'ISCO-08') -> bool:
        """
        Extract ISCO-08 codes from Excel file.
        
        Args:
            excel_file_path: Path to the ISCO-08 Excel source file
            sheet_name: Name of the Excel sheet containing the data
            
        Returns:
            bool: True if extraction successful, False otherwise
        """
        try:
            # Read Excel file
            df = pd.read_excel(excel_file_path, sheet_name=sheet_name)
            
            # Validate required columns
            required_columns = ['ISCO 08 Code', 'Title EN', 'Definition']
            missing_columns = [col for col in required_columns if col not in df.columns]
            if missing_columns:
                print(f"Error: Missing required columns: {missing_columns}")
                print(f"Available columns: {list(df.columns)}")
                return False
            
            # Process each row
            for _, row in df.iterrows():
                code = str(row['ISCO 08 Code']).strip()
                title = str(row['Title EN']).strip()
                definition = str(row['Definition']).strip()
                
                # Skip empty rows
                if not code or code == 'nan':
                    continue
                    
                self.codes[code] = {
                    'display': title,
                    'definition': definition if definition != 'nan' else title
                }
                
            return True
            
        except FileNotFoundError:
            print(f"Error: Excel file {excel_file_path} not found")
            return False
        except Exception as e:
            print(f"Error processing Excel file {excel_file_path}: {e}")
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
        
        # Sort codes by length first (to maintain hierarchy), then by numeric value
        sorted_codes = sorted(self.codes.items(), key=lambda x: (len(x[0]), int(x[0]) if x[0].isdigit() else float('inf'), x[0]))
        
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

    def extract_and_generate(self, excel_file_path: str, output_file: str = None, sheet_name: str = 'ISCO-08') -> bool:
        """
        Main method to extract ISCO-08 codes and generate FHIR CodeSystem.
        
        Args:
            excel_file_path: Path to the ISCO-08 Excel source file
            output_file: Optional output file path
            sheet_name: Name of the Excel sheet containing the data
            
        Returns:
            bool: True if successful, False otherwise
        """
        print(f"Extracting ISCO-08 codes from {excel_file_path}")
        
        if not os.path.exists(excel_file_path):
            print(f"Error: Source file {excel_file_path} does not exist")
            return False
            
        if not self.extract_from_excel(excel_file_path, sheet_name):
            print("Failed to extract codes from Excel file")
            return False
            
        print(f"Extracted {len(self.codes)} ISCO-08 codes")
        
        if not self.save_codesystem(output_file):
            print("Failed to save CodeSystem")
            return False
            
        return True


def main():
    """Main entry point for the ISCO-08 extractor script."""
    if len(sys.argv) < 2:
        print("Usage: python isco08_extractor.py <excel_file_path> [output_file] [sheet_name]")
        print("Example: python isco08_extractor.py input/data/ISCO-08_EN_Structure_and_definitions.xlsx")
        sys.exit(1)
    
    excel_file_path = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    sheet_name = sys.argv[3] if len(sys.argv) > 3 else 'ISCO-08'
    
    extractor = ISCO08Extractor()
    
    if extractor.extract_and_generate(excel_file_path, output_file, sheet_name):
        print("ISCO-08 extraction completed successfully")
        sys.exit(0)
    else:
        print("ISCO-08 extraction failed")
        sys.exit(1)


if __name__ == "__main__":
    main()