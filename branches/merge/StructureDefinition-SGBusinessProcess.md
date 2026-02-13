# SMART Guidelines Business Process - SMART Base v0.2.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **SMART Guidelines Business Process**

## Resource Profile: SMART Guidelines Business Process 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/SGBusinessProcess | *Version*:0.2.0 |
| Draft as of 2026-02-13 | *Computable Name*:SGBusinessProcess |

 
Defines the minimum expectations for Business Processes represented in SMART Guidelines 

**Usages:**

* This Profile is not used by any profiles in this Implementation Guide

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/smart.who.int.base|current/StructureDefinition/SGBusinessProcess)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-SGBusinessProcess.csv), [Excel](StructureDefinition-SGBusinessProcess.xlsx), [Schematron](StructureDefinition-SGBusinessProcess.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "SGBusinessProcess",
  "url" : "http://smart.who.int/base/StructureDefinition/SGBusinessProcess",
  "version" : "0.2.0",
  "name" : "SGBusinessProcess",
  "title" : "SMART Guidelines Business Process",
  "status" : "draft",
  "date" : "2026-02-13T20:18:33+00:00",
  "publisher" : "WHO",
  "contact" : [
    {
      "name" : "WHO",
      "telecom" : [
        {
          "system" : "url",
          "value" : "http://who.int"
        }
      ]
    }
  ],
  "description" : "Defines the minimum expectations for Business Processes represented in SMART Guidelines",
  "fhirVersion" : "4.0.1",
  "mapping" : [
    {
      "identity" : "workflow",
      "uri" : "http://hl7.org/fhir/workflow",
      "name" : "Workflow Pattern"
    },
    {
      "identity" : "w5",
      "uri" : "http://hl7.org/fhir/fivews",
      "name" : "FiveWs Pattern Mapping"
    },
    {
      "identity" : "objimpl",
      "uri" : "http://hl7.org/fhir/object-implementation",
      "name" : "Object Implementation Information"
    },
    {
      "identity" : "rim",
      "uri" : "http://hl7.org/v3",
      "name" : "RIM Mapping"
    }
  ],
  "kind" : "resource",
  "abstract" : false,
  "type" : "PlanDefinition",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/PlanDefinition",
  "derivation" : "constraint",
  "differential" : {
    "element" : [
      {
        "id" : "PlanDefinition",
        "path" : "PlanDefinition"
      }
    ]
  }
}

```
