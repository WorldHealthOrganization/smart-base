# JSON-LD Type Usage in FHIR ValueSet Vocabularies

## Overview

The JSON-LD vocabularies generated for FHIR ValueSets use [RDF](https://www.w3.org/TR/rdf11-concepts/) types to establish semantic relationships between concepts. This document explains how the `type` property is used in the generated [JSON-LD](https://www.w3.org/TR/json-ld11/) and how [FHIR](http://hl7.org/fhir/R4/) properties are properly declared.

All examples in this document use actual working ValueSets from the smart-base repository that can be accessed at their generated JSON-LD URLs.

## FHIR Property Declarations

All FHIR-specific properties used in the JSON-LD vocabularies are properly declared in the `@context` section following [JSON-LD 1.1 specification](https://www.w3.org/TR/json-ld11/#the-context) requirements:

```json
{
  "@context": {
    "@version": 1.1,
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "schema": "https://schema.org/",
    "fhir": "http://hl7.org/fhir/",
    "prov": "http://www.w3.org/ns/prov#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "fhir:code": "http://hl7.org/fhir/code",
    "fhir:system": "http://hl7.org/fhir/system",
    "fhir:valueSet": "http://hl7.org/fhir/valueSet",
    "generatedAt": {
      "@id": "prov:generatedAtTime",
      "@type": "xsd:dateTime"
    },
    "Enumeration": "schema:Enumeration",
    "Property": "rdf:Property",
    "Entity": "prov:Entity"
  }
}
```

The context defines concise terms for common types to reduce verbosity while maintaining semantic meaning through context expansion. All terms are properly declared with their full namespace IRIs, eliminating the need for `@vocab`.

### FHIR Property Definitions

- **`fhir:code`**: Maps to `http://hl7.org/fhir/code` - represents the actual code value from the [FHIR CodeSystem](http://hl7.org/fhir/R4/codesystem.html)
- **`fhir:system`**: Maps to `http://hl7.org/fhir/system` - represents the IRI (Internationalized Resource Identifier) of the [FHIR CodeSystem](http://hl7.org/fhir/R4/codesystem.html) that defines the code
- **`fhir:valueSet`**: Maps to `http://hl7.org/fhir/valueSet` - links back to the original [FHIR ValueSet](http://hl7.org/fhir/R4/valueset.html) canonical IRI

### Provenance Properties

- **`generatedAt`**: Maps to `prov:generatedAtTime` with type `xsd:dateTime` - timestamps when the vocabulary was generated following [W3C PROV](https://www.w3.org/TR/prov-o/) standards
- **Document type**: `prov:Entity` indicates the JSON-LD document is a provenance-tracked entity

These declarations ensure that the JSON-LD is valid according to [JSON-LD specification](https://www.w3.org/TR/json-ld11/) and can be properly processed by [RDF tools](https://www.w3.org/TR/rdf11-concepts/) and [semantic web frameworks](https://www.w3.org/2001/sw/wiki/Tools).

## Understanding IRIs in JSON-LD

**IRI (Internationalized Resource Identifier)** is the standard way to identify resources in RDF and JSON-LD. All `id` fields in our JSON-LD vocabularies use IRIs to provide globally unique identifiers. Learn more about IRIs in the [RFC 3987 specification](https://tools.ietf.org/html/rfc3987).

## JSON-LD Named Graphs

The JSON-LD vocabularies use [named graphs](https://www.w3.org/TR/json-ld11/#named-graphs) to organize vocabulary content. Each vocabulary document is structured as a named graph with:

- **Document IRI**: The JSON-LD file IRI serves as the named graph identifier
- **Document type**: `prov:Entity` to indicate it's a provenance-tracked entity
- **Generation timestamp**: `generatedAt` property with ISO 8601 timestamp
- **Content graph**: The `@graph` array contains all vocabulary definitions

```json
{
  "@context": { /* context definitions */ },
  "@id": "https://worldhealthorganization.github.io/smart-base/ValueSet-DecisionTableActions.jsonld",
  "@type": "prov:Entity",
  "generatedAt": "2023-12-07T10:30:00Z",
  "@graph": [
    /* vocabulary content */
  ]
}
```

This structure follows [W3C Provenance Ontology (PROV)](https://www.w3.org/TR/prov-o/) standards for tracking generation metadata.

## Type Hierarchy

### 1. Enumeration Class Type

The main ValueSet enumeration uses [`schema:Enumeration`](https://schema.org/Enumeration) as its type:

```json
{
  "id": "https://worldhealthorganization.github.io/smart-base/ValueSet-DecisionTableActions.jsonld",
  "type": "Enumeration",
  "name": "Smart Guidelines Decision Table Actions Enumeration",
  "comment": "Value Set for Smart Guidelines Documentation Decision Table Actions"
}
```

This uses the concise term `Enumeration` defined in the active context, which maps to `schema:Enumeration`. This indicates that the ValueSet defines a controlled vocabulary enumeration compatible with [Schema.org](https://schema.org/).

### 2. Code Instance Types

Individual codes within the ValueSet use the enumeration class IRI as their type, following [RDF/RDFS semantics](https://www.w3.org/TR/rdf-schema/) for class membership:

```json
{
  "id": "http://smart.who.int/base/CodeSystem/DecisionTableActions#output",
  "type": "https://worldhealthorganization.github.io/smart-base/ValueSet-DecisionTableActions.jsonld",
  "name": "Output",
  "fhir:code": "output"
}
```

This establishes that:
- The code is an **instance** of the specific ValueSet enumeration
- The code belongs to the controlled vocabulary defined by that ValueSet
- [RDF processors](https://www.w3.org/TR/rdf11-concepts/) can understand the membership relationship

### 3. Property Type

The property definition uses [`rdf:Property`](http://www.w3.org/1999/02/22-rdf-syntax-ns#Property) as its type:

```json
{
  "id": "http://smart.who.int/base/vocab#decisiontableactions",
  "type": "Property",
  "name": "decisiontableactions",
  "schema:rangeIncludes": {
    "id": "https://worldhealthorganization.github.io/smart-base/ValueSet-DecisionTableActions.jsonld"
  }
}
```

This uses the concise term `Property` defined in the active context, which maps to `rdf:Property`. This creates an [RDF property](https://www.w3.org/TR/rdf-schema/#ch_property) that can be used in data to reference values from the enumeration, with [`schema:rangeIncludes`](https://schema.org/rangeIncludes) specifying the allowed value types.

### Property Definition Purpose

The rdf:Property definition serves as a semantic bridge between applications and ValueSet enumerations:

**Purpose:**
- **Semantic typing**: Enables applications to understand that the term is a property
- **Range constraint**: Specifies that values must come from the specific enumeration
- **Validation support**: Tools can validate that property values are valid enumeration members
- **Documentation**: Provides human-readable description of the property's purpose
- **RDF integration**: Enables SPARQL queries and semantic reasoning over the vocabulary

**Benefits:**
- **Type safety**: Applications can validate property assignments at runtime
- **IDE support**: Code completion and type checking in JSON-LD aware editors
- **Documentation generation**: Automatic API documentation from vocabulary definitions
- **Interoperability**: Standard RDF property semantics enable cross-system integration

## JSON-LD Verbosity Optimization

The vocabularies use concise terms defined in the `@context` to reduce verbosity while maintaining full semantic meaning:

### Before (verbose):
```json
{
  "type": "schema:Enumeration",
  "@type": "prov:Entity"
}
```

### After (concise):
```json
{
  "type": "Enumeration",
  "@type": "Entity"
}
```

This follows [JSON-LD best practices](https://www.w3.org/TR/json-ld11/#dfn-term) for [active context](https://www.w3.org/TR/json-ld11/#dfn-active-context) usage, reducing file size and improving readability while preserving full RDF semantics through context expansion.

## Benefits of This Type System

1. **Semantic Clarity**: Clear distinction between the enumeration definition and its instances following [RDF/RDFS semantics](https://www.w3.org/TR/rdf-schema/)
2. **RDF Compatibility**: Standard [RDF/RDFS semantics](https://www.w3.org/TR/rdf-schema/) for classes and instances
3. **Tool Integration**: [JSON-LD processors](https://www.w3.org/TR/json-ld11-api/) can automatically understand the relationships
4. **Schema.org Compatibility**: Uses standard [Schema.org enumeration patterns](https://schema.org/Enumeration)
5. **FHIR Integration**: Maintains references to original [FHIR resources](http://hl7.org/fhir/R4/) via `fhir:valueSet`

## Usage in Applications

Applications consuming these JSON-LD vocabularies can:

- Query for all instances of a specific enumeration using [SPARQL](https://www.w3.org/TR/sparql11-query/)
- Validate that data uses only allowed enumeration values using [JSON Schema](https://json-schema.org/) or [SHACL](https://www.w3.org/TR/shacl/)
- Automatically generate UI components based on enumeration definitions
- Integrate with [semantic web frameworks](https://www.w3.org/2001/sw/wiki/Tools) and [knowledge graphs](https://www.w3.org/2001/sw/wiki/Knowledge_Graph)

## Example SPARQL Query

```sparql
PREFIX base: <https://worldhealthorganization.github.io/smart-base/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX fhir: <http://hl7.org/fhir/>

# Find all codes in the DecisionTableActions enumeration
SELECT ?code ?display WHERE {
  ?codeInstance a base:ValueSet-DecisionTableActions.jsonld ;
                rdfs:label ?display ;
                fhir:code ?code .
}
```

This query leverages the type relationships to find all codes belonging to a specific ValueSet enumeration, following [SPARQL 1.1 query syntax](https://www.w3.org/TR/sparql11-query/).

## Working with Actual Smart-Base ValueSets

You can access the actual generated JSON-LD vocabularies for smart-base ValueSets at URLs following this pattern:

- **DecisionTableActions**: `https://worldhealthorganization.github.io/smart-base/ValueSet-DecisionTableActions.jsonld`
- **CDSCv1**: `https://worldhealthorganization.github.io/smart-base/ValueSet-CDSCv1.jsonld` 
- **ISCO08ValueSet**: `https://worldhealthorganization.github.io/smart-base/ValueSet-ISCO08ValueSet.jsonld`

During development, preview versions are available at:
`https://worldhealthorganization.github.io/smart-base/branches/{branch-name}/ValueSet-{ValueSetId}.jsonld`

## Standards Compliance

This implementation follows these established standards:

- [JSON-LD 1.1 Specification](https://www.w3.org/TR/json-ld11/) - Core JSON-LD syntax and semantics
- [JSON-LD 1.1 Named Graphs](https://www.w3.org/TR/json-ld11/#named-graphs) - Named graph structure and organization
- [RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/) - RDF data model
- [RDF Schema 1.1](https://www.w3.org/TR/rdf-schema/) - RDF vocabulary description language
- [FHIR R4 Specification](http://hl7.org/fhir/R4/) - Healthcare data exchange standard
- [Schema.org Vocabulary](https://schema.org/) - Structured data vocabulary
- [SPARQL 1.1 Query Language](https://www.w3.org/TR/sparql11-query/) - RDF query language
- [W3C Provenance Ontology (PROV)](https://www.w3.org/TR/prov-o/) - Provenance vocabulary and data model
- [XML Schema Part 2: Datatypes](https://www.w3.org/TR/xmlschema-2/) - Data type definitions

## Related Specifications

- [SHACL (Shapes Constraint Language)](https://www.w3.org/TR/shacl/) - RDF data validation
- [JSON Schema](https://json-schema.org/) - JSON data validation
- [Dublin Core Metadata Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) - Metadata vocabulary
- [SKOS (Simple Knowledge Organization System)](https://www.w3.org/TR/skos-reference/) - Knowledge organization vocabularies
- [W3C Provenance Ontology (PROV)](https://www.w3.org/TR/prov-o/) - Provenance vocabulary and data model
- [XML Schema Part 2: Datatypes](https://www.w3.org/TR/xmlschema-2/) - Data type definitions