Logical: Transaction
Id: Transaction
Parent: Interaction
Title: "Transaction"
Description: """A system-to-system technical exchange contract, extending the Interaction model. 
Adds the technical details needed to describe data exchanges between systems: exchange pattern, 
transport protocol, payload specifications, security requirements, and relationships to other 
transactions. This model is technology-agnostic — it can describe exchanges based on FHIR, 
HL7 v2, CDA, DICOM, X12, SOAP, or any other standard."""

* ^status = #draft
* ^version = "0.1.0"

// Constrain inherited type to system-to-system
* type = #system-to-system

// Exchange classification
* direction 1..1 code "Whether the data consumer (pull) or data source (push) initiates the data flow."
* direction from TransactionDirectionVS (required)
* exchangePattern 1..1 code "The broad architectural pattern (e.g., request-response, messaging, document, publish-subscribe)."
* exchangePattern from ExchangePatternVS (required)
* transportProtocol 0..* code "The transport protocol(s) that may carry this exchange (e.g., HTTP, SOAP, MLLP)."
* transportProtocol from TransportProtocolVS (extensible)
* synchronicity 0..1 code "Whether the exchange completes synchronously or asynchronously."
* synchronicity from SynchronicityVS (required)

// Referenced specifications
* standard 0..* BackboneElement "Specifications, implementation guides, or standards that govern this transaction."
  * url 1..1 url "The URL or identifier of the specification (e.g., an IHE profile URL, a FHIR IG canonical, an RFC, a standard number)."
  * version 0..1 string "The version of the referenced specification."
  * description 0..1 markdown "How this specification applies to the transaction — what is adopted, adapted, or constrained."
  * conformance 0..1 code "How binding this standard is for the transaction."
  * conformance from ConformanceVS (required)
  * constraint 0..* markdown "Specific constraints or restrictions applied to the base standard in this transaction."

// Payload — the request/response backbones are inherited from Interaction;
// Transaction adds the technical details that describe them on the wire.
* request.profile 0..* url "Profile(s) or schema(s) the request payload must conform to (e.g., FHIR StructureDefinition URL, CDA template OID, v2 message structure, XSD URL)."
* request.contentType 0..1 string "The content type or format of the request payload (e.g., a FHIR resource type, a MIME type, a v2 message type like ADT^A01)."

* response.trigger 0..1 string "What triggers the response — typically receipt of the request, but may differ in asynchronous or event-driven patterns (e.g., 'when a matching result becomes available')."
* response.profile 0..* url "Profile(s) or schema(s) the response payload must conform to."
* response.contentType 0..1 string "The content type or format of the response payload."

// Security
* security 0..* BackboneElement "Security requirements for this transaction."
  * mechanism 1..1 code "The category of security mechanism (e.g., transport, authentication, authorization, audit)."
  * mechanism from SecurityMechanismTypeVS (extensible)
  * description 0..1 markdown "Human-readable description of the specific security requirements."
  * profile 0..* url "Reference to a security specification or profile that applies (e.g., IHE IUA, SMART App Launch, IHE ATNA/BALP, WS-Security policy)."

// Relationships
* relatedTransaction 0..* BackboneElement "Relationships to other transactions (e.g., subscription setup, workflow sequencing)."
  * transaction 1..1 Reference(Transaction) "The related transaction."
  * relationship 1..1 code "The nature of the relationship."
  * relationship from TransactionRelationshipTypeVS (required)
