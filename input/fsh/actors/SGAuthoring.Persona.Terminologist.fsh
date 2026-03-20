Instance: SGAuthoring.Persona.Terminologist
InstanceOf: ActorDefinition
Usage: #definition
* status = #draft
* experimental = true
* name = "Terminologist"
* title = "Terminologist"
* type = #person
* description = """
A specialist responsible for ensuring semantic interoperability of SMART
Guidelines through proper terminology management. Terminologists manage
the WHO Commons dictionary, concept mappings, and ensure every data element
is mapped to approved standard terminologies.

Key activities:
- Map data elements to WHO Commons dictionary concepts
- Create and maintain CodeSystem resources
- Create and maintain ValueSet resources
- Create ConceptMap resources for cross-terminology mappings
- Map to ICD-11, SNOMED CT, LOINC, IPS, and WHO FIC
- Onboard new concepts into the Commons dictionary
- Verify no duplicate or overlapping concept definitions
- Review terminology bindings in logical models and profiles
- Flag unapproved concepts as QA issues before publication

**Source**: IG Starter Kit, Governance Concepts page;
L3 authoring pages for CodeSystems, ValueSets, ConceptMaps
"""
