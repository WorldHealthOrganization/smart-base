# Knowledge graph L1: evidence type - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L1: evidence type**

## CodeSystem: Knowledge graph L1: evidence type 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/KGEvidenceType | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGEvidenceType |

 
Which kind of evidence a row is, and so which scale its certainty is on: GRADE for effects, GRADE-CERQual for qualitative findings. Source: smart-kg ontology/l1/l1.json valueSets "evidence-type"; ANC guideline (2016) methods (GRADE and GRADE-CERQual). 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Knowledge graph L1: evidence type](ValueSet-KGEvidenceTypeVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "KGEvidenceType",
  "url" : "http://smart.who.int/base/CodeSystem/KGEvidenceType",
  "version" : "0.3.0",
  "name" : "KGEvidenceType",
  "title" : "Knowledge graph L1: evidence type",
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
  "description" : "Which kind of evidence a row is, and so which scale its certainty is on: GRADE for effects, GRADE-CERQual for qualitative findings. Source: smart-kg ontology/l1/l1.json valueSets \"evidence-type\"; ANC guideline (2016) methods (GRADE and GRADE-CERQual).",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 4,
  "concept" : [{
    "code" : "effect",
    "display" : "Effect",
    "definition" : "Quantitative effect estimate; certainty is GRADE."
  },
  {
    "code" : "qualitative",
    "display" : "Qualitative",
    "definition" : "Qualitative finding; certainty is GRADE-CERQual confidence."
  },
  {
    "code" : "resource-use",
    "display" : "Resource use",
    "definition" : "Costs or resource requirements."
  },
  {
    "code" : "other",
    "display" : "Other",
    "definition" : "Any other kind."
  }]
}

```
