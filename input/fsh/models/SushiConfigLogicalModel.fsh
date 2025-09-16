Logical: SushiConfigLogicalModel
Id: SushiConfigLogicalModel
Title: "SUSHI Configuration Logical Model"
Description: "Logical model defining the structure of sushi-config.yaml files used for FHIR Implementation Guide configuration. This model captures the essential metadata and configuration parameters needed for IG publishing."

* ^url = "http://smart.who.int/base/StructureDefinition/SushiConfigLogicalModel"
* ^version = "0.2.0"
* ^status = #draft
* ^experimental = false
* ^publisher = "WHO"
* ^contact.name = "WHO"
* ^contact.telecom.system = #url
* ^contact.telecom.value = "http://who.int"
* ^jurisdiction = urn:iso:std:iso:3166#001 "World"

// Core IG Identity (should align with DAK metadata)
* id 1..1 string "IG Identifier" "Unique identifier for the IG, should match DAK id (e.g., smart.who.int.trust)"
* canonical 1..1 url "Canonical URL" "Canonical URL for the IG, should match DAK publicationUrl (e.g., http://smart.who.int/trust)"
* name 1..1 string "IG Name" "Short name for the IG, should derive from DAK name (e.g., Trust)"
* title 1..1 string "IG Title" "Full title of the IG, should match DAK title (e.g., WHO SMART Trust)"
* description 1..1 string "IG Description" "Description of the IG, should match DAK description"
* version 1..1 string "IG Version" "Version of the IG, should match DAK version"
* status 1..1 code "IG Status" "Publication status of the IG"
* status from http://hl7.org/fhir/ValueSet/publication-status (required)

// Publication Information (should align with DAK)
* license 1..1 code "License" "License under which the IG is published, should match DAK license"
* license from http://hl7.org/fhir/ValueSet/spdx-license (required)
* copyrightYear 0..1 string "Copyright Year" "Year or year range for copyright, should match DAK"
* experimental 0..1 boolean "Experimental" "Whether this IG is experimental, should match DAK"
* releaseLabel 0..1 string "Release Label" "Label for this release (e.g., ci-build, draft, ballot)"

// Publisher Information (should align with DAK)
* publisher 1..1 BackboneElement "Publisher" "Organization responsible for publishing the IG"
  * name 1..1 string "Publisher Name" "Name of the publishing organization, should match DAK publisher name"
  * url 0..1 url "Publisher URL" "URL of the publishing organization, should match DAK publisher URL"
  * email 0..1 string "Publisher Email" "Contact email for the publisher"

// Technical Configuration
* fhirVersion 1..1 code "FHIR Version" "Version of FHIR this IG is built on"
* fhirVersion from http://hl7.org/fhir/ValueSet/FHIR-version (required)

// Dependencies
* dependencies 0..* BackboneElement "Dependencies" "Other IGs or packages this IG depends on"
  * id 1..1 string "Dependency Package ID" "Package ID of the dependency"
  * version 1..1 string "Dependency Version" "Version of the dependency"
  * reason 0..1 string "Dependency Reason" "Reason for this dependency"

// Content Structure
* pages 0..* BackboneElement "Pages" "Custom pages included in the IG"
  * filename 1..1 string "Page Filename" "Filename of the page (e.g., index.md)"
  * title 1..1 string "Page Title" "Title of the page"

* menu 0..* BackboneElement "Menu Structure" "Navigation menu structure for the IG"
  * title 1..1 string "Menu Title" "Title of the menu item"
  * url 1..1 string "Menu URL" "URL of the menu item"
  * subItems 0..* BackboneElement "Sub Menu Items" "Sub-menu items"
    * title 1..1 string "Sub-item Title" "Title of the sub-menu item"
    * url 1..1 string "Sub-item URL" "URL of the sub-menu item"

// Resource Management
* resources 0..* BackboneElement "Resource Definitions" "Explicit resource definitions for the IG"
  * reference 1..1 string "Resource Reference" "Reference to the resource (used as YAML key)"
  * name 0..1 string "Resource Name" "Human-readable name for the resource"
  * description 0..1 string "Resource Description" "Description of the resource"
  * exampleBoolean 0..1 boolean "Is Example" "Whether this resource is an example"
  * exampleCanonical 0..1 canonical "Example Canonical" "Canonical URL this resource is an example of"
  * groupingId 0..1 string "Grouping ID" "ID of the group this resource belongs to"

* groups 0..* BackboneElement "Resource Groups" "Logical groupings of resources in the IG"
  * id 1..1 string "Group ID" "Identifier for the group"
  * name 1..1 string "Group Name" "Human-readable name for the group"
  * description 1..1 string "Group Description" "Description of the group"
  * resources 0..* string "Group Resources" "List of resources in this group"

// Global Profiles
* global 0..* BackboneElement "Global Profiles" "Global profile assignments"
  * type 1..1 string "Resource Type" "FHIR resource type"
  * profile 1..1 canonical "Profile URL" "URL of the profile to apply globally"

// Metadata
* meta 0..1 BackboneElement "IG Metadata" "Additional metadata for the IG"
  * profile 0..* canonical "Meta Profiles" "Profiles this IG conforms to"

* contact 0..* ContactDetail "Contact Information" "Contact details for this IG"
* useContext 0..* UsageContext "Use Context" "Context where this IG is intended to be used"
* jurisdiction 0..* CodeableConcept "Jurisdiction" "Jurisdictions where this IG applies"

// SUSHI-specific Configuration
* FSHOnly 0..1 boolean "FSH Only" "Whether to export only FSH resources without IG content"
* applyExtensionMetadataToRoot 0..1 boolean "Apply Extension Metadata" "Whether to apply extension metadata to root elements"

* instanceOptions 0..1 BackboneElement "Instance Options" "Configuration for instance processing"
  * setMetaProfile 0..1 code "Set Meta Profile" "When to automatically set meta.profile"
  * setId 0..1 code "Set ID" "When to automatically set id"