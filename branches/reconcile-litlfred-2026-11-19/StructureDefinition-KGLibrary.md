# Knowledge graph L3: Library - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L3: Library**

## Logical Model: Knowledge graph L3: Library 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGLibrary | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGLibrary |

 
A FHIR Library – the resource that carries CQL. Indexed by canonical and status only. Its CONTENTS are deliberately out of scope: a future l3-cql subgraph will elaborate this same IRI, exactly as l2-bpmn elaborates a BPMN file. 279 in the immunizations IG, joined to their PlanDefinition by the `{id}Logic` suffix. Class IRI: http://smart.who.int/kg/library. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGLibrary.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGLibrary.csv), [Excel](StructureDefinition-KGLibrary.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGLibrary",
  "url" : "http://smart.who.int/base/StructureDefinition/KGLibrary",
  "version" : "0.3.0",
  "name" : "KGLibrary",
  "title" : "Knowledge graph L3: Library",
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
  "description" : "A FHIR Library -- the resource that carries CQL. Indexed by canonical and status only. Its CONTENTS are deliberately out of scope: a future l3-cql subgraph will elaborate this same IRI, exactly as l2-bpmn elaborates a BPMN file. 279 in the immunizations IG, joined to their PlanDefinition by the `{id}Logic` suffix. Class IRI: http://smart.who.int/kg/library.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGLibrary",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGLibrary",
      "path" : "KGLibrary",
      "short" : "Knowledge graph L3: Library",
      "definition" : "A FHIR Library -- the resource that carries CQL. Indexed by canonical and status only. Its CONTENTS are deliberately out of scope: a future l3-cql subgraph will elaborate this same IRI, exactly as l2-bpmn elaborates a BPMN file. 279 in the immunizations IG, joined to their PlanDefinition by the `{id}Logic` suffix. Class IRI: http://smart.who.int/kg/library."
    },
    {
      "id" : "KGLibrary.canonical",
      "path" : "KGLibrary.canonical",
      "short" : "Canonical",
      "definition" : "The canonical URL. Only a resolved component carries one.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGLibrary.resourceType",
      "path" : "KGLibrary.resourceType",
      "short" : "Resource type",
      "definition" : "The FHIR resource type.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGLibrary.profile",
      "path" : "KGLibrary.profile",
      "short" : "Profile",
      "definition" : "A profile canonical the artefact declares (meta.profile or the requirement's profile).",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGLibrary.status",
      "path" : "KGLibrary.status",
      "short" : "Status",
      "definition" : "The resource's status (FHIR PublicationStatus).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://smart.who.int/base/ValueSet/KGPublicationStatusVS"
      }
    },
    {
      "id" : "KGLibrary.version",
      "path" : "KGLibrary.version",
      "short" : "Version",
      "definition" : "The business version, as declared.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGLibrary.title",
      "path" : "KGLibrary.title",
      "short" : "Title",
      "definition" : "The human-readable title.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGLibrary.name",
      "path" : "KGLibrary.name",
      "short" : "Name",
      "definition" : "The computable name: the CamelCase identifier a Canonical() reference matches on.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGLibrary.publisher",
      "path" : "KGLibrary.publisher",
      "short" : "Publisher",
      "definition" : "The publisher, as declared.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGLibrary.experimental",
      "path" : "KGLibrary.experimental",
      "short" : "Experimental",
      "definition" : "The resource's experimental flag.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "boolean"
      }]
    },
    {
      "id" : "KGLibrary.libraryType",
      "path" : "KGLibrary.libraryType",
      "short" : "Library type",
      "definition" : "The Library's type (logic-library, model-definition, …).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGLibrary.source",
      "path" : "KGLibrary.source",
      "short" : "Source",
      "definition" : "Where the node was read from: a repository path or URL.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGLibrary.sha256",
      "path" : "KGLibrary.sha256",
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
