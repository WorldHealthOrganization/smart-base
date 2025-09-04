# ISCO-08 Data Sources

This directory contains source data files for ISCO-08 (International Standard Classification of Occupations 2008) codes.

## Files

- `ISCO-08_EN_Structure_and_definitions.xlsx` - Excel file containing comprehensive ISCO-08 classification with codes, titles, and definitions from the International Labour Organization (ILO). Contains 182 codes across all levels: major groups (1-digit), sub-major groups (2-digit), minor groups (3-digit), and unit groups (4-digit).

## Processing

The ISCO-08 data is processed by the `input/scripts/isco08_extractor.py` script, which:

1. Reads the Excel source file using pandas
2. Extracts the "ISCO 08 Code", "Title EN", and "Definition" columns  
3. Generates a FHIR CodeSystem definition in FSH format
4. Saves the result to `input/fsh/codesystems/ISCO08.fsh`

## Usage

To regenerate the ISCO-08 CodeSystem from the source data:

```bash
python input/scripts/isco08_extractor.py input/data/ISCO-08_EN_Structure_and_definitions.xlsx
```

## Source

The official ISCO-08 Excel file should be downloaded from:
https://webapps.ilo.org/ilostat-files/ISCO/newdocs-08-2021/ISCO-08/ISCO-08%20EN%20Structure%20and%20definitions.xlsx

The ISCO-08 classification is maintained by the International Labour Organization (ILO).
Official documentation: https://www.ilo.org/public/english/bureau/stat/isco/isco08/

## Dependencies

The extractor script requires:
- pandas>=2.0.0
- openpyxl>=3.1.0

Install with: `pip install pandas openpyxl`

## License

ISCO-08 © International Labour Organization 2008