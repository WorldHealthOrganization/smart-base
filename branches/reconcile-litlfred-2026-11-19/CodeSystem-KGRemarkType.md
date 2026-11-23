# Knowledge graph L1: remark type - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L1: remark type**

## CodeSystem: Knowledge graph L1: remark type 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/KGRemarkType | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGRemarkType |

 
What a remark is for. Grounded in the six remarks attached to ANC recommendation A.1.1. Source: smart-kg ontology/l1/l1.json valueSets "remark-type"; ANC guideline (2016) p. 15; handbook §10.6, §10.8. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Knowledge graph L1: remark type](ValueSet-KGRemarkTypeVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "KGRemarkType",
  "url" : "http://smart.who.int/base/CodeSystem/KGRemarkType",
  "version" : "0.3.0",
  "name" : "KGRemarkType",
  "title" : "Knowledge graph L1: remark type",
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
  "description" : "What a remark is for. Grounded in the six remarks attached to ANC recommendation A.1.1. Source: smart-kg ontology/l1/l1.json valueSets \"remark-type\"; ANC guideline (2016) p. 15; handbook §10.6, §10.8.",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 7,
  "concept" : [{
    "code" : "definition",
    "display" : "Definition",
    "definition" : "Defines a term used in the recommendation."
  },
  {
    "code" : "implementation",
    "display" : "Implementation",
    "definition" : "How to put the recommendation into practice."
  },
  {
    "code" : "precaution",
    "display" : "Precaution",
    "definition" : "A caution to observe when applying it."
  },
  {
    "code" : "contraindication",
    "display" : "Contraindication",
    "definition" : "When the intervention must not be given."
  },
  {
    "code" : "subgroup",
    "display" : "Subgroup",
    "definition" : "Guidance specific to a subgroup."
  },
  {
    "code" : "research-gap",
    "display" : "Research gap",
    "definition" : "Evidence the guideline group says is still needed (handbook §10.8)."
  },
  {
    "code" : "training",
    "display" : "Training",
    "definition" : "A training or capacity need."
  }]
}

```
