# Knowledge graph L2-DMN: DMN Decision - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L2-DMN: DMN Decision**

## Logical Model: Knowledge graph L2-DMN: DMN Decision 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGDmnDecision | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGDmnDecision |

 
A `dmn:decision` – the question being answered, and the node that carries the link back to the BPMN task invoking it. A file may hold several; the BCG file holds one. Class IRI: http://smart.who.int/kg/dmn-decision. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGDmnDecision.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGDmnDecision.csv), [Excel](StructureDefinition-KGDmnDecision.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGDmnDecision",
  "url" : "http://smart.who.int/base/StructureDefinition/KGDmnDecision",
  "version" : "0.3.0",
  "name" : "KGDmnDecision",
  "title" : "Knowledge graph L2-DMN: DMN Decision",
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
  "description" : "A `dmn:decision` -- the question being answered, and the node that carries the link back to the BPMN task invoking it. A file may hold several; the BCG file holds one. Class IRI: http://smart.who.int/kg/dmn-decision.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGDmnDecision",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGDmnDecision",
      "path" : "KGDmnDecision",
      "short" : "Knowledge graph L2-DMN: DMN Decision",
      "definition" : "A `dmn:decision` -- the question being answered, and the node that carries the link back to the BPMN task invoking it. A file may hold several; the BCG file holds one. Class IRI: http://smart.who.int/kg/dmn-decision."
    },
    {
      "id" : "KGDmnDecision.id",
      "path" : "KGDmnDecision.id",
      "short" : "Id",
      "definition" : "The identifier the source declares (an FSH instance id, a BPMN or DMN element id).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDmnDecision.label",
      "path" : "KGDmnDecision.label",
      "short" : "Label",
      "definition" : "The label, as declared.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDmnDecision.question",
      "path" : "KGDmnDecision.question",
      "short" : "Question",
      "definition" : "The decision's question, as the DMN states it.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGDmnDecision.allowedAnswers",
      "path" : "KGDmnDecision.allowedAnswers",
      "short" : "Allowed answers",
      "definition" : "The decision's allowed answers, as the DMN states them.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    }]
  }
}

```
