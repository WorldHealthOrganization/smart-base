# Knowledge graph L3: predicates - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L3: predicates**

## ValueSet: Knowledge graph L3: predicates 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/ValueSet/KGL3PredicatesVS | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGL3PredicatesVS |

 
All codes of KGL3Predicates. 

 **References** 

This value set is not used here; it may be used elsewhere (e.g. specifications and/or implementations that use this content)

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

##### Knowledge graph L3: predicates Schema API

JSON Schema for Knowledge graph L3: predicates ValueSet codes. Generated from FHIR expansions using IRI format.

**Version:** 1.0.0

## Endpoints

### GET /ValueSet-KGL3PredicatesVS.schema.json

#### JSON Schema definition for the enumeration ValueSet-KGL3PredicatesVS

This endpoint serves the JSON Schema definition for the enumeration ValueSet-KGL3PredicatesVS.

## Schema Definition

### ValueSet-KGL3PredicatesVS

**Description:** JSON Schema for Knowledge graph L3: predicates ValueSet codes. Generated from FHIR expansions using IRI format.

**Type:** string

**This documentation is automatically generated from the OpenAPI specification.**



## Resource Content

```json
{
  "resourceType" : "ValueSet",
  "id" : "KGL3PredicatesVS",
  "url" : "http://smart.who.int/base/ValueSet/KGL3PredicatesVS",
  "version" : "0.3.0",
  "name" : "KGL3PredicatesVS",
  "title" : "Knowledge graph L3: predicates",
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
  "description" : "All codes of KGL3Predicates.",
  "compose" : {
    "include" : [{
      "system" : "http://smart.who.int/base/CodeSystem/KGL3Predicates"
    }]
  }
}

```
