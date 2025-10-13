Logical: CoreDataElement
Parent: SGLogicalModel
Title: "Core Data Element (DAK)"
Description: "Logical Model for representing Core Data Elements from a DAK. A core data element can be one of: a ValueSet, a CodeSystem, a ConceptMap, or a Logical Model adherent to SGLogicalModel. This is the ONE EXCEPTION to allowing FHIR R4 models into the DAK LMs."

* ^status = #active
* ^publisher = "World Health Organization (WHO)"

// Type of core data element (exactly one must be specified)
* type 1..1 code "Type" "Type of core data element: valueset, codesystem, conceptmap, or logicalmodel"
* type from CoreDataElementTypeVS (required)

// Canonical reference (URI)
* canonical 1..1 uri "Canonical" "Canonical URI/IRI pointing to the ValueSet, CodeSystem, ConceptMap, or Logical Model definition"

// Optional metadata
* id 0..1 id "Element ID" "Identifier for the core data element"
* description[x] 0..1 string or uri "Description" "Description of the core data element - either Markdown content or a URI to a Markdown file (absolute or relative to repository root)"