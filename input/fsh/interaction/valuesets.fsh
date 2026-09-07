ValueSet: InteractionTypeVS
Id: interaction-type
Title: "Interaction Type"
Description: "The type of actors involved in an interaction."
* ^status = #draft
* include codes from system InteractionTypeCS

ValueSet: ParticipantRoleVS
Id: participant-role
Title: "Participant Role"
Description: "The role of an additional participant in an interaction."
* ^status = #draft
* include codes from system ParticipantRoleCS

ValueSet: ExchangePatternVS
Id: exchange-pattern
Title: "Exchange Pattern"
Description: "The broad architectural pattern of the data exchange."
* ^status = #draft
* include codes from system ExchangePatternCS

ValueSet: TransportProtocolVS
Id: transport-protocol
Title: "Transport Protocol"
Description: "The transport protocol or mechanism used to carry the exchange."
* ^status = #draft
* include codes from system TransportProtocolCS

ValueSet: TransactionDirectionVS
Id: transaction-direction
Title: "Transaction Direction"
Description: "Whether the data consumer or data source initiates the data flow."
* ^status = #draft
* include codes from system TransactionDirectionCS

ValueSet: SynchronicityVS
Id: synchronicity
Title: "Synchronicity"
Description: "Whether the exchange completes synchronously or asynchronously."
* ^status = #draft
* include codes from system SynchronicityCS

ValueSet: SecurityMechanismTypeVS
Id: security-mechanism-type
Title: "Security Mechanism Type"
Description: "The category of security mechanism."
* ^status = #draft
* include codes from system SecurityMechanismTypeCS

ValueSet: TransactionRelationshipTypeVS
Id: transaction-relationship-type
Title: "Transaction Relationship Type"
Description: "The nature of the relationship between two transactions."
* ^status = #draft
* include codes from system TransactionRelationshipTypeCS

ValueSet: ConformanceVS
Id: conformance
Title: "Conformance Level"
Description: "How binding a referenced standard is for a transaction."
* ^status = #draft
* include codes from system ConformanceCS
