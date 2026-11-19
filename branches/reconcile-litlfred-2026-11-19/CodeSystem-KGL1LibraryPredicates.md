# Knowledge graph L1Library: predicates - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L1Library: predicates**

## CodeSystem: Knowledge graph L1Library: predicates 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/KGL1LibraryPredicates | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGL1LibraryPredicates |

 
The predicates of the L1Library layer. An edge's `predicate` is one of these; which (source, target) pairs each licenses is the layer's edge table. Source: smart-base/L1/schemas/l1-library.ts (migrated from smart-kg ontology/l1-library/l1-library.json). 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Knowledge graph L1Library: predicates](ValueSet-KGL1LibraryPredicatesVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "KGL1LibraryPredicates",
  "url" : "http://smart.who.int/base/CodeSystem/KGL1LibraryPredicates",
  "version" : "0.3.0",
  "name" : "KGL1LibraryPredicates",
  "title" : "Knowledge graph L1Library: predicates",
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
  "description" : "The predicates of the L1Library layer. An edge's `predicate` is one of these; which (source, target) pairs each licenses is the layer's edge table. Source: smart-base/L1/schemas/l1-library.ts (migrated from smart-kg ontology/l1-library/l1-library.json).",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 1,
  "concept" : [{
    "code" : "specializationOf",
    "display" : "specializationOf",
    "definition" : "An L1 layout node to the library node it specialises: the same printed thing, with L1's more specific aspects. Upstream only."
  }]
}

```
