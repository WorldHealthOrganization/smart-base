"""
FHIR CodeSystem Management

This module provides comprehensive management functionality for FHIR CodeSystems
and ValueSets within the SMART guidelines system. It handles the creation,
validation, and organization of clinical terminologies and code classifications
used throughout the implementation.

The codesystem_manager maintains centralized control over:
- CodeSystem creation and population
- ValueSet generation from CodeSystems
- Code validation and hierarchy management
- Resource naming and identifier assignment

Author: SMART Guidelines Team
"""
import re
import pprint
import sys
import stringer
import logging
from typing import Dict, List, Optional, Union, Any
from typing_extensions import TypedDict


class DesignationDict(TypedDict, total=False):
    """Type definition for code designation structure."""
    value: str
    language: Optional[str]
    use: Optional[str]


class PropertyStringDict(TypedDict):
    """Type definition for string property structure."""
    code: str
    value: str


class PropertyCodeDict(TypedDict):
    """Type definition for code property structure."""
    code: str
    value: str


class PropertyCodingDict(TypedDict):
    """Type definition for coding property structure."""
    code: str
    value: Dict[str, str]


class CodeDefinitionDict(TypedDict, total=False):
    """Type definition for complete code definition structure."""
    display: str
    definition: Optional[str]
    designation: List[DesignationDict]
    propertyString: List[PropertyStringDict]
    propertyCode: List[PropertyCodeDict]
    propertyCoding: List[PropertyCodingDict]


class CodeSystemPropertyDict(TypedDict, total=False):
    """Type definition for CodeSystem property metadata."""
    description: str
    type: str

