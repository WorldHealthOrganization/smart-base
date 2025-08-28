Logical: UserScenario
Title: "User Scenario (DAK)"
Description: "Logical Model for representing User Scenarios from a DAK. Narratives that describe how the different personas may interact with each other."

* ^status = #active
* title 1..1 string "Title" "Title of the user scenario"
* id 1..1 id "Scenario ID" "An identifier for the user scenario"
* personas 0..* string "Personas" "References to persona IDs that participate in this scenario"