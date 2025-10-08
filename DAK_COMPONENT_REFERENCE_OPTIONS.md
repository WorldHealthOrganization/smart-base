# Options for Allowing References to Component Instances in DAK Logical Model

## Background

The current DAK Logical Model (https://worldhealthorganization.github.io/smart-base/StructureDefinition-DAK.html) defines 9 component types that are embedded inline:

- `healthInterventions 0..* HealthInterventions`
- `personas 0..* GenericPersona`
- `userScenarios 0..* UserScenario`
- `businessProcesses 0..* BusinessProcessWorkflow`
- `dataElements 0..* CoreDataElement`
- `decisionLogic 0..* DecisionSupportLogic`
- `indicators 0..* ProgramIndicator`
- `requirements 0..* Requirements`
- `testScenarios 0..* TestScenario`

The requirement is to allow each component to be **either**:
1. An inline instance of the component (current behavior)
2. A URL reference to an external instance of that component

### Important Context

**Existing Precedent**: Three component models already use fields pointing to external files:
- `DecisionSupportLogic.source` (1..1 uri) - links to DMN files containing decision logic
- `BusinessProcessWorkflow.source` (1..1 uri) - links to BPMN files containing workflow definitions
- `TestScenario.feature` (1..1 uri) - links to feature files containing test scenarios

These fields point to **machine-readable definitions** (DMN/BPMN/feature files), not component instances. The current requirement is about referencing **component instances themselves** (e.g., a JSON file containing a complete ProgramIndicator instance).

**Component External Reference Status:**

| Component | Current External Field | Purpose |
|-----------|----------------------|---------|
| DecisionSupportLogic | ✅ `source 1..1 uri` | Points to DMN files |
| BusinessProcessWorkflow | ✅ `source 1..1 uri` | Points to BPMN files |
| TestScenario | ✅ `feature 1..1 uri` | Points to feature files |
| HealthInterventions | ❌ None | - |
| GenericPersona | ❌ None | - |
| UserScenario | ❌ None | - |
| CoreDataElement | ❌ None | - |
| ProgramIndicator | ❌ None | - |
| Requirements | ❌ None | - |

## Option 1: Choice Type with BackboneElement and URL

### Description
Use FHIR choice types (`[x]`) to allow each component field to be either the full component type OR a URL reference.

### Implementation
```fsh
// In DAK.fsh, change from:
* indicators 0..* ProgramIndicator "Program Indicators" "..."

// To:
* indicators[x] 0..* ProgramIndicator or url "Program Indicators" "..."
```

### Pros
- Simple syntax, follows existing pattern used in `description[x]`
- Clear semantics: either inline data OR a URL
- Native FHIR choice type support
- JSON serialization would be `indicatorsUrl` or `indicatorsProgramIndicator`

### Cons
- Choice type names in JSON can be verbose (e.g., `indicatorsProgramIndicator`)
- May not work perfectly with complex types in all FHIR tools
- Less intuitive JSON structure

### Example JSON Instance
```json
{
  "resourceType": "DAK",
  "id": "example",
  "indicators": [
    {
      "id": "IND001",
      "name": "Vaccination coverage",
      "definition": "Percentage vaccinated"
    }
  ],
  "indicatorsUrl": [
    "http://example.org/indicators/IND002.json"
  ]
}
```

## Option 2: Choice Type with Reference

### Description
Use FHIR `Reference()` type to point to logical model instances, similar to how `Requirements.fsh` references `FunctionalRequirement`.

### Implementation
```fsh
// In DAK.fsh, change from:
* indicators 0..* ProgramIndicator "Program Indicators" "..."

// To:
* indicators[x] 0..* ProgramIndicator or Reference(ProgramIndicator) "Program Indicators" "..."
```

### Pros
- Uses FHIR's standard Reference mechanism
- Already used successfully in Requirements.fsh
- Supports both relative and absolute references
- Can include display text with reference

### Cons
- Requires instances of components to exist as separate resources
- More complex JSON structure with nested reference object
- May require additional tooling to resolve references

### Example JSON Instance
```json
{
  "resourceType": "DAK",
  "id": "example",
  "indicatorsProgramIndicator": [
    {
      "id": "IND001",
      "name": "Vaccination coverage",
      "definition": "Percentage vaccinated"
    }
  ],
  "indicatorsReference": [
    {
      "reference": "ProgramIndicator/IND002",
      "display": "External indicator"
    }
  ]
}
```

## Option 3: Backbone Element with Content Choice

### Description
Create a wrapper BackboneElement that contains either the inline content OR a URL reference.

### Implementation
```fsh
// In DAK.fsh:
* indicators 0..* BackboneElement "Program Indicators" "..."
  * content[x] 1..1 ProgramIndicator or url "Content" "Either inline indicator or URL to indicator"
```

### Pros
- Very explicit structure
- Single array in JSON with uniform structure
- Clear that each entry is either inline or reference
- Easier to process programmatically

### Cons
- Adds an extra nesting level
- Not a standard FHIR pattern
- More verbose

### Example JSON Instance
```json
{
  "resourceType": "DAK",
  "id": "example",
  "indicators": [
    {
      "contentProgramIndicator": {
        "id": "IND001",
        "name": "Vaccination coverage",
        "definition": "Percentage vaccinated"
      }
    },
    {
      "contentUrl": "http://example.org/indicators/IND002.json"
    }
  ]
}
```

## Option 4: Separate Arrays for Inline and Referenced

### Description
Create two separate arrays: one for inline components and one for references.

### Implementation
```fsh
// In DAK.fsh:
* indicators 0..* ProgramIndicator "Program Indicators (Inline)" "Inline program indicators"
* indicatorsReference 0..* url "Program Indicators (Reference)" "References to external program indicators"
```

### Pros
- Very simple and clear
- No choice types needed
- Easy to process: check both arrays
- Explicit distinction between inline and referenced

### Cons
- Doubles the number of fields in DAK LM
- Not DRY (Don't Repeat Yourself)
- Could lead to confusion about which array to use

### Example JSON Instance
```json
{
  "resourceType": "DAK",
  "id": "example",
  "indicators": [
    {
      "id": "IND001",
      "name": "Vaccination coverage",
      "definition": "Percentage vaccinated"
    }
  ],
  "indicatorsReference": [
    "http://example.org/indicators/IND002.json"
  ]
}
```

## Option 5: URI Field in Each Component

### Description
Add an optional URI field to each component logical model that, when present, indicates the content should be fetched from that URI instead of using inline data.

### Implementation
```fsh
// In ProgramIndicator.fsh and all other component models:
* reference 0..1 url "Reference URL" "If present, the component instance should be fetched from this URL instead of using inline fields"

// DAK.fsh remains unchanged:
* indicators 0..* ProgramIndicator "Program Indicators" "..."
```

### Pros
- No changes to DAK.fsh needed
- Each component can be inline or referenced
- Uniform pattern across all components
- Validates well
- **Consistent with existing `source` pattern** used in DecisionSupportLogic and BusinessProcessWorkflow

### Cons
- Requires changing all 9 component logical models
- Potentially confusing: what if both reference URL and inline data are present?
- Need validation rules to ensure consistency
- Name conflict: `reference` might conflict with FHIR's Reference type

### Example JSON Instance
```json
{
  "resourceType": "DAK",
  "id": "example",
  "indicators": [
    {
      "id": "IND001",
      "name": "Vaccination coverage",
      "definition": "Percentage vaccinated"
    },
    {
      "id": "IND002",
      "reference": "http://example.org/indicators/IND002.json"
    }
  ]
}
```

## Option 6: Extension of Existing Source Pattern

### Description
Extend the existing `source` field pattern (currently used for DMN/BPMN files) to all component models, but clarify that it can reference either source files OR component instances.

### Implementation
```fsh
// In ProgramIndicator.fsh and all other component models:
* source 0..1 url "Source" "Link to an external resource containing this component's content. Could be a JSON file containing the component instance, or for certain component types, a process definition file (DMN/BPMN)"

// DAK.fsh remains unchanged:
* indicators 0..* ProgramIndicator "Program Indicators" "..."
```

### Pros
- Leverages existing pattern from DecisionSupportLogic and BusinessProcessWorkflow
- Single field name across all components
- Natural extension of current architecture
- No changes to DAK.fsh needed

### Cons
- Overloading `source` with multiple meanings (could mean DMN/BPMN OR component instance)
- DecisionSupportLogic.source is currently mandatory (1..1), would need to stay that way or become optional
- BusinessProcessWorkflow.source is also mandatory (1..1), same issue
- Potential semantic confusion

### Example JSON Instance
```json
{
  "resourceType": "DAK",
  "id": "example",
  "indicators": [
    {
      "id": "IND001",
      "name": "Vaccination coverage",
      "definition": "Percentage vaccinated"
    },
    {
      "id": "IND002",
      "source": "http://example.org/indicators/IND002.json"
    }
  ],
  "decisionLogic": [
    {
      "id": "DL001",
      "source": "http://example.org/dmn/decision1.dmn"
    },
    {
      "id": "DL002", 
      "source": "http://example.org/logic/DL002.json"
    }
  ]
}
```

## Recommendation Matrix

| Criterion | Option 1 | Option 2 | Option 3 | Option 4 | Option 5 | Option 6 |
|-----------|----------|----------|----------|----------|----------|----------|
| Simplicity | ⭐⭐⭐ | ⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| FHIR Standards Alignment | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| JSON Clarity | ⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Ease of Processing | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Minimal Changes | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Validation Support | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Consistency with Existing | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **TOTAL** | **21** | **22** | **18** | **24** | **27** | **28** |

## Recommended Approach

### Primary Recommendation: **Option 6 - Extension of Existing Source Pattern**

This approach:
1. ✅ Leverages existing `source` pattern from DecisionSupportLogic and BusinessProcessWorkflow
2. ✅ Provides the clearest JSON structure
3. ✅ Most consistent with current architecture
4. ✅ Requires minimal changes to DAK.fsh (none)
5. ✅ Natural evolution of the current design

**Key Consideration**: For DecisionSupportLogic and BusinessProcessWorkflow, the `source` field is currently mandatory (1..1) and points to DMN/BPMN files. These would need to remain mandatory OR be relaxed to 0..1 if full inline definitions are to be supported.

**Implementation Steps:**
1. Keep DecisionSupportLogic.source and BusinessProcessWorkflow.source as 1..1 (they need external files)
2. Add `source 0..1 url` field to the remaining 7 component logical models
3. Update documentation to clarify that `source` can point to:
   - For DecisionSupportLogic: DMN files OR component instance JSON
   - For BusinessProcessWorkflow: BPMN files OR component instance JSON  
   - For all others: Component instance JSON files
4. Add validation guidance (e.g., if source is present, other fields may be minimal/optional)

### Alternative Recommendation: **Option 5 - URI Field with Different Name**

If semantic clarity is more important than consistency with existing `source` fields:
1. ✅ Very clear that this is a reference to a component instance
2. ✅ No confusion with process definition files
3. ✅ Uses a distinct field name like `reference`, `instanceUrl`, or `contentUrl`
4. ❌ Less consistent with existing pattern

### Secondary Alternative: **Option 4 - Separate Arrays**

If maximum explicitness is desired at the cost of more fields:
1. ✅ Very clear distinction between inline and referenced
2. ✅ Easy to process
3. ✅ No complex choice types or semantic overloading
4. ❌ Requires doubling component fields in DAK.fsh

## Implementation Considerations

### For Option 6 (Recommended) - Extending Source Pattern:

**For components that don't have `source` yet:**
```fsh
// Example change to ProgramIndicator.fsh:
Logical: ProgramIndicator
Title: "Program Indicator (DAK)"
Description: "..."

* ^status = #active
* source 0..1 url "Source" "Reference to an external resource containing this indicator's content. When source is provided, this should be a URL to a JSON file containing a complete ProgramIndicator instance. Other fields may be omitted or provide minimal metadata when source is specified."
* id 1..1 id "Indicator ID" "..."
* name 1..1 string "Name" "..."
// ... rest of fields remain the same
```

**For DecisionSupportLogic (already has source 1..1):**
```fsh
// Update description only:
* source 1..1 uri "Source" "Link to an external resource containing the decision logic. This can be either: (1) A DMN file containing executable decision logic, or (2) A JSON file containing a complete DecisionSupportLogic instance. Source URI could be absolute or relative to the root of the DAK"
```

**For BusinessProcessWorkflow (already has source 1..1):**
```fsh
// Update description only:
* source 1..1 uri "Source" "Link to an external resource containing the workflow. This can be either: (1) A BPMN file containing the workflow definition, or (2) A JSON file containing a complete BusinessProcessWorkflow instance. Source URI could be absolute or relative to the root of the DAK"
```

### For Option 5 - New Reference Field:

```fsh
// Example change to ProgramIndicator.fsh:
Logical: ProgramIndicator
Title: "Program Indicator (DAK)"
Description: "..."

* ^status = #active
* reference 0..1 url "Instance Reference" "URL to an external JSON file containing a complete ProgramIndicator instance. When reference is provided, other fields may be omitted or provide minimal metadata."
* id 1..1 id "Indicator ID" "..."
* description[x] 0..1 string or uri "Description" "..."
// ... rest of fields remain the same
```

### For Option 4 - Separate Arrays:

```fsh
// Example change to DAK.fsh:
// Current:
* indicators 0..* ProgramIndicator "Program Indicators" "..."

// New:
* indicators 0..* ProgramIndicator "Program Indicators" "Core set of indicators (inline definitions)"
* indicatorsRef 0..* url "Program Indicator References" "References to externally defined program indicators (JSON files containing ProgramIndicator instances)"
```

## Validation Rules

Regardless of chosen option, consider adding:

1. **For Option 5**: If `source` is present, require only `id` and make other fields optional
2. **For any option**: Ensure referenced URLs return valid instances of the component type
3. **JSON Schema generation**: Update `generate_logical_model_schemas.py` to handle the chosen pattern
4. **Documentation**: Clear examples of both inline and referenced patterns in IG

## Next Steps

1. Review these options with stakeholders
2. Select preferred approach based on use cases
3. Implement chosen option in FSH files
4. Update JSON schema generation scripts
5. Add examples to documentation
6. Update dak.json template if needed

## Decision Factors to Consider

When selecting an option, consider:

1. **Use Case Priority**: 
   - Will component references be used primarily for modularization (breaking large DAKs into files)?
   - Or for reuse (referencing shared components across multiple DAKs)?

2. **Tooling Impact**:
   - Which option best supports automatic validation and resolution of references?
   - How will the JSON schema generation handle the chosen pattern?

3. **User Experience**:
   - What will be most intuitive for DAK authors?
   - What provides clearest error messages when validation fails?

4. **Migration Path**:
   - How will this affect existing DAK instances?
   - Can we provide automated migration tools?

5. **Consistency**:
   - Should all components use the same pattern (Option 5/6)?
   - Or can we have different patterns for different component types based on their nature?

6. **FHIR Alignment**:
   - How important is strict alignment with FHIR patterns vs. JSON simplicity?
   - Should we prioritize FHIR tooling compatibility or human readability?

## Quick Decision Guide

**Choose Option 6** if:
- You want maximum consistency with existing patterns
- You're comfortable with semantic overloading of `source`/`feature` fields
- Minimal changes are highest priority

**Choose Option 5** if:
- You want clear semantic distinction from `source` fields
- You prefer explicit field naming
- You don't mind adding a new field to 6-9 component models

**Choose Option 4** if:
- You want maximum explicitness in the DAK structure
- Processing simplicity is more important than file size
- You're willing to modify DAK.fsh significantly

**Choose Option 2** if:
- FHIR standards alignment is the top priority
- You need support for contained resources or partial references
- You have tooling for resolving FHIR References

**Choose Option 1** if:
- You want native FHIR choice type support
- You prefer URLs to Reference objects for simplicity
- You're comfortable with verbose JSON field names
