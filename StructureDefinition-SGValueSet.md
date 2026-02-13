# SMART Guidelines ValueSet - SMART Base v0.2.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **SMART Guidelines ValueSet**

## Resource Profile: SMART Guidelines ValueSet 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/SGValueSet | *Version*:0.2.0 |
| Draft as of 2026-02-13 | *Computable Name*:SGValueSet |

 
Defines the minimum expectations for ValueSet resources used in SMART Guidelines 

**Usages:**

* Refer to this Profile: [SMART Guidelines ImplementationGuide](StructureDefinition-SGImplementationGuide.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/smart.who.int.base|current/StructureDefinition/SGValueSet)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-SGValueSet.csv), [Excel](StructureDefinition-SGValueSet.xlsx), [Schematron](StructureDefinition-SGValueSet.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "SGValueSet",
  "url" : "http://smart.who.int/base/StructureDefinition/SGValueSet",
  "version" : "0.2.0",
  "name" : "SGValueSet",
  "title" : "SMART Guidelines ValueSet",
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
  "description" : "Defines the minimum expectations for ValueSet resources used in SMART Guidelines",
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
  "type" : "ValueSet",
  "baseDefinition" : "http://hl7.org/fhir/uv/crmi/StructureDefinition/crmi-shareablevalueset",
  "derivation" : "constraint",
  "differential" : {
    "element" : [
      {
        "id" : "ValueSet",
        "path" : "ValueSet"
      },
      {
        "id" : "ValueSet.name",
        "path" : "ValueSet.name",
        "min" : 1
      },
      {
        "id" : "ValueSet.publisher",
        "path" : "ValueSet.publisher",
        "min" : 1
      }
    ]
  }
}

```