class codesystem_manager(object):
    """
    Central manager for FHIR CodeSystem and ValueSet resources.
    
    This class provides comprehensive functionality for creating, managing,
    and validating FHIR CodeSystems and their associated ValueSets. It
    ensures consistent resource generation and proper code organization
    across the SMART guidelines implementation.
    
    Attributes:
        codesystems (Dict[str, Dict[str, Union[str, CodeDefinitionDict]]]): Collection of managed CodeSystem resources
        codesystem_titles (Dict[str, str]): Mapping of CodeSystem IDs to display titles
        codesystem_properties (Dict[str, Dict[str, CodeSystemPropertyDict]]): Properties and metadata for CodeSystems
    """
    codesystems: Dict[str, Dict[str, Union[str, CodeDefinitionDict]]] = {}
    codesystem_titles: Dict[str, str] = {}
    codesystem_properties: Dict[str, Dict[str, CodeSystemPropertyDict]] = {}

    publisher: str 
    version: str
    
    def __init__(self, publisher: str = "Self Published", version: str = "0.1.0") -> None:
        """
        Initialize the CodeSystem manager.
        
        Args:
            publisher: Name of the publisher for generated CodeSystems
            version: Version string for generated CodeSystems
        """
        self.publisher = publisher
        self.version = version


    def register(self, codesystem_id: str, title: str) -> bool:
        """
        Register a new CodeSystem for management.
        
        Args:
            codesystem_id: Unique identifier for the CodeSystem
            title: Human-readable title for the CodeSystem
            
        Returns:
            True if registration successful
        """
        if self.has_codesystem(codesystem_id):
            logging.getLogger(self.__class__.__name__).info("WARNING: reinitializing codesystem " + codesystem_id)
        self.codesystems[codesystem_id] = {}
        self.codesystem_titles[codesystem_id] = title
        self.codesystem_properties[codesystem_id] = {}
            # need to replace this type of logic with exception handling probably
        return True
    
    def has_codesystem(self, id: str) -> bool:
        """
        Check if a CodeSystem is registered.
        
        Args:
            id: CodeSystem identifier to check
            
        Returns:
            True if CodeSystem exists
        """
        return id in self.codesystems and id in self.codesystem_titles

    def get_title(self, id: str) -> Optional[str]:
        """
        Get the title of a registered CodeSystem.
        
        Args:
            id: CodeSystem identifier
            
        Returns:
            CodeSystem title if found, None otherwise
        """
        if not self.has_codesystem(id):
            return None
        return self.codesystem_titles[id]
    
    
    def get_properties(self, id: str) -> Dict[str, CodeSystemPropertyDict]:
        """
        Get properties of a registered CodeSystem.
        
        Args:
            id: CodeSystem identifier
            
        Returns:
            Dictionary of CodeSystem properties
        """
        if not self.has_codesystem(id):
            return {}
        return self.codesystem_properties[id]


    def get_codes(self, id: str) -> Dict[str, Union[str, CodeDefinitionDict]]:
        """
        Get all codes in a registered CodeSystem.
        
        Args:
            id: CodeSystem identifier
            
        Returns:
            Dictionary of codes and their definitions
        """
        if not self.has_codesystem(id):
            return {}
        return self.codesystems[id]
    
    def get_code(self, codesystem_id: str, code: str) -> Optional[Union[str, CodeDefinitionDict]]:
        """
        Get a specific code definition from a CodeSystem.
        
        Args:
            codesystem_id: CodeSystem identifier
            code: Code to retrieve
            
        Returns:
            Code definition if found, None otherwise
        """
        if not self.has_code(codesystem_id, code):
            return None
        else:
            return self.codesystems[codesystem_id][code]

        
    def merge_code(self, codesystem_id: str, code: str, display: str, definition: Optional[str] = None, designation: List[DesignationDict] = [], propertyString: List[PropertyStringDict] = []) -> bool:
        """
        Merge a code with display and optional properties into a CodeSystem.
        
        Args:
            codesystem_id: Target CodeSystem identifier
            code: Code to add or merge
            display: Display name for the code
            definition: Optional definition text
            designation: List of designations for the code
            propertyString: List of string properties for the code
            
        Returns:
            True if merge successful, False otherwise
        """
        code_defn: CodeDefinitionDict = {'display': display,
                    'definition': definition,
                    'designation': designation,
                    'propertyString': propertyString}
        return self.merge_code_dict(codesystem_id, code, code_defn)
        
    def merge_code_dict(self, codesystem_id: str, code: str, new_code: CodeDefinitionDict) -> bool:
        """
        Merge a complete code definition dictionary into a CodeSystem.
        
        Args:
            codesystem_id: Target CodeSystem identifier
            code: Code to add or merge
            new_code: Complete code definition structure
            
        Returns:
            True if merge successful, False otherwise
        """
        if not self.has_codesystem(codesystem_id):
            logging.getLogger(self.__class__.__name__).info("tyring to create code on non-registered code-system:" + codesystem_id)
            return False
        if not 'display' in new_code:
            logging.getLogger(self.__class__.__name__).info("trying to create code with out display:" + code)
            return False
        if not 'definition' in new_code:
            new_code['definition'] = None
        if not 'designation' in new_code:
            new_code['designation'] = []
        if not 'propertyString' in new_code:
            new_code['propertyString'] = []
        if not 'propertyCode' in new_code:
            new_code['propertyCode'] = []
        if not 'propertyCoding' in new_code:
            new_code['propertyCoding'] = []

        existing_code = self.get_code(codesystem_id, code)
        if existing_code:
            logging.getLogger(self.__class__.__name__).info("Trying to create a code '" + code + "'when it already exists in " + codesystem_id)
            if isinstance(existing_code, dict) and 'display' in existing_code:
                if not existing_code['display'] == new_code['display']:
                    logging.getLogger(self.__class__.__name__).info("Mismatched display of code '" + code + "': '" + existing_code['display'] \
                            + "' !=  '" + new_code['display'] + "'")
                if not self.is_blank(existing_code.get('definition')) and not self.is_blank(new_code.get('definition')) \
                   and not existing_code['definition'] == new_code['definition']:
                    logging.getLogger(self.__class__.__name__).info("Mismatched definitions of code '" + code + "': '" + str(existing_code['definition']) \
                            + "' !=  '" + str(new_code['definition']) + "'")
                new_code['designation'] += existing_code.get('designation', [])
                new_code['propertyString'] += existing_code.get('propertyString', [])
                new_code['propertyCode'] += existing_code.get('propertyCode', [])
        self.codesystems[codesystem_id][code] = new_code
        return True

    def add_properties(self, codesystem_id: str, vals: Dict[str, CodeSystemPropertyDict]) -> None:
        """
        Add multiple properties to a CodeSystem.
        
        Args:
            codesystem_id: Target CodeSystem identifier
            vals: Dictionary of property definitions to add
        """
        for k, v in vals.items():
            self.add_property(codesystem_id, k, v)
      
    def add_property(self, codesystem_id: str, k: str, v: CodeSystemPropertyDict) -> None:
        """
        Add a single property to a CodeSystem.
        
        Args:
            codesystem_id: Target CodeSystem identifier
            k: Property key/name
            v: Property definition structure
        """
        self.codesystem_properties[codesystem_id][k] = v

    def add_dict(self, codesystem_id: str, inputs: Dict[str, Union[str, CodeDefinitionDict]]) -> bool:
        """
        Add multiple codes from a dictionary to a CodeSystem.
        
        Args:
            codesystem_id: Target CodeSystem identifier
            inputs: Dictionary of codes and their definitions
            
        Returns:
            True if all codes added successfully
        """
        result = True
        for code, expr in inputs.items():
            if isinstance(expr, str):
                # Convert string to proper CodeDefinitionDict
                code_def: CodeDefinitionDict = {
                    'display': expr,
                    'definition': None,
                    'designation': [],
                    'propertyString': [],
                    'propertyCode': [],
                    'propertyCoding': []
                }
                result &= self.merge_code_dict(codesystem_id, code, code_def)
            else:
                result &= self.merge_code_dict(codesystem_id, code, expr)
        return result

    def has_code(self, codesystem_id: str, code: str) -> bool:
        """
        Check if a specific code exists in a CodeSystem.
        
        Args:
            codesystem_id: CodeSystem identifier to check
            code: Code to look for
            
        Returns:
            True if code exists in the CodeSystem
        """
        return codesystem_id in self.codesystems and code in self.codesystems[codesystem_id]


    def escape(self, input: str) -> str:
        """
        Escape string for safe use in generated content.
        
        Args:
            input: String to escape
            
        Returns:
            Escaped string
        """
        return stringer.escape(input)
        
    def escape_code(self, input: str) -> Optional[str]:
        """
        Escape and validate code for safe use as identifier.
        
        Args:
            input: Code string to escape
            
        Returns:
            Escaped code string, or None if invalid input
        """
        original = input
        if not isinstance(input, str):
            return None
        input = input.strip()
        input = re.sub(r"['\"]", "", input)
        #SUSHI BUG on processing codes with double quote.  sushi fails
        #Example \"Bivalent oral polio vaccine (bOPV)–inactivated polio vaccine (IPV)\" schedule (in countries with high vaccination coverage [e.g. 90–95%] and low importation risk [where neighbouring countries and/or countries that share substantial population movement have a similarly high coverage])" 
        
        input = re.sub(r"\s+", " ", input)
        if len(input) > 245:
            # max filename size is 255, leave space for extensions such as .fsh
            logging.getLogger(self.__class__.__name__).info("ERROR: name of id is too long.hashing: " + input)        
            input = stringer.to_hash(input, 245)
            logging.getLogger(self.__class__.__name__).info("Escaping code " + original + " to " + input)
        return input

    def is_blank(self, value: Any) -> bool:
        """
        Check if a value is blank or None.
        
        Args:
            value: Value to check
            
        Returns:
            True if value is considered blank
        """
        return stringer.is_blank(value)

    def render_valueset_allcodes(self, vs_id: str, title: str, cs_id: str) -> str:
        """
        Render a ValueSet that includes all codes from a CodeSystem.
        
        Args:
            vs_id: ValueSet identifier
            title: ValueSet title
            cs_id: Source CodeSystem identifier
            
        Returns:
            Generated FSH ValueSet content
        """
        valueset = 'ValueSet: ' + stringer.escape(vs_id) + '\n'
        valueset += 'Title: "' + stringer.escape(title) + '"\n'
        valueset += 'Description:  "Value Set for ' + stringer.escape(title) + '. Autogenerated from DAK artifacts"\n'
        #valueset += 'Usage: #definition\n'
        #valueset += "* publisher = \"" + stringer.escape(self.publisher) + "\"\n" 
        #valueset += "* experimental = false\n"
        #valueset += "* version = \"" + self.version + "\"\n"
        valueset += '* ^status = #active\n'
        valueset += '* include codes from system ' + stringer.escape(cs_id) + '\n'
        return valueset

    def render_vs_from_list(self, id: str, codesystem_id: str, title: str, codes: List[str]) -> str:
        """
        Render a ValueSet from a specific list of codes.
        
        Args:
            id: ValueSet identifier
            codesystem_id: Source CodeSystem identifier
            title: ValueSet title
            codes: List of codes to include
            
        Returns:
            Generated FSH ValueSet content
        """
        valueset = 'ValueSet: ' + stringer.escape(id) + '\n'
        valueset += 'Title: "' + stringer.escape(title) + '"\n'
        valueset += 'Description:  "Value Set for ' + stringer.escape(title) + '. Autogenerated from DAK artifacts"\n'
        #valueset += "Usage: #definition\n"
        #valueset += "* publisher = \"" + stringer.escape(self.publisher) + "\"\n" 
        #valueset += "* experimental = false\n"
        #valueset += "* version = \"" + self.version + "\"\n"
        valueset += '* ^status = #active\n'
        for code in codes:
            valueset += '* include ' + stringer.escape(codesystem_id) + '#"' + stringer.escape_code(code) + '"\n'            
        return valueset

    def render_vs_from_dict(self, id: str, title: str, codelist: Dict[str, Union[str, CodeDefinitionDict]], properties: Dict[str, CodeSystemPropertyDict] = {}) -> Union[str, bool]:
        """
        Render a ValueSet from a dictionary of codes and register the CodeSystem.
        
        Args:
            id: CodeSystem and ValueSet identifier
            title: Display title for the resources
            codelist: Dictionary of codes and their definitions
            properties: Optional properties for the CodeSystem
            
        Returns:
            Generated FSH ValueSet content, or False if failed
        """
        logging.getLogger(self.__class__.__name__).info("trying to register codesystem " + id)
        if not self.register(id, title):
            logging.getLogger(self.__class__.__name__).info("Skipping CS and VS for " + id + " could not register")
            return False
        if not self.add_dict(id, codelist):
            logging.getLogger(self.__class__.__name__).info("Skipping CS and VS for " + id + " could not add dictionary")
            return False
        self.add_properties(id, properties)
        return self.render_valueset_allcodes(id, title, id)
    
    def render_codesystems(self) -> Dict[str, Union[str, bool]]:
        """
        Render all registered CodeSystems.
        
        Returns:
            Dictionary mapping CodeSystem IDs to their FSH content
        """
        result: Dict[str, Union[str, bool]] = {}
        for id in self.codesystems.keys():
            result[id] = self.render_codesystem(id)
        return result
    
    def render_codesystem(self, id: str) -> Union[str, bool]:
        """
        Render a single CodeSystem to FSH format.
        
        Args:
            id: CodeSystem identifier to render
            
        Returns:
            Generated FSH CodeSystem content, or False if failed
        """
        if not self.has_codesystem(id):
            logging.getLogger(self.__class__.__name__).info("Trying to render absent codesystem " + id)
            return False
        title = self.get_title(id)
        codesystem = 'CodeSystem: ' + stringer.escape(id) + '\n'
        codesystem += 'Title: "' + stringer.escape(title) + '"\n'
        codesystem += 'Description:  "CodeSystem for ' + stringer.escape(title) + '. Autogenerated from DAK artifacts"\n'
        #codesystem += "* version = \"" + self.version + "\"\n"
        #codesystem += "* publisher = \"" + stringer.escape(self.publisher) + "\"\n" 
        #codesystem += '* ^experimental = false\n'
        codesystem += '* ^caseSensitive = false\n'
        codesystem += '* ^status = #active\n'
        for code, vals in self.get_properties(id).items():
            codesystem += '* ^property[+].code = #"' + stringer.escape_code(code) + '"\n'
            for k, v in vals.items():
                codesystem += '* ^property[=].' + k + ' = ' + v + "\n" # user is responsible for content

        for code, val in self.get_codes(id).items():
            if isinstance(val, str):
                codesystem += '* #"' + stringer.escape_code(code) +  '" "' + stringer.escape(val) + '"\n'
            elif isinstance(val, dict) and 'display' in val:
                codesystem += '* #"' + stringer.escape_code(code) +  '" "' + stringer.escape(val['display']) + '"\n'
                if 'definition' in val and not stringer.is_blank(val['definition']):
                    codesystem += '  * ^definition = """' + val['definition'] + '\n"""\n'
                if 'designation' in val and isinstance(val['designation'], list):
                    for d_val in val['designation']:
                        if not isinstance(d_val, dict) or not 'value' in d_val:
                            continue
                        codesystem += '  * ^designation[+].value = ' + d_val['value'] + "\n"
                        d_val_copy = dict(d_val)
                        d_val_copy.pop('value')
                        for k, v in d_val_copy.items():
                            codesystem += '  * ^designation[=].' + k + " = " + v + "\n"

                if 'propertyString' in val and isinstance(val['propertyString'], list):
                    for p in val['propertyString']:
                        if not isinstance(p, dict) or not 'code' in p or not 'value' in p:
                            continue
                        codesystem += '  * ^property[+].code = #"' + stringer.escape_code(p['code']) +  '"\n'
                        codesystem += '  * ^property[=].valueString = "' + stringer.escape(p['value']) +  '"\n'

                if 'propertyCode' in val and isinstance(val['propertyCode'], list):
                    for p in val['propertyCode']:
                        if not isinstance(p, dict) or not 'code' in p or not 'value' in p:
                            continue
                        codesystem += '  * ^property[+].code = #"' + stringer.escape_code(p['code']) +  '"\n'
                        codesystem += '  * ^property[=].valueCode = "' + stringer.escape_code(p['value']) +  '"\n'

                if 'propertyCoding' in val and isinstance(val['propertyCoding'], list):
                    for p in val['propertyCoding']:
                        if not isinstance(p, dict) or not 'code' in p or not 'value' in p \
                           or not isinstance(p['value'], dict):
                            continue
                        codesystem += '  * ^property[+].code = #"' + stringer.escape_code(p['code']) +  '"\n'
                        for coding_k, coding_v in p['value'].items():
                            codesystem += '  * ^property[=].valueCoding.' + coding_k + ' = '
                            if coding_k == 'code':
                                codesystem +=  '#' + stringer.escape_code(coding_v) +  '\n'
                            elif coding_k == 'userSelected':
                                codesystem +=  str(coding_v) +  '\n'
                            else:
                                codesystem +=  '"' + stringer.escape(coding_v) +  '"\n'
            else:
                logging.getLogger(self.__class__.__name__).info("  failed to add code (expected string or dict with 'display' property)" + str(code))
                logging.getLogger(self.__class__.__name__).info(val)
        return codesystem

