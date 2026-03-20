Instance: SGAuthoring.Skills.ManageStakeholders
InstanceOf: SGRequirements
Usage: #definition
* status = #draft
* experimental = true
* name = "SkillManageStakeholders"
* title = "Can manage stakeholders"
* description = "Capability to engage SMEs, coordinate consultations, and manage the RASCI matrix for DAK development."
* actor[+] = Canonical(SGAuthoring.Persona.ProgrammeManager)

* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"

* extension[userstory][+].extension[capability].valueString = "engage SMEs, coordinate consultations, and manage the RASCI matrix"
* extension[userstory][=].extension[benefit].valueString = "all stakeholders are appropriately engaged with clear roles throughout DAK development"

* statement[+].key = "STAKEHOLDER-01"
* statement[=].label = "Define RASCI matrix"
* statement[=].requirement = "Can define and maintain a RASCI (Responsible, Accountable, Support, Consulted, Informed) matrix for all DAK activities."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "STAKEHOLDER-02"
* statement[=].label = "Engage guideline stewards"
* statement[=].requirement = "Can ensure that authors of source documents and subject matter experts are actively engaged in collaborative DAK development."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "STAKEHOLDER-03"
* statement[=].label = "Plan SME consultations"
* statement[=].requirement = "Can define meeting cadence and format for SME consultations, including workshops, in-person country visits, and online sessions."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "STAKEHOLDER-04"
* statement[=].label = "Prepare consultation materials"
* statement[=].requirement = "Can create agendas, question lists, and visual aids for SME consultation meetings."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "STAKEHOLDER-05"
* statement[=].label = "Coordinate cross-programme collaboration"
* statement[=].requirement = "Can identify and coordinate with other health programmes for overlapping components such as shared indicators or data items."
* statement[=].conformance[+] = #SHOULD


Instance: SGAuthoring.Skills.PlanIterations
InstanceOf: SGRequirements
Usage: #definition
* status = #draft
* experimental = true
* name = "SkillPlanIterations"
* title = "Can plan iterations"
* description = "Capability to plan sprint iterations, maintain the DAK backlog, draft the project roadmap, and facilitate retrospectives."
* actor[+] = Canonical(SGAuthoring.Persona.ProgrammeManager)

* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"
* extension[task][+].valueCoding = $SGTasks#userTask "User Task"

* extension[userstory][+].extension[capability].valueString = "plan sprint iterations, maintain the backlog, and facilitate retrospectives"
* extension[userstory][=].extension[benefit].valueString = "DAK development proceeds in focused, time-boxed increments with continuous improvement"

* statement[+].key = "ITERATE-01"
* statement[=].label = "Maintain DAK backlog"
* statement[=].requirement = "Can create and maintain a prioritized, estimated backlog of work items, decomposing big items into smaller items accomplishable in days."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "ITERATE-02"
* statement[=].label = "Plan iteration scope"
* statement[=].requirement = "Can plan fixed-length iterations (1 month or less) considering team capacity, prior results, and backlog items."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "ITERATE-03"
* statement[=].label = "Define iteration goals"
* statement[=].requirement = "Can define iteration goals that create coherence and focus for the team during each sprint."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "ITERATE-04"
* statement[=].label = "Facilitate retrospectives"
* statement[=].requirement = "Can facilitate retrospective meetings to assess what went well, identify problems, and improve team effectiveness."
* statement[=].conformance[+] = #SHOULD

* statement[+].key = "ITERATE-05"
* statement[=].label = "Draft project roadmap"
* statement[=].requirement = "Can draft a project roadmap with estimates for each phase and key milestone dates."
* statement[=].conformance[+] = #SHALL
