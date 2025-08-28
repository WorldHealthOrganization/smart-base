Logical: BusinessProcessWorkflow
Title: "Business Process Workflow (DAK)"
Description: "Logical Model for representing Generic Business Processes and Workflows from a DAK. A business process is a set of related activities or tasks performed together to achieve the objectives of the health programme area."

* ^status = #active
* source 1..1 uri "Source" "Link to a BPMN file containing the workflow definition"
* scenario 0..* id "Scenario" "References to user scenario IDs related to this workflow"
* objectives 1..1 markdown "Objectives" "Description of the objectives of the workflow"
* task 0..* BackboneElement "Task" "Tasks within the business process workflow"
  * id 1..1 id "Task ID" "Identifier for the task"
  * name 1..1 string "Task Name" "Name of the task"
  * description 1..1 string "Task Description" "Description of what the task involves"