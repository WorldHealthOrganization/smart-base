# Knowledge graph L1-LIBRARY: Implementation practice - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L1-LIBRARY: Implementation practice**

## Logical Model: Knowledge graph L1-LIBRARY: Implementation practice 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/StructureDefinition/KGImplementationPractice | *Version*:0.3.0 |
| Active as of 2026-11-19 | *Computable Name*:KGImplementationPractice |

 
A statement of how to put guidance into practice, printed in a publication whose publicationType is implementation-guidance or methodology: the handbook's "products that are not guidelines" (§1.9), a "how to" document that makes no recommendations of its own. Not a recommendation, and not a good practice statement — both are made by a guideline and approved by the GRC; this is neither. It carries no kind, direction, strength or certainty, because nothing graded it. A handbook's own "Best practices" lists are the typical source. Owner ruling 1b, 2026-10-12: model these as their own class, not as recommendation nodes of a new kind. statement is verbatim and is the only stored copy, as recommendation's is. identifier is used in the IRI. There is no remark: L1 3.0's remark is minted under a recommendation (its iriPattern) and hasRemark starts at one, so a remark of a practice needs L1 itself to change — proposed upstream, not patched here. Class IRI: http://smart.who.int/kg/implementation-practice. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/smart.who.int.base|current/StructureDefinition/StructureDefinition-KGImplementationPractice.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-KGImplementationPractice.csv), [Excel](StructureDefinition-KGImplementationPractice.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "KGImplementationPractice",
  "url" : "http://smart.who.int/base/StructureDefinition/KGImplementationPractice",
  "version" : "0.3.0",
  "name" : "KGImplementationPractice",
  "title" : "Knowledge graph L1-LIBRARY: Implementation practice",
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
  "description" : "A statement of how to put guidance into practice, printed in a publication whose publicationType is implementation-guidance or methodology: the handbook's \"products that are not guidelines\" (§1.9), a \"how to\" document that makes no recommendations of its own. Not a recommendation, and not a good practice statement — both are made by a guideline and approved by the GRC; this is neither. It carries no kind, direction, strength or certainty, because nothing graded it. A handbook's own \"Best practices\" lists are the typical source. Owner ruling 1b, 2026-10-12: model these as their own class, not as recommendation nodes of a new kind. statement is verbatim and is the only stored copy, as recommendation's is. identifier is used in the IRI. There is no remark: L1 3.0's remark is minted under a recommendation (its iriPattern) and hasRemark starts at one, so a remark of a practice needs L1 itself to change — proposed upstream, not patched here. Class IRI: http://smart.who.int/kg/implementation-practice.",
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "http://smart.who.int/base/StructureDefinition/KGImplementationPractice",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "KGImplementationPractice",
      "path" : "KGImplementationPractice",
      "short" : "Knowledge graph L1-LIBRARY: Implementation practice",
      "definition" : "A statement of how to put guidance into practice, printed in a publication whose publicationType is implementation-guidance or methodology: the handbook's \"products that are not guidelines\" (§1.9), a \"how to\" document that makes no recommendations of its own. Not a recommendation, and not a good practice statement — both are made by a guideline and approved by the GRC; this is neither. It carries no kind, direction, strength or certainty, because nothing graded it. A handbook's own \"Best practices\" lists are the typical source. Owner ruling 1b, 2026-10-12: model these as their own class, not as recommendation nodes of a new kind. statement is verbatim and is the only stored copy, as recommendation's is. identifier is used in the IRI. There is no remark: L1 3.0's remark is minted under a recommendation (its iriPattern) and hasRemark starts at one, so a remark of a practice needs L1 itself to change — proposed upstream, not patched here. Class IRI: http://smart.who.int/kg/implementation-practice."
    },
    {
      "id" : "KGImplementationPractice.identifier",
      "path" : "KGImplementationPractice.identifier",
      "short" : "Identifier",
      "definition" : "The key the extraction gives it (e.g. NPC-R06), or the printed number where the publication numbers its practices; used in the IRI.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    },
    {
      "id" : "KGImplementationPractice.statement",
      "path" : "KGImplementationPractice.statement",
      "short" : "Statement",
      "definition" : "The practice, VERBATIM; the only stored copy.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "markdown"
      }]
    },
    {
      "id" : "KGImplementationPractice.contentHash",
      "path" : "KGImplementationPractice.contentHash",
      "short" : "Content hash",
      "definition" : "sha256 of the normalised statement; unchanged on re-extraction means current.",
      "min" : 0,
      "max" : "1",
      "type" : [{
        "code" : "string"
      }]
    }]
  }
}

```
