# Knowledge graph L1: Recommendation - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L1: Recommendation**

## Logical Model: Knowledge graph L1: Recommendation 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGRecommendation | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGRecommendation |

 
A normative statement from a WHO guideline. Kinds other than a graded recommendation (context-specific, research-only, good practice statement, no-recommendation) are the same node with a different kind. statement is verbatim and is the only stored copy. intervention, population, setting, provider and timing are verbatim slots taken from the statement, its remarks, or the enclosing caption or heading. setting absorbs the former conditionality. identifier is the published number (e.g. A.1.1), used in the IRI; sub-recommendations append their letter. Class IRI: http://smart.who.int/kg/recommendation. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGRecommendation.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGRecommendation.csv), [Excel](StructureDefinition-KGRecommendation.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGRecommendation",
  "url" : "http://smart.who.int/base/StructureDefinition/KGRecommendation",
  "version" : "0.3.0",
  "name" : "KGRecommendation",
  "title" : "Knowledge graph L1: Recommendation",
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
  "description" : "A normative statement from a WHO guideline. Kinds other than a graded recommendation (context-specific, research-only, good practice statement, no-recommendation) are the same node with a different kind. statement is verbatim and is the only stored copy. intervention, population, setting, provider and timing are verbatim slots taken from the statement, its remarks, or the enclosing caption or heading. setting absorbs the former conditionality. identifier is the published number (e.g. A.1.1), used in the IRI; sub-recommendations append their letter. Class IRI: http://smart.who.int/kg/recommendation.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGRecommendation",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGRecommendation",
      "path" : "KGRecommendation",
      "short" : "Knowledge graph L1: Recommendation",
      "definition" : "A normative statement from a WHO guideline. Kinds other than a graded recommendation (context-specific, research-only, good practice statement, no-recommendation) are the same node with a different kind. statement is verbatim and is the only stored copy. intervention, population, setting, provider and timing are verbatim slots taken from the statement, its remarks, or the enclosing caption or heading. setting absorbs the former conditionality. identifier is the published number (e.g. A.1.1), used in the IRI; sub-recommendations append their letter. Class IRI: http://smart.who.int/kg/recommendation."
    },
    {
      "id" : "KGRecommendation.identifier",
      "path" : "KGRecommendation.identifier",
      "short" : "Identifier",
      "definition" : "The published number (e.g. A.1.1); sub-recommendations append their letter.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGRecommendation.statement",
      "path" : "KGRecommendation.statement",
      "short" : "Statement",
      "definition" : "The recommendation, VERBATIM; the only stored copy.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGRecommendation.kind",
      "path" : "KGRecommendation.kind",
      "short" : "Kind",
      "definition" : "What sort of normative statement this is.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://smart.who.int/base/ValueSet/KGRecommendationKindVS"
      }
    },
    {
      "id" : "KGRecommendation.direction",
      "path" : "KGRecommendation.direction",
      "short" : "Direction",
      "definition" : "For or against.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://smart.who.int/base/ValueSet/KGRecommendationDirectionVS"
      }
    },
    {
      "id" : "KGRecommendation.strength",
      "path" : "KGRecommendation.strength",
      "short" : "Strength",
      "definition" : "GRADE strength.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://smart.who.int/base/ValueSet/KGRecommendationStrengthVS"
      }
    },
    {
      "id" : "KGRecommendation.overallCertainty",
      "path" : "KGRecommendation.overallCertainty",
      "short" : "Overall certainty",
      "definition" : "GRADE certainty of evidence.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://smart.who.int/base/ValueSet/KGCertaintyVS"
      }
    },
    {
      "id" : "KGRecommendation.justification",
      "path" : "KGRecommendation.justification",
      "short" : "Justification",
      "definition" : "The printed justification, verbatim.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGRecommendation.status",
      "path" : "KGRecommendation.status",
      "short" : "Status",
      "definition" : "Whether a recommendation is still in force.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://smart.who.int/base/ValueSet/KGRecommendationStatusVS"
      }
    },
    {
      "id" : "KGRecommendation.changeStatus",
      "path" : "KGRecommendation.changeStatus",
      "short" : "Change status",
      "definition" : "Whether this edition of a consolidated guideline introduces, updates or carries a recommendation or indicator unchanged.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://smart.who.int/base/ValueSet/KGChangeStatusVS"
      }
    },
    {
      "id" : "KGRecommendation.intervention",
      "path" : "KGRecommendation.intervention",
      "short" : "Intervention",
      "definition" : "Verbatim slot: the intervention, quoted from the statement, a remark, caption or heading.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGRecommendation.interventionType",
      "path" : "KGRecommendation.interventionType",
      "short" : "Intervention type",
      "definition" : "DRAFT.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://smart.who.int/base/ValueSet/KGInterventionTypeVS"
      }
    },
    {
      "id" : "KGRecommendation.population",
      "path" : "KGRecommendation.population",
      "short" : "Population",
      "definition" : "Verbatim slot: the population.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGRecommendation.setting",
      "path" : "KGRecommendation.setting",
      "short" : "Setting",
      "definition" : "Verbatim slot: the setting (absorbs the former conditionality).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGRecommendation.provider",
      "path" : "KGRecommendation.provider",
      "short" : "Provider",
      "definition" : "Verbatim slot: who provides it.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGRecommendation.timing",
      "path" : "KGRecommendation.timing",
      "short" : "Timing",
      "definition" : "Verbatim slot: when.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGRecommendation.contentHash",
      "path" : "KGRecommendation.contentHash",
      "short" : "Content hash",
      "definition" : "sha256 of the normalised statement; unchanged on re-extraction means current.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    }]
  }
}

```
