ValueSet: DAKActors
Title: "DAK Actors"
Description: "Value set containing actors and personas defined in the Digital Adaptation Kit (DAK) components"
* ^experimental = true
* ^status = #active
* include codes from system DAK where concept is-a #actor
* include codes from system DAK where concept is-a #persona

// Example actor concepts from the DAK CodeSystem
ValueSet: DAKActorsHealthWorker
Id: health-worker
Title: "Health Worker Actor"
Description: "Health worker actor from DAK CodeSystem"
* ^experimental = true
* ^status = #active
* DAK#health-worker "Health Worker"

ValueSet: DAKActorsPatient
Id: patient
Title: "Patient Actor" 
Description: "Patient actor from DAK CodeSystem"
* ^experimental = true
* ^status = #active
* DAK#patient "Patient"

ValueSet: DAKActorsAdministrator
Id: administrator
Title: "Administrator Actor"
Description: "Administrator actor from DAK CodeSystem" 
* ^experimental = true
* ^status = #active
* DAK#administrator "Administrator"