# SMART Guidelines StructureMap - SMART Base v0.2.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **SMART Guidelines StructureMap**

## Resource Profile: SMART Guidelines StructureMap 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/SGStructureMap | *Version*:0.2.0 |
| Draft as of 2025-10-11 | *Computable Name*:SGStructureMap |

 
Defines the minimum expectations for StructureMap resources used in SMART Guidelines 

**Usages:**

* Refer to this Profile: [SMART Guidelines ImplementationGuide](StructureDefinition-SGImplementationGuide.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/smart.who.int.base|current/StructureDefinition/SGStructureMap)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-SGStructureMap.csv), [Excel](StructureDefinition-SGStructureMap.xlsx), [Schematron](StructureDefinition-SGStructureMap.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "SGStructureMap",
  "url" : "http://smart.who.int/base/StructureDefinition/SGStructureMap",
  "version" : "0.2.0",
  "name" : "SGStructureMap",
  "title" : "SMART Guidelines StructureMap",
  "status" : "draft",
  "date" : "2025-10-11T22:03:24+00:00",
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
  "description" : "Defines the minimum expectations for StructureMap resources used in SMART Guidelines",
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
  "type" : "StructureMap",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/StructureMap",
  "derivation" : "constraint",
  "differential" : {
    "element" : [
      {
        "id" : "StructureMap",
        "path" : "StructureMap"
      },
      {
        "id" : "StructureMap.version",
        "path" : "StructureMap.version",
        "min" : 1
      },
      {
        "id" : "StructureMap.title",
        "path" : "StructureMap.title",
        "min" : 1
      },
      {
        "id" : "StructureMap.publisher",
        "path" : "StructureMap.publisher",
        "min" : 1
      },
      {
        "id" : "StructureMap.description",
        "path" : "StructureMap.description",
        "min" : 1
      }
    ]
  }
}

```
