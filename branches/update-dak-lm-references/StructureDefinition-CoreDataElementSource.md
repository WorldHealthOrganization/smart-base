# Core Data Element Source - SMART Base v0.2.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Core Data Element Source**

## Logical Model: Core Data Element Source 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/CoreDataElementSource | *Version*:0.2.0 |
| Active as of 2025-10-09 | *Computable Name*:CoreDataElementSource |

 
Source reference for Core Data Element - can be URL, canonical reference, or inline instance 

**Usages:**

* Use this Logical Model: [Digital Adaptation Kit (DAK)](StructureDefinition-DAK.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/smart.who.int.base|current/StructureDefinition/CoreDataElementSource)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-CoreDataElementSource.csv), [Excel](StructureDefinition-CoreDataElementSource.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "CoreDataElementSource",
  "url" : "http://smart.who.int/base/StructureDefinition/CoreDataElementSource",
  "version" : "0.2.0",
  "name" : "CoreDataElementSource",
  "title" : "Core Data Element Source",
  "status" : "active",
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
  "description" : "Source reference for Core Data Element - can be URL, canonical reference, or inline instance",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/CoreDataElementSource",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [
      {
        "id" : "CoreDataElementSource",
        "path" : "CoreDataElementSource",
        "short" : "Core Data Element Source",
        "definition" : "Source reference for Core Data Element - can be URL, canonical reference, or inline instance"
      },
      {
        "id" : "CoreDataElementSource.url",
        "path" : "CoreDataElementSource.url",
        "short" : "URL",
        "definition" : "URL to retrieve CoreDataElement definition from input/ or external source",
        "min" : 0,
        "max" : "1",
        "type" : [
          {
            "code" : "url"
          }
        ]
      },
      {
        "id" : "CoreDataElementSource.canonical",
        "path" : "CoreDataElementSource.canonical",
        "short" : "Canonical",
        "definition" : "Canonical URI pointing to the CoreDataElement definition",
        "min" : 0,
        "max" : "1",
        "type" : [
          {
            "code" : "canonical",
            "targetProfile" : [
              "http://smart.who.int/base/StructureDefinition/CoreDataElement"
            ]
          }
        ]
      },
      {
        "id" : "CoreDataElementSource.instance",
        "path" : "CoreDataElementSource.instance",
        "short" : "Instance",
        "definition" : "Inline CoreDataElement instance data",
        "min" : 0,
        "max" : "1",
        "type" : [
          {
            "code" : "http://smart.who.int/base/StructureDefinition/CoreDataElement"
          }
        ]
      }
    ]
  }
}

```
