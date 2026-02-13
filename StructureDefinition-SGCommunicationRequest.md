# SMART Guidelines Communication Request - SMART Base v0.2.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **SMART Guidelines Communication Request**

## Resource Profile: SMART Guidelines Communication Request 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/SGCommunicationRequest | *Version*:0.2.0 |
| Draft as of 2026-02-13 | *Computable Name*:SGCommunicationRequest |

 
Provide communication 

**Usages:**

* This Profile is not used by any profiles in this Implementation Guide

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/smart.who.int.base|current/StructureDefinition/SGCommunicationRequest)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-SGCommunicationRequest.csv), [Excel](StructureDefinition-SGCommunicationRequest.xlsx), [Schematron](StructureDefinition-SGCommunicationRequest.sch) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "SGCommunicationRequest",
  "extension" : [
    {
      "url" : "http://hl7.org/fhir/uv/cpg/StructureDefinition/cpg-knowledgeCapability",
      "valueCode" : "computable"
    }
  ],
  "url" : "http://smart.who.int/base/StructureDefinition/SGCommunicationRequest",
  "version" : "0.2.0",
  "name" : "SGCommunicationRequest",
  "title" : "SMART Guidelines Communication Request",
  "status" : "draft",
  "date" : "2026-02-13T20:26:50+00:00",
  "publisher" : "WHO",
  "contact" : [
    {
      "name" : "WHO",
      "telecom" : [
        {
          "system" : "url",
          "value" : "http://who.int"
        }
      ]
    }
  ],
  "description" : "Provide communication",
  "fhirVersion" : "4.0.1",
  "mapping" : [
    {
      "identity" : "workflow",
      "uri" : "http://hl7.org/fhir/workflow",
      "name" : "Workflow Pattern"
    },
    {
      "identity" : "w5",
      "uri" : "http://hl7.org/fhir/fivews",
      "name" : "FiveWs Pattern Mapping"
    },
    {
      "identity" : "rim",
      "uri" : "http://hl7.org/v3",
      "name" : "RIM Mapping"
    }
  ],
  "kind" : "resource",
  "abstract" : false,
  "type" : "CommunicationRequest",
  "baseDefinition" : "http://hl7.org/fhir/uv/cpg/StructureDefinition/cpg-communicationrequest",
  "derivation" : "constraint",
  "differential" : {
    "element" : [
      {
        "id" : "CommunicationRequest",
        "path" : "CommunicationRequest"
      },
      {
        "id" : "CommunicationRequest.status",
        "path" : "CommunicationRequest.status",
        "patternCode" : "active"
      },
      {
        "id" : "CommunicationRequest.doNotPerform",
        "path" : "CommunicationRequest.doNotPerform",
        "patternBoolean" : false
      }
    ]
  }
}

```
