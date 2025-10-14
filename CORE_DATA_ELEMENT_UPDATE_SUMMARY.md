# CoreDataElement and DAK Logical Models Update Summary

## Overview
This document summarizes the changes made to update the CoreDataElement logical model and all DAK logical models to comply with the SGLogicalModel profile and improve markdown usage for longer text fields.

## Issue Requirements
The issue requested three main changes:
1. **CoreDataElement Restructure**: Completely restart from scratch, removing all data fields. Support one of:
   - ValueSet (source as URL/canonical)
   - CodeSystem (source as URL/canonical)
   - ConceptMap (source as URL/canonical)
   - Logical Model adherent to SGLogicalModel
   
2. **SGLogicalModel Compliance**: All DAK logical models should adhere to SGLogicalModel

3. **String to Markdown**: Review use of string in DAK LMs and change to markdown where appropriate (longer text like definitions, descriptions)

## Changes Implemented

### 1. CoreDataElement Complete Rewrite

**Before:**
```fsh
Logical: CoreDataElement
Title: "Core Data Element (DAK)"
Description: "..."

* ^status = #active
* code 1..1 code "Code" "Code that identifies the concept"
* display 1..1 string "Display" "Text displayed to the user"
* definition 1..1 string "Definition" "Formal definition of the data element"
* description[x] 0..1 string or uri "Description" "..."
```

**After:**
```fsh
Logical: CoreDataElement
Parent: SGLogicalModel
Title: "Core Data Element (DAK)"
Description: "... A core data element can be one of: a ValueSet, a CodeSystem, a ConceptMap, or a Logical Model adherent to SGLogicalModel. This is the ONE EXCEPTION to allowing FHIR R4 models into the DAK LMs."

* ^status = #active
* ^publisher = "World Health Organization (WHO)"

// Type of core data element (exactly one must be specified)
* type 1..1 code "Type" "Type of core data element: valueset, codesystem, conceptmap, or logicalmodel"
* type from CoreDataElementTypeVS (required)

// Source reference (URL, canonical, or relative path)
* source 1..1 uri "Source" "URL (absolute or relative) or canonical/IRI pointing to the ValueSet, CodeSystem, ConceptMap, or Logical Model definition"

// Optional metadata
* id 0..1 id "Element ID" "Identifier for the core data element"
* description 0..1 markdown "Description" "Description of the core data element"
```

**Supporting Resources Created:**
- `input/fsh/codesystems/CoreDataElementType.fsh` - Defines codes: valueset, codesystem, conceptmap, logicalmodel
- `input/fsh/valuesets/CoreDataElementTypeVS.fsh` - ValueSet including all codes from CoreDataElementType

### 2. SGLogicalModel Compliance

All 23 logical models now include:
```fsh
Parent: SGLogicalModel
* ^publisher = "World Health Organization (WHO)"
```

**Models Updated:**
- Core DAK Components (14): DAK, CoreDataElement, GenericPersona, HealthInterventions, BusinessProcessWorkflow, DecisionSupportLogic, ProgramIndicator, Requirements, UserScenario, TestScenario, FunctionalRequirement, NonFunctionalRequirement, DublinCore, Persona
- Source Wrappers (9): HealthInterventionsSource, GenericPersonaSource, UserScenarioSource, BusinessProcessWorkflowSource, CoreDataElementSource, DecisionSupportLogicSource, ProgramIndicatorSource, RequirementsSource, TestScenarioSource

### 3. String to Markdown Conversions

**Pattern Applied:**
- **Longer descriptive text** → `markdown` data type
- **Short identifiers/names** → remain `string`

**Specific Changes:**

| Model | Field | Before | After |
|-------|-------|--------|-------|
| DAK | description | `string or uri` | `markdown` |
| GenericPersona | description | `string or uri` | `markdown` |
| HealthInterventions | description | `string or uri` | `markdown` |
| ProgramIndicator | description | `string or uri` | `markdown` |
| ProgramIndicator | definition | `string` | `markdown` |
| ProgramIndicator | numerator | `string` | `markdown` |
| ProgramIndicator | denominator | `string` | `markdown` |
| ProgramIndicator | disaggregation | `string` | `markdown` |
| Requirements | description | `string or uri` | `markdown` |
| UserScenario | description | `string or uri` | `markdown` |
| BusinessProcessWorkflow | description | `string or uri` | `markdown` |
| BusinessProcessWorkflow | task.description | `string` | `markdown` |
| DecisionSupportLogic | description | `string or uri` | `markdown` |
| TestScenario | description | `string or uri` | `markdown` |
| FunctionalRequirement | activity | `string` | `markdown` |
| FunctionalRequirement | capability[x] | `string or Coding` | `markdown or Coding` |
| FunctionalRequirement | benefit[x] | `string or Coding` | `markdown or Coding` |
| NonFunctionalRequirement | requirement | `string` | `markdown` |
| Persona | description | `string` | `markdown` |
| DublinCore | description | `string` | `markdown` |
| CoreDataElement | description | - | `markdown` (new field) |

**Fields Kept as String:**
- id, name, title (short identifiers)
- otherNames (list of short names)
- iscoCode (codes)
- All URL/URI/canonical fields

## Validation

### SUSHI Compilation
✅ Successfully preprocessed 59 documents with 27 aliases
✅ Successfully imported 62 definitions and 3 instances
✅ No FSH syntax errors

