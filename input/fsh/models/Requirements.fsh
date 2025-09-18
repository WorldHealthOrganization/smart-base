Logical: Requirements
Title: "Functional and Non-Functional Requirements (DAK)"
Description: "Logical Model for representing Functional and Non-Functional Requirements from a DAK. A high-level list of core functions and capabilities that the system must have to meet the end users' needs."

* ^status = #active
* functional 0..* Reference(FunctionalRequirement) "Functional Requirements" "Functional requirements for the system that reference https://worldhealthorganization.github.io/smart-base/branches/fix-152/StructureDefinition-FunctionalRequirement.html"
* nonfunctional 0..* Reference(NonFunctionalRequirement) "Non-Functional Requirements" "Non-functional requirements for the system that reference https://worldhealthorganization.github.io/smart-base/branches/fix-152/StructureDefinition-NonFunctionalRequirement.html"