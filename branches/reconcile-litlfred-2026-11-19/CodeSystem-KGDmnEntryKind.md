# Knowledge graph L2-DMN: dmn entry kind - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L2-DMN: dmn entry kind**

## CodeSystem: Knowledge graph L2-DMN: dmn entry kind 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/KGDmnEntryKind | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGDmnEntryKind |

 
Which DMN element type a column's cells are serialised as. Added by the smart-base migration from smart-kg's propertyNote, which named the two values in prose. Source: smart-kg ontology/l2-dmn/l2-dmn.json valueSets "dmn-entry-kind"; OMG DMN 1.3, DecisionRule.outputEntry and annotationEntry. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Knowledge graph L2-DMN: dmn entry kind](ValueSet-KGDmnEntryKindVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "KGDmnEntryKind",
  "url" : "http://smart.who.int/base/CodeSystem/KGDmnEntryKind",
  "version" : "0.3.0",
  "name" : "KGDmnEntryKind",
  "title" : "Knowledge graph L2-DMN: dmn entry kind",
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
  "description" : "Which DMN element type a column's cells are serialised as. Added by the smart-base migration from smart-kg's propertyNote, which named the two values in prose. Source: smart-kg ontology/l2-dmn/l2-dmn.json valueSets \"dmn-entry-kind\"; OMG DMN 1.3, DecisionRule.outputEntry and annotationEntry.",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 2,
  "concept" : [{
    "code" : "outputEntry",
    "display" : "OutputEntry",
    "definition" : "The column's cells are the rule's outputEntry elements."
  },
  {
    "code" : "annotationEntry",
    "display" : "AnnotationEntry",
    "definition" : "The column's cells are the rule's annotationEntry elements."
  }]
}

```
