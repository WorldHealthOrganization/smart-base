# Summary: DAK Component Reference Options

## Request
Allow DAK Logical Model component instances to be either:
1. **Inline**: Full component content embedded in dak.json
2. **Referenced**: URL pointing to an external component instance

## Current State
- 9 component types in DAK.fsh (healthInterventions, personas, userScenarios, etc.)
- 3 components already have external file references:
  - `DecisionSupportLogic.source` → DMN files
  - `BusinessProcessWorkflow.source` → BPMN files  
  - `TestScenario.feature` → Feature files
- 6 components have no external reference mechanism

## Six Options Analyzed

### ⭐ Option 6: Extend Existing Source Pattern (RECOMMENDED - Score: 28/35)
Add/extend `source` field in component models
- **Changes**: 6 component models need new `source` field, 3 need updated descriptions
- **JSON**: `{"indicators": [{"id": "X", "name": "Y"}, {"id": "Z", "source": "url"}]}`
- **Why**: Maximum consistency, minimal DAK.fsh changes, natural evolution

### ⭐ Option 5: New Reference Field (ALTERNATIVE - Score: 27/35)  
Add distinct `reference` field to avoid semantic overload
- **Changes**: 9 component models need new field
- **JSON**: Same as Option 6 but field named `reference` instead of `source`
- **Why**: Clearer semantics, no confusion with process files

### Option 4: Separate Arrays (Score: 24/35)
Two arrays in DAK.fsh: one inline, one references
- **Changes**: DAK.fsh gets 9 new fields (`indicatorsRef`, `personasRef`, etc.)
- **JSON**: `{"indicators": [...], "indicatorsRef": ["url1", "url2"]}`
- **Why**: Maximum explicitness, easy processing

### Option 2: Reference Type (Score: 22/35)
Use FHIR `Reference()` type
- **Changes**: DAK.fsh components become choice types
- **JSON**: `{"indicatorsReference": [{"reference": "ProgramIndicator/X"}]}`
- **Why**: FHIR standard alignment, supports contained resources

### Option 1: Choice Type with URL (Score: 21/35)
Make component fields choice types
- **Changes**: DAK.fsh components become `component[x]` choice types
- **JSON**: `{"indicatorsProgramIndicator": [...], "indicatorsUrl": [...]}`
- **Why**: Native FHIR choice types

### Option 3: Backbone Wrapper (Score: 18/35)
Wrap components in BackboneElement with content choice
- **Changes**: Significant DAK.fsh restructuring
- **JSON**: `{"indicators": [{"contentProgramIndicator": {...}}, {"contentUrl": "..."}]}`
- **Why**: Explicit structure, uniform array

## Implementation Examples

### Option 6 (Recommended):
```fsh
// ProgramIndicator.fsh - ADD
* source 0..1 url "Source" "URL to JSON file with complete instance"

// DecisionSupportLogic.fsh - UPDATE description only
* source 1..1 uri "Source" "DMN file OR JSON instance"
```

### Option 5 (Alternative):
```fsh
// ProgramIndicator.fsh - ADD
* reference 0..1 url "Instance Reference" "URL to JSON instance"
```

### Option 4 (Alternative):
```fsh
// DAK.fsh - ADD for each component
* indicators 0..* ProgramIndicator "Inline indicators"
* indicatorsRef 0..* url "Referenced indicators"
```

## Decision Matrix

| Criterion | Opt 1 | Opt 2 | Opt 3 | Opt 4 | Opt 5 | Opt 6 |
|-----------|-------|-------|-------|-------|-------|-------|
| Simplicity | ⭐⭐⭐ | ⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| FHIR Alignment | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| JSON Clarity | ⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Processing | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Minimal Changes | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Validation | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| Consistency | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **TOTAL** | **21** | **22** | **18** | **24** | **27** | **28** |

## Quick Selection Guide

**Choose Option 6** if:
✅ Consistency with existing architecture is important  
✅ You want minimal changes to DAK.fsh  
✅ Semantic overloading of `source` is acceptable

**Choose Option 5** if:
✅ Clear semantic distinction is more important than consistency  
✅ You want explicit field naming (`reference` vs `source`)  
✅ Minor duplication across models is acceptable

**Choose Option 4** if:
✅ Explicit separation of inline vs referenced is critical  
✅ Processing simplicity trumps file size  
✅ You're willing to double DAK.fsh component fields

## Files Affected

### Option 6 (Recommended):
- ✏️ Modify: 6 component models (add `source` field)
- ✏️ Modify: 3 component models (update `source` description)
- ✅ No change: DAK.fsh
- ✏️ Update: JSON schema generation script
- 📝 Update: Documentation

### Option 5 (Alternative):
- ✏️ Modify: 9 component models (add `reference` field)
- ✅ No change: DAK.fsh
- ✏️ Update: JSON schema generation script
- 📝 Update: Documentation

### Option 4 (Alternative):
- ✅ No change: 9 component models
- ✏️ Modify: DAK.fsh (add 9 new reference fields)
- ✏️ Update: JSON schema generation script
- 📝 Update: Documentation

## Next Steps

1. 🤔 Review options and select preferred approach
2. 🛠️ Implement chosen option in FSH files
3. 🔧 Update `generate_logical_model_schemas.py`
4. 📚 Add examples to documentation
5. ✅ Validate with test instances
6. 🔄 Update dak.json if needed

## Full Analysis
See `DAK_COMPONENT_REFERENCE_OPTIONS.md` for:
- Detailed pros/cons for each option
- Complete implementation examples
- JSON schema considerations
- Migration strategies
- Validation rules
