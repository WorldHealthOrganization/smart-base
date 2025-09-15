Logical: DAKLogicalModel
Id: DAKLogicalModel
Title: "DAK (Digital Adaptation Kit) Logical Model"
Description: "Logical model defining the structure and metadata for Digital Adaptation Kits (DAKs). A DAK contains the digital representation of WHO SMART guidelines including business processes, decision logic, content, and technical assets."

* ^url = "http://smart.who.int/base/StructureDefinition/DAKLogicalModel"
* ^version = "0.2.0"
* ^status = #draft
* ^experimental = false
* ^publisher = "WHO"
* ^contact.name = "WHO"
* ^contact.telecom.system = #url
* ^contact.telecom.value = "http://who.int"
* ^jurisdiction = urn:iso:std:iso:3166#001 "World"

// Core DAK Identity
* id 1..1 string "DAK Identifier" "Unique identifier for the DAK (e.g., smart.who.int.trust)"
* name 1..1 string "DAK Name" "Human-readable name for the DAK (e.g., Trust)"
* title 1..1 string "DAK Title" "Full title of the DAK (e.g., WHO SMART Trust)"
* description 1..1 string "DAK Description" "Description of the DAK's purpose and scope (e.g., SMART Trust Implementation Guide)"
* version 1..1 string "DAK Version" "Version of the DAK following semantic versioning"
* status 1..1 code "DAK Status" "Publication status of the DAK"
* status from http://hl7.org/fhir/ValueSet/publication-status (required)

// Publication Information  
* publicationUrl 1..1 url "Publication URL" "Canonical URL where the DAK is published (e.g., http://smart.who.int/trust)"
* license 1..1 code "License" "License under which the DAK is published"
* license from http://hl7.org/fhir/ValueSet/spdx-license (required)
* copyrightYear 0..1 string "Copyright Year" "Year or year range for copyright (e.g., 2023+)"

// Publisher Information
* publisher 1..1 BackboneElement "Publisher" "Organization responsible for publishing the DAK"
  * name 1..1 string "Publisher Name" "Name of the publishing organization (e.g., WHO)"
  * url 0..1 url "Publisher URL" "URL of the publishing organization (e.g., http://who.int)"
  * email 0..1 string "Publisher Email" "Contact email for the publisher"

// DAK Content Classification
* experimental 0..1 boolean "Experimental" "Whether this DAK is experimental"
* useContext 0..* UsageContext "Use Context" "Context where this DAK is intended to be used"
* jurisdiction 0..* CodeableConcept "Jurisdiction" "Jurisdictions where this DAK applies"

// Technical Dependencies
* fhirVersion 1..1 code "FHIR Version" "Version of FHIR this DAK is built on"
* fhirVersion from http://hl7.org/fhir/ValueSet/FHIR-version (required)
* dependencies 0..* BackboneElement "Dependencies" "Other IGs or packages this DAK depends on"
  * id 1..1 string "Dependency ID" "Package ID of the dependency"
  * version 1..1 string "Dependency Version" "Version of the dependency"
  * reason 0..1 string "Dependency Reason" "Reason for this dependency"

// DAK-Specific Features
* generateDmnQuestionnaires 0..1 boolean "Generate DMN Questionnaires" "Whether to generate questionnaires from DMN decision tables"
* transformDmnFiles 0..1 boolean "Transform DMN Files" "Whether to transform DMN files to HTML"
* generateValuesetSchemas 0..1 boolean "Generate ValueSet Schemas" "Whether to generate JSON schemas for ValueSets"
* generateLogicalModelSchemas 0..1 boolean "Generate Logical Model Schemas" "Whether to generate JSON schemas for logical models"
* generateDakApiHub 0..1 boolean "Generate DAK API Hub" "Whether to generate API documentation hub"
* generateJsonldVocabularies 0..1 boolean "Generate JSON-LD Vocabularies" "Whether to generate JSON-LD vocabularies from ValueSet expansions"

// Content Organization
* pages 0..* BackboneElement "Pages" "Custom pages included in the DAK"
  * filename 1..1 string "Page Filename" "Filename of the page"
  * title 1..1 string "Page Title" "Title of the page"
  
* menu 0..* BackboneElement "Menu Structure" "Navigation menu structure for the DAK"
  * title 1..1 string "Menu Title" "Title of the menu item"
  * url 1..1 string "Menu URL" "URL of the menu item"
  * subItems 0..* BackboneElement "Sub Menu Items" "Sub-menu items"
    * title 1..1 string "Sub-item Title" "Title of the sub-menu item"
    * url 1..1 string "Sub-item URL" "URL of the sub-menu item"

// Metadata
* releaseLabel 0..1 string "Release Label" "Label for this release (e.g., ci-build, draft, ballot)"
* date 0..1 dateTime "Publication Date" "Date this DAK was published"
* contact 0..* ContactDetail "Contact Information" "Contact details for this DAK"