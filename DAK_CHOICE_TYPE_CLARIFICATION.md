# DAK Choice Type Clarification - Corrected Approach

## Important Design Clarification

**Source field should NOT be inside the Logical Model** (except for specific data elements like `description[x]`).

The `source` field would be used to load instance data by resolving the URL, which creates modeling issues because you wouldn't know the values of required fields before loading the content referenced in source.

## Corrected Approach: Three Data Types Only

Each GenericPersona (and other DAK components) should be **exactly one of three data types**:

1. **URL** - Absolute or relative to `input/` directory where the definition (as FSH or JSON) can be retrieved
2. **Canonical** - FHIR canonical reference
3. **Instance Data** - Inline GenericPersona instance data

## FSH Implementation Options

### Option 1: Choice Type (url or canonical or GenericPersona)

**DAK.fsh:**
```fsh
// Current:
* personas 0..* GenericPersona "Generic Personas" "Depiction of the human and system actors"

// Change to:
* personas[x] 0..* url or canonical or GenericPersona "Generic Personas" "Each persona is either: (1) URL to retrieve definition from input/ directory or external source, (2) canonical reference, or (3) inline GenericPersona instance data"
```

**GenericPersona.fsh:**
```fsh
// NO CHANGES - Do not add source field
Logical: GenericPersona
Title: "Generic Persona (DAK)"
Description: "Logical Model for representing Generic Personas from a DAK. Depiction of the human and system actors."

* ^status = #active
* title 1..1 string "Title" "Title of the persona"
* id 1..1 id "Persona ID" "Identifier for the persona"
* description[x] 1..1 string or uri "Description" "Description of the persona - either Markdown content or a URI to a Markdown file"
* otherNames 0..* string "Other Names/Examples" "Other names or examples for the persona"
* iscoCode 0..* code "ISCO Code" "ISCO-08 codes for occupation classification"
* iscoCode from ISCO08ValueSet (extensible)
```

**Resulting JSON structure:**
```json
{
  "resourceType": "DAK",
  "id": "smart.who.int.anc",
  
  "personasUrl": [
    "input/personas/community-health-worker.json",
    "http://external.org/personas/midwife.fsh"
  ],
  
  "personasCanonical": [
    "http://smart.who.int/base/GenericPersona/clinical-officer",
    "GenericPersona/nurse-practitioner"
  ],
  
  "personasGenericPersona": [
    {
      "id": "P01",
      "title": "ANC Coordinator",
      "description": "Coordinates antenatal care services",
      "iscoCode": ["1342"]
    }
  ]
}
```

### Option 2: Three Separate Arrays

**DAK.fsh:**
```fsh
// Current:
* personas 0..* GenericPersona "Generic Personas" "Depiction of the human and system actors"

// Change to:
* personasUrl 0..* url "Persona URLs" "URLs (absolute or relative to input/) to retrieve persona definitions"
* personasCanonical 0..* canonical "Persona Canonical References" "Canonical references to external personas"
* personas 0..* GenericPersona "Inline Personas" "Inline GenericPersona instance data"
```

**GenericPersona.fsh:**
```fsh
// NO CHANGES - Do not add source field
```

**Resulting JSON structure:**
```json
{
  "resourceType": "DAK",
  "id": "smart.who.int.anc",
  
  "personasUrl": [
    "input/personas/community-health-worker.json",
    "http://external.org/personas/midwife.fsh"
  ],
  
  "personasCanonical": [
    "http://smart.who.int/base/GenericPersona/clinical-officer",
    "GenericPersona/nurse-practitioner"
  ],
  
  "personas": [
    {
      "id": "P01",
      "title": "ANC Coordinator",
      "description": "Coordinates antenatal care services",
      "iscoCode": ["1342"]
    }
  ]
}
```

### Option 3: BackboneElement with Choice

