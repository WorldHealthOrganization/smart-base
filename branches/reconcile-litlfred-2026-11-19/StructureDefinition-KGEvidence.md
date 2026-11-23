# Knowledge graph L1: Evidence - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L1: Evidence**

## Logical Model: Knowledge graph L1: Evidence 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGEvidence | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGEvidence |

 
One row of an evidence profile: the evidence for one outcome of one key question, with its certainty (handbook §9.2). Class IRI: http://smart.who.int/kg/evidence. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGEvidence.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGEvidence.csv), [Excel](StructureDefinition-KGEvidence.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGEvidence",
  "url" : "http://smart.who.int/base/StructureDefinition/KGEvidence",
  "version" : "0.3.0",
  "name" : "KGEvidence",
  "title" : "Knowledge graph L1: Evidence",
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
  "description" : "One row of an evidence profile: the evidence for one outcome of one key question, with its certainty (handbook §9.2). Class IRI: http://smart.who.int/kg/evidence.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGEvidence",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGEvidence",
      "path" : "KGEvidence",
      "short" : "Knowledge graph L1: Evidence",
      "definition" : "One row of an evidence profile: the evidence for one outcome of one key question, with its certainty (handbook §9.2). Class IRI: http://smart.who.int/kg/evidence."
    },
    {
      "id" : "KGEvidence.evidenceType",
      "path" : "KGEvidence.evidenceType",
      "short" : "Evidence type",
      "definition" : "Which kind of evidence a row is, and so which scale its certainty is on: GRADE for effects, GRADE-CERQual for qualitative findings.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://smart.who.int/base/ValueSet/KGEvidenceTypeVS"
      }
    },
    {
      "id" : "KGEvidence.certainty",
      "path" : "KGEvidence.certainty",
      "short" : "Certainty",
      "definition" : "GRADE certainty of evidence.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://smart.who.int/base/ValueSet/KGCertaintyVS"
      }
    },
    {
      "id" : "KGEvidence.summary",
      "path" : "KGEvidence.summary",
      "short" : "Summary",
      "definition" : "Summary of the body of evidence.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGEvidence.studyCount",
      "path" : "KGEvidence.studyCount",
      "short" : "Study count",
      "definition" : "Number of studies in the body of evidence.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "unsignedInt"
      }]
    },
    {
      "id" : "KGEvidence.citation",
      "path" : "KGEvidence.citation",
      "short" : "Citation",
      "definition" : "Bibliographic citation of the evidence review.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGEvidence.contentHash",
      "path" : "KGEvidence.contentHash",
      "short" : "Content hash",
      "definition" : "sha256 of the normalised summary.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    }]
  }
}

```
