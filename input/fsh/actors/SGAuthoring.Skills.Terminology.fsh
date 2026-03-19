Instance: SGAuthoring.Skills.ReviewTerminology
InstanceOf: SGRequirements
Usage: #definition
* status = #draft
* experimental = true
* name = "SkillReviewTerminology"
* title = "Skill: Can review terminology"
* description = "Capability to review and validate terminology bindings, code systems, and value sets for correctness and completeness."

* statement[+].key = "TERMREV-01"
* statement[=].label = "Review CodeSystem definitions"
* statement[=].requirement = "Can review FHIR CodeSystem resources for correctness, completeness, and proper hierarchy."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "TERMREV-02"
* statement[=].label = "Review ValueSet compositions"
* statement[=].requirement = "Can review FHIR ValueSet resources for correct include/exclude criteria and appropriate expansion."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "TERMREV-03"
* statement[=].label = "Review terminology bindings"
* statement[=].requirement = "Can review terminology binding strength (required, extensible, preferred) on profiles and logical models."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "TERMREV-04"
* statement[=].label = "Identify terminology QA issues"
* statement[=].requirement = "Can identify unapproved concepts, missing mappings, and duplicate definitions from QA reports."
* statement[=].conformance[+] = #SHALL


Instance: SGAuthoring.Skills.MapConcepts
InstanceOf: SGRequirements
Usage: #definition
* status = #draft
* experimental = true
* name = "SkillMapConcepts"
* title = "Skill: Can map concepts"
* description = "Capability to map data elements to WHO Commons dictionary, ICD-11, SNOMED CT, LOINC, and other standard terminologies."

* statement[+].key = "CMAP-01"
* statement[=].label = "Map to WHO Commons dictionary"
* statement[=].requirement = "Can map every data element to a WHO Commons concept, ensuring the pivotal semantic reference is maintained."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "CMAP-02"
* statement[=].label = "Map to ICD-11 and WHO FIC"
* statement[=].requirement = "Can map concepts to ICD-11 or WHO Family of International Classifications where content exists."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "CMAP-03"
* statement[=].label = "Map to SNOMED CT and LOINC"
* statement[=].requirement = "Can map concepts to SNOMED CT, LOINC, and other openly available reference vocabularies."
* statement[=].conformance[+] = #SHOULD

* statement[+].key = "CMAP-04"
* statement[=].label = "Onboard new concepts"
* statement[=].requirement = "Can onboard new concepts into the Commons dictionary, whether from scratch or from existing reference dictionaries."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "CMAP-05"
* statement[=].label = "Verify no overlaps or duplicates"
* statement[=].requirement = "Can verify that new concepts do not duplicate or overlap with existing concepts in the Commons dictionary."
* statement[=].conformance[+] = #SHALL


Instance: SGAuthoring.Skills.AuthorCodeSystems
InstanceOf: SGRequirements
Usage: #definition
* status = #draft
* experimental = true
* name = "SkillAuthorCodeSystems"
* title = "Skill: Can author code systems"
* description = "Capability to create and maintain FHIR CodeSystem resources."

* statement[+].key = "CS-01"
* statement[=].label = "Create CodeSystem resources"
* statement[=].requirement = "Can create FHIR CodeSystem resources with appropriate properties, hierarchy, and designations."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "CS-02"
* statement[=].label = "Maintain CodeSystem versioning"
* statement[=].requirement = "Can manage CodeSystem versioning following SMART Guidelines change tracking policies."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "CS-03"
* statement[=].label = "Write FSH for CodeSystems"
* statement[=].requirement = "Can author CodeSystem definitions using FHIR Shorthand (FSH) syntax."
* statement[=].conformance[+] = #SHALL


Instance: SGAuthoring.Skills.AuthorValueSets
InstanceOf: SGRequirements
Usage: #definition
* status = #draft
* experimental = true
* name = "SkillAuthorValueSets"
* title = "Skill: Can author value sets"
* description = "Capability to create and maintain FHIR ValueSet resources with appropriate terminology bindings."

* statement[+].key = "VS-01"
* statement[=].label = "Create ValueSet resources"
* statement[=].requirement = "Can create FHIR ValueSet resources with appropriate include/exclude criteria."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "VS-02"
* statement[=].label = "Conform to Executable profile"
* statement[=].requirement = "Can ensure ValueSets conform to the CRMI Executable profile where required."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "VS-03"
* statement[=].label = "Write FSH for ValueSets"
* statement[=].requirement = "Can author ValueSet definitions using FHIR Shorthand (FSH) syntax."
* statement[=].conformance[+] = #SHALL


Instance: SGAuthoring.Skills.AuthorConceptMaps
InstanceOf: SGRequirements
Usage: #definition
* status = #draft
* experimental = true
* name = "SkillAuthorConceptMaps"
* title = "Skill: Can author concept maps"
* description = "Capability to create FHIR ConceptMap resources for cross-terminology mappings."

* statement[+].key = "CM-01"
* statement[=].label = "Create ConceptMap resources"
* statement[=].requirement = "Can create FHIR ConceptMap resources defining mappings between source and target code systems."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "CM-02"
* statement[=].label = "Define equivalence relationships"
* statement[=].requirement = "Can define appropriate equivalence relationships (equivalent, wider, narrower, etc.) between mapped concepts."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "CM-03"
* statement[=].label = "Write FSH for ConceptMaps"
* statement[=].requirement = "Can author ConceptMap definitions using FHIR Shorthand (FSH) syntax."
* statement[=].conformance[+] = #SHALL
