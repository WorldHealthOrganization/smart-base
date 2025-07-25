# Requirements Documentation

## 2.3 DAK Component Management

REQ-DAK-001: The system SHALL display all 8 WHO SMART Guidelines DAK components on the home page

Visual dashboard with distinctive cards/tiles for each component
WHO SMART Guidelines branding and color codes
WHO-provided icons for each component
Clear visual distinction between Level 2 (Business Logic & Processes) and Level 3 (Technical Implementation) content

All 8 components have canonical/authoritative representations as knowledge artifacts. For L2 artifacts there will be one set of artifacts. For L3 there will usually be a different set, depending on the component.

The difference between L2 and L3 versions of the components is that L2 is agnostic to the data model, while L3 involves an explicit choice to use the FHIR R4 data model and follows the enterprise architecture defined at http://smart.who.int/ra.

There is a FHIR CodeSystem with id DAK at `input/fsh/codesystems/DAK.fsh` that contains concepts defined across all 8 components. Each component has specific rules for what constitutes a concept and its canonical representation:

### Component-Specific Canonical Representations

**L2 Business Processes:**
- Captured canonically as .bpmn diagrams (as per [OMG BPMN 2.0 specification](https://www.omg.org/spec/BPMN/2.0/)) from `input/business-processes`

**L2 Persona/Actor Definitions:**
- Each persona/actor definition is captured as a concept in the DAK codesystem
- FHIR value set named `actors` from `input/fsh/valuesets/DAK.actors.fsh` where the id is the code in the code system for the actor, which is also being used as the instance id

**L2 Decision Tables:**
- Canonically captured as DMN tables (as per [OMG DMN 1.3 specification](https://www.omg.org/spec/DMN/1.3/))
- As L3 assets, they are represented as FHIR PlanDefinition resources

### The 8 Core DAK Components

| Component | Level | Canonical Representation |
|-----------|-------|---------------------------|
| **Business Processes** | L2 | BPMN diagrams (.bpmn files) in `input/business-processes/` |
| **Business Processes** | L3 | FHIR ActivityDefinition and PlanDefinition resources |
| **Decision Support Logic** | L2 | DMN tables (Decision Model and Notation) |
| **Decision Support Logic** | L3 | FHIR PlanDefinition resources |
| **Indicators & Measures** | L2 | Logical model specifications |
| **Indicators & Measures** | L3 | FHIR Measure resources |
| **Data Entry Forms** | L2 | Form logical models |
| **Data Entry Forms** | L3 | FHIR Questionnaire resources |
| **Terminology** | L2 | Concept definitions and relationships |
| **Terminology** | L3 | FHIR CodeSystem and ValueSet resources |
| **FHIR Profiles** | L2 | Data model specifications |
| **FHIR Profiles** | L3 | FHIR StructureDefinition resources |
| **FHIR Extensions** | L2 | Extension specifications |
| **FHIR Extensions** | L3 | FHIR StructureDefinition resources (type = extension) |
| **Test Data & Examples** | L2 | Example scenarios and test cases |
| **Test Data & Examples** | L3 | FHIR Example instances and test bundles |

**Note:** Scheduling tables are considered a special case of decision tables within Decision Support Logic.