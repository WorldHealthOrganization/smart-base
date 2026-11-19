# Knowledge graph L3: Logical Model - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L3: Logical Model**

## Logical Model: Knowledge graph L3: Logical Model 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGStructureDefinition | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGStructureDefinition |

 
A StructureDefinition with kind `logical` – one data dictionary tab as a data structure. Distinct from `profile`, which constrains a FHIR resource: WHO's ArchiMate model has Logical Model realising Data Object while Profile realises Data Element, and the two are not interchangeable. 15 in the immunizations IG. Class IRI: http://smart.who.int/kg/structure-definition. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGStructureDefinition.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGStructureDefinition.csv), [Excel](StructureDefinition-KGStructureDefinition.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGStructureDefinition",
  "url" : "http://smart.who.int/base/StructureDefinition/KGStructureDefinition",
  "version" : "0.3.0",
  "name" : "KGStructureDefinition",
  "title" : "Knowledge graph L3: Logical Model",
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
  "description" : "A StructureDefinition with kind `logical` -- one data dictionary tab as a data structure. Distinct from `profile`, which constrains a FHIR resource: WHO's ArchiMate model has Logical Model realising Data Object while Profile realises Data Element, and the two are not interchangeable. 15 in the immunizations IG. Class IRI: http://smart.who.int/kg/structure-definition.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGStructureDefinition",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGStructureDefinition",
      "path" : "KGStructureDefinition",
      "short" : "Knowledge graph L3: Logical Model",
      "definition" : "A StructureDefinition with kind `logical` -- one data dictionary tab as a data structure. Distinct from `profile`, which constrains a FHIR resource: WHO's ArchiMate model has Logical Model realising Data Object while Profile realises Data Element, and the two are not interchangeable. 15 in the immunizations IG. Class IRI: http://smart.who.int/kg/structure-definition."
    },
    {
      "id" : "KGStructureDefinition.canonical",
      "path" : "KGStructureDefinition.canonical",
      "short" : "Canonical",
      "definition" : "The canonical URL. Only a resolved component carries one.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGStructureDefinition.resourceType",
      "path" : "KGStructureDefinition.resourceType",
      "short" : "Resource type",
      "definition" : "The FHIR resource type.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGStructureDefinition.profile",
      "path" : "KGStructureDefinition.profile",
      "short" : "Profile",
      "definition" : "A profile canonical the artefact declares (meta.profile or the requirement's profile).",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGStructureDefinition.status",
      "path" : "KGStructureDefinition.status",
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
      "id" : "KGStructureDefinition.version",
      "path" : "KGStructureDefinition.version",
      "short" : "Version",
      "definition" : "The business version, as declared.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGStructureDefinition.title",
      "path" : "KGStructureDefinition.title",
      "short" : "Title",
      "definition" : "The human-readable title.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGStructureDefinition.name",
      "path" : "KGStructureDefinition.name",
      "short" : "Name",
      "definition" : "The computable name: the CamelCase identifier a Canonical() reference matches on.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGStructureDefinition.publisher",
      "path" : "KGStructureDefinition.publisher",
      "short" : "Publisher",
      "definition" : "The publisher, as declared.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGStructureDefinition.experimental",
      "path" : "KGStructureDefinition.experimental",
      "short" : "Experimental",
      "definition" : "The resource's experimental flag.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "boolean"
      }]
    },
    {
      "id" : "KGStructureDefinition.kind",
      "path" : "KGStructureDefinition.kind",
      "short" : "Kind",
      "definition" : "The StructureDefinition's kind.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://smart.who.int/base/ValueSet/KGStructureDefinitionKindVS"
      }
    },
    {
      "id" : "KGStructureDefinition.source",
      "path" : "KGStructureDefinition.source",
      "short" : "Source",
      "definition" : "Where the node was read from: a repository path or URL.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGStructureDefinition.sha256",
      "path" : "KGStructureDefinition.sha256",
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
