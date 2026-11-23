# Knowledge graph L2-BPMN: BPMN Task - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L2-BPMN: BPMN Task**

## Logical Model: Knowledge graph L2-BPMN: BPMN Task 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGBpmnTask | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGBpmnTask |

 
A task or sub-process. It is what a DMN usingTask href points at, what sequence flows connect, and what a DAK-level task entry describes. Sub-processes carry isSubProcess rather than getting a class of their own – the lifecycle BPMN has exactly one. Class IRI: http://smart.who.int/kg/bpmn-task. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGBpmnTask.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGBpmnTask.csv), [Excel](StructureDefinition-KGBpmnTask.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGBpmnTask",
  "url" : "http://smart.who.int/base/StructureDefinition/KGBpmnTask",
  "version" : "0.3.0",
  "name" : "KGBpmnTask",
  "title" : "Knowledge graph L2-BPMN: BPMN Task",
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
  "description" : "A task or sub-process. It is what a DMN usingTask href points at, what sequence flows connect, and what a DAK-level task entry describes. Sub-processes carry isSubProcess rather than getting a class of their own -- the lifecycle BPMN has exactly one. Class IRI: http://smart.who.int/kg/bpmn-task.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGBpmnTask",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGBpmnTask",
      "path" : "KGBpmnTask",
      "short" : "Knowledge graph L2-BPMN: BPMN Task",
      "definition" : "A task or sub-process. It is what a DMN usingTask href points at, what sequence flows connect, and what a DAK-level task entry describes. Sub-processes carry isSubProcess rather than getting a class of their own -- the lifecycle BPMN has exactly one. Class IRI: http://smart.who.int/kg/bpmn-task."
    },
    {
      "id" : "KGBpmnTask.id",
      "path" : "KGBpmnTask.id",
      "short" : "Id",
      "definition" : "The identifier the source declares (an FSH instance id, a BPMN or DMN element id).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGBpmnTask.name",
      "path" : "KGBpmnTask.name",
      "short" : "Name",
      "definition" : "The computable name: the CamelCase identifier a Canonical() reference matches on.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGBpmnTask.taskType",
      "path" : "KGBpmnTask.taskType",
      "short" : "Task type",
      "definition" : "The BPMN element type (userTask, serviceTask, businessRuleTask, subProcess, …).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGBpmnTask.isSubProcess",
      "path" : "KGBpmnTask.isSubProcess",
      "short" : "Is sub-process",
      "definition" : "Whether the activity is a sub-process.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "boolean"
      }]
    },
    {
      "id" : "KGBpmnTask.parent",
      "path" : "KGBpmnTask.parent",
      "short" : "Parent",
      "definition" : "The id of the sub-process that contains it, when nested.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    }]
  }
}

```
