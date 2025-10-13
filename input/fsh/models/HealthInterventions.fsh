Logical: HealthInterventions
Parent: SGLogicalModel
Title: "Health Interventions and Recommendations (DAK)"
Description: "Logical Model for representing Health Interventions and Recommendations from a DAK. Overview of the health interventions and WHO, regional or national recommendations included within the DAK."

* ^status = #active
* ^publisher = "World Health Organization (WHO)"
* id 1..1 id "Health Intervention ID" "An identifier for the health intervention"
* description 0..1 markdown "Description" "Description of the health intervention in Markdown format"
* reference 1..* DublinCore "Reference" "Reference data element using Dublin Core metadata"