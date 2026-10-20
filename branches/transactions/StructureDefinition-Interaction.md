# Interaction - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Interaction**

## Logical Model: Interaction 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/Interaction | *Version*:0.3.0 |
| Draft as of 2026-09-07 | *Computable Name*:Interaction |

 
A logical model representing an exchange between actors. This is the base model for all interactions, including user-to-system, system-to-user, system-to-system, and user-to-user exchanges. The Transaction logical model extends this for system-to-system technical contracts. 

**Usages:**

* Derived from this Logical Model: [Transaction](StructureDefinition-Transaction.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-Interaction.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-Interaction.csv), [Excel](StructureDefinition-Interaction.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Interaction",
  "url" : "http://smart.who.int/base/StructureDefinition/Interaction",
  "version" : "0.3.0",
  "name" : "Interaction",
  "title" : "Interaction",
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
  "description" : "A logical model representing an exchange between actors. \nThis is the base model for all interactions, including user-to-system, system-to-user, \nsystem-to-system, and user-to-user exchanges. The Transaction logical model extends \nthis for system-to-system technical contracts.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/Interaction",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Interaction",
      "path" : "Interaction",
      "short" : "Interaction",
      "definition" : "A logical model representing an exchange between actors. \nThis is the base model for all interactions, including user-to-system, system-to-user, \nsystem-to-system, and user-to-user exchanges. The Transaction logical model extends \nthis for system-to-system technical contracts."
    },
    {
      "id" : "Interaction.identifier",
      "path" : "Interaction.identifier",
      "short" : "Unique identifier(s) for this interaction definition.",
      "definition" : "Unique identifier(s) for this interaction definition.",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "Identifier"
      }]
    },
    {
      "id" : "Interaction.name",
      "path" : "Interaction.name",
      "short" : "A short human-readable label for the interaction (e.g., 'Patient Demographics Query').",
      "definition" : "A short human-readable label for the interaction (e.g., 'Patient Demographics Query').",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Interaction.title",
      "path" : "Interaction.title",
      "short" : "A display title for the interaction.",
      "definition" : "A display title for the interaction.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Interaction.description",
      "path" : "Interaction.description",
      "short" : "A human-readable description of what this interaction accomplishes.",
      "definition" : "A human-readable description of what this interaction accomplishes.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "Interaction.type",
      "path" : "Interaction.type",
      "short" : "The type of actors involved.",
      "definition" : "The type of actors involved.",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://smart.who.int/base/ValueSet/interaction-type"
      }
    },
    {
      "id" : "Interaction.status",
      "path" : "Interaction.status",
      "short" : "The publication status of this interaction definition.",
      "definition" : "The publication status of this interaction definition.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://hl7.org/fhir/ValueSet/publication-status"
      }
    },
    {
      "id" : "Interaction.date",
      "path" : "Interaction.date",
      "short" : "The date this interaction definition was last changed.",
      "definition" : "The date this interaction definition was last changed.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "dateTime"
      }]
    },
    {
      "id" : "Interaction.purpose",
      "path" : "Interaction.purpose",
      "short" : "Why this interaction is defined — the business or clinical need it addresses.",
      "definition" : "Why this interaction is defined — the business or clinical need it addresses.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "Interaction.initiator",
      "path" : "Interaction.initiator",
      "short" : "The actor that triggers the interaction (logical source).",
      "definition" : "The actor that triggers the interaction (logical source).",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "Reference",
        "targetProfile" : ["http://hl7.org/fhir/StructureDefinition/ActorDefinition"]
      }]
    },
    {
      "id" : "Interaction.responder",
      "path" : "Interaction.responder",
      "short" : "The actor that receives and responds to the interaction (logical endpoint).",
      "definition" : "The actor that receives and responds to the interaction (logical endpoint).",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "Reference",
        "targetProfile" : ["http://hl7.org/fhir/StructureDefinition/ActorDefinition"]
      }]
    },
    {
      "id" : "Interaction.participant",
      "path" : "Interaction.participant",
      "short" : "Additional actors involved in the interaction beyond initiator and responder.",
      "definition" : "Additional actors involved in the interaction beyond initiator and responder.",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "BackboneElement"
      }]
    },
    {
      "id" : "Interaction.participant.actor",
      "path" : "Interaction.participant.actor",
      "short" : "The participant actor.",
      "definition" : "The participant actor.",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "Reference",
        "targetProfile" : ["http://hl7.org/fhir/StructureDefinition/ActorDefinition"]
      }]
    },
    {
      "id" : "Interaction.participant.role",
      "path" : "Interaction.participant.role",
      "short" : "The role this participant plays in the interaction.",
      "definition" : "The role this participant plays in the interaction.",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "extensible",
        "valueSet" : "http://smart.who.int/base/ValueSet/participant-role"
      }
    },
    {
      "id" : "Interaction.participant.position",
      "path" : "Interaction.participant.position",
      "short" : "Order in a sequential chain of intermediaries (1-based). Used when multiple participants form an ordered path between initiator and responder.",
      "definition" : "Order in a sequential chain of intermediaries (1-based). Used when multiple participants form an ordered path between initiator and responder.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "integer"
      }]
    },
    {
      "id" : "Interaction.participant.description",
      "path" : "Interaction.participant.description",
      "short" : "What this participant does in the context of this specific interaction.",
      "definition" : "What this participant does in the context of this specific interaction.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Interaction.trigger",
      "path" : "Interaction.trigger",
      "short" : "A description of the event or condition that initiates this interaction.",
      "definition" : "A description of the event or condition that initiates this interaction.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Interaction.preCondition",
      "path" : "Interaction.preCondition",
      "short" : "Conditions that must be true before this interaction can occur.",
      "definition" : "Conditions that must be true before this interaction can occur.",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Interaction.postCondition",
      "path" : "Interaction.postCondition",
      "short" : "Conditions that are expected to be true after this interaction completes successfully.",
      "definition" : "Conditions that are expected to be true after this interaction completes successfully.",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Interaction.request",
      "path" : "Interaction.request",
      "short" : "The outbound payload — what the initiator supplies.",
      "definition" : "The outbound payload — what the initiator supplies.",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "BackboneElement"
      }]
    },
    {
      "id" : "Interaction.request.description",
      "path" : "Interaction.request.description",
      "short" : "A human-readable description of the request — the semantics of what is supplied, including what a human actor is expected to enter.",
      "definition" : "A human-readable description of the request — the semantics of what is supplied, including what a human actor is expected to enter.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "Interaction.response",
      "path" : "Interaction.response",
      "short" : "The return payload — what the responder returns. Absent for fire-and-forget patterns.",
      "definition" : "The return payload — what the responder returns. Absent for fire-and-forget patterns.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "BackboneElement"
      }]
    },
    {
      "id" : "Interaction.response.description",
      "path" : "Interaction.response.description",
      "short" : "A human-readable description of the response — the semantics of what is returned.",
      "definition" : "A human-readable description of the response — the semantics of what is returned.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "Interaction.semantics",
      "path" : "Interaction.semantics",
      "short" : "The processing semantics of the interaction — what actors do during the exchange, beyond what is expressed in pre/postConditions and the payload structure.",
      "definition" : "The processing semantics of the interaction — what actors do during the exchange, beyond what is expressed in pre/postConditions and the payload structure.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "BackboneElement"
      }]
    },
    {
      "id" : "Interaction.semantics.description",
      "path" : "Interaction.semantics.description",
      "short" : "Overall narrative description of the processing semantics.",
      "definition" : "Overall narrative description of the processing semantics.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "Interaction.semantics.actorBehavior",
      "path" : "Interaction.semantics.actorBehavior",
      "short" : "The expected behavior of a specific actor during this interaction.",
      "definition" : "The expected behavior of a specific actor during this interaction.",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "BackboneElement"
      }]
    },
    {
      "id" : "Interaction.semantics.actorBehavior.actor",
      "path" : "Interaction.semantics.actorBehavior.actor",
      "short" : "The actor whose behavior is described.",
      "definition" : "The actor whose behavior is described.",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "Reference",
        "targetProfile" : ["http://hl7.org/fhir/StructureDefinition/ActorDefinition"]
      }]
    },
    {
      "id" : "Interaction.semantics.actorBehavior.expectation",
      "path" : "Interaction.semantics.actorBehavior.expectation",
      "short" : "What this actor is expected to do during the interaction (e.g., validate, cross-reference, transform, store, forward).",
      "definition" : "What this actor is expected to do during the interaction (e.g., validate, cross-reference, transform, store, forward).",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    }]
  }
}

```
