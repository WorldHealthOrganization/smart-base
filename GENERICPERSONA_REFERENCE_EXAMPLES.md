# GenericPersona Reference Examples - Canonical References and Choice Types

This document provides specific examples for the GenericPersona component showing how to support **either inline instances OR canonical/URI references**.

## Key Clarification

The examples show references using:
- **Canonical URLs** (e.g., `http://smart.who.int/base/GenericPersona/community-health-worker`)
- **Relative canonical references** (e.g., `GenericPersona/midwife`)
- **Absolute URI references** to external resources

This is different from just file path references - these are proper FHIR-style canonical identifiers.

## Current GenericPersona Structure

```fsh
Logical: GenericPersona
Title: "Generic Persona (DAK)"
Description: "..."

* ^status = #active
* title 1..1 string "Title" "Title of the persona"
* id 1..1 id "Persona ID" "Identifier for the persona"
* description[x] 1..1 string or uri "Description" "Description of the persona"
* otherNames 0..* string "Other Names/Examples" "Other names or examples for the persona"
* iscoCode 0..* code "ISCO Code" "ISCO-08 codes for occupation classification"
* iscoCode from ISCO08ValueSet (extensible)
```

---

## Option 1: Choice Type with URL (Simple References)

### FSH Change to GenericPersona
```fsh
// No changes to GenericPersona.fsh needed
```

### FSH Change to DAK.fsh
```fsh
// Change from:
* personas 0..* GenericPersona "Generic Personas" "..."

// To:
* personas[x] 0..* GenericPersona or url "Generic Personas" "Persona instances or canonical references"
```

### Example JSON Instance
```json
{
  "resourceType": "DAK",
  "id": "smart.who.int.anc",
  "name": "ANC",
  
  "personasGenericPersona": [
    {
      "id": "P01",
      "title": "Community Health Worker",
      "description": "Provides basic ANC services at community level",
      "otherNames": ["CHW", "Village Health Worker"],
      "iscoCode": ["3253"]
    },
    {
      "id": "P02",
      "title": "Midwife",
      "description": "Provides skilled maternal care",
      "iscoCode": ["2222"]
    }
  ],
  
  "personasUrl": [
    "http://smart.who.int/base/GenericPersona/clinical-officer",
    "http://smart.who.int/ig-library/GenericPersona/nurse-practitioner",
    "GenericPersona/anc-coordinator"
  ]
}
```

### Pros
- ✅ Uses canonical URLs (proper FHIR references)
- ✅ Supports absolute and relative references
- ✅ Native FHIR choice type

### Cons
- ⚠️ Verbose JSON field names (`personasGenericPersona`, `personasUrl`)
- ⚠️ Two separate arrays for inline vs referenced

---

## Option 2: Choice Type with Reference (FHIR Reference Objects)

### FSH Change to GenericPersona
```fsh
// No changes to GenericPersona.fsh needed
```

### FSH Change to DAK.fsh
```fsh
// Change from:
* personas 0..* GenericPersona "Generic Personas" "..."

// To:
* personas[x] 0..* GenericPersona or Reference(GenericPersona) "Generic Personas" "Persona instances or references"
```

### Example JSON Instance
```json
{
  "resourceType": "DAK",
  "id": "smart.who.int.anc",
  "name": "ANC",
  
  "personasGenericPersona": [
    {
      "id": "P01",
      "title": "Community Health Worker",
      "description": "Provides basic ANC services at community level",
      "otherNames": ["CHW", "Village Health Worker"],
      "iscoCode": ["3253"]
    }
  ],
  
  "personasReference": [
    {
      "reference": "http://smart.who.int/base/GenericPersona/clinical-officer",
      "display": "Clinical Officer"
    },
    {
      "reference": "GenericPersona/midwife",
      "display": "Midwife"
    },
    {
      "reference": "http://smart.who.int/ig-library/GenericPersona/nurse-practitioner"
    }
  ]
}
```

