Logical: ProgramIndicator
Parent: SGLogicalModel
Title: "Program Indicator (DAK)"
Description: "Logical Model for representing Program Indicators from a DAK. Core set of indicators that need to be aggregated for decision-making, performance metrics and subnational and national reporting."

* ^status = #active
* ^publisher = "World Health Organization (WHO)"
* id 1..1 id "Indicator ID" "Identifier for the program indicator"
* description[x] 0..1 string or uri "Description" "Description of the program indicator - either Markdown content or a URI to a Markdown file (absolute or relative to repository root)"
* name 1..1 string "Name" "Name of the indicator"
* definition 1..1 markdown "Definition" "Definition of what the indicator measures"
* numerator 1..1 markdown "Numerator" "Description of the numerator calculation"
* denominator 1..1 markdown "Denominator" "Description of the denominator calculation"
* disaggregation 1..1 markdown "Disaggregation" "Description of how the indicator should be disaggregated"
* references 0..* id "References" "References to Health Intervention IDs providing additional context"