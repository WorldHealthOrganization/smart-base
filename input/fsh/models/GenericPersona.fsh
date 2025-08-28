Logical: GenericPersona
Title: "Generic Persona (DAK)"
Description: "Logical Model for representing Generic Personas from a DAK. Depiction of the human and system actors. Human actors are end users, supervisors and related stakeholders who would be interacting with the digital system or involved in the clinical care, public health or health system pathway."

* ^status = #active
* title 1..1 string "Title" "Title of the persona"
* id 1..1 id "Persona ID" "Identifier for the persona"
* description 1..1 string "Description" "Description of the persona"
* otherNames 0..* string "Other Names/Examples" "Other names or examples for the persona"
* iscoCode 0..* code "ISCO Code" "ISCO-08 codes for occupation classification"
  * from ISCO08ValueSet (extensible)