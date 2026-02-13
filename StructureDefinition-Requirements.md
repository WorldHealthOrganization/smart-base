# Functional and Non-Functional Requirements (DAK) - SMART Base v0.2.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Functional and Non-Functional Requirements (DAK)**

## Logical Model: Functional and Non-Functional Requirements (DAK) 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/Requirements | *Version*:0.2.0 |
| Active as of 2026-02-13 | *Computable Name*:Requirements |

 
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
        "definition" : "Functional requirements for the system - can be provided as canonical reference or inline instance data",
        "min" : 0,
        "max" : "*",
        "type" : [
          {
            "code" : "BackboneElement"
          }
        ]
      },
      {
        "id" : "Requirements.functional.canonical",
        "path" : "Requirements.functional.canonical",
        "short" : "Canonical",
        "definition" : "Canonical URI pointing to the FunctionalRequirement definition",
        "min" : 0,
        "max" : "1",
        "type" : [
          {
            "code" : "canonical",
            "targetProfile" : [
              "http://smart.who.int/base/StructureDefinition/FunctionalRequirement"
            ]
          }
        ]
      },
      {
        "id" : "Requirements.functional.instance",
        "path" : "Requirements.functional.instance",
        "short" : "Instance",
        "definition" : "Inline FunctionalRequirement instance data",
        "min" : 0,
        "max" : "1",
        "type" : [
          {
            "code" : "http://smart.who.int/base/StructureDefinition/FunctionalRequirement"
          }
        ]
      },
      {
        "id" : "Requirements.nonfunctional",
        "path" : "Requirements.nonfunctional",
        "short" : "Non-Functional Requirements",
        "definition" : "Non-functional requirements for the system - can be provided as canonical reference or inline instance data",
        "min" : 0,
        "max" : "*",
        "type" : [
          {
            "code" : "BackboneElement"
          }
        ]
      },
      {
        "id" : "Requirements.nonfunctional.canonical",
        "path" : "Requirements.nonfunctional.canonical",
        "short" : "Canonical",
        "definition" : "Canonical URI pointing to the NonFunctionalRequirement definition",
        "min" : 0,
        "max" : "1",
        "type" : [
          {
            "code" : "canonical",
            "targetProfile" : [
              "http://smart.who.int/base/StructureDefinition/NonFunctionalRequirement"
            ]
          }
        ]
      },
      {
        "id" : "Requirements.nonfunctional.instance",
        "path" : "Requirements.nonfunctional.instance",
        "short" : "Instance",
        "definition" : "Inline NonFunctionalRequirement instance data",
        "min" : 0,
        "max" : "1",
        "type" : [
          {
            "code" : "http://smart.who.int/base/StructureDefinition/NonFunctionalRequirement"
          }
        ]
      }
    ]
  }
}

```
