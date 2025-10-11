### Overview

This implementation guide contains base conformance resources for use in all WHO SMART Guidelines implementation guides.

See the [SMART IG Starter Kit](https://smart.who.int/ig-starter-kit/) for more information on building and using WHO SMART Guidelines.

### DAK (Digital Adaptation Kit) Repository Detection

This repository contains a `dak.json` file in the root directory, which serves as the primary indicator that this is a WHO SMART Guidelines DAK repository. External tools and applications should check for the presence of `dak.json` when scanning repositories to determine if they contain DAK content. This approach avoids unnecessary 404 errors that would occur when checking for `sushi-config.yaml`, which is present in all FHIR Implementation Guides, not just DAK repositories.

For detailed guidance on detecting DAK repositories programmatically, see the [DAK Repository Detection Guide](https://github.com/WorldHealthOrganization/smart-base/blob/main/.github/DAK-REPOSITORY-DETECTION.md).

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