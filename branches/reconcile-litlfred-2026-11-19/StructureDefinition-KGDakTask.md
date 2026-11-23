# Knowledge graph L2: Task Entry - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L2: Task Entry**

## Logical Model: Knowledge graph L2: Task Entry 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGDakTask | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGDakTask |

 
One task of a DAK business process, as the DAK document's "notes and annotations" describe it: identifier, name, description, and the personas, data elements, requirements and decision tables it links to. A node rather than a property because the same task is also drawn in the BPMN file, and the two have to be joinable to be checkable against each other (`describes`). Read from a BPMN file's `dak-task-annotations/v1` sidecar (smart-base/L2-bpmn/schemas/task-annotations.ts); BusinessProcessWorkflow's `task 0..*` backbone carries the first three fields of the same thing. Class IRI: http://smart.who.int/kg/dak-task. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGDakTask.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGDakTask.csv), [Excel](StructureDefinition-KGDakTask.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGDakTask",
  "url" : "http://smart.who.int/base/StructureDefinition/KGDakTask",
  "version" : "0.3.0",
  "name" : "KGDakTask",
  "title" : "Knowledge graph L2: Task Entry",
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
  "description" : "One task of a DAK business process, as the DAK document's \"notes and annotations\" describe it: identifier, name, description, and the personas, data elements, requirements and decision tables it links to. A node rather than a property because the same task is also drawn in the BPMN file, and the two have to be joinable to be checkable against each other (`describes`). Read from a BPMN file's `dak-task-annotations/v1` sidecar (smart-base/L2-bpmn/schemas/task-annotations.ts); BusinessProcessWorkflow's `task 0..*` backbone carries the first three fields of the same thing. Class IRI: http://smart.who.int/kg/dak-task.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGDakTask",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGDakTask",
      "path" : "KGDakTask",
      "short" : "Knowledge graph L2: Task Entry",
      "definition" : "One task of a DAK business process, as the DAK document's \"notes and annotations\" describe it: identifier, name, description, and the personas, data elements, requirements and decision tables it links to. A node rather than a property because the same task is also drawn in the BPMN file, and the two have to be joinable to be checkable against each other (`describes`). Read from a BPMN file's `dak-task-annotations/v1` sidecar (smart-base/L2-bpmn/schemas/task-annotations.ts); BusinessProcessWorkflow's `task 0..*` backbone carries the first three fields of the same thing. Class IRI: http://smart.who.int/kg/dak-task."
    },
    {
      "id" : "KGDakTask.identifier",
      "path" : "KGDakTask.identifier",
      "short" : "Identifier",
      "definition" : "The identifier, as declared.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDakTask.name",
      "path" : "KGDakTask.name",
      "short" : "Name",
      "definition" : "The computable name: the CamelCase identifier a Canonical() reference matches on.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDakTask.description",
      "path" : "KGDakTask.description",
      "short" : "Description",
      "definition" : "A description, as the source gives it.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGDakTask.activityId",
      "path" : "KGDakTask.activityId",
      "short" : "Activity id",
      "definition" : "The DAK activity id (`IMMZ.B1`, `TB.A5`): the process id and the step number, the key the DAK spreadsheets use.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDakTask.matchedBy",
      "path" : "KGDakTask.matchedBy",
      "short" : "Matched by",
      "definition" : "How the annotation was joined to its BPMN task: `id`, `step-number`, `name` or `adjudicated` by a person.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDakTask.sourceDocument",
      "path" : "KGDakTask.sourceDocument",
      "short" : "Source document",
      "definition" : "The L1 library document the annotation was read from.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDakTask.sourceItem",
      "path" : "KGDakTask.sourceItem",
      "short" : "Source item",
      "definition" : "The annotation's item number as printed (`1`, `2.3`).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDakTask.source",
      "path" : "KGDakTask.source",
      "short" : "Source",
      "definition" : "Where the node was read from: a repository path or URL.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    }]
  }
}

```
