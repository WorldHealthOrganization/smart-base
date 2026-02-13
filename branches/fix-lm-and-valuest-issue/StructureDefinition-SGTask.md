# SGTask - SMART Base v0.2.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **SGTask**

## Extension: SGTask 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/SGTask | *Version*:0.2.0 |
| Draft as of 2025-10-09 | *Computable Name*:SGTask |

Extension to reference SMART Guidelines task type

**Context of Use**

**Usage info**

**Usages:**

* Use this Extension: [SMART Guidelines Requirements](StructureDefinition-SGRequirements.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/smart.who.int.base|current/StructureDefinition/SGTask)

### Formal Views of Extension Content

 [Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-SGTask.csv), [Excel](StructureDefinition-SGTask.xlsx), [Schematron](StructureDefinition-SGTask.sch) 

#### Constraints



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "SGTask",
  "url" : "http://smart.who.int/base/StructureDefinition/SGTask",
  "version" : "0.2.0",
  "name" : "SGTask",
  "status" : "draft",
  "date" : "2025-10-09T20:42:55+00:00",
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
  "description" : "Extension to reference SMART Guidelines task type",
  "fhirVersion" : "4.0.1",
  "mapping" : [
    {
      "identity" : "rim",
      "uri" : "http://hl7.org/v3",
      "name" : "RIM Mapping"
    }
  ],
  "kind" : "complex-type",
  "abstract" : false,
  "context" : [
    {
      "type" : "element",
      "expression" : "Element"
    }
  ],
  "type" : "Extension",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Extension",
  "derivation" : "constraint",
  "differential" : {
    "element" : [
      {
        "id" : "Extension",
        "path" : "Extension",
        "definition" : "Extension to reference SMART Guidelines task type"
      },
      {
        "id" : "Extension.extension",
        "path" : "Extension.extension",
        "max" : "0"
      },
      {
        "id" : "Extension.url",
        "path" : "Extension.url",
        "fixedUri" : "http://smart.who.int/base/StructureDefinition/SGTask"
      },
      {
        "id" : "Extension.value[x]",
        "path" : "Extension.value[x]",
        "slicing" : {
          "discriminator" : [
            {
              "type" : "type",
              "path" : "$this"
            }
          ],
          "ordered" : false,
          "rules" : "open"
        },
        "min" : 1
      },
      {
        "id" : "Extension.value[x]:valueCoding",
        "path" : "Extension.value[x]",
        "sliceName" : "valueCoding",
        "min" : 1,
        "max" : "1",
        "type" : [
          {
            "code" : "Coding"
          }
        ]
      },
      {
        "id" : "Extension.value[x]:valueCoding.system",
        "path" : "Extension.value[x].system",
        "min" : 1,
        "fixedUri" : "http://smart.who.int/base/CodeSystem/SGTasks",
        "mustSupport" : true
      },
      {
        "id" : "Extension.value[x]:valueCoding.code",
        "path" : "Extension.value[x].code",
        "min" : 1,
        "mustSupport" : true
      }
    ]
  }
}

```
