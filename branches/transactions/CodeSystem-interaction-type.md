# Interaction Type - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Interaction Type**

## CodeSystem: Interaction Type 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/interaction-type | *Version*:0.3.0 |
| Draft as of 2026-09-07 | *Computable Name*:InteractionTypeCS |

 
The type of actors involved in an interaction. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Interaction Type](ValueSet-interaction-type.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "interaction-type",
  "url" : "http://smart.who.int/base/CodeSystem/interaction-type",
  "version" : "0.3.0",
  "name" : "InteractionTypeCS",
  "title" : "Interaction Type",
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
  "description" : "The type of actors involved in an interaction.",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 4,
  "concept" : [{
    "code" : "user-to-system",
    "display" : "User to System",
    "definition" : "A human actor initiates an exchange with a system."
  },
  {
    "code" : "system-to-user",
    "display" : "System to User",
    "definition" : "A system initiates an exchange directed at a human actor."
  },
  {
    "code" : "system-to-system",
    "display" : "System to System",
    "definition" : "An exchange between two systems with no human involvement."
  },
  {
    "code" : "user-to-user",
    "display" : "User to User",
    "definition" : "An exchange between two human actors, mediated by systems."
  }]
}

```
