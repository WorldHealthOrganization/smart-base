# Knowledge graph L3: Concept Map - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L3: Concept Map**

## Logical Model: Knowledge graph L3: Concept Map 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGConceptMap | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGConceptMap |

 
A FHIR ConceptMap – one per target code system in the dictionary's terminology mappings. 8 in the immunizations IG. Records that a mapping exists; the mappings themselves belong to terminology. Class IRI: http://smart.who.int/kg/concept-map. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGConceptMap.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGConceptMap.csv), [Excel](StructureDefinition-KGConceptMap.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGConceptMap",
  "url" : "http://smart.who.int/base/StructureDefinition/KGConceptMap",
  "version" : "0.3.0",
  "name" : "KGConceptMap",
  "title" : "Knowledge graph L3: Concept Map",
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
  "description" : "A FHIR ConceptMap -- one per target code system in the dictionary's terminology mappings. 8 in the immunizations IG. Records that a mapping exists; the mappings themselves belong to terminology. Class IRI: http://smart.who.int/kg/concept-map.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGConceptMap",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGConceptMap",
      "path" : "KGConceptMap",
      "short" : "Knowledge graph L3: Concept Map",
      "definition" : "A FHIR ConceptMap -- one per target code system in the dictionary's terminology mappings. 8 in the immunizations IG. Records that a mapping exists; the mappings themselves belong to terminology. Class IRI: http://smart.who.int/kg/concept-map."
    },
    {
      "id" : "KGConceptMap.canonical",
      "path" : "KGConceptMap.canonical",
      "short" : "Canonical",
      "definition" : "The canonical URL. Only a resolved component carries one.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGConceptMap.resourceType",
      "path" : "KGConceptMap.resourceType",
      "short" : "Resource type",
      "definition" : "The FHIR resource type.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGConceptMap.profile",
      "path" : "KGConceptMap.profile",
      "short" : "Profile",
      "definition" : "A profile canonical the artefact declares (meta.profile or the requirement's profile).",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGConceptMap.status",
      "path" : "KGConceptMap.status",
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
      "id" : "KGConceptMap.version",
      "path" : "KGConceptMap.version",
      "short" : "Version",
      "definition" : "The business version, as declared.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGConceptMap.title",
      "path" : "KGConceptMap.title",
      "short" : "Title",
      "definition" : "The human-readable title.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGConceptMap.name",
      "path" : "KGConceptMap.name",
      "short" : "Name",
      "definition" : "The computable name: the CamelCase identifier a Canonical() reference matches on.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGConceptMap.publisher",
      "path" : "KGConceptMap.publisher",
      "short" : "Publisher",
      "definition" : "The publisher, as declared.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGConceptMap.experimental",
      "path" : "KGConceptMap.experimental",
      "short" : "Experimental",
      "definition" : "The resource's experimental flag.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "boolean"
      }]
    },
    {
      "id" : "KGConceptMap.sourceScope",
      "path" : "KGConceptMap.sourceScope",
      "short" : "Source scope",
      "definition" : "The ConceptMap's sourceScope.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGConceptMap.targetScope",
      "path" : "KGConceptMap.targetScope",
      "short" : "Target scope",
      "definition" : "The ConceptMap's targetScope.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGConceptMap.source",
      "path" : "KGConceptMap.source",
      "short" : "Source",
      "definition" : "Where the node was read from: a repository path or URL.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGConceptMap.sha256",
      "path" : "KGConceptMap.sha256",
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
