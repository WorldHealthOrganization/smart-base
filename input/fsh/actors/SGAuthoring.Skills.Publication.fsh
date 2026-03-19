Instance: SGAuthoring.Skills.ConfigureIG
InstanceOf: SGRequirements
Usage: #definition
* status = #draft
* experimental = true
* name = "SkillConfigureIG"
* title = "Skill: Can configure IG"
* description = "Capability to set up and configure a FHIR Implementation Guide (sushi-config, canonical URL, packages)."

* statement[+].key = "IGCFG-01"
* statement[=].label = "Fork IG template"
* statement[=].requirement = "Can fork the smart-ig-empty template repository using 'Use this Template' with 'Include all branches' to ensure gh-pages branch is cloned."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "IGCFG-02"
* statement[=].label = "Configure sushi-config.yaml"
* statement[=].requirement = "Can configure sushi-config.yaml with correct canonical URL (https://smart.who.int/<ig_code>), package ID (smart.who.int.<ig_code>), and dependencies."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "IGCFG-03"
* statement[=].label = "Enable GitHub Pages"
* statement[=].requirement = "Can enable GitHub Pages from the gh-pages branch and confirm repo allows GitHub Actions read/write access."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "IGCFG-04"
* statement[=].label = "Configure for national adaptations"
* statement[=].requirement = "Can configure package IDs for national adaptations following HL7 affiliate conventions (hl7.fhir.country.smart.<ig_code>)."
* statement[=].conformance[+] = #SHOULD


Instance: SGAuthoring.Skills.BuildIG
InstanceOf: SGRequirements
Usage: #definition
* status = #draft
* experimental = true
* name = "SkillBuildIG"
* title = "Skill: Can build IG"
* description = "Capability to run the FHIR IG Publisher build process and verify output."

* statement[+].key = "BUILD-01"
* statement[=].label = "Run IG Publisher locally"
* statement[=].requirement = "Can run the FHIR IG Publisher build process locally and interpret build output."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "BUILD-02"
* statement[=].label = "Verify GitHub Pages build"
* statement[=].requirement = "Can verify CI builds on GitHub Pages (org.github.io/repo for default branch, /branches/branch_name for other branches)."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "BUILD-03"
* statement[=].label = "Verify FHIR build"
* statement[=].requirement = "Can verify builds on build.fhir.org/ig/ for tooling and registry recognition."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "BUILD-04"
* statement[=].label = "Interpret build errors"
* statement[=].requirement = "Can interpret IG Publisher build errors and resolve common issues (missing dependencies, invalid references, SUSHI errors)."
* statement[=].conformance[+] = #SHALL


Instance: SGAuthoring.Skills.ManageReleases
InstanceOf: SGRequirements
Usage: #definition
* status = #draft
* experimental = true
* name = "SkillManageReleases"
* title = "Skill: Can manage releases"
* description = "Capability to manage versioning, publication-request.json, release tags, and publication workflow."

* statement[+].key = "REL-01"
* statement[=].label = "Determine version number"
* statement[=].requirement = "Can review changes since last release, determine if changes are breaking, and update version number following semantic versioning."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "REL-02"
* statement[=].label = "Update IG status for release"
* statement[=].requirement = "Can update IG and all conformance artifacts: status to active, version without label, releaseLabel to release, and date to current date."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "REL-03"
* statement[=].label = "Create publication-request.json"
* statement[=].requirement = "Can create a correct publication-request.json with matching package-id, version, path, ci-build, and first/subsequent flags."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "REL-04"
* statement[=].label = "Create release tag"
* statement[=].requirement = "Can create a GitHub release and tag in the form vX.Y.Z to trigger the automated publication workflow."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "REL-05"
* statement[=].label = "Verify publication"
* statement[=].requirement = "Can verify the publication workflow succeeded and the IG is available at the sitepreview URL."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "REL-06"
* statement[=].label = "Reset to draft"
* statement[=].requirement = "Can reset the main branch to draft status with updated version number after publication."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "REL-07"
* statement[=].label = "Maintain change log"
* statement[=].requirement = "Can maintain a changes page with release summary, known issues, and categorized changes (non-compatible, compatible substantive, non-substantive)."
* statement[=].conformance[+] = #SHALL


Instance: SGAuthoring.Skills.ManageGovernance
InstanceOf: SGRequirements
Usage: #definition
* status = #draft
* experimental = true
* name = "SkillManageGovernance"
* title = "Skill: Can manage governance"
* description = "Capability to manage cross-IG governance for shared artifacts including common personas, terminology, and libraries."

* statement[+].key = "GOV-01"
* statement[=].label = "Manage shared artifact lifecycle"
* statement[=].requirement = "Can manage the lifecycle of shared artifacts (common personas, terminology, CQL libraries) across multiple SMART Guidelines IGs."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "GOV-02"
* statement[=].label = "Coordinate concept approval"
* statement[=].requirement = "Can coordinate the approval process for new concepts being onboarded into the WHO Commons dictionary."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "GOV-03"
* statement[=].label = "Track cross-IG dependencies"
* statement[=].requirement = "Can track and manage dependencies between IGs and shared artifact repositories."
* statement[=].conformance[+] = #SHALL

* statement[+].key = "GOV-04"
* statement[=].label = "Coordinate smart.who.int updates"
* statement[=].requirement = "Can coordinate with the WHO SMART Guidelines team (smart@who.int) for website updates and package list pull requests."
* statement[=].conformance[+] = #SHALL
