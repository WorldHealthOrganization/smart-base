# Knowledge graph L1: identifier type - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L1: identifier type**

## CodeSystem: Knowledge graph L1: identifier type 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/KGIdentifierType | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGIdentifierType |

 
Which kind of identifier a publication carries. The first available, in this order, builds the publication IRI. url comes last: a web address is the least stable identifier and is used only for sources that have no other. Source: smart-kg ontology/l1/l1.json valueSets "identifier-type"; WHO IRIS practice; CDHIv2.fsh carries an ISBN. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Knowledge graph L1: identifier type](ValueSet-KGIdentifierTypeVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "KGIdentifierType",
  "url" : "http://smart.who.int/base/CodeSystem/KGIdentifierType",
  "version" : "0.3.0",
  "name" : "KGIdentifierType",
  "title" : "Knowledge graph L1: identifier type",
  "status" : "active",
  "experimental" : false,
  "date" : "2026-11-19T20:24:57+00:00",
  "publisher" : "WHO",
  "contact" : [{
    "name" : "WHO",
    "telecom" : [{
      "system" : "url",
      "value" : "http://who.int"
    }]
  }],
  "description" : "Which kind of identifier a publication carries. The first available, in this order, builds the publication IRI. url comes last: a web address is the least stable identifier and is used only for sources that have no other. Source: smart-kg ontology/l1/l1.json valueSets \"identifier-type\"; WHO IRIS practice; CDHIv2.fsh carries an ISBN.",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 6,
  "concept" : [{
    "code" : "isbn",
    "display" : "Isbn",
    "definition" : "ISBN-13, electronic version preferred."
  },
  {
    "code" : "iris-handle",
    "display" : "Iris handle",
    "definition" : "WHO IRIS handle, e.g. 10665/250796."
  },
  {
    "code" : "doi",
    "display" : "Doi",
    "definition" : "Digital Object Identifier."
  },
  {
    "code" : "issn",
    "display" : "Issn",
    "definition" : "ISSN, for serials such as the Weekly Epidemiological Record."
  },
  {
    "code" : "url",
    "display" : "Url",
    "definition" : "The canonical web address of a WHO source published only on the web, such as the routine immunization summary tables or the UHC Compendium. Used for the IRI only when no isbn, iris-handle, doi or issn exists; scheme, query and trailing slash are dropped. A moved page is a new publication, linked to the old one by supersedes."
  },
  {
    "code" : "other",
    "display" : "Other",
    "definition" : "Any other identifier; never used to build an IRI."
  }]
}

```
