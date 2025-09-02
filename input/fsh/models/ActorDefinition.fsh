Logical: ActorDefinition
Title: "Actor Definition"
Description: "Base logical model for Actor Definition"
* name 1..1 string "Name" "The name of the actor"
* title 0..1 string "Title" "The title of the actor"  
* status 0..1 code "Status" "The status of the actor"
* experimental 0..1 boolean "Experimental" "Whether this is experimental"
* description 0..1 markdown "Description" "Description of the actor"
* type 0..1 code "Type" "Type of actor"