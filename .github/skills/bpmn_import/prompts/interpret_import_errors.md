# Interpret Import Errors

You are helping a DAK author understand errors from the BPMN import pipeline.

## Import Output

{import_output}

## Errors Found

{error_list}

## Instructions

For each error:
1. Explain what went wrong in plain language.
2. Identify the likely cause (missing actor, malformed BPMN, XSLT issue).
3. Suggest a concrete fix the author can apply.

Return your analysis as JSON:
```json
{{
  "summary": "...",
  "errors": [
    {{"code": "...", "message": "...", "cause": "...", "fix": "..."}}
  ]
}}
```
