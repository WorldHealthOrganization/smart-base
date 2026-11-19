# Knowledge graph L1: Outcome - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L1: Outcome**

## Logical Model: Knowledge graph L1: Outcome 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGOutcome | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGOutcome |

 
An outcome a guideline group chose to judge a key question by, with its importance in this guideline (handbook §7.6). A node because evidence attaches to it and one list is shared by several questions (ANC Web annex 1). Flat: one node per specific outcome. name as first printed; aliases are the other printed forms (e.g. 'EGWG'); category is the printed group heading (e.g. 'Fetal/newborn morbidity'). Class IRI: http://smart.who.int/kg/outcome. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGOutcome.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGOutcome.csv), [Excel](StructureDefinition-KGOutcome.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGOutcome",
  "url" : "http://smart.who.int/base/StructureDefinition/KGOutcome",
  "version" : "0.3.0",
  "name" : "KGOutcome",
  "title" : "Knowledge graph L1: Outcome",
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
  "description" : "An outcome a guideline group chose to judge a key question by, with its importance in this guideline (handbook §7.6). A node because evidence attaches to it and one list is shared by several questions (ANC Web annex 1). Flat: one node per specific outcome. name as first printed; aliases are the other printed forms (e.g. 'EGWG'); category is the printed group heading (e.g. 'Fetal/newborn morbidity'). Class IRI: http://smart.who.int/kg/outcome.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGOutcome",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGOutcome",
      "path" : "KGOutcome",
      "short" : "Knowledge graph L1: Outcome",
      "definition" : "An outcome a guideline group chose to judge a key question by, with its importance in this guideline (handbook §7.6). A node because evidence attaches to it and one list is shared by several questions (ANC Web annex 1). Flat: one node per specific outcome. name as first printed; aliases are the other printed forms (e.g. 'EGWG'); category is the printed group heading (e.g. 'Fetal/newborn morbidity'). Class IRI: http://smart.who.int/kg/outcome."
    },
    {
      "id" : "KGOutcome.name",
      "path" : "KGOutcome.name",
      "short" : "Name",
      "definition" : "The outcome as first printed.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGOutcome.importance",
      "path" : "KGOutcome.importance",
      "short" : "Importance",
      "definition" : "How the guideline development group rated an outcome on the 1–9 scale: 7–9 critical, 4–6 important.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://smart.who.int/base/ValueSet/KGOutcomeImportanceVS"
      }
    },
    {
      "id" : "KGOutcome.aliases",
      "path" : "KGOutcome.aliases",
      "short" : "Aliases",
      "definition" : "Other printed forms of the outcome (e.g. 'EGWG').",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGOutcome.category",
      "path" : "KGOutcome.category",
      "short" : "Category",
      "definition" : "The printed group heading (e.g. 'Fetal/newborn morbidity').",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    }]
  }
}

```
