CodeSystem: DAK
Title: "Digital Adaptation Kit (DAK) Components"
Description: "CodeSystem for Digital Adaptation Kit (DAK) components and concepts defined across all 8 DAK components"
* ^experimental = true
* ^caseSensitive = false
* ^status = #active

// Business Processes
* #business-process "Business Process" "Business process workflow or procedure"
* #actor "Actor" "Person, role, or system that participates in business processes"
* #persona "Persona" "Characterization of a user type for system design"

// Specific Actors
* #health-worker "Health Worker" "Healthcare professional providing medical services"
* #patient "Patient" "Individual receiving healthcare services"
* #administrator "Administrator" "System administrator or healthcare facility administrator"

// Decision Support Logic
* #decision-table "Decision Table" "Decision logic represented as a table"
* #decision-rule "Decision Rule" "Individual decision rule or condition"
* #scheduling-table "Scheduling Table" "Special case of decision table for scheduling logic"

// Indicators & Measures
* #indicator "Indicator" "Measurable metric for monitoring and evaluation"
* #measure "Measure" "Calculated measurement or assessment"

// Data Entry Forms
* #form "Form" "Data collection form or questionnaire"
* #form-field "Form Field" "Individual field within a form"

// Terminology
* #concept "Concept" "Terminology concept or term"
* #concept-relationship "Concept Relationship" "Relationship between terminology concepts"

// FHIR Profiles
* #profile "Profile" "FHIR profile specification"
* #constraint "Constraint" "Constraint applied in a profile"

// FHIR Extensions
* #extension "Extension" "FHIR extension definition"

// Test Data & Examples
* #test-case "Test Case" "Test scenario or example"
* #example "Example" "Sample data or instance"