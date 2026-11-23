# Knowledge graph L2-BPMN: BPMN Event - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L2-BPMN: BPMN Event**

## Logical Model: Knowledge graph L2-BPMN: BPMN Event 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGBpmnEvent | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGBpmnEvent |

 
A start, end or intermediate event (WHO's DAK BPMN draw intermediate throw and catch events inside sub-processes). Same connectivity argument as gateway, plus one of its own: entry and exit points are what make 'is this task reachable' and 'does this path terminate' answerable at all. Class IRI: http://smart.who.int/kg/bpmn-event. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGBpmnEvent.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGBpmnEvent.csv), [Excel](StructureDefinition-KGBpmnEvent.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGBpmnEvent",
  "url" : "http://smart.who.int/base/StructureDefinition/KGBpmnEvent",
  "version" : "0.3.0",
  "name" : "KGBpmnEvent",
  "title" : "Knowledge graph L2-BPMN: BPMN Event",
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
  "description" : "A start, end or intermediate event (WHO's DAK BPMN draw intermediate throw and catch events inside sub-processes). Same connectivity argument as gateway, plus one of its own: entry and exit points are what make 'is this task reachable' and 'does this path terminate' answerable at all. Class IRI: http://smart.who.int/kg/bpmn-event.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGBpmnEvent",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGBpmnEvent",
      "path" : "KGBpmnEvent",
      "short" : "Knowledge graph L2-BPMN: BPMN Event",
      "definition" : "A start, end or intermediate event (WHO's DAK BPMN draw intermediate throw and catch events inside sub-processes). Same connectivity argument as gateway, plus one of its own: entry and exit points are what make 'is this task reachable' and 'does this path terminate' answerable at all. Class IRI: http://smart.who.int/kg/bpmn-event."
    },
    {
      "id" : "KGBpmnEvent.id",
      "path" : "KGBpmnEvent.id",
      "short" : "Id",
      "definition" : "The identifier the source declares (an FSH instance id, a BPMN or DMN element id).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGBpmnEvent.name",
      "path" : "KGBpmnEvent.name",
      "short" : "Name",
      "definition" : "The computable name: the CamelCase identifier a Canonical() reference matches on.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGBpmnEvent.eventType",
      "path" : "KGBpmnEvent.eventType",
      "short" : "Event type",
      "definition" : "The BPMN event element type (startEvent, endEvent, intermediateCatchEvent, …).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGBpmnEvent.parent",
      "path" : "KGBpmnEvent.parent",
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
