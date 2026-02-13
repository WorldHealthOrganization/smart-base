# SGDecisionTableGuidance - SMART Base v0.2.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **SGDecisionTableGuidance**

## ActivityDefinition: SGDecisionTableGuidance 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/ActivityDefinition/SGDecisionTableGuidance | *Version*:0.2.0 |
| Draft as of 2025-06-07 | *Computable Name*:SGDecisionTableGuidance |

* **Id: **: **Version: **
  * SGDecisionTableGuidance: 0.2.0
* **Id: **: **Status: **
  * SGDecisionTableGuidance: draft
* **Id: **: **Date (date last changed): **
  * SGDecisionTableGuidance: 2025-06-07
* **Id: **: **Publisher (steward): **
  * SGDecisionTableGuidance: WHO
* **Id: **: **Knowledge Capability: **
  * SGDecisionTableGuidance: computable
* **Id: **: **Kind: **
  * SGDecisionTableGuidance: CommunicationRequest
* **Id: **: **Profile: **
  * SGDecisionTableGuidance: http://hl7.org/fhir/uv/cpg/StructureDefinition/cpg-communicationrequest
* **Id: **: **Intent: **
  * SGDecisionTableGuidance: proposal
* **Id: **: **doNotPerform: **
  * SGDecisionTableGuidance: false



## Resource Content

```json
{
  "resourceType" : "ActivityDefinition",
  "id" : "SGDecisionTableGuidance",
  "meta" : {
    "profile" : [
      "http://hl7.org/fhir/uv/cpg/StructureDefinition/cpg-communicationactivity"
    ]
  },
  "extension" : [
    {
      "url" : "http://hl7.org/fhir/uv/cpg/StructureDefinition/cpg-knowledgeCapability",
      "valueCode" : "computable"
    }
  ],
  "url" : "http://smart.who.int/base/ActivityDefinition/SGDecisionTableGuidance",
  "version" : "0.2.0",
  "name" : "SGDecisionTableGuidance",
  "status" : "draft",
  "experimental" : false,
  "date" : "2025-06-07",
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
  "kind" : "CommunicationRequest",
  "profile" : "http://hl7.org/fhir/uv/cpg/StructureDefinition/cpg-communicationrequest",
  "intent" : "proposal",
  "doNotPerform" : false
}

```
