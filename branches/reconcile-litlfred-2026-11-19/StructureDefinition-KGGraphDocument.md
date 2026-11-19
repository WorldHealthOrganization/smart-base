# Knowledge graph L1: graph document - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L1: graph document**

## Logical Model: Knowledge graph L1: graph document 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGGraphDocument | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGGraphDocument |

 
One L1 knowledge-graph document: typed nodes and reified edges, provenance-pinned to the sources it was extracted from. In JSON the context element is written @context. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGGraphDocument.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGGraphDocument.csv), [Excel](StructureDefinition-KGGraphDocument.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGGraphDocument",
  "url" : "http://smart.who.int/base/StructureDefinition/KGGraphDocument",
  "version" : "0.3.0",
  "name" : "KGGraphDocument",
  "title" : "Knowledge graph L1: graph document",
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
  "description" : "One L1 knowledge-graph document: typed nodes and reified edges, provenance-pinned to the sources it was extracted from. In JSON the context element is written @context.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGGraphDocument",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGGraphDocument",
      "path" : "KGGraphDocument",
      "short" : "Knowledge graph L1: graph document",
      "definition" : "One L1 knowledge-graph document: typed nodes and reified edges, provenance-pinned to the sources it was extracted from. In JSON the context element is written @context."
    },
    {
      "id" : "KGGraphDocument.context",
      "path" : "KGGraphDocument.context",
      "short" : "Context",
      "definition" : "The JSON-LD context (written @context in JSON).",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGGraphDocument.id",
      "path" : "KGGraphDocument.id",
      "short" : "ID",
      "definition" : "IRI of this graph document.",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGGraphDocument.type",
      "path" : "KGGraphDocument.type",
      "short" : "Type",
      "definition" : "Always Entity (prov:Entity).",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }]
    },
    {
      "id" : "KGGraphDocument.ontologyVersion",
      "path" : "KGGraphDocument.ontologyVersion",
      "short" : "Ontology version",
      "definition" : "schemaVersion of the ontology this graph was built against.",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGGraphDocument.generatedAt",
      "path" : "KGGraphDocument.generatedAt",
      "short" : "Generated at",
      "definition" : "When the document was generated.",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "dateTime"
      }]
    },
    {
      "id" : "KGGraphDocument.wasDerivedFrom",
      "path" : "KGGraphDocument.wasDerivedFrom",
      "short" : "Derived from",
      "definition" : "The sources this graph was extracted from, each pinned by hash.",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://smart.who.int/base/StructureDefinition/KGProvenanceSource"
      }]
    },
    {
      "id" : "KGGraphDocument.nodes",
      "path" : "KGGraphDocument.nodes",
      "short" : "Nodes",
      "definition" : "The nodes.",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://smart.who.int/base/StructureDefinition/KGNode"
      }]
    },
    {
      "id" : "KGGraphDocument.edges",
      "path" : "KGGraphDocument.edges",
      "short" : "Edges",
      "definition" : "The edges.",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "http://smart.who.int/base/StructureDefinition/KGEdge"
      }]
    },
    {
      "id" : "KGGraphDocument.dak",
      "path" : "KGGraphDocument.dak",
      "short" : "DAK",
      "definition" : "The DAK envelope: the fields of the DAK logical model.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "BackboneElement"
      }]
    }]
  }
}

```
