# Knowledge graph L2: Digital Adaptation Kit - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L2: Digital Adaptation Kit**

## Logical Model: Knowledge graph L2: Digital Adaptation Kit 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGDak | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGDak |

 
The kit itself. Properties are exactly the metadata fields DAK.fsh declares and dak.json carries – no more, so that a dak node can be produced from a real file without anything being invented. canonicalUrl equals publicationUrl on a release branch and previewUrl on a development branch, per DAK.fsh. Both are kept because which one canonicalUrl currently equals is what says whether a graph describes a release or a build. Class IRI: http://smart.who.int/kg/dak. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGDak.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGDak.csv), [Excel](StructureDefinition-KGDak.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGDak",
  "url" : "http://smart.who.int/base/StructureDefinition/KGDak",
  "version" : "0.3.0",
  "name" : "KGDak",
  "title" : "Knowledge graph L2: Digital Adaptation Kit",
  "status" : "active",
  "date" : "2026-11-19T20:24:57+00:00",
  "publisher" : "WHO",
  "contact" : [{
    "name" : "WHO",
    "telecom" : [{
      "system" : "url",
      "value" : "http://who.int"
    }]
  }],
  "description" : "The kit itself. Properties are exactly the metadata fields DAK.fsh declares and dak.json carries -- no more, so that a dak node can be produced from a real file without anything being invented. canonicalUrl equals publicationUrl on a release branch and previewUrl on a development branch, per DAK.fsh. Both are kept because which one canonicalUrl currently equals is what says whether a graph describes a release or a build. Class IRI: http://smart.who.int/kg/dak.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGDak",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGDak",
      "path" : "KGDak",
      "short" : "Knowledge graph L2: Digital Adaptation Kit",
      "definition" : "The kit itself. Properties are exactly the metadata fields DAK.fsh declares and dak.json carries -- no more, so that a dak node can be produced from a real file without anything being invented. canonicalUrl equals publicationUrl on a release branch and previewUrl on a development branch, per DAK.fsh. Both are kept because which one canonicalUrl currently equals is what says whether a graph describes a release or a build. Class IRI: http://smart.who.int/kg/dak."
    },
    {
      "id" : "KGDak.id",
      "path" : "KGDak.id",
      "short" : "Id",
      "definition" : "The identifier the source declares (an FSH instance id, a BPMN or DMN element id).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDak.name",
      "path" : "KGDak.name",
      "short" : "Name",
      "definition" : "The computable name: the CamelCase identifier a Canonical() reference matches on.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDak.title",
      "path" : "KGDak.title",
      "short" : "Title",
      "definition" : "The human-readable title.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDak.description",
      "path" : "KGDak.description",
      "short" : "Description",
      "definition" : "A description, as the source gives it.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGDak.version",
      "path" : "KGDak.version",
      "short" : "Version",
      "definition" : "The business version, as declared.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDak.status",
      "path" : "KGDak.status",
      "short" : "Status",
      "definition" : "The DAK's publication status (DAK.fsh, FHIR PublicationStatus).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://smart.who.int/base/ValueSet/KGPublicationStatusVS"
      }
    },
    {
      "id" : "KGDak.publicationUrl",
      "path" : "KGDak.publicationUrl",
      "short" : "Publication URL",
      "definition" : "Where the DAK is published (DAK.fsh).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGDak.previewUrl",
      "path" : "KGDak.previewUrl",
      "short" : "Preview URL",
      "definition" : "Where the development build is previewed (DAK.fsh).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGDak.canonicalUrl",
      "path" : "KGDak.canonicalUrl",
      "short" : "Canonical URL",
      "definition" : "The canonical base; equals publicationUrl on a release branch and previewUrl on a development branch.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGDak.license",
      "path" : "KGDak.license",
      "short" : "License",
      "definition" : "The licence, as DAK.fsh declares it (an SPDX code).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDak.copyrightYear",
      "path" : "KGDak.copyrightYear",
      "short" : "Copyright year",
      "definition" : "The copyright year or range, as declared.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDak.publisherName",
      "path" : "KGDak.publisherName",
      "short" : "Publisher name",
      "definition" : "The publisher's name.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDak.publisherUrl",
      "path" : "KGDak.publisherUrl",
      "short" : "Publisher URL",
      "definition" : "The publisher's web address.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "uri"
      }]
    }]
  }
}

```
