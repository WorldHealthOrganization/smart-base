# Knowledge graph L1: recommendation kind - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L1: recommendation kind**

## CodeSystem: Knowledge graph L1: recommendation kind 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/KGRecommendationKind | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGRecommendationKind |

 
What sort of normative statement this is. Grading is optional: ANC 2016 prints a direction ('Recommended', 'Not recommended') and no GRADE strength. A strength always needs a direction. A good practice statement and a no-recommendation carry no strength or certainty, and a no-recommendation carries no direction. Source: smart-kg ontology/l1/l1.json valueSets "recommendation-kind"; WHO handbook §10.4, §10.7; ANC guideline (2016) Table 1, verified; Guyatt et al. 2016 on good practice statements. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Knowledge graph L1: recommendation kind](ValueSet-KGRecommendationKindVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "KGRecommendationKind",
  "url" : "http://smart.who.int/base/CodeSystem/KGRecommendationKind",
  "version" : "0.3.0",
  "name" : "KGRecommendationKind",
  "title" : "Knowledge graph L1: recommendation kind",
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
  "description" : "What sort of normative statement this is. Grading is optional: ANC 2016 prints a direction ('Recommended', 'Not recommended') and no GRADE strength. A strength always needs a direction. A good practice statement and a no-recommendation carry no strength or certainty, and a no-recommendation carries no direction. Source: smart-kg ontology/l1/l1.json valueSets \"recommendation-kind\"; WHO handbook §10.4, §10.7; ANC guideline (2016) Table 1, verified; Guyatt et al. 2016 on good practice statements.",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 5,
  "concept" : [{
    "code" : "recommendation",
    "display" : "Recommendation",
    "definition" : "A graded recommendation, with a direction and a strength. Handbook §10.4."
  },
  {
    "code" : "context-specific",
    "display" : "Context specific",
    "definition" : "Recommended only in specified contexts or settings, stated in the recommendation. ANC guideline (2016) Table 1, verified."
  },
  {
    "code" : "research-context",
    "display" : "Research context",
    "definition" : "Recommended only in the context of rigorous research. ANC guideline (2016) Table 1, verified."
  },
  {
    "code" : "good-practice-statement",
    "display" : "Good practice statement",
    "definition" : "An ungraded statement whose benefit is so clear that grading the evidence is not a useful exercise. Carries no strength or certainty. Guyatt et al. 2016."
  },
  {
    "code" : "no-recommendation",
    "display" : "No recommendation",
    "definition" : "\"No recommendation can be made because…\" — the guideline development group decided the evidence could not support one. Handbook §10.7. Distinct from very-low certainty: absent evidence and weak evidence are different findings."
  }]
}

```
