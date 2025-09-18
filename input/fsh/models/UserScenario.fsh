Logical: UserScenario
Title: "User Scenario (DAK)"
Description: "Logical Model for representing User Scenarios from a DAK. Narratives that describe how the different personas may interact with each other."

* ^status = #active
* title 1..1 string "Title" "Title of the user scenario"
* id 1..1 id "Scenario ID" "An identifier for the user scenario"
* description 1..1 string "Description" "Description of the scenario, either Markdown content or a URI to a Markdown file. The URL could be absolute or relative to the root of the DAK, like input/pagecontent/scenario-XYZ.md"
* personas 0..* id "Personas" "References to persona IDs that participate in this scenario"