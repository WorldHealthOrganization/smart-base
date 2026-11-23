# Knowledge graph: evidence location - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph: evidence location**

## Logical Model: Knowledge graph: evidence location 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGEvidenceLocation | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGEvidenceLocation |

 
Where a node or edge came from in its source. Required on anything not mechanically derived. 

**Usages:**

* Use this Logical Model: [Knowledge graph: edge](StructureDefinition-KGEdge.md) and [Knowledge graph: node](StructureDefinition-KGNode.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGEvidenceLocation.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGEvidenceLocation.csv), [Excel](StructureDefinition-KGEvidenceLocation.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGEvidenceLocation",
  "url" : "http://smart.who.int/base/StructureDefinition/KGEvidenceLocation",
  "version" : "0.3.0",
  "name" : "KGEvidenceLocation",
  "title" : "Knowledge graph: evidence location",
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
  "description" : "Where a node or edge came from in its source. Required on anything not mechanically derived.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGEvidenceLocation",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGEvidenceLocation",
      "path" : "KGEvidenceLocation",
      "short" : "Knowledge graph: evidence location",
      "definition" : "Where a node or edge came from in its source. Required on anything not mechanically derived."
    },
    {
      "id" : "KGEvidenceLocation.location",
      "path" : "KGEvidenceLocation.location",
      "short" : "Location",
      "definition" : "file:line, a spreadsheet sheet and cell, or a BPMN element id.",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGEvidenceLocation.quote",
      "path" : "KGEvidenceLocation.quote",
      "short" : "Quote",
      "definition" : "Verbatim text from the source.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGEvidenceLocation.artifact",
      "path" : "KGEvidenceLocation.artifact",
      "short" : "Artifact",
      "definition" : "The generated artifact affected, where one exists.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGEvidenceLocation.by",
      "path" : "KGEvidenceLocation.by",
      "short" : "By",
      "definition" : "Who made the judgement; required when derivation is decided.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGEvidenceLocation.at",
      "path" : "KGEvidenceLocation.at",
      "short" : "At",
      "definition" : "When the judgement was made; required when derivation is decided.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "date"
      }]
    }]
  }
}

```
