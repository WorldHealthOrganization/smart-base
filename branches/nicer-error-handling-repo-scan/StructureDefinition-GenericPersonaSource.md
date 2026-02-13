# Generic Persona Source - SMART Base v0.2.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Generic Persona Source**

## Logical Model: Generic Persona Source 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/GenericPersonaSource | *Version*:0.2.0 |
| Active as of 2025-10-11 | *Computable Name*:GenericPersonaSource |

 
Source reference for Generic Persona - exactly one of the following must be provided: 
* url (url data type): URL to retrieve GenericPersona definition from input/ or external source
* canonical (canonical data type): Canonical URI pointing to the GenericPersona definition
* instance: Inline GenericPersona instance data
 

**Usages:**

* Use this Logical Model: [Digital Adaptation Kit (DAK)](StructureDefinition-DAK.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/smart.who.int.base|current/StructureDefinition/GenericPersonaSource)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-GenericPersonaSource.csv), [Excel](StructureDefinition-GenericPersonaSource.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "GenericPersonaSource",
  "url" : "http://smart.who.int/base/StructureDefinition/GenericPersonaSource",
  "version" : "0.2.0",
  "name" : "GenericPersonaSource",
  "title" : "Generic Persona Source",
  "status" : "active",
  "date" : "2025-10-11T22:03:24+00:00",
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
  "description" : "Source reference for Generic Persona - exactly one of the following must be provided:\n- url (url data type): URL to retrieve GenericPersona definition from input/ or external source\n- canonical (canonical data type): Canonical URI pointing to the GenericPersona definition\n- instance: Inline GenericPersona instance data",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/GenericPersonaSource",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [
      {
        "id" : "GenericPersonaSource",
        "path" : "GenericPersonaSource",
        "short" : "Generic Persona Source",
        "definition" : "Source reference for Generic Persona - exactly one of the following must be provided:\n- url (url data type): URL to retrieve GenericPersona definition from input/ or external source\n- canonical (canonical data type): Canonical URI pointing to the GenericPersona definition\n- instance: Inline GenericPersona instance data"
      },
      {
        "id" : "GenericPersonaSource.url",
        "path" : "GenericPersonaSource.url",
        "short" : "URL",
        "definition" : "URL to retrieve GenericPersona definition from input/ or external source",
        "min" : 0,
        "max" : "1",
        "type" : [
          {
            "code" : "url"
          }
        ]
      },
      {
        "id" : "GenericPersonaSource.canonical",
        "path" : "GenericPersonaSource.canonical",
        "short" : "Canonical",
        "definition" : "Canonical URI pointing to the GenericPersona definition",
        "min" : 0,
        "max" : "1",
        "type" : [
          {
            "code" : "canonical",
            "targetProfile" : [
              "http://smart.who.int/base/StructureDefinition/GenericPersona"
            ]
          }
        ]
      },
      {
        "id" : "GenericPersonaSource.instance",
        "path" : "GenericPersonaSource.instance",
        "short" : "Instance",
        "definition" : "Inline GenericPersona instance data",
        "min" : 0,
        "max" : "1",
        "type" : [
          {
            "code" : "http://smart.who.int/base/StructureDefinition/GenericPersona"
          }
        ]
      }
    ]
  }
}

```
