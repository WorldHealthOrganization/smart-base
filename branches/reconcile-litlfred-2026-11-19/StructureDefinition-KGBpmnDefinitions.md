# Knowledge graph L2-BPMN: BPMN File - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L2-BPMN: BPMN File**

## Logical Model: Knowledge graph L2-BPMN: BPMN File 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGBpmnDefinitions | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGBpmnDefinitions |

 
One BPMN file as a unit – the `bpmn:definitions` root. Shares its IRI with the l1:external-artifact for the same file, so the component that points at it and the subgraph that opens it name one resource. Class IRI: http://smart.who.int/kg/bpmn-definitions. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGBpmnDefinitions.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGBpmnDefinitions.csv), [Excel](StructureDefinition-KGBpmnDefinitions.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGBpmnDefinitions",
  "url" : "http://smart.who.int/base/StructureDefinition/KGBpmnDefinitions",
  "version" : "0.3.0",
  "name" : "KGBpmnDefinitions",
  "title" : "Knowledge graph L2-BPMN: BPMN File",
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
  "description" : "One BPMN file as a unit -- the `bpmn:definitions` root. Shares its IRI with the l1:external-artifact for the same file, so the component that points at it and the subgraph that opens it name one resource. Class IRI: http://smart.who.int/kg/bpmn-definitions.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGBpmnDefinitions",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGBpmnDefinitions",
      "path" : "KGBpmnDefinitions",
      "short" : "Knowledge graph L2-BPMN: BPMN File",
      "definition" : "One BPMN file as a unit -- the `bpmn:definitions` root. Shares its IRI with the l1:external-artifact for the same file, so the component that points at it and the subgraph that opens it name one resource. Class IRI: http://smart.who.int/kg/bpmn-definitions."
    },
    {
      "id" : "KGBpmnDefinitions.id",
      "path" : "KGBpmnDefinitions.id",
      "short" : "Id",
      "definition" : "The identifier the source declares (an FSH instance id, a BPMN or DMN element id).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGBpmnDefinitions.targetNamespace",
      "path" : "KGBpmnDefinitions.targetNamespace",
      "short" : "Target namespace",
      "definition" : "The BPMN definitions' targetNamespace.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGBpmnDefinitions.exporter",
      "path" : "KGBpmnDefinitions.exporter",
      "short" : "Exporter",
      "definition" : "The tool that wrote the file.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGBpmnDefinitions.exporterVersion",
      "path" : "KGBpmnDefinitions.exporterVersion",
      "short" : "Exporter version",
      "definition" : "The version of that tool.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGBpmnDefinitions.source",
      "path" : "KGBpmnDefinitions.source",
      "short" : "Source",
      "definition" : "Where the node was read from: a repository path or URL.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGBpmnDefinitions.sha256",
      "path" : "KGBpmnDefinitions.sha256",
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
