# Artifacts Summary - SMART Base v0.3.0

* [**Table of Contents**](toc.md)
* **Artifacts Summary**

## Artifacts Summary

This page provides a list of the FHIR artifacts defined as part of this implementation guide.

### Conformance 

constraints and profile structures for SMART Guidelines resources

| | |
| :--- | :--- |
| [SMART Guidelines ActivityDefinition](StructureDefinition-SGActivityDefinition.md) | The minimum expectations for ActivityDefinition resources used in SMART Guidelines |
| [SMART Guidelines Actor](StructureDefinition-SGActor.md) | Structure and constraints for ActorDefinition resources used in SMART Guidelines |
| [SMART Guidelines Business Process](StructureDefinition-SGBusinessProcess.md) | Structure and constraints for Business Processes represented in SMART Guidelines |
| [SMART Guidelines CodeSystem](StructureDefinition-SGCodeSystem.md) | Defines the minimum expectations for CodeSystem resources used in SMART Guidelines |
| [SMART Guidelines ConceptMap](StructureDefinition-SGConceptMap.md) | Defines the minimum expectations for ConceptMap resources used in SMART Guidelines |
| [SMART Guidelines GraphDefinition](StructureDefinition-SGGraphDefinition.md) | The minimum expectations for GraphDefinition resources used in SMART Guidelines |
| [SMART Guidelines Group Definition](StructureDefinition-SGGroupDefinition.md) | Structure and constraints for Group Definitions represented in SMART Guidelines |
| [SMART Guidelines ImplementationGuide](StructureDefinition-SGImplementationGuide.md) | Defines the minimum expectations for ImplementationGuide resources used in SMART Guidelines |
| [SMART Guidelines Library](StructureDefinition-SGLibrary.md) | Defines the minimum expectations for Library resources used in SMART Guidelines |
| [SMART Guidelines Logical Model](StructureDefinition-SGLogicalModel.md) | Defines the minimum expectations for Logical Models used in SMART Guidelines |
| [SMART Guidelines Measure](StructureDefinition-SGMeasure.md) | Defines the minimum expectations for Measure resources used in SMART Guidelines |
| [SMART Guidelines PlanDefinition](StructureDefinition-SGPlanDefinition.md) | Defines the minimum expectations for PlanDefinition resources used in SMART Guidelines |
| [SMART Guidelines Questionnaire](StructureDefinition-SGQuestionnaire.md) | Defines the minimum expectations for Questionnaire resources used in SMART Guidelines |
| [SMART Guidelines StructureDefinition](StructureDefinition-SGStructureDefinition.md) | Defines the minimum expectations for StructureDefinition resources used in SMART Guidelines |
| [SMART Guidelines StructureMap](StructureDefinition-SGStructureMap.md) | Defines the minimum expectations for StructureMap resources used in SMART Guidelines |
| [SMART Guidelines Transaction](StructureDefinition-SGTransaction.md) | Structure and constraints for TransactionDefinition resources used in SMART Guidelines |
| [SMART Guidelines ValueSet](StructureDefinition-SGValueSet.md) | Defines the minimum expectations for ValueSet resources used in SMART Guidelines |

### Requirements: Actor Definitions 

The following artifacts define the types of individuals and/or systems that will interact as part of the use cases covered by this implementation guide.

| | |
| :--- | :--- |
| [Business Analyst](ActorDefinition-SGAuthoring.Persona.BusinessAnalyst.md) | A digital health informatician specializing in business analysis who authors L2 DAK components. Business analysts translate clinical guidelines and normative products into structured DAK artifacts including business processes, data dictionaries, decision-support logic, and requirements.Key activities:* Review L1 source documents and extract structured content
* Author generic personas based on task-shifting guidelines
* Create user scenario narratives
* Design BPMN 2.0 business process diagrams
* Define core data elements and data dictionary
* Develop decision-support logic tables (DMN standard)
* Develop scheduling logic tables
* Define indicators and performance metrics
* Capture functional and non-functional requirements
* Streamline content across DAK components for consistency
**Source**: IG Starter Kit, L2 DAK Authoring, Section 2.1 "Fill in DAK components"; Community of Practice page |
| [Clinical Subject Matter Expert](ActorDefinition-SGAuthoring.Persona.ClinicalSME.md) | A clinician or subject matter expert (SME) of a specific health area who validates the clinical accuracy and completeness of DAK content against WHO guidelines and other normative products. SMEs should be the authors of the source documents or recognized experts actively engaged in, if not leading, the collaborative development of the DAKs.Key activities:* Validate that DAK components accurately reflect L1 recommendations
* Provide clinical ground-truthing through country visits and interviews
* Identify gaps or needed changes in DAK content
* Review decision-support logic for clinical correctness
* Confirm that workflows represent 80% of clinical scenarios
* Validate personas against real-world practice settings
* Advise on cross-programme overlaps (e.g. TB/HIV indicators)
**Source**: IG Starter Kit, L2 DAK Authoring, Sections 1 "Plan" and 2.2 "Validate" |
| [Community Health Worker](ActorDefinition-DAK.Persona.CommunityHealthWorker.md) | A frontline member of the health workforce who delivers health interventions at the community level, acting as a link between communities and formal health facilities. Community health workers are a key sub-group of healthcare providers.Community health workers use DHIs to:* Register and follow-up community members (2.1, 2.2.1)
* Receive community-based decision support and job aids (2.3)
* Report public health events from point of diagnosis (3.3.1)
* Access mobile training and competency assessments (2.8)
* Communicate with supervising clinical staff (2.5.1)
* Manage their daily visit planning and activities (2.7)
**ISCO-08**: 3255 (Community health workers), 5321 (Health care assistants).**Examples**: Village health worker, health extension worker, community health volunteer, lay health advisor, peer educator, traditional birth attendant, community case manager. |
| [Content Reviewer / Approver](ActorDefinition-SGAuthoring.Persona.ContentReviewer.md) | A designated reviewer responsible for approving SMART Guidelines content at key decision gates in the authoring lifecycle. Content Reviewers ensure that DAK and IG content meets quality standards, accurately reflects WHO normative guidance, and is ready to proceed to the next phase.Content Reviewers may be senior technical officers, programme leads, or designated governance committee members. They provide formal sign-off at phase transitions (L2→L3, draft→publication).Key activities:* Review and approve L2 DAK content before L3 authoring begins
* Review and approve L3 IG content before publication
* Assess whether content changes are breaking or non-breaking
* Approve draft publications for stakeholder circulation
* Provide final sign-off for release publication
* Ensure content aligns with WHO guidelines governance policies
* Participate in cross-programme content harmonization reviews
**Source**: IG Starter Kit, Publication page (review process); DAK Authoring, Section 2.2 "Validate DAK content with SMEs" |
| [FHIR Modeller](ActorDefinition-SGAuthoring.Persona.FHIRModeller.md) | An L3 author who creates machine-readable FHIR artifacts from L2 DAK specifications. FHIR Modellers use FSH (FHIR Shorthand), SUSHI, and the IG Publisher toolchain to produce conformant Implementation Guides.Key activities:* Verify L2 input availability and consistency
* Author FHIR Logical Models from L2 data dictionaries
* Create FHIR Profiles (StructureDefinitions)
* Author FHIR Questionnaires from L2 forms
* Write CQL for decision logic, scheduling logic, and indicators
* Create StructureMaps for data extraction
* Author PlanDefinitions for business processes and decision tables
* Create ActorDefinitions from L2 personas (reusing Commons repository)
* Create ExampleScenario resources from L2 user scenarios
* Author FHIR Measure resources from L2 indicators
* Create FHIR Requirements resources
* Develop test cases (TestPlan, TestScript, example instances)
* Ensure all artifacts conform to CRMI Shareable/Publishable profiles
**Source**: IG Starter Kit, L2-L3 Overview and all L3 authoring pages |
| [Health Data Manager and Analyst](ActorDefinition-DAK.Persona.DataManager.md) | A professional who manages, analyses, and disseminates health data to support evidence-based decision-making. This corresponds to the 'Data services' user group in CDISAH v2, providing crosscutting functionality across the health system.Data managers use DHIs to:* Create data collection forms and manage data acquisition (4.1.1)
* Store and aggregate health data (4.1.2)
* Synthesise and visualise data for reporting and dashboards (4.1.3)
* Apply automated analytics and predictive modelling including AI/ML (4.1.4)
* Parse, de-duplicate, and curate coded datasets and terminologies (4.2)
* Classify disease codes and causes of mortality (4.2.3)
* Map geographic locations of facilities, events, populations, and providers (4.3)
* Enable point-to-point data integration and standards-compliant interoperability (4.4)
* Maintain data governance including authentication, privacy, and consent (4.5)
**ISCO-08**: 2120 (Mathematicians, actuaries and statisticians), 2521 (Database designers and administrators), 2523 (Computer network professionals), 3120 (Computer network and systems technicians).**Examples**: Biostatistician, epidemiologist, health informatician, data analyst, DHIS2 administrator, GIS specialist, interoperability engineer, terminology manager. |
| [Health System Manager](ActorDefinition-DAK.Persona.HealthSystemManager.md) | A professional involved in the administration and oversight of health systems.Health system managers use DHIs to:* Manage health workforce information, performance, and certification (3.1)
* Oversee supply chain, inventory, cold chain, and procurement (3.2)
* Receive notifications of public health events (3.3)
* Register and certify vital events — births and deaths (3.4)
* Administer health coverage schemes, billing, payroll, and budgets (3.5)
* Monitor and track health equipment and assets (3.6)
* Manage health facility information and conduct assessments (3.7)
* Manage person-centred health certificate information (3.8)
**ISCO-08**: 1342 (Health services managers), 2446 (Social work professionals n.e.c.), 3354 (Government social benefits officials), 4311 (Accounting and bookkeeping clerks).**Examples**: District health officer, programme manager, supply chain officer, HMIS coordinator, hospital administrator, vital registration officer, health insurance administrator. |
| [Healthcare Provider](ActorDefinition-DAK.Persona.HealthcareProvider.md) | A member of the health workforce who delivers health interventions. This group has also been described as 'health workers' or 'healthcare workers'.Healthcare providers use DHIs to:* Identify and register persons for health services (2.1)
* Manage person-centred health records (2.2)
* Receive clinical decision support prompts and checklists (2.3)
* Conduct telemedicine consultations and remote monitoring (2.4)
* Communicate with supervisors, peers, and receive AI-assisted content (2.5)
* Coordinate referrals and emergency transport (2.6)
* Schedule and plan their clinical activities (2.7)
* Access training content and assessments (2.8)
* Manage prescriptions and medication adherence (2.9)
* Order and receive laboratory and diagnostic results (2.10)
* Verify health coverage and receive payments from individuals (2.11)
**ISCO-08**: 2211 (Generalist medical practitioners), 2212 (Specialist medical practitioners), 2221 (Nursing professionals), 2222 (Midwifery professionals), 3211 (Medical imaging and therapeutic equipment technicians), 3212 (Medical and pathology laboratory technicians), 3213 (Pharmaceutical technicians and assistants), 3221 (Nursing associate professionals), 3222 (Midwifery associate professionals), 3255 (Community health workers).**Examples**: Physician, nurse, midwife, clinical officer, pharmacist, laboratory technician, dentist, allied health professional. |
| [Laboratory Information System (LIS)](ActorDefinition-DAK.Persona.System.LIS.md) | A digital system that manages the complete lifecycle of laboratory test orders, specimen tracking, result production, and result reporting to healthcare providers and persons.The LIS supports DHIs including:* Transmit and track diagnostic orders (2.10.2)
* Capture diagnostic results from digital devices (2.10.3)
* Transmit person's diagnostic result to healthcare provider (2.10.1)
* Transmit diagnostics result or availability of result to person(s) (1.1.4)
* Track biological specimens (2.10.4)
**Services and Application Type**: A6 — Laboratory information systems**Functional areas**: Lab requests/test ordering, sample tracking, sample processing, results reporting. |
| [Person (Health Service User)](ActorDefinition-DAK.Persona.Person.md) | A member of the public who is a potential or current user of health services, including health prevention and wellness activities. Other terms used for this group include 'patient', 'client', 'individual', and 'health service user'. Caregivers of individuals receiving health services are also included.Persons interact with DHIs to:* Receive targeted (1.1) and untargeted (1.2) health communications
* Communicate with other persons as peers (1.3)
* Track their own health data and records (1.4)
* Report health events and system feedback (1.5)
* Access health information on demand including via chatbot/AI (1.6)
* Manage their financial transactions related to health services (1.7)
* Manage their consent for health data access and sharing (1.8)
**ISCO-08**: Not applicable (non-occupational role).**Examples**: Patient, pregnant woman, caregiver, child, community member, health scheme beneficiary, person living with a chronic condition. |
| [Programme Manager](ActorDefinition-SGAuthoring.Persona.ProgrammeManager.md) | A programme manager responsible for the overall coordination and management of the Digital Adaptation Kit (DAK) development process. Programme managers lead scoping, resource allocation, timeline planning, and stakeholder engagement.The DAK development team should be small (<10 people) and nimble. The Programme Manager ensures the team is empowered to self-organize and manage DAK-related work including collaboration with stakeholders, content development, validation, and publication.Key activities:* Define DAK scope and purpose
* Form and coordinate the DAK development team
* Establish development process and governance
* Define RASCI matrix for roles and responsibilities
* Plan sprint iterations and maintain the DAK backlog
* Coordinate SME consultations (workshops, country visits)
* Draft project roadmap with milestone dates
* Assess and secure resources and budget
**Source**: IG Starter Kit, L2 DAK Authoring, Section 1 "Plan" |
| [Public Health and Disease Surveillance System](ActorDefinition-DAK.Persona.System.SurveillanceSystem.md) | A digital system for detecting, monitoring, investigating, and responding to disease outbreaks and public health threats.The surveillance system supports DHIs including:* Notification of public health events from point of diagnosis (3.3.1)
* Transmit health event alerts to specific population group(s) (1.1.1)
* Map location of health event (4.3.2)
* Data synthesis and visualizations for outbreak response (4.1.3)
* Automated analysis of data to generate predictions (4.1.4)
**Services and Application Type**: E2 — Public health and disease surveillance systems |
| [Publication Manager](ActorDefinition-SGAuthoring.Persona.PublicationManager.md) | A specialist responsible for managing the FHIR Implementation Guide configuration, build process, versioning, and release publication workflow. Publication Managers ensure IGs are correctly configured, built, and published to smart.who.int following the established publication process.Key activities:* Set up IG repositories from smart-ig-empty template
* Configure sushi-config.yaml (canonical URL, package ID, dependencies)
* Enable GitHub Pages and CI build workflows
* Run FHIR IG Publisher builds and verify output
* Manage semantic versioning (major.minor.patch)
* Create publication-request.json for releases
* Create release branches, tags, and GitHub releases
* Monitor automated publication workflows
* Coordinate with WHO SMART Guidelines team for smart.who.int updates
* Manage cross-IG governance for shared artifacts
* Reset main branch to draft status after publication
**Source**: IG Starter Kit, IG Setup, IG Publication, and IG Configuration pages |
| [Quality Control Reviewer](ActorDefinition-SGAuthoring.Persona.QCReviewer.md) | A quality assurance specialist responsible for reviewing SMART Guidelines Implementation Guides for publication readiness. QC Reviewers use the publication checklist across L1-L4 layers, interpret QA validation reports, and verify artifact conformance and cross-component consistency.Key activities:* Run and interpret IG Publisher QA reports (qa.html)
* Review publication checklist across L1, L2, L3, L4, and Global sections
* Verify conformance to Shareable, Publishable, Computable, Executable profiles
* Validate StructureMap extraction produces expected output
* Verify CQL execution and measure calculations
* Check cross-component consistency (personas, data elements, processes)
* Validate all artifacts have required title, description, and mappings
* Confirm naming conventions and reference resolution
* Review change log completeness and versioning compliance
**Source**: IG Starter Kit, QA Check page, Checklist page, Validating IG page |
| [Technical Officer](ActorDefinition-SGAuthoring.Persona.TechnicalOfficer.md) | A health area technical officer who coordinates the work on the DAK and performs first-pass review and validation of DAK content. Technical officers are part of the DAK development team and serve as the primary bridge between the development team and the broader group of Subject Matter Experts.Key activities:* Coordinate DAK development work within the health programme area
* Perform first-pass review of drafted DAK components
* Validate that components accurately reflect L1 recommendations
* Identify gaps, ambiguities, and alternatives in DAK content
* Prepare agendas and questions for SME consultation meetings
* Ensure content is software-neutral and context-appropriate
* Spread awareness of SMART Guidelines within the department
**Source**: IG Starter Kit, L2 DAK Authoring, Section 2.2 "Validate DAK content with SMEs" |
| [Terminologist](ActorDefinition-SGAuthoring.Persona.Terminologist.md) | A specialist responsible for ensuring semantic interoperability of SMART Guidelines through proper terminology management. Terminologists manage the WHO Commons dictionary, concept mappings, and ensure every data element is mapped to approved standard terminologies.Key activities:* Map data elements to WHO Commons dictionary concepts
* Create and maintain CodeSystem resources
* Create and maintain ValueSet resources
* Create ConceptMap resources for cross-terminology mappings
* Map to ICD-11, SNOMED CT, LOINC, IPS, and WHO FIC
* Onboard new concepts into the Commons dictionary
* Verify no duplicate or overlapping concept definitions
* Review terminology bindings in logical models and profiles
* Flag unapproved concepts as QA issues before publication
**Source**: IG Starter Kit, Governance Concepts page; L3 authoring pages for CodeSystems, ValueSets, ConceptMaps |
| [Translator](ActorDefinition-SGAuthoring.Persona.Translator.md) | A language specialist responsible for translating SMART Guidelines Implementation Guide content across UN languages to support global adoption and adaptation.Key activities:* Translate IG narrative content across UN languages
* Translate FHIR resource display names and descriptions
* Review translated content for accuracy and clinical correctness
* Manage .pot/.po translation template files
* Coordinate with clinical SMEs for domain-specific terminology
* Ensure translated examples are available for each non-abstract profile
**Source**: IG Starter Kit, Checklist L4 (example resources per UN language); PR 288 translation skill infrastructure |

