# Knowledge graph L1: intervention type - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L1: intervention type**

## CodeSystem: Knowledge graph L1: intervention type 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/KGInterventionType | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGInterventionType |

 
DRAFT. What kind of intervention a recommendation or catalogued intervention concerns. To be aligned with the UHC Compendium's categories once checked. Source: smart-kg ontology/l1/l1.json valueSets "intervention-type"; WHO handbook §1.7.1 (clinical, health system, public health, diagnostic, surveillance); digital interventions per CDHI. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Knowledge graph L1: intervention type](ValueSet-KGInterventionTypeVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "KGInterventionType",
  "url" : "http://smart.who.int/base/CodeSystem/KGInterventionType",
  "version" : "0.3.0",
  "name" : "KGInterventionType",
  "title" : "Knowledge graph L1: intervention type",
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
  "description" : "DRAFT. What kind of intervention a recommendation or catalogued intervention concerns. To be aligned with the UHC Compendium's categories once checked. Source: smart-kg ontology/l1/l1.json valueSets \"intervention-type\"; WHO handbook §1.7.1 (clinical, health system, public health, diagnostic, surveillance); digital interventions per CDHI.",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 10,
  "concept" : [{
    "code" : "medicine",
    "display" : "Medicine",
    "definition" : "A medicine or supplement."
  },
  {
    "code" : "vaccine",
    "display" : "Vaccine",
    "definition" : "A vaccine."
  },
  {
    "code" : "diagnostic",
    "display" : "Diagnostic",
    "definition" : "A test or screening."
  },
  {
    "code" : "procedure",
    "display" : "Procedure",
    "definition" : "A clinical procedure."
  },
  {
    "code" : "device-product",
    "display" : "Device product",
    "definition" : "A device or commodity."
  },
  {
    "code" : "behavioural",
    "display" : "Behavioural",
    "definition" : "Counselling, education or behaviour change."
  },
  {
    "code" : "public-health",
    "display" : "Public health",
    "definition" : "A population-level public health measure."
  },
  {
    "code" : "health-system",
    "display" : "Health system",
    "definition" : "Service delivery, workforce or financing."
  },
  {
    "code" : "health-information",
    "display" : "Health information",
    "definition" : "Data collection, monitoring or surveillance."
  },
  {
    "code" : "digital",
    "display" : "Digital",
    "definition" : "A digital health intervention, classified by CDHI."
  }]
}

```
