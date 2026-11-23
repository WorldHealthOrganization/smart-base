# Knowledge graph L2: Program Indicator - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L2: Program Indicator**

## Logical Model: Knowledge graph L2: Program Indicator 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGProgramIndicator | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGProgramIndicator |

 
DAK component 7. Named program-indicator and not `indicator` because L1 already declares an `indicator` – one normatively defined in a publication. They are different things: this is the DAK's operational measure, and `derivedFrom` is how it points at the normative one. Collapsing them would silently merge a WHO definition with a country's implementation of it. numerator, denominator and disaggregation are all `1..1 markdown` – prose, not a computable expression. Nothing here should be read as a calculable measure; the L3 FHIR Measure is where that would live. resolutionStatus is `unresolved` on a component that something else names but no DAK declares – an L3 artefact whose title carries the component id, for instance. The node exists so the gap is queryable and carries the referenced id and nothing else. Class IRI: http://smart.who.int/kg/program-indicator. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGProgramIndicator.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGProgramIndicator.csv), [Excel](StructureDefinition-KGProgramIndicator.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGProgramIndicator",
  "url" : "http://smart.who.int/base/StructureDefinition/KGProgramIndicator",
  "version" : "0.3.0",
  "name" : "KGProgramIndicator",
  "title" : "Knowledge graph L2: Program Indicator",
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
  "description" : "DAK component 7. Named program-indicator and not `indicator` because L1 already declares an `indicator` -- one normatively defined in a publication. They are different things: this is the DAK's operational measure, and `derivedFrom` is how it points at the normative one. Collapsing them would silently merge a WHO definition with a country's implementation of it. numerator, denominator and disaggregation are all `1..1 markdown` -- prose, not a computable expression. Nothing here should be read as a calculable measure; the L3 FHIR Measure is where that would live. resolutionStatus is `unresolved` on a component that something else names but no DAK declares -- an L3 artefact whose title carries the component id, for instance. The node exists so the gap is queryable and carries the referenced id and nothing else. Class IRI: http://smart.who.int/kg/program-indicator.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGProgramIndicator",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGProgramIndicator",
      "path" : "KGProgramIndicator",
      "short" : "Knowledge graph L2: Program Indicator",
      "definition" : "DAK component 7. Named program-indicator and not `indicator` because L1 already declares an `indicator` -- one normatively defined in a publication. They are different things: this is the DAK's operational measure, and `derivedFrom` is how it points at the normative one. Collapsing them would silently merge a WHO definition with a country's implementation of it. numerator, denominator and disaggregation are all `1..1 markdown` -- prose, not a computable expression. Nothing here should be read as a calculable measure; the L3 FHIR Measure is where that would live. resolutionStatus is `unresolved` on a component that something else names but no DAK declares -- an L3 artefact whose title carries the component id, for instance. The node exists so the gap is queryable and carries the referenced id and nothing else. Class IRI: http://smart.who.int/kg/program-indicator."
    },
    {
      "id" : "KGProgramIndicator.id",
      "path" : "KGProgramIndicator.id",
      "short" : "Id",
      "definition" : "The identifier the source declares (an FSH instance id, a BPMN or DMN element id).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGProgramIndicator.name",
      "path" : "KGProgramIndicator.name",
      "short" : "Name",
      "definition" : "The computable name: the CamelCase identifier a Canonical() reference matches on.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGProgramIndicator.definition",
      "path" : "KGProgramIndicator.definition",
      "short" : "Definition",
      "definition" : "The definition, as the source gives it.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGProgramIndicator.numerator",
      "path" : "KGProgramIndicator.numerator",
      "short" : "Numerator",
      "definition" : "The numerator, in prose: not a computable expression.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGProgramIndicator.denominator",
      "path" : "KGProgramIndicator.denominator",
      "short" : "Denominator",
      "definition" : "The denominator, in prose: not a computable expression.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGProgramIndicator.disaggregation",
      "path" : "KGProgramIndicator.disaggregation",
      "short" : "Disaggregation",
      "definition" : "How the indicator is disaggregated, in prose.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGProgramIndicator.description",
      "path" : "KGProgramIndicator.description",
      "short" : "Description",
      "definition" : "A description, as the source gives it.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGProgramIndicator.sourceKind",
      "path" : "KGProgramIndicator.sourceKind",
      "short" : "Source kind",
      "definition" : "What kind of artefact the component was read from (an FSH instance, a spreadsheet, a BPMN file).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGProgramIndicator.source",
      "path" : "KGProgramIndicator.source",
      "short" : "Source",
      "definition" : "Where the node was read from: a repository path or URL.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGProgramIndicator.resolutionStatus",
      "path" : "KGProgramIndicator.resolutionStatus",
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
