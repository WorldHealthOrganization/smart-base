Instance: SGAuthoring.Skills.TranslateContent
InstanceOf: SGRequirements
Usage: #definition
* status = #draft
* experimental = true
* name = "SkillTranslateContent"
* title = "Can translate content"
* description = "Capability to translate IG content across UN languages."
* actor[+] = Canonical(SGAuthoring.Persona.Translator)

* statement[+].key = "TRANS-01"
* statement[=].label = "Translate narrative pages"
* statement[=].requirement = "Can translate IG narrative page content (markdown/HTML) to target UN languages."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "TRANS-02"
* statement[=].label = "Translate resource metadata"
* statement[=].requirement = "Can translate FHIR resource display names, titles, and descriptions."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "TRANS-03"
* statement[=].label = "Manage translation files"
* statement[=].requirement = "Can manage .pot/.po translation template files and the translation extraction/registration workflow."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "TRANS-04"
* statement[=].label = "Coordinate domain terminology"
* statement[=].requirement = "Can coordinate with clinical SMEs for domain-specific terminology in translations."
* statement[=].conformance[+] = #SHOULD


Instance: SGAuthoring.Skills.ReviewTranslations
InstanceOf: SGRequirements
Usage: #definition
* status = #draft
* experimental = true
* name = "SkillReviewTranslations"
* title = "Can review translations"
* description = "Capability to review translated content for accuracy and completeness."
* actor[+] = Canonical(SGAuthoring.Persona.Translator)

* statement[+].key = "TRANSREV-01"
* statement[=].label = "Review translation accuracy"
* statement[=].requirement = "Can review translated content for linguistic accuracy and clinical correctness."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "TRANSREV-02"
* statement[=].label = "Verify translation completeness"
* statement[=].requirement = "Can verify that all translatable content has been translated for each target language."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "TRANSREV-03"
* statement[=].label = "Verify example resource translations"
* statement[=].requirement = "Can verify that example resources exist for each non-abstract profile in each UN language."
* statement[=].conformance[+] = #SHALL
