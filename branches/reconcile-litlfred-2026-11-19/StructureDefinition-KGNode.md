# Knowledge graph: node - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph: node**

## Logical Model: Knowledge graph: node 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGNode | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGNode |

 
One typed node of a knowledge-graph document. Its instance fields are an instance of the logical model of its class (see definedBy), e.g. KGPublication for a publication. 

**Usages:**

* Use this Logical Model: [Knowledge graph L1: graph document](StructureDefinition-KGGraphDocument.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGNode.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGNode.csv), [Excel](StructureDefinition-KGNode.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGNode",
  "url" : "http://smart.who.int/base/StructureDefinition/KGNode",
  "version" : "0.3.0",
  "name" : "KGNode",
  "title" : "Knowledge graph: node",
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
  "description" : "One typed node of a knowledge-graph document. Its instance fields are an instance of the logical model of its class (see definedBy), e.g. KGPublication for a publication.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGNode",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGNode",
      "path" : "KGNode",
      "short" : "Knowledge graph: node",
      "definition" : "One typed node of a knowledge-graph document. Its instance fields are an instance of the logical model of its class (see definedBy), e.g. KGPublication for a publication."
    },
    {
      "id" : "KGNode.id",
      "path" : "KGNode.id",
      "short" : "ID",
      "definition" : "IRI, unique within the document.",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGNode.type",
      "path" : "KGNode.type",
      "short" : "Type",
      "definition" : "The node's class.",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "extensible",
        "valueSet" : "http://smart.who.int/base/ValueSet/KGL1ClassesVS"
      }
    },
    {
      "id" : "KGNode.label",
      "path" : "KGNode.label",
      "short" : "Label",
      "definition" : "Human-readable name. Required so a retrieved node reads without resolving it.",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGNode.definedBy",
      "path" : "KGNode.definedBy",
      "short" : "Defined by",
      "definition" : "Canonical URL of the logical model giving this node's instance shape.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGNode.properties",
      "path" : "KGNode.properties",
      "short" : "Properties",
      "definition" : "Instance fields, as declared by the class's logical model.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "BackboneElement"
      }]
    },
    {
      "id" : "KGNode.derivation",
      "path" : "KGNode.derivation",
      "short" : "Derivation",
      "definition" : "derived | inferred | decided.",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://smart.who.int/base/ValueSet/KGDerivationVS"
      }
    },
    {
      "id" : "KGNode.note",
      "path" : "KGNode.note",
      "short" : "Note",
      "definition" : "Why it is what it is. Required unless derived.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGNode.evidence",
      "path" : "KGNode.evidence",
      "short" : "Evidence",
      "definition" : "Where it came from. Required unless derived.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://smart.who.int/base/StructureDefinition/KGEvidenceLocation"
      }]
    },
    {
      "id" : "KGNode.flagRef",
      "path" : "KGNode.flagRef",
      "short" : "Flag",
      "definition" : "Id of a flag raised while extracting this node.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGNode.skill",
      "path" : "KGNode.skill",
      "short" : "Skill",
      "definition" : "Skill id that produced this node.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    }]
  }
}

```
