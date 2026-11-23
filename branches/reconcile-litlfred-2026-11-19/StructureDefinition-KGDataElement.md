# Knowledge graph L2: Core Data Element - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L2: Core Data Element**

## Logical Model: Knowledge graph L2: Core Data Element 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGDataElement | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGDataElement |

 

| | | | |
| :--- | :--- | :--- | :--- |
| DAK component 5. CoreDataElement.fsh calls itself "the ONE EXCEPTION to allowing FHIR R4 models into the DAK LMs":`type`is one of valueset | codesystem | conceptmap | logicalmodel and`canonical 1..1 uri`points at it. The canonical is recorded; nothing inside it is copied, because FHIR is its own query layer.`name`,`resolutionStatus`and`extractionRule`are for elements recovered from DMN input expressions rather than declared in a dictionary. A recovered element is a name that was REFERENCED, not a definition that was found, and only a resolved one may carry a canonical. Class IRI: http://smart.who.int/kg/data-element. |

 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGDataElement.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGDataElement.csv), [Excel](StructureDefinition-KGDataElement.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGDataElement",
  "url" : "http://smart.who.int/base/StructureDefinition/KGDataElement",
  "version" : "0.3.0",
  "name" : "KGDataElement",
  "title" : "Knowledge graph L2: Core Data Element",
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
  "description" : "DAK component 5. CoreDataElement.fsh calls itself \"the ONE EXCEPTION to allowing FHIR R4 models into the DAK LMs\": `type` is one of valueset | codesystem | conceptmap | logicalmodel and `canonical 1..1 uri` points at it. The canonical is recorded; nothing inside it is copied, because FHIR is its own query layer. `name`, `resolutionStatus` and `extractionRule` are for elements recovered from DMN input expressions rather than declared in a dictionary. A recovered element is a name that was REFERENCED, not a definition that was found, and only a resolved one may carry a canonical. Class IRI: http://smart.who.int/kg/data-element.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGDataElement",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGDataElement",
      "path" : "KGDataElement",
      "short" : "Knowledge graph L2: Core Data Element",
      "definition" : "DAK component 5. CoreDataElement.fsh calls itself \"the ONE EXCEPTION to allowing FHIR R4 models into the DAK LMs\": `type` is one of valueset | codesystem | conceptmap | logicalmodel and `canonical 1..1 uri` points at it. The canonical is recorded; nothing inside it is copied, because FHIR is its own query layer. `name`, `resolutionStatus` and `extractionRule` are for elements recovered from DMN input expressions rather than declared in a dictionary. A recovered element is a name that was REFERENCED, not a definition that was found, and only a resolved one may carry a canonical. Class IRI: http://smart.who.int/kg/data-element."
    },
    {
      "id" : "KGDataElement.id",
      "path" : "KGDataElement.id",
      "short" : "Id",
      "definition" : "The identifier the source declares (an FSH instance id, a BPMN or DMN element id).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDataElement.name",
      "path" : "KGDataElement.name",
      "short" : "Name",
      "definition" : "The name a DMN input expression referenced, for a recovered element.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDataElement.type",
      "path" : "KGDataElement.type",
      "short" : "Type",
      "definition" : "The data type, as the data dictionary declares it.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDataElement.canonical",
      "path" : "KGDataElement.canonical",
      "short" : "Canonical",
      "definition" : "The canonical URL. Only a resolved component carries one.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGDataElement.description",
      "path" : "KGDataElement.description",
      "short" : "Description",
      "definition" : "A description, as the source gives it.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGDataElement.sourceKind",
      "path" : "KGDataElement.sourceKind",
      "short" : "Source kind",
      "definition" : "What kind of artefact the component was read from (an FSH instance, a spreadsheet, a BPMN file).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDataElement.source",
      "path" : "KGDataElement.source",
      "short" : "Source",
      "definition" : "Where the node was read from: a repository path or URL.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDataElement.resolutionStatus",
      "path" : "KGDataElement.resolutionStatus",
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
    },
    {
      "id" : "KGDataElement.extractionRule",
      "path" : "KGDataElement.extractionRule",
      "short" : "Extraction rule",
      "definition" : "How a data element recovered from a DMN input expression was found.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    }]
  }
}

```
