Instance: CDSCv1toCDSCv2
InstanceOf: ConceptMap
Description: """
Mapping from the Classification of Digital Health System Categories v1 (CDSCv1, 2018)
to the Classification of Digital Health Services and Application Types v2 (CDSCv2, 2023).

The v1 used 25 single-letter codes (A–Y). The v2 completely restructured this into
5 representations within the digital health enterprise architecture, each with
alphanumeric codes (A1–A9, B1–B8, C1–C11, D1–D8, E1–E2).

Several new v2 categories have no v1 equivalent:
A3 (Decision support), A4 (Diagnostics), B1 (Blood bank), B3 (Health program monitoring),
B7 (Patient administration), C4 (Facility registries), C5 (Health worker registry),
C7 (Immunisation information), C8 (Master patient index), C9 (Product catalogues),
C10 (Public Key directories), D1 (Analytics), D3 (Data warehouses).
"""
Usage: #definition
* name = "CDSCv1toCDSCv2"
* title = "Mapping from CDSC v1 to Services and Application Types v2"
* status = #draft
* experimental = true
* sourceCanonical = Canonical(CDSCv1)
* targetCanonical = Canonical(CDSCv2)
* group[+]
  * source = Canonical(CDSCv1)
  * target = Canonical(CDSCv2)
  * insert ElementMapComment( A, C1, equivalent,  "v1 'Census; population information & data warehouse' → v2 C1 'Census and population information systems'")
  * insert ElementMapComment( B, C2, equivalent,  "v1 'Civil Registration and Vital Statistics' → v2 C2 [same concept; refined name]")
  * insert ElementMapComment( C, A7, inexact,     "v1 'Client applications' [broad] most closely maps to v2 A7 'Personal health records'; point-of-service apps generally fall under A. group")
  * insert ElementMapComment( D, A1, equivalent,  "v1 'Client communication system' → v2 A1 'Communication systems'")
  * insert ElementMapComment( E, C11, equivalent, "v1 'Clinical terminology and classifications' → v2 C11 'Terminology and classification systems'")
  * insert ElementMapComment( F, A2, equivalent,  "v1 'Community-based Information System' → v2 A2 'Community-based information systems'")
  * insert ElementMapComment( G, D2, equivalent,  "v1 'Data interchange interoperability and accessibility' → v2 D2 'Data interchange and interoperability'")
  * insert ElementMapComment( H, A5, equivalent,  "v1 'Electronic Medical Record' → v2 A5 'Electronic medical record systems'")
  * insert ElementMapComment( I, E1, equivalent,  "v1 'Emergency response system' → v2 E1 'Emergency preparedness and response systems'")
  * insert ElementMapComment( J, D4, equivalent,  "v1 'Environmental monitoring systems' → v2 D4 'Environmental monitoring systems'")
  * insert ElementMapComment( K, C3, equivalent,  "v1 'Facility Management Information System' → v2 C3 'Facility management information systems'")
  * insert ElementMapComment( L, D5, equivalent,  "v1 'Geographic Information Systems' → v2 D5 'Geographic information systems [GIS]'")
  * insert ElementMapComment( M, B2, equivalent,  "v1 'Health finance and insurance system' → v2 B2 'Health finance-related information systems'")
  * insert ElementMapComment( N, D6, equivalent,  "v1 'Health Management Information System' → v2 D6 'Health Management Information systems [HMIS]'")
  * insert ElementMapComment( O, B4, equivalent,  "v1 'Human Resource Information System' → v2 B4 'Human resource information systems'")
  * insert ElementMapComment( P, C6, equivalent,  "v1 'Identification registries and directories' → v2 C6 [same concept]")
  * insert ElementMapComment( Q, D7, equivalent,  "v1 'Knowledge Management' → v2 D7 'Knowledge management systems'")
  * insert ElementMapComment( R, A6, equivalent,  "v1 'Laboratory and Diagnostic System' → v2 A6 'Laboratory information systems'")
  * insert ElementMapComment( S, B5, equivalent,  "v1 'Learning and Training System' → v2 B5 'Learning and training systems'")
  * insert ElementMapComment( T, B6, equivalent,  "v1 'Logistics Management Information System' → v2 B6 'Logistics management information systems [LMIS]'")
  * insert ElementMapComment( U, A8, equivalent,  "v1 'Pharmacy Information System' → v2 A8 'Pharmacy information systems'")
  * insert ElementMapComment( V, E2, equivalent,  "v1 'Public health and disease surveillance' → v2 E2 'Public health and disease surveillance systems'")
  * insert ElementMapComment( W, B8, equivalent,  "v1 'Research information system' → v2 B8 'Research information systems'")
  * insert ElementMapComment( X, D8, equivalent,  "v1 'SHR and health information repositories' → v2 D8 'Shared Health Record and Health Information Repository'")
  * insert ElementMapComment( Y, A9, equivalent,  "v1 'Telemedicine' → v2 A9 'Telehealth systems'")