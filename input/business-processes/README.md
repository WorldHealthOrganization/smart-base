# Business Processes

This directory contains business process definitions in BPMN 2.0 format.

Business processes represent Level 2 (L2) Digital Adaptation Kit (DAK) components that are data model agnostic. These processes define the workflow and procedures that guide healthcare delivery and system operations.

## File Format

Business processes are stored as `.bpmn` files following the [OMG BPMN 2.0 specification](https://www.omg.org/spec/BPMN/2.0/).

## Integration with FHIR

These L2 business processes are transformed into L3 FHIR resources following the enterprise architecture defined at http://smart.who.int/ra, typically as:
- FHIR ActivityDefinition resources
- FHIR PlanDefinition resources

## Actors and Personas

Actors and personas referenced in these business processes are defined as concepts in the DAK CodeSystem and have corresponding ValueSets in `input/fsh/valuesets/DAK.actors.fsh`.