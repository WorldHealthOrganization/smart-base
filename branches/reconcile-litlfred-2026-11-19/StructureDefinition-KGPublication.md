# Knowledge graph L1: Publication - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L1: Publication**

## Logical Model: Knowledge graph L1: Publication 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGPublication | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGPublication |

 
A WHO publication: a guideline of any of the handbook's types, a position paper, a summary table, a classification, implementation guidance, or a supplement. Metadata follows Dublin Core. identifiers is a list of {type, value}; type is from identifier-type, and the first of isbn, iris-handle, doi, issn, url builds the IRI, so an edition change is a new publication. issued and modified are Dublin Core. reviewBy is the handbook's review-by date (§12.5.1). sha256 pins the PDF. Derives from DublinCore (smart-base input/fsh/models/DublinCore.fsh); title, creator, publisher, language, rights are its elements. Class IRI: http://smart.who.int/kg/publication. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGPublication.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGPublication.csv), [Excel](StructureDefinition-KGPublication.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGPublication",
  "url" : "http://smart.who.int/base/StructureDefinition/KGPublication",
  "version" : "0.3.0",
  "name" : "KGPublication",
  "title" : "Knowledge graph L1: Publication",
  "status" : "active",
  "date" : "2026-11-23T18:43:32+00:00",
  "publisher" : "WHO",
  "contact" : [{
    "name" : "WHO",
    "telecom" : [{
      "system" : "url",
      "value" : "http://who.int"
    }]
  }],
  "description" : "A WHO publication: a guideline of any of the handbook's types, a position paper, a summary table, a classification, implementation guidance, or a supplement. Metadata follows Dublin Core. identifiers is a list of {type, value}; type is from identifier-type, and the first of isbn, iris-handle, doi, issn, url builds the IRI, so an edition change is a new publication. issued and modified are Dublin Core. reviewBy is the handbook's review-by date (§12.5.1). sha256 pins the PDF. Derives from DublinCore (smart-base input/fsh/models/DublinCore.fsh); title, creator, publisher, language, rights are its elements. Class IRI: http://smart.who.int/kg/publication.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGPublication",
  "baseDefinition" : "http://smart.who.int/base/StructureDefinition/DublinCore",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGPublication",
      "path" : "KGPublication",
      "short" : "Knowledge graph L1: Publication",
      "definition" : "A WHO publication: a guideline of any of the handbook's types, a position paper, a summary table, a classification, implementation guidance, or a supplement. Metadata follows Dublin Core. identifiers is a list of {type, value}; type is from identifier-type, and the first of isbn, iris-handle, doi, issn, url builds the IRI, so an edition change is a new publication. issued and modified are Dublin Core. reviewBy is the handbook's review-by date (§12.5.1). sha256 pins the PDF. Derives from DublinCore (smart-base input/fsh/models/DublinCore.fsh); title, creator, publisher, language, rights are its elements. Class IRI: http://smart.who.int/kg/publication."
    },
    {
      "id" : "KGPublication.issued",
      "path" : "KGPublication.issued",
      "short" : "Issued",
      "definition" : "Dublin Core dcterms:issued — date of formal issuance (YYYY, YYYY-MM or YYYY-MM-DD).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "date"
      }]
    },
    {
      "id" : "KGPublication.modified",
      "path" : "KGPublication.modified",
      "short" : "Modified",
      "definition" : "Dublin Core dcterms:modified — date the publication was changed.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "date"
      }]
    },
    {
      "id" : "KGPublication.version",
      "path" : "KGPublication.version",
      "short" : "Version",
      "definition" : "Edition or version, as printed.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGPublication.identifiers",
      "path" : "KGPublication.identifiers",
      "short" : "Identifiers",
      "definition" : "Typed identifiers; the first of isbn, iris-handle, doi, issn, url builds the IRI.",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "BackboneElement"
      }]
    },
    {
      "id" : "KGPublication.identifiers.type",
      "path" : "KGPublication.identifiers.type",
      "short" : "Type",
      "definition" : "The identifier's kind.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://smart.who.int/base/ValueSet/KGIdentifierTypeVS"
      }
    },
    {
      "id" : "KGPublication.identifiers.value",
      "path" : "KGPublication.identifiers.value",
      "short" : "Value",
      "definition" : "The identifier, as printed.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGPublication.url",
      "path" : "KGPublication.url",
      "short" : "URL",
      "definition" : "Where the publication is published.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGPublication.sha256",
      "path" : "KGPublication.sha256",
      "short" : "SHA-256",
      "definition" : "Hash of the PDF; pins the source.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGPublication.publicationType",
      "path" : "KGPublication.publicationType",
      "short" : "Publication type",
      "definition" : "What kind of publication this is.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://smart.who.int/base/ValueSet/KGPublicationTypeVS"
      }
    },
    {
      "id" : "KGPublication.grcStatus",
      "path" : "KGPublication.grcStatus",
      "short" : "Grc status",
      "definition" : "Whether the Guideline Review Committee approved the publication.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://smart.who.int/base/ValueSet/KGGrcStatusVS"
      }
    },
    {
      "id" : "KGPublication.reviewBy",
      "path" : "KGPublication.reviewBy",
      "short" : "Review by",
      "definition" : "The handbook's review-by date (§12.5.1).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "date"
      }]
    }]
  }
}

```
