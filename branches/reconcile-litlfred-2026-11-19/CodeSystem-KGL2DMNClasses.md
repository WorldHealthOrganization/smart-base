# Knowledge graph L2DMN: classes - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L2DMN: classes**

## CodeSystem: Knowledge graph L2DMN: classes 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/KGL2DMNClasses | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGL2DMNClasses |

 
The classes of the L2DMN layer of the SMART Guidelines knowledge graph. A node's `type` is one of these. Source: smart-base/L1/schemas/L2-DMN.ts (migrated from smart-kg ontology/L2-DMN/L2-DMN.json). 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Knowledge graph L2DMN: classes](ValueSet-KGL2DMNClassesVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "KGL2DMNClasses",
  "url" : "http://smart.who.int/base/CodeSystem/KGL2DMNClasses",
  "version" : "0.3.0",
  "name" : "KGL2DMNClasses",
  "title" : "Knowledge graph L2DMN: classes",
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
  "description" : "The classes of the L2DMN layer of the SMART Guidelines knowledge graph. A node's `type` is one of these. Source: smart-base/L1/schemas/L2-DMN.ts (migrated from smart-kg ontology/L2-DMN/L2-DMN.json).",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 6,
  "concept" : [{
    "code" : "dmn-definitions",
    "display" : "DMN File",
    "definition" : "One DMN file as a unit -- the `dmn:definitions` root. Shares its IRI with the l1:external-artifact for the same file, so the l2:decision-support-logic component that points at it and this subgraph name one resource."
  },
  {
    "code" : "dmn-decision",
    "display" : "DMN Decision",
    "definition" : "A `dmn:decision` -- the question being answered, and the node that carries the link back to the BPMN task invoking it. A file may hold several; the BCG file holds one."
  },
  {
    "code" : "dmn-decision-table",
    "display" : "DMN Decision Table",
    "definition" : "The table realising a decision. Separate from dmn-decision because DMN permits other expression kinds -- a literal expression, an invocation -- and collapsing the two would make the graph unable to say which was used."
  },
  {
    "code" : "dmn-input-clause",
    "display" : "DMN Input Clause",
    "definition" : "An input column. Its expression text is where data element names are embedded, which is the only reason this is a node rather than a property of the table."
  },
  {
    "code" : "dmn-output-clause",
    "display" : "DMN Output Clause",
    "definition" : "An output column. The BCG table's four are Care Plan, Guidance displayed to health worker, Annotations and Reference(s). These are column DEFINITIONS in a decision table, not clinical records: no edge from this class reaches an execution artefact, and none may."
  },
  {
    "code" : "dmn-rule",
    "display" : "DMN Rule",
    "definition" : "One row. Its input and output cells are carried as properties, not nodes: 250 of them in the BCG table alone, none the target of a cross-model edge. What the rule needs a node for is its citation edge into L1."
  }]
}

```
