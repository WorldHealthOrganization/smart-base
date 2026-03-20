Instance: SGAuthoring.Persona.PublicationManager
InstanceOf: ActorDefinition
Usage: #definition
* status = #draft
* experimental = true
* name = "PublicationManager"
* title = "Publication Manager"
* type = #person
* description = """
A specialist responsible for managing the FHIR Implementation Guide
configuration, build process, versioning, and release publication workflow.
Publication Managers ensure IGs are correctly configured, built, and
published to smart.who.int following the established publication process.

Key activities:
- Set up IG repositories from smart-ig-empty template
- Configure sushi-config.yaml (canonical URL, package ID, dependencies)
- Enable GitHub Pages and CI build workflows
- Run FHIR IG Publisher builds and verify output
- Manage semantic versioning (major.minor.patch)
- Create publication-request.json for releases
- Create release branches, tags, and GitHub releases
- Monitor automated publication workflows
- Coordinate with WHO SMART Guidelines team for smart.who.int updates
- Manage cross-IG governance for shared artifacts
- Reset main branch to draft status after publication

**Source**: IG Starter Kit, IG Setup, IG Publication, and IG Configuration pages
"""
