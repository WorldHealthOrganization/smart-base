# Knowledge graph L1: certainty - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L1: certainty**

## CodeSystem: Knowledge graph L1: certainty 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/KGCertainty | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGCertainty |

 
GRADE certainty of evidence. The 2014 handbook calls it quality of evidence and names certainty as a synonym (§9.1). Rated per outcome on evidence; the overall certainty on a recommendation is the lowest across its critical outcomes (§9.6). Source: smart-kg ontology/l1/l1.json valueSets "certainty"; WHO handbook for guideline development (2014) §9.1, §9.5–9.6. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Knowledge graph L1: certainty](ValueSet-KGCertaintyVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "KGCertainty",
  "url" : "http://smart.who.int/base/CodeSystem/KGCertainty",
  "version" : "0.3.0",
  "name" : "KGCertainty",
  "title" : "Knowledge graph L1: certainty",
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
  "description" : "GRADE certainty of evidence. The 2014 handbook calls it quality of evidence and names certainty as a synonym (§9.1). Rated per outcome on evidence; the overall certainty on a recommendation is the lowest across its critical outcomes (§9.6). Source: smart-kg ontology/l1/l1.json valueSets \"certainty\"; WHO handbook for guideline development (2014) §9.1, §9.5–9.6.",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 4,
  "concept" : [{
    "code" : "high",
    "display" : "High",
    "definition" : "Very confident the true effect lies close to the estimate."
  },
  {
    "code" : "moderate",
    "display" : "Moderate",
    "definition" : "Moderately confident; the true effect is likely close to the estimate but may be substantially different."
  },
  {
    "code" : "low",
    "display" : "Low",
    "definition" : "Limited confidence; the true effect may be substantially different."
  },
  {
    "code" : "very-low",
    "display" : "Very low",
    "definition" : "Very little confidence; the true effect is likely substantially different. Not the same as no evidence — that is kind no-recommendation."
  }]
}

```
