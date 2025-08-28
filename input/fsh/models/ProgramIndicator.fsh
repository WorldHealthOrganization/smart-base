Logical: ProgramIndicator
Title: "Program Indicator (DAK)"
Description: "Logical Model for representing Program Indicators from a DAK. Core set of indicators that need to be aggregated for decision-making, performance metrics and subnational and national reporting."

* ^status = #active
* id 1..1 id "Indicator ID" "Identifier for the program indicator"
* name 1..1 string "Name" "Name of the indicator"
* definition 1..1 string "Definition" "Definition of what the indicator measures"
* numerator 1..1 string "Numerator" "Description of the numerator calculation"
* denominator 1..1 string "Denominator" "Description of the denominator calculation"
* disaggregation 1..1 string "Disaggregation" "Description of how the indicator should be disaggregated"
* references 0..* string "References" "References to Dublin Core metadata elements providing additional context"