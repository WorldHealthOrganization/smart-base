# Knowledge graph L2-BPMN: BPMN Process - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L2-BPMN: BPMN Process**

## Logical Model: Knowledge graph L2-BPMN: BPMN Process 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGBpmnProcess | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGBpmnProcess |

 
One `bpmn:process`. Present as a node because a participant references it by processRef, and without it the pool-to-element attribution has nothing to travel through. Class IRI: http://smart.who.int/kg/bpmn-process. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGBpmnProcess.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGBpmnProcess.csv), [Excel](StructureDefinition-KGBpmnProcess.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGBpmnProcess",
  "url" : "http://smart.who.int/base/StructureDefinition/KGBpmnProcess",
  "version" : "0.3.0",
  "name" : "KGBpmnProcess",
  "title" : "Knowledge graph L2-BPMN: BPMN Process",
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
  "description" : "One `bpmn:process`. Present as a node because a participant references it by processRef, and without it the pool-to-element attribution has nothing to travel through. Class IRI: http://smart.who.int/kg/bpmn-process.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGBpmnProcess",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGBpmnProcess",
      "path" : "KGBpmnProcess",
      "short" : "Knowledge graph L2-BPMN: BPMN Process",
      "definition" : "One `bpmn:process`. Present as a node because a participant references it by processRef, and without it the pool-to-element attribution has nothing to travel through. Class IRI: http://smart.who.int/kg/bpmn-process."
    },
    {
      "id" : "KGBpmnProcess.id",
      "path" : "KGBpmnProcess.id",
      "short" : "Id",
      "definition" : "The identifier the source declares (an FSH instance id, a BPMN or DMN element id).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGBpmnProcess.name",
      "path" : "KGBpmnProcess.name",
      "short" : "Name",
      "definition" : "The computable name: the CamelCase identifier a Canonical() reference matches on.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGBpmnProcess.isExecutable",
      "path" : "KGBpmnProcess.isExecutable",
      "short" : "Is executable",
      "definition" : "The process's isExecutable attribute.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "boolean"
      }]
    }]
  }
}

```
