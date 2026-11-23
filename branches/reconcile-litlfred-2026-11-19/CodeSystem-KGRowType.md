# Knowledge graph L1: row type - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L1: row type**

## CodeSystem: Knowledge graph L1: row type 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/KGRowType | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGRowType |

 
The role of a row within a table. Source: smart-kg ontology/l1/l1.json valueSets "row-type"; HIV SI guideline Table 2.3; ANC Table 1. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Knowledge graph L1: row type](ValueSet-KGRowTypeVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "KGRowType",
  "url" : "http://smart.who.int/base/CodeSystem/KGRowType",
  "version" : "0.3.0",
  "name" : "KGRowType",
  "title" : "Knowledge graph L1: row type",
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
  "description" : "The role of a row within a table. Source: smart-kg ontology/l1/l1.json valueSets \"row-type\"; HIV SI guideline Table 2.3; ANC Table 1.",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 4,
  "concept" : [{
    "code" : "header",
    "display" : "Header",
    "definition" : "A header row, including repeated headers on later pages."
  },
  {
    "code" : "group",
    "display" : "Group",
    "definition" : "A group heading row such as 'A. Nutritional interventions'."
  },
  {
    "code" : "data",
    "display" : "Data",
    "definition" : "A row carrying content."
  },
  {
    "code" : "note",
    "display" : "Note",
    "definition" : "A note row inside the table."
  }]
}

```
