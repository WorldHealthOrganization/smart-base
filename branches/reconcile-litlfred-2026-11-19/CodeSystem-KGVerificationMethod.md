# Knowledge graph L2: verification method - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L2: verification method**

## CodeSystem: Knowledge graph L2: verification method 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/KGVerificationMethod | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGVerificationMethod |

 
How a success criterion is verified: the classic verification methods, the same field name and codes as folio-assistant's requirement.ts `successCriteria`, so the two map 1:1. From litlfred/smart-kg main (folio-assistant#2406). Source: smart-kg ontology/l2/l2.json valueSets "verification-method"; folio-assistant-core schemas requirement.ts successCriteria.verification. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Knowledge graph L2: verification method](ValueSet-KGVerificationMethodVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "KGVerificationMethod",
  "url" : "http://smart.who.int/base/CodeSystem/KGVerificationMethod",
  "version" : "0.3.0",
  "name" : "KGVerificationMethod",
  "title" : "Knowledge graph L2: verification method",
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
  "description" : "How a success criterion is verified: the classic verification methods, the same field name and codes as folio-assistant's requirement.ts `successCriteria`, so the two map 1:1. From litlfred/smart-kg main (folio-assistant#2406). Source: smart-kg ontology/l2/l2.json valueSets \"verification-method\"; folio-assistant-core schemas requirement.ts successCriteria.verification.",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 4,
  "concept" : [{
    "code" : "test",
    "display" : "Test",
    "definition" : "Verified by executing a test."
  },
  {
    "code" : "inspection",
    "display" : "Inspection",
    "definition" : "Verified by examining the artefact."
  },
  {
    "code" : "review",
    "display" : "Review",
    "definition" : "Verified by a person's review."
  },
  {
    "code" : "analysis",
    "display" : "Analysis",
    "definition" : "Verified by analysis or calculation."
  }]
}

```
