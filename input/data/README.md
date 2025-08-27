# ISCO-08 Data Sources

This directory contains source data files for ISCO-08 (International Standard Classification of Occupations 2008) codes.

## Files

- `isco08.xml` - XML structure containing ISCO-08 classification hierarchy from the International Labour Organization (ILO)

## Processing

The ISCO-08 data is processed by the `input/scripts/isco08_extractor.py` script, which:

1. Reads the XML source file
2. Extracts the hierarchical occupation codes and descriptions
3. Generates a FHIR CodeSystem definition in FSH format
4. Saves the result to `input/fsh/codesystems/ISCO08.fsh`

## Usage

To regenerate the ISCO-08 CodeSystem from the source data:

```bash
python input/scripts/isco08_extractor.py input/data/isco08.xml
```

## Source

The ISCO-08 classification is maintained by the International Labour Organization (ILO).
Official documentation: https://www.ilo.org/public/english/bureau/stat/isco/isco08/

## License

ISCO-08 © International Labour Organization 2008