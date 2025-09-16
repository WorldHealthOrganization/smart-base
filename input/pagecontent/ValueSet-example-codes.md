# ValueSet-example-codes API Documentation

<!-- This content is automatically generated from ValueSet-example-codes.openapi.json -->

## API Information

**Example Codes for Testing Schema API**

JSON Schema for Example Codes for Testing ValueSet codes. Generated from FHIR expansions using IRI format.

**Version:** 1.0.0

## Endpoints

### GET /ValueSet-example-codes.schema.json

**JSON Schema definition for the enumeration ValueSet-example-codes**

This endpoint serves the JSON Schema definition for the enumeration ValueSet-example-codes.

## Schema Definition

### ValueSet-example-codes

**Description:** JSON Schema for Example Codes for Testing ValueSet codes. Generated from FHIR expansions using IRI format.

**Type:** string

**Schema ID:** [http://smart.who.int/base/ValueSet-example-codes.schema.json](http://smart.who.int/base/ValueSet-example-codes.schema.json)

**FHIR Page:** [View full FHIR definition](ValueSet-example-codes.html)

**Allowed values:**

<div class="enum-values">
<span class="enum-value">http://example.org/codes#test1</span>
<span class="enum-value">http://example.org/codes#test2</span>
</div>

<details>
<summary>Full Schema (JSON)</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "http://smart.who.int/base/ValueSet-example-codes.schema.json",
  "title": "Example Codes for Testing Schema",
  "description": "JSON Schema for Example Codes for Testing ValueSet codes. Generated from FHIR expansions using IRI format.",
  "type": "string",
  "enum": [
    "http://example.org/codes#test1",
    "http://example.org/codes#test2"
  ],
  "narrative": "This schema validates IRI-formatted codes for the Example Codes for Testing ValueSet. Each enum value includes the system URI in the format {systemuri}#{code} to match JSON-LD enumeration IRIs. Display values are available at http://smart.who.int/base/ValueSet-example-codes.displays.json. For a complete listing of all ValueSets, see artifacts.html#terminology-value-sets.",
  "fhir:displays": "http://smart.who.int/base/ValueSet-example-codes.displays.json",
  "fhir:valueSet": "http://smart.who.int/base/ValueSet/example-codes",
  "fhir:expansionTimestamp": "2024-01-01T00:00:00Z"
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
