# Home - SMART Base v0.2.0

* [**Table of Contents**](toc.md)
* **Home**

## Home

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/ImplementationGuide/smart.who.int.base | *Version*:0.2.0 |
| Draft as of 2026-03-06 | *Computable Name*:Base |

### Overview

**WHO SMART Guidelines** (Standards-based, Machine-readable, Adaptive, Requirements-based, and Testable) are a set of WHO clinical guidelines that have been transformed into a computable, interoperable format. They enable countries to rapidly adopt, adapt, and implement WHO recommendations within their digital health systems by providing structured, machine-readable clinical content.

A **Digital Adaptation Kit (DAK)** is the primary artefact of WHO SMART Guidelines. It is a structured, standardised package of clinical and operational content that represents a WHO health intervention in a computable form. Each DAK contains:

* **Health interventions and recommendations** – the clinical guidance from WHO
* **Generic personas** – representative end-users and actors in the health system
* **User scenarios** – narrative descriptions of how the guidance is used in practice
* **Business processes and workflows** – step-by-step care pathways
* **Core data elements** – the data dictionary for the health domain
* **Decision-support logic** – computable clinical decision rules
* **Functional and non-functional requirements** – system capability requirements
* **Program indicators** – aggregate measures and metrics for monitoring and evaluation
* **Test scenarios** – structured tests to validate conformance

The diagram below illustrates the nine components of a WHO DAK and how they relate to one another:

Figure 1 – The nine components of a WHO Digital Adaptation Kit (DAK)
This implementation guide contains base conformance resources for use in all WHO SMART Guidelines implementation guides.

