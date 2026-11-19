# Knowledge graph L2: External artefact - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L2: External artefact**

## Logical Model: Knowledge graph L2: External artefact 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGExternalArtifact | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGExternalArtifact |

 
A DAK file addressed by canonical URL: a BPMN process, a DMN decision table, a FHIR resource, a workbook. Deliberately opaque: it carries an IRI and a kind, and nothing about its interior. The L2-BPMN, L2-DMN and L3 classes that describe a file's interior elaborate this class at the same IRI. Moved here from L1 in 3.0 unchanged: a DAK file is the DAK's material, not WHO content. Class IRI: http://smart.who.int/kg/external-artifact. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGExternalArtifact.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGExternalArtifact.csv), [Excel](StructureDefinition-KGExternalArtifact.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGExternalArtifact",
  "url" : "http://smart.who.int/base/StructureDefinition/KGExternalArtifact",
  "version" : "0.3.0",
  "name" : "KGExternalArtifact",
  "title" : "Knowledge graph L2: External artefact",
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
  "description" : "A DAK file addressed by canonical URL: a BPMN process, a DMN decision table, a FHIR resource, a workbook. Deliberately opaque: it carries an IRI and a kind, and nothing about its interior. The L2-BPMN, L2-DMN and L3 classes that describe a file's interior elaborate this class at the same IRI. Moved here from L1 in 3.0 unchanged: a DAK file is the DAK's material, not WHO content. Class IRI: http://smart.who.int/kg/external-artifact.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGExternalArtifact",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGExternalArtifact",
      "path" : "KGExternalArtifact",
      "short" : "Knowledge graph L2: External artefact",
      "definition" : "A DAK file addressed by canonical URL: a BPMN process, a DMN decision table, a FHIR resource, a workbook. Deliberately opaque: it carries an IRI and a kind, and nothing about its interior. The L2-BPMN, L2-DMN and L3 classes that describe a file's interior elaborate this class at the same IRI. Moved here from L1 in 3.0 unchanged: a DAK file is the DAK's material, not WHO content. Class IRI: http://smart.who.int/kg/external-artifact."
    },
    {
      "id" : "KGExternalArtifact.iri",
      "path" : "KGExternalArtifact.iri",
      "short" : "IRI",
      "definition" : "The canonical IRI the file is addressed by.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "uri"
      }]
    },
    {
      "id" : "KGExternalArtifact.targetKind",
      "path" : "KGExternalArtifact.targetKind",
      "short" : "Target kind",
      "definition" : "What kind of file the artefact is.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "code"
      }],
      "binding" : {
        "strength" : "required",
        "valueSet" : "http://smart.who.int/base/ValueSet/KGArtifactKindVS"
      }
    },
    {
      "id" : "KGExternalArtifact.version",
      "path" : "KGExternalArtifact.version",
      "short" : "Version",
      "definition" : "The business version, as declared.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    }]
  }
}

```
