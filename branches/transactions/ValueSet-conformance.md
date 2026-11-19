# Conformance Level - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Conformance Level**

## ValueSet: Conformance Level 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/ValueSet/conformance | *Version*:0.3.0 |
| Draft as of 2026-09-07 | *Computable Name*:ConformanceVS |

 
How binding a referenced standard is for a transaction. 

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

##### Conformance Level Schema API

JSON Schema for Conformance Level ValueSet codes. Generated from FHIR expansions using IRI format.

**Version:** 1.0.0

## Endpoints

### GET /ValueSet-conformance.schema.json

#### JSON Schema definition for the enumeration ValueSet-conformance

This endpoint serves the JSON Schema definition for the enumeration ValueSet-conformance.

## Schema Definition

### ValueSet-conformance

**Description:** JSON Schema for Conformance Level ValueSet codes. Generated from FHIR expansions using IRI format.

**Type:** string

**This documentation is automatically generated from the OpenAPI specification.**



## Resource Content

```json
{
  "resourceType" : "ValueSet",
  "id" : "conformance",
  "url" : "http://smart.who.int/base/ValueSet/conformance",
  "version" : "0.3.0",
  "name" : "ConformanceVS",
  "title" : "Conformance Level",
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
  "description" : "How binding a referenced standard is for a transaction.",
  "compose" : {
    "include" : [{
      "system" : "http://smart.who.int/base/CodeSystem/conformance"
    }]
  }
}

```
