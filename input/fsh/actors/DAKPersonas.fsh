// ============================================================================
// DAK Candidate User Personas
// Derived from the Classification of Digital Interventions, Services and
// Applications in Health (CDISAH), second edition (2023).
// ISBN 978-92-4-008194-9
//
// The CDISAH organises DHIs around four primary user groups:
//   1. Persons         — members of the public who are potential or current
//                        users of health services, including caregivers
//   2. Healthcare providers — members of the health workforce who deliver
//                        health interventions
//   3. Health management and support personnel — involved in the administration
//                        and oversight of health systems
//   4. Data services   — crosscutting functionality to support data
//                        management, use, and data governance compliance
//
// Human personas correspond to groups 1–3.
// System personas correspond to the digital services and application types
// (from the Services and Application Types classification, groups A–E).
// ============================================================================

// ─── Human Personas ──────────────────────────────────────────────────────────

Instance: DAK.Persona.Person
InstanceOf: ActorDefinition
Usage: #definition
* status = #draft
* experimental = true
* name = "Person"
* title = "Person (Health Service User)"
* type = #person
* description = """
A member of the public who is a potential or current user of health services,
including health prevention and wellness activities. Other terms used for this
group include 'patient', 'client', 'individual', and 'health service user'.
Caregivers of individuals receiving health services are also included.

In the CDISAH v2, this group was previously called 'Client(s)' in v1 and has
been renamed to 'Person(s)' or 'Individual(s)' to maintain neutral and inclusive
terminology.

Persons interact with DHIs to:
- Receive targeted (1.1) and untargeted (1.2) health communications
- Communicate with other persons as peers (1.3)
- Track their own health data and records (1.4)
- Report health events and system feedback (1.5)
- Access health information on demand including via chatbot/AI (1.6)
- Manage their financial transactions related to health services (1.7)
- Manage their consent for health data access and sharing (1.8)

**ISCO-08**: Not applicable (non-occupational role).

**Examples**: Patient, pregnant woman, caregiver, child, community member,
health scheme beneficiary, person living with a chronic condition.
"""
* documentation = "https://www.who.int/publications/i/item/9789240081949"

Instance: DAK.Persona.HealthcareProvider
InstanceOf: ActorDefinition
Usage: #definition
* status = #draft
* experimental = true
* name = "HealthcareProvider"
* title = "Healthcare Provider"
* type = #person
* description = """
A member of the health workforce who delivers health interventions. This group
has also been described as 'health workers' or 'healthcare workers'.

Healthcare providers use DHIs to:
- Identify and register persons for health services (2.1)
- Manage person-centred health records (2.2)
- Receive clinical decision support prompts and checklists (2.3)
- Conduct telemedicine consultations and remote monitoring (2.4)
- Communicate with supervisors, peers, and receive AI-assisted content (2.5)
- Coordinate referrals and emergency transport (2.6)
- Schedule and plan their clinical activities (2.7)
- Access training content and assessments (2.8)
- Manage prescriptions and medication adherence (2.9)
- Order and receive laboratory and diagnostic results (2.10)
- Verify health coverage and receive payments from individuals (2.11)

**ISCO-08**: 2211 (Generalist medical practitioners), 2212 (Specialist medical
practitioners), 2221 (Nursing professionals), 2222 (Midwifery professionals),
3211 (Medical imaging and therapeutic equipment technicians), 3212 (Medical
and pathology laboratory technicians), 3213 (Pharmaceutical technicians and
assistants), 3221 (Nursing associate professionals), 3222 (Midwifery associate
professionals), 3255 (Community health workers).

**Examples**: Physician, nurse, midwife, clinical officer, pharmacist,
laboratory technician, dentist, allied health professional.
"""
* documentation = "https://www.who.int/publications/i/item/9789240081949"

Instance: DAK.Persona.CommunityHealthWorker
InstanceOf: ActorDefinition
Usage: #definition
* status = #draft
* experimental = true
* name = "CommunityHealthWorker"
* title = "Community Health Worker"
* type = #person
* description = """
A frontline member of the health workforce who delivers health interventions
at the community level, acting as a link between communities and formal health
facilities. Community health workers are a key sub-group of healthcare providers.

Community health workers use DHIs to:
- Register and follow-up community members (2.1, 2.2.1)
- Receive community-based decision support and job aids (2.3)
- Report public health events from point of diagnosis (3.3.1)
- Access mobile training and competency assessments (2.8)
- Communicate with supervising clinical staff (2.5.1)
- Manage their daily visit planning and activities (2.7)

**ISCO-08**: 3255 (Community health workers), 5321 (Health care assistants).

**Examples**: Village health worker, health extension worker, community health
volunteer, lay health advisor, peer educator, traditional birth attendant,
community case manager.
"""
* documentation = "https://www.who.int/publications/i/item/9789240081949"

