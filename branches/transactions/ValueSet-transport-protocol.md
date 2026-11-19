# Transport Protocol - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Transport Protocol**

## ValueSet: Transport Protocol 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/ValueSet/transport-protocol | *Version*:0.3.0 |
| Draft as of 2026-09-07 | *Computable Name*:TransportProtocolVS |

 
The transport protocol or mechanism used to carry the exchange. 

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

##### Transport Protocol Schema API

JSON Schema for Transport Protocol ValueSet codes. Generated from FHIR expansions using IRI format.

**Version:** 1.0.0

## Endpoints

### GET /ValueSet-transport-protocol.schema.json

#### JSON Schema definition for the enumeration ValueSet-transport-protocol

This endpoint serves the JSON Schema definition for the enumeration ValueSet-transport-protocol.

## Schema Definition

### ValueSet-transport-protocol

**Description:** JSON Schema for Transport Protocol ValueSet codes. Generated from FHIR expansions using IRI format.

**Type:** string

**This documentation is automatically generated from the OpenAPI specification.**



## Resource Content

```json
{
  "resourceType" : "ValueSet",
  "id" : "transport-protocol",
  "url" : "http://smart.who.int/base/ValueSet/transport-protocol",
  "version" : "0.3.0",
  "name" : "TransportProtocolVS",
  "title" : "Transport Protocol",
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
  "description" : "The transport protocol or mechanism used to carry the exchange.",
  "compose" : {
    "include" : [{
      "system" : "http://smart.who.int/base/CodeSystem/transport-protocol"
    }]
  }
}

```
