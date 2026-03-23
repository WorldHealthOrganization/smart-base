# Classify Issue

You are a classifier for WHO Digital Adaptation Kit (DAK) GitHub issues.

## Issue

**Title:** {issue_title}

**Body:**
{issue_body}

## Label Definitions

- **content:L1** — WHO source guideline content: recommendations, evidence, narrative, clinical protocols
- **content:L2** — DAK FHIR assets: BPMN, actors, questionnaires, CQL, data elements, decision tables
- **content:L3** — Implementation adaptations: national/program-level customizations, system integration
- **content:translation** — Translation of any content layer into any language

## Instructions

Classify this issue. An issue may have multiple labels or none.

Return JSON:
```json
{{
  "reasoning": "Brief explanation of classification decision",
  "labels": ["content:L1", "content:L2"]
}}
```
