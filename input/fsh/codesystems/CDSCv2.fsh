CodeSystem: CDSCv2
Title: "Classification of Digital Health Services and Application Types v2"
Description: """
CodeSystem for the Classification of Digital Health Services and Application Types v2,
as defined in the Classification of Digital Interventions, Services and Applications in Health
(CDISAH), second edition (2023). ISBN 978-92-4-008194-9.

Services and Application Types represent the types of software, ICT systems and services
or communication channels that deliver or execute digital health interventions (DHIs) and
health content.

The types are organised into five representations within the Digital Health Architecture:
  A. Point of service
  B. Health system/Provider administration
  C. Registries and Directories
  D. Data Management services
  E. Surveillance and Response
"""
* ^experimental = true
* ^caseSensitive = false
* ^status = #active
* ^url = "http://smart.who.int/base/CodeSystem/CDSCv2"
* ^version = "2.0.0"
* ^publisher = "World Health Organization (WHO)"
* ^copyright = "WHO © 2023. Some rights reserved. CC BY-NC-SA 3.0 IGO."

// ─── A. Point of service ──────────────────────────────────────────────────────
* #A    "Point of service"
  "Systems that facilitate the provision and delivery of healthcare services to persons at the point of care."
* #A1   "Communication systems"
  "Systems that are used to transfer electronic information. Messages can be exchanged between healthcare providers or between healthcare providers and persons."
* #A2   "Community-based information systems"
  "Applications that facilitate data collection and use at the community level, utilised by community-based workers who provide health promotion and disease prevention activities."
* #A3   "Decision support systems"
  "Computer based tools which combine medical information databases and algorithms with patient specific data, intended to provide healthcare professionals and/or users with recommendations for diagnosis, prognosis, monitoring and treatment."
* #A4   "Diagnostics information systems"
  "Systems for diagnostic applications found in devices (software in a medical device), wearables that collect health data, radiology information systems, medical imaging systems, and picture archiving and communication systems (PACS)."
* #A5   "Electronic medical record systems"
  "A secure, online system that holds information about people's health and clinical care, managed by healthcare providers. Also known as electronic health record (EHR)."
* #A6   "Laboratory information systems"
  "Systems that support the process from patient sample to patient result, including lab requests/test ordering, sample tracking and processing, and results reporting."
* #A7   "Personal health records"
  "A digital personal health record is a record of an individual's health information in a structured digital format, over which the person has agency."
* #A8   "Pharmacy information systems"
  "Systems that manage prescriptions, dispensing, stock and billing for medicines and health products."
* #A9   "Telehealth systems"
  "Systems that enable remote clinical consultation, monitoring and diagnosis between persons and healthcare providers at a distance."

// ─── B. Health system/Provider administration ─────────────────────────────────
* #B    "Health system/Provider administration"
  "Systems that support the administrative and managerial functions of health systems and healthcare organisations."
* #B1   "Blood bank information management systems"
  "Systems for managing the collection, testing, processing, storage, and distribution of blood and blood products."
* #B2   "Health finance-related information systems"
  "Systems that manage health financing, insurance enrolment, claims, billing, reimbursement, and budgeting."
* #B3   "Health program monitoring systems"
  "Systems used to collect and analyse aggregate health data for programme planning, monitoring and evaluation."
* #B4   "Human resource information systems"
  "Systems for managing health workforce data including cadres, deployment, credentials, performance and payroll."
* #B5   "Learning and training systems"
  "Systems for delivering, tracking, and assessing training and professional development of health workers."
* #B6   "Logistics management information systems (LMIS)"
  "Systems for managing the health supply chain from forecasting to distribution and stock monitoring."
* #B7   "Patient Administration systems"
  "Systems that manage patient administrative information including admissions, discharges, transfers, appointments and billing."
* #B8   "Research information systems"
  "Systems that support the design, conduct, data management and reporting of health research and clinical trials."

// ─── C. Registries and Directories ────────────────────────────────────────────
* #C    "Registries and Directories"
  "Systems that create, maintain, and provide authoritative master records for persons, providers, facilities, products and health events."
* #C1   "Census and population information systems"
  "Systems that collect, store, and manage population-level demographic data including census information."
* #C2   "Civil registration and vital statistics (CRVS) systems"
  "Systems that register and certify vital events such as births, deaths, marriages and their underlying causes."
* #C3   "Facility management information systems"
  "Systems for managing health facility information, infrastructure, equipment, capacity and assessments."
* #C4   "(Health) Facility registries"
  "Master lists of health facilities with unique identifiers, locations, services offered, and operational information."
* #C5   "Health worker registry"
  "Systems maintaining authoritative directories of health workforce cadres, credentials, and deployment information."
* #C6   "Identification registries and directories"
  "Systems that create, maintain, and verify unique identities for persons, healthcare providers, and other health actors."
* #C7   "Immunization information systems"
  "Systems for recording, tracking, and reporting individual and population-level immunization history and coverage."
* #C8   "Master patient index"
  "Systems that uniquely identify and link patient records across multiple health information systems and facilities."
* #C9   "Product catalogues"
  "Systems that maintain authoritative lists of approved health commodities, medicines, devices and equipment."
* #C10  "Public Key directories"
  "Systems that manage and distribute public cryptographic keys to support digital signature and identity verification."
* #C11  "Terminology and classification systems"
  "Systems for managing and applying standardised clinical terminologies, ontologies, and health classifications."

// ─── D. Data Management services ─────────────────────────────────────────────
* #D    "Data Management services"
  "Services and systems that support the collection, aggregation, storage, analysis, and exchange of health data."
* #D1   "Analytics Systems"
  "Systems that process and analyse health data to produce insights, dashboards, reports and predictive models."
* #D2   "Data interchange and interoperability"
  "Systems and standards that enable health data exchange between disparate systems, including APIs, messaging standards, and interoperability platforms."
* #D3   "Data warehouses"
  "Systems that consolidate and store large volumes of historical health data from multiple sources for analysis and reporting."
* #D4   "Environmental monitoring systems"
  "Systems that monitor environmental determinants of health such as air quality, water safety and vector habitats."
* #D5   "Geographic information systems (GIS)"
  "Systems that capture, analyse and visualise geospatial health data for mapping health events, facilities, and populations."
* #D6   "Health Management Information systems (HMIS)"
  "Systems for aggregate health data reporting, target-setting, and programme monitoring, typically at district and national levels."
* #D7   "Knowledge management systems"
  "Systems for curating, organising and disseminating clinical guidelines, protocols, and health knowledge resources."
* #D8   "Shared Health Record and Health Information Repository"
  "Systems that aggregate and share longitudinal health records across facilities and providers."

// ─── E. Surveillance and Response ────────────────────────────────────────────
* #E    "Surveillance and Response"
  "Systems that support the detection, monitoring, and response to disease outbreaks and public health threats."
* #E1   "Emergency preparedness and response systems"
  "Systems that coordinate emergency medical services, disaster preparedness, and mass casualty management."
* #E2   "Public health and disease surveillance systems"
  "Systems for detecting, monitoring, investigating and responding to disease outbreaks and public health threats."