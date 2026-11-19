# Knowledge graph L2-DMN: DMN Output Clause - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L2-DMN: DMN Output Clause**

## Logical Model: Knowledge graph L2-DMN: DMN Output Clause 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGDmnOutputClause | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGDmnOutputClause |

 
An output column. The BCG table's four are Care Plan, Guidance displayed to health worker, Annotations and Reference(s). These are column DEFINITIONS in a decision table, not clinical records: no edge from this class reaches an execution artefact, and none may. serialisedAs is outputEntry or annotationEntry – DMN splits the columns across two element types and the split is positional, so recording it is what lets a rule's cells be matched back to their columns. isReferenceColumn marks the L1 column, found by its description rather than its index. Class IRI: http://smart.who.int/kg/dmn-output-clause. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGDmnOutputClause.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGDmnOutputClause.csv), [Excel](StructureDefinition-KGDmnOutputClause.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGDmnOutputClause",
  "url" : "http://smart.who.int/base/StructureDefinition/KGDmnOutputClause",
  "version" : "0.3.0",
  "name" : "KGDmnOutputClause",
  "title" : "Knowledge graph L2-DMN: DMN Output Clause",
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
  "description" : "An output column. The BCG table's four are Care Plan, Guidance displayed to health worker, Annotations and Reference(s). These are column DEFINITIONS in a decision table, not clinical records: no edge from this class reaches an execution artefact, and none may. serialisedAs is outputEntry or annotationEntry -- DMN splits the columns across two element types and the split is positional, so recording it is what lets a rule's cells be matched back to their columns. isReferenceColumn marks the L1 column, found by its description rather than its index. Class IRI: http://smart.who.int/kg/dmn-output-clause.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGDmnOutputClause",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGDmnOutputClause",
      "path" : "KGDmnOutputClause",
      "short" : "Knowledge graph L2-DMN: DMN Output Clause",
      "definition" : "An output column. The BCG table's four are Care Plan, Guidance displayed to health worker, Annotations and Reference(s). These are column DEFINITIONS in a decision table, not clinical records: no edge from this class reaches an execution artefact, and none may. serialisedAs is outputEntry or annotationEntry -- DMN splits the columns across two element types and the split is positional, so recording it is what lets a rule's cells be matched back to their columns. isReferenceColumn marks the L1 column, found by its description rather than its index. Class IRI: http://smart.who.int/kg/dmn-output-clause."
    },
    {
      "id" : "KGDmnOutputClause.id",
      "path" : "KGDmnOutputClause.id",
      "short" : "Id",
      "definition" : "The identifier the source declares (an FSH instance id, a BPMN or DMN element id).",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDmnOutputClause.label",
      "path" : "KGDmnOutputClause.label",
      "short" : "Label",
      "definition" : "The label, as declared.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGDmnOutputClause.description",
      "path" : "KGDmnOutputClause.description",
      "short" : "Description",
      "definition" : "A description, as the source gives it.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGDmnOutputClause.ordinal",
      "path" : "KGDmnOutputClause.ordinal",
      "short" : "Ordinal",
      "definition" : "Position, counted from 0, in the order the source lists it.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "unsignedInt"
      }]
    },
    {
      "id" : "KGDmnOutputClause.serialisedAs",
      "path" : "KGDmnOutputClause.serialisedAs",
      "short" : "Serialised as",
      "definition" : "Which DMN element type the column's cells are: outputEntry or annotationEntry. The split is positional, so this is what matches a rule's cells back to their columns.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://smart.who.int/base/ValueSet/KGDmnEntryKindVS"
      }
    },
    {
      "id" : "KGDmnOutputClause.isReferenceColumn",
      "path" : "KGDmnOutputClause.isReferenceColumn",
      "short" : "Is reference column",
      "definition" : "Marks the L1 reference column, found by its description rather than its index.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "boolean"
      }]
    }]
  }
}

```
