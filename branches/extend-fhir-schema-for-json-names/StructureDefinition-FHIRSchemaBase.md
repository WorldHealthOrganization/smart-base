# FHIR Schema Base (SMART Guidelines) - SMART Base v0.2.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **FHIR Schema Base (SMART Guidelines)**

## Logical Model: FHIR Schema Base (SMART Guidelines) 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/FHIRSchemaBase | *Version*:0.2.0 |
| Active as of 2026-03-03 | *Computable Name*:FHIRSchemaBase |

 
Base logical model providing the common schema metadata interface inherited by all SMART Guidelines logical models. Every SMART Guidelines logical model schema derives from this base, which documents the shared FHIR and JSON-LD metadata properties used by the JSON Schema generation pipeline. 

**Usages:**

* This Logical Model is not used by any profiles in this Implementation Guide

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/smart.who.int.base|current/StructureDefinition/FHIRSchemaBase)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-FHIRSchemaBase.csv), [Excel](StructureDefinition-FHIRSchemaBase.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "FHIRSchemaBase",
  "url" : "http://smart.who.int/base/StructureDefinition/FHIRSchemaBase",
  "version" : "0.2.0",
  "name" : "FHIRSchemaBase",
  "title" : "FHIR Schema Base (SMART Guidelines)",
  "status" : "active",
  "date" : "2026-03-03T17:20:02+00:00",
  "publisher" : "WHO",
  "contact" : [{
    "name" : "WHO",
    "telecom" : [{
      "system" : "url",
      "value" : "http://who.int"
    }]
  }],
  "description" : "Base logical model providing the common schema metadata interface inherited by all SMART Guidelines logical models. Every SMART Guidelines logical model schema derives from this base, which documents the shared FHIR and JSON-LD metadata properties used by the JSON Schema generation pipeline.",
  "fhirVersion" : "4.0.1",
  "mapping" : [{
    "identity" : "json-schema-property-names",
    "uri" : "https://json-schema.org",
    "name" : "JSON Schema Property Names",
    "comment" : "Maps FHIR logical model element names to their JSON Schema property names. FHIR element names cannot contain colons, so elements such as fhirParent use FHIR-conformant identifiers in the logical model that differ from their JSON property names (e.g. fhir:parent, jsonld:context)."
  }],
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/FHIRSchemaBase",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "FHIRSchemaBase",
      "path" : "FHIRSchemaBase",
      "short" : "FHIR Schema Base (SMART Guidelines)",
      "definition" : "Base logical model providing the common schema metadata interface inherited by all SMART Guidelines logical models. Every SMART Guidelines logical model schema derives from this base, which documents the shared FHIR and JSON-LD metadata properties used by the JSON Schema generation pipeline."
    },
    {
      "id" : "FHIRSchemaBase.resourceType",
      "path" : "FHIRSchemaBase.resourceType",
      "short" : "Resource Type",
      "definition" : "The FHIR resource type identifying this logical model resource",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "FHIRSchemaBase.resourceDefinition",
      "path" : "FHIRSchemaBase.resourceDefinition",
      "short" : "Resource Definition",
      "definition" : "Canonical URI of the FHIR StructureDefinition that defines this logical model",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "FHIRSchemaBase.fhirParent",
      "path" : "FHIRSchemaBase.fhirParent",
      "short" : "FHIR Parent",
      "definition" : "The FHIR parent base type from which this logical model is derived (serialised as 'fhir:parent' in JSON)",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }],
      "mapping" : [{
        "identity" : "json-schema-property-names",
        "map" : "fhir:parent"
      }]
    },
    {
      "id" : "FHIRSchemaBase.jsonldContext",
      "path" : "FHIRSchemaBase.jsonldContext",
      "short" : "JSON-LD Context",
      "definition" : "JSON-LD context for this logical model (serialised as 'jsonld:context' in JSON)",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }],
      "mapping" : [{
        "identity" : "json-schema-property-names",
        "map" : "jsonld:context"
      }]
    }]
  }
}

```
