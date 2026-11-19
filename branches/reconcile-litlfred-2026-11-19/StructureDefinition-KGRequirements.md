# Knowledge graph L3: Requirements - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L3: Requirements**

## Logical Model: Knowledge graph L3: Requirements 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGRequirements | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGRequirements |

 
A FHIR Requirements resource. The ONE place the published SOP names an SG profile – SGRequirements – and the grain is one resource per business process holding many statements, not one per requirement. ZERO in the immunizations IG and 41 in smart-base. Class IRI: http://smart.who.int/kg/requirements. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGRequirements.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGRequirements.csv), [Excel](StructureDefinition-KGRequirements.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGRequirements",
  "url" : "http://smart.who.int/base/StructureDefinition/KGRequirements",
  "version" : "0.3.0",
  "name" : "KGRequirements",
  "title" : "Knowledge graph L3: Requirements",
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
  "description" : "A FHIR Requirements resource. The ONE place the published SOP names an SG profile -- SGRequirements -- and the grain is one resource per business process holding many statements, not one per requirement. ZERO in the immunizations IG and 41 in smart-base. Class IRI: http://smart.who.int/kg/requirements.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGRequirements",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGRequirements",
      "path" : "KGRequirements",
      "short" : "Knowledge graph L3: Requirements",
      "definition" : "A FHIR Requirements resource. The ONE place the published SOP names an SG profile -- SGRequirements -- and the grain is one resource per business process holding many statements, not one per requirement. ZERO in the immunizations IG and 41 in smart-base. Class IRI: http://smart.who.int/kg/requirements."
    },
    {
      "id" : "KGRequirements.canonical",
      "path" : "KGRequirements.canonical",
      "short" : "Canonical",
      "definition" : "The canonical URL. Only a resolved component carries one.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGRequirements.resourceType",
      "path" : "KGRequirements.resourceType",
      "short" : "Resource type",
      "definition" : "The FHIR resource type.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGRequirements.profile",
      "path" : "KGRequirements.profile",
      "short" : "Profile",
      "definition" : "A profile canonical the artefact declares (meta.profile or the requirement's profile).",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGRequirements.status",
      "path" : "KGRequirements.status",
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
      "id" : "KGRequirements.version",
      "path" : "KGRequirements.version",
      "short" : "Version",
      "definition" : "The business version, as declared.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGRequirements.title",
      "path" : "KGRequirements.title",
      "short" : "Title",
      "definition" : "The human-readable title.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGRequirements.name",
      "path" : "KGRequirements.name",
      "short" : "Name",
      "definition" : "The computable name: the CamelCase identifier a Canonical() reference matches on.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGRequirements.publisher",
      "path" : "KGRequirements.publisher",
      "short" : "Publisher",
      "definition" : "The publisher, as declared.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGRequirements.experimental",
      "path" : "KGRequirements.experimental",
      "short" : "Experimental",
      "definition" : "The resource's experimental flag.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "boolean"
      }]
    },
    {
      "id" : "KGRequirements.statementCount",
      "path" : "KGRequirements.statementCount",
      "short" : "Statement count",
      "definition" : "How many statements the Requirements resource holds.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "unsignedInt"
      }]
    },
    {
      "id" : "KGRequirements.source",
      "path" : "KGRequirements.source",
      "short" : "Source",
      "definition" : "Where the node was read from: a repository path or URL.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGRequirements.sha256",
      "path" : "KGRequirements.sha256",
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
