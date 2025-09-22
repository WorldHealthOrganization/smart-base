# JSON-LD Type Usage in FHIR ValueSet Vocabularies

## Overview

The JSON-LD vocabularies generated for FHIR ValueSets use RDF types to establish semantic relationships between concepts. This document explains how the `type` property is used in the generated JSON-LD.

## Type Hierarchy

### 1. Enumeration Class Type

The main ValueSet enumeration uses `schema:Enumeration` as its type:

```json
{
  "id": "https://worldhealthorganization.github.io/smart-trust/ValueSet-KeyUsage.jsonld",
  "type": "schema:Enumeration",
  "name": "Key Usage Enumeration",
  "comment": "Allowed values for key usage."
}
```

This indicates that the ValueSet defines a controlled vocabulary enumeration compatible with Schema.org.

### 2. Code Instance Types

Individual codes within the ValueSet use the enumeration class URL as their type:

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
- RDF processors can understand the membership relationship

### 3. Property Type

The property definition uses `rdf:Property` as its type:

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

This creates an RDF property that can be used in data to reference values from the enumeration.

## Benefits of This Type System

1. **Semantic Clarity**: Clear distinction between the enumeration definition and its instances
2. **RDF Compatibility**: Standard RDF/RDFS semantics for classes and instances
3. **Tool Integration**: JSON-LD processors can automatically understand the relationships
4. **Schema.org Compatibility**: Uses standard Schema.org enumeration patterns
5. **FHIR Integration**: Maintains references to original FHIR resources via `fhir:valueSet`

## Usage in Applications

Applications consuming these JSON-LD vocabularies can:

- Query for all instances of a specific enumeration using SPARQL
- Validate that data uses only allowed enumeration values
- Automatically generate UI components based on enumeration definitions
- Integrate with semantic web frameworks and knowledge graphs

## Example SPARQL Query

```sparql
PREFIX ex: <https://worldhealthorganization.github.io/smart-trust/>

# Find all codes in the KeyUsage enumeration
SELECT ?code ?display WHERE {
  ?codeInstance a ex:ValueSet-KeyUsage.jsonld ;
                rdfs:label ?display ;
                fhir:code ?code .
}
```

This query leverages the type relationships to find all codes belonging to a specific ValueSet enumeration.