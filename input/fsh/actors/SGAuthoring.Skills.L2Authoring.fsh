Instance: SGAuthoring.Skills.AuthorPersonas
InstanceOf: SGRequirements
Usage: #definition
* status = #draft
* experimental = true
* name = "SkillAuthorPersonas"
* title = "Can author personas"
* description = "Capability to define generic personas based on task-shifting guidelines and ground-truthing interviews."
* actor[+] = Canonical(SGAuthoring.Persona.BusinessAnalyst)

* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"

* extension[userstory][+].extension[capability].valueString = "define generic personas from L1 guidance and SME consultations"
* extension[userstory][=].extension[benefit].valueString = "workflows accurately reflect the roles and competencies of health workers in real-world settings"

* statement[+].key = "PERSONA-01"
* statement[=].label = "Identify personas from L1 guidance"
* statement[=].requirement = "Can identify personas referenced in L1 normative guidance."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "PERSONA-02"
* statement[=].label = "Identify personas from SME consultations"
* statement[=].requirement = "Can identify personas participating in workflows through consultations with SMEs."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "PERSONA-03"
* statement[=].label = "Define persona competencies"
* statement[=].requirement = "Can define descriptions, competencies, and essential interventions performed by each persona."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "PERSONA-04"
* statement[=].label = "Ensure cross-component consistency"
* statement[=].requirement = "Can verify that the same persona names are used consistently across all DAK components."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "PERSONA-05"
* statement[=].label = "Validate through facility interviews"
* statement[=].requirement = "Can validate personas through in-person interviews at health facilities."
* statement[=].conformance[+] = #SHOULD


Instance: SGAuthoring.Skills.AuthorUserScenarios
InstanceOf: SGRequirements
Usage: #definition
* status = #draft
* experimental = true
* name = "SkillAuthorUserScenarios"
* title = "Can author user scenarios"
* description = "Capability to create user scenario narratives depicting typical interactions in health programme workflows."
* actor[+] = Canonical(SGAuthoring.Persona.BusinessAnalyst)

* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"

* extension[userstory][+].extension[capability].valueString = "create user scenario narratives depicting typical health worker interactions"
* extension[userstory][=].extension[benefit].valueString = "stakeholders can understand workflows through concrete, real-world examples"

* statement[+].key = "SCENARIO-01"
* statement[=].label = "Create workflow narratives"
* statement[=].requirement = "Can create high-level narratives based on the actual context the majority of end users operate in."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "SCENARIO-02"
* statement[=].label = "Illustrate typical interactions"
* statement[=].requirement = "Can illustrate user scenarios depicting typical interactions (screening, diagnosis, treatment, reporting)."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "SCENARIO-03"
* statement[=].label = "Include complex scenarios"
* statement[=].requirement = "Can include scenarios that are intricate in terms of normative guidance where helpful for understanding."
* statement[=].conformance[+] = #SHOULD

* statement[+].key = "SCENARIO-04"
* statement[=].label = "Align with business processes"
* statement[=].requirement = "Can ensure user scenario narratives align with the sequence of activities depicted in business process workflows."
* statement[=].conformance[+] = #SHALL


Instance: SGAuthoring.Skills.AuthorBusinessProcesses
InstanceOf: SGRequirements
Usage: #definition
* status = #draft
* experimental = true
* name = "SkillAuthorBusinessProcesses"
* title = "Can author business processes"
* description = "Capability to create BPMN 2.0 business process diagrams for DAK workflows."
* actor[+] = Canonical(SGAuthoring.Persona.BusinessAnalyst)

* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"

* extension[userstory][+].extension[capability].valueString = "create BPMN 2.0 business process diagrams for DAK workflows"
* extension[userstory][=].extension[benefit].valueString = "health programme workflows are clearly documented and implementable across country contexts"

* statement[+].key = "BPMN-01"
* statement[=].label = "Create BPMN 2.0 diagrams"
* statement[=].requirement = "Can create business process diagrams following the BPMN 2.0 standard."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "BPMN-02"
* statement[=].label = "Create overview process diagram"
* statement[=].requirement = "Can create an overview diagram reflecting all key business processes for the health area."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "BPMN-03"
* statement[=].label = "Create detailed workflow annotations"
* statement[=].requirement = "Can create detailed workflow annotations for each identified business process with activities, decision points, and interactions."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "BPMN-04"
* statement[=].label = "Apply 80/20 generalization rule"
* statement[=].requirement = "Can ensure workflows capture 80% of the scenario, leaving 20% for country-level adaptation."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "BPMN-05"
* statement[=].label = "Use swimlanes for personas"
* statement[=].requirement = "Can assign activities to the correct persona swimlanes in BPMN diagrams."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "BPMN-06"
* statement[=].label = "Identify sub-processes"
* statement[=].requirement = "Can identify repeating activities and refactor them into sub-processes or referenced business processes."
* statement[=].conformance[+] = #SHOULD


