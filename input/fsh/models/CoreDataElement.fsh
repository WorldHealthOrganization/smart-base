Logical: CoreDataElement
Parent: SGLogicalModel
Title: "Core Data Element (DAK)"
Description: "Logical Model for representing Core Data Elements from a DAK. A core data element can be one of: a ValueSet, a CodeSystem, a ConceptMap, or a Logical Model adherent to SGLogicalModel. This is the ONE EXCEPTION to allowing FHIR R4 models into the DAK LMs."

* ^status = #active
* ^publisher = "World Health Organization (WHO)"

// Type of core data element (exactly one must be specified)
* type 1..1 code "Type" "Type of core data element: valueset, codesystem, conceptmap, or logicalmodel"
* type from CoreDataElementTypeVS (required)

// Source reference (URL, canonical, or relative path)
* source 1..1 uri "Source" "URL (absolute or relative) or canonical/IRI pointing to the ValueSet, CodeSystem, ConceptMap, or Logical Model definition"

// Optional metadata
* id 0..1 id "Element ID" "Identifier for the core data element"
* description 0..1 markdown "Description" "Description of the core data element"