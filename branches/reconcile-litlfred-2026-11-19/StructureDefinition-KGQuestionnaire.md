# Knowledge graph L3: Questionnaire - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L3: Questionnaire**

## Logical Model: Knowledge graph L3: Questionnaire 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGQuestionnaire | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGQuestionnaire |

 
A FHIR Questionnaire – a data-collection form over a logical model. 10 in the immunizations IG. Its `sdc-questionnaire-targetStructureMap` extension names the StructureMap that extracts it, which is a real canonical reference. The SOP states no linkId convention and none exists in the estate, so no edge is licensed on linkId. Class IRI: http://smart.who.int/kg/questionnaire. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGQuestionnaire.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGQuestionnaire.csv), [Excel](StructureDefinition-KGQuestionnaire.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGQuestionnaire",
  "url" : "http://smart.who.int/base/StructureDefinition/KGQuestionnaire",
  "version" : "0.3.0",
  "name" : "KGQuestionnaire",
  "title" : "Knowledge graph L3: Questionnaire",
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
  "description" : "A FHIR Questionnaire -- a data-collection form over a logical model. 10 in the immunizations IG. Its `sdc-questionnaire-targetStructureMap` extension names the StructureMap that extracts it, which is a real canonical reference. The SOP states no linkId convention and none exists in the estate, so no edge is licensed on linkId. Class IRI: http://smart.who.int/kg/questionnaire.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGQuestionnaire",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGQuestionnaire",
      "path" : "KGQuestionnaire",
      "short" : "Knowledge graph L3: Questionnaire",
      "definition" : "A FHIR Questionnaire -- a data-collection form over a logical model. 10 in the immunizations IG. Its `sdc-questionnaire-targetStructureMap` extension names the StructureMap that extracts it, which is a real canonical reference. The SOP states no linkId convention and none exists in the estate, so no edge is licensed on linkId. Class IRI: http://smart.who.int/kg/questionnaire."
    },
    {
      "id" : "KGQuestionnaire.canonical",
      "path" : "KGQuestionnaire.canonical",
      "short" : "Canonical",
      "definition" : "The canonical URL. Only a resolved component carries one.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGQuestionnaire.resourceType",
      "path" : "KGQuestionnaire.resourceType",
      "short" : "Resource type",
      "definition" : "The FHIR resource type.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGQuestionnaire.profile",
      "path" : "KGQuestionnaire.profile",
      "short" : "Profile",
      "definition" : "A profile canonical the artefact declares (meta.profile or the requirement's profile).",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGQuestionnaire.status",
      "path" : "KGQuestionnaire.status",
      "short" : "Status",
      "definition" : "The resource's status (FHIR PublicationStatus).",
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
      "id" : "KGQuestionnaire.version",
      "path" : "KGQuestionnaire.version",
      "short" : "Version",
      "definition" : "The business version, as declared.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGQuestionnaire.title",
      "path" : "KGQuestionnaire.title",
      "short" : "Title",
      "definition" : "The human-readable title.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGQuestionnaire.name",
      "path" : "KGQuestionnaire.name",
      "short" : "Name",
      "definition" : "The computable name: the CamelCase identifier a Canonical() reference matches on.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGQuestionnaire.publisher",
      "path" : "KGQuestionnaire.publisher",
      "short" : "Publisher",
      "definition" : "The publisher, as declared.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGQuestionnaire.experimental",
      "path" : "KGQuestionnaire.experimental",
      "short" : "Experimental",
      "definition" : "The resource's experimental flag.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "boolean"
      }]
    },
    {
      "id" : "KGQuestionnaire.source",
      "path" : "KGQuestionnaire.source",
      "short" : "Source",
      "definition" : "Where the node was read from: a repository path or URL.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGQuestionnaire.sha256",
      "path" : "KGQuestionnaire.sha256",
      "short" : "SHA-256",
      "definition" : "Hash of the file the node was read from; pins the source.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    }]
  }
}

```
