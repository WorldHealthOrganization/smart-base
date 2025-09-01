Instance: DAK.DT.IMMZ.D2.DT.BCGQuestionnaire
InstanceOf: SGQuestionnaire
Title: "Questionnaire for IMMZ.D2 Determine required vaccination(s) if any"
Description: "Auto-generated questionnaire for decision table DAK.DT.IMMZ.D2.DT.BCG"
Usage: #definition

* name = "DAK.DT.IMMZ.D2.DT.BCGQuestionnaire"
* title = "IMMZ.D2 Determine required vaccination(s) if any"
* version = "1.0.0"
* status = #draft
* experimental = true
* publisher = "World Health Organization (WHO)"
* description = "This questionnaire supports the decision logic for: IMMZ.D2 Determine required vaccination(s) if any"

// Required extensions for SGQuestionnaire profile
* extension[actor].valueReference = Reference(HealthcareWorkerActor)
* extension[task].valueCoding = $SGTasks#userTask

* item[+]
  * linkId = "input.DAK.DT.IMMZ.D2.DT.BCG.NumberofBCGprimaryseriesdosesadministered"
  * text = "Number of BCG primary series doses administered"
  * type = #choice
  * required = false
  * answerOption[0].valueString = "No BCG primary series dose was administered"
  * answerOption[1].valueString = "One BCG primary series dose was administered"

* item[+]
  * linkId = "input.DAK.DT.IMMZ.D2.DT.BCG.Age"
  * text = "Age"
  * type = #choice
  * required = false
  * answerOption[0].valueString = "Clients age is between 28 days and 5 years"
  * answerOption[1].valueString = "Clients age is less than or equal to 28 days"
  * answerOption[2].valueString = "Clients age is more than 5 years"

* item[+]
  * linkId = "input.DAK.DT.IMMZ.D2.DT.BCG.HIVstatus"
  * text = "HIV status"
  * type = #choice
  * required = false
  * answerOption[0].valueString = "Clients HIV status is negative or unknown"
  * answerOption[1].valueString = "Clients HIV status is positive"

* item[+]
  * linkId = "input.DAK.DT.IMMZ.D2.DT.BCG.CurrentlyonART"
  * text = "Currently on ART"
  * type = #choice
  * required = false
  * answerOption[0].valueString = "Client is currently not receiving antiretroviral therapy"
  * answerOption[1].valueString = "Client is currently receiving antiretroviral therapy"

* item[+]
  * linkId = "input.DAK.DT.IMMZ.D2.DT.BCG.Immunologicallystable"
  * text = "Immunologically stable"
  * type = #choice
  * required = false
  * answerOption[0].valueString = "Client is immunologically stable"
  * answerOption[1].valueString = "Client is not immunologically stable"

* item[+]
  * linkId = "input.DAK.DT.IMMZ.D2.DT.BCG.TBinfectiontestresult"
  * text = "TB infection test result"
  * type = #choice
  * required = false
  * answerOption[0].valueString = "Clients TB infection test result is negative"
  * answerOption[1].valueString = "Clients TB infection test result is positive"
  * answerOption[2].valueString = "Clients TB infection test result is unknown (test not done or no result yet)"

* item[+]
  * linkId = "input.DAK.DT.IMMZ.D2.DT.BCG.Timepassedsincealivevaccinewasadministered"
  * text = "Time passed since a live vaccine was administered"
  * type = #choice
  * required = false
  * answerOption[0].valueString = "Live vaccine was administered in the last four weeks"
  * answerOption[1].valueString = "No live vaccine was administered"
  * answerOption[2].valueString = "No live vaccine was administered in the last four weeks"

* item[+]
  * linkId = "input.DAK.DT.IMMZ.D2.DT.BCG.Clinicallywell"
  * text = "Clinically well"
  * type = #choice
  * required = false
  * answerOption[0].valueString = "Client is clinically well"
  * answerOption[1].valueString = "Client is not clinically well"