The SUSHI build encountered expected network failures when downloading FHIR package dependencies (hl7.terminology, hl7.fhir.uv.extensions.r4, etc.), but this is due to the sandboxed environment and does not indicate any issues with the FSH syntax or structure.

## Impact Assessment

### Breaking Changes
⚠️ **CoreDataElement**: Complete restructure - existing instances will need migration
- Old structure used: `code`, `display`, `definition`, `description[x]`
- New structure uses: `type`, `source`, `id`, `description`

⚠️ **Markdown Fields**: Changed from `string or uri` to `markdown`
- Systems expecting URI references in description fields will need adjustment
- Markdown provides richer formatting for longer text content

### Backward Compatibility
- All other model structures remain compatible
- Addition of `Parent: SGLogicalModel` is additive (no breaking changes)
- Addition of publisher metadata is additive (no breaking changes)

## Benefits

1. **CoreDataElement Clarity**: New structure explicitly defines what a core data element represents (a reference to a FHIR resource type)

2. **SGLogicalModel Compliance**: All models now properly inherit from the profile, ensuring consistency and validation

3. **Better Content Formatting**: Markdown support for longer text fields enables:
   - Rich text formatting (bold, italic, lists)
   - Links and references
   - Code blocks for technical content
   - Better rendering in documentation

4. **Consistency**: All DAK models follow the same patterns and standards

## Migration Guide

### For CoreDataElement Instances

**Old Format Example:**
```json
{
  "resourceType": "CoreDataElement",
  "code": "IMMZ.D1.DE1",
  "display": "BCG vaccine",
  "definition": "Bacillus Calmette-Guérin vaccine",
  "description": "Vaccine for tuberculosis prevention"
}
```

**New Format Example (ValueSet Reference):**
```json
{
  "resourceType": "CoreDataElement",
  "type": "valueset",
  "source": "http://smart.who.int/base/ValueSet/BCGVaccineValueSet",
  "id": "IMMZ.D1.DE1",
  "description": "Bacillus Calmette-Guérin vaccine for tuberculosis prevention"
}
```

**New Format Example (Logical Model Reference):**
```json
{
  "resourceType": "CoreDataElement",
  "type": "logicalmodel",
  "source": "http://smart.who.int/base/StructureDefinition/ImmunizationRecommendation",
  "id": "IMMZ.C.DE1",
  "description": "Immunization recommendation data elements"
}
```

### For Markdown Fields

**Old Format:**
```json
{
  "description": "This is a simple description"
}
```

**New Format (same text, but markdown capable):**
```json
{
  "description": "This is a **simple** description with *markdown* support"
}
```

## Files Modified

1. `input/fsh/models/CoreDataElement.fsh` - Complete rewrite
2. `input/fsh/models/DAK.fsh` - Parent + publisher + markdown
3. `input/fsh/models/GenericPersona.fsh` - Parent + publisher + markdown
4. `input/fsh/models/HealthInterventions.fsh` - Parent + publisher + markdown
5. `input/fsh/models/ProgramIndicator.fsh` - Parent + publisher + markdown
6. `input/fsh/models/Requirements.fsh` - Parent + publisher + markdown
7. `input/fsh/models/UserScenario.fsh` - Parent + publisher + markdown
8. `input/fsh/models/BusinessProcessWorkflow.fsh` - Parent + publisher + markdown
9. `input/fsh/models/DecisionSupportLogic.fsh` - Parent + publisher + markdown
10. `input/fsh/models/TestScenario.fsh` - Parent + publisher + markdown
11. `input/fsh/models/FunctionalRequirement.fsh` - Parent + publisher + markdown
12. `input/fsh/models/NonFunctionalRequirement.fsh` - Parent + publisher + markdown
13. `input/fsh/models/Persona.fsh` - Parent + publisher + markdown
14. `input/fsh/models/DublinCore.fsh` - Parent + publisher + markdown
15. `input/fsh/models/DAKComponentSources.fsh` - Parent + publisher for all 9 source models

## Files Created

1. `input/fsh/codesystems/CoreDataElementType.fsh` - New CodeSystem
2. `input/fsh/valuesets/CoreDataElementTypeVS.fsh` - New ValueSet

## Next Steps

1. ✅ Changes validated with SUSHI (syntax correct)
2. ⏭️ Full IG build will require network access to download FHIR packages
3. ⏭️ Update any existing CoreDataElement instances to use new structure
4. ⏭️ Update documentation to reflect new CoreDataElement structure
5. ⏭️ Consider updating extraction scripts if they generate CoreDataElement instances

## Questions & Answers

**Q: Why was CoreDataElement completely restructured?**
A: The issue specifically requested starting from scratch to make CoreDataElement a reference to one of four FHIR resource types (ValueSet, CodeSystem, ConceptMap, or Logical Model), rather than containing inline data fields.

**Q: Why change from `string or uri` to `markdown`?**
A: The issue requested changing longer text fields to markdown for better formatting support. Markdown is a superset of plain text, so existing plain text content will still work, but now supports rich formatting.

**Q: Are the Source models (HealthInterventionsSource, etc.) DAK components?**
A: No, they are wrapper types that allow DAK components to be referenced via URL, canonical, or inline instances. However, they now also inherit from SGLogicalModel for consistency.

**Q: What about SushiConfigLogicalModel?**
A: It was intentionally not changed because it represents the sushi-config.yaml file structure (a configuration file), not a DAK component. The YAML format expects string fields, not markdown.
