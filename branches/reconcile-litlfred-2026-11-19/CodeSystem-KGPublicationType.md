# Knowledge graph L1: publication type - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Knowledge graph L1: publication type**

## CodeSystem: Knowledge graph L1: publication type 

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/CodeSystem/KGPublicationType | *Version*:0.3.0 |
| Active as of 2026-11-23 | *Computable Name*:KGPublicationType |

 
What kind of publication this is. The distinction that matters most for provenance is guideline versus not: a summary table or position paper restates recommendations made elsewhere, and a §1.9 product makes none of its own. Conflating them makes a citation resolve to the wrong authority. Source: smart-kg ontology/l1/l1.json valueSets "publication-type"; WHO handbook for guideline development (2014), Table 1.2 and §1.7–1.9; the BCG decision table's citation for summary-table; CDHIv2.fsh for classification. 

 This Code system is referenced in the content logical definition of the following value sets: 

* [Knowledge graph L1: publication type](ValueSet-KGPublicationTypeVS.md)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "KGPublicationType",
  "url" : "http://smart.who.int/base/CodeSystem/KGPublicationType",
  "version" : "0.3.0",
  "name" : "KGPublicationType",
  "title" : "Knowledge graph L1: publication type",
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
  "description" : "What kind of publication this is. The distinction that matters most for provenance is guideline versus not: a summary table or position paper restates recommendations made elsewhere, and a §1.9 product makes none of its own. Conflating them makes a citation resolve to the wrong authority. Source: smart-kg ontology/l1/l1.json valueSets \"publication-type\"; WHO handbook for guideline development (2014), Table 1.2 and §1.7–1.9; the BCG decision table's citation for summary-table; CDHIv2.fsh for classification.",
  "caseSensitive" : true,
  "content" : "complete",
  "count" : 14,
  "concept" : [{
    "code" : "standard-guideline",
    "display" : "Standard guideline",
    "definition" : "Recommendations on a specific topic or condition, usually new. Most WHO guidelines. Handbook §1.7.1."
  },
  {
    "code" : "consolidated-guideline",
    "display" : "Consolidated guideline",
    "definition" : "Aggregates existing recommendations on a disease or condition, evaluated as up to date; may add new ones. Existing recommendations must be explicitly cross-referenced. Handbook §1.7.2."
  },
  {
    "code" : "interim-guideline",
    "display" : "Interim guideline",
    "definition" : "Guidance when data are incomplete and more are expected; short shelf-life, states when an update is anticipated. Handbook §1.7.3."
  },
  {
    "code" : "rapid-advice-guideline",
    "display" : "Rapid advice guideline",
    "definition" : "Produced in one to three months in a public health emergency, with a review-by date. Handbook §1.7.4, chapter 11."
  },
  {
    "code" : "emergency-guideline",
    "display" : "Emergency guideline",
    "definition" : "Rapid response guidance within hours to days; may rest on expert opinion only. Handbook §1.7.4."
  },
  {
    "code" : "collaborative-guideline",
    "display" : "Collaborative guideline",
    "definition" : "Developed with one or more external organizations sharing the remit. Handbook §1.8.1."
  },
  {
    "code" : "external-guideline",
    "display" : "External guideline",
    "definition" : "Developed by an external organization and adopted by WHO. Handbook §1.8.2."
  },
  {
    "code" : "adapted-guideline",
    "display" : "Adapted guideline",
    "definition" : "An existing WHO guideline adapted to a local context by a Member State. Handbook §1.8.3, §13.1."
  },
  {
    "code" : "position-paper",
    "display" : "Position paper",
    "definition" : "A WHO position paper — for vaccines, the SAGE-reviewed statement of WHO's position published in the Weekly Epidemiological Record. States recommendations; the immunization summary tables are drawn from these."
  },
  {
    "code" : "summary-table",
    "display" : "Summary table",
    "definition" : "A tabular restatement of recommendations made in other publications — e.g. \"WHO recommendations for routine immunization – summary tables\". Cite-worthy, but not the originating authority: a citation resolving here should normally be followed on to the recommendation it restates."
  },
  {
    "code" : "classification",
    "display" : "Classification",
    "definition" : "A WHO classification, such as the Classification of Digital Health Interventions (CDHI). Its codes are cross-referenced through terminology-code, never modelled here."
  },
  {
    "code" : "implementation-guidance",
    "display" : "Implementation guidance",
    "definition" : "An operational manual, implementation guide or tool based on approved guidelines — a \"how to\" document. Makes no recommendations of its own. Handbook §1.9. A DAK is one of these."
  },
  {
    "code" : "methodology",
    "display" : "Methodology",
    "definition" : "A document describing how guidance is produced — the guideline development handbook itself. Handbook §1.9 (standard operating procedures)."
  },
  {
    "code" : "supplement",
    "display" : "Supplement",
    "definition" : "A web annex or supplementary document of another publication, typically holding systematic reviews, GRADE evidence profiles and evidence-to-decision tables. Handbook §12.1. Reached by hasSupplement."
  }]
}

```
