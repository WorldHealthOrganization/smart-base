Logical:       Persona
Title:	       "Persona (DAK)"
Description:   "Logical Model for representing Generic Personas from a DAK. Depiction of the human and system actors."

* ^status = #active
* title 1..1 string "Title" "Title of the persona"
* id 1..1 SGid "Persona ID" "An identifier for the persona"
* description 1..1 string "Description" "Description of the persona"
* otherNames 0..* string "Other Names/Examples" "Other names or examples for the persona"
* iscoCode 0..* code "ISCO Code" "ISCO-08 codes for the persona"
* iscoCode from ISCO08ValueSet (extensible)
