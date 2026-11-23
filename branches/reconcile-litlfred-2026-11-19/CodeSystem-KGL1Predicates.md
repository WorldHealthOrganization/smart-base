# Knowledge graph L1: predicates - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L1: predicates**

## CodeSystem: Knowledge graph L1: predicates 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/KGL1Predicates | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGL1Predicates |

 
The predicates of the L1 layer. An edge's `predicate` is one of these; which (source, target) pairs each licenses is the layer's edge table. Source: smart-base/L1/schemas/L1.ts (migrated from smart-kg ontology/L1/L1.json). 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Knowledge graph L1: predicates](ValueSet-KGL1PredicatesVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "KGL1Predicates",
  "url" : "http://smart.who.int/base/CodeSystem/KGL1Predicates",
  "version" : "0.3.0",
  "name" : "KGL1Predicates",
  "title" : "Knowledge graph L1: predicates",
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
  "description" : "The predicates of the L1 layer. An edge's `predicate` is one of these; which (source, target) pairs each licenses is the layer's edge table. Source: smart-base/L1/schemas/L1.ts (migrated from smart-kg ontology/L1/L1.json).",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 21,
  "concept" : [{
    "code" : "contains",
    "display" : "contains",
    "definition" : "Layout containment only: publication, sections, elements. It never points at content."
  },
  {
    "code" : "hasSupplement",
    "display" : "hasSupplement",
    "definition" : "A guideline to its web annex or supplementary document (handbook §12.1)."
  },
  {
    "code" : "supersedes",
    "display" : "supersedes",
    "definition" : "This replaces that, between publications and between individual recommendations (handbook §1.7.2, §12.5; ANC Table 1 footnotes)."
  },
  {
    "code" : "refines",
    "display" : "refines",
    "definition" : "A recommendation narrows or conditions another."
  },
  {
    "code" : "partOf",
    "display" : "partOf",
    "definition" : "A sub-recommendation a), b) to its parent. Each part carries its own change status (HIV SI 2022)."
  },
  {
    "code" : "definedIn",
    "display" : "definedIn",
    "definition" : "The one publication that issued this content: its authority."
  },
  {
    "code" : "presentedIn",
    "display" : "presentedIn",
    "definition" : "A place this content is printed, in any publication. Many per node. Restatement is presentedIn into a publication other than definedIn. The edge carries renderedText only when the printed wording differs from the stored text."
  },
  {
    "code" : "answers",
    "display" : "answers",
    "definition" : "A recommendation answers a key question. Many-to-many (handbook §7.4)."
  },
  {
    "code" : "addresses",
    "display" : "addresses",
    "definition" : "A row of an evidence profile addresses a key question."
  },
  {
    "code" : "hasOutcome",
    "display" : "hasOutcome",
    "definition" : "A key question names an outcome. A list shared by several questions is one set of outcome nodes."
  },
  {
    "code" : "forOutcome",
    "display" : "forOutcome",
    "definition" : "An evidence row grades one outcome. Optional: qualitative evidence may concern a criterion such as values."
  },
  {
    "code" : "aboutIntervention",
    "display" : "aboutIntervention",
    "definition" : "The I of a key question, joined to a catalogued intervention."
  },
  {
    "code" : "supportedBy",
    "display" : "supportedBy",
    "definition" : "A recommendation to the evidence it rests on."
  },
  {
    "code" : "hasRemark",
    "display" : "hasRemark",
    "definition" : "A recommendation to a remark: definition, implementation, precaution, contraindication, subgroup, research gap or training."
  },
  {
    "code" : "recommends",
    "display" : "recommends",
    "definition" : "A recommendation concerns a catalogued intervention. Optional: only when the mapping is known."
  },
  {
    "code" : "measures",
    "display" : "measures",
    "definition" : "What an indicator counts: a catalogued intervention, or adherence to a recommendation (handbook Table 10.2)."
  },
  {
    "code" : "justifiedBy",
    "display" : "justifiedBy",
    "definition" : "Why an indicator exists: the recommendation its rationale cites (HIV SI 2022, PRV.3)."
  },
  {
    "code" : "crossReferences",
    "display" : "crossReferences",
    "definition" : "Names an external code. Records that a code was cited, never what it means. Terminology is a leaf."
  },
  {
    "code" : "classifiedAs",
    "display" : "classifiedAs",
    "definition" : "Placement of a catalogued intervention in UHC, ICHI or CDHI."
  },
  {
    "code" : "numberedAs",
    "display" : "numberedAs",
    "definition" : "A citation's '(n)' to row n of the same artefact's reference list. Mechanical."
  },
  {
    "code" : "resolvesTo",
    "display" : "resolvesTo",
    "definition" : "What a citation or reference entry refers to, as precisely as the string allows. Matching is a judgement: inferred, or decided when a person chose between candidates."
  }]
}

```
