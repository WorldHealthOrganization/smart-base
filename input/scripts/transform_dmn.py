#!/usr/bin/env python3
"""
DMN to HTML Transformation Script

This standalone script transforms DMN (Decision Model and Notation) XML files
to HTML tables using XSLT, designed to be run as part of the GitHub Actions
CI/CD pipeline before the IG publisher.

Usage:
    python transform_dmn.py [--dmn-dir DIR] [--output-dir DIR] [--xslt-file FILE]

Arguments:
    --dmn-dir       Directory containing .dmn files (default: input/dmn)
    --output-dir    Directory to save HTML files (default: input/pagecontent)
    --xslt-file     Path to XSLT transformation file (default: input/includes/dmn2html.xslt)
"""

import argparse
import glob
import logging
import os
import sys
from pathlib import Path
from typing import Optional

import lxml.etree as ET


def setup_logging() -> logging.Logger:
    """Set up logging configuration."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(levelname)s: %(message)s'
    )
    return logging.getLogger(__name__)


def load_xslt_transformer(xslt_path: Path, logger: logging.Logger) -> Optional[ET.XSLT]:
    """
    Load and compile the XSLT transformer.
    
    Args:
        xslt_path: Path to the XSLT file
        logger: Logger instance
        
    Returns:
        Compiled XSLT transformer or None if failed
    """
    try:
        # Register DMN namespace
        ET.register_namespace('dmn', "https://www.omg.org/spec/DMN/20240513/MODEL/")
        
        logger.info(f"Loading XSLT transformer from {xslt_path}")
        with open(xslt_path, "rb") as f:
            xslt_doc = ET.parse(f)
            return ET.XSLT(xslt_doc)
    except Exception as e:
        logger.error(f"Failed to load XSLT transformer from {xslt_path}: {e}")
        return None


def transform_dmn_file(dmn_path: Path, output_path: Path, transformer: ET.XSLT, logger: logging.Logger) -> bool:
    """
    Transform a single DMN file to HTML.
    
    Args:
        dmn_path: Path to the DMN file
        output_path: Path for the output HTML file
        transformer: Compiled XSLT transformer
        logger: Logger instance
        
    Returns:
        True if successful, False otherwise
    """
    try:
        logger.info(f"Transforming {dmn_path} -> {output_path}")
        
        # Parse the DMN XML file
        with open(dmn_path, "rb") as f:
            dmn_doc = ET.parse(f)
        
        # Apply XSLT transformation
        result = transformer(dmn_doc)
        
        # Write the HTML output
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(str(ET.tostring(
                result.getroot(),
                encoding="unicode",
                pretty_print=True,
                doctype=None
            )))
        
        logger.info(f"Successfully transformed {dmn_path.name}")
        return True
        
    except Exception as e:
        logger.error(f"Failed to transform {dmn_path}: {e}")
        return False


def main():
    """Main function to handle command line arguments and coordinate transformation."""
    parser = argparse.ArgumentParser(
        description="Transform DMN files to HTML using XSLT",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    
    parser.add_argument(
        "--dmn-dir",
        type=Path,
        default=Path("input/dmn"),
        help="Directory containing .dmn files (default: input/dmn)"
    )
    
    parser.add_argument(
        "--output-dir", 
        type=Path,
        default=Path("input/pagecontent"),
        help="Directory to save HTML files (default: input/pagecontent)"
    )
    
    parser.add_argument(
        "--xslt-file",
        type=Path,
        default=Path("input/includes/dmn2html.xslt"),
        help="Path to XSLT transformation file (default: input/includes/dmn2html.xslt)"
    )
    
    args = parser.parse_args()
    logger = setup_logging()
    
    # Validate inputs
    if not args.xslt_file.exists():
        logger.error(f"XSLT file not found: {args.xslt_file}")
        sys.exit(1)
    
    if not args.dmn_dir.exists():
        logger.warning(f"DMN directory not found: {args.dmn_dir}")
        logger.info("No DMN files to transform")
        sys.exit(0)
    
    # Load XSLT transformer
    transformer = load_xslt_transformer(args.xslt_file, logger)
    if not transformer:
        sys.exit(1)
    
    # Find all DMN files
    dmn_files = list(args.dmn_dir.glob("*.dmn"))
    if not dmn_files:
        logger.info(f"No .dmn files found in {args.dmn_dir}")
        sys.exit(0)
    
    logger.info(f"Found {len(dmn_files)} DMN files to transform")
    
    # Transform each DMN file
    success_count = 0
    for dmn_file in dmn_files:
        # Output file will have same name but .xml extension
        output_file = args.output_dir / f"{dmn_file.stem}.xml"
        
        if transform_dmn_file(dmn_file, output_file, transformer, logger):
            success_count += 1
    
    logger.info(f"Successfully transformed {success_count}/{len(dmn_files)} DMN files")
    
    if success_count != len(dmn_files):
        sys.exit(1)


if __name__ == "__main__":
    main()