# Knowledge graph L2BPMN: predicates - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L2BPMN: predicates**

## CodeSystem: Knowledge graph L2BPMN: predicates 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/KGL2BPMNPredicates | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGL2BPMNPredicates |

 
The predicates of the L2BPMN layer. An edge's `predicate` is one of these; which (source, target) pairs each licenses is the layer's edge table. Source: smart-base/L1/schemas/L2-BPMN.ts (migrated from smart-kg ontology/L2-BPMN/L2-BPMN.json). 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Knowledge graph L2BPMN: predicates](ValueSet-KGL2BPMNPredicatesVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "KGL2BPMNPredicates",
  "url" : "http://smart.who.int/base/CodeSystem/KGL2BPMNPredicates",
  "version" : "0.3.0",
  "name" : "KGL2BPMNPredicates",
  "title" : "Knowledge graph L2BPMN: predicates",
  "status" : "active",
  "experimental" : false,
  "date" : "2026-11-23T18:43:32+00:00",
  "publisher" : "WHO",
  "contact" : [{
    "name" : "WHO",
    "telecom" : [{
      "system" : "url",
      "value" : "http://who.int"
    }]
  }],
  "description" : "The predicates of the L2BPMN layer. An edge's `predicate` is one of these; which (source, target) pairs each licenses is the layer's edge table. Source: smart-base/L1/schemas/L2-BPMN.ts (migrated from smart-kg ontology/L2-BPMN/L2-BPMN.json).",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 3,
  "concept" : [{
    "code" : "flowsTo",
    "display" : "flowsTo",
    "definition" : "A sequence flow, within one process. The qualifier carries the flow's name where it has one -- 6 of 70 in the lifecycle BPMN, all gateway branches such as \"Yes - approved\". No flow in that file carries a conditionExpression, so the label is the whole of the branch condition and nothing more is claimed. `openQualifier` says the value is free text authored in the diagram, not a term from a vocabulary, so an unseen label is not a finding."
  },
  {
    "code" : "messageTo",
    "display" : "messageTo",
    "definition" : "A message flow, which by definition crosses participants. Kept distinct from flowsTo because a handoff between two roles is what governance and country adaptation look for, and burying 10 of them among 70 intra-process flows loses them."
  },
  {
    "code" : "performedBy",
    "display" : "performedBy",
    "definition" : "A participant pool, or a DAK task (from its lane, else its pool, as the task-annotations sidecar records it), is performed by a persona. For a pool: STRING EQUALITY between the pool's @name and an ActorDefinition's title, across two file formats with no shared identifier. Compare l2:fulfilledBy, where a requirement names a persona by Canonical() and resolves without guessing -- the mechanism exists; BPMN does not use it. Every instance carries a resolutionStatus."
  }]
}

```
