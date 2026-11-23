# Knowledge graph L1: outcome importance - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L1: outcome importance**

## CodeSystem: Knowledge graph L1: outcome importance 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/KGOutcomeImportance | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGOutcomeImportance |

 
How the guideline development group rated an outcome on the 1–9 scale: 7–9 critical, 4–6 important. Unimportant outcomes are not carried into evidence profiles, so they have no code here. Source: smart-kg ontology/l1/l1.json valueSets "outcome-importance"; WHO handbook for guideline development (2014) §7.6, Fig. 7.1. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Knowledge graph L1: outcome importance](ValueSet-KGOutcomeImportanceVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "KGOutcomeImportance",
  "url" : "http://smart.who.int/base/CodeSystem/KGOutcomeImportance",
  "version" : "0.3.0",
  "name" : "KGOutcomeImportance",
  "title" : "Knowledge graph L1: outcome importance",
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
  "description" : "How the guideline development group rated an outcome on the 1–9 scale: 7–9 critical, 4–6 important. Unimportant outcomes are not carried into evidence profiles, so they have no code here. Source: smart-kg ontology/l1/l1.json valueSets \"outcome-importance\"; WHO handbook for guideline development (2014) §7.6, Fig. 7.1.",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 2,
  "concept" : [{
    "code" : "critical",
    "display" : "Critical",
    "definition" : "Rated 7–9: critical for decision-making. Only critical outcomes determine overall certainty."
  },
  {
    "code" : "important",
    "display" : "Important",
    "definition" : "Rated 4–6: important but not critical for decision-making."
  }]
}

```
