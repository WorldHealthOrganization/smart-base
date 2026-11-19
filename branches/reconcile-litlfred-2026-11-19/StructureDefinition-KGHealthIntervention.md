# Knowledge graph L1: Health intervention - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L1: Health intervention**

## Logical Model: Knowledge graph L1: Health intervention 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGHealthIntervention | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGHealthIntervention |

 
An intervention identified in a WHO catalogue or classification (UHC Compendium, ICHI, CDHI), digital interventions included. A peer of recommendation, not a recommendation. A DAK may draw on both. Corresponds to HealthInterventions: identifier and description correspond to HealthInterventions.id and description[x]; not a Parent because HealthInterventions requires reference 1..* DublinCore, which here is an edge (definedIn) rather than a field. Class IRI: http://smart.who.int/kg/health-intervention. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGHealthIntervention.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGHealthIntervention.csv), [Excel](StructureDefinition-KGHealthIntervention.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGHealthIntervention",
  "url" : "http://smart.who.int/base/StructureDefinition/KGHealthIntervention",
  "version" : "0.3.0",
  "name" : "KGHealthIntervention",
  "title" : "Knowledge graph L1: Health intervention",
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
  "description" : "An intervention identified in a WHO catalogue or classification (UHC Compendium, ICHI, CDHI), digital interventions included. A peer of recommendation, not a recommendation. A DAK may draw on both. Corresponds to HealthInterventions: identifier and description correspond to HealthInterventions.id and description[x]; not a Parent because HealthInterventions requires reference 1..* DublinCore, which here is an edge (definedIn) rather than a field. Class IRI: http://smart.who.int/kg/health-intervention.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGHealthIntervention",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGHealthIntervention",
      "path" : "KGHealthIntervention",
      "short" : "Knowledge graph L1: Health intervention",
      "definition" : "An intervention identified in a WHO catalogue or classification (UHC Compendium, ICHI, CDHI), digital interventions included. A peer of recommendation, not a recommendation. A DAK may draw on both. Corresponds to HealthInterventions: identifier and description correspond to HealthInterventions.id and description[x]; not a Parent because HealthInterventions requires reference 1..* DublinCore, which here is an edge (definedIn) rather than a field. Class IRI: http://smart.who.int/kg/health-intervention."
    },
    {
      "id" : "KGHealthIntervention.identifier",
      "path" : "KGHealthIntervention.identifier",
      "short" : "Identifier",
      "definition" : "The catalogue code (UHC, ICHI, CDHI).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGHealthIntervention.name",
      "path" : "KGHealthIntervention.name",
      "short" : "Name",
      "definition" : "Name, as catalogued.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGHealthIntervention.description",
      "path" : "KGHealthIntervention.description",
      "short" : "Description",
      "definition" : "Description, as catalogued.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGHealthIntervention.interventionType",
      "path" : "KGHealthIntervention.interventionType",
      "short" : "Intervention type",
      "definition" : "DRAFT.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://smart.who.int/base/ValueSet/KGInterventionTypeVS"
      }
    }]
  }
}

```
