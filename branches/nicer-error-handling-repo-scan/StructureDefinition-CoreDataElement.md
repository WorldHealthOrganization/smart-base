# Core Data Element (DAK) - SMART Base v0.2.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Core Data Element (DAK)**

## Logical Model: Core Data Element (DAK) 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/CoreDataElement | *Version*:0.2.0 |
| Active as of 2025-10-11 | *Computable Name*:CoreDataElement |

 
Logical Model for representing Core Data Elements from a DAK. Data elements are required throughout the different points of a workflow and are mapped to established concept mapping standards. 

**Usages:**

* Use this Logical Model: [Core Data Element Source](StructureDefinition-CoreDataElementSource.md)
* Refer to this Logical Model: [Core Data Element Source](StructureDefinition-CoreDataElementSource.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/smart.who.int.base|current/StructureDefinition/CoreDataElement)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-CoreDataElement.csv), [Excel](StructureDefinition-CoreDataElement.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "CoreDataElement",
  "url" : "http://smart.who.int/base/StructureDefinition/CoreDataElement",
  "version" : "0.2.0",
  "name" : "CoreDataElement",
  "title" : "Core Data Element (DAK)",
  "status" : "active",
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
  "description" : "Logical Model for representing Core Data Elements from a DAK. Data elements are required throughout the different points of a workflow and are mapped to established concept mapping standards.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/CoreDataElement",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [
      {
        "id" : "CoreDataElement",
        "path" : "CoreDataElement",
        "short" : "Core Data Element (DAK)",
        "definition" : "Logical Model for representing Core Data Elements from a DAK. Data elements are required throughout the different points of a workflow and are mapped to established concept mapping standards."
      },
      {
        "id" : "CoreDataElement.code",
        "path" : "CoreDataElement.code",
        "short" : "Code",
        "definition" : "Code that identifies the concept",
        "min" : 1,
        "max" : "1",
        "type" : [
          {
            "code" : "code"
          }
        ]
      },
      {
        "id" : "CoreDataElement.display",
        "path" : "CoreDataElement.display",
        "short" : "Display",
        "definition" : "Text displayed to the user",
        "min" : 1,
        "max" : "1",
        "type" : [
          {
            "code" : "string"
          }
        ]
      },
      {
        "id" : "CoreDataElement.definition",
        "path" : "CoreDataElement.definition",
        "short" : "Definition",
        "definition" : "Formal definition of the data element",
        "min" : 1,
        "max" : "1",
        "type" : [
          {
            "code" : "string"
          }
        ]
      },
      {
        "id" : "CoreDataElement.description[x]",
        "path" : "CoreDataElement.description[x]",
        "short" : "Description",
        "definition" : "Description of the core data element - either Markdown content or a URI to a Markdown file (absolute or relative to repository root)",
        "min" : 0,
        "max" : "1",
        "type" : [
          {
            "code" : "string"
          },
          {
            "code" : "uri"
          }
        ]
      }
    ]
  }
}

```
