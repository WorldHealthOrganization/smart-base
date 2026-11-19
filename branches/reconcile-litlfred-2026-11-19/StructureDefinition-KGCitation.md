# Knowledge graph L1: Citation - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L1: Citation**

## Logical Model: Knowledge graph L1: Citation 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGCitation | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGCitation |

 
One citation string exactly as written in a DAK artefact. A cell holding several citations yields several nodes. Content-addressed in the DAK's namespace, so one string is one node across artefacts. Where a citation was found is recorded by appearsIn (L2) and by each use edge (L2-DMN, L3 citesSource), not on the node. Class IRI: http://smart.who.int/kg/citation. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGCitation.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGCitation.csv), [Excel](StructureDefinition-KGCitation.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGCitation",
  "url" : "http://smart.who.int/base/StructureDefinition/KGCitation",
  "version" : "0.3.0",
  "name" : "KGCitation",
  "title" : "Knowledge graph L1: Citation",
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
  "description" : "One citation string exactly as written in a DAK artefact. A cell holding several citations yields several nodes. Content-addressed in the DAK's namespace, so one string is one node across artefacts. Where a citation was found is recorded by appearsIn (L2) and by each use edge (L2-DMN, L3 citesSource), not on the node. Class IRI: http://smart.who.int/kg/citation.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGCitation",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGCitation",
      "path" : "KGCitation",
      "short" : "Knowledge graph L1: Citation",
      "definition" : "One citation string exactly as written in a DAK artefact. A cell holding several citations yields several nodes. Content-addressed in the DAK's namespace, so one string is one node across artefacts. Where a citation was found is recorded by appearsIn (L2) and by each use edge (L2-DMN, L3 citesSource), not on the node. Class IRI: http://smart.who.int/kg/citation."
    },
    {
      "id" : "KGCitation.text",
      "path" : "KGCitation.text",
      "short" : "Text",
      "definition" : "The citation string, VERBATIM, as written in the DAK artefact.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGCitation.numbering",
      "path" : "KGCitation.numbering",
      "short" : "Numbering",
      "definition" : "The '(n)' back-reference into the artefact's reference list.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGCitation.citationKind",
      "path" : "KGCitation.citationKind",
      "short" : "Citation kind",
      "definition" : "Whether a citation string names a source, or stands in for one that is missing.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://smart.who.int/base/ValueSet/KGCitationKindVS"
      }
    },
    {
      "id" : "KGCitation.resolutionStatus",
      "path" : "KGCitation.resolutionStatus",
      "short" : "Resolution status",
      "definition" : "Whether a citation string has been matched to what it cites.",
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
