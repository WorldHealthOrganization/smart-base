Logical: Requirements
Title: "Functional and Non-Functional Requirements (DAK)"
Description: "Logical Model for representing Functional and Non-Functional Requirements from a DAK. A high-level list of core functions and capabilities that the system must have to meet the end users' needs."

* ^status = #active
* ^publisher = "World Health Organization (WHO)"
* description[x] 0..1 string or uri "Description" "Description of the requirements - either Markdown content or a URI to a Markdown file (absolute or relative to repository root)"
* functional 0..* BackboneElement "Functional Requirements" "Functional requirements for the system - can be provided as canonical reference or inline instance data"
  * canonical 0..1 canonical "Canonical" "Canonical URI pointing to the FunctionalRequirement definition"
  * canonical ^type[0].targetProfile = "http://smart.who.int/base/StructureDefinition/FunctionalRequirement"
  * instance 0..1 FunctionalRequirement "Instance" "Inline FunctionalRequirement instance data"
* nonfunctional 0..* BackboneElement "Non-Functional Requirements" "Non-functional requirements for the system - can be provided as canonical reference or inline instance data"
  * canonical 0..1 canonical "Canonical" "Canonical URI pointing to the NonFunctionalRequirement definition"
  * canonical ^type[0].targetProfile = "http://smart.who.int/base/StructureDefinition/NonFunctionalRequirement"
  * instance 0..1 NonFunctionalRequirement "Instance" "Inline NonFunctionalRequirement instance data"