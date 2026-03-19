Instance: SGAuthoring.Skills.ReviewL1Guidelines
InstanceOf: SGRequirements
Usage: #definition
* status = #draft
* experimental = true
* name = "SkillReviewL1Guidelines"
* title = "Skill: Can review L1 guidelines"
* description = "Capability to review WHO L1 narrative guidelines and normative products for accuracy and completeness."

* statement[+].key = "L1REV-01"
* statement[=].label = "Identify source documents"
* statement[=].requirement = "Can identify and locate relevant WHO guidelines, normative products, and associated publications for a given health area."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "L1REV-02"
* statement[=].label = "Extract health interventions"
* statement[=].requirement = "Can extract health interventions from the UHC menu of interventions and digital health interventions from the WHO classification."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "L1REV-03"
* statement[=].label = "Identify clinical recommendations"
* statement[=].requirement = "Can identify and interpret clinical recommendations embedded in L1 source documents."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "L1REV-04"
* statement[=].label = "Assess guideline currency"
* statement[=].requirement = "Can assess whether guidelines are recently updated and identify forward-looking system requirements."
* statement[=].conformance[+] = #SHOULD

* statement[+].key = "L1REV-05"
* statement[=].label = "Verify L2 coverage of L1"
* statement[=].requirement = "Can verify that L2 DAK components accurately reflect and cover the L1 recommendations."
* statement[=].conformance[+] = #SHALL


Instance: SGAuthoring.Skills.InterpretClinicalRecommendations
InstanceOf: SGRequirements
Usage: #definition
* status = #draft
* experimental = true
* name = "SkillInterpretClinicalRecommendations"
* title = "Skill: Can interpret clinical recommendations"
* description = "Capability to interpret clinical recommendations from L1 source documents with domain expertise."

* statement[+].key = "CLINREC-01"
* statement[=].label = "Interpret clinical protocols"
* statement[=].requirement = "Can interpret clinical protocols, treatment algorithms, and care pathways described in L1 guidelines."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "CLINREC-02"
* statement[=].label = "Validate clinical accuracy"
* statement[=].requirement = "Can validate that DAK decision-support logic and scheduling logic accurately represent clinical recommendations."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "CLINREC-03"
* statement[=].label = "Ground-truth with field practice"
* statement[=].requirement = "Can validate DAK content against real-world clinical practice through country visits and facility interviews."
* statement[=].conformance[+] = #SHOULD

* statement[+].key = "CLINREC-04"
* statement[=].label = "Assess cross-country applicability"
* statement[=].requirement = "Can assess whether workflows and recommendations hold across various country contexts (80/20 rule)."
* statement[=].conformance[+] = #SHALL
