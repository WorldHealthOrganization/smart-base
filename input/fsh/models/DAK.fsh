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





// 9 DAK Components with cardinality 0..* - each component can be either a URL, canonical reference, or inline instance
* healthInterventions[x] 0..* url or canonical or HealthInterventions "Health Interventions and Recommendations" "Each health intervention is either: (1) URL to retrieve definition from input/ or external source, (2) canonical reference to HealthInterventions, or (3) inline HealthInterventions instance data"
* personas[x] 0..* url or canonical or GenericPersona "Generic Personas" "Each persona is either: (1) URL to retrieve definition from input/ or external source, (2) canonical reference to GenericPersona, or (3) inline GenericPersona instance data"
* userScenarios[x] 0..* url or canonical or UserScenario "User Scenarios" "Each user scenario is either: (1) URL to retrieve definition from input/ or external source, (2) canonical reference to UserScenario, or (3) inline UserScenario instance data"
* businessProcesses[x] 0..* url or canonical or BusinessProcessWorkflow "Generic Business Processes and Workflows" "Each business process is either: (1) URL to retrieve definition from input/ or external source, (2) canonical reference to BusinessProcessWorkflow, or (3) inline BusinessProcessWorkflow instance data"
* dataElements[x] 0..* url or canonical or CoreDataElement "Core Data Elements" "Each data element is either: (1) URL to retrieve definition from input/ or external source, (2) canonical reference to CoreDataElement, or (3) inline CoreDataElement instance data"
* decisionLogic[x] 0..* url or canonical or DecisionSupportLogic "Decision-Support Logic" "Each decision logic is either: (1) URL to retrieve definition from input/ or external source, (2) canonical reference to DecisionSupportLogic, or (3) inline DecisionSupportLogic instance data"
* indicators[x] 0..* url or canonical or ProgramIndicator "Program Indicators" "Each indicator is either: (1) URL to retrieve definition from input/ or external source, (2) canonical reference to ProgramIndicator, or (3) inline ProgramIndicator instance data"
* requirements[x] 0..* url or canonical or Requirements "Functional and Non-Functional Requirements" "Each requirement is either: (1) URL to retrieve definition from input/ or external source, (2) canonical reference to Requirements, or (3) inline Requirements instance data"
* testScenarios[x] 0..* url or canonical or TestScenario "Test Scenarios" "Each test scenario is either: (1) URL to retrieve definition from input/ or external source, (2) canonical reference to TestScenario, or (3) inline TestScenario instance data"