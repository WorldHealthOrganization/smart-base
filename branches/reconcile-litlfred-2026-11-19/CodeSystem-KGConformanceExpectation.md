# Knowledge graph L2: conformance expectation - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L2: conformance expectation**

## CodeSystem: Knowledge graph L2: conformance expectation 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/KGConformanceExpectation | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGConformanceExpectation |

 
The conformance verb of a requirement statement. Added by the smart-base migration from smart-kg's propertyNote, which named the four values in prose. Source: smart-kg ontology/l2/l2.json valueSets "conformance-expectation"; http://hl7.org/fhir/ValueSet/conformance-expectation. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Knowledge graph L2: conformance expectation](ValueSet-KGConformanceExpectationVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "KGConformanceExpectation",
  "url" : "http://smart.who.int/base/CodeSystem/KGConformanceExpectation",
  "version" : "0.3.0",
  "name" : "KGConformanceExpectation",
  "title" : "Knowledge graph L2: conformance expectation",
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
  "description" : "The conformance verb of a requirement statement. Added by the smart-base migration from smart-kg's propertyNote, which named the four values in prose. Source: smart-kg ontology/l2/l2.json valueSets \"conformance-expectation\"; http://hl7.org/fhir/ValueSet/conformance-expectation.",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 4,
  "concept" : [{
    "code" : "SHALL",
    "display" : "SHALL",
    "definition" : "Support for the specified capability is required to be considered conformant."
  },
  {
    "code" : "SHOULD",
    "display" : "SHOULD",
    "definition" : "Support for the specified capability is strongly encouraged."
  },
  {
    "code" : "MAY",
    "display" : "MAY",
    "definition" : "Support for the specified capability is not necessary to be considered conformant."
  },
  {
    "code" : "SHOULD-NOT",
    "display" : "SHOULD NOT",
    "definition" : "Support for the specified capability is strongly discouraged."
  }]
}

```
