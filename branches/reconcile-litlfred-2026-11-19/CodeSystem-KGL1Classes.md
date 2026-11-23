# Knowledge graph L1: classes - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L1: classes**

## CodeSystem: Knowledge graph L1: classes 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/KGL1Classes | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGL1Classes |

 
The classes of the L1 layer of the SMART Guidelines knowledge graph. A node's `type` is one of these. Source: smart-base/L1/schemas/L1.ts (migrated from smart-kg ontology/L1/L1.json). 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Knowledge graph L1: classes](ValueSet-KGL1ClassesVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "KGL1Classes",
  "url" : "http://smart.who.int/base/CodeSystem/KGL1Classes",
  "version" : "0.3.0",
  "name" : "KGL1Classes",
  "title" : "Knowledge graph L1: classes",
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
  "description" : "The classes of the L1 layer of the SMART Guidelines knowledge graph. A node's `type` is one of these. Source: smart-base/L1/schemas/L1.ts (migrated from smart-kg ontology/L1/L1.json).",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 13,
  "concept" : [{
    "code" : "publication",
    "display" : "Publication",
    "definition" : "A WHO publication: a guideline of any of the handbook's types, a position paper, a summary table, a classification, implementation guidance, or a supplement. Metadata follows Dublin Core."
  },
  {
    "code" : "publication-section",
    "display" : "Publication section",
    "definition" : "A chapter, annex or numbered section, at any depth."
  },
  {
    "code" : "publication-element",
    "display" : "Publication element",
    "definition" : "One printed block: a table, a table row, a footnote, a figure, a chart, an image, a flowchart, a box or a list. It records where something is printed and exactly what is printed that no content node holds. It carries no meaning of its own; meaning lives in content nodes, joined by presentedIn."
  },
  {
    "code" : "recommendation",
    "display" : "Recommendation",
    "definition" : "A normative statement from a WHO guideline. Kinds other than a graded recommendation (context-specific, research-only, good practice statement, no-recommendation) are the same node with a different kind."
  },
  {
    "code" : "remark",
    "display" : "Remark",
    "definition" : "A remark attached to a recommendation (handbook §10.6). May also be printed as a table footnote."
  },
  {
    "code" : "key-question",
    "display" : "Key question",
    "definition" : "A question in PICO format, framed before the evidence search (handbook §7.1–7.4). P and C are verbatim text with codes through crossReferences; I is also joined to a catalogued intervention; O is the outcome node."
  },
  {
    "code" : "outcome",
    "display" : "Outcome",
    "definition" : "An outcome a guideline group chose to judge a key question by, with its importance in this guideline (handbook §7.6). A node because evidence attaches to it and one list is shared by several questions (ANC Web annex 1). Flat: one node per specific outcome."
  },
  {
    "code" : "evidence",
    "display" : "Evidence",
    "definition" : "One row of an evidence profile: the evidence for one outcome of one key question, with its certainty (handbook §9.2)."
  },
  {
    "code" : "health-intervention",
    "display" : "Health intervention",
    "definition" : "An intervention identified in a WHO catalogue or classification (UHC Compendium, ICHI, CDHI), digital interventions included. A peer of recommendation, not a recommendation. A DAK may draw on both."
  },
  {
    "code" : "indicator",
    "display" : "Indicator",
    "definition" : "A WHO indicator, identified by its published reference number. Printed in several places (HIV SI 2022: summary list, Table 2.3, reference sheet) and stored once."
  },
  {
    "code" : "citation",
    "display" : "Citation",
    "definition" : "One citation string exactly as written in a DAK artefact. A cell holding several citations yields several nodes. Content-addressed in the DAK's namespace, so one string is one node across artefacts."
  },
  {
    "code" : "reference-entry",
    "display" : "Reference entry",
    "definition" : "One row of a DAK artefact's own reference list: '(1)' and the full bibliographic text and URL it stands for. Resolved once; every citation numbered to it shares the result."
  },
  {
    "code" : "terminology-code",
    "display" : "Terminology code",
    "definition" : "A code in an external terminology — ICD-10, ICD-11, SNOMED CT, ATC, or a WHO classification such as CDHI. CROSS-REFERENCE ONLY. It records system, code and display, and asserts NOTHING about the terminology: no hierarchy, no subsumption, no synonyms, no post-coordination. The terminology has its own authority, its own release cycle and its own tooling, and a partial copy here would be wrong within one release. Resolve meaning against the terminology server, not against this graph."
  }]
}

```
