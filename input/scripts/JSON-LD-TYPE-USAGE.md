# JSON-LD Type Usage in FHIR ValueSet Vocabularies

## Overview

The JSON-LD vocabularies generated for FHIR ValueSets use [RDF](https://www.w3.org/TR/rdf11-concepts/) types to establish semantic relationships between concepts. This document explains how the `type` property is used in the generated [JSON-LD](https://www.w3.org/TR/json-ld11/) and how [FHIR](http://hl7.org/fhir/R4/) properties are properly declared.

## FHIR Property Declarations

All FHIR-specific properties used in the JSON-LD vocabularies are properly declared in the `@context` section following [JSON-LD 1.1 specification](https://www.w3.org/TR/json-ld11/#the-context) requirements:

```json
{
  "@context": {
    "@vocab": "https://worldhealthorganization.github.io/smart-trust/ValueSet-KeyUsage.jsonld",
    "fhir": "http://hl7.org/fhir/",
    "fhir:code": "http://hl7.org/fhir/code",
    "fhir:system": "http://hl7.org/fhir/system",
    "fhir:valueSet": "http://hl7.org/fhir/valueSet"
  }
}
```

### FHIR Property Definitions

- **`fhir:code`**: Maps to `http://hl7.org/fhir/code` - represents the actual code value from the [FHIR CodeSystem](http://hl7.org/fhir/R4/codesystem.html)
- **`fhir:system`**: Maps to `http://hl7.org/fhir/system` - represents the URI of the [FHIR CodeSystem](http://hl7.org/fhir/R4/codesystem.html) that defines the code
- **`fhir:valueSet`**: Maps to `http://hl7.org/fhir/valueSet` - links back to the original [FHIR ValueSet](http://hl7.org/fhir/R4/valueset.html) canonical URL

These declarations ensure that the JSON-LD is valid according to [JSON-LD specification](https://www.w3.org/TR/json-ld11/) and can be properly processed by [RDF tools](https://www.w3.org/TR/rdf11-concepts/) and [semantic web frameworks](https://www.w3.org/2001/sw/wiki/Tools).

## Type Hierarchy

### 1. Enumeration Class Type

The main ValueSet enumeration uses [`schema:Enumeration`](https://schema.org/Enumeration) as its type:

```json
{
  "id": "https://worldhealthorganization.github.io/smart-trust/ValueSet-KeyUsage.jsonld",
  "type": "schema:Enumeration",
  "name": "Key Usage Enumeration",
  "comment": "Allowed values for key usage."
}
```

This indicates that the ValueSet defines a controlled vocabulary enumeration compatible with [Schema.org](https://schema.org/).

### 2. Code Instance Types

Individual codes within the ValueSet use the enumeration class URL as their type, following [RDF/RDFS semantics](https://www.w3.org/TR/rdf-schema/) for class membership:

```json
{
  "id": "http://example.org/fhir/CodeSystem/KeyUsage#digitalSignature",
  "type": "https://worldhealthorganization.github.io/smart-trust/ValueSet-KeyUsage.jsonld",
  "name": "Digital Signature",
  "fhir:code": "digitalSignature"
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
  "id": "https://worldhealthorganization.github.io/smart-trust/vocab#keyusage",
  "type": "rdf:Property",
  "name": "keyusage",
  "schema:rangeIncludes": {
    "id": "https://worldhealthorganization.github.io/smart-trust/ValueSet-KeyUsage.jsonld"
  }
}
```

This creates an [RDF property](https://www.w3.org/TR/rdf-schema/#ch_property) that can be used in data to reference values from the enumeration, with [`schema:rangeIncludes`](https://schema.org/rangeIncludes) specifying the allowed value types.

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
PREFIX ex: <https://worldhealthorganization.github.io/smart-trust/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX fhir: <http://hl7.org/fhir/>

# Find all codes in the KeyUsage enumeration
SELECT ?code ?display WHERE {
  ?codeInstance a ex:ValueSet-KeyUsage.jsonld ;
                rdfs:label ?display ;
                fhir:code ?code .
}
```

This query leverages the type relationships to find all codes belonging to a specific ValueSet enumeration, following [SPARQL 1.1 query syntax](https://www.w3.org/TR/sparql11-query/).

## Standards Compliance

This implementation follows these established standards:

- [JSON-LD 1.1 Specification](https://www.w3.org/TR/json-ld11/) - Core JSON-LD syntax and semantics
- [RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/) - RDF data model
- [RDF Schema 1.1](https://www.w3.org/TR/rdf-schema/) - RDF vocabulary description language
- [FHIR R4 Specification](http://hl7.org/fhir/R4/) - Healthcare data exchange standard
- [Schema.org Vocabulary](https://schema.org/) - Structured data vocabulary
- [SPARQL 1.1 Query Language](https://www.w3.org/TR/sparql11-query/) - RDF query language

## Related Specifications

- [SHACL (Shapes Constraint Language)](https://www.w3.org/TR/shacl/) - RDF data validation
- [JSON Schema](https://json-schema.org/) - JSON data validation
- [Dublin Core Metadata Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) - Metadata vocabulary
- [SKOS (Simple Knowledge Organization System)](https://www.w3.org/TR/skos-reference/) - Knowledge organization vocabularies