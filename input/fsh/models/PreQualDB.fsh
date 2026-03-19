
Logical: 	PreQualDB
Title: 		"WHO Vaccine PreQual DB"
Description:	"""WHO Vaccine PreQual DB.  Logical model for WHO PreQual DB as CSV file available at:
     https://extranet.who.int/prequal/vaccines/prequalified-vaccines
Columns of the CSV are as follows
  1:Date of Prequalification  
  2:Vaccine Type
  3:Commercial Name
  4:Presentation
  5:No. of doses
  6:Manufacturer
  7:Responsible NRA

"""
* dateOfPrequal 1..1 dateTime "Date of Prequalification (DD/MM/YY)"
* vaccineType 1..1 CodeableConcept "Vaccine Type"
* commercialName 1..1 string "Commercial Name"
* presentation 1..1 CodeableConcept "Presentation"
* numDoses 0..1 decimal "Number of doses"
* manufacturer 1..1 CodeableConcept "Manufacturer"
* responsibleNRA 1..1 CodeableConcept "Responsible NRA"



Logical: 	PreQualDBwithIds
Parent:		PreQualDB
Title:		"WHO Vaccine PreQual DB with IDs"
Description:    """Logical model for WHO PreQual DB as CSV file available at:
     https://extranet.who.int/prequal/vaccines/prequalified-vaccines
Columns of the CSV are as follows
with additional data fields for appropriately referencing associated data objects
"""
* index 1..1 Identifier "An index or identifier of the prequalificaiton for the product."
* index obeys is-a-prequal-product-id
* manufacturerReference 1..1 Reference(IHE.mCSD.Organization)  "Manufacturer referecne"
* responsibleNRAReference 1..1 Reference(IHE.mCSD.Organization)  "Responsible NRA reference"
* productReference 0..1 Reference  "Product reference (when available from pcmt dependency)"




Invariant: is-a-prequal-product-id
Description: "Product ID comes from the PreQual Databatase"
Expression: "system = 'http://smart.who.int/pcmt-vaxprequal/CodeSystem/PreQualProductIds'"
Severity: #error
