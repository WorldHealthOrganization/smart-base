CodeSystem: InteractionTypeCS
Id: interaction-type
Title: "Interaction Type"
Description: "The type of actors involved in an interaction."
* ^status = #draft
* ^caseSensitive = true
* #user-to-system "User to System" "A human actor initiates an exchange with a system."
* #system-to-user "System to User" "A system initiates an exchange directed at a human actor."
* #system-to-system "System to System" "An exchange between two systems with no human involvement."
* #user-to-user "User to User" "An exchange between two human actors, mediated by systems."

CodeSystem: ParticipantRoleCS
Id: participant-role
Title: "Participant Role"
Description: "The role of an additional participant in an interaction."
* ^status = #draft
* ^caseSensitive = true
* #gateway "Gateway" "An intermediary that bridges between networks or domains (e.g., XCA gateway, national contact point)."
* #broker "Broker" "A routing or orchestration intermediary (e.g., message broker, integration engine, central services hub)."
* #proxy "Proxy" "A transparent intermediary acting on behalf of the initiator or responder."
* #observer "Observer" "An actor that receives information about the interaction without affecting it (e.g., audit repository)."
* #authz-server "Authorization Server" "An actor that provides authorization decisions or tokens."
* #fulfiller "Fulfiller" "An actor (often human) that performs the action requested by the interaction."
* #validator "Validator" "An actor that validates content or identity during the interaction."

CodeSystem: ExchangePatternCS
Id: exchange-pattern
Title: "Exchange Pattern"
Description: "The broad architectural pattern of the data exchange, independent of technology or standard."
* ^status = #draft
* ^caseSensitive = true
* #request-response "Request-Response" "A synchronous or asynchronous pattern where one party sends a request and expects a response (e.g., REST API call, SOAP request, HL7 v2 query)."
* #query "Query" "A pattern where the consumer searches or queries the source for data matching specific criteria."
* #messaging "Messaging" "Exchange of discrete messages between systems, typically through a messaging infrastructure (e.g., HL7 v2 messages, FHIR messaging, EDIFACT)."
* #document "Document" "Exchange of self-contained, human-readable documents that package related information (e.g., CDA documents, FHIR documents, PDF reports)."
* #publish-subscribe "Publish-Subscribe" "An event-driven pattern where a consumer registers interest and the source pushes notifications when relevant events occur."
* #event-notification "Event Notification" "A source pushes unsolicited notifications about events to one or more consumers, without prior subscription."
* #batch "Batch" "A collection of independent operations submitted together for efficiency."

CodeSystem: TransportProtocolCS
Id: transport-protocol
Title: "Transport Protocol"
Description: "The transport protocol or mechanism used to carry the exchange."
* ^status = #draft
* ^caseSensitive = true
* #http "HTTP/REST" "Exchange over HTTP or HTTPS using RESTful conventions."
* #soap "SOAP" "Exchange using SOAP web services."
* #mllp "MLLP" "Minimal Lower Layer Protocol, used for HL7 v2 messaging."
* #smtp "SMTP" "Exchange via email (e.g., Direct messaging)."
* #ftp "FTP/SFTP" "File-based exchange via FTP or SFTP."
* #dicom "DICOM" "DICOM network protocol for imaging exchange."
* #websocket "WebSocket" "Persistent bidirectional connection."
* #amqp "AMQP" "Advanced Message Queuing Protocol."
* #kafka "Kafka" "Event streaming via Apache Kafka or similar platforms."
* #filesystem "File System" "Exchange via shared file system or media."

CodeSystem: TransactionDirectionCS
Id: transaction-direction
Title: "Transaction Direction"
Description: "Whether the data consumer or data source initiates the data flow."
* ^status = #draft
* ^caseSensitive = true
* #pull "Pull" "The data consumer initiates the exchange to retrieve data from the source."
* #push "Push" "The data source initiates the exchange to send data to the consumer."

CodeSystem: SynchronicityCS
Id: synchronicity
Title: "Synchronicity"
Description: "Whether the exchange completes synchronously or asynchronously."
* ^status = #draft
* ^caseSensitive = true
* #synchronous "Synchronous" "The response is returned within the same connection or session."
* #asynchronous "Asynchronous" "The response is returned separately, via callback, polling, or a different channel."

CodeSystem: SecurityMechanismTypeCS
Id: security-mechanism-type
Title: "Security Mechanism Type"
Description: "The category of security mechanism required for a transaction."
* ^status = #draft
* ^caseSensitive = true
* #transport "Transport Security" "Security at the transport layer (e.g., TLS, mTLS)."
* #authentication "Authentication" "Verification of actor identity."
* #authorization "Authorization" "Access control and scope enforcement."
* #audit "Audit" "Logging and audit trail requirements."
* #consent "Consent" "Patient or user consent enforcement."

CodeSystem: TransactionRelationshipTypeCS
Id: transaction-relationship-type
Title: "Transaction Relationship Type"
Description: "The nature of the relationship between two transactions."
* ^status = #draft
* ^caseSensitive = true
* #setup "Setup" "The related transaction must be completed before this one (e.g., subscription registration before notification delivery)."
* #follows "Follows" "This transaction typically follows the related one in a workflow."
* #triggers "Triggers" "Completion of the related transaction triggers this one."
* #alternative "Alternative" "The related transaction is an alternative approach to achieve the same goal."

CodeSystem: ConformanceCS
Id: conformance
Title: "Conformance Level"
Description: "How binding a referenced standard is for a transaction."
* ^status = #draft
* ^caseSensitive = true
* #required "Required" "The transaction must conform to this standard."
* #recommended "Recommended" "The transaction should conform to this standard."
* #optional "Optional" "The transaction may conform to this standard."
