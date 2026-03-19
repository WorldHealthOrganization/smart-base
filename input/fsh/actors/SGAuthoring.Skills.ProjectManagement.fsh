Instance: SGAuthoring.Skills.ScopeDAK
InstanceOf: SGRequirements
Usage: #definition
* status = #draft
* experimental = true
* name = "SkillScopeDAK"
* title = "Skill: Can scope DAK"
* description = "Capability to define DAK scope, identify source documents, and establish the development process and governance."

* statement[+].key = "SCOPE-01"
* statement[=].label = "Define DAK purpose and target audience"
* statement[=].requirement = "Can articulate the purpose of the DAK, identify the target audience, assess whether similar publications exist, and define the gaps the DAK will address."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "SCOPE-02"
* statement[=].label = "Establish development process"
* statement[=].requirement = "Can establish the development process and governance to be used, including selection of agile methodology and determination of ownership and key stakeholders."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "SCOPE-03"
* statement[=].label = "Determine project tooling"
* statement[=].requirement = "Can determine the tools to be used for project tracking, communication, and DAK components design (e.g. BPMN tooling)."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "SCOPE-04"
* statement[=].label = "Assess resource requirements"
* statement[=].requirement = "Can assess the necessary resources to develop the DAK, including securing adequate budget for each step of the process."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "SCOPE-05"
* statement[=].label = "Gather source documents"
* statement[=].requirement = "Can gather and catalogue source documents including normative products, policy documents, paper registers, tally sheets, and reporting tools."
* statement[=].conformance[+] = #SHALL
