#!/usr/bin/env python3
"""
Data and Knowledge (DAK) Multi-Extractor Pipeline

This command-line script orchestrates the extraction of multiple types of
data and knowledge assets for the SMART guidelines system. It coordinates
various specialized extractors to process different file formats and data
sources in a unified workflow.

The script integrates multiple extractors including:
- Data Dictionary (DD) extractor for structured data definitions
- Requirements extractor for functional specifications  
- BPMN extractor for business process models
- Decision Table (DT) extractor for clinical decision logic
- SVG extractor for visual diagrams and illustrations

This provides a comprehensive pipeline for processing all DAK L2 content
into FHIR-compatible resources.

Usage:
    python extract_dak.py

Author: SMART Guidelines Team
"""

import stringer
import logging
from typing import List, Type, Any
from codesystem_manager import codesystem_manager
from installer import installer
from dd_extractor import dd_extractor
from req_extractor import req_extractor 
from bpmn_extractor import bpmn_extractor
from dt_extractor import dt_extractor
from svg_extractor import svg_extractor
import getopt
import sys


class extract_dak:
    """
    Multi-extractor pipeline for comprehensive DAK content processing.
    
    This class coordinates multiple specialized extractors to process
    various types of data and knowledge assets in a single workflow,
    ensuring consistent resource generation and proper integration
    between different content types.
    
    Attributes:
        extractors (List[Type[Any]]): List of extractor classes to run
    """
    
    extractors = [dd_extractor, bpmn_extractor, svg_extractor, req_extractor, dt_extractor]
    
    def usage(self) -> None:
        """
        Display usage information and exit.
        
        Prints command-line usage instructions and available options
        before terminating the program.
        """
        print("Usage: scans for source DAK L2 content for extraction ")
        print("OPTIONS:")
        print(" none")
        print("--help|h : print this information")
        sys.exit(2)

    def extract(self) -> bool:
        """
        Execute the multi-extractor pipeline.
        
        Initializes an installer instance and runs all configured extractors
        in sequence, processing various types of DAK content.
        
        Returns:
            True if all extraction and installation completed successfully
        """
        try:
            ins = installer()
            for extractor_class in self.extractors:
                logging.getLogger(self.__class__.__name__).info("Initializing extractor " + extractor_class.__name__)
                ext = extractor_class(ins)
                if not ext.extract():
                    classname = extractor_class.__name__
                    logging.getLogger(self.__class__.__name__).info(f"ERROR: Could not extract on {classname}")
                    return False
            logging.getLogger(self.__class__.__name__).info("Installing generated resources and such")
            return ins.install()
        except Exception as e:            
            logging.getLogger(self.__class__.__name__).exception(f"ERROR: Could not extract: {e}")
            return False

    def main(self) -> bool:
        """
        Main entry point for the DAK extraction script.
        
        Handles command-line argument processing and orchestrates
        the extraction workflow.
        
        Returns:
            True if successful, calls sys.exit(1) on failure
        """
        try:
            opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
        except getopt.GetoptError:
            self.usage()

        if not self.extract():
            sys.exit(1)
        return True
    

if __name__ == "__main__":
    extract_dak().main()
