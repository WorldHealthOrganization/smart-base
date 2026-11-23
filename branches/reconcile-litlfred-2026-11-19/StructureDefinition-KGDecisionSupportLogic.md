# Knowledge graph L2: Decision-Support Logic - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L2: Decision-Support Logic**

## Logical Model: Knowledge graph L2: Decision-Support Logic 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGDecisionSupportLogic | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGDecisionSupportLogic |

 
DAK component 6. The whole model is an id, an optional description and `source 1..1 uri` to a DMN file. Nothing about the decision itself – which is the gap the l2-dmn subgraph fills. resolutionStatus is `unresolved` on a component that something else names but no DAK declares – an L3 artefact whose title carries the component id, for instance. The node exists so the gap is queryable and carries the referenced id and nothing else. Class IRI: http://smart.who.int/kg/decision-support-logic. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGDecisionSupportLogic.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGDecisionSupportLogic.csv), [Excel](StructureDefinition-KGDecisionSupportLogic.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGDecisionSupportLogic",
  "url" : "http://smart.who.int/base/StructureDefinition/KGDecisionSupportLogic",
  "version" : "0.3.0",
  "name" : "KGDecisionSupportLogic",
  "title" : "Knowledge graph L2: Decision-Support Logic",
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
  "description" : "DAK component 6. The whole model is an id, an optional description and `source 1..1 uri` to a DMN file. Nothing about the decision itself -- which is the gap the l2-dmn subgraph fills. resolutionStatus is `unresolved` on a component that something else names but no DAK declares -- an L3 artefact whose title carries the component id, for instance. The node exists so the gap is queryable and carries the referenced id and nothing else. Class IRI: http://smart.who.int/kg/decision-support-logic.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGDecisionSupportLogic",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGDecisionSupportLogic",
      "path" : "KGDecisionSupportLogic",
      "short" : "Knowledge graph L2: Decision-Support Logic",
      "definition" : "DAK component 6. The whole model is an id, an optional description and `source 1..1 uri` to a DMN file. Nothing about the decision itself -- which is the gap the l2-dmn subgraph fills. resolutionStatus is `unresolved` on a component that something else names but no DAK declares -- an L3 artefact whose title carries the component id, for instance. The node exists so the gap is queryable and carries the referenced id and nothing else. Class IRI: http://smart.who.int/kg/decision-support-logic."
    },
    {
      "id" : "KGDecisionSupportLogic.id",
      "path" : "KGDecisionSupportLogic.id",
      "short" : "Id",
      "definition" : "The identifier the source declares (an FSH instance id, a BPMN or DMN element id).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDecisionSupportLogic.description",
      "path" : "KGDecisionSupportLogic.description",
      "short" : "Description",
      "definition" : "A description, as the source gives it.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGDecisionSupportLogic.sourceKind",
      "path" : "KGDecisionSupportLogic.sourceKind",
      "short" : "Source kind",
      "definition" : "What kind of artefact the component was read from (an FSH instance, a spreadsheet, a BPMN file).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDecisionSupportLogic.source",
      "path" : "KGDecisionSupportLogic.source",
      "short" : "Source",
      "definition" : "Where the node was read from: a repository path or URL.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDecisionSupportLogic.resolutionStatus",
      "path" : "KGDecisionSupportLogic.resolutionStatus",
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
