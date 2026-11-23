# Knowledge graph L3: classes - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L3: classes**

## CodeSystem: Knowledge graph L3: classes 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/KGL3Classes | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGL3Classes |

 
The classes of the L3 layer of the SMART Guidelines knowledge graph. A node's `type` is one of these. Source: smart-base/L1/schemas/L3.ts (migrated from smart-kg ontology/L3/L3.json). 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Knowledge graph L3: classes](ValueSet-KGL3ClassesVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "KGL3Classes",
  "url" : "http://smart.who.int/base/CodeSystem/KGL3Classes",
  "version" : "0.3.0",
  "name" : "KGL3Classes",
  "title" : "Knowledge graph L3: classes",
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
  "description" : "The classes of the L3 layer of the SMART Guidelines knowledge graph. A node's `type` is one of these. Source: smart-base/L1/schemas/L3.ts (migrated from smart-kg ontology/L3/L3.json).",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 14,
  "concept" : [{
    "code" : "plan-definition",
    "display" : "Plan Definition",
    "definition" : "A FHIR PlanDefinition. The published mapping gives it two sources -- Processes and Decision Tables -- so a PlanDefinition alone does not say which it came from; the implementedBy edge does. 138 in the immunizations IG, all declaring cpg-recommendationdefinition, all decision tables. Shares its IRI with the l1:external-artifact for the same canonical."
  },
  {
    "code" : "activity-definition",
    "display" : "Activity Definition",
    "definition" : "A FHIR ActivityDefinition -- the concrete act a plan's action invokes. Reached from a PlanDefinition action's `definitionCanonical`, which is a real reference rather than a convention. 3 in the immunizations IG: two cpg-immunizationactivity, one cpg-communicationactivity."
  },
  {
    "code" : "library",
    "display" : "Library",
    "definition" : "A FHIR Library -- the resource that carries CQL. Indexed by canonical and status only. Its CONTENTS are deliberately out of scope: a future l3-cql subgraph will elaborate this same IRI, exactly as l2-bpmn elaborates a BPMN file. 279 in the immunizations IG, joined to their PlanDefinition by the `{id}Logic` suffix."
  },
  {
    "code" : "cql-library",
    "display" : "CQL File",
    "definition" : "A .cql file on disk, as opposed to the FHIR Library resource that wraps it. A node so that the mapping table's four CQL rows -- CQL Concepts and CQL Data Elements under Elements, CQL under Decision Tables, CQL IndicatorLogic under Indicators -- do not dead-end. It carries a name, a path and a hash and NOTHING about the logic: no expressions, no comment tags, no data requirements. 279 in the immunizations IG. The l3-cql subgraph is where that content belongs, and it is not built yet."
  },
  {
    "code" : "measure",
    "display" : "Measure",
    "definition" : "A FHIR Measure -- an indicator made computable. 41 in the immunizations IG, all declaring proportion-measure-cqfm; the SOP makes the profile depend on scoring type, which is why the profile is read rather than assumed. Joined to its L2 indicator by id convention (IMMZ.IND.08 -> IMMZIND08)."
  },
  {
    "code" : "questionnaire",
    "display" : "Questionnaire",
    "definition" : "A FHIR Questionnaire -- a data-collection form over a logical model. 10 in the immunizations IG. Its `sdc-questionnaire-targetStructureMap` extension names the StructureMap that extracts it, which is a real canonical reference. The SOP states no linkId convention and none exists in the estate, so no edge is licensed on linkId."
  },
  {
    "code" : "structure-map",
    "display" : "Structure Map",
    "definition" : "A FHIR StructureMap. The SOP requires them in threes -- QuestionnaireResponse to logical model, logical model to resource, and a grouping map -- so a count that is not a multiple of three is worth a look. 16 .fml files in the immunizations IG."
  },
  {
    "code" : "structure-definition",
    "display" : "Logical Model",
    "definition" : "A StructureDefinition with kind `logical` -- one data dictionary tab as a data structure. Distinct from `profile`, which constrains a FHIR resource: WHO's ArchiMate model has Logical Model realising Data Object while Profile realises Data Element, and the two are not interchangeable. 15 in the immunizations IG."
  },
  {
    "code" : "profile",
    "display" : "Profile",
    "definition" : "A StructureDefinition constraining a FHIR resource. Separate from structure-definition for the reason above. 5 in the immunizations IG. Its internals -- differentials, element definitions, bindings -- are the clearest case of what this layer refuses to re-represent."
  },
  {
    "code" : "value-set",
    "display" : "Value Set",
    "definition" : "A FHIR ValueSet. 192 in the immunizations IG -- the most numerous artefact of all. Indexed by canonical; its expansion, its compose rules and the codes it contains are terminology, which docs/SCOPE.md keeps at arm's length as firmly here as at L1."
  },
  {
    "code" : "code-system",
    "display" : "Code System",
    "definition" : "A FHIR CodeSystem. The SOP says each guideline defines one guideline-level code system holding a concept for every data dictionary element -- which is what makes `code[WHO] = IMMZ.DE9` on a logical model element resolvable. 6 in the immunizations IG. The codes themselves are not copied here."
  },
  {
    "code" : "concept-map",
    "display" : "Concept Map",
    "definition" : "A FHIR ConceptMap -- one per target code system in the dictionary's terminology mappings. 8 in the immunizations IG. Records that a mapping exists; the mappings themselves belong to terminology."
  },
  {
    "code" : "actor-definition",
    "display" : "Actor Definition",
    "definition" : "A FHIR ActorDefinition -- an L2 persona made a FHIR resource. ZERO in the immunizations IG and 22 in smart-base, which is itself worth a coverage query. The SOP names no profile for it and says one is not currently possible because SUSHI cannot profile an R5 resource in an R4 IG, and it tells authors not to assign an identifier -- so expect a bare resource and do not infer more."
  },
  {
    "code" : "requirements",
    "display" : "Requirements",
    "definition" : "A FHIR Requirements resource. The ONE place the published SOP names an SG profile -- SGRequirements -- and the grain is one resource per business process holding many statements, not one per requirement. ZERO in the immunizations IG and 41 in smart-base."
  }]
}

```
