# Knowledge graph L1: recommendation strength - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L1: recommendation strength**

## CodeSystem: Knowledge graph L1: recommendation strength 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/KGRecommendationStrength | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGRecommendationStrength |

 
GRADE strength. Strength is not certainty: a strong recommendation can rest on low-certainty evidence and a conditional one on high. Record "weak" as conditional; the handbook treats them as synonyms (§10.4). Source: smart-kg ontology/l1/l1.json valueSets "recommendation-strength"; WHO handbook for guideline development (2014) §10.4. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Knowledge graph L1: recommendation strength](ValueSet-KGRecommendationStrengthVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "KGRecommendationStrength",
  "url" : "http://smart.who.int/base/CodeSystem/KGRecommendationStrength",
  "version" : "0.3.0",
  "name" : "KGRecommendationStrength",
  "title" : "Knowledge graph L1: recommendation strength",
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
  "description" : "GRADE strength. Strength is not certainty: a strong recommendation can rest on low-certainty evidence and a conditional one on high. Record \"weak\" as conditional; the handbook treats them as synonyms (§10.4). Source: smart-kg ontology/l1/l1.json valueSets \"recommendation-strength\"; WHO handbook for guideline development (2014) §10.4.",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 2,
  "concept" : [{
    "code" : "strong",
    "display" : "Strong",
    "definition" : "The desirable effects of adherence clearly outweigh the undesirable. Handbook §10.4.1."
  },
  {
    "code" : "conditional",
    "display" : "Conditional",
    "definition" : "Less certain about the balance of benefits and harms; generally states the conditions under which to implement. Also called weak. Handbook §10.4.2."
  }]
}

```