### Requirements: Formal Requirements 

The following artifacts describe the specific requirements to be met by systems compliant with the implementation guide.

| | |
| :--- | :--- |
| [Can author CQL](Requirements-SGAuthoring.Skills.AuthorCQL.md) | Capability to write Clinical Quality Language (CQL) for decision logic, scheduling logic, and indicator calculations. |
| [Can author FHIR profiles](Requirements-SGAuthoring.Skills.AuthorFHIRProfiles.md) | Capability to create FHIR profiles (StructureDefinitions) constraining base FHIR resources. |
| [Can author FHIR requirements](Requirements-SGAuthoring.Skills.AuthorFHIRRequirements.md) | Capability to create FHIR Requirements resources from L2 functional and non-functional requirements. |
| [Can author actor definitions](Requirements-SGAuthoring.Skills.AuthorActorDefinitions.md) | Capability to create FHIR ActorDefinitions from L2 personas, reusing existing definitions from the Commons repository. |
| [Can author business processes](Requirements-SGAuthoring.Skills.AuthorBusinessProcesses.md) | Capability to create BPMN 2.0 business process diagrams for DAK workflows. |
| [Can author code systems](Requirements-SGAuthoring.Skills.AuthorCodeSystems.md) | Capability to create and maintain FHIR CodeSystem resources. |
| [Can author concept maps](Requirements-SGAuthoring.Skills.AuthorConceptMaps.md) | Capability to create FHIR ConceptMap resources for cross-terminology mappings. |
| [Can author data dictionary](Requirements-SGAuthoring.Skills.AuthorDataDictionary.md) | Capability to define core data elements and map to standard terminologies. |
| [Can author decision-support logic](Requirements-SGAuthoring.Skills.AuthorDecisionLogic.md) | Capability to develop decision-support logic tables following the DMN standard. |
| [Can author example scenarios](Requirements-SGAuthoring.Skills.AuthorExampleScenarios.md) | Capability to create ExampleScenario resources from L2 user scenarios. |
| [Can author functional requirements](Requirements-SGAuthoring.Skills.AuthorFunctionalRequirements.md) | Capability to define high-level functional and non-functional requirements linked to personas and business processes. |
| [Can author indicators](Requirements-SGAuthoring.Skills.AuthorIndicators.md) | Capability to define indicators and performance metrics with numerator/denominator specifications. |
| [Can author logical models](Requirements-SGAuthoring.Skills.AuthorLogicalModels.md) | Capability to create FHIR logical models (StructureDefinitions) from L2 data dictionaries. |
| [Can author measures](Requirements-SGAuthoring.Skills.AuthorMeasures.md) | Capability to create FHIR Measure resources from L2 indicators. |
| [Can author personas](Requirements-SGAuthoring.Skills.AuthorPersonas.md) | Capability to define generic personas based on task-shifting guidelines and ground-truthing interviews. |
| [Can author plan definitions](Requirements-SGAuthoring.Skills.AuthorPlanDefinitions.md) | Capability to create FHIR PlanDefinitions for business processes and decision tables. |
| [Can author questionnaires](Requirements-SGAuthoring.Skills.AuthorQuestionnaires.md) | Capability to create FHIR Questionnaire resources aligned with L2 forms and data collection needs. |
| [Can author scheduling logic](Requirements-SGAuthoring.Skills.AuthorSchedulingLogic.md) | Capability to develop scheduling logic tables following the DMN standard. |
| [Can author structure maps](Requirements-SGAuthoring.Skills.AuthorStructureMaps.md) | Capability to create FHIR StructureMaps for data extraction from QuestionnaireResponses to FHIR resources. |
| [Can author test cases](Requirements-SGAuthoring.Skills.AuthorTestCases.md) | Capability to create TestPlan, TestScript, and example instances for validation of L3 artifacts. |
| [Can author user scenarios](Requirements-SGAuthoring.Skills.AuthorUserScenarios.md) | Capability to create user scenario narratives depicting typical interactions in health programme workflows. |
| [Can author value sets](Requirements-SGAuthoring.Skills.AuthorValueSets.md) | Capability to create and maintain FHIR ValueSet resources with appropriate terminology bindings. |
| [Can build IG](Requirements-SGAuthoring.Skills.BuildIG.md) | Capability to run the FHIR IG Publisher build process and verify output. |
| [Can configure IG](Requirements-SGAuthoring.Skills.ConfigureIG.md) | Capability to set up and configure a FHIR Implementation Guide (sushi-config, canonical URL, packages). |
| [Can interpret clinical recommendations](Requirements-SGAuthoring.Skills.InterpretClinicalRecommendations.md) | Capability to interpret clinical recommendations from L1 source documents with domain expertise. |
| [Can manage governance](Requirements-SGAuthoring.Skills.ManageGovernance.md) | Capability to manage cross-IG governance for shared artifacts including common personas, terminology, and libraries. |
| [Can manage releases](Requirements-SGAuthoring.Skills.ManageReleases.md) | Capability to manage versioning, publication-request.json, release tags, and publication workflow. |
| [Can manage stakeholders](Requirements-SGAuthoring.Skills.ManageStakeholders.md) | Capability to engage SMEs, coordinate consultations, and manage the RASCI matrix for DAK development. |
| [Can map concepts](Requirements-SGAuthoring.Skills.MapConcepts.md) | Capability to map data elements to WHO Commons dictionary, ICD-11, SNOMED CT, LOINC, and other standard terminologies. |
| [Can plan iterations](Requirements-SGAuthoring.Skills.PlanIterations.md) | Capability to plan sprint iterations, maintain the DAK backlog, draft the project roadmap, and facilitate retrospectives. |
| [Can review L1 guidelines](Requirements-SGAuthoring.Skills.ReviewL1Guidelines.md) | Capability to review WHO L1 narrative guidelines and normative products for accuracy and completeness. |
| [Can review and approve content](Requirements-SGAuthoring.Skills.ReviewAndApproveContent.md) | Capability to review and formally approve SMART Guidelines content at decision gates in the authoring lifecycle. |
| [Can review checklist](Requirements-SGAuthoring.Skills.ReviewChecklist.md) | Capability to review the SMART Guidelines publication checklist across L1-L4 layers and global requirements. |
| [Can review terminology](Requirements-SGAuthoring.Skills.ReviewTerminology.md) | Capability to review and validate terminology bindings, code systems, and value sets for correctness and completeness. |
| [Can review translations](Requirements-SGAuthoring.Skills.ReviewTranslations.md) | Capability to review translated content for accuracy and completeness. |
| [Can run QA checks](Requirements-SGAuthoring.Skills.RunQAChecks.md) | Capability to run and interpret IG Publisher QA validation reports. |
| [Can scope DAK](Requirements-SGAuthoring.Skills.ScopeDAK.md) | Capability to define DAK scope, identify source documents, and establish the development process and governance. |
| [Can translate content](Requirements-SGAuthoring.Skills.TranslateContent.md) | Capability to translate IG content across UN languages. |
| [Can validate DAK content](Requirements-SGAuthoring.Skills.ValidateDAKContent.md) | Capability to review and validate DAK components against L1 source documents and for cross-component consistency. |
| [Can validate L3 functionality](Requirements-SGAuthoring.Skills.ValidateL3Functionality.md) | Capability to test StructureMap extraction, CQL execution, and measure calculation using reference tooling. |
| [Can validate artifact conformance](Requirements-SGAuthoring.Skills.ValidateArtifactConformance.md) | Capability to verify conformance to CRMI Shareable, Publishable, Computable, and Executable profiles. |

