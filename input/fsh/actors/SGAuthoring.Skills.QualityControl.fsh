Instance: SGAuthoring.Skills.RunQAChecks
InstanceOf: SGRequirements
Usage: #definition
* status = #draft
* experimental = true
* name = "SkillRunQAChecks"
* title = "Skill: Can run QA checks"
* description = "Capability to run and interpret IG Publisher QA validation reports."

* statement[+].key = "QA-01"
* statement[=].label = "Run IG Publisher QA"
* statement[=].requirement = "Can run the FHIR IG Publisher and locate the generated qa.html report."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "QA-02"
* statement[=].label = "Interpret QA errors and warnings"
* statement[=].requirement = "Can interpret QA validation errors, warnings, and information messages to identify issues requiring resolution."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "QA-03"
* statement[=].label = "Triage suppressions"
* statement[=].requirement = "Can assess whether warnings can be legitimately suppressed with reasonable explanation, and document suppressions."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "QA-04"
* statement[=].label = "Verify zero-error status"
* statement[=].requirement = "Can verify that the QA report shows no errors or unsuppressed warnings before publication."
* statement[=].conformance[+] = #SHALL


Instance: SGAuthoring.Skills.ReviewChecklist
InstanceOf: SGRequirements
Usage: #definition
* status = #draft
* experimental = true
* name = "SkillReviewChecklist"
* title = "Skill: Can review checklist"
* description = "Capability to review the SMART Guidelines publication checklist across L1-L4 layers and global requirements."

* statement[+].key = "CHKLST-01"
* statement[=].label = "Review L1 checklist"
* statement[=].requirement = "Can verify L1 checklist items: home page summary, providing feedback section, and adapting guidelines page."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "CHKLST-02"
* statement[=].label = "Review L2 checklist"
* statement[=].requirement = "Can verify L2 checklist items: concepts, personas, use cases, business processes, data dictionary, decision-support, indicators, and requirements pages."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "CHKLST-03"
* statement[=].label = "Review L3 checklist"
* statement[=].requirement = "Can verify L3 checklist items: system actors, sequence diagrams, transactions, logical models, indicators/measures, mappings, and artifact profile conformance."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "CHKLST-04"
* statement[=].label = "Review L4 checklist"
* statement[=].requirement = "Can verify L4 checklist items: example data per UN language, test definitions, test data, reference implementations, and downloads."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "CHKLST-05"
* statement[=].label = "Review global checklist"
* statement[=].requirement = "Can verify global checklist items: maturity level, versioning policy, HL7 publishing requirements, QA report, and changes page."
* statement[=].conformance[+] = #SHALL


Instance: SGAuthoring.Skills.ValidateArtifactConformance
InstanceOf: SGRequirements
Usage: #definition
* status = #draft
* experimental = true
* name = "SkillValidateArtifactConformance"
* title = "Skill: Can validate artifact conformance"
* description = "Capability to verify conformance to CRMI Shareable, Publishable, Computable, and Executable profiles."

* statement[+].key = "CONF-01"
* statement[=].label = "Check Shareable conformance"
* statement[=].requirement = "Can verify artifacts conform to CRMIShareable profiles (name, title, description, status)."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "CONF-02"
* statement[=].label = "Check Publishable conformance"
* statement[=].requirement = "Can verify active published artifacts conform to CRMIPublishable profiles."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "CONF-03"
* statement[=].label = "Check Computable conformance"
* statement[=].requirement = "Can verify artifacts conform to CRMIComputable profiles where applicable."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "CONF-04"
* statement[=].label = "Check Executable conformance"
* statement[=].requirement = "Can verify ValueSet and Library artifacts conform to CRMIExecutable profiles."
* statement[=].conformance[+] = #SHALL


Instance: SGAuthoring.Skills.ValidateL3Functionality
InstanceOf: SGRequirements
Usage: #definition
* status = #draft
* experimental = true
* name = "SkillValidateL3Functionality"
* title = "Skill: Can validate L3 functionality"
* description = "Capability to test StructureMap extraction, CQL execution, and measure calculation using reference tooling."

* statement[+].key = "L3FUNC-01"
* statement[=].label = "Test StructureMap extraction"
* statement[=].requirement = "Can execute StructureMaps against test QuestionnaireResponses and verify extracted resources match expected output."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "L3FUNC-02"
* statement[=].label = "Test CQL execution"
* statement[=].requirement = "Can execute CQL libraries against test data and verify decision logic, scheduling logic, and indicator calculations."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "L3FUNC-03"
* statement[=].label = "Test measure calculation"
* statement[=].requirement = "Can execute FHIR Measure evaluations and verify numerator/denominator calculations against expected results."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "L3FUNC-04"
* statement[=].label = "Verify L2 content coverage"
* statement[=].requirement = "Can manually verify that all L2 specifications are covered by corresponding L3 artifacts."
* statement[=].conformance[+] = #SHALL
