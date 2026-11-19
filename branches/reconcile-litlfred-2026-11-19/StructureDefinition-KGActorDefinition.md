# Knowledge graph L3: Actor Definition - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L3: Actor Definition**

## Logical Model: Knowledge graph L3: Actor Definition 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGActorDefinition | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGActorDefinition |

 
A FHIR ActorDefinition – an L2 persona made a FHIR resource. ZERO in the immunizations IG and 22 in smart-base, which is itself worth a coverage query. The SOP names no profile for it and says one is not currently possible because SUSHI cannot profile an R5 resource in an R4 IG, and it tells authors not to assign an identifier – so expect a bare resource and do not infer more. Class IRI: http://smart.who.int/kg/actor-definition. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGActorDefinition.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGActorDefinition.csv), [Excel](StructureDefinition-KGActorDefinition.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGActorDefinition",
  "url" : "http://smart.who.int/base/StructureDefinition/KGActorDefinition",
  "version" : "0.3.0",
  "name" : "KGActorDefinition",
  "title" : "Knowledge graph L3: Actor Definition",
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
  "description" : "A FHIR ActorDefinition -- an L2 persona made a FHIR resource. ZERO in the immunizations IG and 22 in smart-base, which is itself worth a coverage query. The SOP names no profile for it and says one is not currently possible because SUSHI cannot profile an R5 resource in an R4 IG, and it tells authors not to assign an identifier -- so expect a bare resource and do not infer more. Class IRI: http://smart.who.int/kg/actor-definition.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGActorDefinition",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGActorDefinition",
      "path" : "KGActorDefinition",
      "short" : "Knowledge graph L3: Actor Definition",
      "definition" : "A FHIR ActorDefinition -- an L2 persona made a FHIR resource. ZERO in the immunizations IG and 22 in smart-base, which is itself worth a coverage query. The SOP names no profile for it and says one is not currently possible because SUSHI cannot profile an R5 resource in an R4 IG, and it tells authors not to assign an identifier -- so expect a bare resource and do not infer more. Class IRI: http://smart.who.int/kg/actor-definition."
    },
    {
      "id" : "KGActorDefinition.canonical",
      "path" : "KGActorDefinition.canonical",
      "short" : "Canonical",
      "definition" : "The canonical URL. Only a resolved component carries one.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGActorDefinition.resourceType",
      "path" : "KGActorDefinition.resourceType",
      "short" : "Resource type",
      "definition" : "The FHIR resource type.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGActorDefinition.profile",
      "path" : "KGActorDefinition.profile",
      "short" : "Profile",
      "definition" : "A profile canonical the artefact declares (meta.profile or the requirement's profile).",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGActorDefinition.status",
      "path" : "KGActorDefinition.status",
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
      "id" : "KGActorDefinition.version",
      "path" : "KGActorDefinition.version",
      "short" : "Version",
      "definition" : "The business version, as declared.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGActorDefinition.title",
      "path" : "KGActorDefinition.title",
      "short" : "Title",
      "definition" : "The human-readable title.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGActorDefinition.name",
      "path" : "KGActorDefinition.name",
      "short" : "Name",
      "definition" : "The computable name: the CamelCase identifier a Canonical() reference matches on.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGActorDefinition.publisher",
      "path" : "KGActorDefinition.publisher",
      "short" : "Publisher",
      "definition" : "The publisher, as declared.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGActorDefinition.experimental",
      "path" : "KGActorDefinition.experimental",
      "short" : "Experimental",
      "definition" : "The resource's experimental flag.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "boolean"
      }]
    },
    {
      "id" : "KGActorDefinition.actorType",
      "path" : "KGActorDefinition.actorType",
      "short" : "Actor type",
      "definition" : "The ActorDefinition's type (person, system).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGActorDefinition.source",
      "path" : "KGActorDefinition.source",
      "short" : "Source",
      "definition" : "Where the node was read from: a repository path or URL.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGActorDefinition.sha256",
      "path" : "KGActorDefinition.sha256",
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
