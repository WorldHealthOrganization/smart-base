# Knowledge graph L2: Generic Persona - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L2: Generic Persona**

## Logical Model: Knowledge graph L2: Generic Persona 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGPersona | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGPersona |

 
DAK component 2. Grounded in GenericPersona.fsh – title, id, description, otherNames, iscoCode bound to ISCO08ValueSet – and in the 22 committed ActorDefinition instances that carry name, title, type and description. The two disagree about where ISCO lives, which the properties record rather than smooth over. `title` is the human-readable label a BPMN pool matches on; `name` is the CamelCase identifier a Canonical() reference matches on. They are different strings for the same persona and conflating them is precisely how the pool join breaks. GenericPersona.fsh declares `iscoCode 0..* code`, but the committed ActorDefinitions record ISCO in prose inside description, so iscoCode is usually empty and is not authoritative. Class IRI: http://smart.who.int/kg/persona. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGPersona.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGPersona.csv), [Excel](StructureDefinition-KGPersona.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGPersona",
  "url" : "http://smart.who.int/base/StructureDefinition/KGPersona",
  "version" : "0.3.0",
  "name" : "KGPersona",
  "title" : "Knowledge graph L2: Generic Persona",
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
  "description" : "DAK component 2. Grounded in GenericPersona.fsh -- title, id, description, otherNames, iscoCode bound to ISCO08ValueSet -- and in the 22 committed ActorDefinition instances that carry name, title, type and description. The two disagree about where ISCO lives, which the properties record rather than smooth over. `title` is the human-readable label a BPMN pool matches on; `name` is the CamelCase identifier a Canonical() reference matches on. They are different strings for the same persona and conflating them is precisely how the pool join breaks. GenericPersona.fsh declares `iscoCode 0..* code`, but the committed ActorDefinitions record ISCO in prose inside description, so iscoCode is usually empty and is not authoritative. Class IRI: http://smart.who.int/kg/persona.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGPersona",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGPersona",
      "path" : "KGPersona",
      "short" : "Knowledge graph L2: Generic Persona",
      "definition" : "DAK component 2. Grounded in GenericPersona.fsh -- title, id, description, otherNames, iscoCode bound to ISCO08ValueSet -- and in the 22 committed ActorDefinition instances that carry name, title, type and description. The two disagree about where ISCO lives, which the properties record rather than smooth over. `title` is the human-readable label a BPMN pool matches on; `name` is the CamelCase identifier a Canonical() reference matches on. They are different strings for the same persona and conflating them is precisely how the pool join breaks. GenericPersona.fsh declares `iscoCode 0..* code`, but the committed ActorDefinitions record ISCO in prose inside description, so iscoCode is usually empty and is not authoritative. Class IRI: http://smart.who.int/kg/persona."
    },
    {
      "id" : "KGPersona.id",
      "path" : "KGPersona.id",
      "short" : "Id",
      "definition" : "The identifier the source declares (an FSH instance id, a BPMN or DMN element id).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGPersona.title",
      "path" : "KGPersona.title",
      "short" : "Title",
      "definition" : "The human-readable title.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGPersona.name",
      "path" : "KGPersona.name",
      "short" : "Name",
      "definition" : "The computable name: the CamelCase identifier a Canonical() reference matches on.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGPersona.description",
      "path" : "KGPersona.description",
      "short" : "Description",
      "definition" : "A description, as the source gives it.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGPersona.otherNames",
      "path" : "KGPersona.otherNames",
      "short" : "Other names",
      "definition" : "Another name the persona is known by.",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGPersona.iscoCode",
      "path" : "KGPersona.iscoCode",
      "short" : "ISCO code",
      "definition" : "An ISCO-08 occupation code (GenericPersona.fsh `iscoCode 0..*`). Usually empty: the committed ActorDefinitions give ISCO in prose.",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGPersona.personaType",
      "path" : "KGPersona.personaType",
      "short" : "Persona type",
      "definition" : "The kind of persona, as declared.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGPersona.sourceKind",
      "path" : "KGPersona.sourceKind",
      "short" : "Source kind",
      "definition" : "What kind of artefact the component was read from (an FSH instance, a spreadsheet, a BPMN file).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGPersona.source",
      "path" : "KGPersona.source",
      "short" : "Source",
      "definition" : "Where the node was read from: a repository path or URL.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGPersona.resolutionStatus",
      "path" : "KGPersona.resolutionStatus",
      "short" : "Resolution status",
      "definition" : "Whether the component something names was found: `unresolved` when nothing declares it, so the gap is queryable.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://smart.who.int/base/ValueSet/KGResolutionStatusVS"
      }
    }]
  }
}

```
