# SMART Guidelines PlanDefinition - SMART Base v0.2.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **SMART Guidelines PlanDefinition**

## Resource Profile: SMART Guidelines PlanDefinition 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/SGPlanDefinition | *Version*:0.2.0 |
| Draft as of 2026-02-13 | *Computable Name*:SGPlanDefinition |

 
Defines the minimum expectations for PlanDefinition resources used in SMART Guidelines 

**Usages:**

* Derived from this Profile: [SMART Guidelines Decision Table](StructureDefinition-SGDecisionTable.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/smart.who.int.base|current/StructureDefinition/SGPlanDefinition)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-SGPlanDefinition.csv), [Excel](StructureDefinition-SGPlanDefinition.xlsx), [Schematron](StructureDefinition-SGPlanDefinition.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "SGPlanDefinition",
  "url" : "http://smart.who.int/base/StructureDefinition/SGPlanDefinition",
  "version" : "0.2.0",
  "name" : "SGPlanDefinition",
  "title" : "SMART Guidelines PlanDefinition",
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
  "description" : "Defines the minimum expectations for PlanDefinition resources used in SMART Guidelines",
  "fhirVersion" : "4.0.1",
  "mapping" : [
    {
      "identity" : "rim",
      "uri" : "http://hl7.org/v3",
      "name" : "RIM Mapping"
    },
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
    }
  ],
  "kind" : "resource",
  "abstract" : false,
  "type" : "PlanDefinition",
  "baseDefinition" : "http://hl7.org/fhir/uv/crmi/StructureDefinition/crmi-shareableplandefinition",
  "derivation" : "constraint",
  "differential" : {
    "element" : [
      {
        "id" : "PlanDefinition",
        "path" : "PlanDefinition"
      },
      {
        "id" : "PlanDefinition.name",
        "path" : "PlanDefinition.name",
        "min" : 1
      },
      {
        "id" : "PlanDefinition.publisher",
        "path" : "PlanDefinition.publisher",
        "min" : 1
      }
    ]
  }
}

```
