# Participant Role - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Participant Role**

## CodeSystem: Participant Role 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/participant-role | *Version*:0.3.0 |
| Draft as of 2026-09-07 | *Computable Name*:ParticipantRoleCS |

 
The role of an additional participant in an interaction. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Participant Role](ValueSet-participant-role.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "participant-role",
  "url" : "http://smart.who.int/base/CodeSystem/participant-role",
  "version" : "0.3.0",
  "name" : "ParticipantRoleCS",
  "title" : "Participant Role",
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
  "description" : "The role of an additional participant in an interaction.",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 7,
  "concept" : [{
    "code" : "gateway",
    "display" : "Gateway",
    "definition" : "An intermediary that bridges between networks or domains (e.g., XCA gateway, national contact point)."
  },
  {
    "code" : "broker",
    "display" : "Broker",
    "definition" : "A routing or orchestration intermediary (e.g., message broker, integration engine, central services hub)."
  },
  {
    "code" : "proxy",
    "display" : "Proxy",
    "definition" : "A transparent intermediary acting on behalf of the initiator or responder."
  },
  {
    "code" : "observer",
    "display" : "Observer",
    "definition" : "An actor that receives information about the interaction without affecting it (e.g., audit repository)."
  },
  {
    "code" : "authz-server",
    "display" : "Authorization Server",
    "definition" : "An actor that provides authorization decisions or tokens."
  },
  {
    "code" : "fulfiller",
    "display" : "Fulfiller",
    "definition" : "An actor (often human) that performs the action requested by the interaction."
  },
  {
    "code" : "validator",
    "display" : "Validator",
    "definition" : "An actor that validates content or identity during the interaction."
  }]
}

```
