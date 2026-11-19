# Knowledge graph L1-LIBRARY: Library node - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L1-LIBRARY: Library node**

## Logical Model: Knowledge graph L1-LIBRARY: Library node 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGLibraryNode | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGLibraryNode |

 
A node in the ingested library L1 is read from: a source document, a section or a block, addressed by the library's own IRI. Opaque, as L1 asserts nothing about the library's internal model; the library is upstream, so pointing at it keeps the layering rule. Class IRI: http://smart.who.int/kg/library-node. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGLibraryNode.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGLibraryNode.csv), [Excel](StructureDefinition-KGLibraryNode.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGLibraryNode",
  "url" : "http://smart.who.int/base/StructureDefinition/KGLibraryNode",
  "version" : "0.3.0",
  "name" : "KGLibraryNode",
  "title" : "Knowledge graph L1-LIBRARY: Library node",
  "status" : "active",
  "date" : "2026-11-19T20:24:57+00:00",
  "publisher" : "WHO",
  "contact" : [{
    "name" : "WHO",
    "telecom" : [{
      "system" : "url",
      "value" : "http://who.int"
    }]
  }],
  "description" : "A node in the ingested library L1 is read from: a source document, a section or a block, addressed by the library's own IRI. Opaque, as L1 asserts nothing about the library's internal model; the library is upstream, so pointing at it keeps the layering rule. Class IRI: http://smart.who.int/kg/library-node.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGLibraryNode",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGLibraryNode",
      "path" : "KGLibraryNode",
      "short" : "Knowledge graph L1-LIBRARY: Library node",
      "definition" : "A node in the ingested library L1 is read from: a source document, a section or a block, addressed by the library's own IRI. Opaque, as L1 asserts nothing about the library's internal model; the library is upstream, so pointing at it keeps the layering rule. Class IRI: http://smart.who.int/kg/library-node."
    },
    {
      "id" : "KGLibraryNode.iri",
      "path" : "KGLibraryNode.iri",
      "short" : "IRI",
      "definition" : "The library node's own IRI.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGLibraryNode.libraryClass",
      "path" : "KGLibraryNode.libraryClass",
      "short" : "Library class",
      "definition" : "The library class it is an instance of (cat-harness:SourceDocument, doco:Section, cat-harness:Block, …).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGLibraryNode.entry",
      "path" : "KGLibraryNode.entry",
      "short" : "Entry",
      "definition" : "The library entry it belongs to (e.g. 9789240016514-eng).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGLibraryNode.pageRange",
      "path" : "KGLibraryNode.pageRange",
      "short" : "Page range",
      "definition" : "Physical pages it covers, where it is a section or block.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    }]
  }
}

```
