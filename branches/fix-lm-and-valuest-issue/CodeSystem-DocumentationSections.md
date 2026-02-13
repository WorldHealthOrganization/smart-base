# Smart Guidelines Documentation Section - SMART Base v0.2.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Smart Guidelines Documentation Section**

## CodeSystem: Smart Guidelines Documentation Section (Experimental) 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/DocumentationSections | *Version*:0.2.0 |
| Active as of 2025-10-09 | *Computable Name*:DocumentationSections |

 
CodeSystem for Smart Guidelines Documentation Section to autogenerate documentation from artifacts 

 This Code system is referenced in the content logical definition of the following value sets: 

* This CodeSystem is not used here; it may be used elsewhere (e.g. specifications and/or implementations that use this content)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "DocumentationSections",
  "url" : "http://smart.who.int/base/CodeSystem/DocumentationSections",
  "version" : "0.2.0",
  "name" : "DocumentationSections",
  "title" : "Smart Guidelines Documentation Section",
  "status" : "active",
  "experimental" : true,
  "date" : "2025-10-09T20:42:55+00:00",
  "publisher" : "WHO",
  "contact" : [
    {
      "name" : "WHO",
      "telecom" : [
        {
          "system" : "url",
          "value" : "http://who.int"
        }
      ]
    }
  ],
  "description" : "CodeSystem for Smart Guidelines Documentation Section to autogenerate documentation from artifacts",
  "caseSensitive" : false,
  "content" : "complete",
  "count" : 7,
  "concept" : [
    {
      "code" : "request-trigger",
      "display" : "Request Trigger Events"
    },
    {
      "code" : "request-semantics",
      "display" : "Request Message Semantics"
    },
    {
      "code" : "request-actions",
      "display" : "Request Expected Actions"
    },
    {
      "code" : "response-trigger",
      "display" : "Response Trigger Events"
    },
    {
      "code" : "response-semantics",
      "display" : "Response Message Semantics"
    },
    {
      "code" : "response-actions",
      "display" : "Response Expected Actions"
    },
    {
      "code" : "security-considerations",
      "display" : "Security Considerations"
    }
  ]
}

```
