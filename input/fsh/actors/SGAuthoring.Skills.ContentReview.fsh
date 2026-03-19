Instance: SGAuthoring.Skills.ReviewAndApproveContent
InstanceOf: SGRequirements
Usage: #definition
* status = #draft
* experimental = true
* name = "SkillReviewAndApproveContent"
* title = "Skill: Can review and approve content"
* description = "Capability to review and formally approve SMART Guidelines content at decision gates in the authoring lifecycle."

* statement[+].key = "APPROVE-01"
* statement[=].label = "Review L2 DAK for completeness"
* statement[=].requirement = "Can review all 9 DAK components for completeness, accuracy against L1 recommendations, and cross-component consistency."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "APPROVE-02"
* statement[=].label = "Approve L2 content for L3 authoring"
* statement[=].requirement = "Can formally approve L2 DAK content as ready for L3 FHIR authoring to begin."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "APPROVE-03"
* statement[=].label = "Review draft publication"
* statement[=].requirement = "Can review a draft IG publication (status=draft, releaseLabel=draft) and provide structured feedback."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "APPROVE-04"
* statement[=].label = "Approve for release publication"
* statement[=].requirement = "Can provide final sign-off for release publication after all review issues have been addressed."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "APPROVE-05"
* statement[=].label = "Assess change impact"
* statement[=].requirement = "Can assess whether content changes are breaking (non-compatible), compatible-substantive, or non-substantive for versioning decisions."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "APPROVE-06"
* statement[=].label = "Enforce governance policies"
* statement[=].requirement = "Can verify content aligns with WHO guidelines governance policies and cross-programme harmonization requirements."
* statement[=].conformance[+] = #SHALL
