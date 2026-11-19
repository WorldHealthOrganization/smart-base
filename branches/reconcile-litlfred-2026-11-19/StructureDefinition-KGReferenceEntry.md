# Knowledge graph L1: Reference entry - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L1: Reference entry**

## Logical Model: Knowledge graph L1: Reference entry 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGReferenceEntry | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGReferenceEntry |

 
One row of a DAK artefact's own reference list: '(1)' and the full bibliographic text and URL it stands for. Resolved once; every citation numbered to it shares the result. Class IRI: http://smart.who.int/kg/reference-entry. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGReferenceEntry.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGReferenceEntry.csv), [Excel](StructureDefinition-KGReferenceEntry.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGReferenceEntry",
  "url" : "http://smart.who.int/base/StructureDefinition/KGReferenceEntry",
  "version" : "0.3.0",
  "name" : "KGReferenceEntry",
  "title" : "Knowledge graph L1: Reference entry",
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
  "description" : "One row of a DAK artefact's own reference list: '(1)' and the full bibliographic text and URL it stands for. Resolved once; every citation numbered to it shares the result. Class IRI: http://smart.who.int/kg/reference-entry.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGReferenceEntry",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGReferenceEntry",
      "path" : "KGReferenceEntry",
      "short" : "Knowledge graph L1: Reference entry",
      "definition" : "One row of a DAK artefact's own reference list: '(1)' and the full bibliographic text and URL it stands for. Resolved once; every citation numbered to it shares the result. Class IRI: http://smart.who.int/kg/reference-entry."
    },
    {
      "id" : "KGReferenceEntry.number",
      "path" : "KGReferenceEntry.number",
      "short" : "Number",
      "definition" : "The entry's number in the reference list.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGReferenceEntry.text",
      "path" : "KGReferenceEntry.text",
      "short" : "Text",
      "definition" : "The full bibliographic text, verbatim.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGReferenceEntry.url",
      "path" : "KGReferenceEntry.url",
      "short" : "URL",
      "definition" : "The URL the entry prints.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGReferenceEntry.resolutionStatus",
      "path" : "KGReferenceEntry.resolutionStatus",
      "short" : "Resolution status",
      "definition" : "Whether a citation string has been matched to what it cites.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://smart.who.int/base/ValueSet/KGResolutionStatusVS"
      }
    }]
  }
}

```
