Logical: DecisionSupportLogic
Parent: SGLogicalModel
Title: "Decision-Support Logic (DAK)"
Description: "Logical Model for representing Decision-Support Logic from a DAK. Decision-support logic and algorithms to support appropriate service delivery in accordance with WHO clinical, public health and data use guidelines."

* ^status = #active
* ^publisher = "World Health Organization (WHO)"
* id 1..1 id "Decision Support Logic ID" "An identifier for the decision support logic"
* description 0..1 markdown "Description" "Description of the decision support logic in Markdown format"
* source 1..1 uri "Source" "Link to a DMN file containing the decision logic. Source URI could be absolute or relative to the root of the DAK"