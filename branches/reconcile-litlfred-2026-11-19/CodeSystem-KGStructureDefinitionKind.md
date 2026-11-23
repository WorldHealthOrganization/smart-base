# Knowledge graph L3: structure definition kind - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L3: structure definition kind**

## CodeSystem: Knowledge graph L3: structure definition kind 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/KGStructureDefinitionKind | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGStructureDefinitionKind |

 
FHIR StructureDefinitionKind. Added by the smart-base migration: smart-kg named the property without binding it. Source: smart-kg ontology/l3/l3.json valueSets "structure-definition-kind"; http://hl7.org/fhir/ValueSet/structure-definition-kind. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Knowledge graph L3: structure definition kind](ValueSet-KGStructureDefinitionKindVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "KGStructureDefinitionKind",
  "url" : "http://smart.who.int/base/CodeSystem/KGStructureDefinitionKind",
  "version" : "0.3.0",
  "name" : "KGStructureDefinitionKind",
  "title" : "Knowledge graph L3: structure definition kind",
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
  "description" : "FHIR StructureDefinitionKind. Added by the smart-base migration: smart-kg named the property without binding it. Source: smart-kg ontology/l3/l3.json valueSets \"structure-definition-kind\"; http://hl7.org/fhir/ValueSet/structure-definition-kind.",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 4,
  "concept" : [{
    "code" : "primitive-type",
    "display" : "Primitive type",
    "definition" : "A primitive type."
  },
  {
    "code" : "complex-type",
    "display" : "Complex type",
    "definition" : "A complex data type."
  },
  {
    "code" : "resource",
    "display" : "Resource",
    "definition" : "A resource."
  },
  {
    "code" : "logical",
    "display" : "Logical",
    "definition" : "A logical model."
  }]
}

```
