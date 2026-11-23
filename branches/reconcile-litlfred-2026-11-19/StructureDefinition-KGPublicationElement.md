# Knowledge graph L1: Publication element - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L1: Publication element**

## Logical Model: Knowledge graph L1: Publication element 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGPublicationElement | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGPublicationElement |

 
One printed block: a table, a table row, a footnote, a figure, a chart, an image, a flowchart, a box or a list. It records where something is printed and exactly what is printed that no content node holds. It carries no meaning of its own; meaning lives in content nodes, joined by presentedIn. columns is the header text, verbatim. columnMap names, per column, the content field that fills it when the table is re-rendered (e.g. 'Recommendation' -> statement). cells holds only text no content node holds; a cell filled through columnMap is null. text is for unmodelled printed text such as a footnote that is not a remark. sha256 is for images. Class IRI: http://smart.who.int/kg/publication-element. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGPublicationElement.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGPublicationElement.csv), [Excel](StructureDefinition-KGPublicationElement.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGPublicationElement",
  "url" : "http://smart.who.int/base/StructureDefinition/KGPublicationElement",
  "version" : "0.3.0",
  "name" : "KGPublicationElement",
  "title" : "Knowledge graph L1: Publication element",
  "status" : "active",
  "date" : "2026-11-23T18:43:32+00:00",
  "publisher" : "WHO",
  "contact" : [{
    "name" : "WHO",
    "telecom" : [{
      "system" : "url",
      "value" : "http://who.int"
    }]
  }],
  "description" : "One printed block: a table, a table row, a footnote, a figure, a chart, an image, a flowchart, a box or a list. It records where something is printed and exactly what is printed that no content node holds. It carries no meaning of its own; meaning lives in content nodes, joined by presentedIn. columns is the header text, verbatim. columnMap names, per column, the content field that fills it when the table is re-rendered (e.g. 'Recommendation' -> statement). cells holds only text no content node holds; a cell filled through columnMap is null. text is for unmodelled printed text such as a footnote that is not a remark. sha256 is for images. Class IRI: http://smart.who.int/kg/publication-element.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGPublicationElement",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGPublicationElement",
      "path" : "KGPublicationElement",
      "short" : "Knowledge graph L1: Publication element",
      "definition" : "One printed block: a table, a table row, a footnote, a figure, a chart, an image, a flowchart, a box or a list. It records where something is printed and exactly what is printed that no content node holds. It carries no meaning of its own; meaning lives in content nodes, joined by presentedIn. columns is the header text, verbatim. columnMap names, per column, the content field that fills it when the table is re-rendered (e.g. 'Recommendation' -> statement). cells holds only text no content node holds; a cell filled through columnMap is null. text is for unmodelled printed text such as a footnote that is not a remark. sha256 is for images. Class IRI: http://smart.who.int/kg/publication-element."
    },
    {
      "id" : "KGPublicationElement.elementType",
      "path" : "KGPublicationElement.elementType",
      "short" : "Element type",
      "definition" : "What kind of printed block a publication element is.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://smart.who.int/base/ValueSet/KGElementTypeVS"
      }
    },
    {
      "id" : "KGPublicationElement.label",
      "path" : "KGPublicationElement.label",
      "short" : "Label",
      "definition" : "The element's printed label (\"Table 3\", \"Box 2\").",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGPublicationElement.caption",
      "path" : "KGPublicationElement.caption",
      "short" : "Caption",
      "definition" : "The element's caption, verbatim.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGPublicationElement.pageRange",
      "path" : "KGPublicationElement.pageRange",
      "short" : "Page range",
      "definition" : "Pages the element is printed on.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGPublicationElement.ordinal",
      "path" : "KGPublicationElement.ordinal",
      "short" : "Ordinal",
      "definition" : "Position among its siblings.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "unsignedInt"
      }]
    },
    {
      "id" : "KGPublicationElement.rowType",
      "path" : "KGPublicationElement.rowType",
      "short" : "Row type",
      "definition" : "The role of a row within a table.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://smart.who.int/base/ValueSet/KGRowTypeVS"
      }
    },
    {
      "id" : "KGPublicationElement.columns",
      "path" : "KGPublicationElement.columns",
      "short" : "Columns",
      "definition" : "The header text, verbatim, one per column; a blank header is an empty string.",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGPublicationElement.columnMap",
      "path" : "KGPublicationElement.columnMap",
      "short" : "Column map",
      "definition" : "Per column, the content field that fills it when the table is re-rendered (e.g. 'Recommendation' -> statement).",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "BackboneElement"
      }]
    },
    {
      "id" : "KGPublicationElement.columnMap.column",
      "path" : "KGPublicationElement.columnMap.column",
      "short" : "column",
      "definition" : "The column.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGPublicationElement.columnMap.field",
      "path" : "KGPublicationElement.columnMap.field",
      "short" : "field",
      "definition" : "The field.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGPublicationElement.cells",
      "path" : "KGPublicationElement.cells",
      "short" : "Cells",
      "definition" : "Text no content node holds, per column; a cell filled through columnMap is null.",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGPublicationElement.text",
      "path" : "KGPublicationElement.text",
      "short" : "Text",
      "definition" : "Unmodelled printed text, such as a footnote that is not a remark.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGPublicationElement.sha256",
      "path" : "KGPublicationElement.sha256",
      "short" : "SHA-256",
      "definition" : "Hash of the image, for an image element.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    }]
  }
}

```
