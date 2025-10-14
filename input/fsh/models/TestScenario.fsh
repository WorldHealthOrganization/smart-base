Logical: TestScenario
Title: "Test Scenario (DAK)"
Description: "Logical Model for representing Test Scenarios from a DAK. A set of test scenarios to validate an implementation of the DAK."

* ^status = #active
* ^publisher = "World Health Organization (WHO)"
* feature 1..1 uri "Feature File" "Link to a feature file containing the test scenarios"
* description[x] 0..1 string or uri "Description" "Description of the test scenario - either Markdown content or a URI to a Markdown file (absolute or relative to repository root)"