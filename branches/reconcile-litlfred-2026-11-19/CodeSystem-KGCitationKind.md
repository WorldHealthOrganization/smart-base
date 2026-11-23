# Knowledge graph L1: citation kind - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L1: citation kind**

## CodeSystem: Knowledge graph L1: citation kind 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/KGCitationKind | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGCitationKind |

 
Whether a citation string names a source, or stands in for one that is missing. Source: smart-kg ontology/l1/l1.json valueSets "citation-kind"; IMMZ DAK indicators workbook: '[Add appropriate reference]'. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Knowledge graph L1: citation kind](ValueSet-KGCitationKindVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "KGCitationKind",
  "url" : "http://smart.who.int/base/CodeSystem/KGCitationKind",
  "version" : "0.3.0",
  "name" : "KGCitationKind",
  "title" : "Knowledge graph L1: citation kind",
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
  "description" : "Whether a citation string names a source, or stands in for one that is missing. Source: smart-kg ontology/l1/l1.json valueSets \"citation-kind\"; IMMZ DAK indicators workbook: '[Add appropriate reference]'.",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 2,
  "concept" : [{
    "code" : "reference",
    "display" : "Reference",
    "definition" : "Names a source."
  },
  {
    "code" : "placeholder",
    "display" : "Placeholder",
    "definition" : "The author's marker that a source is still to be added. Never resolves; counted as a coverage gap."
  }]
}

```
