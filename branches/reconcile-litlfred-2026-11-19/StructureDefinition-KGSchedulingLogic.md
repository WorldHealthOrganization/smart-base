# Knowledge graph L2: Scheduling Logic - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L2: Scheduling Logic**

## Logical Model: Knowledge graph L2: Scheduling Logic 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGSchedulingLogic | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGSchedulingLogic |

 
When an intervention is due, as a DAK component. NOT declared by DAK.fsh – it is added here because the published SOP lists Scheduling Logic as an active L2 input (spreadsheets under input/scheduling-logic), WHO's ArchiMate model declares it a BusinessObject realised by PlanDefinition, and L1's schedules needed an L2 component to reach (since L1 3.0, a recommendation's timing slot). Note that the SOP's own L3 row for scheduling is present but HTML-commented-out and there is no l3_schedulinglogic.md page, so WHO has drafted the mapping and not activated it; the L3 edge is licensed here as a deliberate departure, recorded rather than hidden. resolutionStatus is `unresolved` on a component that something else names but no DAK declares – an L3 artefact whose title carries the component id, for instance. The node exists so the gap is queryable and carries the referenced id and nothing else. Class IRI: http://smart.who.int/kg/scheduling-logic. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGSchedulingLogic.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGSchedulingLogic.csv), [Excel](StructureDefinition-KGSchedulingLogic.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGSchedulingLogic",
  "url" : "http://smart.who.int/base/StructureDefinition/KGSchedulingLogic",
  "version" : "0.3.0",
  "name" : "KGSchedulingLogic",
  "title" : "Knowledge graph L2: Scheduling Logic",
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
  "description" : "When an intervention is due, as a DAK component. NOT declared by DAK.fsh -- it is added here because the published SOP lists Scheduling Logic as an active L2 input (spreadsheets under input/scheduling-logic), WHO's ArchiMate model declares it a BusinessObject realised by PlanDefinition, and L1's schedules needed an L2 component to reach (since L1 3.0, a recommendation's timing slot). Note that the SOP's own L3 row for scheduling is present but HTML-commented-out and there is no l3_schedulinglogic.md page, so WHO has drafted the mapping and not activated it; the L3 edge is licensed here as a deliberate departure, recorded rather than hidden. resolutionStatus is `unresolved` on a component that something else names but no DAK declares -- an L3 artefact whose title carries the component id, for instance. The node exists so the gap is queryable and carries the referenced id and nothing else. Class IRI: http://smart.who.int/kg/scheduling-logic.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGSchedulingLogic",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGSchedulingLogic",
      "path" : "KGSchedulingLogic",
      "short" : "Knowledge graph L2: Scheduling Logic",
      "definition" : "When an intervention is due, as a DAK component. NOT declared by DAK.fsh -- it is added here because the published SOP lists Scheduling Logic as an active L2 input (spreadsheets under input/scheduling-logic), WHO's ArchiMate model declares it a BusinessObject realised by PlanDefinition, and L1's schedules needed an L2 component to reach (since L1 3.0, a recommendation's timing slot). Note that the SOP's own L3 row for scheduling is present but HTML-commented-out and there is no l3_schedulinglogic.md page, so WHO has drafted the mapping and not activated it; the L3 edge is licensed here as a deliberate departure, recorded rather than hidden. resolutionStatus is `unresolved` on a component that something else names but no DAK declares -- an L3 artefact whose title carries the component id, for instance. The node exists so the gap is queryable and carries the referenced id and nothing else. Class IRI: http://smart.who.int/kg/scheduling-logic."
    },
    {
      "id" : "KGSchedulingLogic.id",
      "path" : "KGSchedulingLogic.id",
      "short" : "Id",
      "definition" : "The identifier the source declares (an FSH instance id, a BPMN or DMN element id).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGSchedulingLogic.description",
      "path" : "KGSchedulingLogic.description",
      "short" : "Description",
      "definition" : "A description, as the source gives it.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGSchedulingLogic.sourceKind",
      "path" : "KGSchedulingLogic.sourceKind",
      "short" : "Source kind",
      "definition" : "What kind of artefact the component was read from (an FSH instance, a spreadsheet, a BPMN file).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGSchedulingLogic.source",
      "path" : "KGSchedulingLogic.source",
      "short" : "Source",
      "definition" : "Where the node was read from: a repository path or URL.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGSchedulingLogic.resolutionStatus",
      "path" : "KGSchedulingLogic.resolutionStatus",
      "short" : "Resolution status",
      "definition" : "Whether the component something names was found: `unresolved` when nothing declares it, so the gap is queryable.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://smart.who.int/base/ValueSet/KGResolutionStatusVS"
      }
    }]
  }
}

```
