# Knowledge graph L2: Requirement Statement - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L2: Requirement Statement**

## Logical Model: Knowledge graph L2: Requirement Statement 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGRequirementStatement | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGRequirementStatement |

 

| | | | |
| :--- | :--- | :--- | :--- |
| One numbered, labelled statement inside a requirement, with a conformance verb. A node rather than a property because conformance is queried across a whole DAK – 'every SHALL in this kit, and what fulfils it' is the question requirements exist to answer. It also carries its own success criteria, so 'what would show this SHALL is met' is answerable per statement rather than per requirement. conformance is the FHIR ConformanceExpectation verb: SHALL, SHOULD, MAY or SHOULD-NOT. Across the 41 committed instances it is 155 SHALL and 15 SHOULD. successCriteria is a LIST of objects, each {key, criterion, verification}:`key`is unique within the statement (e.g. SC-1),`criterion`is a checkable sentence, and`verification`is one of test | inspection | review | analysis – the same field name and enum as folio-assistant's requirement.ts`successCriteria`, so the two map 1:1. smart-base types it, so the shape is enforced by the schema; a statement with no successCriteria is still valid (the 170 statements committed in smart-base carry none). Class IRI: http://smart.who.int/kg/requirement-statement. |

 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGRequirementStatement.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGRequirementStatement.csv), [Excel](StructureDefinition-KGRequirementStatement.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGRequirementStatement",
  "url" : "http://smart.who.int/base/StructureDefinition/KGRequirementStatement",
  "version" : "0.3.0",
  "name" : "KGRequirementStatement",
  "title" : "Knowledge graph L2: Requirement Statement",
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
  "description" : "One numbered, labelled statement inside a requirement, with a conformance verb. A node rather than a property because conformance is queried across a whole DAK -- 'every SHALL in this kit, and what fulfils it' is the question requirements exist to answer. It also carries its own success criteria, so 'what would show this SHALL is met' is answerable per statement rather than per requirement. conformance is the FHIR ConformanceExpectation verb: SHALL, SHOULD, MAY or SHOULD-NOT. Across the 41 committed instances it is 155 SHALL and 15 SHOULD. successCriteria is a LIST of objects, each {key, criterion, verification}: `key` is unique within the statement (e.g. SC-1), `criterion` is a checkable sentence, and `verification` is one of test | inspection | review | analysis -- the same field name and enum as folio-assistant's requirement.ts `successCriteria`, so the two map 1:1. smart-base types it, so the shape is enforced by the schema; a statement with no successCriteria is still valid (the 170 statements committed in smart-base carry none). Class IRI: http://smart.who.int/kg/requirement-statement.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGRequirementStatement",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGRequirementStatement",
      "path" : "KGRequirementStatement",
      "short" : "Knowledge graph L2: Requirement Statement",
      "definition" : "One numbered, labelled statement inside a requirement, with a conformance verb. A node rather than a property because conformance is queried across a whole DAK -- 'every SHALL in this kit, and what fulfils it' is the question requirements exist to answer. It also carries its own success criteria, so 'what would show this SHALL is met' is answerable per statement rather than per requirement. conformance is the FHIR ConformanceExpectation verb: SHALL, SHOULD, MAY or SHOULD-NOT. Across the 41 committed instances it is 155 SHALL and 15 SHOULD. successCriteria is a LIST of objects, each {key, criterion, verification}: `key` is unique within the statement (e.g. SC-1), `criterion` is a checkable sentence, and `verification` is one of test | inspection | review | analysis -- the same field name and enum as folio-assistant's requirement.ts `successCriteria`, so the two map 1:1. smart-base types it, so the shape is enforced by the schema; a statement with no successCriteria is still valid (the 170 statements committed in smart-base carry none). Class IRI: http://smart.who.int/kg/requirement-statement."
    },
    {
      "id" : "KGRequirementStatement.key",
      "path" : "KGRequirementStatement.key",
      "short" : "Key",
      "definition" : "The statement's key, unique within its requirement.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGRequirementStatement.label",
      "path" : "KGRequirementStatement.label",
      "short" : "Label",
      "definition" : "The statement text, with its conformance verb.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGRequirementStatement.requirement",
      "path" : "KGRequirementStatement.requirement",
      "short" : "Requirement",
      "definition" : "The id of the requirement the statement belongs to.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGRequirementStatement.conformance",
      "path" : "KGRequirementStatement.conformance",
      "short" : "Conformance",
      "definition" : "The FHIR ConformanceExpectation verb: SHALL, SHOULD, MAY or SHOULD-NOT.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://smart.who.int/base/ValueSet/KGConformanceExpectationVS"
      }
    },
    {
      "id" : "KGRequirementStatement.successCriteria",
      "path" : "KGRequirementStatement.successCriteria",
      "short" : "Success criteria",
      "definition" : "What would show the statement is met, each a checkable sentence with its verification method (folio-assistant requirement.ts `successCriteria`, 1:1).",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "BackboneElement"
      }]
    },
    {
      "id" : "KGRequirementStatement.successCriteria.key",
      "path" : "KGRequirementStatement.successCriteria.key",
      "short" : "Key",
      "definition" : "Unique within the statement, e.g. SC-1.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGRequirementStatement.successCriteria.criterion",
      "path" : "KGRequirementStatement.successCriteria.criterion",
      "short" : "Criterion",
      "definition" : "A checkable sentence.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGRequirementStatement.successCriteria.verification",
      "path" : "KGRequirementStatement.successCriteria.verification",
      "short" : "Verification",
      "definition" : "How the criterion is verified.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://smart.who.int/base/ValueSet/KGVerificationMethodVS"
      }
    }]
  }
}

```