### Pros
- ✅ Standard FHIR Reference pattern
- ✅ Can include display text
- ✅ Supports canonical URLs
- ✅ Can support contained resources

### Cons
- ⚠️ More complex JSON structure (nested objects)
- ⚠️ Verbose field names
- ⚠️ Two separate arrays

---

## Option 3: Backbone Element with Content Choice

### FSH Change to GenericPersona
```fsh
// No changes to GenericPersona.fsh needed
```

### FSH Change to DAK.fsh
```fsh
// Change from:
* personas 0..* GenericPersona "Generic Personas" "..."

// To:
* personas 0..* BackboneElement "Generic Personas" "Persona instances or references"
  * content[x] 1..1 GenericPersona or canonical "Content" "Either inline persona or canonical reference"
```

### Example JSON Instance
```json
{
  "resourceType": "DAK",
  "id": "smart.who.int.anc",
  "name": "ANC",
  
  "personas": [
    {
      "contentGenericPersona": {
        "id": "P01",
        "title": "Community Health Worker",
        "description": "Provides basic ANC services at community level",
        "otherNames": ["CHW", "Village Health Worker"],
        "iscoCode": ["3253"]
      }
    },
    {
      "contentCanonical": "http://smart.who.int/base/GenericPersona/clinical-officer"
    },
    {
      "contentCanonical": "GenericPersona/midwife"
    },
    {
      "contentCanonical": "http://smart.who.int/ig-library/GenericPersona/nurse-practitioner"
    }
  ]
}
```

### Pros
- ✅ Single array with uniform structure
- ✅ Clear that each entry is either inline or reference
- ✅ Uses FHIR canonical type for proper URL references
- ✅ Easy to iterate through all personas

### Cons
- ⚠️ Extra nesting level
- ⚠️ Not a standard FHIR pattern
- ⚠️ Still has verbose choice field names

---

## Option 4: Separate Arrays for Inline and Referenced

### FSH Change to GenericPersona
```fsh
// No changes to GenericPersona.fsh needed
```

### FSH Change to DAK.fsh
```fsh
// Change from:
* personas 0..* GenericPersona "Generic Personas" "..."

// To:
* personas 0..* GenericPersona "Generic Personas (Inline)" "Inline persona definitions"
* personasRef 0..* canonical "Generic Persona References" "Canonical references to external personas"
```

### Example JSON Instance
```json
{
  "resourceType": "DAK",
  "id": "smart.who.int.anc",
  "name": "ANC",
  
  "personas": [
    {
      "id": "P01",
      "title": "Community Health Worker",
      "description": "Provides basic ANC services at community level",
      "otherNames": ["CHW", "Village Health Worker"],
      "iscoCode": ["3253"]
    },
    {
      "id": "P02",
      "title": "Midwife",
      "description": "Provides skilled maternal care",
      "iscoCode": ["2222"]
    }
  ],
  
  "personasRef": [
    "http://smart.who.int/base/GenericPersona/clinical-officer",
    "GenericPersona/anc-coordinator",
    "http://smart.who.int/ig-library/GenericPersona/nurse-practitioner"
  ]
}
```

### Pros
- ✅ Simplest JSON structure
- ✅ Clear separation between inline and referenced
- ✅ Uses canonical type for proper URL references
- ✅ Easy to process: check two arrays
- ✅ No verbose choice type names

### Cons
- ⚠️ Doubles the number of fields in DAK.fsh
- ⚠️ Two arrays to check when getting all personas

---

## Option 5: Add Reference Field to GenericPersona (Recommended for Canonical)

### FSH Change to GenericPersona
```fsh
Logical: GenericPersona
Title: "Generic Persona (DAK)"
Description: "..."

* ^status = #active
* reference 0..1 canonical "Canonical Reference" "Canonical URL referencing an external GenericPersona instance. When present, other fields provide metadata only."
* title 1..1 string "Title" "Title of the persona"
* id 1..1 id "Persona ID" "Identifier for the persona"
* description[x] 1..1 string or uri "Description" "Description of the persona"
* otherNames 0..* string "Other Names/Examples" "Other names or examples for the persona"
* iscoCode 0..* code "ISCO Code" "ISCO-08 codes for occupation classification"
* iscoCode from ISCO08ValueSet (extensible)
```

