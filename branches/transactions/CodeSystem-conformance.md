# Conformance Level - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Conformance Level**

## CodeSystem: Conformance Level 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/conformance | *Version*:0.3.0 |
| Draft as of 2026-09-07 | *Computable Name*:ConformanceCS |

 
How binding a referenced standard is for a transaction. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Conformance Level](ValueSet-conformance.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "conformance",
  "url" : "http://smart.who.int/base/CodeSystem/conformance",
  "version" : "0.3.0",
  "name" : "ConformanceCS",
  "title" : "Conformance Level",
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
  "description" : "How binding a referenced standard is for a transaction.",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 3,
  "concept" : [{
    "code" : "required",
    "display" : "Required",
    "definition" : "The transaction must conform to this standard."
  },
  {
    "code" : "recommended",
    "display" : "Recommended",
    "definition" : "The transaction should conform to this standard."
  },
  {
    "code" : "optional",
    "display" : "Optional",
    "definition" : "The transaction may conform to this standard."
  }]
}

```