Instance: DAK.Persona.HealthSystemManager
InstanceOf: ActorDefinition
Usage: #definition
* status = #draft
* experimental = true
* name = "HealthSystemManager"
* title = "Health System Manager"
* type = #person
* description = """
A professional involved in the administration and oversight of health systems.
This group corresponds to 'Health management and support personnel' in CDISAH v2,
previously called 'Health system managers' in v1.

Health system managers use DHIs to:
- Manage health workforce information, performance, and certification (3.1)
- Oversee supply chain, inventory, cold chain, and procurement (3.2)
- Receive notifications of public health events (3.3)
- Register and certify vital events — births and deaths (3.4)
- Administer health coverage schemes, billing, payroll, and budgets (3.5)
- Monitor and track health equipment and assets (3.6)
- Manage health facility information and conduct assessments (3.7)
- Manage person-centred health certificate information (3.8)

**ISCO-08**: 1342 (Health services managers), 2446 (Social work professionals
n.e.c.), 3354 (Government social benefits officials), 4311 (Accounting and
bookkeeping clerks).

**Examples**: District health officer, programme manager, supply chain officer,
HMIS coordinator, hospital administrator, vital registration officer,
health insurance administrator.
"""
* documentation = "https://www.who.int/publications/i/item/9789240081949"

Instance: DAK.Persona.DataManager
InstanceOf: ActorDefinition
Usage: #definition
* status = #draft
* experimental = true
* name = "DataManager"
* title = "Health Data Manager and Analyst"
* type = #person
* description = """
A professional who manages, analyses, and disseminates health data to support
evidence-based decision-making. This corresponds to the 'Data services' user
group in CDISAH v2, providing crosscutting functionality across the health system.

Data managers use DHIs to:
- Create data collection forms and manage data acquisition (4.1.1)
- Store and aggregate health data (4.1.2)
- Synthesise and visualise data for reporting and dashboards (4.1.3)
- Apply automated analytics and predictive modelling including AI/ML (4.1.4)
- Parse, de-duplicate, and curate coded datasets and terminologies (4.2)
- Classify disease codes and causes of mortality (4.2.3)
- Map geographic locations of facilities, events, populations, and providers (4.3)
- Enable point-to-point data integration and standards-compliant interoperability (4.4)
- Maintain data governance including authentication, privacy, and consent (4.5)

**ISCO-08**: 2120 (Mathematicians, actuaries and statisticians), 2521 (Database
designers and administrators), 2523 (Computer network professionals), 3120
(Computer network and systems technicians).

**Examples**: Biostatistician, epidemiologist, health informatician, data analyst,
DHIS2 administrator, GIS specialist, interoperability engineer, terminology manager.
"""
* documentation = "https://www.who.int/publications/i/item/9789240081949"

// ─── System Personas ──────────────────────────────────────────────────────────

Instance: DAK.Persona.System.EMR
InstanceOf: ActorDefinition
Usage: #definition
* status = #draft
* experimental = true
* name = "ElectronicMedicalRecord"
* title = "Electronic Medical Record (EMR) System"
* type = #system
* description = """
A secure, digital system that holds information about people's health and
clinical care managed by healthcare providers. Also referred to as an
Electronic Health Record (EHR).

The EMR system supports DHIs including:
- Longitudinal tracking of person's health status and services (2.2.1)
- Management of structured clinical records (2.2.2)
- Management of unstructured clinical records such as notes and images (2.2.3)
- Clinical decision support prompts and checklists (2.3)
- Person identification and registration (2.1)
- Prescription and medication management (2.9)
- Laboratory results reception (2.10.1)
- Routine health indicator data collection (2.2.4)

**Services and Application Type**: A5 — Electronic medical record systems

**Functional areas**: Clinical decision support, record management,
person registration, appointment scheduling, referral tracking.
"""
* documentation = "https://www.who.int/publications/i/item/9789240081949"

Instance: DAK.Persona.System.HMIS
InstanceOf: ActorDefinition
Usage: #definition
* status = #draft
* experimental = true
* name = "HealthManagementInformationSystem"
* title = "Health Management Information System (HMIS)"
* type = #system
* description = """
A digital system used to collect, process, report, and use aggregate health data
for programme planning, monitoring, and evaluation at district and national levels.

The HMIS supports DHIs including:
- Routine health indicator data collection and management (2.2.4)
- Non-routine data collection and management (4.1.1)
- Data storage and aggregation (4.1.2)
- Data synthesis and visualisations (4.1.3)
- Data exchange across systems (4.4)

**Services and Application Type**: D6 — Health Management Information Systems (HMIS)

**Functional areas**: Data collection, reporting dashboards, target monitoring,
programme performance tracking, data quality management.
"""
* documentation = "https://www.who.int/publications/i/item/9789240081949"

