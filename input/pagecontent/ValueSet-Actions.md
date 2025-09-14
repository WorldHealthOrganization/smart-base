# ValueSet-Actions API Documentation

<!-- This content is automatically generated from ValueSet-Actions.openapi.json -->

## API Information

**Actions ValueSet API**

Actions that can be taken as part of the care process

**Version:** 1.0.0

## Endpoints

### GET /ValueSet-Actions.schema.json

**JSON Schema definition for the enumeration ValueSet-Actions**

This endpoint serves the JSON Schema definition for the enumeration ValueSet-Actions.

## Schema Definition

### ValueSet-Actions

**Description:** Actions that can be taken as part of the care process

**Type:** string

**Schema ID:** [https://worldhealthorganization.github.io/smart-base/ValueSet-Actions.schema.json](https://worldhealthorganization.github.io/smart-base/ValueSet-Actions.schema.json)

**FHIR Page:** [View full FHIR definition](ValueSet-Actions.html)

**Allowed values:**

<div class="enum-values">
<span class="enum-value">collect-information</span>
<span class="enum-value">create-order</span>
<span class="enum-value">dispense-medication</span>
<span class="enum-value">follow-up</span>
<span class="enum-value">provide-counseling</span>
<span class="enum-value">record-observation</span>
<span class="enum-value">schedule-appointment</span>
</div>

<details>
<summary>Full Schema (JSON)</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://worldhealthorganization.github.io/smart-base/ValueSet-Actions.schema.json",
  "title": "Actions ValueSet",
  "description": "Actions that can be taken as part of the care process",
  "type": "string",
  "enum": [
    "collect-information",
    "create-order",
    "dispense-medication",
    "follow-up",
    "provide-counseling",
    "record-observation",
    "schedule-appointment"
  ]
}
```

</details>


<style>
/* Schema documentation styling that integrates with IG theme */
.enum-values {
  background-color: #e7f3ff;
  border: 1px solid #b8daff;
  border-radius: 4px;
  padding: 1rem;
  margin: 1rem 0;
}

.enum-value {
  display: inline-block;
  background-color: #00477d;
  color: white;
  padding: 0.2rem 0.5rem;
  border-radius: 3px;
  margin: 0.2rem;
  font-size: 0.9rem;
  text-decoration: none;
}

.enum-value a {
  color: white;
  text-decoration: none;
}

.enum-value:hover, .enum-value a:hover {
  background-color: #0070A1;
  color: white;
  text-decoration: none;
}

.enum-truncated {
  margin-top: 0.5rem;
  font-style: italic;
  color: #6c757d;
}

details {
  margin: 1rem 0;
  border: 1px solid #dee2e6;
  border-radius: 4px;
  padding: 0;
}

details summary {
  background: #f8f9fa;
  padding: 0.75rem;
  cursor: pointer;
  border-bottom: 1px solid #dee2e6;
  font-weight: 500;
}

details[open] summary {
  border-bottom: 1px solid #dee2e6;
}

details pre {
  margin: 1rem;
  background: #f8f9fa;
  border: 1px solid #e9ecef;
  border-radius: 4px;
  padding: 1rem;
  overflow-x: auto;
}
</style>

---

*This documentation is automatically generated from the OpenAPI specification.*
