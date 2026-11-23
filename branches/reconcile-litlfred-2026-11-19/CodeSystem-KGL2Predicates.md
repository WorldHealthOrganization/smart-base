# Knowledge graph L2: predicates - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L2: predicates**

## CodeSystem: Knowledge graph L2: predicates 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/KGL2Predicates | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGL2Predicates |

 
The predicates of the L2 layer. An edge's `predicate` is one of these; which (source, target) pairs each licenses is the layer's edge table. Source: smart-base/L1/schemas/L2.ts (migrated from smart-kg ontology/L2/L2.json). 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Knowledge graph L2: predicates](ValueSet-KGL2PredicatesVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "KGL2Predicates",
  "url" : "http://smart.who.int/base/CodeSystem/KGL2Predicates",
  "version" : "0.3.0",
  "name" : "KGL2Predicates",
  "title" : "Knowledge graph L2: predicates",
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
  "description" : "The predicates of the L2 layer. An edge's `predicate` is one of these; which (source, target) pairs each licenses is the layer's edge table. Source: smart-base/L1/schemas/L2.ts (migrated from smart-kg ontology/L2/L2.json).",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 16,
  "concept" : [{
    "code" : "hasComponent",
    "display" : "hasComponent",
    "definition" : "A DAK contains one of its nine components. The qualifier carries the component name from DAK.fsh, so `dak hasComponent persona` and `dak hasComponent program-indicator` stay distinguishable when a query walks the kit."
  },
  {
    "code" : "sourcedFrom",
    "display" : "sourcedFrom",
    "definition" : "A component points at the file that defines it. TWO TARGETS ARE LICENSED, and which one an instance uses says how much is known about the file. Where a subgraph models that file type, the target is the file itself -- `business-process sourcedFrom bpmn-definitions`, licensed in l2-bpmn -- and the graph walks straight on into the file's contents. Where none does (a Gherkin feature, a FHIR canonical, or a BPMN this graph simply does not hold), the target is an l1:external-artifact carrying a URI and nothing else. Prefer the first: routing through external-artifact when the file IS modelled adds a hop through a node that, at instance level, is the same node."
  },
  {
    "code" : "realises",
    "display" : "realises",
    "definition" : "A business process realises a user scenario. From `scenario 0..* id` on BusinessProcessWorkflow -- a bare id string, so an instance carries a resolutionStatus."
  },
  {
    "code" : "involves",
    "display" : "involves",
    "definition" : "A user scenario involves a persona. From `personas 0..* id` on UserScenario -- again bare ids, again a resolutionStatus."
  },
  {
    "code" : "fulfilledBy",
    "display" : "fulfilledBy",
    "definition" : "A functional requirement is fulfilled by a persona. THE ONE JOIN IN THIS LAYER THAT IS NOT STRING MATCHING: the committed instances write `actor[+] = Canonical(SGAuthoring.Persona.BusinessAnalyst)`, a canonical reference that resolves without guessing. It is the counter-example that shows the other joins are a choice, not a necessity."
  },
  {
    "code" : "hasStatement",
    "display" : "hasStatement",
    "definition" : "A requirement carries numbered, labelled statements with a conformance verb. 170 of them exist today."
  },
  {
    "code" : "listsTask",
    "display" : "listsTask",
    "definition" : "BusinessProcessWorkflow declares `task 0..*` with identifier, name and description -- the same tasks the BPMN file draws. Two representations of one list, joined by identifier, which is why dak-task exists as a node rather than a property."
  },
  {
    "code" : "references",
    "display" : "references",
    "definition" : "A program indicator names the health interventions that give it context. From `references 0..* id` on ProgramIndicator -- bare id strings again, so an instance carries a resolutionStatus. Distinct from derivedFrom: referencing an intervention for context is not the same claim as restating a normative indicator."
  },
  {
    "code" : "describes",
    "display" : "describes",
    "definition" : "A DAK-level task entry describes an element of a BPMN file. Declared here and licensed in l2-bpmn, where the target class lives."
  },
  {
    "code" : "usesDataElement",
    "display" : "usesDataElement",
    "definition" : "A DAK task captures or reads a core data element. From the data dictionary's `Activity ID` column, which keys each data element to the activity it is recorded in (`IMMZ.D1.Capture or update client history`), joined to the task by its activity id. The target is the element's id as the dictionary declares it, not a FHIR canonical (owner, 2026-11-18)."
  },
  {
    "code" : "specifiedBy",
    "display" : "specifiedBy",
    "definition" : "A DAK task is specified by a functional requirement. From the requirements workbook's `Activity ID and name` column (`IMMZ.A1.Obtain vaccination location info`), joined by activity id."
  },
  {
    "code" : "invokesDecision",
    "display" : "invokesDecision",
    "definition" : "A DAK task invokes a decision table. From the decision-support workbook's `Trigger` row, which names the activity a decision runs in, and from a BPMN task's calledDecision. Joined by the decision's id (`IMMZ.D2.DT.BCG`), unlike dmn:usingTask, which l2-dmn's invokedBy reads by task name."
  },
  {
    "code" : "implementedBy",
    "display" : "implementedBy",
    "definition" : "Reused from l1, and licensed here for the L1->L2 hop that L1 could not declare itself: l1 cannot name an l2 class without a circular import, but l2 imports l1 and sees both ends. A recommendation is implemented by the DAK component that realises it. Always `inferred`, never `derived` -- deciding that a process realises a recommendation is adaptation, the judgement a DAK exists to record, and it carries a resolutionStatus like every other cross-artefact claim. Note health-intervention has NO implementedBy edge: the published SOP gives Health Interventions an L3 row of `n/a / n/a / n/a` and calls L1 recommendations inputs rather than outputs, so the trace runs through processes, decisions and indicators instead."
  },
  {
    "code" : "derivedFrom",
    "display" : "derivedFrom",
    "definition" : "This normative content restates or operationalises that recommendation."
  },
  {
    "code" : "appearsIn",
    "display" : "appearsIn",
    "definition" : "A citation string appears in an L2 or L3 artefact at a stated location."
  },
  {
    "code" : "verifiedBy",
    "display" : "verifiedBy",
    "definition" : "A requirement statement is verified by a test scenario. The statement is the granularity at which conformance is asserted, so it is also the granularity at which a test is claimed to check it. The edge records the claim that a scenario exists for the statement; whether the scenario actually exercises each success criterion is a review question, recorded per criterion by `verification` on successCriteria, not by this edge."
  }]
}

```
