CodeSystem: CoreDataElementType
Title: "Core Data Element Type"
Description: """
CodeSystem for Core Data Element types - defines the type of FHIR resource that a Core Data Element references.
"""

* ^experimental = false
* ^caseSensitive = true
* ^status = #active
* #valueset "ValueSet" "Reference to a FHIR ValueSet resource"
* #codesystem "CodeSystem" "Reference to a FHIR CodeSystem resource"
* #conceptmap "ConceptMap" "Reference to a FHIR ConceptMap resource"
* #logicalmodel "Logical Model" "Reference to a Logical Model adherent to SGLogicalModel"
