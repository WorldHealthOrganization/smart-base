# Knowledge graph L1: element type - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L1: element type**

## CodeSystem: Knowledge graph L1: element type 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/KGElementType | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGElementType |

 
What kind of printed block a publication element is. Source: smart-kg ontology/l1/l1.json valueSets "element-type"; Observed in the ANC and HIV SI guidelines and the immunization summary tables. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Knowledge graph L1: element type](ValueSet-KGElementTypeVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "KGElementType",
  "url" : "http://smart.who.int/base/CodeSystem/KGElementType",
  "version" : "0.3.0",
  "name" : "KGElementType",
  "title" : "Knowledge graph L1: element type",
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
  "description" : "What kind of printed block a publication element is. Source: smart-kg ontology/l1/l1.json valueSets \"element-type\"; Observed in the ANC and HIV SI guidelines and the immunization summary tables.",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 9,
  "concept" : [{
    "code" : "table",
    "display" : "Table",
    "definition" : "A table, with columns and rows."
  },
  {
    "code" : "table-row",
    "display" : "Table row",
    "definition" : "One row of a table."
  },
  {
    "code" : "footnote",
    "display" : "Footnote",
    "definition" : "A footnote attached to a row or a block."
  },
  {
    "code" : "figure",
    "display" : "Figure",
    "definition" : "A figure."
  },
  {
    "code" : "chart",
    "display" : "Chart",
    "definition" : "A chart; its data stays with its source."
  },
  {
    "code" : "image",
    "display" : "Image",
    "definition" : "An image."
  },
  {
    "code" : "flowchart",
    "display" : "Flowchart",
    "definition" : "A flowchart or algorithm; its steps are modelled at L2, not here."
  },
  {
    "code" : "box",
    "display" : "Box",
    "definition" : "A boxed panel."
  },
  {
    "code" : "list",
    "display" : "List",
    "definition" : "A list set apart on the page."
  }]
}

```
