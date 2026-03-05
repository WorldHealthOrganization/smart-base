Instance: DAK.Persona.System.ClientRegistry
InstanceOf: ActorDefinition
Usage: #definition
* status = #draft
* experimental = true
* name = "ClientRegistry"
* title = "Client Registry / Master Patient Index"
* type = #system
* description = """
A digital system that creates, maintains, and provides authoritative unique
identifiers for individuals (persons) accessing health services, enabling
cross-facility patient matching and de-duplication.

The client registry supports DHIs including:
- Verify a person's unique identity (2.1.1)
- Enrol person(s) for health services/clinical care plan (2.1.2)
- Merge, de-duplicate and curate coded datasets (4.2.2)
- Standards-compliant interoperability to link records across systems (4.4.2)

**Services and Application Types**:
- C6 — Identification registries and directories
- C8 — Master patient index
"""
* documentation = "https://www.who.int/publications/i/item/9789240081949"
