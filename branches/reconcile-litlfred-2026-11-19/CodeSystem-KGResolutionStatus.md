# Knowledge graph L1: resolution status - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L1: resolution status**

## CodeSystem: Knowledge graph L1: resolution status 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/KGResolutionStatus | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGResolutionStatus |

 
Whether a citation string has been matched to what it cites. `ambiguous` is a legitimate terminal state — two publications with similar titles is a question for a person — and must not be collapsed to resolved. Source: smart-kg ontology/l1/l1.json valueSets "resolution-status"; docs/SCOPE.md. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Knowledge graph L1: resolution status](ValueSet-KGResolutionStatusVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "KGResolutionStatus",
  "url" : "http://smart.who.int/base/CodeSystem/KGResolutionStatus",
  "version" : "0.3.0",
  "name" : "KGResolutionStatus",
  "title" : "Knowledge graph L1: resolution status",
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
  "description" : "Whether a citation string has been matched to what it cites. `ambiguous` is a legitimate terminal state — two publications with similar titles is a question for a person — and must not be collapsed to resolved. Source: smart-kg ontology/l1/l1.json valueSets \"resolution-status\"; docs/SCOPE.md.",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 3,
  "concept" : [{
    "code" : "unresolved",
    "display" : "Unresolved",
    "definition" : "Not yet matched."
  },
  {
    "code" : "resolved",
    "display" : "Resolved",
    "definition" : "Matched; a resolvesTo edge says to what."
  },
  {
    "code" : "ambiguous",
    "display" : "Ambiguous",
    "definition" : "More than one candidate, and choosing is a judgement for a person."
  }]
}

```
