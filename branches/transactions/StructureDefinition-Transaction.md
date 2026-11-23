# Transaction - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Transaction**

## Logical Model: Transaction 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/Transaction | *Version*:0.3.0 |
| Draft as of 2026-09-07 | *Computable Name*:Transaction |

 
A system-to-system technical exchange contract, extending the Interaction model. Adds the technical details needed to describe data exchanges between systems: exchange pattern, transport protocol, payload specifications, security requirements, and relationships to other transactions. This model is technology-agnostic — it can describe exchanges based on FHIR, HL7 v2, CDA, DICOM, X12, SOAP, or any other standard. 

**Usages:**

* Refer to this Logical Model: [Transaction](StructureDefinition-Transaction.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-Transaction.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-Transaction.csv), [Excel](StructureDefinition-Transaction.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "Transaction",
  "url" : "http://smart.who.int/base/StructureDefinition/Transaction",
  "version" : "0.3.0",
  "name" : "Transaction",
  "title" : "Transaction",
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
  "description" : "A system-to-system technical exchange contract, extending the Interaction model. \nAdds the technical details needed to describe data exchanges between systems: exchange pattern, \ntransport protocol, payload specifications, security requirements, and relationships to other \ntransactions. This model is technology-agnostic — it can describe exchanges based on FHIR, \nHL7 v2, CDA, DICOM, X12, SOAP, or any other standard.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/Transaction",
  "baseDefinition" : "http://smart.who.int/base/StructureDefinition/Interaction",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "Transaction",
      "path" : "Transaction",
      "short" : "Transaction",
      "definition" : "A system-to-system technical exchange contract, extending the Interaction model. \nAdds the technical details needed to describe data exchanges between systems: exchange pattern, \ntransport protocol, payload specifications, security requirements, and relationships to other \ntransactions. This model is technology-agnostic — it can describe exchanges based on FHIR, \nHL7 v2, CDA, DICOM, X12, SOAP, or any other standard."
    },
    {
      "id" : "Transaction.type",
      "path" : "Transaction.type",
      "patternCode" : "system-to-system"
    },
    {
      "id" : "Transaction.request.profile",
      "path" : "Transaction.request.profile",
      "short" : "Profile(s) or schema(s) the request payload must conform to (e.g., FHIR StructureDefinition URL, CDA template OID, v2 message structure, XSD URL).",
      "definition" : "Profile(s) or schema(s) the request payload must conform to (e.g., FHIR StructureDefinition URL, CDA template OID, v2 message structure, XSD URL).",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "url"
      }]
    },
    {
      "id" : "Transaction.request.contentType",
      "path" : "Transaction.request.contentType",
      "short" : "The content type or format of the request payload (e.g., a FHIR resource type, a MIME type, a v2 message type like ADT^A01).",
      "definition" : "The content type or format of the request payload (e.g., a FHIR resource type, a MIME type, a v2 message type like ADT^A01).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Transaction.response.trigger",
      "path" : "Transaction.response.trigger",
      "short" : "What triggers the response — typically receipt of the request, but may differ in asynchronous or event-driven patterns (e.g., 'when a matching result becomes available').",
      "definition" : "What triggers the response — typically receipt of the request, but may differ in asynchronous or event-driven patterns (e.g., 'when a matching result becomes available').",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Transaction.response.profile",
      "path" : "Transaction.response.profile",
      "short" : "Profile(s) or schema(s) the response payload must conform to.",
      "definition" : "Profile(s) or schema(s) the response payload must conform to.",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "url"
      }]
    },
    {
      "id" : "Transaction.response.contentType",
      "path" : "Transaction.response.contentType",
      "short" : "The content type or format of the response payload.",
      "definition" : "The content type or format of the response payload.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Transaction.direction",
      "path" : "Transaction.direction",
      "short" : "Whether the data consumer (pull) or data source (push) initiates the data flow.",
      "definition" : "Whether the data consumer (pull) or data source (push) initiates the data flow.",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://smart.who.int/base/ValueSet/transaction-direction"
      }
    },
    {
      "id" : "Transaction.exchangePattern",
      "path" : "Transaction.exchangePattern",
      "short" : "The broad architectural pattern (e.g., request-response, messaging, document, publish-subscribe).",
      "definition" : "The broad architectural pattern (e.g., request-response, messaging, document, publish-subscribe).",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://smart.who.int/base/ValueSet/exchange-pattern"
      }
    },
    {
      "id" : "Transaction.transportProtocol",
      "path" : "Transaction.transportProtocol",
      "short" : "The transport protocol(s) that may carry this exchange (e.g., HTTP, SOAP, MLLP).",
      "definition" : "The transport protocol(s) that may carry this exchange (e.g., HTTP, SOAP, MLLP).",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "extensible",
        "valueSet" : "http://smart.who.int/base/ValueSet/transport-protocol"
      }
    },
    {
      "id" : "Transaction.synchronicity",
      "path" : "Transaction.synchronicity",
      "short" : "Whether the exchange completes synchronously or asynchronously.",
      "definition" : "Whether the exchange completes synchronously or asynchronously.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://smart.who.int/base/ValueSet/synchronicity"
      }
    },
    {
      "id" : "Transaction.standard",
      "path" : "Transaction.standard",
      "short" : "Specifications, implementation guides, or standards that govern this transaction.",
      "definition" : "Specifications, implementation guides, or standards that govern this transaction.",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "BackboneElement"
      }]
    },
    {
      "id" : "Transaction.standard.url",
      "path" : "Transaction.standard.url",
      "short" : "The URL or identifier of the specification (e.g., an IHE profile URL, a FHIR IG canonical, an RFC, a standard number).",
      "definition" : "The URL or identifier of the specification (e.g., an IHE profile URL, a FHIR IG canonical, an RFC, a standard number).",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "url"
      }]
    },
    {
      "id" : "Transaction.standard.version",
      "path" : "Transaction.standard.version",
      "short" : "The version of the referenced specification.",
      "definition" : "The version of the referenced specification.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "Transaction.standard.description",
      "path" : "Transaction.standard.description",
      "short" : "How this specification applies to the transaction — what is adopted, adapted, or constrained.",
      "definition" : "How this specification applies to the transaction — what is adopted, adapted, or constrained.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "Transaction.standard.conformance",
      "path" : "Transaction.standard.conformance",
      "short" : "How binding this standard is for the transaction.",
      "definition" : "How binding this standard is for the transaction.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://smart.who.int/base/ValueSet/conformance"
      }
    },
    {
      "id" : "Transaction.standard.constraint",
      "path" : "Transaction.standard.constraint",
      "short" : "Specific constraints or restrictions applied to the base standard in this transaction.",
      "definition" : "Specific constraints or restrictions applied to the base standard in this transaction.",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "Transaction.security",
      "path" : "Transaction.security",
      "short" : "Security requirements for this transaction.",
      "definition" : "Security requirements for this transaction.",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "BackboneElement"
      }]
    },
    {
      "id" : "Transaction.security.mechanism",
      "path" : "Transaction.security.mechanism",
      "short" : "The category of security mechanism (e.g., transport, authentication, authorization, audit).",
      "definition" : "The category of security mechanism (e.g., transport, authentication, authorization, audit).",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "extensible",
        "valueSet" : "http://smart.who.int/base/ValueSet/security-mechanism-type"
      }
    },
    {
      "id" : "Transaction.security.description",
      "path" : "Transaction.security.description",
      "short" : "Human-readable description of the specific security requirements.",
      "definition" : "Human-readable description of the specific security requirements.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "Transaction.security.profile",
      "path" : "Transaction.security.profile",
      "short" : "Reference to a security specification or profile that applies (e.g., IHE IUA, SMART App Launch, IHE ATNA/BALP, WS-Security policy).",
      "definition" : "Reference to a security specification or profile that applies (e.g., IHE IUA, SMART App Launch, IHE ATNA/BALP, WS-Security policy).",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "url"
      }]
    },
    {
      "id" : "Transaction.relatedTransaction",
      "path" : "Transaction.relatedTransaction",
      "short" : "Relationships to other transactions (e.g., subscription setup, workflow sequencing).",
      "definition" : "Relationships to other transactions (e.g., subscription setup, workflow sequencing).",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "BackboneElement"
      }]
    },
    {
      "id" : "Transaction.relatedTransaction.transaction",
      "path" : "Transaction.relatedTransaction.transaction",
      "short" : "The related transaction.",
      "definition" : "The related transaction.",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "Reference",
        "targetProfile" : ["http://smart.who.int/base/StructureDefinition/Transaction"]
      }]
    },
    {
      "id" : "Transaction.relatedTransaction.relationship",
      "path" : "Transaction.relatedTransaction.relationship",
      "short" : "The nature of the relationship.",
      "definition" : "The nature of the relationship.",
      "min" : 1,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://smart.who.int/base/ValueSet/transaction-relationship-type"
      }
    }]
  }
}

```
