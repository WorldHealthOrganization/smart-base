# Knowledge graph L2-DMN: DMN Decision Table - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L2-DMN: DMN Decision Table**

## Logical Model: Knowledge graph L2-DMN: DMN Decision Table 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGDmnDecisionTable | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGDmnDecisionTable |

 
The table realising a decision. Separate from dmn-decision because DMN permits other expression kinds – a literal expression, an invocation – and collapsing the two would make the graph unable to say which was used. hitPolicy is optional and recorded as null when absent, which it is in the BCG table. DMN's default is UNIQUE, but asserting it here would put words in the author's mouth. Class IRI: http://smart.who.int/kg/dmn-decision-table. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGDmnDecisionTable.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGDmnDecisionTable.csv), [Excel](StructureDefinition-KGDmnDecisionTable.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGDmnDecisionTable",
  "url" : "http://smart.who.int/base/StructureDefinition/KGDmnDecisionTable",
  "version" : "0.3.0",
  "name" : "KGDmnDecisionTable",
  "title" : "Knowledge graph L2-DMN: DMN Decision Table",
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
  "description" : "The table realising a decision. Separate from dmn-decision because DMN permits other expression kinds -- a literal expression, an invocation -- and collapsing the two would make the graph unable to say which was used. hitPolicy is optional and recorded as null when absent, which it is in the BCG table. DMN's default is UNIQUE, but asserting it here would put words in the author's mouth. Class IRI: http://smart.who.int/kg/dmn-decision-table.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGDmnDecisionTable",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGDmnDecisionTable",
      "path" : "KGDmnDecisionTable",
      "short" : "Knowledge graph L2-DMN: DMN Decision Table",
      "definition" : "The table realising a decision. Separate from dmn-decision because DMN permits other expression kinds -- a literal expression, an invocation -- and collapsing the two would make the graph unable to say which was used. hitPolicy is optional and recorded as null when absent, which it is in the BCG table. DMN's default is UNIQUE, but asserting it here would put words in the author's mouth. Class IRI: http://smart.who.int/kg/dmn-decision-table."
    },
    {
      "id" : "KGDmnDecisionTable.id",
      "path" : "KGDmnDecisionTable.id",
      "short" : "Id",
      "definition" : "The identifier the source declares (an FSH instance id, a BPMN or DMN element id).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDmnDecisionTable.hitPolicy",
      "path" : "KGDmnDecisionTable.hitPolicy",
      "short" : "Hit policy",
      "definition" : "The decision table's hitPolicy. Absent when the DMN gives none: DMN's default UNIQUE is not asserted.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDmnDecisionTable.aggregation",
      "path" : "KGDmnDecisionTable.aggregation",
      "short" : "Aggregation",
      "definition" : "The decision table's aggregation, for a COLLECT hit policy.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    }]
  }
}

```
