# DAK Component Reference Implementation Options

This directory contains comprehensive documentation for implementing component references in the DAK (Digital Adaptation Kit) Logical Model.

## 📋 Issue Summary

**Goal**: Allow DAK component instances to be either embedded inline OR referenced via URL.

**Current State**: All 9 DAK components (healthInterventions, personas, indicators, etc.) must be embedded inline in dak.json.

**Desired State**: Each component can be either:
- Inline: Full component content in dak.json
- Referenced: URL pointing to external JSON file with component instance

## 📚 Documents in This Analysis

### 1. **Start Here**: [SUMMARY_DAK_COMPONENT_REFERENCES.md](SUMMARY_DAK_COMPONENT_REFERENCES.md)
**Quick overview document (5 pages)**

Contains:
- Executive summary of the 6 options
- Decision matrix with scoring
- Quick selection guide
- Files affected by each option
- Next steps

**Read this first** for a high-level understanding.

---

### 2. **Deep Dive**: [DAK_COMPONENT_REFERENCE_OPTIONS.md](DAK_COMPONENT_REFERENCE_OPTIONS.md)
**Comprehensive analysis document (17 pages)**

Contains:
- Detailed description of each option with FSH implementation examples
- Complete pros/cons analysis
- Current state analysis (which components already have external references)
- Implementation considerations for each approach
- Validation rules
- Decision factors to consider

**Read this** when you need complete details on any option.

---

### 3. **Visual Examples**: [JSON_EXAMPLES_COMPONENT_REFERENCES.md](JSON_EXAMPLES_COMPONENT_REFERENCES.md)
**Practical examples document (8 pages)**

Contains:
- Side-by-side JSON examples for top 3 options
- Processing code examples (pseudocode)
- Validation scenario walkthroughs
- Migration paths from current state
- Concrete dak.json instances showing how each option works

**Read this** to see what the solutions look like in practice.

---

## 🎯 Quick Recommendations

### Primary: **Option 6 - Extend Source Pattern** ⭐⭐⭐⭐⭐
- Extends existing `source` pattern to all components
- Minimal changes (6 models add field, 3 models update description)
- Most consistent with current architecture
- Score: 28/35

### Alternative: **Option 5 - New Reference Field** ⭐⭐⭐⭐
- Adds new `reference` field to all 9 component models  
- Clearer semantics (no overloading of `source`)
- Slightly more changes but clearer intent
- Score: 27/35

### Secondary: **Option 4 - Separate Arrays** ⭐⭐⭐⭐
- Adds 9 new reference fields to DAK.fsh
- Most explicit (clear separation)
- Easiest to process but more verbose
- Score: 24/35

## 🎭 All Six Options at a Glance

| # | Name | Key Change | JSON Pattern | Score |
|---|------|------------|--------------|-------|
| 6 | Extend Source | Add `source` to models | `[{...}, {"source": "url"}]` | 28 |
| 5 | New Reference | Add `reference` to models | `[{...}, {"reference": "url"}]` | 27 |
| 4 | Separate Arrays | Double DAK fields | `"items": [...], "itemsRef": [...]` | 24 |
| 2 | Reference Type | Use FHIR Reference | `"itemsReference": [{"reference": "..."}]` | 22 |
| 1 | Choice Type | Use choice `[x]` | `"itemsType": [...], "itemsUrl": [...]` | 21 |
| 3 | Backbone Wrapper | Add wrapper layer | `[{"contentType": {...}}, {"contentUrl": "..."}]` | 18 |

## 🔍 Finding Information

**Want to know...**
- ✅ Which option to choose? → See Summary doc or this README
- ✅ How Option X works in detail? → See Comprehensive doc
- ✅ What the JSON looks like? → See Examples doc
- ✅ What files need changing? → See Summary doc "Files Affected" section
- ✅ How to process references? → See Examples doc "Processing Comparison"
- ✅ Migration strategy? → See Examples doc "Migration from Current State"
- ✅ Current state of components? → See Comprehensive doc "Component External Reference Status"

## 🛠️ Implementation Path (Once Option Selected)

### For Option 6 (Recommended):
1. ✏️ Add `source 0..1 url` to 6 component models (HealthInterventions, GenericPersona, UserScenario, CoreDataElement, ProgramIndicator, Requirements)
2. ✏️ Update description of `source` in 3 models (DecisionSupportLogic, BusinessProcessWorkflow, TestScenario)
3. 🔧 Update `input/scripts/generate_logical_model_schemas.py` to handle source field
4. 📝 Add documentation and examples
5. ✅ Test with example instances

### For Option 5:
1. ✏️ Add `reference 0..1 url` to all 9 component models
2. 🔧 Update `input/scripts/generate_logical_model_schemas.py` to handle reference field
3. 📝 Add documentation and examples
4. ✅ Test with example instances

### For Option 4:
1. ✏️ Add 9 new `*Ref` fields to DAK.fsh
2. 🔧 Update `input/scripts/generate_logical_model_schemas.py` to handle dual arrays
3. 📝 Add documentation and examples
4. ✅ Test with example instances

## 📊 Implementation Effort Comparison

| Aspect | Option 6 | Option 5 | Option 4 |
|--------|----------|----------|----------|
| Component models to modify | 9 (6 add, 3 update) | 9 (all add) | 0 |
| DAK.fsh changes | None | None | Add 9 fields |
| Schema script changes | Minor | Minor | Minor |
| Documentation needs | Medium | Medium | Medium |
| **Total Effort** | **Medium** | **Medium** | **Medium** |
| **Complexity** | **Low** | **Low** | **Low** |

All three top options have similar implementation effort!

## 🔗 Related Files in Repository

- **Current DAK LM**: `input/fsh/models/DAK.fsh`
- **Component Models**: `input/fsh/models/*.fsh`
- **Schema Generator**: `input/scripts/generate_logical_model_schemas.py`
- **Example Instance**: `dak.json`

## ❓ Questions?

For questions or clarifications:
1. Review the three analysis documents
2. Check the specific option's detailed section in the comprehensive doc
3. Look at JSON examples for practical understanding
4. Refer back to the original issue for context

## 📝 Note

**This is an options analysis, not an implementation.** The issue specifically requested options be provided without implementation. Select your preferred option before proceeding with implementation.
