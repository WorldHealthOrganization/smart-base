# Knowledge graph L1: Terminology code - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L1: Terminology code**

## Logical Model: Knowledge graph L1: Terminology code 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGTerminologyCode | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGTerminologyCode |

 
A code in an external terminology — ICD-10, ICD-11, SNOMED CT, ATC, or a WHO classification such as CDHI. CROSS-REFERENCE ONLY. It records system, code and display, and asserts NOTHING about the terminology: no hierarchy, no subsumption, no synonyms, no post-coordination. The terminology has its own authority, its own release cycle and its own tooling, and a partial copy here would be wrong within one release. Resolve meaning against the terminology server, not against this graph. Derives from Coding (FHIR R4 core datatype); system, code, display, version are its elements. Class IRI: http://smart.who.int/kg/terminology-code. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGTerminologyCode.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGTerminologyCode.csv), [Excel](StructureDefinition-KGTerminologyCode.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGTerminologyCode",
  "url" : "http://smart.who.int/base/StructureDefinition/KGTerminologyCode",
  "version" : "0.3.0",
  "name" : "KGTerminologyCode",
  "title" : "Knowledge graph L1: Terminology code",
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
  "description" : "A code in an external terminology — ICD-10, ICD-11, SNOMED CT, ATC, or a WHO classification such as CDHI. CROSS-REFERENCE ONLY. It records system, code and display, and asserts NOTHING about the terminology: no hierarchy, no subsumption, no synonyms, no post-coordination. The terminology has its own authority, its own release cycle and its own tooling, and a partial copy here would be wrong within one release. Resolve meaning against the terminology server, not against this graph. Derives from Coding (FHIR R4 core datatype); system, code, display, version are its elements. Class IRI: http://smart.who.int/kg/terminology-code.",
  "fhirVersion" : "4.0.1",
  "mapping" : [{
    "identity" : "v2",
    "uri" : "http://hl7.org/v2",
    "name" : "HL7 v2 Mapping"
  },
  {
    "identity" : "rim",
    "uri" : "http://hl7.org/v3",
    "name" : "RIM Mapping"
  },
  {
    "identity" : "orim",
    "uri" : "http://hl7.org/orim",
    "name" : "Ontological RIM Mapping"
  }],
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGTerminologyCode",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Coding",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGTerminologyCode",
      "path" : "KGTerminologyCode",
      "short" : "Knowledge graph L1: Terminology code",
      "definition" : "A code in an external terminology — ICD-10, ICD-11, SNOMED CT, ATC, or a WHO classification such as CDHI. CROSS-REFERENCE ONLY. It records system, code and display, and asserts NOTHING about the terminology: no hierarchy, no subsumption, no synonyms, no post-coordination. The terminology has its own authority, its own release cycle and its own tooling, and a partial copy here would be wrong within one release. Resolve meaning against the terminology server, not against this graph. Derives from Coding (FHIR R4 core datatype); system, code, display, version are its elements. Class IRI: http://smart.who.int/kg/terminology-code."
    }]
  }
}

```
