# ValueSet-ExampleCodes API Documentation

<!-- This content is automatically generated from ValueSet-ExampleCodes.openapi.json -->

## API Information

**Example ValueSet API**

An example ValueSet for testing

**Version:** 1.0.0

## Endpoints

### GET /ValueSet-ExampleCodes.schema.json

**JSON Schema definition for the enumeration ValueSet-ExampleCodes**

This endpoint serves the JSON Schema definition for the enumeration ValueSet-ExampleCodes.

## Schema Definition

### ValueSet-ExampleCodes

**Description:** An example ValueSet for testing

**Type:** object

**Schema ID:** [ValueSet-ExampleCodes.schema.json](ValueSet-ExampleCodes.schema.json)

**FHIR Page:** [View full FHIR definition](ValueSet-ExampleCodes.html)

**Properties:**

- **code** (string): Example codes
<details>
<summary>Full Schema (JSON)</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "ValueSet-ExampleCodes.schema.json",
  "title": "Example ValueSet",
  "description": "An example ValueSet for testing",
  "type": "object",
  "properties": {
    "code": {
      "type": "string",
      "enum": [
        "example1",
        "example2",
        "example3"
      ],
      "description": "Example codes"
    }
  }
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