Instance: SGAuthoring.Skills.AuthorDataDictionary
InstanceOf: SGRequirements
Usage: #definition
* status = #draft
* experimental = true
* name = "SkillAuthorDataDictionary"
* title = "Can author data dictionary"
* description = "Capability to define core data elements and map to standard terminologies."
* actor[+] = Canonical(SGAuthoring.Persona.BusinessAnalyst)

* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"

* extension[userstory][+].extension[capability].valueString = "define core data elements and map them to standard terminologies"
* extension[userstory][=].extension[benefit].valueString = "data collection is standardized and interoperable across health information systems"

* statement[+].key = "DICT-01"
* statement[=].label = "Define data elements from workflows"
* statement[=].requirement = "Can define data elements required throughout different points of the workflow for service delivery and indicator reporting."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "DICT-02"
* statement[=].label = "Apply data capture criteria"
* statement[=].requirement = "Can apply the criterion that only data needed for reporting, auditing, decision-support, aggregation, or exchange should be captured."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "DICT-03"
* statement[=].label = "Map to standard terminologies"
* statement[=].requirement = "Can map data elements to standards-based classifications and terminologies (ICD, LOINC, SNOMED)."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "DICT-04"
* statement[=].label = "Identify and remove duplicates"
* statement[=].requirement = "Can identify duplicate data elements and consolidate Boolean data elements into List data elements where appropriate."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "DICT-05"
* statement[=].label = "Fill data dictionary template"
* statement[=].requirement = "Can complete the standardized DAK data dictionary spreadsheet template with detailed data specifications."
* statement[=].conformance[+] = #SHALL


Instance: SGAuthoring.Skills.AuthorDecisionLogic
InstanceOf: SGRequirements
Usage: #definition
* status = #draft
* experimental = true
* name = "SkillAuthorDecisionLogic"
* title = "Can author decision-support logic"
* description = "Capability to develop decision-support logic tables following the DMN standard."
* actor[+] = Canonical(SGAuthoring.Persona.BusinessAnalyst)

* extension[task][+].valueCoding = $SGTasks#businessRuleTask "Business Rule Task"
* extension[task][+].valueCoding = $SGTasks#businessRuleTask "Business Rule Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"

* extension[userstory][+].extension[capability].valueString = "develop decision-support logic tables following the DMN standard"
* extension[userstory][=].extension[benefit].valueString = "clinical decision-support recommendations are computable and consistently applied"

* statement[+].key = "DT-01"
* statement[=].label = "Create DMN-compliant decision tables"
* statement[=].requirement = "Can create decision-support logic tables following the normative contents of the DMN standard."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "DT-02"
* statement[=].label = "Define inputs, outputs, and triggers"
* statement[=].requirement = "Can define inputs, outputs, and triggers for each decision-support logic table in spreadsheet format."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "DT-03"
* statement[=].label = "Limit table complexity"
* statement[=].requirement = "Can avoid decision tables relying on 10+ inputs and split complex tables into separate, manageable tables."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "DT-04"
* statement[=].label = "Link to business process activities"
* statement[=].requirement = "Can link decision-support logic tables to the corresponding activities in business process workflows."
* statement[=].conformance[+] = #SHALL


Instance: SGAuthoring.Skills.AuthorSchedulingLogic
InstanceOf: SGRequirements
Usage: #definition
* status = #draft
* experimental = true
* name = "SkillAuthorSchedulingLogic"
* title = "Can author scheduling logic"
* description = "Capability to develop scheduling logic tables following the DMN standard."
* actor[+] = Canonical(SGAuthoring.Persona.BusinessAnalyst)

* extension[task][+].valueCoding = $SGTasks#businessRuleTask "Business Rule Task"
* extension[task][+].valueCoding = $SGTasks#businessRuleTask "Business Rule Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"

* extension[userstory][+].extension[capability].valueString = "develop scheduling logic tables following the DMN standard"
* extension[userstory][=].extension[benefit].valueString = "service reminders and follow-up visit schedules are automated and consistent"

* statement[+].key = "SCHED-01"
* statement[=].label = "Create scheduling logic tables"
* statement[=].requirement = "Can create scheduling logic tables following the DMN standard for service reminders and follow-up visits."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "SCHED-02"
* statement[=].label = "Define schedule parameters"
* statement[=].requirement = "Can define scheduling logic in spreadsheet format with appropriate timing, conditions, and service specifications."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "SCHED-03"
* statement[=].label = "Link to business process activities"
* statement[=].requirement = "Can link scheduling logic to corresponding activities in business process workflows."
* statement[=].conformance[+] = #SHALL


