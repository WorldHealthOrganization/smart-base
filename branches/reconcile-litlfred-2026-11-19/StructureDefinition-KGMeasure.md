# Knowledge graph L3: Measure - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L3: Measure**

## Logical Model: Knowledge graph L3: Measure 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGMeasure | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGMeasure |

 
A FHIR Measure – an indicator made computable. 41 in the immunizations IG, all declaring proportion-measure-cqfm; the SOP makes the profile depend on scoring type, which is why the profile is read rather than assumed. Joined to its L2 indicator by id convention (IMMZ.IND.08 -> IMMZIND08). Class IRI: http://smart.who.int/kg/measure. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGMeasure.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGMeasure.csv), [Excel](StructureDefinition-KGMeasure.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGMeasure",
  "url" : "http://smart.who.int/base/StructureDefinition/KGMeasure",
  "version" : "0.3.0",
  "name" : "KGMeasure",
  "title" : "Knowledge graph L3: Measure",
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
  "description" : "A FHIR Measure -- an indicator made computable. 41 in the immunizations IG, all declaring proportion-measure-cqfm; the SOP makes the profile depend on scoring type, which is why the profile is read rather than assumed. Joined to its L2 indicator by id convention (IMMZ.IND.08 -> IMMZIND08). Class IRI: http://smart.who.int/kg/measure.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGMeasure",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGMeasure",
      "path" : "KGMeasure",
      "short" : "Knowledge graph L3: Measure",
      "definition" : "A FHIR Measure -- an indicator made computable. 41 in the immunizations IG, all declaring proportion-measure-cqfm; the SOP makes the profile depend on scoring type, which is why the profile is read rather than assumed. Joined to its L2 indicator by id convention (IMMZ.IND.08 -> IMMZIND08). Class IRI: http://smart.who.int/kg/measure."
    },
    {
      "id" : "KGMeasure.canonical",
      "path" : "KGMeasure.canonical",
      "short" : "Canonical",
      "definition" : "The canonical URL. Only a resolved component carries one.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGMeasure.resourceType",
      "path" : "KGMeasure.resourceType",
      "short" : "Resource type",
      "definition" : "The FHIR resource type.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGMeasure.profile",
      "path" : "KGMeasure.profile",
      "short" : "Profile",
      "definition" : "A profile canonical the artefact declares (meta.profile or the requirement's profile).",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGMeasure.status",
      "path" : "KGMeasure.status",
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
      "id" : "KGMeasure.version",
      "path" : "KGMeasure.version",
      "short" : "Version",
      "definition" : "The business version, as declared.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGMeasure.title",
      "path" : "KGMeasure.title",
      "short" : "Title",
      "definition" : "The human-readable title.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGMeasure.name",
      "path" : "KGMeasure.name",
      "short" : "Name",
      "definition" : "The computable name: the CamelCase identifier a Canonical() reference matches on.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGMeasure.publisher",
      "path" : "KGMeasure.publisher",
      "short" : "Publisher",
      "definition" : "The publisher, as declared.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGMeasure.experimental",
      "path" : "KGMeasure.experimental",
      "short" : "Experimental",
      "definition" : "The resource's experimental flag.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "boolean"
      }]
    },
    {
      "id" : "KGMeasure.scoring",
      "path" : "KGMeasure.scoring",
      "short" : "Scoring",
      "definition" : "The Measure's scoring (proportion, ratio, cohort, continuous-variable).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGMeasure.source",
      "path" : "KGMeasure.source",
      "short" : "Source",
      "definition" : "Where the node was read from: a repository path or URL.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGMeasure.sha256",
      "path" : "KGMeasure.sha256",
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
