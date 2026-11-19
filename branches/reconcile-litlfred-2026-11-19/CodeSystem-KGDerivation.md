# Knowledge graph: derivation - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph: derivation**

## CodeSystem: Knowledge graph: derivation 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/KGDerivation | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGDerivation |

 
How a node or edge of a SMART Guidelines knowledge graph came to be. Every node and edge is exactly one of the three, and `decided` is the one a reviewer needs to find. Source: smart-kg shapes/recommendation-graph.schema.json $defs.derivation. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Knowledge graph: derivation](ValueSet-KGDerivationVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "KGDerivation",
  "url" : "http://smart.who.int/base/CodeSystem/KGDerivation",
  "version" : "0.3.0",
  "name" : "KGDerivation",
  "title" : "Knowledge graph: derivation",
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
  "description" : "How a node or edge of a SMART Guidelines knowledge graph came to be. Every node and edge is exactly one of the three, and `decided` is the one a reviewer needs to find. Source: smart-kg shapes/recommendation-graph.schema.json $defs.derivation.",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 3,
  "concept" : [{
    "code" : "derived",
    "display" : "Derived",
    "definition" : "Mechanically produced, no choice involved."
  },
  {
    "code" : "inferred",
    "display" : "Inferred",
    "definition" : "A rule that could reasonably have gone another way."
  },
  {
    "code" : "decided",
    "display" : "Decided",
    "definition" : "The source is silent and someone chose."
  }]
}

```
