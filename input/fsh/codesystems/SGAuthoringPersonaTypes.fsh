CodeSystem: SGAuthoringPersonaTypes
Title:        "SMART Guidelines Authoring Persona Types"
Description:  """
CodeSystem for SMART Guidelines authoring persona types.
These represent roles involved in the authoring, review, and publication
of SMART Guidelines and Digital Adaptation Kits, as distinct from
the clinical/health personas defined within a DAK.
"""

* ^experimental = true
* ^caseSensitive = false
* ^status = #active
* #programme-manager "Programme Manager" "Manages DAK development scope, timeline, resources, and stakeholder engagement"
* #technical-officer "Technical Officer" "Coordinates DAK development work and performs first-pass content review"
* #clinical-sme "Clinical Subject Matter Expert" "Validates clinical accuracy of DAK content against L1 guidelines"
* #business-analyst "Business Analyst" "Authors L2 DAK components including business processes, data dictionaries, and requirements"
* #fhir-modeller "FHIR Modeller" "Authors L3 FHIR artifacts from L2 DAK specifications"
* #terminologist "Terminologist" "Manages terminology bindings, concept mappings, and WHO Commons dictionary alignment"
* #qc-reviewer "Quality Control Reviewer" "Reviews publication readiness using checklists and QA validation reports"
* #publication-manager "Publication Manager" "Manages IG configuration, build process, versioning, and release publication"
* #content-reviewer "Content Reviewer / Approver" "Reviews and formally approves content at decision gates in the authoring lifecycle"
* #translator "Translator" "Translates IG content across UN languages"
