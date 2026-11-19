# Exchange Pattern - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Exchange Pattern**

## ValueSet: Exchange Pattern 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/ValueSet/exchange-pattern | *Version*:0.3.0 |
| Draft as of 2026-09-07 | *Computable Name*:ExchangePatternVS |

 
The broad architectural pattern of the data exchange. 

 **References** 

* [Transaction](StructureDefinition-Transaction.md)

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

##### Exchange Pattern Schema API

JSON Schema for Exchange Pattern ValueSet codes. Generated from FHIR expansions using IRI format.

**Version:** 1.0.0

## Endpoints

### GET /ValueSet-exchange-pattern.schema.json

#### JSON Schema definition for the enumeration ValueSet-exchange-pattern

This endpoint serves the JSON Schema definition for the enumeration ValueSet-exchange-pattern.

## Schema Definition

### ValueSet-exchange-pattern

**Description:** JSON Schema for Exchange Pattern ValueSet codes. Generated from FHIR expansions using IRI format.

**Type:** string

**This documentation is automatically generated from the OpenAPI specification.**



## Resource Content

```json
{
  "resourceType" : "ValueSet",
  "id" : "exchange-pattern",
  "url" : "http://smart.who.int/base/ValueSet/exchange-pattern",
  "version" : "0.3.0",
  "name" : "ExchangePatternVS",
  "title" : "Exchange Pattern",
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
  "description" : "The broad architectural pattern of the data exchange.",
  "compose" : {
    "include" : [{
      "system" : "http://smart.who.int/base/CodeSystem/exchange-pattern"
    }]
  }
}

```