### FSH Change to DAK.fsh
```fsh
// No changes needed - personas remains:
* personas 0..* GenericPersona "Generic Personas" "..."
```

### Example JSON Instance
```json
{
  "resourceType": "DAK",
  "id": "smart.who.int.anc",
  "name": "ANC",
  
  "personas": [
    {
      "id": "P01",
      "title": "Community Health Worker",
      "description": "Provides basic ANC services at community level",
      "otherNames": ["CHW", "Village Health Worker"],
      "iscoCode": ["3253"]
    },
    {
      "id": "P02",
      "title": "Midwife",
      "reference": "http://smart.who.int/base/GenericPersona/midwife"
    },
    {
      "id": "P03",
      "title": "Clinical Officer",
      "reference": "GenericPersona/clinical-officer"
    },
    {
      "id": "P04",
      "reference": "http://smart.who.int/ig-library/GenericPersona/nurse-practitioner"
    }
  ]
}
```

### Pros
- ✅ **Best for canonical references** - uses proper FHIR canonical type
- ✅ Single array, clean JSON structure
- ✅ Can provide metadata (id, title) alongside reference
- ✅ No changes to DAK.fsh needed
- ✅ Consistent pattern across all components

### Cons
- ⚠️ Need to modify GenericPersona.fsh and all other component models
- ⚠️ Need validation: what if both reference and full data are present?

---

## Option 6: Extend Source Pattern with Canonical Support

### FSH Change to GenericPersona
```fsh
Logical: GenericPersona
Title: "Generic Persona (DAK)"
Description: "..."

* ^status = #active
* source 0..1 uri "Source" "URI or canonical reference to an external GenericPersona instance. When present, other fields provide metadata only."
* title 1..1 string "Title" "Title of the persona"
* id 1..1 id "Persona ID" "Identifier for the persona"
* description[x] 1..1 string or uri "Description" "Description of the persona"
* otherNames 0..* string "Other Names/Examples" "Other names or examples for the persona"
* iscoCode 0..* code "ISCO Code" "ISCO-08 codes for occupation classification"
* iscoCode from ISCO08ValueSet (extensible)
```

### FSH Change to DAK.fsh
```fsh
// No changes needed - personas remains:
* personas 0..* GenericPersona "Generic Personas" "..."
```

### Example JSON Instance
```json
{
  "resourceType": "DAK",
  "id": "smart.who.int.anc",
  "name": "ANC",
  
  "personas": [
    {
      "id": "P01",
      "title": "Community Health Worker",
      "description": "Provides basic ANC services at community level",
      "otherNames": ["CHW", "Village Health Worker"],
      "iscoCode": ["3253"]
    },
    {
      "id": "P02",
      "title": "Midwife",
      "source": "http://smart.who.int/base/GenericPersona/midwife"
    },
    {
      "id": "P03",
      "title": "Clinical Officer",
      "source": "GenericPersona/clinical-officer"
    },
    {
      "id": "P04",
      "source": "http://smart.who.int/ig-library/GenericPersona/nurse-practitioner"
    }
  ]
}
```

### Pros
- ✅ Consistent with existing source pattern
- ✅ Single array, clean JSON structure
- ✅ Can provide metadata alongside reference
- ✅ No changes to DAK.fsh needed
- ✅ Uses uri type (supports both URLs and canonical)

### Cons
- ⚠️ Semantic overloading if source already means something else
- ⚠️ Less explicit than "reference" or "canonical"

---

## Comparison: Which Option Best Supports Canonical References?

