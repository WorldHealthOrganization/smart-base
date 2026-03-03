Logical: FHIRSchemaBase
Title: "FHIR Schema Base (SMART Guidelines)"
Description: "Base logical model providing the common schema metadata interface inherited by all SMART Guidelines logical models. Every SMART Guidelines logical model schema derives from this base, which documents the shared FHIR and JSON-LD metadata properties used by the JSON Schema generation pipeline."

* ^status = #active
* ^publisher = "World Health Organization (WHO)"
* resourceType 0..1 string "Resource Type" "The FHIR resource type identifying this logical model resource"
* resourceDefinition 0..1 uri "Resource Definition" "Canonical URI of the FHIR StructureDefinition that defines this logical model"
* fhirParent 0..1 string "FHIR Parent" "The FHIR parent base type from which this logical model is derived (serialised as 'fhir:parent' in JSON)"
* jsonldContext 0..1 string "JSON-LD Context" "JSON-LD context for this logical model (serialised as 'jsonld:context' in JSON)"

Mapping: FHIRSchemaBaseToJsonSchemaPropertyNames
Id: json-schema-property-names
Source: FHIRSchemaBase
Target: "https://json-schema.org"
Title: "JSON Schema Property Names"
Description: "Maps FHIR logical model element names to their JSON Schema property names. FHIR element names cannot contain colons, so elements such as fhirParent use FHIR-conformant identifiers in the logical model that differ from their JSON property names (e.g. fhir:parent, jsonld:context)."
* fhirParent -> "fhir:parent"
* jsonldContext -> "jsonld:context"
