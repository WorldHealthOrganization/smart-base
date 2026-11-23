# Knowledge graph L1: Indicator - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L1: Indicator**

## Logical Model: Knowledge graph L1: Indicator 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGIndicator | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGIndicator |

 
A WHO indicator, identified by its published reference number. Printed in several places (HIV SI 2022: summary list, Table 2.3, reference sheet) and stored once. variants is a list of {population, definition, numerator, denominator} for population-specific or level-specific forms (PRV.17, PRV.3). Corresponds to ProgramIndicator: definition, numerator, denominator and disaggregation are ProgramIndicator's elements and types (markdown); not a Parent because ProgramIndicator makes them 1..1 and an L1 indicator is recorded with what its source prints. Class IRI: http://smart.who.int/kg/indicator. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGIndicator.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGIndicator.csv), [Excel](StructureDefinition-KGIndicator.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGIndicator",
  "url" : "http://smart.who.int/base/StructureDefinition/KGIndicator",
  "version" : "0.3.0",
  "name" : "KGIndicator",
  "title" : "Knowledge graph L1: Indicator",
  "status" : "active",
  "date" : "2026-11-23T18:43:32+00:00",
  "publisher" : "WHO",
  "contact" : [{
    "name" : "WHO",
    "telecom" : [{
      "system" : "url",
      "value" : "http://who.int"
    }]
  }],
  "description" : "A WHO indicator, identified by its published reference number. Printed in several places (HIV SI 2022: summary list, Table 2.3, reference sheet) and stored once. variants is a list of {population, definition, numerator, denominator} for population-specific or level-specific forms (PRV.17, PRV.3). Corresponds to ProgramIndicator: definition, numerator, denominator and disaggregation are ProgramIndicator's elements and types (markdown); not a Parent because ProgramIndicator makes them 1..1 and an L1 indicator is recorded with what its source prints. Class IRI: http://smart.who.int/kg/indicator.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGIndicator",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGIndicator",
      "path" : "KGIndicator",
      "short" : "Knowledge graph L1: Indicator",
      "definition" : "A WHO indicator, identified by its published reference number. Printed in several places (HIV SI 2022: summary list, Table 2.3, reference sheet) and stored once. variants is a list of {population, definition, numerator, denominator} for population-specific or level-specific forms (PRV.17, PRV.3). Corresponds to ProgramIndicator: definition, numerator, denominator and disaggregation are ProgramIndicator's elements and types (markdown); not a Parent because ProgramIndicator makes them 1..1 and an L1 indicator is recorded with what its source prints. Class IRI: http://smart.who.int/kg/indicator."
    },
    {
      "id" : "KGIndicator.refNo",
      "path" : "KGIndicator.refNo",
      "short" : "Reference number",
      "definition" : "The indicator's printed reference number (e.g. PRV.3).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGIndicator.shortName",
      "path" : "KGIndicator.shortName",
      "short" : "Short name",
      "definition" : "Short name, as printed.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGIndicator.definition",
      "path" : "KGIndicator.definition",
      "short" : "Definition",
      "definition" : "Definition, verbatim.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGIndicator.numerator",
      "path" : "KGIndicator.numerator",
      "short" : "Numerator",
      "definition" : "Numerator, verbatim.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGIndicator.denominator",
      "path" : "KGIndicator.denominator",
      "short" : "Denominator",
      "definition" : "Denominator, verbatim.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGIndicator.variants",
      "path" : "KGIndicator.variants",
      "short" : "Variants",
      "definition" : "Population- or level-specific forms (PRV.17, PRV.3).",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "BackboneElement"
      }]
    },
    {
      "id" : "KGIndicator.variants.population",
      "path" : "KGIndicator.variants.population",
      "short" : "Population",
      "definition" : "The population this variant is for.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGIndicator.variants.definition",
      "path" : "KGIndicator.variants.definition",
      "short" : "Definition",
      "definition" : "Definition, verbatim.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGIndicator.variants.numerator",
      "path" : "KGIndicator.variants.numerator",
      "short" : "Numerator",
      "definition" : "Numerator, verbatim.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGIndicator.variants.denominator",
      "path" : "KGIndicator.variants.denominator",
      "short" : "Denominator",
      "definition" : "Denominator, verbatim.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGIndicator.whatItMeasures",
      "path" : "KGIndicator.whatItMeasures",
      "short" : "What it measures",
      "definition" : "As printed.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGIndicator.rationale",
      "path" : "KGIndicator.rationale",
      "short" : "Rationale",
      "definition" : "As printed.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGIndicator.methodOfMeasurement",
      "path" : "KGIndicator.methodOfMeasurement",
      "short" : "Method of measurement",
      "definition" : "As printed.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGIndicator.disaggregation",
      "path" : "KGIndicator.disaggregation",
      "short" : "Disaggregation",
      "definition" : "As printed.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGIndicator.programmeArea",
      "path" : "KGIndicator.programmeArea",
      "short" : "Programme area",
      "definition" : "As printed.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGIndicator.isCore",
      "path" : "KGIndicator.isCore",
      "short" : "Is core",
      "definition" : "Whether the publication marks it a core indicator.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "boolean"
      }]
    },
    {
      "id" : "KGIndicator.isSurveyBased",
      "path" : "KGIndicator.isSurveyBased",
      "short" : "Is survey-based",
      "definition" : "Whether it is measured by survey.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "boolean"
      }]
    },
    {
      "id" : "KGIndicator.changeStatus",
      "path" : "KGIndicator.changeStatus",
      "short" : "Change status",
      "definition" : "Whether this edition of a consolidated guideline introduces, updates or carries a recommendation or indicator unchanged.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://smart.who.int/base/ValueSet/KGChangeStatusVS"
      }
    },
    {
      "id" : "KGIndicator.contentHash",
      "path" : "KGIndicator.contentHash",
      "short" : "Content hash",
      "definition" : "sha256 of the normalised definition, numerator and denominator.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    }]
  }
}

```
