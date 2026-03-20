Instance: SGAuthoring.Skills.AuthorLogicalModels
InstanceOf: SGRequirements
Usage: #definition
* status = #draft
* experimental = true
* name = "SkillAuthorLogicalModels"
* title = "Can author logical models"
* description = "Capability to create FHIR logical models (StructureDefinitions) from L2 data dictionaries."
* actor[+] = Canonical(SGAuthoring.Persona.FHIRModeller)

* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"

* extension[userstory][+].extension[capability].valueString = "create FHIR logical models from L2 data dictionaries"
* extension[userstory][=].extension[benefit].valueString = "data elements are formally modelled and mapped to standard terminologies for interoperability"

* statement[+].key = "LM-01"
* statement[=].label = "Create StructureDefinition from data dictionary"
* statement[=].requirement = "Can create a FHIR StructureDefinition (kind: logical) for each core data set from the L2 data dictionary."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "LM-02"
* statement[=].label = "Map elements to WHO Commons"
* statement[=].requirement = "Can ensure every data element in the logical model is mapped to a WHO Commons concept in the WHO Common dictionary."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "LM-03"
* statement[=].label = "Add standard terminology mappings"
* statement[=].requirement = "Can add mappings to LOINC, SNOMED, ICD-11, and other standard terminologies on logical model elements."
* statement[=].conformance[+] = #SHOULD

* statement[+].key = "LM-04"
* statement[=].label = "Write FSH for logical models"
* statement[=].requirement = "Can author logical models using FHIR Shorthand (FSH) syntax."
* statement[=].conformance[+] = #SHALL


Instance: SGAuthoring.Skills.AuthorFHIRProfiles
InstanceOf: SGRequirements
Usage: #definition
* status = #draft
* experimental = true
* name = "SkillAuthorFHIRProfiles"
* title = "Can author FHIR profiles"
* description = "Capability to create FHIR profiles (StructureDefinitions) constraining base FHIR resources."
* actor[+] = Canonical(SGAuthoring.Persona.FHIRModeller)

* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"

* extension[userstory][+].extension[capability].valueString = "create FHIR profiles constraining base FHIR resources"
* extension[userstory][=].extension[benefit].valueString = "resource structures are constrained and validated for DAK-specific use cases"

* statement[+].key = "PROF-01"
* statement[=].label = "Create resource profiles"
* statement[=].requirement = "Can create FHIR StructureDefinition profiles that constrain base FHIR resources for DAK use cases."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "PROF-02"
* statement[=].label = "Apply CRMI conformance profiles"
* statement[=].requirement = "Can ensure profiles conform to CRMI Shareable, Publishable, Computable, and Executable profiles as appropriate."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "PROF-03"
* statement[=].label = "Bind terminology"
* statement[=].requirement = "Can add appropriate terminology bindings (required, extensible, preferred) to profile elements."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "PROF-04"
* statement[=].label = "Write FSH for profiles"
* statement[=].requirement = "Can author profiles using FHIR Shorthand (FSH) syntax."
* statement[=].conformance[+] = #SHALL


Instance: SGAuthoring.Skills.AuthorQuestionnaires
InstanceOf: SGRequirements
Usage: #definition
* status = #draft
* experimental = true
* name = "SkillAuthorQuestionnaires"
* title = "Can author questionnaires"
* description = "Capability to create FHIR Questionnaire resources aligned with L2 forms and data collection needs."
* actor[+] = Canonical(SGAuthoring.Persona.FHIRModeller)

* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"

* extension[userstory][+].extension[capability].valueString = "create FHIR Questionnaire resources aligned with L2 data collection forms"
* extension[userstory][=].extension[benefit].valueString = "data collection instruments are standardized and linked to the logical model"

