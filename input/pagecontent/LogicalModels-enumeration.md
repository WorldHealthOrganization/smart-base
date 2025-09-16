# LogicalModels-enumeration API Documentation

<!-- This content is automatically generated from LogicalModels-enumeration.openapi.json -->

## API Information

**LogicalModels Enumeration API**

API endpoint providing an enumeration of all available Logical Model schemas

**Version:** 1.0.0

## Endpoints

### GET /LogicalModels.schema.json

**Get enumeration of all Logical Model schemas**

Returns a list of all available Logical Model schemas with metadata

## Schema Definition

### EnumerationResponse

**Description:** JSON Schema defining the structure of the Logical Model enumeration endpoint response

**Type:** object

**Schema ID:** [#/LogicalModels.schema.json](#/LogicalModels.schema.json)

**FHIR Page:** [View full FHIR definition](artifacts.html#structures-logical-models)

**Properties:**

- **type** (string): The type of schemas enumerated (logical_model)
- **count** (integer): Total number of schemas available
- **schemas** (array): Array of available schemas

**Required fields:** type, count, schemas

<details>
<summary>Full Schema (JSON)</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "#/LogicalModels.schema.json",
  "title": "Logical Model Enumeration Schema",
  "description": "JSON Schema defining the structure of the Logical Model enumeration endpoint response",
  "type": "object",
  "properties": {
    "type": {
      "type": "string",
      "const": "logical_model",
      "description": "The type of schemas enumerated (logical_model)"
    },
    "count": {
      "type": "integer",
      "description": "Total number of schemas available"
    },
    "schemas": {
      "type": "array",
      "description": "Array of available schemas",
      "items": {
        "type": "object",
        "properties": {
          "filename": {
            "type": "string",
            "description": "Schema filename"
          },
          "id": {
            "type": "string",
            "description": "Schema $id"
          },
          "title": {
            "type": "string",
            "description": "Schema title"
          },
          "description": {
            "type": "string",
            "description": "Schema description"
          },
          "url": {
            "type": "string",
            "description": "Relative URL to the schema file"
          },
          "logicalModelUrl": {
            "type": "string",
            "description": "FHIR canonical URL of the Logical Model"
          },
          "propertyCount": {
            "type": "integer",
            "description": "Number of properties in the Logical Model"
          }
        },
        "required": [
          "filename",
          "title",
          "url"
        ]
      }
    }
  },
  "required": [
    "type",
    "count",
    "schemas"
  ],
  "example": {
    "type": "logical_model",
    "count": 1,
    "schemas": [
      {
        "filename": "StructureDefinition-ExampleDAKModel.schema.json",
        "id": "http://smart.who.int/base/StructureDefinition-ExampleDAKModel.schema.json",
        "title": "Example DAK Model",
        "description": "An example logical model for DAK API testing",
        "url": "./StructureDefinition-ExampleDAKModel.schema.json",
        "logicalModelUrl": "http://smart.who.int/base/StructureDefinition/ExampleDAKModel",
        "propertyCount": 2
      }
    ]
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