Instance: SGAuthoring.Skills.AuthorIndicators
InstanceOf: SGRequirements
Usage: #definition
* status = #draft
* experimental = true
* name = "SkillAuthorIndicators"
* title = "Can author indicators"
* description = "Capability to define indicators and performance metrics with numerator/denominator specifications."
* actor[+] = Canonical(SGAuthoring.Persona.BusinessAnalyst)

* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"

* extension[userstory][+].extension[capability].valueString = "define indicators and performance metrics with numerator/denominator specifications"
* extension[userstory][=].extension[benefit].valueString = "programme monitoring and evaluation is data-driven and standardized"

* statement[+].key = "IND-01"
* statement[=].label = "Define indicator specifications"
* statement[=].requirement = "Can define indicators with numerator, denominator, and appropriate disaggregation in the indicators table."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "IND-02"
* statement[=].label = "Focus on primary care level"
* statement[=].requirement = "Can focus on indicators derivable from data collected at the primary health care level, following 'collect once, use many' principle."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "IND-03"
* statement[=].label = "Verify data element availability"
* statement[=].requirement = "Can verify that all data elements needed for indicator calculation are captured in the data dictionary."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "IND-04"
* statement[=].label = "Reference WHO indicator standards"
* statement[=].requirement = "Can reference WHO indicators (data.who.int) for higher-level national and global aggregated reporting needs."
* statement[=].conformance[+] = #SHOULD


Instance: SGAuthoring.Skills.AuthorFunctionalRequirements
InstanceOf: SGRequirements
Usage: #definition
* status = #draft
* experimental = true
* name = "SkillAuthorFunctionalRequirements"
* title = "Can author functional requirements"
* description = "Capability to define high-level functional and non-functional requirements linked to personas and business processes."
* actor[+] = Canonical(SGAuthoring.Persona.BusinessAnalyst)

* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"

* extension[userstory][+].extension[capability].valueString = "define functional and non-functional requirements linked to personas and business processes"
* extension[userstory][=].extension[benefit].valueString = "implementation requirements are traceable to clinical guidance and user workflows"

* statement[+].key = "FREQ-01"
* statement[=].label = "Define functional requirements from L1"
* statement[=].requirement = "Can define functional requirements based on L1 recommendations in terms of health content, decision-support, and scheduling logic."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "FREQ-02"
* statement[=].label = "Define non-functional requirements"
* statement[=].requirement = "Can define non-functional requirements including user-friendliness and cybersecurity, informed by implementer best practices."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "FREQ-03"
* statement[=].label = "Link requirements to personas"
* statement[=].requirement = "Can link each functional requirement to the correct persona and business process activity."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "FREQ-04"
* statement[=].label = "Verify scenario coverage"
* statement[=].requirement = "Can verify that functionalities depicted in user scenarios are captured in the requirements list."
* statement[=].conformance[+] = #SHALL


Instance: SGAuthoring.Skills.ValidateDAKContent
InstanceOf: SGRequirements
Usage: #definition
* status = #draft
* experimental = true
* name = "SkillValidateDAKContent"
* title = "Can validate DAK content"
* description = "Capability to review and validate DAK components against L1 source documents and for cross-component consistency."
* actor[+] = Canonical(SGAuthoring.Persona.BusinessAnalyst)
* actor[+] = Canonical(SGAuthoring.Persona.ClinicalSME)

* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"

* extension[userstory][+].extension[capability].valueString = "review and validate DAK components against L1 source documents"
* extension[userstory][=].extension[benefit].valueString = "DAK content is accurate, consistent, and faithfully represents WHO clinical recommendations"

* statement[+].key = "DAKVAL-01"
* statement[=].label = "Verify L1 accuracy"
* statement[=].requirement = "Can verify that DAK components accurately reflect L1 recommendations."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "DAKVAL-02"
* statement[=].label = "Identify gaps and changes"
* statement[=].requirement = "Can identify gaps, key changes, and alternatives in DAK content."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "DAKVAL-03"
* statement[=].label = "Verify software neutrality"
* statement[=].requirement = "Can verify that DAK components are software-neutral and do not assume any specific software or device."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "DAKVAL-04"
* statement[=].label = "Streamline cross-component consistency"
* statement[=].requirement = "Can review DAK for cross-component consistency: persona naming, data element usage, workflow alignment, and requirement linkage."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "DAKVAL-05"
* statement[=].label = "Incorporate SME feedback"
* statement[=].requirement = "Can analyse feedback from SMEs, identify patterns, incorporate changes, and confirm accurate reflection of suggestions."
* statement[=].conformance[+] = #SHALL
