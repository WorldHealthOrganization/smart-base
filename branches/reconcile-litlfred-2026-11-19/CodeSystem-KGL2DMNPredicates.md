# Knowledge graph L2DMN: predicates - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L2DMN: predicates**

## CodeSystem: Knowledge graph L2DMN: predicates 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/KGL2DMNPredicates | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGL2DMNPredicates |

 
The predicates of the L2DMN layer. An edge's `predicate` is one of these; which (source, target) pairs each licenses is the layer's edge table. Source: smart-base/L1/schemas/L2-DMN.ts (migrated from smart-kg ontology/L2-DMN/L2-DMN.json). 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Knowledge graph L2DMN: predicates](ValueSet-KGL2DMNPredicatesVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "KGL2DMNPredicates",
  "url" : "http://smart.who.int/base/CodeSystem/KGL2DMNPredicates",
  "version" : "0.3.0",
  "name" : "KGL2DMNPredicates",
  "title" : "Knowledge graph L2DMN: predicates",
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
  "description" : "The predicates of the L2DMN layer. An edge's `predicate` is one of these; which (source, target) pairs each licenses is the layer's edge table. Source: smart-base/L1/schemas/L2-DMN.ts (migrated from smart-kg ontology/L2-DMN/L2-DMN.json).",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 3,
  "concept" : [{
    "code" : "invokedBy",
    "display" : "invokedBy",
    "definition" : "A decision is invoked by a business-rule task. Read from dmn:usingTask/@href, whose fragment is the URL-encoded task NAME rather than its id -- so it resolves only while that prose stays byte-identical in the BPMN, punctuation and the en dash in \"Calmette-Guerin\" included. Carries a resolutionStatus; the target is a bpmn-task when the BPMN is present and an opaque l1:external-artifact when it is not."
  },
  {
    "code" : "reads",
    "display" : "reads",
    "definition" : "An input clause reads a data element. Recovered heuristically from free text, so every instance carries the extraction rule that produced it and a resolutionStatus. The target is an l2:data-element -- the DAK component -- so a recovered name and a declared dictionary entry are the same class and can meet when a dictionary exists."
  },
  {
    "code" : "citesSource",
    "display" : "citesSource",
    "definition" : "A decision rule cites an L1 source. The target is an l1:citation minted from the same string by the citation extractor, so the DMN subgraph and the L1 graph join without either knowing the other exists. Grounded but sparse: 1 of 25 BCG rules. The sparseness is the finding -- a rule with no citesSource edge is a rule with no stated source."
  }]
}

```
