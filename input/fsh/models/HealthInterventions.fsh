Logical: HealthInterventions
Title: "Health Interventions and Recommendations (DAK)"
Description: "Logical Model for representing Health Interventions and Recommendations from a DAK. Overview of the health interventions and WHO, regional or national recommendations included within the DAK."

* ^status = #active
* reference 1..* DublinCore "Reference" "Reference data element using Dublin Core metadata"
* source 0..* uri "Source" "Source URI for the health intervention or recommendation"