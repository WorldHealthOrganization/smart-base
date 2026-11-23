# Knowledge graph L2-DMN: DMN Input Clause - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L2-DMN: DMN Input Clause**

## Logical Model: Knowledge graph L2-DMN: DMN Input Clause 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGDmnInputClause | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGDmnInputClause |

 
An input column. Its expression text is where data element names are embedded, which is the only reason this is a node rather than a property of the table. Class IRI: http://smart.who.int/kg/dmn-input-clause. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGDmnInputClause.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGDmnInputClause.csv), [Excel](StructureDefinition-KGDmnInputClause.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGDmnInputClause",
  "url" : "http://smart.who.int/base/StructureDefinition/KGDmnInputClause",
  "version" : "0.3.0",
  "name" : "KGDmnInputClause",
  "title" : "Knowledge graph L2-DMN: DMN Input Clause",
  "status" : "active",
  "date" : "2026-11-23T18:43:32+00:00",
  "publisher" : "WHO",
  "contact" : [{
    "name" : "WHO",
    "telecom" : [{
      "system" : "url",
      "value" : "http://who.int"
    }]
  }],
  "description" : "An input column. Its expression text is where data element names are embedded, which is the only reason this is a node rather than a property of the table. Class IRI: http://smart.who.int/kg/dmn-input-clause.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGDmnInputClause",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGDmnInputClause",
      "path" : "KGDmnInputClause",
      "short" : "Knowledge graph L2-DMN: DMN Input Clause",
      "definition" : "An input column. Its expression text is where data element names are embedded, which is the only reason this is a node rather than a property of the table. Class IRI: http://smart.who.int/kg/dmn-input-clause."
    },
    {
      "id" : "KGDmnInputClause.id",
      "path" : "KGDmnInputClause.id",
      "short" : "Id",
      "definition" : "The identifier the source declares (an FSH instance id, a BPMN or DMN element id).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDmnInputClause.label",
      "path" : "KGDmnInputClause.label",
      "short" : "Label",
      "definition" : "The label, as declared.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDmnInputClause.expression",
      "path" : "KGDmnInputClause.expression",
      "short" : "Expression",
      "definition" : "The input expression, in FEEL or the DAK's convention.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDmnInputClause.typeRef",
      "path" : "KGDmnInputClause.typeRef",
      "short" : "Type ref",
      "definition" : "The input's typeRef.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDmnInputClause.ordinal",
      "path" : "KGDmnInputClause.ordinal",
      "short" : "Ordinal",
      "definition" : "Position, counted from 0, in the order the source lists it.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "unsignedInt"
      }]
    }]
  }
}

```