* statement[+].key = "QUEST-01"
* statement[=].label = "Create FHIR Questionnaires"
* statement[=].requirement = "Can create FHIR Questionnaire resources aligned with L2 data collection forms and workflow activities."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "QUEST-02"
* statement[=].label = "Conform to SDC profiles"
* statement[=].requirement = "Can ensure questionnaires conform to SDC (Structured Data Capture) profiles."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "QUEST-03"
* statement[=].label = "Link to logical models"
* statement[=].requirement = "Can link questionnaire items to corresponding logical model data elements."
* statement[=].conformance[+] = #SHALL


Instance: SGAuthoring.Skills.AuthorCQL
InstanceOf: SGRequirements
Usage: #definition
* status = #draft
* experimental = true
* name = "SkillAuthorCQL"
* title = "Can author CQL"
* description = "Capability to write Clinical Quality Language (CQL) for decision logic, scheduling logic, and indicator calculations."
* actor[+] = Canonical(SGAuthoring.Persona.FHIRModeller)

* extension[task][+].valueCoding = $SGTasks#scriptTask "Script Task"
* extension[task][+].valueCoding = $SGTasks#scriptTask "Script Task"
* extension[task][+].valueCoding = $SGTasks#scriptTask "Script Task"
* extension[task][+].valueCoding = $SGTasks#scriptTask "Script Task"
* extension[task][+].valueCoding = $SGTasks#scriptTask "Script Task"

* extension[userstory][+].extension[capability].valueString = "write CQL for decision logic, scheduling logic, and indicator calculations"
* extension[userstory][=].extension[benefit].valueString = "clinical decision-support and indicator calculations are computable and testable"

* statement[+].key = "CQL-01"
* statement[=].label = "Write CQL decision logic"
* statement[=].requirement = "Can write CQL libraries implementing L2 decision-support logic tables."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "CQL-02"
* statement[=].label = "Write CQL scheduling logic"
* statement[=].requirement = "Can write CQL libraries implementing L2 scheduling logic tables."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "CQL-03"
* statement[=].label = "Write CQL indicator logic"
* statement[=].requirement = "Can write CQL libraries implementing indicator calculations with numerator/denominator definitions."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "CQL-04"
* statement[=].label = "Create CQL concept definitions"
* statement[=].requirement = "Can create CQL concept and data element definitions for use across libraries."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "CQL-05"
* statement[=].label = "Test CQL execution"
* statement[=].requirement = "Can validate CQL execution against test data using reference tooling."
* statement[=].conformance[+] = #SHALL


Instance: SGAuthoring.Skills.AuthorStructureMaps
InstanceOf: SGRequirements
Usage: #definition
* status = #draft
* experimental = true
* name = "SkillAuthorStructureMaps"
* title = "Can author structure maps"
* description = "Capability to create FHIR StructureMaps for data extraction from QuestionnaireResponses to FHIR resources."
* actor[+] = Canonical(SGAuthoring.Persona.FHIRModeller)

* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#scriptTask "Script Task"

* extension[userstory][+].extension[capability].valueString = "create FHIR StructureMaps for data extraction from QuestionnaireResponses"
* extension[userstory][=].extension[benefit].valueString = "questionnaire data is automatically extracted into structured FHIR resources"

* statement[+].key = "SMAP-01"
* statement[=].label = "Create StructureMaps"
* statement[=].requirement = "Can create FHIR StructureMaps for extracting data from QuestionnaireResponses into FHIR resources."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "SMAP-02"
* statement[=].label = "Map to IPS"
* statement[=].requirement = "Can create StructureMaps mapping logical models to the International Patient Summary (IPS) data set."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "SMAP-03"
* statement[=].label = "Validate extraction output"
* statement[=].requirement = "Can validate that StructureMap extraction produces exactly the expected output using reference tooling."
* statement[=].conformance[+] = #SHALL


Instance: SGAuthoring.Skills.AuthorPlanDefinitions
InstanceOf: SGRequirements
Usage: #definition
* status = #draft
* experimental = true
* name = "SkillAuthorPlanDefinitions"
* title = "Can author plan definitions"
* description = "Capability to create FHIR PlanDefinitions for business processes and decision tables."
* actor[+] = Canonical(SGAuthoring.Persona.FHIRModeller)

* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"

* extension[userstory][+].extension[capability].valueString = "create FHIR PlanDefinitions for business processes and decision tables"
* extension[userstory][=].extension[benefit].valueString = "business processes and decision logic are formally represented as executable FHIR resources"

* statement[+].key = "PLAN-01"
* statement[=].label = "Create business process PlanDefinitions"
* statement[=].requirement = "Can create FHIR PlanDefinitions of type workflow-definition for each L2 business process."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "PLAN-02"
* statement[=].label = "Define actions and participants"
* statement[=].requirement = "Can define action elements with title, description, participant (persona), and relatedAction (flow) for each process node."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "PLAN-03"
* statement[=].label = "Conform to CRMI profiles"
* statement[=].requirement = "Can ensure PlanDefinitions conform to CRMIShareablePlanDefinition and CRMIPublishablePlanDefinition profiles."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "PLAN-04"
* statement[=].label = "Create decision table PlanDefinitions"
* statement[=].requirement = "Can create FHIR PlanDefinitions implementing L2 decision tables with associated CQL libraries."
* statement[=].conformance[+] = #SHALL


Instance: SGAuthoring.Skills.AuthorActorDefinitions
InstanceOf: SGRequirements
Usage: #definition
* status = #draft
* experimental = true
* name = "SkillAuthorActorDefinitions"
* title = "Can author actor definitions"
* description = "Capability to create FHIR ActorDefinitions from L2 personas, reusing existing definitions from the Commons repository."
* actor[+] = Canonical(SGAuthoring.Persona.FHIRModeller)

* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"

* extension[userstory][+].extension[capability].valueString = "create FHIR ActorDefinitions from L2 personas"
* extension[userstory][=].extension[benefit].valueString = "personas are formally defined as reusable FHIR resources across SMART Guidelines IGs"

* statement[+].key = "ACTOR-01"
* statement[=].label = "Reuse Commons personas"
* statement[=].requirement = "Can check the Commons repository for existing ActorDefinitions and reuse them when adequate."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "ACTOR-02"
* statement[=].label = "Create new ActorDefinitions"
* statement[=].requirement = "Can create draft ActorDefinitions with appropriate name, title, description, and type when no existing persona fits."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "ACTOR-03"
* statement[=].label = "Submit for governance approval"
* statement[=].requirement = "Can submit new persona definitions to the Commons governance process for approval before final publication."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "ACTOR-04"
* statement[=].label = "Write FSH for ActorDefinitions"
* statement[=].requirement = "Can author ActorDefinition instances using FHIR Shorthand (FSH) syntax."
* statement[=].conformance[+] = #SHALL


Instance: SGAuthoring.Skills.AuthorExampleScenarios
InstanceOf: SGRequirements
Usage: #definition
* status = #draft
* experimental = true
* name = "SkillAuthorExampleScenarios"
* title = "Can author example scenarios"
* description = "Capability to create ExampleScenario resources from L2 user scenarios."
* actor[+] = Canonical(SGAuthoring.Persona.FHIRModeller)

* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"

* extension[userstory][+].extension[capability].valueString = "create ExampleScenario resources from L2 user scenarios"
* extension[userstory][=].extension[benefit].valueString = "user scenarios are formally represented and linked to actors and business processes"

* statement[+].key = "EXSC-01"
* statement[=].label = "Create ExampleScenario resources"
* statement[=].requirement = "Can create FHIR ExampleScenario resources that formalize L2 user scenarios."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "EXSC-02"
* statement[=].label = "Link to actors and processes"
* statement[=].requirement = "Can link ExampleScenarios to corresponding ActorDefinitions and PlanDefinitions."
* statement[=].conformance[+] = #SHALL


