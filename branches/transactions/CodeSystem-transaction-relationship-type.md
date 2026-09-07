# Transaction Relationship Type - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Transaction Relationship Type**

## CodeSystem: Transaction Relationship Type 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/transaction-relationship-type | *Version*:0.3.0 |
| Draft as of 2026-09-07 | *Computable Name*:TransactionRelationshipTypeCS |

 
The nature of the relationship between two transactions. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Transaction Relationship Type](ValueSet-transaction-relationship-type.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "transaction-relationship-type",
  "url" : "http://smart.who.int/base/CodeSystem/transaction-relationship-type",
  "version" : "0.3.0",
  "name" : "TransactionRelationshipTypeCS",
  "title" : "Transaction Relationship Type",
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
  "description" : "The nature of the relationship between two transactions.",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 4,
  "concept" : [{
    "code" : "setup",
    "display" : "Setup",
    "definition" : "The related transaction must be completed before this one (e.g., subscription registration before notification delivery)."
  },
  {
    "code" : "follows",
    "display" : "Follows",
    "definition" : "This transaction typically follows the related one in a workflow."
  },
  {
    "code" : "triggers",
    "display" : "Triggers",
    "definition" : "Completion of the related transaction triggers this one."
  },
  {
    "code" : "alternative",
    "display" : "Alternative",
    "definition" : "The related transaction is an alternative approach to achieve the same goal."
  }]
}

```
