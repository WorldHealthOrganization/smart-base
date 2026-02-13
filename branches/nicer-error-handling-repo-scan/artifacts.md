# Artifacts Summary - SMART Base v0.2.0

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
| [Core Data Element (DAK)](StructureDefinition-CoreDataElement.md) | Logical Model for representing Core Data Elements from a DAK. Data elements are required throughout the different points of a workflow and are mapped to established concept mapping standards. |
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
| [SGString](StructureDefinition-SGString.md) | Smart Guidelines (required) string extension for use in a complex extension |
| [SGTask](StructureDefinition-SGTask.md) | Extension to reference SMART Guidelines task type |
| [SGUserStory](StructureDefinition-SGUserStory.md) | Smart Guidelines extension to support structured User Stories (As a <Actor> I want to <capability> so that <benfit>) extension |
| [SGcode](StructureDefinition-SGcode.md) | Smart Guidelines code extension |
| [Satisfies](StructureDefinition-Satisfies.md) | Indicates that if the conditions for this requirement are satisified, then that it should be viewed as satisifying the referenced requirement. |

### Terminology: Value Sets 

These define sets of codes used by systems conforming to this implementation guide.

| | |
| :--- | :--- |
| [Classification of Digital Health Interventions v1](ValueSet-CDHIv1.md) | Value Set for Classification of Digital Health Interventions v1. Autogenerated from DAK artifacts |
| [Classification of Digital Health System Categories v1](ValueSet-CDSCv1.md) | Value Set for Classification of Digital Health System Categories v1. Autogenerated from DAK artifacts |
| [ISCO-08 Value Set](ValueSet-ISCO08ValueSet.md) | Extensible value set of ISCO-08 codes for persona classification |
| [Smart Guidelines Decision Table Actions](ValueSet-DecisionTableActions.md) | Value Set for Smart Guidelines Documentation Decision Table Actions |
| [Smart Guidelines Documentation Section](ValueSet-DocumentationSection.md) | Value Set for Smart Guidelines Documentation Section to autogenerate documentation from artifacts |
| [Smart Guidelines Persona Types Value Set](ValueSet-SGPersonaTypesVS.md) | Value Set for Smart Guidelines Persona Section to autogenerate documentation from artifacts |

### Terminology: Code Systems 

These define new code systems used by systems conforming to this implementation guide.

| | |
| :--- | :--- |
| [Classification of Digital Health Interventions v1](CodeSystem-CDHIv1.md) | CodeSystem for Classification of Digital Health Interventions v1. Autogenerated from DAK artifacts |
| [Classification of Digital Health System Categories v1](CodeSystem-CDSCv1.md) | CodeSystem for Classification of Digital Health System Categories v1. Autogenerated from DAK artifacts |
| [International Standard Classification of Occupations 2008](CodeSystem-ISCO08.md) | ISCO-08 codes from the International Labour Organization official classification |
| [SMART Guidelines Persona Types](CodeSystem-SGPersonaTypes.md) | CodeSystem for SMART Guidelines Persona Types |
| [SMART Guidelines Tasks](CodeSystem-SGTasks.md) | CodeSystem for SMART Guidelines tasks which are specializations of the Business Process Modeling Notatiton (BPMN) tasks, which are included in this codesystemSee[BPMN Spectification](https://www.omg.org/spec/BPMN)for more info. The descriptions were adapted from the[normative human readable documentation](https://www.omg.org/spec/BPMN/2.0.2/PDF). |
| [Smart Guidelines Actions (columns) for Decision Tables](CodeSystem-DecisionTableActions.md) | CodeSystem for Smart Guidelines Documentation Actions for Decision Tables" |
| [Smart Guidelines Documentation Section](CodeSystem-DocumentationSections.md) | CodeSystem for Smart Guidelines Documentation Section to autogenerate documentation from artifacts |

### Terminology: Concept Maps 

These define transformations to convert between codes by systems conforming with this implementation guide.

| | |
| :--- | :--- |
| [Hierarchy of the Classification of Digital Health Interventions v1](ConceptMap-CDHIv1Hierarchy.md) | Mapping to represent hierarchy within Hierarchy of the Classification of Digital Health Interventions v1. |

