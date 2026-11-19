# Knowledge graph L3: Value Set - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L3: Value Set**

## Logical Model: Knowledge graph L3: Value Set 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGValueSet | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGValueSet |

 
A FHIR ValueSet. 192 in the immunizations IG – the most numerous artefact of all. Indexed by canonical; its expansion, its compose rules and the codes it contains are terminology, which docs/SCOPE.md keeps at arm's length as firmly here as at L1. Class IRI: http://smart.who.int/kg/value-set. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGValueSet.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGValueSet.csv), [Excel](StructureDefinition-KGValueSet.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGValueSet",
  "url" : "http://smart.who.int/base/StructureDefinition/KGValueSet",
  "version" : "0.3.0",
  "name" : "KGValueSet",
  "title" : "Knowledge graph L3: Value Set",
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
  "description" : "A FHIR ValueSet. 192 in the immunizations IG -- the most numerous artefact of all. Indexed by canonical; its expansion, its compose rules and the codes it contains are terminology, which docs/SCOPE.md keeps at arm's length as firmly here as at L1. Class IRI: http://smart.who.int/kg/value-set.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGValueSet",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGValueSet",
      "path" : "KGValueSet",
      "short" : "Knowledge graph L3: Value Set",
      "definition" : "A FHIR ValueSet. 192 in the immunizations IG -- the most numerous artefact of all. Indexed by canonical; its expansion, its compose rules and the codes it contains are terminology, which docs/SCOPE.md keeps at arm's length as firmly here as at L1. Class IRI: http://smart.who.int/kg/value-set."
    },
    {
      "id" : "KGValueSet.canonical",
      "path" : "KGValueSet.canonical",
      "short" : "Canonical",
      "definition" : "The canonical URL. Only a resolved component carries one.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGValueSet.resourceType",
      "path" : "KGValueSet.resourceType",
      "short" : "Resource type",
      "definition" : "The FHIR resource type.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGValueSet.profile",
      "path" : "KGValueSet.profile",
      "short" : "Profile",
      "definition" : "A profile canonical the artefact declares (meta.profile or the requirement's profile).",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGValueSet.status",
      "path" : "KGValueSet.status",
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
      "id" : "KGValueSet.version",
      "path" : "KGValueSet.version",
      "short" : "Version",
      "definition" : "The business version, as declared.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGValueSet.title",
      "path" : "KGValueSet.title",
      "short" : "Title",
      "definition" : "The human-readable title.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGValueSet.name",
      "path" : "KGValueSet.name",
      "short" : "Name",
      "definition" : "The computable name: the CamelCase identifier a Canonical() reference matches on.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGValueSet.publisher",
      "path" : "KGValueSet.publisher",
      "short" : "Publisher",
      "definition" : "The publisher, as declared.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGValueSet.experimental",
      "path" : "KGValueSet.experimental",
      "short" : "Experimental",
      "definition" : "The resource's experimental flag.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "boolean"
      }]
    },
    {
      "id" : "KGValueSet.source",
      "path" : "KGValueSet.source",
      "short" : "Source",
      "definition" : "Where the node was read from: a repository path or URL.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGValueSet.sha256",
      "path" : "KGValueSet.sha256",
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
