# Validate DAK Structure

Review the DAK repository structure for completeness and correctness.

## Repository Root

{ig_root}

## Files Found

{file_listing}

## Validation Results

{validation_results}

## Instructions

Check:
1. Required directories exist (input/fsh/, input/business-processes/, etc.)
2. sushi-config.yaml is present and valid
3. All referenced profiles and extensions exist
4. No broken cross-references between BPMN lanes and ActorDefinition files

Return your analysis as JSON:
```json
{{
  "valid": true/false,
  "summary": "...",
  "issues": [
    {{"severity": "...", "message": "...", "fix": "..."}}
  ]
}}
```
