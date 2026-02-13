# SMART Guidelines ActivityDefinition - SMART Base v0.2.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **SMART Guidelines ActivityDefinition**

## Resource Profile: SMART Guidelines ActivityDefinition 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/SGActivityDefinition | *Version*:0.2.0 |
| Draft as of 2025-10-09 | *Computable Name*:SGActivityDefinition |

 
Defines the minimum expectations for ActivityDefinition resources used in SMART Guidelines 

**Usages:**

* Refer to this Profile: [SMART Guidelines ImplementationGuide](StructureDefinition-SGImplementationGuide.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/smart.who.int.base|current/StructureDefinition/SGActivityDefinition)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-SGActivityDefinition.csv), [Excel](StructureDefinition-SGActivityDefinition.xlsx), [Schematron](StructureDefinition-SGActivityDefinition.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "SGActivityDefinition",
  "url" : "http://smart.who.int/base/StructureDefinition/SGActivityDefinition",
  "version" : "0.2.0",
  "name" : "SGActivityDefinition",
  "title" : "SMART Guidelines ActivityDefinition",
  "status" : "draft",
  "date" : "2025-10-09T13:26:01+00:00",
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
  "description" : "Defines the minimum expectations for ActivityDefinition resources used in SMART Guidelines",
  "fhirVersion" : "4.0.1",
  "mapping" : [
    {
      "identity" : "workflow",
      "uri" : "http://hl7.org/fhir/workflow",
      "name" : "Workflow Pattern"
    },
    {
      "identity" : "rim",
      "uri" : "http://hl7.org/v3",
      "name" : "RIM Mapping"
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
  "type" : "ActivityDefinition",
  "baseDefinition" : "http://hl7.org/fhir/uv/crmi/StructureDefinition/crmi-shareableactivitydefinition",
  "derivation" : "constraint",
  "differential" : {
    "element" : [
      {
        "id" : "ActivityDefinition",
        "path" : "ActivityDefinition"
      },
      {
        "id" : "ActivityDefinition.name",
        "path" : "ActivityDefinition.name",
        "min" : 1
      },
      {
        "id" : "ActivityDefinition.publisher",
        "path" : "ActivityDefinition.publisher",
        "min" : 1
      }
    ]
  }
}

```
