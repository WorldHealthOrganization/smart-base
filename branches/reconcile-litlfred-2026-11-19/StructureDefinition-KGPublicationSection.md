# Knowledge graph L1: Publication section - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L1: Publication section**

## Logical Model: Knowledge graph L1: Publication section 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGPublicationSection | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGPublicationSection |

 
A chapter, annex or numbered section, at any depth. Class IRI: http://smart.who.int/kg/publication-section. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGPublicationSection.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGPublicationSection.csv), [Excel](StructureDefinition-KGPublicationSection.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGPublicationSection",
  "url" : "http://smart.who.int/base/StructureDefinition/KGPublicationSection",
  "version" : "0.3.0",
  "name" : "KGPublicationSection",
  "title" : "Knowledge graph L1: Publication section",
  "status" : "active",
  "date" : "2026-11-19T20:24:57+00:00",
  "publisher" : "WHO",
  "contact" : [{
    "name" : "WHO",
    "telecom" : [{
      "system" : "url",
      "value" : "http://who.int"
    }]
  }],
  "description" : "A chapter, annex or numbered section, at any depth. Class IRI: http://smart.who.int/kg/publication-section.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGPublicationSection",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGPublicationSection",
      "path" : "KGPublicationSection",
      "short" : "Knowledge graph L1: Publication section",
      "definition" : "A chapter, annex or numbered section, at any depth. Class IRI: http://smart.who.int/kg/publication-section."
    },
    {
      "id" : "KGPublicationSection.heading",
      "path" : "KGPublicationSection.heading",
      "short" : "Heading",
      "definition" : "The section heading, verbatim.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGPublicationSection.number",
      "path" : "KGPublicationSection.number",
      "short" : "Number",
      "definition" : "The section number as printed (\"1.2\", \"Annex 3\").",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGPublicationSection.pageRange",
      "path" : "KGPublicationSection.pageRange",
      "short" : "Page range",
      "definition" : "Pages the section occupies, as printed or physical (\"12-18\").",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGPublicationSection.ordinal",
      "path" : "KGPublicationSection.ordinal",
      "short" : "Ordinal",
      "definition" : "Position among its siblings.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "unsignedInt"
      }]
    }]
  }
}

```
