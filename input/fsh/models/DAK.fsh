Logical: DAK
Title: "Digital Adaptation Kit (DAK)"
Description: "Logical Model for representing a complete Digital Adaptation Kit (DAK) with metadata and all 9 DAK components"

* ^status = #active

// Core DAK metadata fields (aligned with dak.json structure)
* id 1..1 string "DAK ID" "Identifier for the DAK (e.g., smart.who.int.base)"
* name 1..1 string "DAK Name" "Short name for the DAK (e.g., Base)"
* title 1..1 string "DAK Title" "Full title of the DAK (e.g., SMART Base)"
* description[x] 1..1 string or uri "DAK Description" "Description of the DAK - either Markdown content or a URI to a Markdown file (absolute or relative to repository root)"
* version 1..1 string "DAK Version" "Version of the DAK"
* status 1..1 code "DAK Status" "Publication status of the DAK"
* publicationUrl 1..1 url "Publication URL" "Canonical URL for the DAK (e.g., http://smart.who.int/base)"
* license 1..1 code "License" "License under which the DAK is published"
* copyrightYear 1..1 string "Copyright Year" "Year or year range for copyright"

// Publisher information
* publisher 1..1 BackboneElement "Publisher" "Organization responsible for publishing the DAK"
  * name 1..1 string "Publisher Name" "Name of the publishing organization"
  * url 0..1 url "Publisher URL" "URL of the publishing organization"





// 9 DAK Components - each component can be either a URL, canonical reference, or inline instance
// Health Interventions and Recommendations
* healthInterventionsUrl 0..* url "Health Interventions URL" "URL to retrieve HealthInterventions definition from input/ or external source"
* healthInterventionsCanonical 0..* canonical "Health Interventions Canonical" "Canonical URI pointing to the HealthInterventions definition"
* healthInterventionsCanonical ^type[0].targetProfile = "http://smart.who.int/base/StructureDefinition/HealthInterventions"
* healthInterventionsInline 0..* HealthInterventions "Health Interventions Inline" "Inline HealthInterventions instance data"

// Generic Personas
* personasUrl 0..* url "Personas URL" "URL to retrieve GenericPersona definition from input/ or external source"
* personasCanonical 0..* canonical "Personas Canonical" "Canonical URI pointing to the GenericPersona definition"
* personasCanonical ^type[0].targetProfile = "http://smart.who.int/base/StructureDefinition/GenericPersona"
* personasInline 0..* GenericPersona "Personas Inline" "Inline GenericPersona instance data"

// User Scenarios
* userScenariosUrl 0..* url "User Scenarios URL" "URL to retrieve UserScenario definition from input/ or external source"
* userScenariosCanonical 0..* canonical "User Scenarios Canonical" "Canonical URI pointing to the UserScenario definition"
* userScenariosCanonical ^type[0].targetProfile = "http://smart.who.int/base/StructureDefinition/UserScenario"
* userScenariosInline 0..* UserScenario "User Scenarios Inline" "Inline UserScenario instance data"

// Generic Business Processes and Workflows
* businessProcessesUrl 0..* url "Business Processes URL" "URL to retrieve BusinessProcessWorkflow definition from input/ or external source"
* businessProcessesCanonical 0..* canonical "Business Processes Canonical" "Canonical URI pointing to the BusinessProcessWorkflow definition"
* businessProcessesCanonical ^type[0].targetProfile = "http://smart.who.int/base/StructureDefinition/BusinessProcessWorkflow"
* businessProcessesInline 0..* BusinessProcessWorkflow "Business Processes Inline" "Inline BusinessProcessWorkflow instance data"

// Core Data Elements
* dataElementsUrl 0..* url "Data Elements URL" "URL to retrieve CoreDataElement definition from input/ or external source"
* dataElementsCanonical 0..* canonical "Data Elements Canonical" "Canonical URI pointing to the CoreDataElement definition"
* dataElementsCanonical ^type[0].targetProfile = "http://smart.who.int/base/StructureDefinition/CoreDataElement"
* dataElementsInline 0..* CoreDataElement "Data Elements Inline" "Inline CoreDataElement instance data"

// Decision-Support Logic
* decisionLogicUrl 0..* url "Decision Logic URL" "URL to retrieve DecisionSupportLogic definition from input/ or external source"
* decisionLogicCanonical 0..* canonical "Decision Logic Canonical" "Canonical URI pointing to the DecisionSupportLogic definition"
* decisionLogicCanonical ^type[0].targetProfile = "http://smart.who.int/base/StructureDefinition/DecisionSupportLogic"
* decisionLogicInline 0..* DecisionSupportLogic "Decision Logic Inline" "Inline DecisionSupportLogic instance data"

// Program Indicators
* indicatorsUrl 0..* url "Indicators URL" "URL to retrieve ProgramIndicator definition from input/ or external source"
* indicatorsCanonical 0..* canonical "Indicators Canonical" "Canonical URI pointing to the ProgramIndicator definition"
* indicatorsCanonical ^type[0].targetProfile = "http://smart.who.int/base/StructureDefinition/ProgramIndicator"
* indicatorsInline 0..* ProgramIndicator "Indicators Inline" "Inline ProgramIndicator instance data"

// Functional and Non-Functional Requirements
* requirementsUrl 0..* url "Requirements URL" "URL to retrieve Requirements definition from input/ or external source"
* requirementsCanonical 0..* canonical "Requirements Canonical" "Canonical URI pointing to the Requirements definition"
* requirementsCanonical ^type[0].targetProfile = "http://smart.who.int/base/StructureDefinition/Requirements"
* requirementsInline 0..* Requirements "Requirements Inline" "Inline Requirements instance data"

// Test Scenarios
* testScenariosUrl 0..* url "Test Scenarios URL" "URL to retrieve TestScenario definition from input/ or external source"
* testScenariosCanonical 0..* canonical "Test Scenarios Canonical" "Canonical URI pointing to the TestScenario definition"
* testScenariosCanonical ^type[0].targetProfile = "http://smart.who.int/base/StructureDefinition/TestScenario"
* testScenariosInline 0..* TestScenario "Test Scenarios Inline" "Inline TestScenario instance data"