Instance: DAK.Persona.System.ClientRegistry
InstanceOf: ActorDefinition
Usage: #definition
* status = #draft
* experimental = true
* name = "ClientRegistry"
* title = "Client Registry / Master Patient Index"
* type = #system
* description = """
A digital system that creates, maintains, and provides authoritative unique
identifiers for individuals (persons) accessing health services, enabling
cross-facility patient matching and de-duplication.

The client registry supports DHIs including:
- Verify a person's unique identity (2.1.1)
- Enrol person(s) for health services/clinical care plan (2.1.2)
- Merge, de-duplicate and curate coded datasets (4.2.2)
- Standards-compliant interoperability to link records across systems (4.4.2)

**Services and Application Types**:
- C6 — Identification registries and directories
- C8 — Master patient index
"""
* documentation = "https://www.who.int/publications/i/item/9789240081949"

Instance: DAK.Persona.System.LIS
InstanceOf: ActorDefinition
Usage: #definition
* status = #draft
* experimental = true
* name = "LaboratoryInformationSystem"
* title = "Laboratory Information System (LIS)"
* type = #system
* description = """
A digital system that manages the complete lifecycle of laboratory test orders,
specimen tracking, result production, and result reporting to healthcare providers
and persons.

The LIS supports DHIs including:
- Transmit and track diagnostic orders (2.10.2)
- Capture diagnostic results from digital devices (2.10.3)
- Transmit person's diagnostic result to healthcare provider (2.10.1)
- Transmit diagnostics result or availability of result to person(s) (1.1.4)
- Track biological specimens (2.10.4)

**Services and Application Type**: A6 — Laboratory information systems

**Functional areas**: Lab requests/test ordering, sample tracking, sample
processing, results reporting.
"""
* documentation = "https://www.who.int/publications/i/item/9789240081949"

Instance: DAK.Persona.System.InteropPlatform
InstanceOf: ActorDefinition
Usage: #definition
* status = #draft
* experimental = true
* name = "InteroperabilityPlatform"
* title = "Health Information Exchange / Interoperability Platform"
* type = #system
* description = """
A middleware system or shared infrastructure that enables health data exchange
between disparate health information systems using standard protocols and formats.

The interoperability platform supports DHIs including:
- Point-to-point data integration (4.4.1)
- Standards-compliant interoperability (4.4.2)
- Message routing to appropriate architecture components (4.4.3)
- Data storage and aggregation across systems (4.1.2)

**Services and Application Type**: D2 — Data interchange and interoperability

**Functional areas**: Semantic interoperability, technical interoperability,
information exchange, data mediation, enterprise service bus.
"""
* documentation = "https://www.who.int/publications/i/item/9789240081949"

Instance: DAK.Persona.System.LMIS
InstanceOf: ActorDefinition
Usage: #definition
* status = #draft
* experimental = true
* name = "LogisticsManagementInformationSystem"
* title = "Logistics Management Information System (LMIS)"
* type = #system
* description = """
A digital system that manages the health supply chain from quantification
and forecasting through distribution, inventory management, and consumption tracking.

The LMIS supports DHIs including:
- Manage inventory and distribution of health commodities (3.2.1)
- Notify stock levels of health commodities (3.2.2)
- Monitor cold-chain sensitive commodities (3.2.3)
- Register licensed drugs and health commodities (3.2.4)
- Manage procurement of commodities (3.2.5)

**Services and Application Type**: B6 — Logistics management information systems (LMIS)
"""
* documentation = "https://www.who.int/publications/i/item/9789240081949"

Instance: DAK.Persona.System.SurveillanceSystem
InstanceOf: ActorDefinition
Usage: #definition
* status = #draft
* experimental = true
* name = "PublicHealthSurveillanceSystem"
* title = "Public Health and Disease Surveillance System"
* type = #system
* description = """
A digital system for detecting, monitoring, investigating, and responding to
disease outbreaks and public health threats.

The surveillance system supports DHIs including:
- Notification of public health events from point of diagnosis (3.3.1)
- Transmit health event alerts to specific population group(s) (1.1.1)
- Map location of health event (4.3.2)
- Data synthesis and visualizations for outbreak response (4.1.3)
- Automated analysis of data to generate predictions (4.1.4)

**Services and Application Type**: E2 — Public health and disease surveillance systems
"""
* documentation = "https://www.who.int/publications/i/item/9789240081949"
