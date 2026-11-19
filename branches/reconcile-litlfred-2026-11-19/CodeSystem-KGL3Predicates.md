# Knowledge graph L3: predicates - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L3: predicates**

## CodeSystem: Knowledge graph L3: predicates 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/KGL3Predicates | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGL3Predicates |

 
The predicates of the L3 layer. An edge's `predicate` is one of these; which (source, target) pairs each licenses is the layer's edge table. Source: smart-base/L1/schemas/L3.ts (migrated from smart-kg ontology/L3/L3.json). 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Knowledge graph L3: predicates](ValueSet-KGL3PredicatesVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "KGL3Predicates",
  "url" : "http://smart.who.int/base/CodeSystem/KGL3Predicates",
  "version" : "0.3.0",
  "name" : "KGL3Predicates",
  "title" : "Knowledge graph L3: predicates",
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
  "description" : "The predicates of the L3 layer. An edge's `predicate` is one of these; which (source, target) pairs each licenses is the layer's edge table. Source: smart-base/L1/schemas/L3.ts (migrated from smart-kg ontology/L3/L3.json).",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 3,
  "concept" : [{
    "code" : "implementedBy",
    "display" : "implementedBy",
    "definition" : "An L2 component is implemented by a FHIR artefact. Reused from l1 and licensed here per (component, resource) pair transcribed from the published mapping table. ALWAYS `inferred`, never `derived`: with no back-pointer extension in the estate, the join is a naming convention or a canonical reference, and every instance records which rule matched and a resolutionStatus. The optional `targetPath` property on an instance names the element reached (e.g. `PlanDefinition.action[2]`) so traceability can be element-level without this layer modelling FHIR internals as nodes."
  },
  {
    "code" : "citesSource",
    "display" : "citesSource",
    "definition" : "A FHIR artefact cites an L1 source through `relatedArtifact[type = #citation]`. The target is an l1:citation minted from the same string by tools/extract-citations.mjs, so L3 and L1 join without either extractor knowing about the other -- the same mechanism l2-dmn uses from a decision rule."
  },
  {
    "code" : "uses",
    "display" : "uses",
    "definition" : "One FHIR artefact references another by canonical: a PlanDefinition its Library, an action its ActivityDefinition, a Questionnaire its StructureMap, a Measure its Library. These are real canonical references rather than conventions, so unlike implementedBy they are `derived` when read straight from the field."
  }]
}

```
