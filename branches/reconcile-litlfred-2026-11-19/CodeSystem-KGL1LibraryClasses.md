# Knowledge graph L1Library: classes - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L1Library: classes**

## CodeSystem: Knowledge graph L1Library: classes 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/KGL1LibraryClasses | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGL1LibraryClasses |

 
The classes of the L1Library layer of the SMART Guidelines knowledge graph. A node's `type` is one of these. Source: smart-base/L1/schemas/l1-library.ts (migrated from smart-kg ontology/l1-library/l1-library.json). 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Knowledge graph L1Library: classes](ValueSet-KGL1LibraryClassesVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "KGL1LibraryClasses",
  "url" : "http://smart.who.int/base/CodeSystem/KGL1LibraryClasses",
  "version" : "0.3.0",
  "name" : "KGL1LibraryClasses",
  "title" : "Knowledge graph L1Library: classes",
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
  "description" : "The classes of the L1Library layer of the SMART Guidelines knowledge graph. A node's `type` is one of these. Source: smart-base/L1/schemas/l1-library.ts (migrated from smart-kg ontology/l1-library/l1-library.json).",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 2,
  "concept" : [{
    "code" : "implementation-practice",
    "display" : "Implementation practice",
    "definition" : "A statement of how to put guidance into practice, printed in a publication whose publicationType is implementation-guidance or methodology: the handbook's \"products that are not guidelines\" (§1.9), a \"how to\" document that makes no recommendations of its own. Not a recommendation, and not a good practice statement — both are made by a guideline and approved by the GRC; this is neither. It carries no kind, direction, strength or certainty, because nothing graded it. A handbook's own \"Best practices\" lists are the typical source. Owner ruling 1b, 2026-10-12: model these as their own class, not as recommendation nodes of a new kind."
  },
  {
    "code" : "library-node",
    "display" : "Library node",
    "definition" : "A node in the ingested library L1 is read from: a source document, a section or a block, addressed by the library's own IRI. Opaque, as L1 asserts nothing about the library's internal model; the library is upstream, so pointing at it keeps the layering rule."
  }]
}

```
