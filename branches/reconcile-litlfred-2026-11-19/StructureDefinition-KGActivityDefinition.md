# Knowledge graph L3: Activity Definition - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L3: Activity Definition**

## Logical Model: Knowledge graph L3: Activity Definition 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGActivityDefinition | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGActivityDefinition |

 
A FHIR ActivityDefinition – the concrete act a plan's action invokes. Reached from a PlanDefinition action's `definitionCanonical`, which is a real reference rather than a convention. 3 in the immunizations IG: two cpg-immunizationactivity, one cpg-communicationactivity. Class IRI: http://smart.who.int/kg/activity-definition. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGActivityDefinition.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGActivityDefinition.csv), [Excel](StructureDefinition-KGActivityDefinition.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGActivityDefinition",
  "url" : "http://smart.who.int/base/StructureDefinition/KGActivityDefinition",
  "version" : "0.3.0",
  "name" : "KGActivityDefinition",
  "title" : "Knowledge graph L3: Activity Definition",
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
  "description" : "A FHIR ActivityDefinition -- the concrete act a plan's action invokes. Reached from a PlanDefinition action's `definitionCanonical`, which is a real reference rather than a convention. 3 in the immunizations IG: two cpg-immunizationactivity, one cpg-communicationactivity. Class IRI: http://smart.who.int/kg/activity-definition.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGActivityDefinition",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGActivityDefinition",
      "path" : "KGActivityDefinition",
      "short" : "Knowledge graph L3: Activity Definition",
      "definition" : "A FHIR ActivityDefinition -- the concrete act a plan's action invokes. Reached from a PlanDefinition action's `definitionCanonical`, which is a real reference rather than a convention. 3 in the immunizations IG: two cpg-immunizationactivity, one cpg-communicationactivity. Class IRI: http://smart.who.int/kg/activity-definition."
    },
    {
      "id" : "KGActivityDefinition.canonical",
      "path" : "KGActivityDefinition.canonical",
      "short" : "Canonical",
      "definition" : "The canonical URL. Only a resolved component carries one.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGActivityDefinition.resourceType",
      "path" : "KGActivityDefinition.resourceType",
      "short" : "Resource type",
      "definition" : "The FHIR resource type.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGActivityDefinition.profile",
      "path" : "KGActivityDefinition.profile",
      "short" : "Profile",
      "definition" : "A profile canonical the artefact declares (meta.profile or the requirement's profile).",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGActivityDefinition.status",
      "path" : "KGActivityDefinition.status",
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
      "id" : "KGActivityDefinition.version",
      "path" : "KGActivityDefinition.version",
      "short" : "Version",
      "definition" : "The business version, as declared.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGActivityDefinition.title",
      "path" : "KGActivityDefinition.title",
      "short" : "Title",
      "definition" : "The human-readable title.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGActivityDefinition.name",
      "path" : "KGActivityDefinition.name",
      "short" : "Name",
      "definition" : "The computable name: the CamelCase identifier a Canonical() reference matches on.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGActivityDefinition.publisher",
      "path" : "KGActivityDefinition.publisher",
      "short" : "Publisher",
      "definition" : "The publisher, as declared.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGActivityDefinition.experimental",
      "path" : "KGActivityDefinition.experimental",
      "short" : "Experimental",
      "definition" : "The resource's experimental flag.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "boolean"
      }]
    },
    {
      "id" : "KGActivityDefinition.source",
      "path" : "KGActivityDefinition.source",
      "short" : "Source",
      "definition" : "Where the node was read from: a repository path or URL.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGActivityDefinition.sha256",
      "path" : "KGActivityDefinition.sha256",
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
