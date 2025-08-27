Logical: DAK
Title: "Digital Adaptation Kit (DAK)"
Description: "Logical Model for representing a complete Digital Adaptation Kit (DAK) with metadata and all 9 DAK components"

* ^status = #active

// Metadata element with cardinality 1..1
* metadata 1..1 BackboneElement "Metadata" "Metadata for the DAK"
  * id 1..1 SGid "DAK ID" "Identifier for the DAK"
  * canonical 1..1 canonical "Canonical URL" "Canonical URL for the DAK"
  * name 1..1 string "Name" "Name of the DAK"

// 9 DAK Components with cardinality 0..*
* healthInterventions 0..* Reference(DublinCore) "Health Interventions and Recommendations" "Overview of the health interventions and WHO, regional or national recommendations included within the DAK"
* personas 0..* Reference(Persona) "Generic Personas" "Depiction of the human and system actors"
* userScenarios 0..* Reference(UserScenario) "User Scenarios" "Narratives that describe how the different personas may interact with each other"
* businessProcesses 0..* Reference(BusinessProcessWorkflow) "Generic Business Processes and Workflows" "Business processes and workflows for achieving health programme objectives"
* dataElements 0..* Reference(CoreDataElement) "Core Data Elements" "Data elements required throughout the different points of a workflow"
* decisionLogic 0..* Reference(DecisionSupportLogic) "Decision-Support Logic" "Decision-support logic and algorithms to support appropriate service delivery"
* indicators 0..* Reference(ProgramIndicator) "Program Indicators" "Core set of indicators for decision-making, performance metrics and reporting"
* requirements 0..* Reference(Requirements) "Functional and Non-Functional Requirements" "High-level list of core functions and capabilities that the system must have"
* testScenarios 0..* Reference(TestScenario) "Test Scenarios" "Set of test scenarios to validate an implementation of the DAK"