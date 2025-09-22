#!/usr/bin/env python3
"""
Test script to understand current JSON-LD generation behavior
"""

import json
import sys
import os

# Add the scripts directory to the path so we can import the module
sys.path.insert(0, 'input/scripts')

from generate_jsonld_vocabularies import generate_jsonld_vocabulary

def create_sample_valueset():
    """Create a sample ValueSet resource to test with"""
    return {
        "resourceType": "ValueSet",
        "id": "KeyUsage", 
        "url": "https://worldhealthorganization.github.io/smart-trust/ValueSet/KeyUsage",
        "name": "KeyUsage",
        "title": "Key Usage",
        "description": "Allowed values for key usage.",
        "version": "1.0.0",
        "publisher": "World Health Organization",
        "date": "2023-01-01",
        "expansion": {
            "timestamp": "2023-01-01T00:00:00Z",
            "contains": [
                {
                    "code": "digitalSignature",
                    "display": "Digital Signature",
                    "system": "http://example.org/fhir/CodeSystem/KeyUsage"
                },
                {
                    "code": "keyEncipherment", 
                    "display": "Key Encipherment",
                    "system": "http://example.org/fhir/CodeSystem/KeyUsage"
                }
            ]
        }
    }

def test_current_behavior():
    """Test the current JSON-LD generation behavior"""
    
    # Create sample data
    valueset = create_sample_valueset()
    codes = [
        {
            "code": "digitalSignature",
            "display": "Digital Signature", 
            "system": "http://example.org/fhir/CodeSystem/KeyUsage"
        },
        {
            "code": "keyEncipherment",
            "display": "Key Encipherment",
            "system": "http://example.org/fhir/CodeSystem/KeyUsage"
        }
    ]
    
    # Generate JSON-LD vocabulary using current implementation
    jsonld_vocab = generate_jsonld_vocabulary(valueset, codes)
    
    # Print the output
    print("=== CURRENT JSON-LD OUTPUT ===")
    print(json.dumps(jsonld_vocab, indent=2))
    
    # Analyze the issues
    print("\n=== ANALYSIS ===")
    
    context = jsonld_vocab.get("@context", {})
    vocab = context.get("@vocab", "")
    print(f"Current @vocab: {vocab}")
    print(f"Expected @vocab should be: https://worldhealthorganization.github.io/smart-trust/ValueSet-KeyUsage.jsonld")
    
    graph = jsonld_vocab.get("@graph", [])
    if graph:
        first_object = graph[0]
        print(f"First object id: {first_object.get('id', 'NO ID')}")
        print(f"First object type: {first_object.get('type', 'NO TYPE')}")
        
        print("\nCode objects:")
        for obj in graph[1:]:
            if obj.get('fhir:code'):
                print(f"  Code: {obj.get('fhir:code')}, ID: {obj.get('id')}, Type: {obj.get('type')}")

if __name__ == "__main__":
    test_current_behavior()