# Knowledge graph L3: Profile - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L3: Profile**

## Logical Model: Knowledge graph L3: Profile 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGProfile | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGProfile |

 
A StructureDefinition constraining a FHIR resource. Separate from structure-definition for the reason above. 5 in the immunizations IG. Its internals – differentials, element definitions, bindings – are the clearest case of what this layer refuses to re-represent. Class IRI: http://smart.who.int/kg/profile. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGProfile.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGProfile.csv), [Excel](StructureDefinition-KGProfile.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGProfile",
  "url" : "http://smart.who.int/base/StructureDefinition/KGProfile",
  "version" : "0.3.0",
  "name" : "KGProfile",
  "title" : "Knowledge graph L3: Profile",
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
  "description" : "A StructureDefinition constraining a FHIR resource. Separate from structure-definition for the reason above. 5 in the immunizations IG. Its internals -- differentials, element definitions, bindings -- are the clearest case of what this layer refuses to re-represent. Class IRI: http://smart.who.int/kg/profile.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGProfile",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGProfile",
      "path" : "KGProfile",
      "short" : "Knowledge graph L3: Profile",
      "definition" : "A StructureDefinition constraining a FHIR resource. Separate from structure-definition for the reason above. 5 in the immunizations IG. Its internals -- differentials, element definitions, bindings -- are the clearest case of what this layer refuses to re-represent. Class IRI: http://smart.who.int/kg/profile."
    },
    {
      "id" : "KGProfile.canonical",
      "path" : "KGProfile.canonical",
      "short" : "Canonical",
      "definition" : "The canonical URL. Only a resolved component carries one.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGProfile.resourceType",
      "path" : "KGProfile.resourceType",
      "short" : "Resource type",
      "definition" : "The FHIR resource type.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGProfile.profile",
      "path" : "KGProfile.profile",
      "short" : "Profile",
      "definition" : "A profile canonical the artefact declares (meta.profile or the requirement's profile).",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGProfile.status",
      "path" : "KGProfile.status",
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
      "id" : "KGProfile.version",
      "path" : "KGProfile.version",
      "short" : "Version",
      "definition" : "The business version, as declared.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGProfile.title",
      "path" : "KGProfile.title",
      "short" : "Title",
      "definition" : "The human-readable title.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGProfile.name",
      "path" : "KGProfile.name",
      "short" : "Name",
      "definition" : "The computable name: the CamelCase identifier a Canonical() reference matches on.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGProfile.publisher",
      "path" : "KGProfile.publisher",
      "short" : "Publisher",
      "definition" : "The publisher, as declared.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGProfile.experimental",
      "path" : "KGProfile.experimental",
      "short" : "Experimental",
      "definition" : "The resource's experimental flag.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "boolean"
      }]
    },
    {
      "id" : "KGProfile.baseDefinition",
      "path" : "KGProfile.baseDefinition",
      "short" : "Base definition",
      "definition" : "The profile's baseDefinition.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGProfile.source",
      "path" : "KGProfile.source",
      "short" : "Source",
      "definition" : "Where the node was read from: a repository path or URL.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGProfile.sha256",
      "path" : "KGProfile.sha256",
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
