<!--badges-->
[![License: CC BY-IGO 3.0](https://licensebuttons.net/l/by-nc/3.0/igo/80x15.png)](https://creativecommons.org/licenses/by/3.0/igo)
![CI Build](https://img.shields.io/github/actions/workflow/status/WorldHealthOrganization/smart-ig-empty/ghbuild.yml)  
   
![QA errors](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2FWorldHealthOrganization.github.io%2Fsmart-ig-empty%2Fqa.json&query=%24.errs&logoColor=red&label=QA%20errors&color=yellow)
![QA warnings](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2FWorldHealthOrganization.github.io%2Fsmart-ig-empty%2Fqa.json&query=%24.warnings&logoColor=orange&label=QA%20warnings&color=yellow)
![QA hints](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2FWorldHealthOrganization.github.io%2Fsmart-ig-empty%2Fqa.json&query=%24.hints&logoColor=yellow&label=QA%20hints&color=yellow)
<!--/badges-->

# WHO SMART GUIDELINES 

This is an empty framework, to be used to create SMART Implementation Guides.

Please see these [instructions](https://smart.who.int/ig-starter-kit/ig_setup.html#github-setup)

CI Build [here](https://worldhealthorganization.github.io/smart-prequal-vaccines/) 

## Generating Instances Locally

To generate FSH logical model instances from the sample data (no API credentials needed):

```bash
python3 scripts/import_salesforce.py --json-file data/prequal.json
```

This reads 35 products from `data/prequal.json` and writes generated FSH files into `input/fsh/`:
- `input/fsh/examples/prequal_database_products.fsh` — FinishedVaccineProducts, Product, and ProductAuthorization instances
- `input/fsh/examples/prequal_database_manufacturers.fsh` — Manufacturer FHIR Organization instances
- `input/fsh/examples/prequal_database_holders.fsh` — NRA/Holder FHIR Organization instances
- `input/fsh/examples/prequal_database_manufacturer_lm.fsh` — PreQualManufacturer LM instances (full address, website)
- `input/fsh/examples/prequal_database_nra_lm.fsh` — PreQualNRA LM instances (country, website)
- `input/fsh/examples/prequal_database_vaccine_lm.fsh` — PreQualVaccine LM instances (vaccine type details)
- `input/fsh/codesystems/` — CodeSystems for presentations, vaccine types, and product identifiers
- `input/fsh/valuesets/` — ValueSet for product identifiers
- `input/fsh/concept_maps/` — ConceptMap from CSV IDs to API IDs

To run tests:

```bash
python3 -m unittest tests/test_import_salesforce.py -v
```

## Sample Generated Instances

For each product in the WHO PreQual database, the import script generates:
1. A `FinishedVaccineProducts` logical model instance (with references to Manufacturer, NRA, and Vaccine LM instances)

Additionally, for each unique referenced object, the script generates:
- `PreQualManufacturer` LM instances (11 unique manufacturers with full address and contact info)
- `PreQualNRA` LM instances (8 unique NRAs with country and website)
- `PreQualVaccine` LM instances (17 unique vaccine types with full and abbreviated names)

Products with missing essential data (e.g. withdrawn products) are automatically skipped.

Here is a sample for the CYVAC malaria vaccine showing the product and its referenced LM instances:

```fsh
Instance: PreQualDBa3K3X000005atRtUAI
InstanceOf: FinishedVaccineProducts
* dateOfPrequal = 2023-12-19
* status = "Prequalified"
* presentation.coding.system = "https://extranet.who.int/prequal/vaccines/prequalified-vaccines"
* presentation.coding.code = #Vial
* presentation.coding.display = "Vial"
* numDoses = 2
* productId.system = "https://extranet.who.int/prequal/api"
* productId.value = "a3K3X000005atRtUAI"
* productName = "FVP-P-447"
* vaccineFullName = "Recombinant malaria vaccine"
* vaccineAbbreviatedName = "Malaria"
* vaccineCommercialName = "CYVAC"
* applicantName = "Serum Institute of India"
* nraName = "Central Drugs Standard Control Organization (CDSCO)"
* manufacturerReference = Reference(Manufacturer0013X00003cPkzfQAC)
* responsibleNRAReference = Reference(Holder0013X0000498p4fQAA)
* manufacturerLM = Reference(PreQualManufacturer0013X00003cPkzfQAC)
* nraLM = Reference(PreQualNRA0013X0000498p4fQAA)
* vaccineLM = Reference(PreQualVaccinea3S3X000003cSpnUAE)

Instance: PreQualManufacturer0013X00003cPkzfQAC
InstanceOf: PreQualManufacturer
* manufacturerId.system = "https://extranet.who.int/prequal/api"
* manufacturerId.value = "0013X00003cPkzfQAC"
* name = "Serum Institute of India"
* addressLine1 = "SERUM BIO-PHARMA PARK SEZ UNIT-1, 212/2 Off Soli Poonawala Road, Hadaspar"
* city = "Pune"
* state = "Maharashtra"
* country = "India"
* postalCode = "411 028"
* isoCountryCode = "IND"
* region = "SEARO"
* website = "http://www.seruminstitute.com/"
* organizationReference = Reference(Manufacturer0013X00003cPkzfQAC)

Instance: PreQualNRA0013X0000498p4fQAA
InstanceOf: PreQualNRA
* nraId.system = "https://extranet.who.int/prequal/api"
* nraId.value = "0013X0000498p4fQAA"
* name = "Central Drugs Standard Control Organization (CDSCO)"
* country = "India"
* website = "www.cdsco.nic.in"
* organizationReference = Reference(Holder0013X0000498p4fQAA)

Instance: PreQualVaccinea3S3X000003cSpnUAE
InstanceOf: PreQualVaccine
* vaccineId.system = "https://extranet.who.int/prequal/api"
* vaccineId.value = "a3S3X000003cSpnUAE"
* fullName = "Recombinant malaria vaccine"
* abbreviatedName = "Malaria"
```

## Changes and feedback

Feedback and issues about this empty framework can be submitted via the [issues](issues) page, and will be incorporated into subsequent releases.