**DAK.fsh:**
```fsh
// Current:
* personas 0..* GenericPersona "Generic Personas" "Depiction of the human and system actors"

// Change to:
* personas 0..* BackboneElement "Generic Personas" "Persona definitions via URL, canonical, or inline data"
  * definition[x] 1..1 url or canonical or GenericPersona "Persona Definition" "Either URL, canonical reference, or inline instance"
```

**GenericPersona.fsh:**
```fsh
// NO CHANGES - Do not add source field
```

**Resulting JSON structure:**
```json
{
  "resourceType": "DAK",
  "id": "smart.who.int.anc",
  
  "personas": [
    {
      "definitionUrl": "input/personas/community-health-worker.json"
    },
    {
      "definitionCanonical": "http://smart.who.int/base/GenericPersona/clinical-officer"
    },
    {
      "definitionGenericPersona": {
        "id": "P01",
        "title": "ANC Coordinator",
        "description": "Coordinates antenatal care services",
        "iscoCode": ["1342"]
      }
    }
  ]
}
```

## Canonical Derivation from Relative URLs

**Important Note:** When a relative URL to `input/` is used (e.g., `input/personas/midwife.json`), the canonical can be derived based on:

1. The deployment URL to gh-pages
2. What is in the repository's `dak.json`
3. FHIR IG Publisher rules for each directory under `input/`

This should be implemented as a **central service** that determines the DAK's deploy URL and derives the canonical ID of an asset under `input/`.

### FHIR IG Publisher Rules

According to FHIR IG Publisher conventions:
- Resources in `input/` directories map to canonical URLs based on the IG's base URL
- Each resource type has its own directory (e.g., `input/personas/`, `input/indicators/`)
- The canonical URL is typically: `{baseUrl}/{ResourceType}/{id}`
- Example: `input/personas/midwife.json` → `http://smart.who.int/base/GenericPersona/midwife`

## Processing Logic

```javascript
async function loadPersona(personaDefinition) {
  if (typeof personaDefinition === 'string') {
    if (personaDefinition.startsWith('http://') || personaDefinition.startsWith('https://')) {
      if (isCanonical(personaDefinition)) {
        // Canonical reference - resolve to instance
        return await resolveCanonical(personaDefinition);
      } else {
        // Absolute URL - fetch directly
        return await fetch(personaDefinition);
      }
    } else if (personaDefinition.startsWith('input/')) {
      // Relative URL to input/ directory
      // Derive canonical from deployment URL
      const canonical = deriveCanonicalFromInputPath(personaDefinition);
      return await resolveCanonical(canonical);
    } else {
      // Assume it's a relative canonical reference
      return await resolveCanonical(personaDefinition);
    }
  } else {
    // It's already instance data
    return personaDefinition;
  }
}

function deriveCanonicalFromInputPath(relativePath) {
  // Central service to derive canonical from input/ path
  // Example: input/personas/midwife.json → http://smart.who.int/base/GenericPersona/midwife
  const baseUrl = getDeploymentBaseUrl(); // From dak.json or config
  const resourceType = extractResourceType(relativePath); // e.g., "GenericPersona"
  const id = extractIdFromPath(relativePath); // e.g., "midwife"
  return `${baseUrl}/${resourceType}/${id}`;
}
```

## Recommendation

**Option 1 (Choice Type)** is recommended because:
1. ✅ Single field in DAK.fsh
2. ✅ Clear three-way choice matches the design intent
3. ✅ FHIR native choice type pattern
4. ✅ Handles all three data types explicitly

**Option 2 (Three Separate Arrays)** is also viable if:
- Explicit separation of concerns is more important
- Processing each type separately is preferred
- JSON clarity is prioritized over single field

## Key Takeaways

1. **Do NOT add `source` field to GenericPersona or other component Logical Models**
2. **Each component is one of three types**: URL, canonical, or instance data
3. **Relative URLs to `input/`** enable canonical derivation via central service
4. **FHIR IG Publisher conventions** determine canonical URL patterns
5. **Central service needed** for deriving canonicals from `input/` paths
