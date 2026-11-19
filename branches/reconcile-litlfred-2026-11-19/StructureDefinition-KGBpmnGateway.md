# Knowledge graph L2-BPMN: BPMN Gateway - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L2-BPMN: BPMN Gateway**

## Logical Model: Knowledge graph L2-BPMN: BPMN Gateway 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGBpmnGateway | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGBpmnGateway |

 
A branch or merge. Included for connectivity rather than for a cross-model edge: a flow through a gateway with no node would point at nothing, and every reachability question over the process would break at the first decision point. Class IRI: http://smart.who.int/kg/bpmn-gateway. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGBpmnGateway.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGBpmnGateway.csv), [Excel](StructureDefinition-KGBpmnGateway.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGBpmnGateway",
  "url" : "http://smart.who.int/base/StructureDefinition/KGBpmnGateway",
  "version" : "0.3.0",
  "name" : "KGBpmnGateway",
  "title" : "Knowledge graph L2-BPMN: BPMN Gateway",
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
  "description" : "A branch or merge. Included for connectivity rather than for a cross-model edge: a flow through a gateway with no node would point at nothing, and every reachability question over the process would break at the first decision point. Class IRI: http://smart.who.int/kg/bpmn-gateway.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGBpmnGateway",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGBpmnGateway",
      "path" : "KGBpmnGateway",
      "short" : "Knowledge graph L2-BPMN: BPMN Gateway",
      "definition" : "A branch or merge. Included for connectivity rather than for a cross-model edge: a flow through a gateway with no node would point at nothing, and every reachability question over the process would break at the first decision point. Class IRI: http://smart.who.int/kg/bpmn-gateway."
    },
    {
      "id" : "KGBpmnGateway.id",
      "path" : "KGBpmnGateway.id",
      "short" : "Id",
      "definition" : "The identifier the source declares (an FSH instance id, a BPMN or DMN element id).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGBpmnGateway.name",
      "path" : "KGBpmnGateway.name",
      "short" : "Name",
      "definition" : "The computable name: the CamelCase identifier a Canonical() reference matches on.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGBpmnGateway.gatewayType",
      "path" : "KGBpmnGateway.gatewayType",
      "short" : "Gateway type",
      "definition" : "The BPMN gateway element type (exclusiveGateway, parallelGateway, …).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGBpmnGateway.direction",
      "path" : "KGBpmnGateway.direction",
      "short" : "Direction",
      "definition" : "The gateway's gatewayDirection.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://smart.who.int/base/ValueSet/KGGatewayDirectionVS"
      }
    },
    {
      "id" : "KGBpmnGateway.parent",
      "path" : "KGBpmnGateway.parent",
      "short" : "Parent",
      "definition" : "The id of the sub-process that contains it, when nested.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    }]
  }
}

```
