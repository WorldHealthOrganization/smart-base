# Knowledge graph L2-DMN: DMN File - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L2-DMN: DMN File**

## Logical Model: Knowledge graph L2-DMN: DMN File 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGDmnDefinitions | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGDmnDefinitions |

 
One DMN file as a unit – the `dmn:definitions` root. Shares its IRI with the l1:external-artifact for the same file, so the l2:decision-support-logic component that points at it and this subgraph name one resource. Class IRI: http://smart.who.int/kg/dmn-definitions. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGDmnDefinitions.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGDmnDefinitions.csv), [Excel](StructureDefinition-KGDmnDefinitions.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGDmnDefinitions",
  "url" : "http://smart.who.int/base/StructureDefinition/KGDmnDefinitions",
  "version" : "0.3.0",
  "name" : "KGDmnDefinitions",
  "title" : "Knowledge graph L2-DMN: DMN File",
  "status" : "active",
  "date" : "2026-11-19T20:24:57+00:00",
  "publisher" : "WHO",
  "contact" : [{
    "name" : "WHO",
    "telecom" : [{
      "system" : "url",
      "value" : "http://who.int"
    }]
  }],
  "description" : "One DMN file as a unit -- the `dmn:definitions` root. Shares its IRI with the l1:external-artifact for the same file, so the l2:decision-support-logic component that points at it and this subgraph name one resource. Class IRI: http://smart.who.int/kg/dmn-definitions.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGDmnDefinitions",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGDmnDefinitions",
      "path" : "KGDmnDefinitions",
      "short" : "Knowledge graph L2-DMN: DMN File",
      "definition" : "One DMN file as a unit -- the `dmn:definitions` root. Shares its IRI with the l1:external-artifact for the same file, so the l2:decision-support-logic component that points at it and this subgraph name one resource. Class IRI: http://smart.who.int/kg/dmn-definitions."
    },
    {
      "id" : "KGDmnDefinitions.id",
      "path" : "KGDmnDefinitions.id",
      "short" : "Id",
      "definition" : "The identifier the source declares (an FSH instance id, a BPMN or DMN element id).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDmnDefinitions.namespace",
      "path" : "KGDmnDefinitions.namespace",
      "short" : "Namespace",
      "definition" : "The DMN definitions' namespace.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGDmnDefinitions.label",
      "path" : "KGDmnDefinitions.label",
      "short" : "Label",
      "definition" : "The label, as declared.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDmnDefinitions.source",
      "path" : "KGDmnDefinitions.source",
      "short" : "Source",
      "definition" : "Where the node was read from: a repository path or URL.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDmnDefinitions.sha256",
      "path" : "KGDmnDefinitions.sha256",
      "short" : "SHA-256",
      "definition" : "Hash of the file the node was read from; pins the source.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    }]
  }
}

```
