# Knowledge graph L1: recommendation status - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L1: recommendation status**

## CodeSystem: Knowledge graph L1: recommendation status 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/KGRecommendationStatus | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGRecommendationStatus |

 
Whether a recommendation is still in force. Recommendations in one guideline go out of date at different times (§1.7.2), and a department that doubts a recommendation's validity should say so before the update is done (§12.5.4). This is what impact analysis filters on. Source: smart-kg ontology/l1/l1.json valueSets "recommendation-status"; WHO handbook for guideline development (2014) §1.7.2, §12.5. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Knowledge graph L1: recommendation status](ValueSet-KGRecommendationStatusVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "KGRecommendationStatus",
  "url" : "http://smart.who.int/base/CodeSystem/KGRecommendationStatus",
  "version" : "0.3.0",
  "name" : "KGRecommendationStatus",
  "title" : "Knowledge graph L1: recommendation status",
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
  "description" : "Whether a recommendation is still in force. Recommendations in one guideline go out of date at different times (§1.7.2), and a department that doubts a recommendation's validity should say so before the update is done (§12.5.4). This is what impact analysis filters on. Source: smart-kg ontology/l1/l1.json valueSets \"recommendation-status\"; WHO handbook for guideline development (2014) §1.7.2, §12.5.",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 4,
  "concept" : [{
    "code" : "current",
    "display" : "Current",
    "definition" : "In force."
  },
  {
    "code" : "under-review",
    "display" : "Under review",
    "definition" : "Flagged as possibly out of date, with an update planned. Handbook §12.5.4."
  },
  {
    "code" : "superseded",
    "display" : "Superseded",
    "definition" : "Replaced by another recommendation, reached by supersedes."
  },
  {
    "code" : "withdrawn",
    "display" : "Withdrawn",
    "definition" : "Withdrawn without replacement."
  }]
}

```