See the [SMART IG Starter Kit](https://smart.who.int/ig-starter-kit/) for more information on building and using WHO SMART Guidelines.

### DAK (Digital Adaptation Kit) URL Handling

For repositories that contain a `dak.json` file in the root directory, this implementation guide provides enhanced URL handling for publication and preview scenarios:

#### Publication URLs

* **WHO Repositories**: For repositories owned by `WorldHealthOrganization`, the publication URL follows the pattern `https://smart.who.int/{stub}` where `{stub}` is the repository name with any `smart-` prefix removed.
* **Other Repositories**: Use the canonical URL specified in `sushi-config.yaml` or fall back to GitHub Pages pattern.

#### Preview URLs

* **All Repositories**: Preview URLs use the GitHub Pages pattern `https://{profile}.github.io/{repo}` for current CI builds.

#### Branch-Based URL Selection

* **Release Branches** (prefixed with `release-`): Use publication URLs for canonical references and resource identifiers.
* **Development Branches**: Use preview URLs for canonical references and resource identifiers.

The DAK configuration is automatically regenerated during CI builds to ensure URLs are appropriate for the current branch context.

### Dependencies

### Cross Version Analysis

This is an R4 IG. None of the features it uses are changed in R4B, so it can be used as is with R4B systems. Packages for both [R4 (smart.who.int.base.r4)](package.r4.tgz) and [R4B (smart.who.int.base.r4b)](package.r4b.tgz) are available.

### Global Profiles

*There are no Global profiles defined*

### IP Statements

This publication includes IP covered under the following statements.

* © International Labour Organization 2008

* [International Standard Classification of Occupations 2008](CodeSystem-ISCO08.md): [GenericPersona](StructureDefinition-GenericPersona.md) and [ISCO08ValueSet](ValueSet-ISCO08ValueSet.md)


* WHO © 2023. Some rights reserved. CC BY-NC-SA 3.0 IGO.

* [Classification of Digital Health Interventions v2](CodeSystem-CDHIv2.md): [CDHIv2](ValueSet-CDHIv2.md), [CDHIv2.1](ValueSet-CDHIv2.1.md), [CDHIv2.2](ValueSet-CDHIv2.2.md), [CDHIv2.3](ValueSet-CDHIv2.3.md) and [CDHIv2.4](ValueSet-CDHIv2.4.md)
* [Classification of Digital Health Services and Application Types v2](CodeSystem-CDSCv2.md): [CDSCv2](ValueSet-CDSCv2.md), [CDSCv2.A](ValueSet-CDSCv2.A.md)... Show 4 more, [CDSCv2.B](ValueSet-CDSCv2.B.md), [CDSCv2.C](ValueSet-CDSCv2.C.md), [CDSCv2.D](ValueSet-CDSCv2.D.md) and [CDSCv2.E](ValueSet-CDSCv2.E.md)




## Resource Content

```json
{
  "resourceType" : "ImplementationGuide",
  "id" : "smart.who.int.base",
  "meta" : {
    "profile" : ["http://smart.who.int/base/StructureDefinition/SGImplementationGuide"]
  },
  "url" : "http://smart.who.int/base/ImplementationGuide/smart.who.int.base",
  "version" : "0.2.0",
  "name" : "Base",
  "title" : "SMART Base",
  "status" : "draft",
  "experimental" : false,
  "date" : "2026-03-06T03:20:56+00:00",
  "publisher" : "WHO",
  "contact" : [{
    "name" : "WHO",
    "telecom" : [{
      "system" : "url",
      "value" : "http://who.int"
    }]
  }],
  "description" : "Base SMART Guidelines implementation guide to be used as the base dependency for all SMART Guidelines IGs",
  "packageId" : "smart.who.int.base",
  "license" : "CC-BY-SA-3.0-IGO",
  "fhirVersion" : ["4.0.1"],
  "dependsOn" : [{
    "id" : "hl7_terminology",
    "uri" : "http://terminology.hl7.org/ImplementationGuide/hl7.terminology",
    "packageId" : "hl7.terminology",
    "version" : "5.5.0"
  },
  {
    "id" : "hl7_fhir_uv_extensions_r4",
    "uri" : "http://hl7.org/fhir/extensions/ImplementationGuide/hl7.fhir.uv.extensions",
    "packageId" : "hl7.fhir.uv.extensions.r4",
    "version" : "5.1.0"
  },
  {
    "id" : "hl7_fhir_uv_extensions_r5",
    "uri" : "http://hl7.org/fhir/extensions/ImplementationGuide/hl7.fhir.uv.extensions",
    "packageId" : "hl7.fhir.uv.extensions.r5",
    "version" : "5.2.0"
  },
  {
    "id" : "cql",
    "extension" : [{
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ImplementationGuide.dependsOn.reason",
      "valueMarkdown" : "This IG uses CQL profiles and capabilities provided by the Using CQL With FHIR IG"
    }],
    "uri" : "http://hl7.org/fhir/uv/cql/ImplementationGuide/hl7.fhir.uv.cql",
    "packageId" : "hl7.fhir.uv.cql",
    "version" : "1.0.0"
  },
  {
    "id" : "cpg",
    "extension" : [{
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ImplementationGuide.dependsOn.reason",
      "valueMarkdown" : "For Decision Tables"
    }],
    "uri" : "http://hl7.org/fhir/uv/cpg/ImplementationGuide/hl7.fhir.uv.cpg",
    "packageId" : "hl7.fhir.uv.cpg",
    "version" : "2.0.0"
  },
  {
    "id" : "crmi",
    "extension" : [{
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ImplementationGuide.dependsOn.reason",
      "valueMarkdown" : "This IG uses content management profiles and capabilities provided by the Canonical Resource Management Infrastructure (CRMI) IG"
    }],
    "uri" : "http://hl7.org/fhir/uv/crmi/ImplementationGuide/hl7.fhir.uv.crmi",
    "packageId" : "hl7.fhir.uv.crmi",
    "version" : "1.0.0"
  },
  {
    "id" : "sdc",
    "extension" : [{
      "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ImplementationGuide.dependsOn.reason",
      "valueMarkdown" : "This IG uses questionnaire profiles and capabilities provided by the Structure Data Capture (SDC) IG"
    }],
    "uri" : "http://hl7.org/fhir/uv/sdc/ImplementationGuide/hl7.fhir.uv.sdc",
    "packageId" : "hl7.fhir.uv.sdc",
    "version" : "3.0.0"
  }],
  "definition" : {
    "extension" : [{
      "extension" : [{
        "url" : "code",
        "valueString" : "copyrightyear"
      },
      {
        "url" : "value",
        "valueString" : "2023+"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "releaselabel"
      },
      {
        "url" : "value",
        "valueString" : "ci-build"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "autoload-resources"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "path-liquid"
      },
      {
        "url" : "value",
        "valueString" : "template/liquid"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "path-liquid"
      },
      {
        "url" : "value",
        "valueString" : "input/liquid"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "path-qa"
      },
      {
        "url" : "value",
        "valueString" : "temp/qa"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "path-temp"
      },
      {
        "url" : "value",
        "valueString" : "temp/pages"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "path-output"
      },
      {
        "url" : "value",
        "valueString" : "output"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "path-suppressed-warnings"
      },
      {
        "url" : "value",
        "valueString" : "input/ignoreWarnings.txt"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "path-history"
      },
      {
        "url" : "value",
        "valueString" : "http://smart.who.int/base/history.html"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "template-html"
      },
      {
        "url" : "value",
        "valueString" : "template-page.html"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "template-md"
      },
      {
        "url" : "value",
        "valueString" : "template-page-md.html"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "apply-contact"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "apply-context"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "apply-copyright"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "apply-jurisdiction"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "apply-license"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "apply-publisher"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "apply-version"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "apply-wg"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "active-tables"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "fmm-definition"
      },
      {
        "url" : "value",
        "valueString" : "http://hl7.org/fhir/versions.html#maturity"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "propagate-status"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "excludelogbinaryformat"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueString" : "tabbed-snapshots"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-internal-dependency",
      "valueCode" : "hl7.fhir.uv.tools.r4#0.9.0"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "copyrightyear"
      },
      {
        "url" : "value",
        "valueString" : "2023+"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "releaselabel"
      },
      {
        "url" : "value",
        "valueString" : "ci-build"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "autoload-resources"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "path-liquid"
      },
      {
        "url" : "value",
        "valueString" : "template/liquid"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "path-liquid"
      },
      {
        "url" : "value",
        "valueString" : "input/liquid"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "path-qa"
      },
      {
        "url" : "value",
        "valueString" : "temp/qa"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "path-temp"
      },
      {
        "url" : "value",
        "valueString" : "temp/pages"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "path-output"
      },
      {
        "url" : "value",
        "valueString" : "output"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "path-suppressed-warnings"
      },
      {
        "url" : "value",
        "valueString" : "input/ignoreWarnings.txt"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "path-history"
      },
      {
        "url" : "value",
        "valueString" : "http://smart.who.int/base/history.html"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "template-html"
      },
      {
        "url" : "value",
        "valueString" : "template-page.html"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "template-md"
      },
      {
        "url" : "value",
        "valueString" : "template-page-md.html"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "apply-contact"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "apply-context"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "apply-copyright"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "apply-jurisdiction"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "apply-license"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "apply-publisher"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "apply-version"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "apply-wg"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "active-tables"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "fmm-definition"
      },
      {
        "url" : "value",
        "valueString" : "http://hl7.org/fhir/versions.html#maturity"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "propagate-status"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "excludelogbinaryformat"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    },
    {
      "extension" : [{
        "url" : "code",
        "valueCode" : "tabbed-snapshots"
      },
      {
        "url" : "value",
        "valueString" : "true"
      }],
      "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
    }],
    "grouping" : [{
      "id" : "Conformance",
      "name" : "Conformance",
      "description" : "constraints and profile structures for SMART Guidelines resources"
    }],
    "resource" : [{
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      }],
      "reference" : {
        "reference" : "StructureDefinition/BusinessProcessWorkflow"
      },
      "name" : "Business Process Workflow (DAK)",
      "description" : "Logical Model for representing Generic Business Processes and Workflows from a DAK. A business process is a set of related activities or tasks performed together to achieve the objectives of the health programme area.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      }],
      "reference" : {
        "reference" : "StructureDefinition/BusinessProcessWorkflowSource"
      },
      "name" : "Business Process Workflow Source",
      "description" : "Source reference for Business Process Workflow - exactly one of the following must be provided:\n- url (url data type): URL to retrieve BusinessProcessWorkflow definition from input/ or external source\n- canonical (canonical data type): Canonical URI pointing to the BusinessProcessWorkflow definition\n- instance: Inline BusinessProcessWorkflow instance data",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/CDHIv1"
      },
      "name" : "Classification of Digital Health Interventions v1",
      "description" : "Value Set for Classification of Digital Health Interventions v1. Autogenerated from DAK artifacts",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      }],
      "reference" : {
        "reference" : "CodeSystem/CDHIv1"
      },
      "name" : "Classification of Digital Health Interventions v1",
      "description" : "CodeSystem for Classification of Digital Health Interventions v1. Autogenerated from DAK artifacts",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/CDHIv2"
      },
      "name" : "Classification of Digital Health Interventions v2",
      "description" : "Value Set for the Classification of Digital Interventions, Services and Applications in Health (CDISAH), second edition (2023).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      }],
      "reference" : {
        "reference" : "CodeSystem/CDHIv2"
      },
      "name" : "Classification of Digital Health Interventions v2",
      "description" : "CodeSystem for the Classification of Digital Interventions, Services and Applications in Health\n(CDISAH), second edition (2023). ISBN 978-92-4-008194-9.\n\nOrganised into four groups based on the primary user:\n  1. Persons\n  2. Healthcare providers\n  3. Health management and support personnel\n  4. Data services\n\nNew categories vs v1: 1.4.4, 1.6.2, 1.8, 2.5.6, 2.11, 3.1.5, 3.5.7, 3.5.8, 3.8, 4.3.5, 4.4.2, 4.4.3, 4.5.\nSee ConceptMap CDHIv1toCDHIv2 for the full mapping from the first edition.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      }],
      "reference" : {
        "reference" : "CodeSystem/CDSCv2"
      },
      "name" : "Classification of Digital Health Services and Application Types v2",
      "description" : "CodeSystem for the Classification of Digital Health Services and Application Types v2,\nas defined in the Classification of Digital Interventions, Services and Applications in Health\n(CDISAH), second edition (2023). ISBN 978-92-4-008194-9.\n\nServices and Application Types represent the types of software, ICT systems and services\nor communication channels that deliver or execute digital health interventions (DHIs) and\nhealth content.\n\nThe types are organised into five representations within the Digital Health Architecture:\n  A. Point of service\n  B. Health system/Provider administration\n  C. Registries and Directories\n  D. Data Management services\n  E. Surveillance and Response",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      }],
      "reference" : {
        "reference" : "CodeSystem/CDSCv1"
      },
      "name" : "Classification of Digital Health System Categories v1",
      "description" : "CodeSystem for Classification of Digital Health System Categories v1. Autogenerated from DAK artifacts",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ActorDefinition"
      }],
      "reference" : {
        "reference" : "ActorDefinition/DAK.Persona.System.ClientRegistry"
      },
      "name" : "Client Registry / Master Patient Index",
      "description" : "A digital system that creates, maintains, and provides authoritative unique\nidentifiers for individuals (persons) accessing health services, enabling\ncross-facility patient matching and de-duplication.\n\nThe client registry supports DHIs including:\n- Verify a person's unique identity (2.1.1)\n- Enrol person(s) for health services/clinical care plan (2.1.2)\n- Merge, de-duplicate and curate coded datasets (4.2.2)\n- Standards-compliant interoperability to link records across systems (4.4.2)\n\n**Services and Application Types**:\n- C6 — Identification registries and directories\n- C8 — Master patient index",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ActorDefinition"
      }],
      "reference" : {
        "reference" : "ActorDefinition/DAK.Persona.CommunityHealthWorker"
      },
      "name" : "Community Health Worker",
      "description" : "A frontline member of the health workforce who delivers health interventions\nat the community level, acting as a link between communities and formal health\nfacilities. Community health workers are a key sub-group of healthcare providers.\n\nCommunity health workers use DHIs to:\n- Register and follow-up community members (2.1, 2.2.1)\n- Receive community-based decision support and job aids (2.3)\n- Report public health events from point of diagnosis (3.3.1)\n- Access mobile training and competency assessments (2.8)\n- Communicate with supervising clinical staff (2.5.1)\n- Manage their daily visit planning and activities (2.7)\n\n**ISCO-08**: 3255 (Community health workers), 5321 (Health care assistants).\n\n**Examples**: Village health worker, health extension worker, community health\nvolunteer, lay health advisor, peer educator, traditional birth attendant,\ncommunity case manager.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      }],
      "reference" : {
        "reference" : "StructureDefinition/CoreDataElement"
      },
      "name" : "Core Data Element (DAK)",
      "description" : "Logical Model for representing Core Data Elements from a DAK. A core data element can be one of: a ValueSet, a CodeSystem, a ConceptMap, or a Logical Model adherent to SGLogicalModel. This is the ONE EXCEPTION to allowing FHIR R4 models into the DAK LMs.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      }],
      "reference" : {
        "reference" : "StructureDefinition/CoreDataElementSource"
      },
      "name" : "Core Data Element Source",
      "description" : "Source reference for Core Data Element - exactly one of the following must be provided:\n- url (url data type): URL to retrieve CoreDataElement definition from input/ or external source\n- canonical (canonical data type): Canonical URI pointing to the CoreDataElement definition\n- instance: Inline CoreDataElement instance data",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      }],
      "reference" : {
        "reference" : "CodeSystem/CoreDataElementType"
      },
      "name" : "Core Data Element Type",
      "description" : "CodeSystem for Core Data Element types - defines the type of FHIR resource that a Core Data Element references.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/CoreDataElementTypeVS"
      },
      "name" : "Core Data Element Type Value Set",
      "description" : "Value set of core data element types",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      }],
      "reference" : {
        "reference" : "StructureDefinition/DecisionSupportLogicSource"
      },
      "name" : "Decision Support Logic Source",
      "description" : "Source reference for Decision Support Logic - exactly one of the following must be provided:\n- url (url data type): URL to retrieve DecisionSupportLogic definition from input/ or external source\n- canonical (canonical data type): Canonical URI pointing to the DecisionSupportLogic definition\n- instance: Inline DecisionSupportLogic instance data",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      }],
      "reference" : {
        "reference" : "StructureDefinition/DecisionSupportLogic"
      },
      "name" : "Decision-Support Logic (DAK)",
      "description" : "Logical Model for representing Decision-Support Logic from a DAK. Decision-support logic and algorithms to support appropriate service delivery in accordance with WHO clinical, public health and data use guidelines.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      }],
      "reference" : {
        "reference" : "StructureDefinition/DAK"
      },
      "name" : "Digital Adaptation Kit (DAK)",
      "description" : "Logical Model for representing a complete Digital Adaptation Kit (DAK) with metadata and all 9 DAK components",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/CDHIv1.1"
      },
      "name" : "Digital Health Interventions for Clients",
      "description" : "Digital Health Interventions whose primary user group is Clients (persons using health services). Group 1 of the Classification of Digital Health Interventions v1 (2018).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/CDHIv2.3"
      },
      "name" : "Digital Health Interventions for Health Management and Support Personnel",
      "description" : "Digital Health Interventions whose primary user group is Health Management and Support Personnel. Group 3 of the Classification of Digital Interventions, Services and Applications in Health v2 (CDISAH, 2023).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/CDHIv1.3"
      },
      "name" : "Digital Health Interventions for Health System Managers",
      "description" : "Digital Health Interventions whose primary user group is Health System Managers. Group 3 of the Classification of Digital Health Interventions v1 (2018).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/CDHIv1.2"
      },
      "name" : "Digital Health Interventions for Health Workers",
      "description" : "Digital Health Interventions whose primary user group is Health Workers. Group 2 of the Classification of Digital Health Interventions v1 (2018).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/CDHIv2.2"
      },
      "name" : "Digital Health Interventions for Healthcare Providers",
      "description" : "Digital Health Interventions whose primary user group is Healthcare Providers. Group 2 of the Classification of Digital Interventions, Services and Applications in Health v2 (CDISAH, 2023).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/CDHIv2.1"
      },
      "name" : "Digital Health Interventions for Persons",
      "description" : "Digital Health Interventions whose primary user group is Persons (health service users). Group 1 of the Classification of Digital Interventions, Services and Applications in Health v2 (CDISAH, 2023).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/CDHIv1.4"
      },
      "name" : "Digital Health Interventions: Data Services",
      "description" : "Crosscutting Data Services DHIs. Group 4 of the Classification of Digital Health Interventions v1 (2018).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/CDHIv2.4"
      },
      "name" : "Digital Health Interventions: Data Services",
      "description" : "Crosscutting Data Services DHIs. Group 4 of the Classification of Digital Interventions, Services and Applications in Health v2 (CDISAH, 2023).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      }],
      "reference" : {
        "reference" : "StructureDefinition/DublinCore"
      },
      "name" : "Dublin Core Metadata Element Set",
      "description" : "Logical Model representing Dublin Core metadata elements as defined at https://www.dublincore.org/specifications/dublin-core/dcmi-terms/",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ActorDefinition"
      }],
      "reference" : {
        "reference" : "ActorDefinition/DAK.Persona.System.EMR"
      },
      "name" : "Electronic Medical Record (EMR) System",
      "description" : "A secure, digital system that holds information about people's health and\nclinical care managed by healthcare providers. Also referred to as an\nElectronic Health Record (EHR).\n\nThe EMR system supports DHIs including:\n- Longitudinal tracking of person's health status and services (2.2.1)\n- Management of structured clinical records (2.2.2)\n- Management of unstructured clinical records such as notes and images (2.2.3)\n- Clinical decision support prompts and checklists (2.3)\n- Person identification and registration (2.1)\n- Prescription and medication management (2.9)\n- Laboratory results reception (2.10.1)\n- Routine health indicator data collection (2.2.4)\n\n**Services and Application Type**: A5 — Electronic medical record systems\n\n**Functional areas**: Clinical decision support, record management,\nperson registration, appointment scheduling, referral tracking.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      }],
      "reference" : {
        "reference" : "StructureDefinition/FHIRSchemaBase"
      },
      "name" : "FHIR Schema Base (SMART Guidelines)",
      "description" : "Base logical model providing the common schema metadata interface inherited by all SMART Guidelines logical models. Every SMART Guidelines logical model schema derives from this base, which documents the shared FHIR and JSON-LD metadata properties used by the JSON Schema generation pipeline.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Requirements"
      },
      "name" : "Functional and Non-Functional Requirements (DAK)",
      "description" : "Logical Model for representing Functional and Non-Functional Requirements from a DAK. A high-level list of core functions and capabilities that the system must have to meet the end users' needs.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      }],
      "reference" : {
        "reference" : "StructureDefinition/FunctionalRequirement"
      },
      "name" : "Functional Requirement (DAK)",
      "description" : "Logical Model for representing functional requirement from a DAK",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      }],
      "reference" : {
        "reference" : "StructureDefinition/GenericPersona"
      },
      "name" : "Generic Persona (DAK)",
      "description" : "Logical Model for representing Generic Personas from a DAK. Depiction of the human and system actors. Human actors are end users, supervisors and related stakeholders who would be interacting with the digital system or involved in the clinical care, public health or health system pathway.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      }],
      "reference" : {
        "reference" : "StructureDefinition/GenericPersonaSource"
      },
      "name" : "Generic Persona Source",
      "description" : "Source reference for Generic Persona - exactly one of the following must be provided:\n- url (url data type): URL to retrieve GenericPersona definition from input/ or external source\n- canonical (canonical data type): Canonical URI pointing to the GenericPersona definition\n- instance: Inline GenericPersona instance data",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ActorDefinition"
      }],
      "reference" : {
        "reference" : "ActorDefinition/DAK.Persona.DataManager"
      },
      "name" : "Health Data Manager and Analyst",
      "description" : "A professional who manages, analyses, and disseminates health data to support\nevidence-based decision-making. This corresponds to the 'Data services' user\ngroup in CDISAH v2, providing crosscutting functionality across the health system.\n\nData managers use DHIs to:\n- Create data collection forms and manage data acquisition (4.1.1)\n- Store and aggregate health data (4.1.2)\n- Synthesise and visualise data for reporting and dashboards (4.1.3)\n- Apply automated analytics and predictive modelling including AI/ML (4.1.4)\n- Parse, de-duplicate, and curate coded datasets and terminologies (4.2)\n- Classify disease codes and causes of mortality (4.2.3)\n- Map geographic locations of facilities, events, populations, and providers (4.3)\n- Enable point-to-point data integration and standards-compliant interoperability (4.4)\n- Maintain data governance including authentication, privacy, and consent (4.5)\n\n**ISCO-08**: 2120 (Mathematicians, actuaries and statisticians), 2521 (Database\ndesigners and administrators), 2523 (Computer network professionals), 3120\n(Computer network and systems technicians).\n\n**Examples**: Biostatistician, epidemiologist, health informatician, data analyst,\nDHIS2 administrator, GIS specialist, interoperability engineer, terminology manager.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ActorDefinition"
      }],
      "reference" : {
        "reference" : "ActorDefinition/DAK.Persona.System.InteropPlatform"
      },
      "name" : "Health Information Exchange / Interoperability Platform",
      "description" : "A middleware system or shared infrastructure that enables health data exchange\nbetween disparate health information systems using standard protocols and formats.\n\nThe interoperability platform supports DHIs including:\n- Point-to-point data integration (4.4.1)\n- Standards-compliant interoperability (4.4.2)\n- Message routing to appropriate architecture components (4.4.3)\n- Data storage and aggregation across systems (4.1.2)\n\n**Services and Application Type**: D2 — Data interchange and interoperability\n\n**Functional areas**: Semantic interoperability, technical interoperability,\ninformation exchange, data mediation, enterprise service bus.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      }],
      "reference" : {
        "reference" : "StructureDefinition/HealthInterventions"
      },
      "name" : "Health Interventions and Recommendations (DAK)",
      "description" : "Logical Model for representing Health Interventions and Recommendations from a DAK. Overview of the health interventions and WHO, regional or national recommendations included within the DAK.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      }],
      "reference" : {
        "reference" : "StructureDefinition/HealthInterventionsSource"
      },
      "name" : "Health Interventions Source",
      "description" : "Source reference for Health Interventions - exactly one of the following must be provided:\n- url (url data type): URL to retrieve HealthInterventions definition from input/ or external source\n- canonical (canonical data type): Canonical URI pointing to the HealthInterventions definition\n- instance: Inline HealthInterventions instance data",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ActorDefinition"
      }],
      "reference" : {
        "reference" : "ActorDefinition/DAK.Persona.System.HMIS"
      },
      "name" : "Health Management Information System (HMIS)",
      "description" : "A digital system used to collect, process, report, and use aggregate health data\nfor programme planning, monitoring, and evaluation at district and national levels.\n\nThe HMIS supports DHIs including:\n- Routine health indicator data collection and management (2.2.4)\n- Non-routine data collection and management (4.1.1)\n- Data storage and aggregation (4.1.2)\n- Data synthesis and visualisations (4.1.3)\n- Data exchange across systems (4.4)\n\n**Services and Application Type**: D6 — Health Management Information Systems (HMIS)\n\n**Functional areas**: Data collection, reporting dashboards, target monitoring,\nprogramme performance tracking, data quality management.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/CDSCv1"
      },
      "name" : "Health System Challenges",
      "description" : "Value set for Health System Challenges (Classification of Digital Health System Categories v1, 2018). Includes all 25 system category codes (A–Y).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ActorDefinition"
      }],
      "reference" : {
        "reference" : "ActorDefinition/DAK.Persona.HealthSystemManager"
      },
      "name" : "Health System Manager",
      "description" : "A professional involved in the administration and oversight of health systems.\n\nHealth system managers use DHIs to:\n- Manage health workforce information, performance, and certification (3.1)\n- Oversee supply chain, inventory, cold chain, and procurement (3.2)\n- Receive notifications of public health events (3.3)\n- Register and certify vital events — births and deaths (3.4)\n- Administer health coverage schemes, billing, payroll, and budgets (3.5)\n- Monitor and track health equipment and assets (3.6)\n- Manage health facility information and conduct assessments (3.7)\n- Manage person-centred health certificate information (3.8)\n\n**ISCO-08**: 1342 (Health services managers), 2446 (Social work professionals\nn.e.c.), 3354 (Government social benefits officials), 4311 (Accounting and\nbookkeeping clerks).\n\n**Examples**: District health officer, programme manager, supply chain officer,\nHMIS coordinator, hospital administrator, vital registration officer,\nhealth insurance administrator.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ActorDefinition"
      }],
      "reference" : {
        "reference" : "ActorDefinition/DAK.Persona.HealthcareProvider"
      },
      "name" : "Healthcare Provider",
      "description" : "A member of the health workforce who delivers health interventions. This group\nhas also been described as 'health workers' or 'healthcare workers'.\n\nHealthcare providers use DHIs to:\n- Identify and register persons for health services (2.1)\n- Manage person-centred health records (2.2)\n- Receive clinical decision support prompts and checklists (2.3)\n- Conduct telemedicine consultations and remote monitoring (2.4)\n- Communicate with supervisors, peers, and receive AI-assisted content (2.5)\n- Coordinate referrals and emergency transport (2.6)\n- Schedule and plan their clinical activities (2.7)\n- Access training content and assessments (2.8)\n- Manage prescriptions and medication adherence (2.9)\n- Order and receive laboratory and diagnostic results (2.10)\n- Verify health coverage and receive payments from individuals (2.11)\n\n**ISCO-08**: 2211 (Generalist medical practitioners), 2212 (Specialist medical\npractitioners), 2221 (Nursing professionals), 2222 (Midwifery professionals),\n3211 (Medical imaging and therapeutic equipment technicians), 3212 (Medical\nand pathology laboratory technicians), 3213 (Pharmaceutical technicians and\nassistants), 3221 (Nursing associate professionals), 3222 (Midwifery associate\nprofessionals), 3255 (Community health workers).\n\n**Examples**: Physician, nurse, midwife, clinical officer, pharmacist,\nlaboratory technician, dentist, allied health professional.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ConceptMap"
      }],
      "reference" : {
        "reference" : "ConceptMap/CDHIv1Hierarchy"
      },
      "name" : "Hierarchy of the Classification of Digital Health Interventions v1",
      "description" : "Mapping to represent hierarchy within the Classification of Digital Health Interventions v1.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ConceptMap"
      }],
      "reference" : {
        "reference" : "ConceptMap/CDHIv2Hierarchy"
      },
      "name" : "Hierarchy of the Classification of Digital Health Interventions v2",
      "description" : "Mapping to represent hierarchy within the Classification of Digital Interventions, Services and Applications in Health (CDISAH) v2.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      }],
      "reference" : {
        "reference" : "CodeSystem/ISCO08"
      },
      "name" : "International Standard Classification of Occupations 2008",
      "description" : "ISCO-08 codes from the International Labour Organization official classification",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/ISCO08ValueSet"
      },
      "name" : "ISCO-08 Value Set",
      "description" : "Extensible value set of ISCO-08 codes for persona classification",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ActorDefinition"
      }],
      "reference" : {
        "reference" : "ActorDefinition/DAK.Persona.System.LIS"
      },
      "name" : "Laboratory Information System (LIS)",
      "description" : "A digital system that manages the complete lifecycle of laboratory test orders,\nspecimen tracking, result production, and result reporting to healthcare providers\nand persons.\n\nThe LIS supports DHIs including:\n- Transmit and track diagnostic orders (2.10.2)\n- Capture diagnostic results from digital devices (2.10.3)\n- Transmit person's diagnostic result to healthcare provider (2.10.1)\n- Transmit diagnostics result or availability of result to person(s) (1.1.4)\n- Track biological specimens (2.10.4)\n\n**Services and Application Type**: A6 — Laboratory information systems\n\n**Functional areas**: Lab requests/test ordering, sample tracking, sample\nprocessing, results reporting.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:extension"
      }],
      "reference" : {
        "reference" : "StructureDefinition/LinkIdExt"
      },
      "name" : "LinkIdExt",
      "description" : "Smart Guidelines link identifier extension",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ActorDefinition"
      }],
      "reference" : {
        "reference" : "ActorDefinition/DAK.Persona.System.LMIS"
      },
      "name" : "Logistics Management Information System (LMIS)",
      "description" : "A digital system that manages the health supply chain from quantification\nand forecasting through distribution, inventory management, and consumption tracking.\n\nThe LMIS supports DHIs including:\n- Manage inventory and distribution of health commodities (3.2.1)\n- Notify stock levels of health commodities (3.2.2)\n- Monitor cold-chain sensitive commodities (3.2.3)\n- Register licensed drugs and health commodities (3.2.4)\n- Manage procurement of commodities (3.2.5)\n\n**Services and Application Type**: B6 — Logistics management information systems (LMIS)",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ConceptMap"
      }],
      "reference" : {
        "reference" : "ConceptMap/CDHIv1toCDHIv2"
      },
      "name" : "Mapping from CDHI v1 to CDISAH v2",
      "description" : "Mapping from the Classification of Digital Health Interventions v1 (CDHI v1, 2018)\nto the Classification of Digital Interventions, Services and Applications in Health v2\n(CDISAH v2, 2023).\n\nKey structural changes reflected in this map:\n- User group labels updated throughout (e.g. 'Clients' → 'Persons',\n  'Health workers' → 'Healthcare providers', 'Health system managers' →\n  'Health management and support personnel').\n- Civil Registration and Vital Statistics (CRVS) consolidated: six v1 codes\n  (3.4.1–3.4.6) merged into two v2 codes (3.4.1, 3.4.2).\n- Health financing section restructured: v1 3.5.1 (insurance membership) and\n  3.5.2 (billing) updated; v1 3.5.3–3.5.6 shifted by one (now 3.5.4–3.5.6 + new 3.5.3).\n- Data services (group 4) substantially revised: 4.1.1 changed scope,\n  4.3 expanded from 4 to 5 codes, 4.4 split from 1 to 3 codes, 4.5 is entirely new.\n- New v2 categories with no v1 equivalent are listed as 'unmatched' targets.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ConceptMap"
      }],
      "reference" : {
        "reference" : "ConceptMap/CDSCv1toCDSCv2"
      },
      "name" : "Mapping from CDSC v1 to Services and Application Types v2",
      "description" : "Mapping from the Classification of Digital Health System Categories v1 (CDSCv1, 2018)\nto the Classification of Digital Health Services and Application Types v2 (CDSCv2, 2023).\n\nThe v1 used 25 single-letter codes (A–Y). The v2 completely restructured this into\n5 representations within the digital health enterprise architecture, each with\nalphanumeric codes (A1–A9, B1–B8, C1–C11, D1–D8, E1–E2).\n\nSeveral new v2 categories have no v1 equivalent:\nA3 (Decision support), A4 (Diagnostics), B1 (Blood bank), B3 (Health program monitoring),\nB7 (Patient administration), C4 (Facility registries), C5 (Health worker registry),\nC7 (Immunisation information), C8 (Master patient index), C9 (Product catalogues),\nC10 (Public Key directories), D1 (Analytics), D3 (Data warehouses).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:extension"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Markdown"
      },
      "name" : "Markdown",
      "description" : "Markdown extension",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      }],
      "reference" : {
        "reference" : "StructureDefinition/NonFunctionalRequirement"
      },
      "name" : "Non-Functional Requirement (DAK)",
      "description" : "Logical Model for representing non-functional requirement from a DAK",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ActorDefinition"
      }],
      "reference" : {
        "reference" : "ActorDefinition/DAK.Persona.Person"
      },
      "name" : "Person (Health Service User)",
      "description" : "A member of the public who is a potential or current user of health services,\nincluding health prevention and wellness activities. Other terms used for this\ngroup include 'patient', 'client', 'individual', and 'health service user'.\nCaregivers of individuals receiving health services are also included.\n\nPersons interact with DHIs to:\n- Receive targeted (1.1) and untargeted (1.2) health communications\n- Communicate with other persons as peers (1.3)\n- Track their own health data and records (1.4)\n- Report health events and system feedback (1.5)\n- Access health information on demand including via chatbot/AI (1.6)\n- Manage their financial transactions related to health services (1.7)\n- Manage their consent for health data access and sharing (1.8)\n\n**ISCO-08**: Not applicable (non-occupational role).\n\n**Examples**: Patient, pregnant woman, caregiver, child, community member,\nhealth scheme beneficiary, person living with a chronic condition.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Persona"
      },
      "name" : "Persona (DAK)",
      "description" : "Logical Model for representing Personas from a DAK",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      }],
      "reference" : {
        "reference" : "StructureDefinition/ProgramIndicator"
      },
      "name" : "Program Indicator (DAK)",
      "description" : "Logical Model for representing Program Indicators from a DAK. Core set of indicators that need to be aggregated for decision-making, performance metrics and subnational and national reporting.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      }],
      "reference" : {
        "reference" : "StructureDefinition/ProgramIndicatorSource"
      },
      "name" : "Program Indicator Source",
      "description" : "Source reference for Program Indicator - exactly one of the following must be provided:\n- url (url data type): URL to retrieve ProgramIndicator definition from input/ or external source\n- canonical (canonical data type): Canonical URI pointing to the ProgramIndicator definition\n- instance: Inline ProgramIndicator instance data",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ActorDefinition"
      }],
      "reference" : {
        "reference" : "ActorDefinition/DAK.Persona.System.SurveillanceSystem"
      },
      "name" : "Public Health and Disease Surveillance System",
      "description" : "A digital system for detecting, monitoring, investigating, and responding to\ndisease outbreaks and public health threats.\n\nThe surveillance system supports DHIs including:\n- Notification of public health events from point of diagnosis (3.3.1)\n- Transmit health event alerts to specific population group(s) (1.1.1)\n- Map location of health event (4.3.2)\n- Data synthesis and visualizations for outbreak response (4.1.3)\n- Automated analysis of data to generate predictions (4.1.4)\n\n**Services and Application Type**: E2 — Public health and disease surveillance systems",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "Questionnaire"
      }],
      "reference" : {
        "reference" : "Questionnaire/DAK.DT.IMMZ.D2.DT.BCGQuestionnaire"
      },
      "name" : "Questionnaire for IMMZ.D2 Determine required vaccination(s) if any",
      "description" : "Auto-generated questionnaire for decision table DAK.DT.IMMZ.D2.DT.BCG",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      }],
      "reference" : {
        "reference" : "StructureDefinition/RequirementsSource"
      },
      "name" : "Requirements Source",
      "description" : "Source reference for Requirements - exactly one of the following must be provided:\n- url (url data type): URL to retrieve Requirements definition from input/ or external source\n- canonical (canonical data type): Canonical URI pointing to the Requirements definition\n- instance: Inline Requirements instance data",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:extension"
      }],
      "reference" : {
        "reference" : "StructureDefinition/Satisfies"
      },
      "name" : "Satisfies",
      "description" : "Indicates that if the conditions for this requirement are satisified, then that it should be viewed as satisifying  the referenced requirement.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/CDSCv2"
      },
      "name" : "Services and Application Types",
      "description" : "Value set for Services and Application Types (Classification of Digital Health Services and Application Types v2, CDISAH 2023). Includes all codes across the five architecture groups (A–E).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/CDSCv2.D"
      },
      "name" : "Services and Application Types: Data Management Services",
      "description" : "Services and systems that support the collection, aggregation, storage, analysis, and exchange of health data. Group D of the Classification of Digital Health Services and Application Types v2 (CDISAH, 2023).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/CDSCv2.B"
      },
      "name" : "Services and Application Types: Health System/Provider Administration",
      "description" : "Systems that support the administrative and managerial functions of health systems and healthcare organisations. Group B of the Classification of Digital Health Services and Application Types v2 (CDISAH, 2023).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/CDSCv2.A"
      },
      "name" : "Services and Application Types: Point of Service",
      "description" : "Systems that facilitate the provision and delivery of healthcare services to persons at the point of care. Group A of the Classification of Digital Health Services and Application Types v2 (CDISAH, 2023).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/CDSCv2.C"
      },
      "name" : "Services and Application Types: Registries and Directories",
      "description" : "Systems that create, maintain, and provide authoritative master records for persons, providers, facilities, products and health events. Group C of the Classification of Digital Health Services and Application Types v2 (CDISAH, 2023).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/CDSCv2.E"
      },
      "name" : "Services and Application Types: Surveillance and Response",
      "description" : "Systems that support the detection, monitoring, and response to disease outbreaks and public health threats. Group E of the Classification of Digital Health Services and Application Types v2 (CDISAH, 2023).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:extension"
      }],
      "reference" : {
        "reference" : "StructureDefinition/SGActorExt"
      },
      "name" : "SGActorExt",
      "description" : "Smart Guidelines Actor Reference extension",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:extension"
      }],
      "reference" : {
        "reference" : "StructureDefinition/SGcode"
      },
      "name" : "SGcode",
      "description" : "Smart Guidelines code extension",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ActivityDefinition"
      }],
      "reference" : {
        "reference" : "ActivityDefinition/SGDecisionTableGuidance"
      },
      "name" : "SGDecisionTableGuidance",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:extension"
      }],
      "reference" : {
        "reference" : "StructureDefinition/SGDocumentation"
      },
      "name" : "SGDocumentation",
      "description" : "Smart Guidelines Documentation extension",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:extension"
      }],
      "reference" : {
        "reference" : "StructureDefinition/SGMarkdown"
      },
      "name" : "SGMarkdown",
      "description" : "Smart Guidelines markdown extension",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:extension"
      }],
      "reference" : {
        "reference" : "StructureDefinition/SGRequirementExt"
      },
      "name" : "SGRequirementExt",
      "description" : "Smart Guidelines Requirements extension",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:extension"
      }],
      "reference" : {
        "reference" : "StructureDefinition/SGString"
      },
      "name" : "SGString",
      "description" : "Smart Guidelines (required) string extension for use in a complex extension",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:extension"
      }],
      "reference" : {
        "reference" : "StructureDefinition/SGTask"
      },
      "name" : "SGTask",
      "description" : "Extension to reference SMART Guidelines task type",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:extension"
      }],
      "reference" : {
        "reference" : "StructureDefinition/SGUserStory"
      },
      "name" : "SGUserStory",
      "description" : "Smart Guidelines extension to support structured User Stories (As a `Actor` I want to `capability` so that `benefit`) extension",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      }],
      "reference" : {
        "reference" : "CodeSystem/DecisionTableActions"
      },
      "name" : "Smart Guidelines Actions (columns) for Decision Tables",
      "description" : "CodeSystem for Smart Guidelines Documentation Actions for Decision Tables\"",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/SGActivityDefinition"
      },
      "name" : "SMART Guidelines ActivityDefinition",
      "description" : "The minimum expectations for ActivityDefinition resources used in SMART Guidelines",
      "exampleBoolean" : false,
      "groupingId" : "Conformance"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/SGActor"
      },
      "name" : "SMART Guidelines Actor",
      "description" : "Structure and constraints for ActorDefinition resources used in SMART Guidelines",
      "exampleBoolean" : false,
      "groupingId" : "Conformance"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/SGBusinessProcess"
      },
      "name" : "SMART Guidelines Business Process",
      "description" : "Structure and constraints for Business Processes represented in SMART Guidelines",
      "exampleBoolean" : false,
      "groupingId" : "Conformance"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/SGCodeSystem"
      },
      "name" : "SMART Guidelines CodeSystem",
      "description" : "Defines the minimum expectations for CodeSystem resources used in SMART Guidelines",
      "exampleBoolean" : false,
      "groupingId" : "Conformance"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/SGCommunicationRequest"
      },
      "name" : "SMART Guidelines Communication Request",
      "description" : "Provide communication",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/SGConceptMap"
      },
      "name" : "SMART Guidelines ConceptMap",
      "description" : "Defines the minimum expectations for ConceptMap resources used in SMART Guidelines",
      "exampleBoolean" : false,
      "groupingId" : "Conformance"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/SGDecisionTable"
      },
      "name" : "SMART Guidelines Decision Table",
      "description" : "Defines the minimum expectations for PlanDefinition resources used in SMART Guidelines which are derived from DAK Decision Tables",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/DecisionTableActions"
      },
      "name" : "Smart Guidelines Decision Table Actions",
      "description" : "Value Set for Smart Guidelines Documentation Decision Table Actions",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/DocumentationSection"
      },
      "name" : "Smart Guidelines Documentation Section",
      "description" : "Value Set for Smart Guidelines Documentation Section to autogenerate documentation from artifacts",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      }],
      "reference" : {
        "reference" : "CodeSystem/DocumentationSections"
      },
      "name" : "Smart Guidelines Documentation Section",
      "description" : "CodeSystem for Smart Guidelines Documentation Section to autogenerate documentation from artifacts",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/SGGraphDefinition"
      },
      "name" : "SMART Guidelines GraphDefinition",
      "description" : "The minimum expectations for GraphDefinition resources used in SMART Guidelines",
      "exampleBoolean" : false,
      "groupingId" : "Conformance"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/SGGroupDefinition"
      },
      "name" : "SMART Guidelines Group Definition",
      "description" : "Structure and constraints for Group Definitions represented in SMART Guidelines",
      "exampleBoolean" : false,
      "groupingId" : "Conformance"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/SGImplementationGuide"
      },
      "name" : "SMART Guidelines ImplementationGuide",
      "description" : "Defines the minimum expectations for ImplementationGuide resources used in SMART Guidelines",
      "exampleBoolean" : false,
      "groupingId" : "Conformance"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/SGLibrary"
      },
      "name" : "SMART Guidelines Library",
      "description" : "Defines the minimum expectations for Library resources used in SMART Guidelines",
      "exampleBoolean" : false,
      "groupingId" : "Conformance"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/SGLogicalModel"
      },
      "name" : "SMART Guidelines Logical Model",
      "description" : "Defines the minimum expectations for Logical Models used in SMART Guidelines",
      "exampleBoolean" : false,
      "groupingId" : "Conformance"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/SGMeasure"
      },
      "name" : "SMART Guidelines Measure",
      "description" : "Defines the minimum expectations for Measure resources used in SMART Guidelines",
      "exampleBoolean" : false,
      "groupingId" : "Conformance"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      }],
      "reference" : {
        "reference" : "CodeSystem/SGPersonaTypes"
      },
      "name" : "SMART Guidelines Persona Types",
      "description" : "CodeSystem for SMART Guidelines Persona Types",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "ValueSet"
      }],
      "reference" : {
        "reference" : "ValueSet/SGPersonaTypesVS"
      },
      "name" : "Smart Guidelines Persona Types Value Set",
      "description" : "Value Set for Smart Guidelines Persona Section to autogenerate documentation from artifacts",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/SGPlanDefinition"
      },
      "name" : "SMART Guidelines PlanDefinition",
      "description" : "Defines the minimum expectations for PlanDefinition resources used in SMART Guidelines",
      "exampleBoolean" : false,
      "groupingId" : "Conformance"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/SGQuestionnaire"
      },
      "name" : "SMART Guidelines Questionnaire",
      "description" : "Defines the minimum expectations for Questionnaire resources used in SMART Guidelines",
      "exampleBoolean" : false,
      "groupingId" : "Conformance"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/SGRequirements"
      },
      "name" : "SMART Guidelines Requirements",
      "description" : "Smart Guidelines Requirements",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/SGStructureDefinition"
      },
      "name" : "SMART Guidelines StructureDefinition",
      "description" : "Defines the minimum expectations for StructureDefinition resources used in SMART Guidelines",
      "exampleBoolean" : false,
      "groupingId" : "Conformance"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/SGStructureMap"
      },
      "name" : "SMART Guidelines StructureMap",
      "description" : "Defines the minimum expectations for StructureMap resources used in SMART Guidelines",
      "exampleBoolean" : false,
      "groupingId" : "Conformance"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "CodeSystem"
      }],
      "reference" : {
        "reference" : "CodeSystem/SGTasks"
      },
      "name" : "SMART Guidelines Tasks",
      "description" : "CodeSystem for SMART Guidelines tasks which are specializations of the Business Process Modeling Notatiton (BPMN) tasks, which are included in this codesystem\n\nSee [BPMN Spectification](https://www.omg.org/spec/BPMN) for more info.  The descriptions were adapted from the [normative human readable documentation](https://www.omg.org/spec/BPMN/2.0.2/PDF).",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/SGTransaction"
      },
      "name" : "SMART Guidelines Transaction",
      "description" : "Structure and constraints for TransactionDefinition resources used in SMART Guidelines",
      "exampleBoolean" : false,
      "groupingId" : "Conformance"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:resource"
      }],
      "reference" : {
        "reference" : "StructureDefinition/SGValueSet"
      },
      "name" : "SMART Guidelines ValueSet",
      "description" : "Defines the minimum expectations for ValueSet resources used in SMART Guidelines",
      "exampleBoolean" : false,
      "groupingId" : "Conformance"
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      }],
      "reference" : {
        "reference" : "StructureDefinition/SushiConfigLogicalModel"
      },
      "name" : "SUSHI Configuration Logical Model",
      "description" : "Logical model defining the structure of sushi-config.yaml files used for FHIR Implementation Guide configuration. This model captures the essential metadata and configuration parameters needed for IG publishing.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      }],
      "reference" : {
        "reference" : "StructureDefinition/TestScenario"
      },
      "name" : "Test Scenario (DAK)",
      "description" : "Logical Model for representing Test Scenarios from a DAK. A set of test scenarios to validate an implementation of the DAK.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      }],
      "reference" : {
        "reference" : "StructureDefinition/TestScenarioSource"
      },
      "name" : "Test Scenario Source",
      "description" : "Source reference for Test Scenario - exactly one of the following must be provided:\n- url (url data type): URL to retrieve TestScenario definition from input/ or external source\n- canonical (canonical data type): Canonical URI pointing to the TestScenario definition\n- instance: Inline TestScenario instance data",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      }],
      "reference" : {
        "reference" : "StructureDefinition/UserScenario"
      },
      "name" : "User Scenario (DAK)",
      "description" : "Logical Model for representing User Scenarios from a DAK. Narratives that describe how the different personas may interact with each other.",
      "exampleBoolean" : false
    },
    {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
        "valueString" : "StructureDefinition:logical"
      }],
      "reference" : {
        "reference" : "StructureDefinition/UserScenarioSource"
      },
      "name" : "User Scenario Source",
      "description" : "Source reference for User Scenario - exactly one of the following must be provided:\n- url (url data type): URL to retrieve UserScenario definition from input/ or external source\n- canonical (canonical data type): Canonical URI pointing to the UserScenario definition\n- instance: Inline UserScenario instance data",
      "exampleBoolean" : false
    }],
    "page" : {
      "extension" : [{
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
        "valueUrl" : "toc.html"
      }],
      "nameUrl" : "toc.html",
      "title" : "Table of Contents",
      "generation" : "html",
      "page" : [{
        "extension" : [{
          "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
          "valueUrl" : "index.html"
        }],
        "nameUrl" : "index.html",
        "title" : "Home",
        "generation" : "markdown"
      },
      {
        "extension" : [{
          "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
          "valueUrl" : "changes.html"
        }],
        "nameUrl" : "changes.html",
        "title" : "Changes",
        "generation" : "markdown"
      },
      {
        "extension" : [{
          "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
          "valueUrl" : "downloads.html"
        }],
        "nameUrl" : "downloads.html",
        "title" : "Downloads",
        "generation" : "markdown"
      },
      {
        "extension" : [{
          "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
          "valueUrl" : "license.html"
        }],
        "nameUrl" : "license.html",
        "title" : "License",
        "generation" : "markdown"
      },
      {
        "extension" : [{
          "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
          "valueUrl" : "dak-api.html"
        }],
        "nameUrl" : "dak-api.html",
        "title" : "DAK API Documentation Hub",
        "generation" : "markdown"
      }]
    },
    "parameter" : [{
      "code" : "path-resource",
      "value" : "input/capabilities"
    },
    {
      "code" : "path-resource",
      "value" : "input/examples"
    },
    {
      "code" : "path-resource",
      "value" : "input/extensions"
    },
    {
      "code" : "path-resource",
      "value" : "input/models"
    },
    {
      "code" : "path-resource",
      "value" : "input/operations"
    },
    {
      "code" : "path-resource",
      "value" : "input/profiles"
    },
    {
      "code" : "path-resource",
      "value" : "input/resources"
    },
    {
      "code" : "path-resource",
      "value" : "input/vocabulary"
    },
    {
      "code" : "path-resource",
      "value" : "input/maps"
    },
    {
      "code" : "path-resource",
      "value" : "input/testing"
    },
    {
      "code" : "path-resource",
      "value" : "input/history"
    },
    {
      "code" : "path-resource",
      "value" : "fsh-generated/resources"
    },
    {
      "code" : "path-pages",
      "value" : "template/config"
    },
    {
      "code" : "path-pages",
      "value" : "input/images"
    },
    {
      "code" : "path-tx-cache",
      "value" : "input-cache/txcache"
    }]
  }
}

```