### Knowledge Artifacts: Activity Definitions 

These define activities that can be performed as part of content in this implementation guide.

| |
| :--- |
| [SGDecisionTableGuidance](ActivityDefinition-SGDecisionTableGuidance.md) |

### Structures: Logical Models 

These define data models that represent the domain covered by this implementation guide in more business-friendly terms than the underlying FHIR resources.

| | |
| :--- | :--- |
| [Business Process Workflow (DAK)](StructureDefinition-BusinessProcessWorkflow.md) | Logical Model for representing Generic Business Processes and Workflows from a DAK. A business process is a set of related activities or tasks performed together to achieve the objectives of the health programme area. |
| [Business Process Workflow Source](StructureDefinition-BusinessProcessWorkflowSource.md) | Source reference for Business Process Workflow - exactly one of the following must be provided:* url (url data type): URL to retrieve BusinessProcessWorkflow definition from input/ or external source
* canonical (canonical data type): Canonical URI pointing to the BusinessProcessWorkflow definition
* instance: Inline BusinessProcessWorkflow instance data
 |
| [Core Data Element (DAK)](StructureDefinition-CoreDataElement.md) | Logical Model for representing Core Data Elements from a DAK. A core data element can be one of: a ValueSet, a CodeSystem, a ConceptMap, or a Logical Model adherent to SGLogicalModel. This is the ONE EXCEPTION to allowing FHIR R4 models into the DAK LMs. |
| [Core Data Element Source](StructureDefinition-CoreDataElementSource.md) | Source reference for Core Data Element - exactly one of the following must be provided:* url (url data type): URL to retrieve CoreDataElement definition from input/ or external source
* canonical (canonical data type): Canonical URI pointing to the CoreDataElement definition
* instance: Inline CoreDataElement instance data
 |
| [Decision Support Logic Source](StructureDefinition-DecisionSupportLogicSource.md) | Source reference for Decision Support Logic - exactly one of the following must be provided:* url (url data type): URL to retrieve DecisionSupportLogic definition from input/ or external source
* canonical (canonical data type): Canonical URI pointing to the DecisionSupportLogic definition
* instance: Inline DecisionSupportLogic instance data
 |
| [Decision-Support Logic (DAK)](StructureDefinition-DecisionSupportLogic.md) | Logical Model for representing Decision-Support Logic from a DAK. Decision-support logic and algorithms to support appropriate service delivery in accordance with WHO clinical, public health and data use guidelines. |
| [Digital Adaptation Kit (DAK)](StructureDefinition-DAK.md) | Logical Model for representing a complete Digital Adaptation Kit (DAK) with metadata and all 9 DAK components |
| [Dublin Core Metadata Element Set](StructureDefinition-DublinCore.md) | Logical Model representing Dublin Core metadata elements as defined at https://www.dublincore.org/specifications/dublin-core/dcmi-terms/ |
| [FHIR Schema Base (SMART Guidelines)](StructureDefinition-FHIRSchemaBase.md) | Base logical model providing the common schema metadata interface inherited by all SMART Guidelines logical models. Every SMART Guidelines logical model schema derives from this base, which documents the shared FHIR and JSON-LD metadata properties used by the JSON Schema generation pipeline. |
| [Functional Requirement (DAK)](StructureDefinition-FunctionalRequirement.md) | Logical Model for representing functional requirement from a DAK |
| [Functional and Non-Functional Requirements (DAK)](StructureDefinition-Requirements.md) | Logical Model for representing Functional and Non-Functional Requirements from a DAK. A high-level list of core functions and capabilities that the system must have to meet the end users' needs. |
| [Generic Persona (DAK)](StructureDefinition-GenericPersona.md) | Logical Model for representing Generic Personas from a DAK. Depiction of the human and system actors. Human actors are end users, supervisors and related stakeholders who would be interacting with the digital system or involved in the clinical care, public health or health system pathway. |
| [Generic Persona Source](StructureDefinition-GenericPersonaSource.md) | Source reference for Generic Persona - exactly one of the following must be provided:* url (url data type): URL to retrieve GenericPersona definition from input/ or external source
* canonical (canonical data type): Canonical URI pointing to the GenericPersona definition
* instance: Inline GenericPersona instance data
 |
| [Health Interventions Source](StructureDefinition-HealthInterventionsSource.md) | Source reference for Health Interventions - exactly one of the following must be provided:* url (url data type): URL to retrieve HealthInterventions definition from input/ or external source
* canonical (canonical data type): Canonical URI pointing to the HealthInterventions definition
* instance: Inline HealthInterventions instance data
 |
