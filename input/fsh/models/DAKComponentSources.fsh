// Complex types for DAK Component sources
// Each component can be referenced via URL, canonical, or provided as inline instance data

Logical: HealthInterventionsSource
Title: "Health Interventions Source"
Description: """
Source reference for Health Interventions - exactly one of the following must be provided:
- url (url data type): URL to retrieve HealthInterventions definition from input/ or external source
- canonical (canonical data type): Canonical URI pointing to the HealthInterventions definition
- instance: Inline HealthInterventions instance data
"""
* ^status = #active
* ^publisher = "World Health Organization (WHO)"
* url 0..1 url "URL" "URL to retrieve HealthInterventions definition from input/ or external source"
* canonical 0..1 canonical "Canonical" "Canonical URI pointing to the HealthInterventions definition"
* canonical ^type[0].targetProfile = "http://smart.who.int/base/StructureDefinition/HealthInterventions"
* instance 0..1 HealthInterventions "Instance" "Inline HealthInterventions instance data"

Logical: GenericPersonaSource
Title: "Generic Persona Source"
Description: """
Source reference for Generic Persona - exactly one of the following must be provided:
- url (url data type): URL to retrieve GenericPersona definition from input/ or external source
- canonical (canonical data type): Canonical URI pointing to the GenericPersona definition
- instance: Inline GenericPersona instance data
"""
* ^status = #active
* ^publisher = "World Health Organization (WHO)"
* url 0..1 url "URL" "URL to retrieve GenericPersona definition from input/ or external source"
* canonical 0..1 canonical "Canonical" "Canonical URI pointing to the GenericPersona definition"
* canonical ^type[0].targetProfile = "http://smart.who.int/base/StructureDefinition/GenericPersona"
* instance 0..1 GenericPersona "Instance" "Inline GenericPersona instance data"

Logical: UserScenarioSource
Title: "User Scenario Source"
Description: """
Source reference for User Scenario - exactly one of the following must be provided:
- url (url data type): URL to retrieve UserScenario definition from input/ or external source
- canonical (canonical data type): Canonical URI pointing to the UserScenario definition
- instance: Inline UserScenario instance data
"""
* ^status = #active
* ^publisher = "World Health Organization (WHO)"
* url 0..1 url "URL" "URL to retrieve UserScenario definition from input/ or external source"
* canonical 0..1 canonical "Canonical" "Canonical URI pointing to the UserScenario definition"
* canonical ^type[0].targetProfile = "http://smart.who.int/base/StructureDefinition/UserScenario"
* instance 0..1 UserScenario "Instance" "Inline UserScenario instance data"

Logical: BusinessProcessWorkflowSource
Title: "Business Process Workflow Source"
Description: """
Source reference for Business Process Workflow - exactly one of the following must be provided:
- url (url data type): URL to retrieve BusinessProcessWorkflow definition from input/ or external source
- canonical (canonical data type): Canonical URI pointing to the BusinessProcessWorkflow definition
- instance: Inline BusinessProcessWorkflow instance data
"""
* ^status = #active
* ^publisher = "World Health Organization (WHO)"
* url 0..1 url "URL" "URL to retrieve BusinessProcessWorkflow definition from input/ or external source"
* canonical 0..1 canonical "Canonical" "Canonical URI pointing to the BusinessProcessWorkflow definition"
* canonical ^type[0].targetProfile = "http://smart.who.int/base/StructureDefinition/BusinessProcessWorkflow"
* instance 0..1 BusinessProcessWorkflow "Instance" "Inline BusinessProcessWorkflow instance data"

Logical: CoreDataElementSource
Title: "Core Data Element Source"
Description: """
Source reference for Core Data Element - exactly one of the following must be provided:
- url (url data type): URL to retrieve CoreDataElement definition from input/ or external source
- canonical (canonical data type): Canonical URI pointing to the CoreDataElement definition
- instance: Inline CoreDataElement instance data
"""
* ^status = #active
* ^publisher = "World Health Organization (WHO)"
* url 0..1 url "URL" "URL to retrieve CoreDataElement definition from input/ or external source"
* canonical 0..1 canonical "Canonical" "Canonical URI pointing to the CoreDataElement definition"
* canonical ^type[0].targetProfile = "http://smart.who.int/base/StructureDefinition/CoreDataElement"
* instance 0..1 CoreDataElement "Instance" "Inline CoreDataElement instance data"

Logical: DecisionSupportLogicSource
Title: "Decision Support Logic Source"
Description: """
Source reference for Decision Support Logic - exactly one of the following must be provided:
- url (url data type): URL to retrieve DecisionSupportLogic definition from input/ or external source
- canonical (canonical data type): Canonical URI pointing to the DecisionSupportLogic definition
- instance: Inline DecisionSupportLogic instance data
"""
* ^status = #active
* ^publisher = "World Health Organization (WHO)"
* url 0..1 url "URL" "URL to retrieve DecisionSupportLogic definition from input/ or external source"
* canonical 0..1 canonical "Canonical" "Canonical URI pointing to the DecisionSupportLogic definition"
* canonical ^type[0].targetProfile = "http://smart.who.int/base/StructureDefinition/DecisionSupportLogic"
* instance 0..1 DecisionSupportLogic "Instance" "Inline DecisionSupportLogic instance data"

Logical: ProgramIndicatorSource
Title: "Program Indicator Source"
Description: """
Source reference for Program Indicator - exactly one of the following must be provided:
- url (url data type): URL to retrieve ProgramIndicator definition from input/ or external source
- canonical (canonical data type): Canonical URI pointing to the ProgramIndicator definition
- instance: Inline ProgramIndicator instance data
"""
* ^status = #active
* ^publisher = "World Health Organization (WHO)"
* url 0..1 url "URL" "URL to retrieve ProgramIndicator definition from input/ or external source"
* canonical 0..1 canonical "Canonical" "Canonical URI pointing to the ProgramIndicator definition"
* canonical ^type[0].targetProfile = "http://smart.who.int/base/StructureDefinition/ProgramIndicator"
* instance 0..1 ProgramIndicator "Instance" "Inline ProgramIndicator instance data"

Logical: RequirementsSource
Title: "Requirements Source"
Description: """
Source reference for Requirements - exactly one of the following must be provided:
- url (url data type): URL to retrieve Requirements definition from input/ or external source
- canonical (canonical data type): Canonical URI pointing to the Requirements definition
- instance: Inline Requirements instance data
"""
* ^status = #active
* ^publisher = "World Health Organization (WHO)"
* url 0..1 url "URL" "URL to retrieve Requirements definition from input/ or external source"
* canonical 0..1 canonical "Canonical" "Canonical URI pointing to the Requirements definition"
* canonical ^type[0].targetProfile = "http://smart.who.int/base/StructureDefinition/Requirements"
* instance 0..1 Requirements "Instance" "Inline Requirements instance data"

Logical: TestScenarioSource
Title: "Test Scenario Source"
Description: """
Source reference for Test Scenario - exactly one of the following must be provided:
- url (url data type): URL to retrieve TestScenario definition from input/ or external source
- canonical (canonical data type): Canonical URI pointing to the TestScenario definition
- instance: Inline TestScenario instance data
"""
* ^status = #active
* ^publisher = "World Health Organization (WHO)"
* url 0..1 url "URL" "URL to retrieve TestScenario definition from input/ or external source"
* canonical 0..1 canonical "Canonical" "Canonical URI pointing to the TestScenario definition"
* canonical ^type[0].targetProfile = "http://smart.who.int/base/StructureDefinition/TestScenario"
* instance 0..1 TestScenario "Instance" "Inline TestScenario instance data"
