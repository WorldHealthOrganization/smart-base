# Knowledge graph L1: Key question - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L1: Key question**

## Logical Model: Knowledge graph L1: Key question 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGKeyQuestion | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGKeyQuestion |

 
A question in PICO format, framed before the evidence search (handbook §7.1–7.4). P and C are verbatim text with codes through crossReferences; I is also joined to a catalogued intervention; O is the outcome node. Class IRI: http://smart.who.int/kg/key-question. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGKeyQuestion.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGKeyQuestion.csv), [Excel](StructureDefinition-KGKeyQuestion.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGKeyQuestion",
  "url" : "http://smart.who.int/base/StructureDefinition/KGKeyQuestion",
  "version" : "0.3.0",
  "name" : "KGKeyQuestion",
  "title" : "Knowledge graph L1: Key question",
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
  "description" : "A question in PICO format, framed before the evidence search (handbook §7.1–7.4). P and C are verbatim text with codes through crossReferences; I is also joined to a catalogued intervention; O is the outcome node. Class IRI: http://smart.who.int/kg/key-question.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGKeyQuestion",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGKeyQuestion",
      "path" : "KGKeyQuestion",
      "short" : "Knowledge graph L1: Key question",
      "definition" : "A question in PICO format, framed before the evidence search (handbook §7.1–7.4). P and C are verbatim text with codes through crossReferences; I is also joined to a catalogued intervention; O is the outcome node. Class IRI: http://smart.who.int/kg/key-question."
    },
    {
      "id" : "KGKeyQuestion.identifier",
      "path" : "KGKeyQuestion.identifier",
      "short" : "Identifier",
      "definition" : "The question's published number.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGKeyQuestion.text",
      "path" : "KGKeyQuestion.text",
      "short" : "Text",
      "definition" : "The question, verbatim.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGKeyQuestion.population",
      "path" : "KGKeyQuestion.population",
      "short" : "Population",
      "definition" : "P, verbatim.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGKeyQuestion.intervention",
      "path" : "KGKeyQuestion.intervention",
      "short" : "Intervention",
      "definition" : "I, verbatim.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGKeyQuestion.comparator",
      "path" : "KGKeyQuestion.comparator",
      "short" : "Comparator",
      "definition" : "C, verbatim.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGKeyQuestion.setting",
      "path" : "KGKeyQuestion.setting",
      "short" : "Setting",
      "definition" : "Setting, verbatim.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGKeyQuestion.contentHash",
      "path" : "KGKeyQuestion.contentHash",
      "short" : "Content hash",
      "definition" : "sha256 of the normalised text.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    }]
  }
}

```
