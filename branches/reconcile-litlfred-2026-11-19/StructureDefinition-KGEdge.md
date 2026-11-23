# Knowledge graph: edge - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph: edge**

## Logical Model: Knowledge graph: edge 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGEdge | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGEdge |

 
One reified statement: a predicate from a source node to a target node, with its derivation and evidence. 

**Usages:**

* Use this Logical Model: [Knowledge graph L1: graph document](StructureDefinition-KGGraphDocument.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGEdge.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGEdge.csv), [Excel](StructureDefinition-KGEdge.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGEdge",
  "url" : "http://smart.who.int/base/StructureDefinition/KGEdge",
  "version" : "0.3.0",
  "name" : "KGEdge",
  "title" : "Knowledge graph: edge",
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
  "description" : "One reified statement: a predicate from a source node to a target node, with its derivation and evidence.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGEdge",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGEdge",
      "path" : "KGEdge",
      "short" : "Knowledge graph: edge",
      "definition" : "One reified statement: a predicate from a source node to a target node, with its derivation and evidence."
    },
    {
      "id" : "KGEdge.type",
      "path" : "KGEdge.type",
      "short" : "Type",
      "definition" : "Always Statement (rdf:Statement).",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }]
    },
    {
      "id" : "KGEdge.predicate",
      "path" : "KGEdge.predicate",
      "short" : "Predicate",
      "definition" : "The predicate; the layer's edge table says which (source, target) pairs it licenses.",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "extensible",
        "valueSet" : "http://smart.who.int/base/ValueSet/KGL1PredicatesVS"
      }
    },
    {
      "id" : "KGEdge.source",
      "path" : "KGEdge.source",
      "short" : "Source",
      "definition" : "IRI of the source node.",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGEdge.target",
      "path" : "KGEdge.target",
      "short" : "Target",
      "definition" : "IRI of the target node.",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGEdge.qualifier",
      "path" : "KGEdge.qualifier",
      "short" : "Qualifier",
      "definition" : "A label on the relationship.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGEdge.derivation",
      "path" : "KGEdge.derivation",
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
      "id" : "KGEdge.note",
      "path" : "KGEdge.note",
      "short" : "Note",
      "definition" : "Why it is what it is. Required unless derived.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGEdge.evidence",
      "path" : "KGEdge.evidence",
      "short" : "Evidence",
      "definition" : "Where it came from. Required unless derived.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "http://smart.who.int/base/StructureDefinition/KGEvidenceLocation"
      }]
    },
    {
      "id" : "KGEdge.flagRef",
      "path" : "KGEdge.flagRef",
      "short" : "Flag",
      "definition" : "Id of a flag raised while extracting this edge.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGEdge.skill",
      "path" : "KGEdge.skill",
      "short" : "Skill",
      "definition" : "Skill id that produced this edge.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGEdge.properties",
      "path" : "KGEdge.properties",
      "short" : "Properties",
      "definition" : "Fields of the statement itself.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "BackboneElement"
      }]
    },
    {
      "id" : "KGEdge.properties.resolutionStatus",
      "path" : "KGEdge.properties.resolutionStatus",
      "short" : "Resolution status",
      "definition" : "For a cross-format join: unresolved | resolved | ambiguous.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://smart.who.int/base/ValueSet/KGResolutionStatusVS"
      }
    },
    {
      "id" : "KGEdge.properties.matchedOn",
      "path" : "KGEdge.properties.matchedOn",
      "short" : "Matched on",
      "definition" : "What the join was matched on.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    }]
  }
}

```
