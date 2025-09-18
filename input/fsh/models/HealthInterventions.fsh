Logical: HealthInterventions
Title: "Health Interventions and Recommendations (DAK)"
Description: "Logical Model for representing Health Interventions and Recommendations from a DAK. Overview of the health interventions and WHO, regional or national recommendations included within the DAK."

* ^status = #active
* id 1..1 id "Health Intervention ID" "An identifier for the health intervention"
* description[x] 0..1 string or uri "Description" "Description of the health intervention - either Markdown content or a URI to a Markdown file (absolute or relative to repository root)"
* reference 1..* DublinCore "Reference" "Reference data element using Dublin Core metadata"