# Home - SMART Base v0.2.0

* [**Table of Contents**](toc.md)
* **Home**

## Home

| | |
| :--- | :--- |
| *Official URL*:http://smart.who.int/base/ImplementationGuide/smart.who.int.base | *Version*:0.2.0 |
| Draft as of 2025-10-14 | *Computable Name*:Base |

### Overview

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




## Resource Content

```json
{
  "resourceType" : "ImplementationGuide",
  "id" : "smart.who.int.base",
  "meta" : {
    "profile" : [
      "http://smart.who.int/base/StructureDefinition/SGImplementationGuide"
    ]
  },
  "url" : "http://smart.who.int/base/ImplementationGuide/smart.who.int.base",
  "version" : "0.2.0",
  "name" : "Base",
  "title" : "SMART Base",
  "status" : "draft",
  "experimental" : false,
  "date" : "2025-10-14T12:39:49+00:00",
  "publisher" : "WHO",
  "contact" : [
    {
      "name" : "WHO",
      "telecom" : [
        {
          "system" : "url",
          "value" : "http://who.int"
        }
      ]
    }
  ],
  "description" : "Base SMART Guidelines implementation guide to be used as the base dependency for all SMART Guidelines IGs",
  "packageId" : "smart.who.int.base",
  "license" : "CC-BY-SA-3.0-IGO",
  "fhirVersion" : ["4.0.1"],
  "dependsOn" : [
    {
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
      "extension" : [
        {
          "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ImplementationGuide.dependsOn.reason",
          "valueMarkdown" : "This IG uses CQL profiles and capabilities provided by the Using CQL With FHIR IG"
        }
      ],
      "uri" : "http://hl7.org/fhir/uv/cql/ImplementationGuide/hl7.fhir.uv.cql",
      "packageId" : "hl7.fhir.uv.cql",
      "version" : "1.0.0"
    },
    {
      "id" : "cpg",
      "extension" : [
        {
          "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ImplementationGuide.dependsOn.reason",
          "valueMarkdown" : "For Decision Tables"
        }
      ],
      "uri" : "http://hl7.org/fhir/uv/cpg/ImplementationGuide/hl7.fhir.uv.cpg",
      "packageId" : "hl7.fhir.uv.cpg",
      "version" : "2.0.0"
    },
    {
      "id" : "crmi",
      "extension" : [
        {
          "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ImplementationGuide.dependsOn.reason",
          "valueMarkdown" : "This IG uses content management profiles and capabilities provided by the Canonical Resource Management Infrastructure (CRMI) IG"
        }
      ],
      "uri" : "http://hl7.org/fhir/uv/crmi/ImplementationGuide/hl7.fhir.uv.crmi",
      "packageId" : "hl7.fhir.uv.crmi",
      "version" : "1.0.0"
    },
    {
      "id" : "sdc",
      "extension" : [
        {
          "url" : "http://hl7.org/fhir/5.0/StructureDefinition/extension-ImplementationGuide.dependsOn.reason",
          "valueMarkdown" : "This IG uses questionnaire profiles and capabilities provided by the Structure Data Capture (SDC) IG"
        }
      ],
      "uri" : "http://hl7.org/fhir/uv/sdc/ImplementationGuide/hl7.fhir.uv.sdc",
      "packageId" : "hl7.fhir.uv.sdc",
      "version" : "3.0.0"
    }
  ],
  "definition" : {
    "extension" : [
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "copyrightyear"
          },
          {
            "url" : "value",
            "valueString" : "2023+"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "releaselabel"
          },
          {
            "url" : "value",
            "valueString" : "ci-build"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "autoload-resources"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "path-liquid"
          },
          {
            "url" : "value",
            "valueString" : "template/liquid"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "path-liquid"
          },
          {
            "url" : "value",
            "valueString" : "input/liquid"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "path-qa"
          },
          {
            "url" : "value",
            "valueString" : "temp/qa"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "path-temp"
          },
          {
            "url" : "value",
            "valueString" : "temp/pages"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "path-output"
          },
          {
            "url" : "value",
            "valueString" : "output"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "path-suppressed-warnings"
          },
          {
            "url" : "value",
            "valueString" : "input/ignoreWarnings.txt"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "path-history"
          },
          {
            "url" : "value",
            "valueString" : "http://smart.who.int/base/history.html"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "template-html"
          },
          {
            "url" : "value",
            "valueString" : "template-page.html"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "template-md"
          },
          {
            "url" : "value",
            "valueString" : "template-page-md.html"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "apply-contact"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "apply-context"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "apply-copyright"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "apply-jurisdiction"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "apply-license"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "apply-publisher"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "apply-version"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "apply-wg"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "active-tables"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "fmm-definition"
          },
          {
            "url" : "value",
            "valueString" : "http://hl7.org/fhir/versions.html#maturity"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "propagate-status"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "excludelogbinaryformat"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueString" : "tabbed-snapshots"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-internal-dependency",
        "valueCode" : "hl7.fhir.uv.tools.r4#0.8.0"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "copyrightyear"
          },
          {
            "url" : "value",
            "valueString" : "2023+"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "releaselabel"
          },
          {
            "url" : "value",
            "valueString" : "ci-build"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "autoload-resources"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "path-liquid"
          },
          {
            "url" : "value",
            "valueString" : "template/liquid"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "path-liquid"
          },
          {
            "url" : "value",
            "valueString" : "input/liquid"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "path-qa"
          },
          {
            "url" : "value",
            "valueString" : "temp/qa"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "path-temp"
          },
          {
            "url" : "value",
            "valueString" : "temp/pages"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "path-output"
          },
          {
            "url" : "value",
            "valueString" : "output"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "path-suppressed-warnings"
          },
          {
            "url" : "value",
            "valueString" : "input/ignoreWarnings.txt"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "path-history"
          },
          {
            "url" : "value",
            "valueString" : "http://smart.who.int/base/history.html"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "template-html"
          },
          {
            "url" : "value",
            "valueString" : "template-page.html"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "template-md"
          },
          {
            "url" : "value",
            "valueString" : "template-page-md.html"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "apply-contact"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "apply-context"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "apply-copyright"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "apply-jurisdiction"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "apply-license"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "apply-publisher"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "apply-version"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "apply-wg"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "active-tables"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "fmm-definition"
          },
          {
            "url" : "value",
            "valueString" : "http://hl7.org/fhir/versions.html#maturity"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "propagate-status"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "excludelogbinaryformat"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      },
      {
        "extension" : [
          {
            "url" : "code",
            "valueCode" : "tabbed-snapshots"
          },
          {
            "url" : "value",
            "valueString" : "true"
          }
        ],
        "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-parameter"
      }
    ],
    "grouping" : [
      {
        "id" : "Conformance",
        "name" : "Conformance",
        "description" : "constraints and profile structures for SMART Guidelines resources"
      }
    ],
    "resource" : [
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:logical"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/BusinessProcessWorkflow"
        },
        "name" : "Business Process Workflow (DAK)",
        "description" : "Logical Model for representing Generic Business Processes and Workflows from a DAK. A business process is a set of related activities or tasks performed together to achieve the objectives of the health programme area.",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:logical"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/BusinessProcessWorkflowSource"
        },
        "name" : "Business Process Workflow Source",
        "description" : "Source reference for Business Process Workflow - exactly one of the following must be provided:\n- url (url data type): URL to retrieve BusinessProcessWorkflow definition from input/ or external source\n- canonical (canonical data type): Canonical URI pointing to the BusinessProcessWorkflow definition\n- instance: Inline BusinessProcessWorkflow instance data",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "ValueSet"
          }
        ],
        "reference" : {
          "reference" : "ValueSet/CDHIv1"
        },
        "name" : "Classification of Digital Health Interventions v1",
        "description" : "Value Set for Classification of Digital Health Interventions v1. Autogenerated from DAK artifacts",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "CodeSystem"
          }
        ],
        "reference" : {
          "reference" : "CodeSystem/CDHIv1"
        },
        "name" : "Classification of Digital Health Interventions v1",
        "description" : "CodeSystem for Classification of Digital Health Interventions v1. Autogenerated from DAK artifacts",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "ValueSet"
          }
        ],
        "reference" : {
          "reference" : "ValueSet/CDSCv1"
        },
        "name" : "Classification of Digital Health System Categories v1",
        "description" : "Value Set for Classification of Digital Health System Categories v1. Autogenerated from DAK artifacts",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "CodeSystem"
          }
        ],
        "reference" : {
          "reference" : "CodeSystem/CDSCv1"
        },
        "name" : "Classification of Digital Health System Categories v1",
        "description" : "CodeSystem for Classification of Digital Health System Categories v1. Autogenerated from DAK artifacts",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:logical"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/CoreDataElement"
        },
        "name" : "Core Data Element (DAK)",
        "description" : "Logical Model for representing Core Data Elements from a DAK. A core data element can be one of: a ValueSet, a CodeSystem, a ConceptMap, or a Logical Model adherent to SGLogicalModel. This is the ONE EXCEPTION to allowing FHIR R4 models into the DAK LMs.",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:logical"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/CoreDataElementSource"
        },
        "name" : "Core Data Element Source",
        "description" : "Source reference for Core Data Element - exactly one of the following must be provided:\n- url (url data type): URL to retrieve CoreDataElement definition from input/ or external source\n- canonical (canonical data type): Canonical URI pointing to the CoreDataElement definition\n- instance: Inline CoreDataElement instance data",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "CodeSystem"
          }
        ],
        "reference" : {
          "reference" : "CodeSystem/CoreDataElementType"
        },
        "name" : "Core Data Element Type",
        "description" : "CodeSystem for Core Data Element types - defines the type of FHIR resource that a Core Data Element references.",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "ValueSet"
          }
        ],
        "reference" : {
          "reference" : "ValueSet/CoreDataElementTypeVS"
        },
        "name" : "Core Data Element Type Value Set",
        "description" : "Value set of core data element types",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:logical"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/DecisionSupportLogicSource"
        },
        "name" : "Decision Support Logic Source",
        "description" : "Source reference for Decision Support Logic - exactly one of the following must be provided:\n- url (url data type): URL to retrieve DecisionSupportLogic definition from input/ or external source\n- canonical (canonical data type): Canonical URI pointing to the DecisionSupportLogic definition\n- instance: Inline DecisionSupportLogic instance data",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:logical"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/DecisionSupportLogic"
        },
        "name" : "Decision-Support Logic (DAK)",
        "description" : "Logical Model for representing Decision-Support Logic from a DAK. Decision-support logic and algorithms to support appropriate service delivery in accordance with WHO clinical, public health and data use guidelines.",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:logical"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/DAK"
        },
        "name" : "Digital Adaptation Kit (DAK)",
        "description" : "Logical Model for representing a complete Digital Adaptation Kit (DAK) with metadata and all 9 DAK components",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:logical"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/DublinCore"
        },
        "name" : "Dublin Core Metadata Element Set",
        "description" : "Logical Model representing Dublin Core metadata elements as defined at https://www.dublincore.org/specifications/dublin-core/dcmi-terms/",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:logical"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/Requirements"
        },
        "name" : "Functional and Non-Functional Requirements (DAK)",
        "description" : "Logical Model for representing Functional and Non-Functional Requirements from a DAK. A high-level list of core functions and capabilities that the system must have to meet the end users' needs.",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:logical"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/FunctionalRequirement"
        },
        "name" : "Functional Requirement (DAK)",
        "description" : "Logical Model for representing functional requirement from a DAK",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:logical"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/GenericPersona"
        },
        "name" : "Generic Persona (DAK)",
        "description" : "Logical Model for representing Generic Personas from a DAK. Depiction of the human and system actors. Human actors are end users, supervisors and related stakeholders who would be interacting with the digital system or involved in the clinical care, public health or health system pathway.",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:logical"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/GenericPersonaSource"
        },
        "name" : "Generic Persona Source",
        "description" : "Source reference for Generic Persona - exactly one of the following must be provided:\n- url (url data type): URL to retrieve GenericPersona definition from input/ or external source\n- canonical (canonical data type): Canonical URI pointing to the GenericPersona definition\n- instance: Inline GenericPersona instance data",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:logical"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/HealthInterventions"
        },
        "name" : "Health Interventions and Recommendations (DAK)",
        "description" : "Logical Model for representing Health Interventions and Recommendations from a DAK. Overview of the health interventions and WHO, regional or national recommendations included within the DAK.",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:logical"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/HealthInterventionsSource"
        },
        "name" : "Health Interventions Source",
        "description" : "Source reference for Health Interventions - exactly one of the following must be provided:\n- url (url data type): URL to retrieve HealthInterventions definition from input/ or external source\n- canonical (canonical data type): Canonical URI pointing to the HealthInterventions definition\n- instance: Inline HealthInterventions instance data",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "ConceptMap"
          }
        ],
        "reference" : {
          "reference" : "ConceptMap/CDHIv1Hierarchy"
        },
        "name" : "Hierarchy of the Classification of Digital Health Interventions v1",
        "description" : "Mapping to represent hierarchy within Hierarchy of the Classification of Digital Health Interventions v1.",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "CodeSystem"
          }
        ],
        "reference" : {
          "reference" : "CodeSystem/ISCO08"
        },
        "name" : "International Standard Classification of Occupations 2008",
        "description" : "ISCO-08 codes from the International Labour Organization official classification",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "ValueSet"
          }
        ],
        "reference" : {
          "reference" : "ValueSet/ISCO08ValueSet"
        },
        "name" : "ISCO-08 Value Set",
        "description" : "Extensible value set of ISCO-08 codes for persona classification",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:extension"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/LinkIdExt"
        },
        "name" : "LinkIdExt",
        "description" : "Smart Guidelines link identifier extension",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:extension"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/Markdown"
        },
        "name" : "Markdown",
        "description" : "Markdown extension",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:logical"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/NonFunctionalRequirement"
        },
        "name" : "Non-Functional Requirement (DAK)",
        "description" : "Logical Model for representing non-functional requirement from a DAK",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:logical"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/Persona"
        },
        "name" : "Persona (DAK)",
        "description" : "Logical Model for representing Personas from a DAK",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:logical"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/ProgramIndicator"
        },
        "name" : "Program Indicator (DAK)",
        "description" : "Logical Model for representing Program Indicators from a DAK. Core set of indicators that need to be aggregated for decision-making, performance metrics and subnational and national reporting.",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:logical"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/ProgramIndicatorSource"
        },
        "name" : "Program Indicator Source",
        "description" : "Source reference for Program Indicator - exactly one of the following must be provided:\n- url (url data type): URL to retrieve ProgramIndicator definition from input/ or external source\n- canonical (canonical data type): Canonical URI pointing to the ProgramIndicator definition\n- instance: Inline ProgramIndicator instance data",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "Questionnaire"
          }
        ],
        "reference" : {
          "reference" : "Questionnaire/DAK.DT.IMMZ.D2.DT.BCGQuestionnaire"
        },
        "name" : "Questionnaire for IMMZ.D2 Determine required vaccination(s) if any",
        "description" : "Auto-generated questionnaire for decision table DAK.DT.IMMZ.D2.DT.BCG",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:logical"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/RequirementsSource"
        },
        "name" : "Requirements Source",
        "description" : "Source reference for Requirements - exactly one of the following must be provided:\n- url (url data type): URL to retrieve Requirements definition from input/ or external source\n- canonical (canonical data type): Canonical URI pointing to the Requirements definition\n- instance: Inline Requirements instance data",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:extension"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/Satisfies"
        },
        "name" : "Satisfies",
        "description" : "Indicates that if the conditions for this requirement are satisified, then that it should be viewed as satisifying  the referenced requirement.",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:extension"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/SGActorExt"
        },
        "name" : "SGActorExt",
        "description" : "Smart Guidelines Actor Reference extension",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:extension"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/SGcode"
        },
        "name" : "SGcode",
        "description" : "Smart Guidelines code extension",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "ActivityDefinition"
          }
        ],
        "reference" : {
          "reference" : "ActivityDefinition/SGDecisionTableGuidance"
        },
        "name" : "SGDecisionTableGuidance",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:extension"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/SGDocumentation"
        },
        "name" : "SGDocumentation",
        "description" : "Smart Guidelines Documentation extension",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:extension"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/SGMarkdown"
        },
        "name" : "SGMarkdown",
        "description" : "Smart Guidelines markdown extension",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:extension"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/SGRequirementExt"
        },
        "name" : "SGRequirementExt",
        "description" : "Smart Guidelines Requirements extension",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:extension"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/SGString"
        },
        "name" : "SGString",
        "description" : "Smart Guidelines (required) string extension for use in a complex extension",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:extension"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/SGTask"
        },
        "name" : "SGTask",
        "description" : "Extension to reference SMART Guidelines task type",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:extension"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/SGUserStory"
        },
        "name" : "SGUserStory",
        "description" : "Smart Guidelines extension to support structured User Stories (As a <Actor> I want to <capability> so that <benfit>) extension",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "CodeSystem"
          }
        ],
        "reference" : {
          "reference" : "CodeSystem/DecisionTableActions"
        },
        "name" : "Smart Guidelines Actions (columns) for Decision Tables",
        "description" : "CodeSystem for Smart Guidelines Documentation Actions for Decision Tables\"",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:resource"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/SGActivityDefinition"
        },
        "name" : "SMART Guidelines ActivityDefinition",
        "description" : "The minimum expectations for ActivityDefinition resources used in SMART Guidelines",
        "exampleBoolean" : false,
        "groupingId" : "Conformance"
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:resource"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/SGActor"
        },
        "name" : "SMART Guidelines Actor",
        "description" : "Structure and constraints for ActorDefinition resources used in SMART Guidelines",
        "exampleBoolean" : false,
        "groupingId" : "Conformance"
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:resource"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/SGBusinessProcess"
        },
        "name" : "SMART Guidelines Business Process",
        "description" : "Structure and constraints for Business Processes represented in SMART Guidelines",
        "exampleBoolean" : false,
        "groupingId" : "Conformance"
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:resource"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/SGCodeSystem"
        },
        "name" : "SMART Guidelines CodeSystem",
        "description" : "Defines the minimum expectations for CodeSystem resources used in SMART Guidelines",
        "exampleBoolean" : false,
        "groupingId" : "Conformance"
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:resource"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/SGCommunicationRequest"
        },
        "name" : "SMART Guidelines Communication Request",
        "description" : "Provide communication",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:resource"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/SGConceptMap"
        },
        "name" : "SMART Guidelines ConceptMap",
        "description" : "Defines the minimum expectations for ConceptMap resources used in SMART Guidelines",
        "exampleBoolean" : false,
        "groupingId" : "Conformance"
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:resource"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/SGDecisionTable"
        },
        "name" : "SMART Guidelines Decision Table",
        "description" : "Defines the minimum expectations for PlanDefinition resources used in SMART Guidelines which are derived from DAK Decision Tables",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "ValueSet"
          }
        ],
        "reference" : {
          "reference" : "ValueSet/DecisionTableActions"
        },
        "name" : "Smart Guidelines Decision Table Actions",
        "description" : "Value Set for Smart Guidelines Documentation Decision Table Actions",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "ValueSet"
          }
        ],
        "reference" : {
          "reference" : "ValueSet/DocumentationSection"
        },
        "name" : "Smart Guidelines Documentation Section",
        "description" : "Value Set for Smart Guidelines Documentation Section to autogenerate documentation from artifacts",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "CodeSystem"
          }
        ],
        "reference" : {
          "reference" : "CodeSystem/DocumentationSections"
        },
        "name" : "Smart Guidelines Documentation Section",
        "description" : "CodeSystem for Smart Guidelines Documentation Section to autogenerate documentation from artifacts",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:resource"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/SGGraphDefinition"
        },
        "name" : "SMART Guidelines GraphDefinition",
        "description" : "The minimum expectations for GraphDefinition resources used in SMART Guidelines",
        "exampleBoolean" : false,
        "groupingId" : "Conformance"
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:resource"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/SGGroupDefinition"
        },
        "name" : "SMART Guidelines Group Definition",
        "description" : "Structure and constraints for Group Definitions represented in SMART Guidelines",
        "exampleBoolean" : false,
        "groupingId" : "Conformance"
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:resource"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/SGImplementationGuide"
        },
        "name" : "SMART Guidelines ImplementationGuide",
        "description" : "Defines the minimum expectations for ImplementationGuide resources used in SMART Guidelines",
        "exampleBoolean" : false,
        "groupingId" : "Conformance"
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:resource"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/SGLibrary"
        },
        "name" : "SMART Guidelines Library",
        "description" : "Defines the minimum expectations for Library resources used in SMART Guidelines",
        "exampleBoolean" : false,
        "groupingId" : "Conformance"
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:resource"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/SGLogicalModel"
        },
        "name" : "SMART Guidelines Logical Model",
        "description" : "Defines the minimum expectations for Logical Models used in SMART Guidelines",
        "exampleBoolean" : false,
        "groupingId" : "Conformance"
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:resource"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/SGMeasure"
        },
        "name" : "SMART Guidelines Measure",
        "description" : "Defines the minimum expectations for Measure resources used in SMART Guidelines",
        "exampleBoolean" : false,
        "groupingId" : "Conformance"
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "CodeSystem"
          }
        ],
        "reference" : {
          "reference" : "CodeSystem/SGPersonaTypes"
        },
        "name" : "SMART Guidelines Persona Types",
        "description" : "CodeSystem for SMART Guidelines Persona Types",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "ValueSet"
          }
        ],
        "reference" : {
          "reference" : "ValueSet/SGPersonaTypesVS"
        },
        "name" : "Smart Guidelines Persona Types Value Set",
        "description" : "Value Set for Smart Guidelines Persona Section to autogenerate documentation from artifacts",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:resource"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/SGPlanDefinition"
        },
        "name" : "SMART Guidelines PlanDefinition",
        "description" : "Defines the minimum expectations for PlanDefinition resources used in SMART Guidelines",
        "exampleBoolean" : false,
        "groupingId" : "Conformance"
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:resource"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/SGQuestionnaire"
        },
        "name" : "SMART Guidelines Questionnaire",
        "description" : "Defines the minimum expectations for Questionnaire resources used in SMART Guidelines",
        "exampleBoolean" : false,
        "groupingId" : "Conformance"
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:resource"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/SGRequirements"
        },
        "name" : "SMART Guidelines Requirements",
        "description" : "Smart Guidelines Requirements",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:resource"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/SGStructureDefinition"
        },
        "name" : "SMART Guidelines StructureDefinition",
        "description" : "Defines the minimum expectations for StructureDefinition resources used in SMART Guidelines",
        "exampleBoolean" : false,
        "groupingId" : "Conformance"
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:resource"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/SGStructureMap"
        },
        "name" : "SMART Guidelines StructureMap",
        "description" : "Defines the minimum expectations for StructureMap resources used in SMART Guidelines",
        "exampleBoolean" : false,
        "groupingId" : "Conformance"
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "CodeSystem"
          }
        ],
        "reference" : {
          "reference" : "CodeSystem/SGTasks"
        },
        "name" : "SMART Guidelines Tasks",
        "description" : "CodeSystem for SMART Guidelines tasks which are specializations of the Business Process Modeling Notatiton (BPMN) tasks, which are included in this codesystem\n\nSee [BPMN Spectification](https://www.omg.org/spec/BPMN) for more info.  The descriptions were adapted from the [normative human readable documentation](https://www.omg.org/spec/BPMN/2.0.2/PDF).",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:resource"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/SGTransaction"
        },
        "name" : "SMART Guidelines Transaction",
        "description" : "Structure and constraints for TransactionDefinition resources used in SMART Guidelines",
        "exampleBoolean" : false,
        "groupingId" : "Conformance"
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:resource"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/SGValueSet"
        },
        "name" : "SMART Guidelines ValueSet",
        "description" : "Defines the minimum expectations for ValueSet resources used in SMART Guidelines",
        "exampleBoolean" : false,
        "groupingId" : "Conformance"
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:logical"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/SushiConfigLogicalModel"
        },
        "name" : "SUSHI Configuration Logical Model",
        "description" : "Logical model defining the structure of sushi-config.yaml files used for FHIR Implementation Guide configuration. This model captures the essential metadata and configuration parameters needed for IG publishing.",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:logical"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/TestScenario"
        },
        "name" : "Test Scenario (DAK)",
        "description" : "Logical Model for representing Test Scenarios from a DAK. A set of test scenarios to validate an implementation of the DAK.",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:logical"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/TestScenarioSource"
        },
        "name" : "Test Scenario Source",
        "description" : "Source reference for Test Scenario - exactly one of the following must be provided:\n- url (url data type): URL to retrieve TestScenario definition from input/ or external source\n- canonical (canonical data type): Canonical URI pointing to the TestScenario definition\n- instance: Inline TestScenario instance data",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:logical"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/UserScenario"
        },
        "name" : "User Scenario (DAK)",
        "description" : "Logical Model for representing User Scenarios from a DAK. Narratives that describe how the different personas may interact with each other.",
        "exampleBoolean" : false
      },
      {
        "extension" : [
          {
            "url" : "http://hl7.org/fhir/tools/StructureDefinition/resource-information",
            "valueString" : "StructureDefinition:logical"
          }
        ],
        "reference" : {
          "reference" : "StructureDefinition/UserScenarioSource"
        },
        "name" : "User Scenario Source",
        "description" : "Source reference for User Scenario - exactly one of the following must be provided:\n- url (url data type): URL to retrieve UserScenario definition from input/ or external source\n- canonical (canonical data type): Canonical URI pointing to the UserScenario definition\n- instance: Inline UserScenario instance data",
        "exampleBoolean" : false
      }
    ],
    "page" : {
      "extension" : [
        {
          "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
          "valueUrl" : "toc.html"
        }
      ],
      "nameUrl" : "toc.html",
      "title" : "Table of Contents",
      "generation" : "html",
      "page" : [
        {
          "extension" : [
            {
              "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
              "valueUrl" : "index.html"
            }
          ],
          "nameUrl" : "index.html",
          "title" : "Home",
          "generation" : "markdown"
        },
        {
          "extension" : [
            {
              "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
              "valueUrl" : "changes.html"
            }
          ],
          "nameUrl" : "changes.html",
          "title" : "Changes",
          "generation" : "markdown"
        },
        {
          "extension" : [
            {
              "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
              "valueUrl" : "downloads.html"
            }
          ],
          "nameUrl" : "downloads.html",
          "title" : "Downloads",
          "generation" : "markdown"
        },
        {
          "extension" : [
            {
              "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
              "valueUrl" : "license.html"
            }
          ],
          "nameUrl" : "license.html",
          "title" : "License",
          "generation" : "markdown"
        },
        {
          "extension" : [
            {
              "url" : "http://hl7.org/fhir/tools/StructureDefinition/ig-page-name",
              "valueUrl" : "dak-api.html"
            }
          ],
          "nameUrl" : "dak-api.html",
          "title" : "DAK API Documentation Hub",
          "generation" : "markdown"
        }
      ]
    },
    "parameter" : [
      {
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
      }
    ]
  }
}

```
