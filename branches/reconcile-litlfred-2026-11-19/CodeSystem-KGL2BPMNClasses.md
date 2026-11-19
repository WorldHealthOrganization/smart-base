# Knowledge graph L2BPMN: classes - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L2BPMN: classes**

## CodeSystem: Knowledge graph L2BPMN: classes 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/KGL2BPMNClasses | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGL2BPMNClasses |

 
The classes of the L2BPMN layer of the SMART Guidelines knowledge graph. A node's `type` is one of these. Source: smart-base/L1/schemas/L2-BPMN.ts (migrated from smart-kg ontology/L2-BPMN/L2-BPMN.json). 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Knowledge graph L2BPMN: classes](ValueSet-KGL2BPMNClassesVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "KGL2BPMNClasses",
  "url" : "http://smart.who.int/base/CodeSystem/KGL2BPMNClasses",
  "version" : "0.3.0",
  "name" : "KGL2BPMNClasses",
  "title" : "Knowledge graph L2BPMN: classes",
  "status" : "active",
  "experimental" : false,
  "date" : "2026-11-19T20:24:57+00:00",
  "publisher" : "WHO",
  "contact" : [{
    "name" : "WHO",
    "telecom" : [{
      "system" : "url",
      "value" : "http://who.int"
    }]
  }],
  "description" : "The classes of the L2BPMN layer of the SMART Guidelines knowledge graph. A node's `type` is one of these. Source: smart-base/L1/schemas/L2-BPMN.ts (migrated from smart-kg ontology/L2-BPMN/L2-BPMN.json).",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 6,
  "concept" : [{
    "code" : "bpmn-definitions",
    "display" : "BPMN File",
    "definition" : "One BPMN file as a unit -- the `bpmn:definitions` root. Shares its IRI with the l1:external-artifact for the same file, so the component that points at it and the subgraph that opens it name one resource."
  },
  {
    "code" : "bpmn-process",
    "display" : "BPMN Process",
    "definition" : "One `bpmn:process`. Present as a node because a participant references it by processRef, and without it the pool-to-element attribution has nothing to travel through."
  },
  {
    "code" : "bpmn-participant",
    "display" : "BPMN Participant",
    "definition" : "A pool: a role that owns part of the collaboration. The lifecycle BPMN has 8 and declares no laneSet at all, so the pool is the only unit of role assignment present and its @name is the sole link to a persona."
  },
  {
    "code" : "bpmn-task",
    "display" : "BPMN Task",
    "definition" : "A task or sub-process. It is what a DMN usingTask href points at, what sequence flows connect, and what a DAK-level task entry describes. Sub-processes carry isSubProcess rather than getting a class of their own -- the lifecycle BPMN has exactly one."
  },
  {
    "code" : "bpmn-gateway",
    "display" : "BPMN Gateway",
    "definition" : "A branch or merge. Included for connectivity rather than for a cross-model edge: a flow through a gateway with no node would point at nothing, and every reachability question over the process would break at the first decision point."
  },
  {
    "code" : "bpmn-event",
    "display" : "BPMN Event",
    "definition" : "A start, end or intermediate event (WHO's DAK BPMN draw intermediate throw and catch events inside sub-processes). Same connectivity argument as gateway, plus one of its own: entry and exit points are what make 'is this task reachable' and 'does this path terminate' answerable at all."
  }]
}

```
