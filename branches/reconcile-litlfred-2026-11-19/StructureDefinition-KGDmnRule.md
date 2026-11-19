# Knowledge graph L2-DMN: DMN Rule - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L2-DMN: DMN Rule**

## Logical Model: Knowledge graph L2-DMN: DMN Rule 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGDmnRule | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGDmnRule |

 
One row. Its input and output cells are carried as properties, not nodes: 250 of them in the BCG table alone, none the target of a cross-model edge. What the rule needs a node for is its citation edge into L1. conditions and outputs are arrays of {clause, description, text}. DMN puts the formal expression in description and the human-readable gloss in text, and both are worth keeping – the gloss is what a reviewer reads and the expression is what an implementer builds. Class IRI: http://smart.who.int/kg/dmn-rule. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGDmnRule.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGDmnRule.csv), [Excel](StructureDefinition-KGDmnRule.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGDmnRule",
  "url" : "http://smart.who.int/base/StructureDefinition/KGDmnRule",
  "version" : "0.3.0",
  "name" : "KGDmnRule",
  "title" : "Knowledge graph L2-DMN: DMN Rule",
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
  "description" : "One row. Its input and output cells are carried as properties, not nodes: 250 of them in the BCG table alone, none the target of a cross-model edge. What the rule needs a node for is its citation edge into L1. conditions and outputs are arrays of {clause, description, text}. DMN puts the formal expression in description and the human-readable gloss in text, and both are worth keeping -- the gloss is what a reviewer reads and the expression is what an implementer builds. Class IRI: http://smart.who.int/kg/dmn-rule.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGDmnRule",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGDmnRule",
      "path" : "KGDmnRule",
      "short" : "Knowledge graph L2-DMN: DMN Rule",
      "definition" : "One row. Its input and output cells are carried as properties, not nodes: 250 of them in the BCG table alone, none the target of a cross-model edge. What the rule needs a node for is its citation edge into L1. conditions and outputs are arrays of {clause, description, text}. DMN puts the formal expression in description and the human-readable gloss in text, and both are worth keeping -- the gloss is what a reviewer reads and the expression is what an implementer builds. Class IRI: http://smart.who.int/kg/dmn-rule."
    },
    {
      "id" : "KGDmnRule.id",
      "path" : "KGDmnRule.id",
      "short" : "Id",
      "definition" : "The identifier the source declares (an FSH instance id, a BPMN or DMN element id).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDmnRule.ordinal",
      "path" : "KGDmnRule.ordinal",
      "short" : "Ordinal",
      "definition" : "Position, counted from 0, in the order the source lists it.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "unsignedInt"
      }]
    },
    {
      "id" : "KGDmnRule.conditions",
      "path" : "KGDmnRule.conditions",
      "short" : "Conditions",
      "definition" : "The rule's input entries, by clause.",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "BackboneElement"
      }]
    },
    {
      "id" : "KGDmnRule.conditions.clause",
      "path" : "KGDmnRule.conditions.clause",
      "short" : "Clause",
      "definition" : "The id of the clause (column) the cell belongs to.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDmnRule.conditions.description",
      "path" : "KGDmnRule.conditions.description",
      "short" : "Description",
      "definition" : "The cell's formal expression.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDmnRule.conditions.text",
      "path" : "KGDmnRule.conditions.text",
      "short" : "Text",
      "definition" : "The cell's human-readable gloss.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDmnRule.outputs",
      "path" : "KGDmnRule.outputs",
      "short" : "Outputs",
      "definition" : "The rule's output entries, by clause.",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "BackboneElement"
      }]
    },
    {
      "id" : "KGDmnRule.outputs.clause",
      "path" : "KGDmnRule.outputs.clause",
      "short" : "Clause",
      "definition" : "The id of the clause (column) the cell belongs to.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDmnRule.outputs.description",
      "path" : "KGDmnRule.outputs.description",
      "short" : "Description",
      "definition" : "The cell's formal expression.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDmnRule.outputs.text",
      "path" : "KGDmnRule.outputs.text",
      "short" : "Text",
      "definition" : "The cell's human-readable gloss.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDmnRule.annotations",
      "path" : "KGDmnRule.annotations",
      "short" : "Annotations",
      "definition" : "The rule's annotation entries, by clause.",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "BackboneElement"
      }]
    },
    {
      "id" : "KGDmnRule.annotations.clause",
      "path" : "KGDmnRule.annotations.clause",
      "short" : "Clause",
      "definition" : "The id of the clause (column) the cell belongs to.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDmnRule.annotations.description",
      "path" : "KGDmnRule.annotations.description",
      "short" : "Description",
      "definition" : "The cell's formal expression.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDmnRule.annotations.text",
      "path" : "KGDmnRule.annotations.text",
      "short" : "Text",
      "definition" : "The cell's human-readable gloss.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    }]
  }
}

```
