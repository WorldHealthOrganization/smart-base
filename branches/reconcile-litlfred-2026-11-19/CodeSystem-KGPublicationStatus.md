# Knowledge graph L2: publication status - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L2: publication status**

## CodeSystem: Knowledge graph L2: publication status 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/KGPublicationStatus | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGPublicationStatus |

 
FHIR PublicationStatus, which DAK.fsh's status and every L3 resource's status take. Added by the smart-base migration: smart-kg named these properties without binding them. Source: smart-kg ontology/l2/l2.json valueSets "publication-status"; http://hl7.org/fhir/ValueSet/publication-status. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Knowledge graph L2: publication status](ValueSet-KGPublicationStatusVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "KGPublicationStatus",
  "url" : "http://smart.who.int/base/CodeSystem/KGPublicationStatus",
  "version" : "0.3.0",
  "name" : "KGPublicationStatus",
  "title" : "Knowledge graph L2: publication status",
  "status" : "active",
  "experimental" : false,
  "date" : "2026-11-19T20:24:57+00:00",
  "publisher" : "WHO",
  "contact" : [{
    "name" : "WHO",
    "telecom" : [{
      "system" : "url",
      "value" : "http://who.int"
    }]
  }],
  "description" : "FHIR PublicationStatus, which DAK.fsh's status and every L3 resource's status take. Added by the smart-base migration: smart-kg named these properties without binding them. Source: smart-kg ontology/l2/l2.json valueSets \"publication-status\"; http://hl7.org/fhir/ValueSet/publication-status.",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 4,
  "concept" : [{
    "code" : "draft",
    "display" : "Draft",
    "definition" : "This resource is still under development and is not yet considered to be ready for normal use."
  },
  {
    "code" : "active",
    "display" : "Active",
    "definition" : "This resource is ready for normal use."
  },
  {
    "code" : "retired",
    "display" : "Retired",
    "definition" : "This resource has been withdrawn or superseded and should no longer be used."
  },
  {
    "code" : "unknown",
    "display" : "Unknown",
    "definition" : "The authoring system does not know which of the status values currently applies for this resource."
  }]
}

```
