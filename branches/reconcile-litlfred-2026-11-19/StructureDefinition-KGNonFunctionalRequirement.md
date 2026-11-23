# Knowledge graph L2: Non-Functional Requirement - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L2: Non-Functional Requirement**

## Logical Model: Knowledge graph L2: Non-Functional Requirement 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGNonFunctionalRequirement | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGNonFunctionalRequirement |

 
DAK component 8, second half. `requirement 1..1 markdown`, an optional category and classification codings. Kept separate from the functional half because the fields genuinely differ – a non-functional requirement has no actor and no benefit. resolutionStatus is `unresolved` on a component that something else names but no DAK declares – an L3 artefact whose title carries the component id, for instance. The node exists so the gap is queryable and carries the referenced id and nothing else. Class IRI: http://smart.who.int/kg/non-functional-requirement. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGNonFunctionalRequirement.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGNonFunctionalRequirement.csv), [Excel](StructureDefinition-KGNonFunctionalRequirement.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGNonFunctionalRequirement",
  "url" : "http://smart.who.int/base/StructureDefinition/KGNonFunctionalRequirement",
  "version" : "0.3.0",
  "name" : "KGNonFunctionalRequirement",
  "title" : "Knowledge graph L2: Non-Functional Requirement",
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
  "description" : "DAK component 8, second half. `requirement 1..1 markdown`, an optional category and classification codings. Kept separate from the functional half because the fields genuinely differ -- a non-functional requirement has no actor and no benefit. resolutionStatus is `unresolved` on a component that something else names but no DAK declares -- an L3 artefact whose title carries the component id, for instance. The node exists so the gap is queryable and carries the referenced id and nothing else. Class IRI: http://smart.who.int/kg/non-functional-requirement.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGNonFunctionalRequirement",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGNonFunctionalRequirement",
      "path" : "KGNonFunctionalRequirement",
      "short" : "Knowledge graph L2: Non-Functional Requirement",
      "definition" : "DAK component 8, second half. `requirement 1..1 markdown`, an optional category and classification codings. Kept separate from the functional half because the fields genuinely differ -- a non-functional requirement has no actor and no benefit. resolutionStatus is `unresolved` on a component that something else names but no DAK declares -- an L3 artefact whose title carries the component id, for instance. The node exists so the gap is queryable and carries the referenced id and nothing else. Class IRI: http://smart.who.int/kg/non-functional-requirement."
    },
    {
      "id" : "KGNonFunctionalRequirement.id",
      "path" : "KGNonFunctionalRequirement.id",
      "short" : "Id",
      "definition" : "The identifier the source declares (an FSH instance id, a BPMN or DMN element id).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGNonFunctionalRequirement.requirement",
      "path" : "KGNonFunctionalRequirement.requirement",
      "short" : "Requirement",
      "definition" : "The requirement text.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGNonFunctionalRequirement.category",
      "path" : "KGNonFunctionalRequirement.category",
      "short" : "Category",
      "definition" : "The category, as declared.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGNonFunctionalRequirement.classification",
      "path" : "KGNonFunctionalRequirement.classification",
      "short" : "Classification",
      "definition" : "The classification, as declared.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGNonFunctionalRequirement.title",
      "path" : "KGNonFunctionalRequirement.title",
      "short" : "Title",
      "definition" : "The human-readable title.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGNonFunctionalRequirement.description",
      "path" : "KGNonFunctionalRequirement.description",
      "short" : "Description",
      "definition" : "A description, as the source gives it.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGNonFunctionalRequirement.profile",
      "path" : "KGNonFunctionalRequirement.profile",
      "short" : "Profile",
      "definition" : "A profile canonical the artefact declares (meta.profile or the requirement's profile).",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGNonFunctionalRequirement.sourceKind",
      "path" : "KGNonFunctionalRequirement.sourceKind",
      "short" : "Source kind",
      "definition" : "What kind of artefact the component was read from (an FSH instance, a spreadsheet, a BPMN file).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGNonFunctionalRequirement.source",
      "path" : "KGNonFunctionalRequirement.source",
      "short" : "Source",
      "definition" : "Where the node was read from: a repository path or URL.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGNonFunctionalRequirement.resolutionStatus",
      "path" : "KGNonFunctionalRequirement.resolutionStatus",
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
