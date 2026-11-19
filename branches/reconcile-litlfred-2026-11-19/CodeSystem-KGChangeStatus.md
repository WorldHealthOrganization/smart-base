# Knowledge graph L1: change status - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L1: change status**

## CodeSystem: Knowledge graph L1: change status 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/KGChangeStatus | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGChangeStatus |

 
Whether this edition of a consolidated guideline introduces, updates or carries a recommendation or indicator unchanged. Printed as NEW / UPDATE tags. Source: smart-kg ontology/l1/l1.json valueSets "change-status"; Consolidated guidelines on person-centred HIV strategic information (2022), summary recommendations; handbook §1.7.2. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Knowledge graph L1: change status](ValueSet-KGChangeStatusVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "KGChangeStatus",
  "url" : "http://smart.who.int/base/CodeSystem/KGChangeStatus",
  "version" : "0.3.0",
  "name" : "KGChangeStatus",
  "title" : "Knowledge graph L1: change status",
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
  "description" : "Whether this edition of a consolidated guideline introduces, updates or carries a recommendation or indicator unchanged. Printed as NEW / UPDATE tags. Source: smart-kg ontology/l1/l1.json valueSets \"change-status\"; Consolidated guidelines on person-centred HIV strategic information (2022), summary recommendations; handbook §1.7.2.",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 3,
  "concept" : [{
    "code" : "new",
    "display" : "New",
    "definition" : "Introduced in this edition."
  },
  {
    "code" : "updated",
    "display" : "Updated",
    "definition" : "Changed in this edition."
  },
  {
    "code" : "unchanged",
    "display" : "Unchanged",
    "definition" : "Carried from an earlier edition without change."
  }]
}

```
