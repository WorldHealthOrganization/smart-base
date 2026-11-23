# Knowledge graph L1: recommendation direction - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L1: recommendation direction**

## CodeSystem: Knowledge graph L1: recommendation direction 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/KGRecommendationDirection | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGRecommendationDirection |

 
For or against. The handbook prefers "we recommend against X" to "X is not recommended", which is ambiguous between against and no recommendation (§10.6). Source: smart-kg ontology/l1/l1.json valueSets "recommendation-direction"; WHO handbook for guideline development (2014) §10.1, §10.6. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Knowledge graph L1: recommendation direction](ValueSet-KGRecommendationDirectionVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "KGRecommendationDirection",
  "url" : "http://smart.who.int/base/CodeSystem/KGRecommendationDirection",
  "version" : "0.3.0",
  "name" : "KGRecommendationDirection",
  "title" : "Knowledge graph L1: recommendation direction",
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
  "description" : "For or against. The handbook prefers \"we recommend against X\" to \"X is not recommended\", which is ambiguous between against and no recommendation (§10.6). Source: smart-kg ontology/l1/l1.json valueSets \"recommendation-direction\"; WHO handbook for guideline development (2014) §10.1, §10.6.",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 2,
  "concept" : [{
    "code" : "for",
    "display" : "For",
    "definition" : "The recommendation is in favour of the intervention."
  },
  {
    "code" : "against",
    "display" : "Against",
    "definition" : "The recommendation is against the intervention."
  }]
}

```
