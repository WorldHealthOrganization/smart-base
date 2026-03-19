
Logical: 	FinishedVaccineProducts
Title: 		"WHO Vaccine PreQual DB - Finished Vaccine Products"
Characteristics: #can-be-target
Description:	"""WHO Vaccine PreQual DB - Finished Vaccine Products.
Logical model for the WHO PreQual DB as provided by the backend API at:
     https://extranet.who.int/prequal/vaccines/prequalified-vaccines
This model provides authoritative vaccine product IDs and a richer data structure compared to the CSV export.
Sub-objects with Identification.Id are modeled as separate logical models and linked via references.

Key fields from the API (FinishedVaccineProducts):
  ProductDetails.Identification.Id - Vaccine Product ID (authoritative)
  ProductDetails.Identification.Name - Product reference name (e.g. FVP-P-447)
  ProductDetails.Type - Product type code (e.g. Finished Vaccine Product)
  ProductDetails.DateOfPreQualifiedAcceptance - Date of prequalification
  ProductDetails.AssessmentProcedure - Assessment procedure code
  ProductDetails.ApplicantOrganization - Manufacturer/applicant with ID, name, address
  ProductDetails.Presentation - Presentation form (Vial, Ampoule, etc.)
  ProductDetails.PharmaceuticalForm - Pharmaceutical form details
  ProductDetails.DosageDetails.NoOfDosagesPerPrimaryContainer - Number of doses
  ProductDetails.NRADetails - Responsible NRA with ID, name, address
  ProductDetails.VaccineDetails - Vaccine type with full, abbreviated, and commercial names
  ProductDetails.StorageDetails - Storage temperature and shelf life
  ProductDetails.Status - Prequalification status code
"""
* ^extension[http://hl7.org/fhir/tools/StructureDefinition/logical-target].valueBoolean = true
* productId 1..1 Identifier "Vaccine Product ID (authoritative)"
* productName 1..1 string "Product reference name (e.g. FVP-P-447)"
* productType 1..1 code "Product type code from PreQualDatabaseMetadata (e.g. FinishedVaccineProduct)"
* dateOfPrequal 1..1 dateTime "Date of prequalification acceptance"
* assessmentProcedure 0..1 code "Assessment procedure code from PreQualDatabaseMetadata (e.g. PrequalificationStandard)"
* status 1..1 code "Product status code from PreQualDatabaseMetadata (e.g. Prequalified)"
* pharmaceuticalForm 0..1 code "Pharmaceutical form code from PreQualDatabaseMetadata"
* presentation 1..1 CodeableConcept "Presentation (e.g. Vial, Ampoule)"
* numDoses 0..1 decimal "Number of doses per primary container"
* vaccineFullName 0..1 string "Vaccine full name"
* vaccineAbbreviatedName 0..1 string "Vaccine abbreviated name"
* vaccineCommercialName 1..1 string "Vaccine commercial name"
* vaccineTypeId 0..1 Identifier "Vaccine type ID"
* routeOfAdministration 0..1 code "Route of administration code from PreQualDatabaseMetadata"
* vialMonitor 0..1 string "Vial monitor type (e.g. Type 14, Type 30)"
* multidoseVialPolicy 0..1 string "Multidose vial policy text"
* presentationOther 0..1 string "Alternative presentation description when Presentation is 'Other'"
* applicantId 0..1 Identifier "Applicant/manufacturer organization ID (may be absent if not yet assigned)"
* applicantName 1..1 string "Applicant/manufacturer organization name (always present from API data)"
* applicantAddress 0..1 Address "Applicant organization address"
* nraId 0..1 Identifier "NRA organization ID (may be absent if not yet assigned)"
* nraName 1..1 string "Responsible NRA name (always present from API data)"
* nraCountry 0..1 string "NRA country"
* shelfLife 0..1 string "Shelf life (e.g. 24 months)"
* storageTemperature 0..1 string "Storage temperature (e.g. 2 - 8°C)"
* diluent 0..1 string "Diluent information"
* lastPublishingDate 0..1 dateTime "Last publishing date"
* publishingRemarks 0..1 string "Publishing remarks"
* preservative 0..1 string "Preservative name (e.g. Thiomersal)"
* preservativeConcentration 0..1 string "Preservative concentration (e.g. 0.01%)"
* manufacturerLM 0..1 Reference(PreQualManufacturer) "Manufacturer logical model instance reference (linked when ApplicantOrganization.Identification.Id is non-null)"
* nraLM 0..1 Reference(PreQualNRA) "NRA logical model instance reference (linked when NRADetails.Identification.Id is non-null)"
* vaccineLM 0..1 Reference(PreQualVaccine) "Vaccine logical model instance reference (linked when VaccineDetails.Identification.Id is non-null)"
* bulkSupplierLM 0..1 Reference(PreQualBulkSupplier) "Bulk supplier logical model instance reference (linked when BulkSupplier.Id is non-null)"
* packagingLM 0..* Reference(PreQualProductPackaging) "Product packaging logical model instance references"
* documentLM 0..* Reference(PreQualDocumentDetail) "Document detail logical model instance references"
* siteLM 0..* Reference(PreQualSiteDetail) "Site detail logical model instance references"
* ingredientLM 0..* Reference(PreQualProductIngredient) "Product ingredient logical model instance references"
* manufacturerReference 1..1 Reference(IHE.mCSD.Organization) "Manufacturer FHIR Organization reference"
* responsibleNRAReference 1..1 Reference(IHE.mCSD.Organization) "Responsible NRA FHIR Organization reference"
* productReference 0..1 Reference "Product FHIR reference (when available from pcmt dependency)"


Logical:	PreQualManufacturer
Title:		"WHO PreQual Manufacturer"
Characteristics: #can-be-target
Description:	"""Logical model for the manufacturer/applicant organization
from the WHO PreQual API (ProductDetails.ApplicantOrganization).
"""
* ^extension[http://hl7.org/fhir/tools/StructureDefinition/logical-target].valueBoolean = true
* manufacturerId 0..1 Identifier "Manufacturer organization ID"
* name 1..1 string "Organization name"
* addressLine1 0..1 string "Address line 1"
* city 0..1 string "City"
* state 0..1 string "State/Province"
* country 0..1 string "Country"
* postalCode 0..1 string "Postal code"
* isoCountryCode 0..1 string "ISO country code"
* region 0..1 string "WHO region"
* website 0..1 string "Website URL"
* organizationReference 1..1 Reference(IHE.mCSD.Organization) "FHIR Organization reference"


Logical:	PreQualNRA
Title:		"WHO PreQual NRA"
Characteristics: #can-be-target
Description:	"""Logical model for the responsible National Regulatory Authority (NRA)
from the WHO PreQual API (ProductDetails.NRADetails).
"""
* ^extension[http://hl7.org/fhir/tools/StructureDefinition/logical-target].valueBoolean = true
* nraId 0..1 Identifier "NRA organization ID"
* name 1..1 string "Organization name"
* addressLine1 0..1 string "Address line 1"
* country 0..1 string "Country"
* website 0..1 string "Website URL"
* organizationReference 1..1 Reference(IHE.mCSD.Organization) "FHIR Organization reference"


Logical:	PreQualVaccine
Title:		"WHO PreQual Vaccine"
Characteristics: #can-be-target
Description:	"""Logical model for the vaccine type details
from the WHO PreQual API (ProductDetails.VaccineDetails).
Contains only vaccine-type-level fields that are stable across products.
Product-specific fields (CommercialName, RouteOfAdministration) remain on FinishedVaccineProducts.
"""
* ^extension[http://hl7.org/fhir/tools/StructureDefinition/logical-target].valueBoolean = true
* vaccineId 0..1 Identifier "Vaccine type ID"
* fullName 0..1 string "Vaccine full name"
* abbreviatedName 0..1 string "Vaccine abbreviated name"


Logical:	PreQualBulkSupplier
Title:		"WHO PreQual Bulk Supplier"
Characteristics: #can-be-target
Description:	"""Logical model for the bulk supplier organization
from the WHO PreQual API (ProductDetails.BulkSupplier).
"""
* ^extension[http://hl7.org/fhir/tools/StructureDefinition/logical-target].valueBoolean = true
* bulkSupplierId 0..1 Identifier "Bulk supplier organization ID"
* name 0..1 string "Organization name"


Logical:	PreQualProductPackaging
Title:		"WHO PreQual Product Packaging"
Characteristics: #can-be-target
Description:	"""Logical model for product packaging details
from the WHO PreQual API (ProductPackaging).
"""
* ^extension[http://hl7.org/fhir/tools/StructureDefinition/logical-target].valueBoolean = true
* packagingId 1..1 Identifier "Packaging record ID"
* packagingType 0..1 code "Packaging type code from PreQualDatabaseMetadata (e.g. Secondary, Tertiary, ShippingContainer)"
* componentPacked 0..1 code "Component packed code from PreQualDatabaseMetadata (e.g. ActiveVaccine, Diluent)"
* coldChainVolume 0..1 string "Cold chain volume per dose"
* description 0..1 string "Packaging description"
* volume 0..1 string "Packaging volume/dimensions"
* totalDoses 0..1 string "Total doses in packaging"
* totalContainers 0..1 string "Total containers in packaging"
* height 0..1 string "Height"
* length 0..1 string "Length"
* width 0..1 string "Width"
* primaryContainers 0..1 string "Number of primary containers"


Logical:	PreQualDocumentDetail
Title:		"WHO PreQual Document Detail"
Characteristics: #can-be-target
Description:	"""Logical model for document details
from the WHO PreQual API (DocumentDetails).
"""
* ^extension[http://hl7.org/fhir/tools/StructureDefinition/logical-target].valueBoolean = true
* documentId 0..1 Identifier "Document ID"
* documentName 0..1 string "Document name"
* documentType 0..1 code "Document type code from PreQualDatabaseMetadata (e.g. ProductInsert, Photo, VSPAR)"
* versionId 0..1 string "Document version ID"
* fileExtension 0..1 string "File extension (e.g. pdf, jpg)"
* fileType 0..1 string "File type (e.g. PDF, JPEG)"


Logical:	PreQualSiteDetail
Title:		"WHO PreQual Site Detail"
Characteristics: #can-be-target
Description:	"""Logical model for manufacturing site details
from the WHO PreQual API (SiteDetails).
"""
* ^extension[http://hl7.org/fhir/tools/StructureDefinition/logical-target].valueBoolean = true
* siteOrganizationId 0..1 Identifier "Site organization ID"
* siteOrganizationName 0..1 string "Site organization name"
* addressLine1 0..1 string "Address line 1"
* city 0..1 string "City"
* state 0..1 string "State/Province"
* country 0..1 string "Country"
* postalCode 0..1 string "Postal code"
* siteStatus 0..1 code "Site status code from PreQualDatabaseMetadata (e.g. Accepted)"
* siteActivity 0..1 code "Site activity code from PreQualDatabaseMetadata (e.g. FVPManufacture)"


Logical:	PreQualProductIngredient
Title:		"WHO PreQual Product Ingredient"
Characteristics: #can-be-target
Description:	"""Logical model for product ingredient details
from the WHO PreQual API (ProductIngredients).
"""
* ^extension[http://hl7.org/fhir/tools/StructureDefinition/logical-target].valueBoolean = true
* ingredientId 0..1 Identifier "Ingredient ID"
* ingredientType 0..1 code "Ingredient type code from PreQualDatabaseMetadata (e.g. VxFVP)"
* unit 0..1 string "Measurement unit"
* product 0..1 string "Product reference ID"
* productComponentType 0..1 code "Product component type code from PreQualDatabaseMetadata (e.g. Diluent)"
* function 0..1 string "Ingredient function"
