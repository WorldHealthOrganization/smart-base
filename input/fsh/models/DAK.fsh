Logical: DAK
Title: "Digital Adaptation Kit (DAK)"
Description: "Logical Model for representing a complete Digital Adaptation Kit (DAK) with metadata and all 9 DAK components"

* ^status = #active

// Core DAK metadata fields (aligned with dak.json structure)
* id 1..1 string "DAK ID" "Identifier for the DAK (e.g., smart.who.int.base)"
* name 1..1 string "DAK Name" "Short name for the DAK (e.g., Base)"
* title 1..1 string "DAK Title" "Full title of the DAK (e.g., SMART Base)"
* description 1..1 string "DAK Description" "Description of the DAK"
* version 1..1 string "DAK Version" "Version of the DAK"
* status 1..1 code "DAK Status" "Publication status of the DAK"
* publicationUrl 1..1 url "Publication URL" "Canonical URL for the DAK (e.g., http://smart.who.int/base)"
* license 1..1 code "License" "License under which the DAK is published"
* copyrightYear 1..1 string "Copyright Year" "Year or year range for copyright"
* experimental 0..1 boolean "Experimental" "Whether this DAK is experimental"
* fhirVersion 1..1 string "FHIR Version" "Version of FHIR this DAK is built on"
* releaseLabel 0..1 string "Release Label" "Label for this release (e.g., ci-build, draft, ballot)"
* date 0..1 string "Date" "Date of last modification"

// Publisher information
* publisher 1..1 BackboneElement "Publisher" "Organization responsible for publishing the DAK"
  * name 1..1 string "Publisher Name" "Name of the publishing organization"
  * url 0..1 url "Publisher URL" "URL of the publishing organization"

// Contact, jurisdiction, use context
* contact 0..* ContactDetail "Contact Information" "Contact details for this DAK"
* useContext 0..* UsageContext "Use Context" "Context where this DAK is intended to be used"
* jurisdiction 0..* CodeableConcept "Jurisdiction" "Jurisdictions where this DAK applies"

// Dependencies
* dependencies 0..* BackboneElement "Dependencies" "Other IGs or packages this DAK depends on"
  * id 1..1 string "Dependency Package ID" "Package ID of the dependency"
  * version 1..1 string "Dependency Version" "Version of the dependency"
  * reason 0..1 string "Dependency Reason" "Reason for this dependency"

// Content structure (pages and menu)
* pages 0..* BackboneElement "Pages" "Custom pages included in the DAK"
  * filename 1..1 string "Page Filename" "Filename of the page (e.g., index.md)"
  * title 1..1 string "Page Title" "Title of the page"

* menu 0..* BackboneElement "Menu Structure" "Navigation menu structure for the DAK"
  * title 1..1 string "Menu Title" "Title of the menu item"
  * url 1..1 string "Menu URL" "URL of the menu item"
  * subItems 0..* BackboneElement "Sub Menu Items" "Sub-menu items"
    * title 1..1 string "Sub-item Title" "Title of the sub-menu item"
    * url 1..1 string "Sub-item URL" "URL of the sub-menu item"

// DAK-specific generation flags
* generateDmnQuestionnaires 0..1 boolean "Generate DMN Questionnaires" "Whether to generate FHIR Questionnaires from DMN files"
* transformDmnFiles 0..1 boolean "Transform DMN Files" "Whether to transform DMN files to HTML"
* generateValuesetSchemas 0..1 boolean "Generate ValueSet Schemas" "Whether to generate JSON schemas for ValueSets"
* generateLogicalModelSchemas 0..1 boolean "Generate Logical Model Schemas" "Whether to generate JSON schemas for Logical Models"
* generateDakApiHub 0..1 boolean "Generate DAK API Hub" "Whether to generate DAK API Documentation Hub"
* generateJsonldVocabularies 0..1 boolean "Generate JSON-LD Vocabularies" "Whether to generate JSON-LD vocabularies from ValueSet expansions"

// 9 DAK Components with cardinality 0..*
* healthInterventions 0..* HealthInterventions "Health Interventions and Recommendations" "Overview of the health interventions and WHO, regional or national recommendations included within the DAK"
* personas 0..* GenericPersona "Generic Personas" "Depiction of the human and system actors"
* userScenarios 0..* UserScenario "User Scenarios" "Narratives that describe how the different personas may interact with each other"
* businessProcesses 0..* BusinessProcessWorkflow "Generic Business Processes and Workflows" "Business processes and workflows for achieving health programme objectives"
* dataElements 0..* CoreDataElement "Core Data Elements" "Data elements required throughout the different points of a workflow"
* decisionLogic 0..* DecisionSupportLogic "Decision-Support Logic" "Decision-support logic and algorithms to support appropriate service delivery"
* indicators 0..* ProgramIndicator "Program Indicators" "Core set of indicators for decision-making, performance metrics and reporting"
* requirements 0..* Requirements "Functional and Non-Functional Requirements" "High-level list of core functions and capabilities that the system must have"
* testScenarios 0..* TestScenario "Test Scenarios" "Set of test scenarios to validate an implementation of the DAK"