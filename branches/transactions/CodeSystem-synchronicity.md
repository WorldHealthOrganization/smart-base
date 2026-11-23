# Synchronicity - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Synchronicity**

## CodeSystem: Synchronicity 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/synchronicity | *Version*:0.3.0 |
| Draft as of 2026-09-07 | *Computable Name*:SynchronicityCS |

 
Whether the exchange completes synchronously or asynchronously. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Synchronicity](ValueSet-synchronicity.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "synchronicity",
  "url" : "http://smart.who.int/base/CodeSystem/synchronicity",
  "version" : "0.3.0",
  "name" : "SynchronicityCS",
  "title" : "Synchronicity",
  "status" : "draft",
  "date" : "2026-09-07T06:11:01+00:00",
  "publisher" : "WHO",
  "contact" : [{
    "name" : "WHO",
    "telecom" : [{
      "system" : "url",
      "value" : "http://who.int"
    }]
  }],
  "description" : "Whether the exchange completes synchronously or asynchronously.",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 2,
  "concept" : [{
    "code" : "synchronous",
    "display" : "Synchronous",
    "definition" : "The response is returned within the same connection or session."
  },
  {
    "code" : "asynchronous",
    "display" : "Asynchronous",
    "definition" : "The response is returned separately, via callback, polling, or a different channel."
  }]
}

```
