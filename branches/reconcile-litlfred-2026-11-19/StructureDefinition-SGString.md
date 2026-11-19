# SGString - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **SGString**

## Extension: SGString 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/SGString | *Version*:0.3.0 |
| Retired as of 2026-11-19 | *Computable Name*:SGString |

Smart Guidelines (required) string extension for use in a complex extension. Retired: SGUserStory now uses inline `capability` and `benefit` sub-extensions, because two slices of one extension definition cannot be told apart.

**Context of Use**

**Usage info**

**Usages:**

* This Extension is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-SGString.json)

### Formal Views of Extension Content

 [Description of Profiles, Differentials, Snapshots, and how the XML and JSON presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-SGString.csv), [Excel](StructureDefinition-SGString.xlsx), [Schematron](StructureDefinition-SGString.sch) 

#### Constraints



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "SGString",
  "url" : "http://smart.who.int/base/StructureDefinition/SGString",
  "version" : "0.3.0",
  "name" : "SGString",
  "status" : "retired",
  "date" : "2026-11-19T20:24:57+00:00",
  "publisher" : "WHO",
  "contact" : [{
    "name" : "WHO",
    "telecom" : [{
      "system" : "url",
      "value" : "http://who.int"
    }]
  }],
  "description" : "Smart Guidelines (required) string extension for use in a complex extension. Retired: SGUserStory now uses inline `capability` and `benefit` sub-extensions, because two slices of one extension definition cannot be told apart.",
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
      "definition" : "Smart Guidelines (required) string extension for use in a complex extension. Retired: SGUserStory now uses inline `capability` and `benefit` sub-extensions, because two slices of one extension definition cannot be told apart."
    },
    {
      "id" : "Extension.extension",
      "path" : "Extension.extension",
      "max" : "0"
    },
    {
      "id" : "Extension.url",
      "path" : "Extension.url",
      "fixedUri" : "http://smart.who.int/base/StructureDefinition/SGString"
    },
    {
      "id" : "Extension.value[x]",
      "path" : "Extension.value[x]",
      "min" : 1,
      "type" : [{
        "code" : "string"
      }],
      "mustSupport" : true
    }]
  }
}

```