Instance: SGAuthoring.Skills.AuthorMeasures
InstanceOf: SGRequirements
Usage: #definition
* status = #draft
* experimental = true
* name = "SkillAuthorMeasures"
* title = "Can author measures"
* description = "Capability to create FHIR Measure resources from L2 indicators."
* actor[+] = Canonical(SGAuthoring.Persona.FHIRModeller)

* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"

* extension[userstory][+].extension[capability].valueString = "create FHIR Measure resources from L2 indicators"
* extension[userstory][=].extension[benefit].valueString = "indicator calculations are computable and aligned with the Data Sharing Specification"

* statement[+].key = "MEAS-01"
* statement[=].label = "Create Measure resources"
* statement[=].requirement = "Can create FHIR Measure resources with population criteria referencing CQL indicator logic."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "MEAS-02"
* statement[=].label = "Define numerator and denominator"
* statement[=].requirement = "Can define numerator and denominator populations using CQL expressions."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "MEAS-03"
* statement[=].label = "Apply DSS specification"
* statement[=].requirement = "Can define measures according to the Data Sharing Specification (DSS) described in the IHE White Paper for mADX."
* statement[=].conformance[+] = #SHOULD


Instance: SGAuthoring.Skills.AuthorFHIRRequirements
InstanceOf: SGRequirements
Usage: #definition
* status = #draft
* experimental = true
* name = "SkillAuthorFHIRRequirements"
* title = "Can author FHIR requirements"
* description = "Capability to create FHIR Requirements resources from L2 functional and non-functional requirements."
* actor[+] = Canonical(SGAuthoring.Persona.FHIRModeller)

* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"

* extension[userstory][+].extension[capability].valueString = "create FHIR Requirements resources from L2 functional and non-functional requirements"
* extension[userstory][=].extension[benefit].valueString = "requirements are formally tracked as FHIR resources with traceability to actors and processes"

* statement[+].key = "FHIRREQ-01"
* statement[=].label = "Create Requirements resources"
* statement[=].requirement = "Can create FHIR Requirements resources representing L2 functional and non-functional requirements."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "FHIRREQ-02"
* statement[=].label = "Define requirement statements"
* statement[=].requirement = "Can define requirement statements with key, label, conformance level, and requirement text."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "FHIRREQ-03"
* statement[=].label = "Link to actors"
* statement[=].requirement = "Can link Requirements resources to the appropriate ActorDefinitions."
* statement[=].conformance[+] = #SHALL


Instance: SGAuthoring.Skills.AuthorTestCases
InstanceOf: SGRequirements
Usage: #definition
* status = #draft
* experimental = true
* name = "SkillAuthorTestCases"
* title = "Can author test cases"
* description = "Capability to create TestPlan, TestScript, and example instances for validation of L3 artifacts."
* actor[+] = Canonical(SGAuthoring.Persona.FHIRModeller)

* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#scriptTask "Script Task"

* extension[userstory][+].extension[capability].valueString = "create TestPlan, TestScript, and example instances for validation"
* extension[userstory][=].extension[benefit].valueString = "L3 artifacts are validated against defined acceptance criteria with reproducible tests"

* statement[+].key = "TEST-01"
* statement[=].label = "Create TestPlan resources"
* statement[=].requirement = "Can create FHIR TestPlan resources defining test scope and acceptance criteria."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "TEST-02"
* statement[=].label = "Create TestScript resources"
* statement[=].requirement = "Can create FHIR TestScript resources for automated validation."
* statement[=].conformance[+] = #SHOULD

* statement[+].key = "TEST-03"
* statement[=].label = "Create example instances"
* statement[=].requirement = "Can create example resource instances for each non-abstract profile in each UN language."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "TEST-04"
* statement[=].label = "Create test data"
* statement[=].requirement = "Can create test data or Synthea scripts for validating CQL execution and measure calculation."
* statement[=].conformance[+] = #SHOULD
