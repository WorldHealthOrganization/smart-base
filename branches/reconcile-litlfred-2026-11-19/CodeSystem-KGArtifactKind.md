# Knowledge graph L2: artifact kind - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L2: artifact kind**

## CodeSystem: Knowledge graph L2: artifact kind 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/KGArtifactKind | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGArtifactKind |

 
What kind of file an external artefact is. Moved with the class from L1, where it was free text. Source: smart-kg ontology/l2/l2.json valueSets "artifact-kind"; Files observed in smart-base and in WHO's immunizations DAK (canonical http://smart.who.int/immunizations). 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Knowledge graph L2: artifact kind](ValueSet-KGArtifactKindVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "KGArtifactKind",
  "url" : "http://smart.who.int/base/CodeSystem/KGArtifactKind",
  "version" : "0.3.0",
  "name" : "KGArtifactKind",
  "title" : "Knowledge graph L2: artifact kind",
  "status" : "active",
  "experimental" : false,
  "date" : "2026-11-23T18:43:32+00:00",
  "publisher" : "WHO",
  "contact" : [{
    "name" : "WHO",
    "telecom" : [{
      "system" : "url",
      "value" : "http://who.int"
    }]
  }],
  "description" : "What kind of file an external artefact is. Moved with the class from L1, where it was free text. Source: smart-kg ontology/l2/l2.json valueSets \"artifact-kind\"; Files observed in smart-base and in WHO's immunizations DAK (canonical http://smart.who.int/immunizations).",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 6,
  "concept" : [{
    "code" : "dmn",
    "display" : "Dmn",
    "definition" : "A DMN decision table."
  },
  {
    "code" : "bpmn",
    "display" : "Bpmn",
    "definition" : "A BPMN process."
  },
  {
    "code" : "fhir-resource",
    "display" : "Fhir resource",
    "definition" : "A FHIR resource, addressed by canonical URL."
  },
  {
    "code" : "spreadsheet",
    "display" : "Spreadsheet",
    "definition" : "A workbook, such as the decision-support logic or indicators workbook."
  },
  {
    "code" : "feature-file",
    "display" : "Feature file",
    "definition" : "A Gherkin feature file."
  },
  {
    "code" : "document",
    "display" : "Document",
    "definition" : "Any other document."
  }]
}

```
