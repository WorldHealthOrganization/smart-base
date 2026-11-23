# Knowledge graph L3: Plan Definition - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L3: Plan Definition**

## Logical Model: Knowledge graph L3: Plan Definition 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGPlanDefinition | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGPlanDefinition |

 
A FHIR PlanDefinition. The published mapping gives it two sources – Processes and Decision Tables – so a PlanDefinition alone does not say which it came from; the implementedBy edge does. 138 in the immunizations IG, all declaring cpg-recommendationdefinition, all decision tables. Shares its IRI with the l1:external-artifact for the same canonical. Class IRI: http://smart.who.int/kg/plan-definition. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGPlanDefinition.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGPlanDefinition.csv), [Excel](StructureDefinition-KGPlanDefinition.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGPlanDefinition",
  "url" : "http://smart.who.int/base/StructureDefinition/KGPlanDefinition",
  "version" : "0.3.0",
  "name" : "KGPlanDefinition",
  "title" : "Knowledge graph L3: Plan Definition",
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
  "description" : "A FHIR PlanDefinition. The published mapping gives it two sources -- Processes and Decision Tables -- so a PlanDefinition alone does not say which it came from; the implementedBy edge does. 138 in the immunizations IG, all declaring cpg-recommendationdefinition, all decision tables. Shares its IRI with the l1:external-artifact for the same canonical. Class IRI: http://smart.who.int/kg/plan-definition.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGPlanDefinition",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGPlanDefinition",
      "path" : "KGPlanDefinition",
      "short" : "Knowledge graph L3: Plan Definition",
      "definition" : "A FHIR PlanDefinition. The published mapping gives it two sources -- Processes and Decision Tables -- so a PlanDefinition alone does not say which it came from; the implementedBy edge does. 138 in the immunizations IG, all declaring cpg-recommendationdefinition, all decision tables. Shares its IRI with the l1:external-artifact for the same canonical. Class IRI: http://smart.who.int/kg/plan-definition."
    },
    {
      "id" : "KGPlanDefinition.canonical",
      "path" : "KGPlanDefinition.canonical",
      "short" : "Canonical",
      "definition" : "The canonical URL. Only a resolved component carries one.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGPlanDefinition.resourceType",
      "path" : "KGPlanDefinition.resourceType",
      "short" : "Resource type",
      "definition" : "The FHIR resource type.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGPlanDefinition.profile",
      "path" : "KGPlanDefinition.profile",
      "short" : "Profile",
      "definition" : "A profile canonical the artefact declares (meta.profile or the requirement's profile).",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGPlanDefinition.status",
      "path" : "KGPlanDefinition.status",
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
      "id" : "KGPlanDefinition.version",
      "path" : "KGPlanDefinition.version",
      "short" : "Version",
      "definition" : "The business version, as declared.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGPlanDefinition.title",
      "path" : "KGPlanDefinition.title",
      "short" : "Title",
      "definition" : "The human-readable title.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGPlanDefinition.name",
      "path" : "KGPlanDefinition.name",
      "short" : "Name",
      "definition" : "The computable name: the CamelCase identifier a Canonical() reference matches on.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGPlanDefinition.publisher",
      "path" : "KGPlanDefinition.publisher",
      "short" : "Publisher",
      "definition" : "The publisher, as declared.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGPlanDefinition.experimental",
      "path" : "KGPlanDefinition.experimental",
      "short" : "Experimental",
      "definition" : "The resource's experimental flag.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "boolean"
      }]
    },
    {
      "id" : "KGPlanDefinition.source",
      "path" : "KGPlanDefinition.source",
      "short" : "Source",
      "definition" : "Where the node was read from: a repository path or URL.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGPlanDefinition.sha256",
      "path" : "KGPlanDefinition.sha256",
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
