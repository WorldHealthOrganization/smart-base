# Security Mechanism Type - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Security Mechanism Type**

## CodeSystem: Security Mechanism Type 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/security-mechanism-type | *Version*:0.3.0 |
| Draft as of 2026-09-07 | *Computable Name*:SecurityMechanismTypeCS |

 
The category of security mechanism required for a transaction. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Security Mechanism Type](ValueSet-security-mechanism-type.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "security-mechanism-type",
  "url" : "http://smart.who.int/base/CodeSystem/security-mechanism-type",
  "version" : "0.3.0",
  "name" : "SecurityMechanismTypeCS",
  "title" : "Security Mechanism Type",
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
  "description" : "The category of security mechanism required for a transaction.",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 5,
  "concept" : [{
    "code" : "transport",
    "display" : "Transport Security",
    "definition" : "Security at the transport layer (e.g., TLS, mTLS)."
  },
  {
    "code" : "authentication",
    "display" : "Authentication",
    "definition" : "Verification of actor identity."
  },
  {
    "code" : "authorization",
    "display" : "Authorization",
    "definition" : "Access control and scope enforcement."
  },
  {
    "code" : "audit",
    "display" : "Audit",
    "definition" : "Logging and audit trail requirements."
  },
  {
    "code" : "consent",
    "display" : "Consent",
    "definition" : "Patient or user consent enforcement."
  }]
}

```
