# Knowledge graph L3: Code System - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L3: Code System**

## Logical Model: Knowledge graph L3: Code System 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGCodeSystem | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGCodeSystem |

 
A FHIR CodeSystem. The SOP says each guideline defines one guideline-level code system holding a concept for every data dictionary element – which is what makes `code[WHO] = IMMZ.DE9` on a logical model element resolvable. 6 in the immunizations IG. The codes themselves are not copied here. Class IRI: http://smart.who.int/kg/code-system. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGCodeSystem.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGCodeSystem.csv), [Excel](StructureDefinition-KGCodeSystem.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGCodeSystem",
  "url" : "http://smart.who.int/base/StructureDefinition/KGCodeSystem",
  "version" : "0.3.0",
  "name" : "KGCodeSystem",
  "title" : "Knowledge graph L3: Code System",
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
  "description" : "A FHIR CodeSystem. The SOP says each guideline defines one guideline-level code system holding a concept for every data dictionary element -- which is what makes `code[WHO] = IMMZ.DE9` on a logical model element resolvable. 6 in the immunizations IG. The codes themselves are not copied here. Class IRI: http://smart.who.int/kg/code-system.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGCodeSystem",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGCodeSystem",
      "path" : "KGCodeSystem",
      "short" : "Knowledge graph L3: Code System",
      "definition" : "A FHIR CodeSystem. The SOP says each guideline defines one guideline-level code system holding a concept for every data dictionary element -- which is what makes `code[WHO] = IMMZ.DE9` on a logical model element resolvable. 6 in the immunizations IG. The codes themselves are not copied here. Class IRI: http://smart.who.int/kg/code-system."
    },
    {
      "id" : "KGCodeSystem.canonical",
      "path" : "KGCodeSystem.canonical",
      "short" : "Canonical",
      "definition" : "The canonical URL. Only a resolved component carries one.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGCodeSystem.resourceType",
      "path" : "KGCodeSystem.resourceType",
      "short" : "Resource type",
      "definition" : "The FHIR resource type.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGCodeSystem.profile",
      "path" : "KGCodeSystem.profile",
      "short" : "Profile",
      "definition" : "A profile canonical the artefact declares (meta.profile or the requirement's profile).",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGCodeSystem.status",
      "path" : "KGCodeSystem.status",
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
      "id" : "KGCodeSystem.version",
      "path" : "KGCodeSystem.version",
      "short" : "Version",
      "definition" : "The business version, as declared.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGCodeSystem.title",
      "path" : "KGCodeSystem.title",
      "short" : "Title",
      "definition" : "The human-readable title.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGCodeSystem.name",
      "path" : "KGCodeSystem.name",
      "short" : "Name",
      "definition" : "The computable name: the CamelCase identifier a Canonical() reference matches on.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGCodeSystem.publisher",
      "path" : "KGCodeSystem.publisher",
      "short" : "Publisher",
      "definition" : "The publisher, as declared.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGCodeSystem.experimental",
      "path" : "KGCodeSystem.experimental",
      "short" : "Experimental",
      "definition" : "The resource's experimental flag.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "boolean"
      }]
    },
    {
      "id" : "KGCodeSystem.source",
      "path" : "KGCodeSystem.source",
      "short" : "Source",
      "definition" : "Where the node was read from: a repository path or URL.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGCodeSystem.sha256",
      "path" : "KGCodeSystem.sha256",
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
