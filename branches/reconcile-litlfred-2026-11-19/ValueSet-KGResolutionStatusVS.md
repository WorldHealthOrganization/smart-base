# Knowledge graph L1: resolution status - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L1: resolution status**

## ValueSet: Knowledge graph L1: resolution status 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/ValueSet/KGResolutionStatusVS | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGResolutionStatusVS |

 
All codes of KGResolutionStatus. 

 **References** 

* [Knowledge graph L2: Business Process Workflow](StructureDefinition-KGBusinessProcess.md)
* [Knowledge graph L1: Citation](StructureDefinition-KGCitation.md)
* [Knowledge graph L2: Core Data Element](StructureDefinition-KGDataElement.md)
* [Knowledge graph L2: Decision-Support Logic](StructureDefinition-KGDecisionSupportLogic.md)
* [Knowledge graph: edge](StructureDefinition-KGEdge.md)
* [Knowledge graph L2: Functional Requirement](StructureDefinition-KGFunctionalRequirement.md)
* [Knowledge graph L2: Non-Functional Requirement](StructureDefinition-KGNonFunctionalRequirement.md)
* [Knowledge graph L2: Generic Persona](StructureDefinition-KGPersona.md)
* [Knowledge graph L2: Program Indicator](StructureDefinition-KGProgramIndicator.md)
* [Knowledge graph L1: Reference entry](StructureDefinition-KGReferenceEntry.md)
* [Knowledge graph L2: Scheduling Logic](StructureDefinition-KGSchedulingLogic.md)
* [Knowledge graph L2: Test Scenario](StructureDefinition-KGTestScenario.md)
* [Knowledge graph L2: User Scenario](StructureDefinition-KGUserScenario.md)

### Logical Definition (CLD)

 

### Expansion

-------

 Explanation of the columns that may appear on this page: 

| | |
| :--- | :--- |
| Level | A few code lists that FHIR defines are hierarchical - each code is assigned a level. In this scheme, some codes are under other codes, and imply that the code they are under also applies |
| System | The source of the definition of the code (when the value set draws in codes defined elsewhere) |
| Code | The code (used as the code in the resource instance) |
| Display | The display (used in the*display*element of a[Coding](http://hl7.org/fhir/R4/datatypes.html#Coding)). If there is no display, implementers should not simply display the code, but map the concept into their application |
| Definition | An explanation of the meaning of the concept |
| Comments | Additional notes about how to use the code |

## API Information

##### Knowledge graph L1: resolution status Schema API

JSON Schema for Knowledge graph L1: resolution status ValueSet codes. Generated from FHIR expansions using IRI format.

**Version:** 1.0.0

## Endpoints

### GET /ValueSet-KGResolutionStatusVS.schema.json

#### JSON Schema definition for the enumeration ValueSet-KGResolutionStatusVS

This endpoint serves the JSON Schema definition for the enumeration ValueSet-KGResolutionStatusVS.

## Schema Definition

### ValueSet-KGResolutionStatusVS

**Description:** JSON Schema for Knowledge graph L1: resolution status ValueSet codes. Generated from FHIR expansions using IRI format.

**Type:** string

**This documentation is automatically generated from the OpenAPI specification.**



## Resource Content

```json
{
  "resourceType" : "ValueSet",
  "id" : "KGResolutionStatusVS",
  "url" : "http://smart.who.int/base/ValueSet/KGResolutionStatusVS",
  "version" : "0.3.0",
  "name" : "KGResolutionStatusVS",
  "title" : "Knowledge graph L1: resolution status",
  "status" : "active",
  "experimental" : false,
  "date" : "2026-11-23T18:43:32+00:00",
  "publisher" : "WHO",
  "contact" : [{
    "name" : "WHO",
    "telecom" : [{
      "system" : "url",
      "value" : "http://who.int"
    }]
  }],
  "description" : "All codes of KGResolutionStatus.",
  "compose" : {
    "include" : [{
      "system" : "http://smart.who.int/base/CodeSystem/KGResolutionStatus"
    }]
  }
}

```
