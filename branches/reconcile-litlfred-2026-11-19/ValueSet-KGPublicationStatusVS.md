# Knowledge graph L2: publication status - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L2: publication status**

## ValueSet: Knowledge graph L2: publication status 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/ValueSet/KGPublicationStatusVS | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGPublicationStatusVS |

 
All codes of KGPublicationStatus. 

 **References** 

* [Knowledge graph L3: Activity Definition](StructureDefinition-KGActivityDefinition.md)
* [Knowledge graph L3: Actor Definition](StructureDefinition-KGActorDefinition.md)
* [Knowledge graph L3: Code System](StructureDefinition-KGCodeSystem.md)
* [Knowledge graph L3: Concept Map](StructureDefinition-KGConceptMap.md)
* [Knowledge graph L2: Digital Adaptation Kit](StructureDefinition-KGDak.md)
* [Knowledge graph L3: Library](StructureDefinition-KGLibrary.md)
* [Knowledge graph L3: Measure](StructureDefinition-KGMeasure.md)
* [Knowledge graph L3: Plan Definition](StructureDefinition-KGPlanDefinition.md)
* [Knowledge graph L3: Profile](StructureDefinition-KGProfile.md)
* [Knowledge graph L3: Questionnaire](StructureDefinition-KGQuestionnaire.md)
* [Knowledge graph L3: Requirements](StructureDefinition-KGRequirements.md)
* [Knowledge graph L3: Logical Model](StructureDefinition-KGStructureDefinition.md)
* [Knowledge graph L3: Structure Map](StructureDefinition-KGStructureMap.md)
* [Knowledge graph L3: Value Set](StructureDefinition-KGValueSet.md)

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

##### Knowledge graph L2: publication status Schema API

JSON Schema for Knowledge graph L2: publication status ValueSet codes. Generated from FHIR expansions using IRI format.

**Version:** 1.0.0

## Endpoints

### GET /ValueSet-KGPublicationStatusVS.schema.json

#### JSON Schema definition for the enumeration ValueSet-KGPublicationStatusVS

This endpoint serves the JSON Schema definition for the enumeration ValueSet-KGPublicationStatusVS.

## Schema Definition

### ValueSet-KGPublicationStatusVS

**Description:** JSON Schema for Knowledge graph L2: publication status ValueSet codes. Generated from FHIR expansions using IRI format.

**Type:** string

**This documentation is automatically generated from the OpenAPI specification.**



## Resource Content

```json
{
  "resourceType" : "ValueSet",
  "id" : "KGPublicationStatusVS",
  "url" : "http://smart.who.int/base/ValueSet/KGPublicationStatusVS",
  "version" : "0.3.0",
  "name" : "KGPublicationStatusVS",
  "title" : "Knowledge graph L2: publication status",
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
  "description" : "All codes of KGPublicationStatus.",
  "compose" : {
    "include" : [{
      "system" : "http://smart.who.int/base/CodeSystem/KGPublicationStatus"
    }]
  }
}

```
