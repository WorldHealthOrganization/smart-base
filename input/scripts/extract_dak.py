#!/usr/bin/env python3
"""
WHO SMART Guidleines Digital Adaptation Kit (DAK) Multi-Extractor Pipeline

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
    python extract_dak.py [--run-publisher] [--tx URL] [--publisher-jar PATH]
                          [--skip-commit] [--commit-message MSG]

Author: SMART Guidelines Team
"""
from typing import List, Type
import stringer
import logging
import os
from codesystem_manager import codesystem_manager
from installer import installer
from dd_extractor import dd_extractor
from req_extractor import req_extractor 
from bpmn_extractor import bpmn_extractor
from dt_extractor import dt_extractor
from svg_extractor import svg_extractor
from extractpr import extractpr
from extractor import extractor
import getopt
import sys

try:
    from run_ig_publisher import run_publisher_and_commit_pot as _run_publisher_and_commit_pot
    _PUBLISHER_RUNNER_AVAILABLE = True
except ImportError:  # pragma: no cover
    _PUBLISHER_RUNNER_AVAILABLE = False
    _run_publisher_and_commit_pot = None  # type: ignore[assignment]


class extract_dak:
    """
    Multi-extractor pipeline for comprehensive DAK content processing.
    
    This class coordinates multiple specialized extractors to process
    various types of data and knowledge assets in a single workflow,
    ensuring consistent resource generation and proper integration
    between different content types.
    """
    
    @property
    def logger(self) -> logging.Logger:
        """Get logger instance for this class."""
        return logging.getLogger(self.__class__.__name__)
    
    def usage(self) -> None:
        print("Usage: scans for source DAK L2 content for extraction ")
        print("OPTIONS:")
        print("--run-publisher      : invoke IG Publisher after extraction and commit .pot files")
        print("--tx URL             : terminology server URL for the IG Publisher (use 'n/a' for offline)")
        print("--publisher-jar PATH : explicit path to publisher.jar")
        print("--skip-commit        : run publisher but do not commit .pot files")
        print("--commit-message MSG : custom git commit message for the .pot update")
        print("--help|h             : print this information")
        sys.exit(2)

    def extract(self) -> bool:
        try:
            ins = installer()
            extractors: List[Type[extractor]] = [dd_extractor,bpmn_extractor,svg_extractor,req_extractor,dt_extractor,extractpr]
            for extractor_class in extractors:
                self.logger.info("Initializing extractor " + extractor_class.__name__)
                ext = extractor_class(ins)
                if not ext.extract():
                    classname = extractor_class.__name__
                    self.logger.info(f"ERROR: Could not extract on {classname}")
                    return False
            self.logger.info("Installing generated resources and such")
            return ins.install()
        except Exception as e:            
            self.logger.exception(f"ERROR: Could not extract: {e}")
            return False

    def main(self) -> bool:
        run_publisher = False
        tx = None
        publisher_jar = None
        skip_commit = False
        commit_message = None

        try:
            opts, args = getopt.getopt(
                sys.argv[1:],
                "h",
                [
                    "help",
                    "run-publisher",
                    "tx=",
                    "publisher-jar=",
                    "skip-commit",
                    "commit-message=",
                ],
            )
        except getopt.GetoptError:
            self.usage()

        for opt, val in opts:
            if opt in ("-h", "--help"):
                self.usage()
            elif opt == "--run-publisher":
                run_publisher = True
            elif opt == "--tx":
                tx = val
            elif opt == "--publisher-jar":
                publisher_jar = val
            elif opt == "--skip-commit":
                skip_commit = True
            elif opt == "--commit-message":
                commit_message = val

        if not self.extract():
            sys.exit(1)

        if run_publisher:
            if not _PUBLISHER_RUNNER_AVAILABLE:
                self.logger.error("run_ig_publisher module is not available; cannot run publisher.")
                sys.exit(1)
            ig_root = os.path.dirname(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            )
            self.logger.info("Running IG Publisher and committing .pot files...")
            if not _run_publisher_and_commit_pot(
                ig_root=ig_root,
                publisher_jar=publisher_jar,
                tx=tx,
                skip_commit=skip_commit,
                commit_message=commit_message,
            ):
                self.logger.error("IG Publisher step failed.")
                sys.exit(1)

        return True
    

if __name__ == "__main__":
    extract_dak().main()
