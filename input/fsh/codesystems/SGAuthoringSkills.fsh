CodeSystem: SGAuthoringSkills
Title:        "SMART Guidelines Authoring Skills"
Description:  """
CodeSystem for SMART Guidelines authoring skill capabilities.
Each code represents a discrete skill that an authoring persona may possess.
Skills are used to define Requirements resources as capability statements.
"""

* ^experimental = true
* ^caseSensitive = false
* ^status = #active

// L1 Skills
* #can-review-l1-guidelines "Can review L1 guidelines" "Ability to review WHO L1 narrative guidelines and normative products for accuracy and completeness"
* #can-interpret-clinical-recommendations "Can interpret clinical recommendations" "Ability to interpret clinical recommendations from L1 source documents"
* #can-identify-health-interventions "Can identify health interventions" "Ability to identify and catalogue health interventions from WHO UHC menu and guidelines"

// L2 DAK Authoring Skills
* #can-author-personas "Can author personas" "Ability to define generic personas based on task-shifting guidelines and ground-truthing"
* #can-author-user-scenarios "Can author user scenarios" "Ability to create user scenario narratives depicting typical workflows"
* #can-author-business-processes "Can author business processes" "Ability to create BPMN 2.0 business process diagrams for DAK workflows"
* #can-author-data-dictionary "Can author data dictionary" "Ability to define core data elements and map to standard terminologies"
* #can-author-decision-logic "Can author decision-support logic" "Ability to develop decision-support logic tables following DMN standard"
* #can-author-scheduling-logic "Can author scheduling logic" "Ability to develop scheduling logic tables following DMN standard"
* #can-author-indicators "Can author indicators" "Ability to define indicators and performance metrics with numerator/denominator specifications"
* #can-author-functional-requirements "Can author functional requirements" "Ability to define high-level functional and non-functional requirements"
* #can-validate-dak-content "Can validate DAK content" "Ability to review and validate DAK components against L1 source documents"

// L3 FHIR Authoring Skills
* #can-author-logical-models "Can author logical models" "Ability to create FHIR logical models from L2 data dictionaries"
* #can-author-fhir-profiles "Can author FHIR profiles" "Ability to create FHIR StructureDefinitions and profiles"
* #can-author-questionnaires "Can author questionnaires" "Ability to create FHIR Questionnaire resources from L2 forms"
* #can-author-cql "Can author CQL" "Ability to write Clinical Quality Language for decision logic, scheduling, and indicators"
* #can-author-structure-maps "Can author structure maps" "Ability to create FHIR StructureMaps for data extraction"
* #can-author-plan-definitions "Can author plan definitions" "Ability to create FHIR PlanDefinitions for business processes and decision tables"
* #can-author-actor-definitions "Can author actor definitions" "Ability to create FHIR ActorDefinitions from L2 personas"
* #can-author-example-scenarios "Can author example scenarios" "Ability to create ExampleScenario resources from L2 user scenarios"
* #can-author-measures "Can author measures" "Ability to create FHIR Measure resources from L2 indicators"
* #can-author-fhir-requirements "Can author FHIR requirements" "Ability to create FHIR Requirements resources from L2 requirements"
* #can-author-test-cases "Can author test cases" "Ability to create TestPlan, TestScript, and example instances for validation"

// Terminology Skills
* #can-review-terminology "Can review terminology" "Ability to review and validate terminology bindings, code systems, and value sets"
* #can-map-concepts "Can map concepts" "Ability to map data elements to WHO Commons dictionary, ICD-11, SNOMED CT, LOINC"
* #can-author-code-systems "Can author code systems" "Ability to create and maintain FHIR CodeSystem resources"
* #can-author-value-sets "Can author value sets" "Ability to create and maintain FHIR ValueSet resources"
* #can-author-concept-maps "Can author concept maps" "Ability to create FHIR ConceptMap resources for cross-terminology mappings"

// Quality Control Skills
* #can-run-qa-checks "Can run QA checks" "Ability to run and interpret IG Publisher QA validation reports"
* #can-review-checklist "Can review checklist" "Ability to review SMART Guidelines publication checklist across L1-L4 layers"
* #can-validate-artifact-conformance "Can validate artifact conformance" "Ability to verify conformance to Shareable, Publishable, Computable, and Executable profiles"
* #can-validate-l3-functionality "Can validate L3 functionality" "Ability to test StructureMap extraction, CQL execution, and measure calculation"

// Publication Skills
* #can-configure-ig "Can configure IG" "Ability to set up and configure a FHIR Implementation Guide (sushi-config, canonical URL, packages)"
* #can-build-ig "Can build IG" "Ability to run the FHIR IG Publisher build process"
* #can-manage-releases "Can manage releases" "Ability to manage versioning, publication-request.json, release tags, and publication workflow"
* #can-manage-governance "Can manage governance" "Ability to manage cross-IG governance for shared artifacts (commons personas, terminology, libraries)"

// Translation Skills
* #can-translate-content "Can translate content" "Ability to translate IG content across UN languages"
* #can-review-translations "Can review translations" "Ability to review translated content for accuracy and completeness"

// Project Management Skills
* #can-scope-dak "Can scope DAK" "Ability to define DAK scope, identify source documents, and establish development process"
* #can-manage-stakeholders "Can manage stakeholders" "Ability to engage SMEs, coordinate consultations, and manage RASCI matrix"
* #can-plan-iterations "Can plan iterations" "Ability to plan sprint iterations, maintain backlog, and facilitate retrospectives"
