Logical: FHIRSchemaBase
Title: "FHIR Schema Base (SMART Guidelines)"
Description: "Base logical model providing the common schema metadata interface inherited by all SMART Guidelines logical models. Every SMART Guidelines logical model schema derives from this base, which documents the shared FHIR and JSON-LD metadata properties used by the JSON Schema generation pipeline."

* ^status = #active
* ^publisher = "World Health Organization (WHO)"
* resourceType 0..1 string "Resource Type" "The FHIR resource type identifying this logical model resource"
* resourceDefinition 0..1 uri "Resource Definition" "Canonical URI of the FHIR StructureDefinition that defines this logical model"
* fhirParent 0..1 string "FHIR Parent" "The FHIR parent base type from which this logical model is derived (serialised as 'fhir:parent' in JSON)"
* fhirParent ^extension[+].url = "http://smart.who.int/base/StructureDefinition/JsonSchemaName"
* fhirParent ^extension[=].valueString = "fhir:parent"
* fhirParent.extension contains $JsonSchemaName named jsonSchemaName 0..1 MS
* jsonldValuesets 0..* uri "JSON-LD Value Sets" "ValueSet identifiers used in this logical model for JSON-LD context generation (serialised as 'jsonld:valuesets' in JSON)"
* jsonldValuesets ^extension[+].url = "http://smart.who.int/base/StructureDefinition/JsonSchemaName"
* jsonldValuesets ^extension[=].valueString = "jsonld:valuesets"
* jsonldValuesets.extension contains $JsonSchemaName named jsonSchemaName 0..1 MS
* jsonldContextTemplate 0..1 string "JSON-LD Context Template" "JSON-LD context template for this logical model (serialised as 'jsonld:contextTemplate' in JSON)"
* jsonldContextTemplate ^extension[+].url = "http://smart.who.int/base/StructureDefinition/JsonSchemaName"
* jsonldContextTemplate ^extension[=].valueString = "jsonld:contextTemplate"
* jsonldContextTemplate.extension contains $JsonSchemaName named jsonSchemaName 0..1 MS
