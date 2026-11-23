# Knowledge graph L2: Functional Requirement - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L2: Functional Requirement**

## Logical Model: Knowledge graph L2: Functional Requirement 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGFunctionalRequirement | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGFunctionalRequirement |

 
DAK component 8, first half. The as-a/I-want/so-that shape: `activity`, `capability[x]`, `benefit[x]`, and `actor 0..* Reference(SGActor)`. The 41 committed instances use the R5 SGRequirements profile rather than this logical model, so a real instance carries `statement` entries and a userstory extension; both shapes are accommodated and `profile` records which was read. resolutionStatus is `unresolved` on a component that something else names but no DAK declares – an L3 artefact whose title carries the component id, for instance. The node exists so the gap is queryable and carries the referenced id and nothing else. Class IRI: http://smart.who.int/kg/functional-requirement. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGFunctionalRequirement.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGFunctionalRequirement.csv), [Excel](StructureDefinition-KGFunctionalRequirement.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGFunctionalRequirement",
  "url" : "http://smart.who.int/base/StructureDefinition/KGFunctionalRequirement",
  "version" : "0.3.0",
  "name" : "KGFunctionalRequirement",
  "title" : "Knowledge graph L2: Functional Requirement",
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
  "description" : "DAK component 8, first half. The as-a/I-want/so-that shape: `activity`, `capability[x]`, `benefit[x]`, and `actor 0..* Reference(SGActor)`. The 41 committed instances use the R5 SGRequirements profile rather than this logical model, so a real instance carries `statement` entries and a userstory extension; both shapes are accommodated and `profile` records which was read. resolutionStatus is `unresolved` on a component that something else names but no DAK declares -- an L3 artefact whose title carries the component id, for instance. The node exists so the gap is queryable and carries the referenced id and nothing else. Class IRI: http://smart.who.int/kg/functional-requirement.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGFunctionalRequirement",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGFunctionalRequirement",
      "path" : "KGFunctionalRequirement",
      "short" : "Knowledge graph L2: Functional Requirement",
      "definition" : "DAK component 8, first half. The as-a/I-want/so-that shape: `activity`, `capability[x]`, `benefit[x]`, and `actor 0..* Reference(SGActor)`. The 41 committed instances use the R5 SGRequirements profile rather than this logical model, so a real instance carries `statement` entries and a userstory extension; both shapes are accommodated and `profile` records which was read. resolutionStatus is `unresolved` on a component that something else names but no DAK declares -- an L3 artefact whose title carries the component id, for instance. The node exists so the gap is queryable and carries the referenced id and nothing else. Class IRI: http://smart.who.int/kg/functional-requirement."
    },
    {
      "id" : "KGFunctionalRequirement.id",
      "path" : "KGFunctionalRequirement.id",
      "short" : "Id",
      "definition" : "The identifier the source declares (an FSH instance id, a BPMN or DMN element id).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGFunctionalRequirement.activity",
      "path" : "KGFunctionalRequirement.activity",
      "short" : "Activity",
      "definition" : "The activity the requirement supports.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGFunctionalRequirement.capability",
      "path" : "KGFunctionalRequirement.capability",
      "short" : "Capability",
      "definition" : "The capability required (\"As a … I want …\").",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGFunctionalRequirement.benefit",
      "path" : "KGFunctionalRequirement.benefit",
      "short" : "Benefit",
      "definition" : "The benefit (\"so that …\").",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGFunctionalRequirement.classification",
      "path" : "KGFunctionalRequirement.classification",
      "short" : "Classification",
      "definition" : "The classification, as declared.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGFunctionalRequirement.title",
      "path" : "KGFunctionalRequirement.title",
      "short" : "Title",
      "definition" : "The human-readable title.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGFunctionalRequirement.description",
      "path" : "KGFunctionalRequirement.description",
      "short" : "Description",
      "definition" : "A description, as the source gives it.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGFunctionalRequirement.profile",
      "path" : "KGFunctionalRequirement.profile",
      "short" : "Profile",
      "definition" : "A profile canonical the artefact declares (meta.profile or the requirement's profile).",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGFunctionalRequirement.sourceKind",
      "path" : "KGFunctionalRequirement.sourceKind",
      "short" : "Source kind",
      "definition" : "What kind of artefact the component was read from (an FSH instance, a spreadsheet, a BPMN file).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGFunctionalRequirement.source",
      "path" : "KGFunctionalRequirement.source",
      "short" : "Source",
      "definition" : "Where the node was read from: a repository path or URL.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGFunctionalRequirement.resolutionStatus",
      "path" : "KGFunctionalRequirement.resolutionStatus",
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
