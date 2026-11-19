# Knowledge graph L3: Structure Map - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L3: Structure Map**

## Logical Model: Knowledge graph L3: Structure Map 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGStructureMap | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGStructureMap |

 
A FHIR StructureMap. The SOP requires them in threes – QuestionnaireResponse to logical model, logical model to resource, and a grouping map – so a count that is not a multiple of three is worth a look. 16 .fml files in the immunizations IG. Class IRI: http://smart.who.int/kg/structure-map. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGStructureMap.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGStructureMap.csv), [Excel](StructureDefinition-KGStructureMap.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGStructureMap",
  "url" : "http://smart.who.int/base/StructureDefinition/KGStructureMap",
  "version" : "0.3.0",
  "name" : "KGStructureMap",
  "title" : "Knowledge graph L3: Structure Map",
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
  "description" : "A FHIR StructureMap. The SOP requires them in threes -- QuestionnaireResponse to logical model, logical model to resource, and a grouping map -- so a count that is not a multiple of three is worth a look. 16 .fml files in the immunizations IG. Class IRI: http://smart.who.int/kg/structure-map.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGStructureMap",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGStructureMap",
      "path" : "KGStructureMap",
      "short" : "Knowledge graph L3: Structure Map",
      "definition" : "A FHIR StructureMap. The SOP requires them in threes -- QuestionnaireResponse to logical model, logical model to resource, and a grouping map -- so a count that is not a multiple of three is worth a look. 16 .fml files in the immunizations IG. Class IRI: http://smart.who.int/kg/structure-map."
    },
    {
      "id" : "KGStructureMap.canonical",
      "path" : "KGStructureMap.canonical",
      "short" : "Canonical",
      "definition" : "The canonical URL. Only a resolved component carries one.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGStructureMap.resourceType",
      "path" : "KGStructureMap.resourceType",
      "short" : "Resource type",
      "definition" : "The FHIR resource type.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGStructureMap.profile",
      "path" : "KGStructureMap.profile",
      "short" : "Profile",
      "definition" : "A profile canonical the artefact declares (meta.profile or the requirement's profile).",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGStructureMap.status",
      "path" : "KGStructureMap.status",
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
      "id" : "KGStructureMap.version",
      "path" : "KGStructureMap.version",
      "short" : "Version",
      "definition" : "The business version, as declared.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGStructureMap.title",
      "path" : "KGStructureMap.title",
      "short" : "Title",
      "definition" : "The human-readable title.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGStructureMap.name",
      "path" : "KGStructureMap.name",
      "short" : "Name",
      "definition" : "The computable name: the CamelCase identifier a Canonical() reference matches on.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGStructureMap.publisher",
      "path" : "KGStructureMap.publisher",
      "short" : "Publisher",
      "definition" : "The publisher, as declared.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGStructureMap.experimental",
      "path" : "KGStructureMap.experimental",
      "short" : "Experimental",
      "definition" : "The resource's experimental flag.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "boolean"
      }]
    },
    {
      "id" : "KGStructureMap.source",
      "path" : "KGStructureMap.source",
      "short" : "Source",
      "definition" : "Where the node was read from: a repository path or URL.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGStructureMap.sha256",
      "path" : "KGStructureMap.sha256",
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