| [Health Interventions and Recommendations (DAK)](StructureDefinition-HealthInterventions.md) | Logical Model for representing Health Interventions and Recommendations from a DAK. Overview of the health interventions and WHO, regional or national recommendations included within the DAK. |
| [Knowledge graph L1-LIBRARY: Implementation practice](StructureDefinition-KGImplementationPractice.md) | A statement of how to put guidance into practice, printed in a publication whose publicationType is implementation-guidance or methodology: the handbook's "products that are not guidelines" (§1.9), a "how to" document that makes no recommendations of its own. Not a recommendation, and not a good practice statement — both are made by a guideline and approved by the GRC; this is neither. It carries no kind, direction, strength or certainty, because nothing graded it. A handbook's own "Best practices" lists are the typical source. Owner ruling 1b, 2026-10-12: model these as their own class, not as recommendation nodes of a new kind. statement is verbatim and is the only stored copy, as recommendation's is. identifier is used in the IRI. There is no remark: L1 3.0's remark is minted under a recommendation (its iriPattern) and hasRemark starts at one, so a remark of a practice needs L1 itself to change — proposed upstream, not patched here. Class IRI: http://smart.who.int/kg/implementation-practice. |
| [Knowledge graph L1-LIBRARY: Library node](StructureDefinition-KGLibraryNode.md) | A node in the ingested library L1 is read from: a source document, a section or a block, addressed by the library's own IRI. Opaque, as L1 asserts nothing about the library's internal model; the library is upstream, so pointing at it keeps the layering rule. Class IRI: http://smart.who.int/kg/library-node. |
| [Knowledge graph L1: Citation](StructureDefinition-KGCitation.md) | One citation string exactly as written in a DAK artefact. A cell holding several citations yields several nodes. Content-addressed in the DAK's namespace, so one string is one node across artefacts. Where a citation was found is recorded by appearsIn (L2) and by each use edge (L2-DMN, L3 citesSource), not on the node. Class IRI: http://smart.who.int/kg/citation. |
| [Knowledge graph L1: Evidence](StructureDefinition-KGEvidence.md) | One row of an evidence profile: the evidence for one outcome of one key question, with its certainty (handbook §9.2). Class IRI: http://smart.who.int/kg/evidence. |
| [Knowledge graph L1: Health intervention](StructureDefinition-KGHealthIntervention.md) | An intervention identified in a WHO catalogue or classification (UHC Compendium, ICHI, CDHI), digital interventions included. A peer of recommendation, not a recommendation. A DAK may draw on both. Corresponds to HealthInterventions: identifier and description correspond to HealthInterventions.id and description[x]; not a Parent because HealthInterventions requires reference 1..* DublinCore, which here is an edge (definedIn) rather than a field. Class IRI: http://smart.who.int/kg/health-intervention. |
| [Knowledge graph L1: Indicator](StructureDefinition-KGIndicator.md) | A WHO indicator, identified by its published reference number. Printed in several places (HIV SI 2022: summary list, Table 2.3, reference sheet) and stored once. variants is a list of {population, definition, numerator, denominator} for population-specific or level-specific forms (PRV.17, PRV.3). Corresponds to ProgramIndicator: definition, numerator, denominator and disaggregation are ProgramIndicator's elements and types (markdown); not a Parent because ProgramIndicator makes them 1..1 and an L1 indicator is recorded with what its source prints. Class IRI: http://smart.who.int/kg/indicator. |
| [Knowledge graph L1: Key question](StructureDefinition-KGKeyQuestion.md) | A question in PICO format, framed before the evidence search (handbook §7.1–7.4). P and C are verbatim text with codes through crossReferences; I is also joined to a catalogued intervention; O is the outcome node. Class IRI: http://smart.who.int/kg/key-question. |
| [Knowledge graph L1: Outcome](StructureDefinition-KGOutcome.md) | An outcome a guideline group chose to judge a key question by, with its importance in this guideline (handbook §7.6). A node because evidence attaches to it and one list is shared by several questions (ANC Web annex 1). Flat: one node per specific outcome. name as first printed; aliases are the other printed forms (e.g. 'EGWG'); category is the printed group heading (e.g. 'Fetal/newborn morbidity'). Class IRI: http://smart.who.int/kg/outcome. |
| [Knowledge graph L1: Publication](StructureDefinition-KGPublication.md) | A WHO publication: a guideline of any of the handbook's types, a position paper, a summary table, a classification, implementation guidance, or a supplement. Metadata follows Dublin Core. identifiers is a list of {type, value}; type is from identifier-type, and the first of isbn, iris-handle, doi, issn, url builds the IRI, so an edition change is a new publication. issued and modified are Dublin Core. reviewBy is the handbook's review-by date (§12.5.1). sha256 pins the PDF. Derives from DublinCore (smart-base input/fsh/models/DublinCore.fsh); title, creator, publisher, language, rights are its elements. Class IRI: http://smart.who.int/kg/publication. |
| [Knowledge graph L1: Publication element](StructureDefinition-KGPublicationElement.md) | One printed block: a table, a table row, a footnote, a figure, a chart, an image, a flowchart, a box or a list. It records where something is printed and exactly what is printed that no content node holds. It carries no meaning of its own; meaning lives in content nodes, joined by presentedIn. columns is the header text, verbatim. columnMap names, per column, the content field that fills it when the table is re-rendered (e.g. 'Recommendation' -> statement). cells holds only text no content node holds; a cell filled through columnMap is null. text is for unmodelled printed text such as a footnote that is not a remark. sha256 is for images. Class IRI: http://smart.who.int/kg/publication-element. |
| [Knowledge graph L1: Publication section](StructureDefinition-KGPublicationSection.md) | A chapter, annex or numbered section, at any depth. Class IRI: http://smart.who.int/kg/publication-section. |
| [Knowledge graph L1: Recommendation](StructureDefinition-KGRecommendation.md) | A normative statement from a WHO guideline. Kinds other than a graded recommendation (context-specific, research-only, good practice statement, no-recommendation) are the same node with a different kind. statement is verbatim and is the only stored copy. intervention, population, setting, provider and timing are verbatim slots taken from the statement, its remarks, or the enclosing caption or heading. setting absorbs the former conditionality. identifier is the published number (e.g. A.1.1), used in the IRI; sub-recommendations append their letter. Class IRI: http://smart.who.int/kg/recommendation. |
| [Knowledge graph L1: Reference entry](StructureDefinition-KGReferenceEntry.md) | One row of a DAK artefact's own reference list: '(1)' and the full bibliographic text and URL it stands for. Resolved once; every citation numbered to it shares the result. Class IRI: http://smart.who.int/kg/reference-entry. |
| [Knowledge graph L1: Remark](StructureDefinition-KGRemark.md) | A remark attached to a recommendation (handbook §10.6). May also be printed as a table footnote. Class IRI: http://smart.who.int/kg/remark. |
| [Knowledge graph L1: Terminology code](StructureDefinition-KGTerminologyCode.md) | A code in an external terminology — ICD-10, ICD-11, SNOMED CT, ATC, or a WHO classification such as CDHI. CROSS-REFERENCE ONLY. It records system, code and display, and asserts NOTHING about the terminology: no hierarchy, no subsumption, no synonyms, no post-coordination. The terminology has its own authority, its own release cycle and its own tooling, and a partial copy here would be wrong within one release. Resolve meaning against the terminology server, not against this graph. Derives from Coding (FHIR R4 core datatype); system, code, display, version are its elements. Class IRI: http://smart.who.int/kg/terminology-code. |
| [Knowledge graph L1: graph document](StructureDefinition-KGGraphDocument.md) | One L1 knowledge-graph document: typed nodes and reified edges, provenance-pinned to the sources it was extracted from. In JSON the context element is written @context. |
| [Knowledge graph L2-BPMN: BPMN Event](StructureDefinition-KGBpmnEvent.md) | A start, end or intermediate event (WHO's DAK BPMN draw intermediate throw and catch events inside sub-processes). Same connectivity argument as gateway, plus one of its own: entry and exit points are what make 'is this task reachable' and 'does this path terminate' answerable at all. Class IRI: http://smart.who.int/kg/bpmn-event. |
| [Knowledge graph L2-BPMN: BPMN File](StructureDefinition-KGBpmnDefinitions.md) | One BPMN file as a unit – the `bpmn:definitions` root. Shares its IRI with the l1:external-artifact for the same file, so the component that points at it and the subgraph that opens it name one resource. Class IRI: http://smart.who.int/kg/bpmn-definitions. |
| [Knowledge graph L2-BPMN: BPMN Gateway](StructureDefinition-KGBpmnGateway.md) | A branch or merge. Included for connectivity rather than for a cross-model edge: a flow through a gateway with no node would point at nothing, and every reachability question over the process would break at the first decision point. Class IRI: http://smart.who.int/kg/bpmn-gateway. |
| [Knowledge graph L2-BPMN: BPMN Participant](StructureDefinition-KGBpmnParticipant.md) | A pool: a role that owns part of the collaboration. The lifecycle BPMN has 8 and declares no laneSet at all, so the pool is the only unit of role assignment present and its @name is the sole link to a persona. Class IRI: http://smart.who.int/kg/bpmn-participant. |
| [Knowledge graph L2-BPMN: BPMN Process](StructureDefinition-KGBpmnProcess.md) | One `bpmn:process`. Present as a node because a participant references it by processRef, and without it the pool-to-element attribution has nothing to travel through. Class IRI: http://smart.who.int/kg/bpmn-process. |
| [Knowledge graph L2-BPMN: BPMN Task](StructureDefinition-KGBpmnTask.md) | A task or sub-process. It is what a DMN usingTask href points at, what sequence flows connect, and what a DAK-level task entry describes. Sub-processes carry isSubProcess rather than getting a class of their own – the lifecycle BPMN has exactly one. Class IRI: http://smart.who.int/kg/bpmn-task. |
| [Knowledge graph L2-DMN: DMN Decision](StructureDefinition-KGDmnDecision.md) | A `dmn:decision` – the question being answered, and the node that carries the link back to the BPMN task invoking it. A file may hold several; the BCG file holds one. Class IRI: http://smart.who.int/kg/dmn-decision. |
| [Knowledge graph L2-DMN: DMN Decision Table](StructureDefinition-KGDmnDecisionTable.md) | The table realising a decision. Separate from dmn-decision because DMN permits other expression kinds – a literal expression, an invocation – and collapsing the two would make the graph unable to say which was used. hitPolicy is optional and recorded as null when absent, which it is in the BCG table. DMN's default is UNIQUE, but asserting it here would put words in the author's mouth. Class IRI: http://smart.who.int/kg/dmn-decision-table. |
| [Knowledge graph L2-DMN: DMN File](StructureDefinition-KGDmnDefinitions.md) | One DMN file as a unit – the `dmn:definitions` root. Shares its IRI with the l1:external-artifact for the same file, so the l2:decision-support-logic component that points at it and this subgraph name one resource. Class IRI: http://smart.who.int/kg/dmn-definitions. |
| [Knowledge graph L2-DMN: DMN Input Clause](StructureDefinition-KGDmnInputClause.md) | An input column. Its expression text is where data element names are embedded, which is the only reason this is a node rather than a property of the table. Class IRI: http://smart.who.int/kg/dmn-input-clause. |
| [Knowledge graph L2-DMN: DMN Output Clause](StructureDefinition-KGDmnOutputClause.md) | An output column. The BCG table's four are Care Plan, Guidance displayed to health worker, Annotations and Reference(s). These are column DEFINITIONS in a decision table, not clinical records: no edge from this class reaches an execution artefact, and none may. serialisedAs is outputEntry or annotationEntry – DMN splits the columns across two element types and the split is positional, so recording it is what lets a rule's cells be matched back to their columns. isReferenceColumn marks the L1 column, found by its description rather than its index. Class IRI: http://smart.who.int/kg/dmn-output-clause. |
| [Knowledge graph L2-DMN: DMN Rule](StructureDefinition-KGDmnRule.md) | One row. Its input and output cells are carried as properties, not nodes: 250 of them in the BCG table alone, none the target of a cross-model edge. What the rule needs a node for is its citation edge into L1. conditions and outputs are arrays of {clause, description, text}. DMN puts the formal expression in description and the human-readable gloss in text, and both are worth keeping – the gloss is what a reviewer reads and the expression is what an implementer builds. Class IRI: http://smart.who.int/kg/dmn-rule. |
| [Knowledge graph L2: Business Process Workflow](StructureDefinition-KGBusinessProcess.md) | DAK component 4. NOT the BPMN file – the component that points at one. `source 1..1 uri` is that pointer, and the BPMN's interior is the l2-bpmn subgraph, reached through the external-artifact this sourcedFrom targets. `objectives 1..1 markdown` is required by BusinessProcessWorkflow.fsh and has no counterpart anywhere in BPMN XML, so it can only ever come from the FSH instance. resolutionStatus is `unresolved` on a component that something else names but no DAK declares – an L3 artefact whose title carries the component id, for instance. The node exists so the gap is queryable and carries the referenced id and nothing else. Class IRI: http://smart.who.int/kg/business-process. |
| [Knowledge graph L2: Core Data Element](StructureDefinition-KGDataElement.md) | 
| | | | |
| :--- | :--- | :--- | :--- |
| DAK component 5. CoreDataElement.fsh calls itself "the ONE EXCEPTION to allowing FHIR R4 models into the DAK LMs":`type`is one of valueset | codesystem | conceptmap | logicalmodel and`canonical 1..1 uri`points at it. The canonical is recorded; nothing inside it is copied, because FHIR is its own query layer.`name`,`resolutionStatus`and`extractionRule`are for elements recovered from DMN input expressions rather than declared in a dictionary. A recovered element is a name that was REFERENCED, not a definition that was found, and only a resolved one may carry a canonical. Class IRI: http://smart.who.int/kg/data-element. |
 |
| [Knowledge graph L2: Decision-Support Logic](StructureDefinition-KGDecisionSupportLogic.md) | DAK component 6. The whole model is an id, an optional description and `source 1..1 uri` to a DMN file. Nothing about the decision itself – which is the gap the l2-dmn subgraph fills. resolutionStatus is `unresolved` on a component that something else names but no DAK declares – an L3 artefact whose title carries the component id, for instance. The node exists so the gap is queryable and carries the referenced id and nothing else. Class IRI: http://smart.who.int/kg/decision-support-logic. |
| [Knowledge graph L2: Digital Adaptation Kit](StructureDefinition-KGDak.md) | The kit itself. Properties are exactly the metadata fields DAK.fsh declares and dak.json carries – no more, so that a dak node can be produced from a real file without anything being invented. canonicalUrl equals publicationUrl on a release branch and previewUrl on a development branch, per DAK.fsh. Both are kept because which one canonicalUrl currently equals is what says whether a graph describes a release or a build. Class IRI: http://smart.who.int/kg/dak. |
| [Knowledge graph L2: External artefact](StructureDefinition-KGExternalArtifact.md) | A DAK file addressed by canonical URL: a BPMN process, a DMN decision table, a FHIR resource, a workbook. Deliberately opaque: it carries an IRI and a kind, and nothing about its interior. The L2-BPMN, L2-DMN and L3 classes that describe a file's interior elaborate this class at the same IRI. Moved here from L1 in 3.0 unchanged: a DAK file is the DAK's material, not WHO content. Class IRI: http://smart.who.int/kg/external-artifact. |
| [Knowledge graph L2: Functional Requirement](StructureDefinition-KGFunctionalRequirement.md) | DAK component 8, first half. The as-a/I-want/so-that shape: `activity`, `capability[x]`, `benefit[x]`, and `actor 0..* Reference(SGActor)`. The 41 committed instances use the R5 SGRequirements profile rather than this logical model, so a real instance carries `statement` entries and a userstory extension; both shapes are accommodated and `profile` records which was read. resolutionStatus is `unresolved` on a component that something else names but no DAK declares – an L3 artefact whose title carries the component id, for instance. The node exists so the gap is queryable and carries the referenced id and nothing else. Class IRI: http://smart.who.int/kg/functional-requirement. |
| [Knowledge graph L2: Generic Persona](StructureDefinition-KGPersona.md) | DAK component 2. Grounded in GenericPersona.fsh – title, id, description, otherNames, iscoCode bound to ISCO08ValueSet – and in the 22 committed ActorDefinition instances that carry name, title, type and description. The two disagree about where ISCO lives, which the properties record rather than smooth over. `title` is the human-readable label a BPMN pool matches on; `name` is the CamelCase identifier a Canonical() reference matches on. They are different strings for the same persona and conflating them is precisely how the pool join breaks. GenericPersona.fsh declares `iscoCode 0..* code`, but the committed ActorDefinitions record ISCO in prose inside description, so iscoCode is usually empty and is not authoritative. Class IRI: http://smart.who.int/kg/persona. |
| [Knowledge graph L2: Non-Functional Requirement](StructureDefinition-KGNonFunctionalRequirement.md) | DAK component 8, second half. `requirement 1..1 markdown`, an optional category and classification codings. Kept separate from the functional half because the fields genuinely differ – a non-functional requirement has no actor and no benefit. resolutionStatus is `unresolved` on a component that something else names but no DAK declares – an L3 artefact whose title carries the component id, for instance. The node exists so the gap is queryable and carries the referenced id and nothing else. Class IRI: http://smart.who.int/kg/non-functional-requirement. |
| [Knowledge graph L2: Program Indicator](StructureDefinition-KGProgramIndicator.md) | DAK component 7. Named program-indicator and not `indicator` because L1 already declares an `indicator` – one normatively defined in a publication. They are different things: this is the DAK's operational measure, and `derivedFrom` is how it points at the normative one. Collapsing them would silently merge a WHO definition with a country's implementation of it. numerator, denominator and disaggregation are all `1..1 markdown` – prose, not a computable expression. Nothing here should be read as a calculable measure; the L3 FHIR Measure is where that would live. resolutionStatus is `unresolved` on a component that something else names but no DAK declares – an L3 artefact whose title carries the component id, for instance. The node exists so the gap is queryable and carries the referenced id and nothing else. Class IRI: http://smart.who.int/kg/program-indicator. |
| [Knowledge graph L2: Requirement Statement](StructureDefinition-KGRequirementStatement.md) | 
| | | | |
| :--- | :--- | :--- | :--- |
| One numbered, labelled statement inside a requirement, with a conformance verb. A node rather than a property because conformance is queried across a whole DAK – 'every SHALL in this kit, and what fulfils it' is the question requirements exist to answer. It also carries its own success criteria, so 'what would show this SHALL is met' is answerable per statement rather than per requirement. conformance is the FHIR ConformanceExpectation verb: SHALL, SHOULD, MAY or SHOULD-NOT. Across the 41 committed instances it is 155 SHALL and 15 SHOULD. successCriteria is a LIST of objects, each {key, criterion, verification}:`key`is unique within the statement (e.g. SC-1),`criterion`is a checkable sentence, and`verification`is one of test | inspection | review | analysis – the same field name and enum as folio-assistant's requirement.ts`successCriteria`, so the two map 1:1. smart-base types it, so the shape is enforced by the schema; a statement with no successCriteria is still valid (the 170 statements committed in smart-base carry none). Class IRI: http://smart.who.int/kg/requirement-statement. |
 |
| [Knowledge graph L2: Scheduling Logic](StructureDefinition-KGSchedulingLogic.md) | When an intervention is due, as a DAK component. NOT declared by DAK.fsh – it is added here because the published SOP lists Scheduling Logic as an active L2 input (spreadsheets under input/scheduling-logic), WHO's ArchiMate model declares it a BusinessObject realised by PlanDefinition, and L1's schedules needed an L2 component to reach (since L1 3.0, a recommendation's timing slot). Note that the SOP's own L3 row for scheduling is present but HTML-commented-out and there is no l3_schedulinglogic.md page, so WHO has drafted the mapping and not activated it; the L3 edge is licensed here as a deliberate departure, recorded rather than hidden. resolutionStatus is `unresolved` on a component that something else names but no DAK declares – an L3 artefact whose title carries the component id, for instance. The node exists so the gap is queryable and carries the referenced id and nothing else. Class IRI: http://smart.who.int/kg/scheduling-logic. |
| [Knowledge graph L2: Task Entry](StructureDefinition-KGDakTask.md) | One task of a DAK business process, as the DAK document's "notes and annotations" describe it: identifier, name, description, and the personas, data elements, requirements and decision tables it links to. A node rather than a property because the same task is also drawn in the BPMN file, and the two have to be joinable to be checkable against each other (`describes`). Read from a BPMN file's `dak-task-annotations/v1` sidecar (smart-base/L2-bpmn/schemas/task-annotations.ts); BusinessProcessWorkflow's `task 0..*` backbone carries the first three fields of the same thing. Class IRI: http://smart.who.int/kg/dak-task. |
| [Knowledge graph L2: Test Scenario](StructureDefinition-KGTestScenario.md) | DAK component 9. `feature 1..1 uri` to a Gherkin feature file, plus an optional description. The feature file's interior is not modelled: no DAK in this estate ships one yet, so a subgraph for it would have no instance to check it against. resolutionStatus is `unresolved` on a component that something else names but no DAK declares – an L3 artefact whose title carries the component id, for instance. The node exists so the gap is queryable and carries the referenced id and nothing else. Class IRI: http://smart.who.int/kg/test-scenario. |
| [Knowledge graph L2: User Scenario](StructureDefinition-KGUserScenario.md) | DAK component 3. A narrative describing how personas interact. Carries `personas 0..* id`, which is the only structured link between the narrative layer and the personas it names. resolutionStatus is `unresolved` on a component that something else names but no DAK declares – an L3 artefact whose title carries the component id, for instance. The node exists so the gap is queryable and carries the referenced id and nothing else. Class IRI: http://smart.who.int/kg/user-scenario. |
| [Knowledge graph L3: Activity Definition](StructureDefinition-KGActivityDefinition.md) | A FHIR ActivityDefinition – the concrete act a plan's action invokes. Reached from a PlanDefinition action's `definitionCanonical`, which is a real reference rather than a convention. 3 in the immunizations IG: two cpg-immunizationactivity, one cpg-communicationactivity. Class IRI: http://smart.who.int/kg/activity-definition. |
| [Knowledge graph L3: Actor Definition](StructureDefinition-KGActorDefinition.md) | A FHIR ActorDefinition – an L2 persona made a FHIR resource. ZERO in the immunizations IG and 22 in smart-base, which is itself worth a coverage query. The SOP names no profile for it and says one is not currently possible because SUSHI cannot profile an R5 resource in an R4 IG, and it tells authors not to assign an identifier – so expect a bare resource and do not infer more. Class IRI: http://smart.who.int/kg/actor-definition. |
| [Knowledge graph L3: CQL File](StructureDefinition-KGCqlLibrary.md) | A .cql file on disk, as opposed to the FHIR Library resource that wraps it. A node so that the mapping table's four CQL rows – CQL Concepts and CQL Data Elements under Elements, CQL under Decision Tables, CQL IndicatorLogic under Indicators – do not dead-end. It carries a name, a path and a hash and NOTHING about the logic: no expressions, no comment tags, no data requirements. 279 in the immunizations IG. The l3-cql subgraph is where that content belongs, and it is not built yet. No canonical, because a .cql file is not a FHIR resource and has no canonical URL. It is reached through the Library that wraps it. Class IRI: http://smart.who.int/kg/cql-library. |
| [Knowledge graph L3: Code System](StructureDefinition-KGCodeSystem.md) | A FHIR CodeSystem. The SOP says each guideline defines one guideline-level code system holding a concept for every data dictionary element – which is what makes `code[WHO] = IMMZ.DE9` on a logical model element resolvable. 6 in the immunizations IG. The codes themselves are not copied here. Class IRI: http://smart.who.int/kg/code-system. |
| [Knowledge graph L3: Concept Map](StructureDefinition-KGConceptMap.md) | A FHIR ConceptMap – one per target code system in the dictionary's terminology mappings. 8 in the immunizations IG. Records that a mapping exists; the mappings themselves belong to terminology. Class IRI: http://smart.who.int/kg/concept-map. |
| [Knowledge graph L3: Library](StructureDefinition-KGLibrary.md) | A FHIR Library – the resource that carries CQL. Indexed by canonical and status only. Its CONTENTS are deliberately out of scope: a future l3-cql subgraph will elaborate this same IRI, exactly as l2-bpmn elaborates a BPMN file. 279 in the immunizations IG, joined to their PlanDefinition by the `{id}Logic` suffix. Class IRI: http://smart.who.int/kg/library. |
| [Knowledge graph L3: Logical Model](StructureDefinition-KGStructureDefinition.md) | A StructureDefinition with kind `logical` – one data dictionary tab as a data structure. Distinct from `profile`, which constrains a FHIR resource: WHO's ArchiMate model has Logical Model realising Data Object while Profile realises Data Element, and the two are not interchangeable. 15 in the immunizations IG. Class IRI: http://smart.who.int/kg/structure-definition. |
| [Knowledge graph L3: Measure](StructureDefinition-KGMeasure.md) | A FHIR Measure – an indicator made computable. 41 in the immunizations IG, all declaring proportion-measure-cqfm; the SOP makes the profile depend on scoring type, which is why the profile is read rather than assumed. Joined to its L2 indicator by id convention (IMMZ.IND.08 -> IMMZIND08). Class IRI: http://smart.who.int/kg/measure. |
| [Knowledge graph L3: Plan Definition](StructureDefinition-KGPlanDefinition.md) | A FHIR PlanDefinition. The published mapping gives it two sources – Processes and Decision Tables – so a PlanDefinition alone does not say which it came from; the implementedBy edge does. 138 in the immunizations IG, all declaring cpg-recommendationdefinition, all decision tables. Shares its IRI with the l1:external-artifact for the same canonical. Class IRI: http://smart.who.int/kg/plan-definition. |
| [Knowledge graph L3: Profile](StructureDefinition-KGProfile.md) | A StructureDefinition constraining a FHIR resource. Separate from structure-definition for the reason above. 5 in the immunizations IG. Its internals – differentials, element definitions, bindings – are the clearest case of what this layer refuses to re-represent. Class IRI: http://smart.who.int/kg/profile. |
| [Knowledge graph L3: Questionnaire](StructureDefinition-KGQuestionnaire.md) | A FHIR Questionnaire – a data-collection form over a logical model. 10 in the immunizations IG. Its `sdc-questionnaire-targetStructureMap` extension names the StructureMap that extracts it, which is a real canonical reference. The SOP states no linkId convention and none exists in the estate, so no edge is licensed on linkId. Class IRI: http://smart.who.int/kg/questionnaire. |
| [Knowledge graph L3: Requirements](StructureDefinition-KGRequirements.md) | A FHIR Requirements resource. The ONE place the published SOP names an SG profile – SGRequirements – and the grain is one resource per business process holding many statements, not one per requirement. ZERO in the immunizations IG and 41 in smart-base. Class IRI: http://smart.who.int/kg/requirements. |
| [Knowledge graph L3: Structure Map](StructureDefinition-KGStructureMap.md) | A FHIR StructureMap. The SOP requires them in threes – QuestionnaireResponse to logical model, logical model to resource, and a grouping map – so a count that is not a multiple of three is worth a look. 16 .fml files in the immunizations IG. Class IRI: http://smart.who.int/kg/structure-map. |
| [Knowledge graph L3: Value Set](StructureDefinition-KGValueSet.md) | A FHIR ValueSet. 192 in the immunizations IG – the most numerous artefact of all. Indexed by canonical; its expansion, its compose rules and the codes it contains are terminology, which docs/SCOPE.md keeps at arm's length as firmly here as at L1. Class IRI: http://smart.who.int/kg/value-set. |
| [Knowledge graph: edge](StructureDefinition-KGEdge.md) | One reified statement: a predicate from a source node to a target node, with its derivation and evidence. |
| [Knowledge graph: evidence location](StructureDefinition-KGEvidenceLocation.md) | Where a node or edge came from in its source. Required on anything not mechanically derived. |
| [Knowledge graph: node](StructureDefinition-KGNode.md) | One typed node of a knowledge-graph document. Its instance fields are an instance of the logical model of its class (see definedBy), e.g. KGPublication for a publication. |
| [Knowledge graph: provenance source](StructureDefinition-KGProvenanceSource.md) | A source a graph document was extracted from, pinned by hash. |
| [Non-Functional Requirement (DAK)](StructureDefinition-NonFunctionalRequirement.md) | Logical Model for representing non-functional requirement from a DAK |
| [Persona (DAK)](StructureDefinition-Persona.md) | Logical Model for representing Personas from a DAK |
| [Program Indicator (DAK)](StructureDefinition-ProgramIndicator.md) | Logical Model for representing Program Indicators from a DAK. Core set of indicators that need to be aggregated for decision-making, performance metrics and subnational and national reporting. |
| [Program Indicator Source](StructureDefinition-ProgramIndicatorSource.md) | Source reference for Program Indicator - exactly one of the following must be provided:* url (url data type): URL to retrieve ProgramIndicator definition from input/ or external source
* canonical (canonical data type): Canonical URI pointing to the ProgramIndicator definition
* instance: Inline ProgramIndicator instance data
 |
| [Requirements Source](StructureDefinition-RequirementsSource.md) | Source reference for Requirements - exactly one of the following must be provided:* url (url data type): URL to retrieve Requirements definition from input/ or external source
* canonical (canonical data type): Canonical URI pointing to the Requirements definition
* instance: Inline Requirements instance data
 |
| [SUSHI Configuration Logical Model](StructureDefinition-SushiConfigLogicalModel.md) | Logical model defining the structure of sushi-config.yaml files used for FHIR Implementation Guide configuration. This model captures the essential metadata and configuration parameters needed for IG publishing. |
| [Test Scenario (DAK)](StructureDefinition-TestScenario.md) | Logical Model for representing Test Scenarios from a DAK. A set of test scenarios to validate an implementation of the DAK. |
| [Test Scenario Source](StructureDefinition-TestScenarioSource.md) | Source reference for Test Scenario - exactly one of the following must be provided:* url (url data type): URL to retrieve TestScenario definition from input/ or external source
* canonical (canonical data type): Canonical URI pointing to the TestScenario definition
* instance: Inline TestScenario instance data
 |
| [User Scenario (DAK)](StructureDefinition-UserScenario.md) | Logical Model for representing User Scenarios from a DAK. Narratives that describe how the different personas may interact with each other. |
| [User Scenario Source](StructureDefinition-UserScenarioSource.md) | Source reference for User Scenario - exactly one of the following must be provided:* url (url data type): URL to retrieve UserScenario definition from input/ or external source
* canonical (canonical data type): Canonical URI pointing to the UserScenario definition
* instance: Inline UserScenario instance data
 |

### Structures: Questionnaires 

These define forms used by systems conforming to this implementation guide to capture or expose data to end users.

| | |
| :--- | :--- |
| [Questionnaire for IMMZ.D2 Determine required vaccination(s) if any](Questionnaire-DAK.DT.IMMZ.D2.DT.BCGQuestionnaire.md) | Auto-generated questionnaire for decision table DAK.DT.IMMZ.D2.DT.BCG |

### Structures: Resource Profiles 

These define constraints on FHIR resources for systems conforming to this implementation guide.

| | |
| :--- | :--- |
| [SMART Guidelines Communication Request](StructureDefinition-SGCommunicationRequest.md) | Provide communication |
| [SMART Guidelines Decision Table](StructureDefinition-SGDecisionTable.md) | Defines the minimum expectations for PlanDefinition resources used in SMART Guidelines which are derived from DAK Decision Tables |
| [SMART Guidelines Requirements](StructureDefinition-SGRequirements.md) | Smart Guidelines Requirements |

### Structures: Extension Definitions 

These define constraints on FHIR data types for systems conforming to this implementation guide.

| | |
| :--- | :--- |
| [LinkIdExt](StructureDefinition-LinkIdExt.md) | Smart Guidelines link identifier extension |
| [Markdown](StructureDefinition-Markdown.md) | Markdown extension |
| [SGActorExt](StructureDefinition-SGActorExt.md) | Smart Guidelines Actor Reference extension |
| [SGDocumentation](StructureDefinition-SGDocumentation.md) | Smart Guidelines Documentation extension |
| [SGMarkdown](StructureDefinition-SGMarkdown.md) | Smart Guidelines markdown extension |
| [SGRequirementExt](StructureDefinition-SGRequirementExt.md) | Smart Guidelines Requirements extension |
| [SGString](StructureDefinition-SGString.md) | Smart Guidelines (required) string extension for use in a complex extension. Retired: SGUserStory now uses inline `capability` and `benefit` sub-extensions, because two slices of one extension definition cannot be told apart. |
| [SGTask](StructureDefinition-SGTask.md) | Extension to reference SMART Guidelines task type |
| [SGUserStory](StructureDefinition-SGUserStory.md) | Smart Guidelines extension to support structured User Stories (As a `Actor` I want to `capability` so that `benefit`) extension |
| [SGcode](StructureDefinition-SGcode.md) | Smart Guidelines code extension |
| [Satisfies](StructureDefinition-Satisfies.md) | Indicates that if the conditions for this requirement are satisified, then that it should be viewed as satisifying the referenced requirement. |

### Terminology: Value Sets 

These define sets of codes used by systems conforming to this implementation guide.

| | |
| :--- | :--- |
| [Classification of Digital Health Interventions v1](ValueSet-CDHIv1.md) | Value Set for Classification of Digital Health Interventions v1. Autogenerated from DAK artifacts |
| [Classification of Digital Health Interventions v2](ValueSet-CDHIv2.md) | Value Set for the Classification of Digital Interventions, Services and Applications in Health (CDISAH), second edition (2023). |
| [Core Data Element Type Value Set](ValueSet-CoreDataElementTypeVS.md) | Value set of core data element types |
| [Digital Health Interventions for Clients](ValueSet-CDHIv1.1.md) | Digital Health Interventions whose primary user group is Clients (persons using health services). Group 1 of the Classification of Digital Health Interventions v1 (2018). |
| [Digital Health Interventions for Health Management and Support Personnel](ValueSet-CDHIv2.3.md) | Digital Health Interventions whose primary user group is Health Management and Support Personnel. Group 3 of the Classification of Digital Interventions, Services and Applications in Health v2 (CDISAH, 2023). |
| [Digital Health Interventions for Health System Managers](ValueSet-CDHIv1.3.md) | Digital Health Interventions whose primary user group is Health System Managers. Group 3 of the Classification of Digital Health Interventions v1 (2018). |
| [Digital Health Interventions for Health Workers](ValueSet-CDHIv1.2.md) | Digital Health Interventions whose primary user group is Health Workers. Group 2 of the Classification of Digital Health Interventions v1 (2018). |
| [Digital Health Interventions for Healthcare Providers](ValueSet-CDHIv2.2.md) | Digital Health Interventions whose primary user group is Healthcare Providers. Group 2 of the Classification of Digital Interventions, Services and Applications in Health v2 (CDISAH, 2023). |
| [Digital Health Interventions for Persons](ValueSet-CDHIv2.1.md) | Digital Health Interventions whose primary user group is Persons (health service users). Group 1 of the Classification of Digital Interventions, Services and Applications in Health v2 (CDISAH, 2023). |
| [Digital Health Interventions: Data Services](ValueSet-CDHIv1.4.md) | Crosscutting Data Services DHIs. Group 4 of the Classification of Digital Health Interventions v1 (2018). |
| [Digital Health Interventions: Data Services](ValueSet-CDHIv2.4.md) | Crosscutting Data Services DHIs. Group 4 of the Classification of Digital Interventions, Services and Applications in Health v2 (CDISAH, 2023). |
| [Health System Challenges](ValueSet-CDSCv1.md) | Value set for Health System Challenges (Classification of Digital Health System Categories v1, 2018). Includes all 25 system category codes (A–Y). |
| [ISCO-08 Value Set](ValueSet-ISCO08ValueSet.md) | Extensible value set of ISCO-08 codes for persona classification |
| [Knowledge graph L1: certainty](ValueSet-KGCertaintyVS.md) | All codes of KGCertainty. |
| [Knowledge graph L1: change status](ValueSet-KGChangeStatusVS.md) | All codes of KGChangeStatus. |
| [Knowledge graph L1: citation kind](ValueSet-KGCitationKindVS.md) | All codes of KGCitationKind. |
| [Knowledge graph L1: classes](ValueSet-KGL1ClassesVS.md) | All codes of KGL1Classes. |
| [Knowledge graph L1: element type](ValueSet-KGElementTypeVS.md) | All codes of KGElementType. |
| [Knowledge graph L1: evidence type](ValueSet-KGEvidenceTypeVS.md) | All codes of KGEvidenceType. |
| [Knowledge graph L1: grc status](ValueSet-KGGrcStatusVS.md) | All codes of KGGrcStatus. |
| [Knowledge graph L1: identifier type](ValueSet-KGIdentifierTypeVS.md) | All codes of KGIdentifierType. |
| [Knowledge graph L1: intervention type](ValueSet-KGInterventionTypeVS.md) | All codes of KGInterventionType. |
| [Knowledge graph L1: outcome importance](ValueSet-KGOutcomeImportanceVS.md) | All codes of KGOutcomeImportance. |
| [Knowledge graph L1: predicates](ValueSet-KGL1PredicatesVS.md) | All codes of KGL1Predicates. |
| [Knowledge graph L1: publication type](ValueSet-KGPublicationTypeVS.md) | All codes of KGPublicationType. |
| [Knowledge graph L1: recommendation direction](ValueSet-KGRecommendationDirectionVS.md) | All codes of KGRecommendationDirection. |
| [Knowledge graph L1: recommendation kind](ValueSet-KGRecommendationKindVS.md) | All codes of KGRecommendationKind. |
| [Knowledge graph L1: recommendation status](ValueSet-KGRecommendationStatusVS.md) | All codes of KGRecommendationStatus. |
| [Knowledge graph L1: recommendation strength](ValueSet-KGRecommendationStrengthVS.md) | All codes of KGRecommendationStrength. |
| [Knowledge graph L1: remark type](ValueSet-KGRemarkTypeVS.md) | All codes of KGRemarkType. |
| [Knowledge graph L1: resolution status](ValueSet-KGResolutionStatusVS.md) | All codes of KGResolutionStatus. |
| [Knowledge graph L1: row type](ValueSet-KGRowTypeVS.md) | All codes of KGRowType. |
| [Knowledge graph L1: terminology system](ValueSet-KGTerminologySystemVS.md) | All codes of KGTerminologySystem. |
| [Knowledge graph L1Library: classes](ValueSet-KGL1LibraryClassesVS.md) | All codes of KGL1LibraryClasses. |
| [Knowledge graph L1Library: predicates](ValueSet-KGL1LibraryPredicatesVS.md) | All codes of KGL1LibraryPredicates. |
| [Knowledge graph L2-BPMN: gateway direction](ValueSet-KGGatewayDirectionVS.md) | All codes of KGGatewayDirection. |
| [Knowledge graph L2-DMN: dmn entry kind](ValueSet-KGDmnEntryKindVS.md) | All codes of KGDmnEntryKind. |
| [Knowledge graph L2: artifact kind](ValueSet-KGArtifactKindVS.md) | All codes of KGArtifactKind. |
| [Knowledge graph L2: classes](ValueSet-KGL2ClassesVS.md) | All codes of KGL2Classes. |
| [Knowledge graph L2: conformance expectation](ValueSet-KGConformanceExpectationVS.md) | All codes of KGConformanceExpectation. |
| [Knowledge graph L2: predicates](ValueSet-KGL2PredicatesVS.md) | All codes of KGL2Predicates. |
| [Knowledge graph L2: publication status](ValueSet-KGPublicationStatusVS.md) | All codes of KGPublicationStatus. |
| [Knowledge graph L2: verification method](ValueSet-KGVerificationMethodVS.md) | All codes of KGVerificationMethod. |
| [Knowledge graph L2BPMN: classes](ValueSet-KGL2BPMNClassesVS.md) | All codes of KGL2BPMNClasses. |
| [Knowledge graph L2BPMN: predicates](ValueSet-KGL2BPMNPredicatesVS.md) | All codes of KGL2BPMNPredicates. |
| [Knowledge graph L2DMN: classes](ValueSet-KGL2DMNClassesVS.md) | All codes of KGL2DMNClasses. |
| [Knowledge graph L2DMN: predicates](ValueSet-KGL2DMNPredicatesVS.md) | All codes of KGL2DMNPredicates. |
| [Knowledge graph L3: classes](ValueSet-KGL3ClassesVS.md) | All codes of KGL3Classes. |
| [Knowledge graph L3: predicates](ValueSet-KGL3PredicatesVS.md) | All codes of KGL3Predicates. |
| [Knowledge graph L3: structure definition kind](ValueSet-KGStructureDefinitionKindVS.md) | All codes of KGStructureDefinitionKind. |
| [Knowledge graph: derivation](ValueSet-KGDerivationVS.md) | All codes of KGDerivation. |
| [SMART Guidelines Authoring Persona Types ValueSet](ValueSet-SGAuthoringPersonaTypesVS.md) | ValueSet for SMART Guidelines authoring persona types |
| [SMART Guidelines Authoring Skills ValueSet](ValueSet-SGAuthoringSkillsVS.md) | ValueSet for all SMART Guidelines authoring skill capabilities |
| [Services and Application Types](ValueSet-CDSCv2.md) | Value set for Services and Application Types (Classification of Digital Health Services and Application Types v2, CDISAH 2023). Includes all codes across the five architecture groups (A–E). |
| [Services and Application Types: Data Management Services](ValueSet-CDSCv2.D.md) | Services and systems that support the collection, aggregation, storage, analysis, and exchange of health data. Group D of the Classification of Digital Health Services and Application Types v2 (CDISAH, 2023). |
| [Services and Application Types: Health System/Provider Administration](ValueSet-CDSCv2.B.md) | Systems that support the administrative and managerial functions of health systems and healthcare organisations. Group B of the Classification of Digital Health Services and Application Types v2 (CDISAH, 2023). |
| [Services and Application Types: Point of Service](ValueSet-CDSCv2.A.md) | Systems that facilitate the provision and delivery of healthcare services to persons at the point of care. Group A of the Classification of Digital Health Services and Application Types v2 (CDISAH, 2023). |
| [Services and Application Types: Registries and Directories](ValueSet-CDSCv2.C.md) | Systems that create, maintain, and provide authoritative master records for persons, providers, facilities, products and health events. Group C of the Classification of Digital Health Services and Application Types v2 (CDISAH, 2023). |
| [Services and Application Types: Surveillance and Response](ValueSet-CDSCv2.E.md) | Systems that support the detection, monitoring, and response to disease outbreaks and public health threats. Group E of the Classification of Digital Health Services and Application Types v2 (CDISAH, 2023). |
| [Smart Guidelines Decision Table Actions](ValueSet-DecisionTableActions.md) | Value Set for Smart Guidelines Documentation Decision Table Actions |
| [Smart Guidelines Documentation Section](ValueSet-DocumentationSection.md) | Value Set for Smart Guidelines Documentation Section to autogenerate documentation from artifacts |
| [Smart Guidelines Persona Types Value Set](ValueSet-SGPersonaTypesVS.md) | Value Set for Smart Guidelines Persona Section to autogenerate documentation from artifacts |

### Terminology: Code Systems 

These define new code systems used by systems conforming to this implementation guide.

| | |
| :--- | :--- |
| [Classification of Digital Health Interventions v1](CodeSystem-CDHIv1.md) | CodeSystem for Classification of Digital Health Interventions v1. Autogenerated from DAK artifacts |
| [Classification of Digital Health Interventions v2](CodeSystem-CDHIv2.md) | CodeSystem for the Classification of Digital Interventions, Services and Applications in Health (CDISAH), second edition (2023). ISBN 978-92-4-008194-9.Organised into four groups based on the primary user:1. Persons
1. Healthcare providers
1. Health management and support personnel
1. Data services
New categories vs v1: 1.4.4, 1.6.2, 1.8, 2.5.6, 2.11, 3.1.5, 3.5.7, 3.5.8, 3.8, 4.3.5, 4.4.2, 4.4.3, 4.5. See ConceptMap CDHIv1toCDHIv2 for the full mapping from the first edition. |
| [Classification of Digital Health Services and Application Types v2](CodeSystem-CDSCv2.md) | CodeSystem for the Classification of Digital Health Services and Application Types v2, as defined in the Classification of Digital Interventions, Services and Applications in Health (CDISAH), second edition (2023). ISBN 978-92-4-008194-9.Services and Application Types represent the types of software, ICT systems and services or communication channels that deliver or execute digital health interventions (DHIs) and health content.The types are organised into five representations within the Digital Health Architecture: A. Point of service B. Health system/Provider administration C. Registries and Directories D. Data Management services E. Surveillance and Response |
| [Classification of Digital Health System Categories v1](CodeSystem-CDSCv1.md) | CodeSystem for Classification of Digital Health System Categories v1. Autogenerated from DAK artifacts |
| [Core Data Element Type](CodeSystem-CoreDataElementType.md) | CodeSystem for Core Data Element types - defines the type of FHIR resource that a Core Data Element references. |
| [International Standard Classification of Occupations 2008](CodeSystem-ISCO08.md) | ISCO-08 codes from the International Labour Organization official classification |
| [Knowledge graph L1: certainty](CodeSystem-KGCertainty.md) | GRADE certainty of evidence. The 2014 handbook calls it quality of evidence and names certainty as a synonym (§9.1). Rated per outcome on evidence; the overall certainty on a recommendation is the lowest across its critical outcomes (§9.6). Source: smart-kg ontology/l1/l1.json valueSets "certainty"; WHO handbook for guideline development (2014) §9.1, §9.5–9.6. |
| [Knowledge graph L1: change status](CodeSystem-KGChangeStatus.md) | Whether this edition of a consolidated guideline introduces, updates or carries a recommendation or indicator unchanged. Printed as NEW / UPDATE tags. Source: smart-kg ontology/l1/l1.json valueSets "change-status"; Consolidated guidelines on person-centred HIV strategic information (2022), summary recommendations; handbook §1.7.2. |
| [Knowledge graph L1: citation kind](CodeSystem-KGCitationKind.md) | Whether a citation string names a source, or stands in for one that is missing. Source: smart-kg ontology/l1/l1.json valueSets "citation-kind"; IMMZ DAK indicators workbook: '[Add appropriate reference]'. |
| [Knowledge graph L1: classes](CodeSystem-KGL1Classes.md) | The classes of the L1 layer of the SMART Guidelines knowledge graph. A node's `type` is one of these. Source: smart-base/L1/schemas/L1.ts (migrated from smart-kg ontology/L1/L1.json). |
| [Knowledge graph L1: element type](CodeSystem-KGElementType.md) | What kind of printed block a publication element is. Source: smart-kg ontology/l1/l1.json valueSets "element-type"; Observed in the ANC and HIV SI guidelines and the immunization summary tables. |
| [Knowledge graph L1: evidence type](CodeSystem-KGEvidenceType.md) | Which kind of evidence a row is, and so which scale its certainty is on: GRADE for effects, GRADE-CERQual for qualitative findings. Source: smart-kg ontology/l1/l1.json valueSets "evidence-type"; ANC guideline (2016) methods (GRADE and GRADE-CERQual). |
| [Knowledge graph L1: grc status](CodeSystem-KGGrcStatus.md) | Whether the Guideline Review Committee approved the publication. All WHO publications containing recommendations must be approved (handbook §1.10.1); a consolidated guideline whose recommendations were all previously approved and unchanged does not require review (§1.7.2). Absent means not recorded — not the same as not reviewed. Source: smart-kg ontology/l1/l1.json valueSets "grc-status"; WHO handbook for guideline development (2014), §1.7.2, §1.10.1. |
| [Knowledge graph L1: identifier type](CodeSystem-KGIdentifierType.md) | Which kind of identifier a publication carries. The first available, in this order, builds the publication IRI. url comes last: a web address is the least stable identifier and is used only for sources that have no other. Source: smart-kg ontology/l1/l1.json valueSets "identifier-type"; WHO IRIS practice; CDHIv2.fsh carries an ISBN. |
| [Knowledge graph L1: intervention type](CodeSystem-KGInterventionType.md) | DRAFT. What kind of intervention a recommendation or catalogued intervention concerns. To be aligned with the UHC Compendium's categories once checked. Source: smart-kg ontology/l1/l1.json valueSets "intervention-type"; WHO handbook §1.7.1 (clinical, health system, public health, diagnostic, surveillance); digital interventions per CDHI. |
| [Knowledge graph L1: outcome importance](CodeSystem-KGOutcomeImportance.md) | How the guideline development group rated an outcome on the 1–9 scale: 7–9 critical, 4–6 important. Unimportant outcomes are not carried into evidence profiles, so they have no code here. Source: smart-kg ontology/l1/l1.json valueSets "outcome-importance"; WHO handbook for guideline development (2014) §7.6, Fig. 7.1. |
| [Knowledge graph L1: predicates](CodeSystem-KGL1Predicates.md) | The predicates of the L1 layer. An edge's `predicate` is one of these; which (source, target) pairs each licenses is the layer's edge table. Source: smart-base/L1/schemas/L1.ts (migrated from smart-kg ontology/L1/L1.json). |
| [Knowledge graph L1: publication type](CodeSystem-KGPublicationType.md) | What kind of publication this is. The distinction that matters most for provenance is guideline versus not: a summary table or position paper restates recommendations made elsewhere, and a §1.9 product makes none of its own. Conflating them makes a citation resolve to the wrong authority. Source: smart-kg ontology/l1/l1.json valueSets "publication-type"; WHO handbook for guideline development (2014), Table 1.2 and §1.7–1.9; the BCG decision table's citation for summary-table; CDHIv2.fsh for classification. |
| [Knowledge graph L1: recommendation direction](CodeSystem-KGRecommendationDirection.md) | For or against. The handbook prefers "we recommend against X" to "X is not recommended", which is ambiguous between against and no recommendation (§10.6). Source: smart-kg ontology/l1/l1.json valueSets "recommendation-direction"; WHO handbook for guideline development (2014) §10.1, §10.6. |
| [Knowledge graph L1: recommendation kind](CodeSystem-KGRecommendationKind.md) | What sort of normative statement this is. Grading is optional: ANC 2016 prints a direction ('Recommended', 'Not recommended') and no GRADE strength. A strength always needs a direction. A good practice statement and a no-recommendation carry no strength or certainty, and a no-recommendation carries no direction. Source: smart-kg ontology/l1/l1.json valueSets "recommendation-kind"; WHO handbook §10.4, §10.7; ANC guideline (2016) Table 1, verified; Guyatt et al. 2016 on good practice statements. |
| [Knowledge graph L1: recommendation status](CodeSystem-KGRecommendationStatus.md) | Whether a recommendation is still in force. Recommendations in one guideline go out of date at different times (§1.7.2), and a department that doubts a recommendation's validity should say so before the update is done (§12.5.4). This is what impact analysis filters on. Source: smart-kg ontology/l1/l1.json valueSets "recommendation-status"; WHO handbook for guideline development (2014) §1.7.2, §12.5. |
| [Knowledge graph L1: recommendation strength](CodeSystem-KGRecommendationStrength.md) | GRADE strength. Strength is not certainty: a strong recommendation can rest on low-certainty evidence and a conditional one on high. Record "weak" as conditional; the handbook treats them as synonyms (§10.4). Source: smart-kg ontology/l1/l1.json valueSets "recommendation-strength"; WHO handbook for guideline development (2014) §10.4. |
| [Knowledge graph L1: remark type](CodeSystem-KGRemarkType.md) | What a remark is for. Grounded in the six remarks attached to ANC recommendation A.1.1. Source: smart-kg ontology/l1/l1.json valueSets "remark-type"; ANC guideline (2016) p. 15; handbook §10.6, §10.8. |
| [Knowledge graph L1: resolution status](CodeSystem-KGResolutionStatus.md) | Whether a citation string has been matched to what it cites. `ambiguous` is a legitimate terminal state — two publications with similar titles is a question for a person — and must not be collapsed to resolved. Source: smart-kg ontology/l1/l1.json valueSets "resolution-status"; docs/SCOPE.md. |
| [Knowledge graph L1: row type](CodeSystem-KGRowType.md) | The role of a row within a table. Source: smart-kg ontology/l1/l1.json valueSets "row-type"; HIV SI guideline Table 2.3; ANC Table 1. |
| [Knowledge graph L1: terminology system](CodeSystem-KGTerminologySystem.md) | Code systems a DAK is expected to use. An unknown system is a warning, because a misspelt system silently breaks joins across guidelines. Source: smart-kg ontology/l1/l1.json valueSets "terminology-system"; smart-base input/fsh/profiles/SGLogicalModel.fsh and Aliases.fsh; UHC Compendium; CDHIv2.fsh. |
| [Knowledge graph L1Library: classes](CodeSystem-KGL1LibraryClasses.md) | The classes of the L1Library layer of the SMART Guidelines knowledge graph. A node's `type` is one of these. Source: smart-base/L1/schemas/l1-library.ts (migrated from smart-kg ontology/l1-library/l1-library.json). |
| [Knowledge graph L1Library: predicates](CodeSystem-KGL1LibraryPredicates.md) | The predicates of the L1Library layer. An edge's `predicate` is one of these; which (source, target) pairs each licenses is the layer's edge table. Source: smart-base/L1/schemas/l1-library.ts (migrated from smart-kg ontology/l1-library/l1-library.json). |
| [Knowledge graph L2-BPMN: gateway direction](CodeSystem-KGGatewayDirection.md) | BPMN 2.0's gatewayDirection. Added by the smart-base migration: smart-kg named the property without binding it. Source: smart-kg ontology/l2-bpmn/l2-bpmn.json valueSets "gateway-direction"; OMG BPMN 2.0.2, Gateway.gatewayDirection. |
| [Knowledge graph L2-DMN: dmn entry kind](CodeSystem-KGDmnEntryKind.md) | Which DMN element type a column's cells are serialised as. Added by the smart-base migration from smart-kg's propertyNote, which named the two values in prose. Source: smart-kg ontology/l2-dmn/l2-dmn.json valueSets "dmn-entry-kind"; OMG DMN 1.3, DecisionRule.outputEntry and annotationEntry. |
| [Knowledge graph L2: artifact kind](CodeSystem-KGArtifactKind.md) | What kind of file an external artefact is. Moved with the class from L1, where it was free text. Source: smart-kg ontology/l2/l2.json valueSets "artifact-kind"; Files observed in smart-base and in WHO's immunizations DAK (canonical http://smart.who.int/immunizations). |
| [Knowledge graph L2: classes](CodeSystem-KGL2Classes.md) | The classes of the L2 layer of the SMART Guidelines knowledge graph. A node's `type` is one of these. Source: smart-base/L1/schemas/L2.ts (migrated from smart-kg ontology/L2/L2.json). |
| [Knowledge graph L2: conformance expectation](CodeSystem-KGConformanceExpectation.md) | The conformance verb of a requirement statement. Added by the smart-base migration from smart-kg's propertyNote, which named the four values in prose. Source: smart-kg ontology/l2/l2.json valueSets "conformance-expectation"; http://hl7.org/fhir/ValueSet/conformance-expectation. |
| [Knowledge graph L2: predicates](CodeSystem-KGL2Predicates.md) | The predicates of the L2 layer. An edge's `predicate` is one of these; which (source, target) pairs each licenses is the layer's edge table. Source: smart-base/L1/schemas/L2.ts (migrated from smart-kg ontology/L2/L2.json). |
| [Knowledge graph L2: publication status](CodeSystem-KGPublicationStatus.md) | FHIR PublicationStatus, which DAK.fsh's status and every L3 resource's status take. Added by the smart-base migration: smart-kg named these properties without binding them. Source: smart-kg ontology/l2/l2.json valueSets "publication-status"; http://hl7.org/fhir/ValueSet/publication-status. |
| [Knowledge graph L2: verification method](CodeSystem-KGVerificationMethod.md) | How a success criterion is verified: the classic verification methods, the same field name and codes as folio-assistant's requirement.ts `successCriteria`, so the two map 1:1. From litlfred/smart-kg main (folio-assistant#2406). Source: smart-kg ontology/l2/l2.json valueSets "verification-method"; folio-assistant-core schemas requirement.ts successCriteria.verification. |
| [Knowledge graph L2BPMN: classes](CodeSystem-KGL2BPMNClasses.md) | The classes of the L2BPMN layer of the SMART Guidelines knowledge graph. A node's `type` is one of these. Source: smart-base/L1/schemas/L2-BPMN.ts (migrated from smart-kg ontology/L2-BPMN/L2-BPMN.json). |
| [Knowledge graph L2BPMN: predicates](CodeSystem-KGL2BPMNPredicates.md) | The predicates of the L2BPMN layer. An edge's `predicate` is one of these; which (source, target) pairs each licenses is the layer's edge table. Source: smart-base/L1/schemas/L2-BPMN.ts (migrated from smart-kg ontology/L2-BPMN/L2-BPMN.json). |
| [Knowledge graph L2DMN: classes](CodeSystem-KGL2DMNClasses.md) | The classes of the L2DMN layer of the SMART Guidelines knowledge graph. A node's `type` is one of these. Source: smart-base/L1/schemas/L2-DMN.ts (migrated from smart-kg ontology/L2-DMN/L2-DMN.json). |
| [Knowledge graph L2DMN: predicates](CodeSystem-KGL2DMNPredicates.md) | The predicates of the L2DMN layer. An edge's `predicate` is one of these; which (source, target) pairs each licenses is the layer's edge table. Source: smart-base/L1/schemas/L2-DMN.ts (migrated from smart-kg ontology/L2-DMN/L2-DMN.json). |
| [Knowledge graph L3: classes](CodeSystem-KGL3Classes.md) | The classes of the L3 layer of the SMART Guidelines knowledge graph. A node's `type` is one of these. Source: smart-base/L1/schemas/L3.ts (migrated from smart-kg ontology/L3/L3.json). |
| [Knowledge graph L3: predicates](CodeSystem-KGL3Predicates.md) | The predicates of the L3 layer. An edge's `predicate` is one of these; which (source, target) pairs each licenses is the layer's edge table. Source: smart-base/L1/schemas/L3.ts (migrated from smart-kg ontology/L3/L3.json). |
| [Knowledge graph L3: structure definition kind](CodeSystem-KGStructureDefinitionKind.md) | FHIR StructureDefinitionKind. Added by the smart-base migration: smart-kg named the property without binding it. Source: smart-kg ontology/l3/l3.json valueSets "structure-definition-kind"; http://hl7.org/fhir/ValueSet/structure-definition-kind. |
| [Knowledge graph: derivation](CodeSystem-KGDerivation.md) | How a node or edge of a SMART Guidelines knowledge graph came to be. Every node and edge is exactly one of the three, and `decided` is the one a reviewer needs to find. Source: smart-kg shapes/recommendation-graph.schema.json $defs.derivation. |
| [SMART Guidelines Authoring Persona Types](CodeSystem-SGAuthoringPersonaTypes.md) | CodeSystem for SMART Guidelines authoring persona types. These represent roles involved in the authoring, review, and publication of SMART Guidelines and Digital Adaptation Kits, as distinct from the clinical/health personas defined within a DAK. |
| [SMART Guidelines Authoring Skills](CodeSystem-SGAuthoringSkills.md) | CodeSystem for SMART Guidelines authoring skill capabilities. Each code represents a discrete skill that an authoring persona may possess. Skills are used to define Requirements resources as capability statements. |
| [SMART Guidelines Persona Types](CodeSystem-SGPersonaTypes.md) | CodeSystem for SMART Guidelines Persona Types |
| [SMART Guidelines Tasks](CodeSystem-SGTasks.md) | CodeSystem for SMART Guidelines tasks which are specializations of the Business Process Modeling Notatiton (BPMN) tasks, which are included in this codesystemSee [BPMN Spectification](https://www.omg.org/spec/BPMN) for more info. The descriptions were adapted from the [normative human readable documentation](https://www.omg.org/spec/BPMN/2.0.2/PDF). |
| [Smart Guidelines Actions (columns) for Decision Tables](CodeSystem-DecisionTableActions.md) | CodeSystem for Smart Guidelines Documentation Actions for Decision Tables" |
| [Smart Guidelines Documentation Section](CodeSystem-DocumentationSections.md) | CodeSystem for Smart Guidelines Documentation Section to autogenerate documentation from artifacts |

### Terminology: Concept Maps 

These define transformations to convert between codes by systems conforming with this implementation guide.

| | |
| :--- | :--- |
| [Hierarchy of the Classification of Digital Health Interventions v1](ConceptMap-CDHIv1Hierarchy.md) | Mapping to represent hierarchy within the Classification of Digital Health Interventions v1. |
| [Hierarchy of the Classification of Digital Health Interventions v2](ConceptMap-CDHIv2Hierarchy.md) | Mapping to represent hierarchy within the Classification of Digital Interventions, Services and Applications in Health (CDISAH) v2. |
| [Mapping from CDHI v1 to CDISAH v2](ConceptMap-CDHIv1toCDHIv2.md) | Mapping from the Classification of Digital Health Interventions v1 (CDHI v1, 2018) to the Classification of Digital Interventions, Services and Applications in Health v2 (CDISAH v2, 2023).Key structural changes reflected in this map:* User group labels updated throughout (e.g. 'Clients' → 'Persons', 'Health workers' → 'Healthcare providers', 'Health system managers' → 'Health management and support personnel').
* Civil Registration and Vital Statistics (CRVS) consolidated: six v1 codes (3.4.1–3.4.6) merged into two v2 codes (3.4.1, 3.4.2).
* Health financing section restructured: v1 3.5.1 (insurance membership) and 3.5.2 (billing) updated; v1 3.5.3–3.5.6 shifted by one (now 3.5.4–3.5.6 + new 3.5.3).
* Data services (group 4) substantially revised: 4.1.1 changed scope, 4.3 expanded from 4 to 5 codes, 4.4 split from 1 to 3 codes, 4.5 is entirely new.
* New v2 categories with no v1 equivalent are listed as 'unmatched' targets.
 |
| [Mapping from CDSC v1 to Services and Application Types v2](ConceptMap-CDSCv1toCDSCv2.md) | Mapping from the Classification of Digital Health System Categories v1 (CDSCv1, 2018) to the Classification of Digital Health Services and Application Types v2 (CDSCv2, 2023).The v1 used 25 single-letter codes (A–Y). The v2 completely restructured this into 5 representations within the digital health enterprise architecture, each with alphanumeric codes (A1–A9, B1–B8, C1–C11, D1–D8, E1–E2).Several new v2 categories have no v1 equivalent: A3 (Decision support), A4 (Diagnostics), B1 (Blood bank), B3 (Health program monitoring), B7 (Patient administration), C4 (Facility registries), C5 (Health worker registry), C7 (Immunisation information), C8 (Master patient index), C9 (Product catalogues), C10 (Public Key directories), D1 (Analytics), D3 (Data warehouses). |

