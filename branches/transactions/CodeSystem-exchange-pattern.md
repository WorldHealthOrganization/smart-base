# Exchange Pattern - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Exchange Pattern**

## CodeSystem: Exchange Pattern 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/exchange-pattern | *Version*:0.3.0 |
| Draft as of 2026-09-07 | *Computable Name*:ExchangePatternCS |

 
The broad architectural pattern of the data exchange, independent of technology or standard. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Exchange Pattern](ValueSet-exchange-pattern.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "exchange-pattern",
  "url" : "http://smart.who.int/base/CodeSystem/exchange-pattern",
  "version" : "0.3.0",
  "name" : "ExchangePatternCS",
  "title" : "Exchange Pattern",
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
  "description" : "The broad architectural pattern of the data exchange, independent of technology or standard.",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 7,
  "concept" : [{
    "code" : "request-response",
    "display" : "Request-Response",
    "definition" : "A synchronous or asynchronous pattern where one party sends a request and expects a response (e.g., REST API call, SOAP request, HL7 v2 query)."
  },
  {
    "code" : "query",
    "display" : "Query",
    "definition" : "A pattern where the consumer searches or queries the source for data matching specific criteria."
  },
  {
    "code" : "messaging",
    "display" : "Messaging",
    "definition" : "Exchange of discrete messages between systems, typically through a messaging infrastructure (e.g., HL7 v2 messages, FHIR messaging, EDIFACT)."
  },
  {
    "code" : "document",
    "display" : "Document",
    "definition" : "Exchange of self-contained, human-readable documents that package related information (e.g., CDA documents, FHIR documents, PDF reports)."
  },
  {
    "code" : "publish-subscribe",
    "display" : "Publish-Subscribe",
    "definition" : "An event-driven pattern where a consumer registers interest and the source pushes notifications when relevant events occur."
  },
  {
    "code" : "event-notification",
    "display" : "Event Notification",
    "definition" : "A source pushes unsolicited notifications about events to one or more consumers, without prior subscription."
  },
  {
    "code" : "batch",
    "display" : "Batch",
    "definition" : "A collection of independent operations submitted together for efficiency."
  }]
}

```
