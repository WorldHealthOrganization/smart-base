# JSON Schema Property Name - SMART Base v0.2.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **JSON Schema Property Name**

## Extension: JSON Schema Property Name 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/JsonSchemaName | *Version*:0.2.0 |
| Draft as of 2026-03-03 | *Computable Name*:JsonSchemaName |

Specifies the property name to use in the generated JSON Schema for this element, when it differs from the FHIR element name. Used by the schema generation pipeline to map FHIR-conformant element names (which cannot contain colons) to their canonical JSON or JSON-LD property names (e.g. 'fhir:parent', 'jsonld:valuesets').

**Context of Use**

**Usage info**

**Usages:**

* Examples for this Extension: [FHIRSchemaBase](StructureDefinition-FHIRSchemaBase.md)

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/smart.who.int.base|current/StructureDefinition/JsonSchemaName)

### Formal Views of Extension Content

 [Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-JsonSchemaName.csv), [Excel](StructureDefinition-JsonSchemaName.xlsx), [Schematron](StructureDefinition-JsonSchemaName.sch) 

#### Constraints



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "JsonSchemaName",
  "url" : "http://smart.who.int/base/StructureDefinition/JsonSchemaName",
  "version" : "0.2.0",
  "name" : "JsonSchemaName",
  "title" : "JSON Schema Property Name",
  "status" : "draft",
  "date" : "2026-03-03T13:30:44+00:00",
  "publisher" : "WHO",
  "contact" : [{
    "name" : "WHO",
    "telecom" : [{
      "system" : "url",
      "value" : "http://who.int"
    }]
  }],
  "description" : "Specifies the property name to use in the generated JSON Schema for this element, when it differs from the FHIR element name. Used by the schema generation pipeline to map FHIR-conformant element names (which cannot contain colons) to their canonical JSON or JSON-LD property names (e.g. 'fhir:parent', 'jsonld:valuesets').",
  "fhirVersion" : "4.0.1",
  "mapping" : [{
    "identity" : "rim",
    "uri" : "http://hl7.org/v3",
    "name" : "RIM Mapping"
  }],
  "kind" : "complex-type",
  "abstract" : false,
  "context" : [{
    "type" : "element",
    "expression" : "Element"
  }],
  "type" : "Extension",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Extension",
  "derivation" : "constraint",
  "differential" : {
    "element" : [{
      "id" : "Extension",
      "path" : "Extension",
      "short" : "JSON Schema Property Name",
      "definition" : "Specifies the property name to use in the generated JSON Schema for this element, when it differs from the FHIR element name. Used by the schema generation pipeline to map FHIR-conformant element names (which cannot contain colons) to their canonical JSON or JSON-LD property names (e.g. 'fhir:parent', 'jsonld:valuesets')."
    },
    {
      "id" : "Extension.extension",
      "path" : "Extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.url",
      "path" : "Extension.url",
      "fixedUri" : "http://smart.who.int/base/StructureDefinition/JsonSchemaName"
    },
    {
      "id" : "Extension.value[x]",
      "path" : "Extension.value[x]",
      "type" : [{
        "code" : "string"
      }]
    }]
  }
}

```
