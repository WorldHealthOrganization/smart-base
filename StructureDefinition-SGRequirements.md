# SMART Guidelines Requirements - SMART Base v0.2.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **SMART Guidelines Requirements**

## Resource Profile: SMART Guidelines Requirements 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/SGRequirements | *Version*:0.2.0 |
| Draft as of 2026-02-13 | *Computable Name*:SMART Guidelines Requirements |

 
Smart Guidelines Requirements 

**Usages:**

* Refer to this Profile: [SGRequirementExt](StructureDefinition-SGRequirementExt.md) and [Satisfies](StructureDefinition-Satisfies.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/smart.who.int.base|current/StructureDefinition/SGRequirements)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-SGRequirements.csv), [Excel](StructureDefinition-SGRequirements.xlsx), [Schematron](StructureDefinition-SGRequirements.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "SGRequirements",
  "extension" : [
    {
      "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-implements",
      "valueUri" : "http://hl7.org/fhir/StructureDefinition/CanonicalResource"
    }
  ],
  "url" : "http://smart.who.int/base/StructureDefinition/SGRequirements",
  "version" : "0.2.0",
  "name" : "SMART Guidelines Requirements",
  "status" : "draft",
  "date" : "2026-02-13T20:26:50+00:00",
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
  "description" : "Smart Guidelines Requirements",
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
      "identity" : "rim",
      "uri" : "http://hl7.org/v3",
      "name" : "RIM Mapping"
    }
  ],
  "kind" : "resource",
  "abstract" : false,
  "type" : "Requirements",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Requirements",
  "derivation" : "constraint",
  "differential" : {
    "element" : [
      {
        "id" : "Requirements",
        "path" : "Requirements"
      },
      {
        "id" : "Requirements.extension",
        "path" : "Requirements.extension",
        "slicing" : {
          "discriminator" : [
            {
              "type" : "value",
              "path" : "url"
            }
          ],
          "ordered" : false,
          "rules" : "open"
        }
      },
      {
        "id" : "Requirements.extension:task",
        "path" : "Requirements.extension",
        "sliceName" : "task",
        "min" : 0,
        "max" : "*",
        "type" : [
          {
            "code" : "Extension",
            "profile" : ["http://smart.who.int/base/StructureDefinition/SGTask"]
          }
        ]
      },
      {
        "id" : "Requirements.extension:satisfies",
        "path" : "Requirements.extension",
        "sliceName" : "satisfies",
        "min" : 0,
        "max" : "*",
        "type" : [
          {
            "code" : "Extension",
            "profile" : ["http://smart.who.int/base/StructureDefinition/Satisfies"]
          }
        ]
      },
      {
        "id" : "Requirements.extension:userstory",
        "path" : "Requirements.extension",
        "sliceName" : "userstory",
        "min" : 0,
        "type" : [
          {
            "code" : "Extension",
            "profile" : ["http://smart.who.int/base/StructureDefinition/SGUserStory"]
          }
        ]
      },
      {
        "id" : "Requirements.name",
        "path" : "Requirements.name",
        "min" : 1
      },
      {
        "id" : "Requirements.title",
        "path" : "Requirements.title",
        "min" : 1
      },
      {
        "id" : "Requirements.status",
        "path" : "Requirements.status",
        "mustSupport" : true
      },
      {
        "id" : "Requirements.experimental",
        "path" : "Requirements.experimental",
        "min" : 1
      },
      {
        "id" : "Requirements.description",
        "path" : "Requirements.description",
        "min" : 1
      },
      {
        "id" : "Requirements.statement.label",
        "path" : "Requirements.statement.label",
        "min" : 1
      }
    ]
  }
}

```
