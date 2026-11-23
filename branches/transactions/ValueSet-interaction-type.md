# Interaction Type - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Interaction Type**

## ValueSet: Interaction Type 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/ValueSet/interaction-type | *Version*:0.3.0 |
| Draft as of 2026-09-07 | *Computable Name*:InteractionTypeVS |

 
The type of actors involved in an interaction. 

 **References** 

* [Interaction](StructureDefinition-Interaction.md)

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

##### Interaction Type Schema API

JSON Schema for Interaction Type ValueSet codes. Generated from FHIR expansions using IRI format.

**Version:** 1.0.0

## Endpoints

### GET /ValueSet-interaction-type.schema.json

#### JSON Schema definition for the enumeration ValueSet-interaction-type

This endpoint serves the JSON Schema definition for the enumeration ValueSet-interaction-type.

## Schema Definition

### ValueSet-interaction-type

**Description:** JSON Schema for Interaction Type ValueSet codes. Generated from FHIR expansions using IRI format.

**Type:** string

**This documentation is automatically generated from the OpenAPI specification.**



## Resource Content

```json
{
  "resourceType" : "ValueSet",
  "id" : "interaction-type",
  "url" : "http://smart.who.int/base/ValueSet/interaction-type",
  "version" : "0.3.0",
  "name" : "InteractionTypeVS",
  "title" : "Interaction Type",
  "status" : "draft",
  "date" : "2026-09-07T06:11:01+00:00",
  "publisher" : "WHO",
  "contact" : [{
    "name" : "WHO",
    "telecom" : [{
      "system" : "url",
      "value" : "http://who.int"
    }]
  }],
  "description" : "The type of actors involved in an interaction.",
  "compose" : {
    "include" : [{
      "system" : "http://smart.who.int/base/CodeSystem/interaction-type"
    }]
  }
}

```
