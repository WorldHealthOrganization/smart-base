# StructureDefinition-PatientSummary API Documentation

<!-- This content is automatically generated from StructureDefinition-PatientSummary.openapi.json -->

## API Information

**Patient Summary Logical Model API**

Logical model for patient summary information

**Version:** 1.0.0

## Endpoints

### GET /StructureDefinition-PatientSummary.schema.json

**JSON Schema definition for the Logical Model StructureDefinition-PatientSummary**

This endpoint serves the JSON Schema definition for the Logical Model StructureDefinition-PatientSummary.

## Schema Definition

### StructureDefinition-PatientSummary

**Description:** Logical model for patient summary information

**Type:** object

**Schema ID:** [https://worldhealthorganization.github.io/smart-base/StructureDefinition-PatientSummary.schema.json](https://worldhealthorganization.github.io/smart-base/StructureDefinition-PatientSummary.schema.json)

**FHIR Page:** [View full FHIR definition](StructureDefinition-PatientSummary.html)

**Properties:**

- **id** (string): Unique identifier for the patient
- **name** (string): Full name of the patient
- **age** (integer): Age of the patient in years
- **diagnosis** (array): List of current diagnoses

**Required fields:** id, name

<details>
<summary>Full Schema (JSON)</summary>

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://worldhealthorganization.github.io/smart-base/StructureDefinition-PatientSummary.schema.json",
  "title": "Patient Summary Logical Model",
  "description": "Logical model for patient summary information",
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "description": "Unique identifier for the patient"
    },
    "name": {
      "type": "string",
      "description": "Full name of the patient"
    },
    "age": {
      "type": "integer",
      "description": "Age of the patient in years"
    },
    "diagnosis": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "List of current diagnoses"
    }
  },
  "required": [
    "id",
    "name"
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
