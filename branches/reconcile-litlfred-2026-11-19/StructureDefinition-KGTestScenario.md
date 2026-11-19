# Knowledge graph L2: Test Scenario - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L2: Test Scenario**

## Logical Model: Knowledge graph L2: Test Scenario 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGTestScenario | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGTestScenario |

 
DAK component 9. `feature 1..1 uri` to a Gherkin feature file, plus an optional description. The feature file's interior is not modelled: no DAK in this estate ships one yet, so a subgraph for it would have no instance to check it against. resolutionStatus is `unresolved` on a component that something else names but no DAK declares – an L3 artefact whose title carries the component id, for instance. The node exists so the gap is queryable and carries the referenced id and nothing else. Class IRI: http://smart.who.int/kg/test-scenario. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGTestScenario.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGTestScenario.csv), [Excel](StructureDefinition-KGTestScenario.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGTestScenario",
  "url" : "http://smart.who.int/base/StructureDefinition/KGTestScenario",
  "version" : "0.3.0",
  "name" : "KGTestScenario",
  "title" : "Knowledge graph L2: Test Scenario",
  "status" : "active",
  "date" : "2026-11-19T20:24:57+00:00",
  "publisher" : "WHO",
  "contact" : [{
    "name" : "WHO",
    "telecom" : [{
      "system" : "url",
      "value" : "http://who.int"
    }]
  }],
  "description" : "DAK component 9. `feature 1..1 uri` to a Gherkin feature file, plus an optional description. The feature file's interior is not modelled: no DAK in this estate ships one yet, so a subgraph for it would have no instance to check it against. resolutionStatus is `unresolved` on a component that something else names but no DAK declares -- an L3 artefact whose title carries the component id, for instance. The node exists so the gap is queryable and carries the referenced id and nothing else. Class IRI: http://smart.who.int/kg/test-scenario.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGTestScenario",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGTestScenario",
      "path" : "KGTestScenario",
      "short" : "Knowledge graph L2: Test Scenario",
      "definition" : "DAK component 9. `feature 1..1 uri` to a Gherkin feature file, plus an optional description. The feature file's interior is not modelled: no DAK in this estate ships one yet, so a subgraph for it would have no instance to check it against. resolutionStatus is `unresolved` on a component that something else names but no DAK declares -- an L3 artefact whose title carries the component id, for instance. The node exists so the gap is queryable and carries the referenced id and nothing else. Class IRI: http://smart.who.int/kg/test-scenario."
    },
    {
      "id" : "KGTestScenario.id",
      "path" : "KGTestScenario.id",
      "short" : "Id",
      "definition" : "The identifier the source declares (an FSH instance id, a BPMN or DMN element id).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGTestScenario.feature",
      "path" : "KGTestScenario.feature",
      "short" : "Feature",
      "definition" : "The Gherkin feature file the scenario is in.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGTestScenario.description",
      "path" : "KGTestScenario.description",
      "short" : "Description",
      "definition" : "A description, as the source gives it.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGTestScenario.sourceKind",
      "path" : "KGTestScenario.sourceKind",
      "short" : "Source kind",
      "definition" : "What kind of artefact the component was read from (an FSH instance, a spreadsheet, a BPMN file).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGTestScenario.source",
      "path" : "KGTestScenario.source",
      "short" : "Source",
      "definition" : "Where the node was read from: a repository path or URL.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGTestScenario.resolutionStatus",
      "path" : "KGTestScenario.resolutionStatus",
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
