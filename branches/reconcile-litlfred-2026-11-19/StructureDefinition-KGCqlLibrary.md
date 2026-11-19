# Knowledge graph L3: CQL File - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L3: CQL File**

## Logical Model: Knowledge graph L3: CQL File 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGCqlLibrary | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGCqlLibrary |

 
A .cql file on disk, as opposed to the FHIR Library resource that wraps it. A node so that the mapping table's four CQL rows – CQL Concepts and CQL Data Elements under Elements, CQL under Decision Tables, CQL IndicatorLogic under Indicators – do not dead-end. It carries a name, a path and a hash and NOTHING about the logic: no expressions, no comment tags, no data requirements. 279 in the immunizations IG. The l3-cql subgraph is where that content belongs, and it is not built yet. No canonical, because a .cql file is not a FHIR resource and has no canonical URL. It is reached through the Library that wraps it. Class IRI: http://smart.who.int/kg/cql-library. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGCqlLibrary.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGCqlLibrary.csv), [Excel](StructureDefinition-KGCqlLibrary.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGCqlLibrary",
  "url" : "http://smart.who.int/base/StructureDefinition/KGCqlLibrary",
  "version" : "0.3.0",
  "name" : "KGCqlLibrary",
  "title" : "Knowledge graph L3: CQL File",
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
  "description" : "A .cql file on disk, as opposed to the FHIR Library resource that wraps it. A node so that the mapping table's four CQL rows -- CQL Concepts and CQL Data Elements under Elements, CQL under Decision Tables, CQL IndicatorLogic under Indicators -- do not dead-end. It carries a name, a path and a hash and NOTHING about the logic: no expressions, no comment tags, no data requirements. 279 in the immunizations IG. The l3-cql subgraph is where that content belongs, and it is not built yet. No canonical, because a .cql file is not a FHIR resource and has no canonical URL. It is reached through the Library that wraps it. Class IRI: http://smart.who.int/kg/cql-library.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGCqlLibrary",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGCqlLibrary",
      "path" : "KGCqlLibrary",
      "short" : "Knowledge graph L3: CQL File",
      "definition" : "A .cql file on disk, as opposed to the FHIR Library resource that wraps it. A node so that the mapping table's four CQL rows -- CQL Concepts and CQL Data Elements under Elements, CQL under Decision Tables, CQL IndicatorLogic under Indicators -- do not dead-end. It carries a name, a path and a hash and NOTHING about the logic: no expressions, no comment tags, no data requirements. 279 in the immunizations IG. The l3-cql subgraph is where that content belongs, and it is not built yet. No canonical, because a .cql file is not a FHIR resource and has no canonical URL. It is reached through the Library that wraps it. Class IRI: http://smart.who.int/kg/cql-library."
    },
    {
      "id" : "KGCqlLibrary.name",
      "path" : "KGCqlLibrary.name",
      "short" : "Name",
      "definition" : "The computable name: the CamelCase identifier a Canonical() reference matches on.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGCqlLibrary.path",
      "path" : "KGCqlLibrary.path",
      "short" : "Path",
      "definition" : "The repository path of the .cql file.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGCqlLibrary.libraryType",
      "path" : "KGCqlLibrary.libraryType",
      "short" : "Library type",
      "definition" : "The Library's type (logic-library, model-definition, …).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGCqlLibrary.source",
      "path" : "KGCqlLibrary.source",
      "short" : "Source",
      "definition" : "Where the node was read from: a repository path or URL.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGCqlLibrary.sha256",
      "path" : "KGCqlLibrary.sha256",
      "short" : "SHA-256",
      "definition" : "Hash of the file the node was read from; pins the source.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    }]
  }
}

```
