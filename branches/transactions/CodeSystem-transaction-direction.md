# Transaction Direction - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Transaction Direction**

## CodeSystem: Transaction Direction 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/transaction-direction | *Version*:0.3.0 |
| Draft as of 2026-09-07 | *Computable Name*:TransactionDirectionCS |

 
Whether the data consumer or data source initiates the data flow. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Transaction Direction](ValueSet-transaction-direction.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "transaction-direction",
  "url" : "http://smart.who.int/base/CodeSystem/transaction-direction",
  "version" : "0.3.0",
  "name" : "TransactionDirectionCS",
  "title" : "Transaction Direction",
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
  "description" : "Whether the data consumer or data source initiates the data flow.",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 2,
  "concept" : [{
    "code" : "pull",
    "display" : "Pull",
    "definition" : "The data consumer initiates the exchange to retrieve data from the source."
  },
  {
    "code" : "push",
    "display" : "Push",
    "definition" : "The data source initiates the exchange to send data to the consumer."
  }]
}

```
