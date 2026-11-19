# Knowledge graph L2-BPMN: BPMN Participant - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L2-BPMN: BPMN Participant**

## Logical Model: Knowledge graph L2-BPMN: BPMN Participant 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGBpmnParticipant | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGBpmnParticipant |

 
A pool: a role that owns part of the collaboration. The lifecycle BPMN has 8 and declares no laneSet at all, so the pool is the only unit of role assignment present and its @name is the sole link to a persona. Class IRI: http://smart.who.int/kg/bpmn-participant. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGBpmnParticipant.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGBpmnParticipant.csv), [Excel](StructureDefinition-KGBpmnParticipant.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGBpmnParticipant",
  "url" : "http://smart.who.int/base/StructureDefinition/KGBpmnParticipant",
  "version" : "0.3.0",
  "name" : "KGBpmnParticipant",
  "title" : "Knowledge graph L2-BPMN: BPMN Participant",
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
  "description" : "A pool: a role that owns part of the collaboration. The lifecycle BPMN has 8 and declares no laneSet at all, so the pool is the only unit of role assignment present and its @name is the sole link to a persona. Class IRI: http://smart.who.int/kg/bpmn-participant.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGBpmnParticipant",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGBpmnParticipant",
      "path" : "KGBpmnParticipant",
      "short" : "Knowledge graph L2-BPMN: BPMN Participant",
      "definition" : "A pool: a role that owns part of the collaboration. The lifecycle BPMN has 8 and declares no laneSet at all, so the pool is the only unit of role assignment present and its @name is the sole link to a persona. Class IRI: http://smart.who.int/kg/bpmn-participant."
    },
    {
      "id" : "KGBpmnParticipant.id",
      "path" : "KGBpmnParticipant.id",
      "short" : "Id",
      "definition" : "The identifier the source declares (an FSH instance id, a BPMN or DMN element id).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGBpmnParticipant.name",
      "path" : "KGBpmnParticipant.name",
      "short" : "Name",
      "definition" : "The computable name: the CamelCase identifier a Canonical() reference matches on.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGBpmnParticipant.processRef",
      "path" : "KGBpmnParticipant.processRef",
      "short" : "Process ref",
      "definition" : "The id of the process the participant's pool holds.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    }]
  }
}

```
