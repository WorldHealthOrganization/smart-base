# Knowledge graph L2-BPMN: gateway direction - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L2-BPMN: gateway direction**

## CodeSystem: Knowledge graph L2-BPMN: gateway direction 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/KGGatewayDirection | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGGatewayDirection |

 
BPMN 2.0's gatewayDirection. Added by the smart-base migration: smart-kg named the property without binding it. Source: smart-kg ontology/l2-bpmn/l2-bpmn.json valueSets "gateway-direction"; OMG BPMN 2.0.2, Gateway.gatewayDirection. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Knowledge graph L2-BPMN: gateway direction](ValueSet-KGGatewayDirectionVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "KGGatewayDirection",
  "url" : "http://smart.who.int/base/CodeSystem/KGGatewayDirection",
  "version" : "0.3.0",
  "name" : "KGGatewayDirection",
  "title" : "Knowledge graph L2-BPMN: gateway direction",
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
  "description" : "BPMN 2.0's gatewayDirection. Added by the smart-base migration: smart-kg named the property without binding it. Source: smart-kg ontology/l2-bpmn/l2-bpmn.json valueSets \"gateway-direction\"; OMG BPMN 2.0.2, Gateway.gatewayDirection.",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 4,
  "concept" : [{
    "code" : "Unspecified",
    "display" : "Unspecified",
    "definition" : "No constraint on incoming and outgoing flows."
  },
  {
    "code" : "Converging",
    "display" : "Converging",
    "definition" : "Many incoming flows, at most one outgoing."
  },
  {
    "code" : "Diverging",
    "display" : "Diverging",
    "definition" : "At most one incoming flow, many outgoing."
  },
  {
    "code" : "Mixed",
    "display" : "Mixed",
    "definition" : "Many incoming and many outgoing flows."
  }]
}

```
