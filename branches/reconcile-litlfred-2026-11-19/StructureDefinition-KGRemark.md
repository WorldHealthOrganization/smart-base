# Knowledge graph L1: Remark - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L1: Remark**

## Logical Model: Knowledge graph L1: Remark 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGRemark | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGRemark |

 
A remark attached to a recommendation (handbook §10.6). May also be printed as a table footnote. Class IRI: http://smart.who.int/kg/remark. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGRemark.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGRemark.csv), [Excel](StructureDefinition-KGRemark.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGRemark",
  "url" : "http://smart.who.int/base/StructureDefinition/KGRemark",
  "version" : "0.3.0",
  "name" : "KGRemark",
  "title" : "Knowledge graph L1: Remark",
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
  "description" : "A remark attached to a recommendation (handbook §10.6). May also be printed as a table footnote. Class IRI: http://smart.who.int/kg/remark.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGRemark",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGRemark",
      "path" : "KGRemark",
      "short" : "Knowledge graph L1: Remark",
      "definition" : "A remark attached to a recommendation (handbook §10.6). May also be printed as a table footnote. Class IRI: http://smart.who.int/kg/remark."
    },
    {
      "id" : "KGRemark.text",
      "path" : "KGRemark.text",
      "short" : "Text",
      "definition" : "The remark, verbatim.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGRemark.remarkType",
      "path" : "KGRemark.remarkType",
      "short" : "Remark type",
      "definition" : "What a remark is for.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://smart.who.int/base/ValueSet/KGRemarkTypeVS"
      }
    },
    {
      "id" : "KGRemark.ordinal",
      "path" : "KGRemark.ordinal",
      "short" : "Ordinal",
      "definition" : "Position among the recommendation's remarks.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "unsignedInt"
      }]
    },
    {
      "id" : "KGRemark.contentHash",
      "path" : "KGRemark.contentHash",
      "short" : "Content hash",
      "definition" : "sha256 of the normalised text.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    }]
  }
}

```
