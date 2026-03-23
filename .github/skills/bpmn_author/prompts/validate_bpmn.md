# Validate BPMN

Review the following BPMN XML for compliance with WHO DAK constraints.

## BPMN XML

```xml
{bpmn_xml}
```

## Validation Results (structural)

{validation_results}

## Instructions

Summarize the validation findings. For each issue:
1. Explain what is wrong and why it matters for DAK compliance.
2. Suggest a specific fix.

If there are no issues, confirm the BPMN is valid.
Return your analysis as JSON:
```json
{{
  "valid": true/false,
  "summary": "...",
  "issues": [
    {{"code": "...", "severity": "...", "message": "...", "fix": "..."}}
  ]
}}
```
