# Functional and Non-Functional Requirements (DAK) - SMART Base v0.2.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Functional and Non-Functional Requirements (DAK)**

## Logical Model: Functional and Non-Functional Requirements (DAK) 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/Requirements | *Version*:0.2.0 |
| Active as of 2025-10-09 | *Computable Name*:Requirements |

 
Logical Model for representing Functional and Non-Functional Requirements from a DAK. A high-level list of core functions and capabilities that the system must have to meet the end users' needs. 

**Usages:**

* Use this Logical Model: [Requirements Source](StructureDefinition-RequirementsSource.md)
* Refer to this Logical Model: [Requirements Source](StructureDefinition-RequirementsSource.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/smart.who.int.base|current/StructureDefinition/Requirements)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-Requirements.csv), [Excel](StructureDefinition-Requirements.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Requirements",
  "url" : "http://smart.who.int/base/StructureDefinition/Requirements",
  "version" : "0.2.0",
  "name" : "Requirements",
  "title" : "Functional and Non-Functional Requirements (DAK)",
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
  "description" : "Logical Model for representing Functional and Non-Functional Requirements from a DAK. A high-level list of core functions and capabilities that the system must have to meet the end users' needs.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/Requirements",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [
      {
        "id" : "Requirements",
        "path" : "Requirements",
        "short" : "Functional and Non-Functional Requirements (DAK)",
        "definition" : "Logical Model for representing Functional and Non-Functional Requirements from a DAK. A high-level list of core functions and capabilities that the system must have to meet the end users' needs."
      },
      {
        "id" : "Requirements.description[x]",
        "path" : "Requirements.description[x]",
        "short" : "Description",
        "definition" : "Description of the requirements - either Markdown content or a URI to a Markdown file (absolute or relative to repository root)",
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
      },
      {
        "id" : "Requirements.functional",
        "path" : "Requirements.functional",
        "short" : "Functional Requirements",
        "definition" : "Functional requirements for the system that reference https://worldhealthorganization.github.io/smart-base/branches/fix-152/StructureDefinition-FunctionalRequirement.html",
        "min" : 0,
        "max" : "*",
        "type" : [
          {
            "code" : "Reference",
            "targetProfile" : [
              "http://smart.who.int/base/StructureDefinition/FunctionalRequirement"
            ]
          }
        ]
      },
      {
        "id" : "Requirements.nonfunctional",
        "path" : "Requirements.nonfunctional",
        "short" : "Non-Functional Requirements",
        "definition" : "Non-functional requirements for the system that reference https://worldhealthorganization.github.io/smart-base/branches/fix-152/StructureDefinition-NonFunctionalRequirement.html",
        "min" : 0,
        "max" : "*",
        "type" : [
          {
            "code" : "Reference",
            "targetProfile" : [
              "http://smart.who.int/base/StructureDefinition/NonFunctionalRequirement"
            ]
          }
        ]
      }
    ]
  }
}

```
