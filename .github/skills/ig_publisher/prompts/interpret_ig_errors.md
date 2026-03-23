# Interpret IG Publisher Errors

You are helping a FHIR Implementation Guide author understand build errors.

## Build Output

{build_output}

## Error Summary

{error_summary}

## Instructions

For each FATAL or ERROR finding:
1. Explain what went wrong in plain language.
2. Identify the likely cause (missing profile, invalid reference, FSH syntax, etc.).
3. Suggest a concrete fix.

For WARNINGs, briefly note whether they need attention.

Return your analysis as JSON:
```json
{{
  "summary": "...",
  "fatal_count": 0,
  "error_count": 0,
  "warning_count": 0,
  "findings": [
    {{
      "severity": "ERROR",
      "message": "...",
      "cause": "...",
      "fix": "..."
    }}
  ]
}}
```
