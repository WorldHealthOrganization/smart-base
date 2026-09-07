Logical: Interaction
Id: Interaction
Title: "Interaction"
Description: """A logical model representing an exchange between actors. 
This is the base model for all interactions, including user-to-system, system-to-user, 
system-to-system, and user-to-user exchanges. The Transaction logical model extends 
this for system-to-system technical contracts."""

* ^status = #draft
* ^version = "0.1.0"

* identifier 0..* Identifier "Unique identifier(s) for this interaction definition."
* name 1..1 string "A short human-readable label for the interaction (e.g., 'Patient Demographics Query')."
* title 0..1 string "A display title for the interaction."
* description 0..1 markdown "A human-readable description of what this interaction accomplishes."
* type 1..1 code "The type of actors involved."
* type from InteractionTypeVS (required)
* status 0..1 code "The publication status of this interaction definition."
* status from http://hl7.org/fhir/ValueSet/publication-status (required)
* date 0..1 dateTime "The date this interaction definition was last changed."
* purpose 0..1 markdown "Why this interaction is defined — the business or clinical need it addresses."

* initiator 1..1 Reference(ActorDefinition) "The actor that triggers the interaction (logical source)."
* responder 1..1 Reference(ActorDefinition) "The actor that receives and responds to the interaction (logical endpoint)."

* participant 0..* BackboneElement "Additional actors involved in the interaction beyond initiator and responder."
  * actor 1..1 Reference(ActorDefinition) "The participant actor."
  * role 1..1 code "The role this participant plays in the interaction."
  * role from ParticipantRoleVS (extensible)
  * position 0..1 integer "Order in a sequential chain of intermediaries (1-based). Used when multiple participants form an ordered path between initiator and responder."
  * description 0..1 string "What this participant does in the context of this specific interaction."

* trigger 0..1 string "A description of the event or condition that initiates this interaction."
* preCondition 0..* string "Conditions that must be true before this interaction can occur."
* postCondition 0..* string "Conditions that are expected to be true after this interaction completes successfully."

* request 1..1 BackboneElement "The outbound payload — what the initiator supplies."
  * description 0..1 markdown "A human-readable description of the request — the semantics of what is supplied, including what a human actor is expected to enter."

* response 0..1 BackboneElement "The return payload — what the responder returns. Absent for fire-and-forget patterns."
  * description 0..1 markdown "A human-readable description of the response — the semantics of what is returned."

// An Interaction describes the exchange, not the data elements it carries, so the
// payloads are narrative here. Left commented out until there is a need to bind
// them to the data dictionary — this is the intended shape if that need arises,
// since it is what would let a user-to-system interaction distinguish the elements
// the user enters from those the system pre-populates or derives.
//
// * request.dataElement 0..* BackboneElement "The data conveyed, at dictionary level."
//   * element 1..1 Reference(CoreDataElement) "The data element conveyed."
//   * cardinality 0..1 string "Whether the element is required or optional in this interaction."
//   * provenance 0..1 code "How the value is obtained (user-entered, pre-populated, system-derived, device-captured)."
//   * guidance 0..1 markdown "Guidance on how the value is obtained in this interaction."
// * response.dataElement 0..* BackboneElement "The data returned, at dictionary level. Same shape as request.dataElement."

* semantics 0..1 BackboneElement "The processing semantics of the interaction — what actors do during the exchange, beyond what is expressed in pre/postConditions and the payload structure."
  * description 0..1 markdown "Overall narrative description of the processing semantics."
  * actorBehavior 0..* BackboneElement "The expected behavior of a specific actor during this interaction."
    * actor 1..1 Reference(ActorDefinition) "The actor whose behavior is described."
    * expectation 1..1 markdown "What this actor is expected to do during the interaction (e.g., validate, cross-reference, transform, store, forward)."
