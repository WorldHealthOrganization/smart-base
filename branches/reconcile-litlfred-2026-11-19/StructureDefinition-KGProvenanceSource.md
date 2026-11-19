# Knowledge graph: provenance source - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph: provenance source**

## Logical Model: Knowledge graph: provenance source 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGProvenanceSource | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGProvenanceSource |

 
A source a graph document was extracted from, pinned by hash. 

**Usages:**

* Use this Logical Model: [Knowledge graph L1: graph document](StructureDefinition-KGGraphDocument.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGProvenanceSource.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGProvenanceSource.csv), [Excel](StructureDefinition-KGProvenanceSource.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGProvenanceSource",
  "url" : "http://smart.who.int/base/StructureDefinition/KGProvenanceSource",
  "version" : "0.3.0",
  "name" : "KGProvenanceSource",
  "title" : "Knowledge graph: provenance source",
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
  "description" : "A source a graph document was extracted from, pinned by hash.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGProvenanceSource",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGProvenanceSource",
      "path" : "KGProvenanceSource",
      "short" : "Knowledge graph: provenance source",
      "definition" : "A source a graph document was extracted from, pinned by hash."
    },
    {
      "id" : "KGProvenanceSource.path",
      "path" : "KGProvenanceSource.path",
      "short" : "Path",
      "definition" : "Path of the source.",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGProvenanceSource.sha256",
      "path" : "KGProvenanceSource.sha256",
      "short" : "SHA-256",
      "definition" : "Hash of the source (64 lower-case hex digits).",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGProvenanceSource.repository",
      "path" : "KGProvenanceSource.repository",
      "short" : "Repository",
      "definition" : "Repository holding the source.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGProvenanceSource.commit",
      "path" : "KGProvenanceSource.commit",
      "short" : "Commit",
      "definition" : "Commit the source was read at.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGProvenanceSource.note",
      "path" : "KGProvenanceSource.note",
      "short" : "Note",
      "definition" : "What the hash covers, where that is not obvious.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    }]
  }
}

```
