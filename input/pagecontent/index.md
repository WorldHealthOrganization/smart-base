{% include smart.liquid %}

### Overview

**WHO SMART Guidelines** (Standards-based, Machine-readable, Adaptive, Requirements-based, and Testable) are a set of WHO clinical guidelines that have been transformed into a computable, interoperable format. They enable countries to rapidly adopt, adapt, and implement WHO recommendations within their digital health systems by providing structured, machine-readable clinical content.

A **Digital Adaptation Kit (DAK)** is the primary artefact of WHO SMART Guidelines. It is a structured, standardised package of clinical and operational content that represents a WHO health intervention in a computable form. Each DAK contains:

- **Health interventions and recommendations** – the clinical guidance from WHO
- **Generic personas** – representative end-users and actors in the health system
- **User scenarios** – narrative descriptions of how the guidance is used in practice
- **Business processes and workflows** – step-by-step care pathways
- **Core data elements** – the data dictionary for the health domain
- **Decision-support logic** – computable clinical decision rules
- **Functional and non-functional requirements** – system capability requirements
- **Program indicators** – aggregate measures and metrics for monitoring and evaluation
- **Test scenarios** – structured tests to validate conformance

The diagram below illustrates the nine components of a WHO DAK and how they relate to one another:

<figure>
  <img src="L2_DAK_components_3x3_logoimage.svg"
       alt="WHO Digital Adaptation Kit – nine-component overview diagram"
       style="width:40em; max-width:100%; height:auto;" />
  <figcaption>Figure 1 – The nine components of a WHO Digital Adaptation Kit (DAK)</figcaption>
</figure>

This implementation guide contains base conformance resources for use in all WHO SMART Guidelines implementation guides.

See the [SMART IG Starter Kit](https://smart.who.int/ig-starter-kit/) for more information on building and using WHO SMART Guidelines.

### DAK (Digital Adaptation Kit) URL Handling

For repositories that contain a `dak.json` file in the root directory, this implementation guide provides enhanced URL handling for publication and preview scenarios:

#### Publication URLs
- **WHO Repositories**: For repositories owned by `WorldHealthOrganization`, the publication URL follows the pattern `https://smart.who.int/{stub}` where `{stub}` is the repository name with any `smart-` prefix removed.
- **Other Repositories**: Use the canonical URL specified in `sushi-config.yaml` or fall back to GitHub Pages pattern.

#### Preview URLs  
- **All Repositories**: Preview URLs use the GitHub Pages pattern `https://{profile}.github.io/{repo}` for current CI builds.

#### Branch-Based URL Selection
- **Release Branches** (prefixed with `release-`): Use publication URLs for canonical references and resource identifiers.
- **Development Branches**: Use preview URLs for canonical references and resource identifiers.

The DAK configuration is automatically regenerated during CI builds to ensure URLs are appropriate for the current branch context.

### Dependencies

{% include dependency-table-short.xhtml %}

### Cross Version Analysis

{% include cross-version-analysis.xhtml %}

### Global Profiles

{% include globals-table.xhtml %}

### IP Statements

{% include ip-statements.xhtml %}