| Option | Canonical Support | JSON Clarity | DAK.fsh Changes | Component Changes | Best For |
|--------|------------------|--------------|-----------------|-------------------|----------|
| **1. Choice URL** | ⭐⭐⭐ url type | ⭐⭐ | Yes - choice types | None | Simple URLs |
| **2. Choice Reference** | ⭐⭐⭐⭐⭐ Reference() | ⭐⭐ | Yes - choice types | None | Standard FHIR |
| **3. Backbone Choice** | ⭐⭐⭐⭐⭐ canonical | ⭐⭐⭐⭐ | Yes - backbone | None | Uniform structure |
| **4. Separate Arrays** | ⭐⭐⭐⭐⭐ canonical | ⭐⭐⭐⭐⭐ | Yes - new field | None | Explicit separation |
| **5. Reference Field** | ⭐⭐⭐⭐⭐ canonical | ⭐⭐⭐⭐⭐ | None | Add reference field | **Canonical references** |
| **6. Source Field** | ⭐⭐⭐⭐ uri | ⭐⭐⭐⭐⭐ | None | Add/update source | Consistency |

## Recommendation for Canonical References

### Primary: **Option 5 - Add Reference Field with Canonical Type**

This is the **best option for proper canonical references** because:

1. ✅ Uses FHIR `canonical` data type designed for this purpose
2. ✅ Cleanest JSON with single array
3. ✅ Supports both absolute and relative canonical references
4. ✅ Can include minimal metadata (id, title) with reference
5. ✅ No changes to DAK.fsh structure

**Implementation:**
```fsh
// In GenericPersona.fsh (and all other component models):
* reference 0..1 canonical "Canonical Reference" "Canonical URL to external instance"
```

### Alternative: **Option 4 - Separate Arrays with Canonical Type**

If explicit separation is preferred:

1. ✅ Very clear: inline personas in one array, references in another
2. ✅ Uses canonical type for proper URL handling
3. ✅ Simplest processing logic
4. ❌ Requires modifying DAK.fsh (adds 9 new fields)

**Implementation:**
```fsh
// In DAK.fsh:
* personas 0..* GenericPersona "Generic Personas (Inline)"
* personasRef 0..* canonical "Generic Persona References"
```

## Processing Canonical References

### Resolving References (Pseudocode)

```javascript
async function getAllPersonas(dak) {
  const personas = [];
  
  for (const persona of dak.personas) {
    if (persona.reference) {
      // Option 5: resolve canonical reference
      const canonical = persona.reference;
      const resolved = await resolveCanonical(canonical);
      
      // Merge any metadata from inline with resolved data
      const merged = {
        ...resolved,
        id: persona.id || resolved.id,
        title: persona.title || resolved.title
      };
      personas.push(merged);
    } else {
      // Use inline persona
      personas.push(persona);
    }
  }
  
  return personas;
}

async function resolveCanonical(canonical) {
  // Handle different canonical formats:
  
  if (canonical.startsWith('http://') || canonical.startsWith('https://')) {
    // Absolute canonical URL
    return await fetch(canonical + '.json');
  } else {
    // Relative reference like "GenericPersona/midwife"
    // Resolve relative to base URL
    const baseUrl = 'http://smart.who.int/base';
    return await fetch(`${baseUrl}/${canonical}.json`);
  }
}
```

## Summary

For supporting **canonical IDs/URIs** (not just file paths), the best options are:

1. **Option 5** (Reference field with canonical type) - Best for clean JSON and proper FHIR canonical support
2. **Option 4** (Separate arrays with canonical type) - Best for explicit separation
3. **Option 3** (Backbone with canonical type) - Good for uniform structure
4. **Option 2** (Reference objects) - Most FHIR-standard but more verbose

All these options properly support:
- Absolute canonical URLs: `http://smart.who.int/base/GenericPersona/midwife`
- Relative canonical references: `GenericPersona/midwife`
- Cross-IG references: `http://smart.who.int/ig-library/GenericPersona/nurse`
