# Knowledge graph L2: classes - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L2: classes**

## CodeSystem: Knowledge graph L2: classes 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/KGL2Classes | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGL2Classes |

 
The classes of the L2 layer of the SMART Guidelines knowledge graph. A node's `type` is one of these. Source: smart-base/L1/schemas/L2.ts (migrated from smart-kg ontology/L2/L2.json). 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Knowledge graph L2: classes](ValueSet-KGL2ClassesVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "KGL2Classes",
  "url" : "http://smart.who.int/base/CodeSystem/KGL2Classes",
  "version" : "0.3.0",
  "name" : "KGL2Classes",
  "title" : "Knowledge graph L2: classes",
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
  "description" : "The classes of the L2 layer of the SMART Guidelines knowledge graph. A node's `type` is one of these. Source: smart-base/L1/schemas/L2.ts (migrated from smart-kg ontology/L2/L2.json).",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 14,
  "concept" : [{
    "code" : "dak",
    "display" : "Digital Adaptation Kit",
    "definition" : "The kit itself. Properties are exactly the metadata fields DAK.fsh declares and dak.json carries -- no more, so that a dak node can be produced from a real file without anything being invented."
  },
  {
    "code" : "persona",
    "display" : "Generic Persona",
    "definition" : "DAK component 2. Grounded in GenericPersona.fsh -- title, id, description, otherNames, iscoCode bound to ISCO08ValueSet -- and in the 22 committed ActorDefinition instances that carry name, title, type and description. The two disagree about where ISCO lives, which the properties record rather than smooth over."
  },
  {
    "code" : "user-scenario",
    "display" : "User Scenario",
    "definition" : "DAK component 3. A narrative describing how personas interact. Carries `personas 0..* id`, which is the only structured link between the narrative layer and the personas it names."
  },
  {
    "code" : "business-process",
    "display" : "Business Process Workflow",
    "definition" : "DAK component 4. NOT the BPMN file -- the component that points at one. `source 1..1 uri` is that pointer, and the BPMN's interior is the l2-bpmn subgraph, reached through the external-artifact this sourcedFrom targets."
  },
  {
    "code" : "dak-task",
    "display" : "Task Entry",
    "definition" : "One task of a DAK business process, as the DAK document's \"notes and annotations\" describe it: identifier, name, description, and the personas, data elements, requirements and decision tables it links to. A node rather than a property because the same task is also drawn in the BPMN file, and the two have to be joinable to be checkable against each other (`describes`). Read from a BPMN file's `dak-task-annotations/v1` sidecar (smart-base/L2-bpmn/schemas/task-annotations.ts); BusinessProcessWorkflow's `task 0..*` backbone carries the first three fields of the same thing."
  },
  {
    "code" : "data-element",
    "display" : "Core Data Element",
    "definition" : "DAK component 5. CoreDataElement.fsh calls itself \"the ONE EXCEPTION to allowing FHIR R4 models into the DAK LMs\": `type` is one of valueset | codesystem | conceptmap | logicalmodel and `canonical 1..1 uri` points at it. The canonical is recorded; nothing inside it is copied, because FHIR is its own query layer."
  },
  {
    "code" : "decision-support-logic",
    "display" : "Decision-Support Logic",
    "definition" : "DAK component 6. The whole model is an id, an optional description and `source 1..1 uri` to a DMN file. Nothing about the decision itself -- which is the gap the l2-dmn subgraph fills."
  },
  {
    "code" : "scheduling-logic",
    "display" : "Scheduling Logic",
    "definition" : "When an intervention is due, as a DAK component. NOT declared by DAK.fsh -- it is added here because the published SOP lists Scheduling Logic as an active L2 input (spreadsheets under input/scheduling-logic), WHO's ArchiMate model declares it a BusinessObject realised by PlanDefinition, and L1's schedules needed an L2 component to reach (since L1 3.0, a recommendation's timing slot). Note that the SOP's own L3 row for scheduling is present but HTML-commented-out and there is no l3_schedulinglogic.md page, so WHO has drafted the mapping and not activated it; the L3 edge is licensed here as a deliberate departure, recorded rather than hidden."
  },
  {
    "code" : "program-indicator",
    "display" : "Program Indicator",
    "definition" : "DAK component 7. Named program-indicator and not `indicator` because L1 already declares an `indicator` -- one normatively defined in a publication. They are different things: this is the DAK's operational measure, and `derivedFrom` is how it points at the normative one. Collapsing them would silently merge a WHO definition with a country's implementation of it."
  },
  {
    "code" : "functional-requirement",
    "display" : "Functional Requirement",
    "definition" : "DAK component 8, first half. The as-a/I-want/so-that shape: `activity`, `capability[x]`, `benefit[x]`, and `actor 0..* Reference(SGActor)`. The 41 committed instances use the R5 SGRequirements profile rather than this logical model, so a real instance carries `statement` entries and a userstory extension; both shapes are accommodated and `profile` records which was read."
  },
  {
    "code" : "non-functional-requirement",
    "display" : "Non-Functional Requirement",
    "definition" : "DAK component 8, second half. `requirement 1..1 markdown`, an optional category and classification codings. Kept separate from the functional half because the fields genuinely differ -- a non-functional requirement has no actor and no benefit."
  },
  {
    "code" : "requirement-statement",
    "display" : "Requirement Statement",
    "definition" : "One numbered, labelled statement inside a requirement, with a conformance verb. A node rather than a property because conformance is queried across a whole DAK -- 'every SHALL in this kit, and what fulfils it' is the question requirements exist to answer. It also carries its own success criteria, so 'what would show this SHALL is met' is answerable per statement rather than per requirement."
  },
  {
    "code" : "test-scenario",
    "display" : "Test Scenario",
    "definition" : "DAK component 9. `feature 1..1 uri` to a Gherkin feature file, plus an optional description. The feature file's interior is not modelled: no DAK in this estate ships one yet, so a subgraph for it would have no instance to check it against."
  },
  {
    "code" : "external-artifact",
    "display" : "External artefact",
    "definition" : "A DAK file addressed by canonical URL: a BPMN process, a DMN decision table, a FHIR resource, a workbook. Deliberately opaque: it carries an IRI and a kind, and nothing about its interior. The L2-BPMN, L2-DMN and L3 classes that describe a file's interior elaborate this class at the same IRI. Moved here from L1 in 3.0 unchanged: a DAK file is the DAK's material, not WHO content."
  }]
}

```
