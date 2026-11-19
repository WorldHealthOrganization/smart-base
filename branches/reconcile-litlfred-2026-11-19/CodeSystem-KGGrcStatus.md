# Knowledge graph L1: grc status - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L1: grc status**

## CodeSystem: Knowledge graph L1: grc status 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/KGGrcStatus | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGGrcStatus |

 
Whether the Guideline Review Committee approved the publication. All WHO publications containing recommendations must be approved (handbook §1.10.1); a consolidated guideline whose recommendations were all previously approved and unchanged does not require review (§1.7.2). Absent means not recorded — not the same as not reviewed. Source: smart-kg ontology/l1/l1.json valueSets "grc-status"; WHO handbook for guideline development (2014), §1.7.2, §1.10.1. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Knowledge graph L1: grc status](ValueSet-KGGrcStatusVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "KGGrcStatus",
  "url" : "http://smart.who.int/base/CodeSystem/KGGrcStatus",
  "version" : "0.3.0",
  "name" : "KGGrcStatus",
  "title" : "Knowledge graph L1: grc status",
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
  "description" : "Whether the Guideline Review Committee approved the publication. All WHO publications containing recommendations must be approved (handbook §1.10.1); a consolidated guideline whose recommendations were all previously approved and unchanged does not require review (§1.7.2). Absent means not recorded — not the same as not reviewed. Source: smart-kg ontology/l1/l1.json valueSets \"grc-status\"; WHO handbook for guideline development (2014), §1.7.2, §1.10.1.",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 3,
  "concept" : [{
    "code" : "approved",
    "display" : "Approved",
    "definition" : "Approved by the GRC."
  },
  {
    "code" : "not-required",
    "display" : "Not required",
    "definition" : "GRC review was not required — a §1.9 product, or a consolidation of previously approved, unchanged recommendations."
  },
  {
    "code" : "not-reviewed",
    "display" : "Not reviewed",
    "definition" : "Contains recommendations and was not reviewed by the GRC — including those published before the GRC was established in 2007, which the handbook says should be updated (§12.5.2)."
  }]
}

```
