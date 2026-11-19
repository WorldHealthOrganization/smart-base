# Knowledge graph L1: terminology system - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L1: terminology system**

## CodeSystem: Knowledge graph L1: terminology system 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/KGTerminologySystem | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGTerminologySystem |

 
Code systems a DAK is expected to use. An unknown system is a warning, because a misspelt system silently breaks joins across guidelines. Source: smart-kg ontology/l1/l1.json valueSets "terminology-system"; smart-base input/fsh/profiles/SGLogicalModel.fsh and Aliases.fsh; UHC Compendium; CDHIv2.fsh. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Knowledge graph L1: terminology system](ValueSet-KGTerminologySystemVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "KGTerminologySystem",
  "url" : "http://smart.who.int/base/CodeSystem/KGTerminologySystem",
  "version" : "0.3.0",
  "name" : "KGTerminologySystem",
  "title" : "Knowledge graph L1: terminology system",
  "status" : "active",
  "experimental" : false,
  "date" : "2026-11-19T20:24:57+00:00",
  "publisher" : "WHO",
  "contact" : [{
    "name" : "WHO",
    "telecom" : [{
      "system" : "url",
      "value" : "http://who.int"
    }]
  }],
  "description" : "Code systems a DAK is expected to use. An unknown system is a warning, because a misspelt system silently breaks joins across guidelines. Source: smart-kg ontology/l1/l1.json valueSets \"terminology-system\"; smart-base input/fsh/profiles/SGLogicalModel.fsh and Aliases.fsh; UHC Compendium; CDHIv2.fsh.",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 8,
  "concept" : [{
    "code" : "SMART",
    "display" : "SMART",
    "definition" : "SMART Guidelines codes."
  },
  {
    "code" : "ICD-11",
    "display" : "ICD 11",
    "definition" : "ICD-11."
  },
  {
    "code" : "ICF",
    "display" : "ICF",
    "definition" : "ICF."
  },
  {
    "code" : "ICHI",
    "display" : "ICHI",
    "definition" : "International Classification of Health Interventions."
  },
  {
    "code" : "SNOMED-GPS",
    "display" : "SNOMED GPS",
    "definition" : "SNOMED CT Global Patient Set."
  },
  {
    "code" : "ATC",
    "display" : "ATC",
    "definition" : "Anatomical Therapeutic Chemical classification."
  },
  {
    "code" : "UHC",
    "display" : "UHC",
    "definition" : "UHC Compendium of health interventions."
  },
  {
    "code" : "CDHI",
    "display" : "CDHI",
    "definition" : "Classification of Digital Health Interventions."
  }]
}

```
