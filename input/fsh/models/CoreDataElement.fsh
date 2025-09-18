Logical: CoreDataElement
Title: "Core Data Element (DAK)"
Description: "Logical Model for representing Core Data Elements from a DAK. Data elements are required throughout the different points of a workflow and are mapped to established concept mapping standards."

* ^status = #active
* code 1..1 code "Code" "Code that identifies the concept"
* display 1..1 string "Display" "Text displayed to the user"
* definition 1..1 string "Definition" "Formal definition of the data element"
* description[x] 0..1 string or uri "Description" "Description of the core data element - either Markdown content or a URI to a Markdown file (absolute or relative to repository root)"