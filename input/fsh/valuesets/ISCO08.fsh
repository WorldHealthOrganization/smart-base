CodeSystem: ISCO08
Id: ISCO08
Title: "International Standard Classification of Occupations 2008"
Description: "ISCO-08 codes extracted from the ILO official classification structure"
* ^url = "http://smart.who.int/base/CodeSystem/ISCO08"
* ^status = #active
* ^experimental = false
* ^caseSensitive = true
* ^content = #example
* ^property[+].code = #definition
* ^property[=].type = #string
* ^property[=].description = "Definition of the ISCO code"

// Sample ISCO-08 codes - this would need to be populated with the full set from the Excel file
* #1 "Managers" "Managers plan, direct, coordinate and evaluate the overall activities of enterprises, governments and other organizations, or of organizational units within them, and formulate and review their policies, laws, rules and regulations."
* #11 "Chief Executives, Senior Officials and Legislators"
* #111 "Legislators and Senior Officials"
* #1111 "Legislators"
* #1112 "Senior Government Officials"
* #1113 "Traditional Chiefs and Heads of Villages"
* #1114 "Senior Officials of Special-Interest Organizations"
* #112 "Managing Directors and Chief Executives"
* #1120 "Managing Directors and Chief Executives"
* #2 "Professionals" "Professionals increase the existing stock of knowledge; apply scientific or artistic concepts and theories; teach about the foregoing in a systematic manner; or engage in any combination of these activities."
* #21 "Science and Engineering Professionals"
* #22 "Health Professionals"
* #221 "Medical Doctors"
* #2211 "Generalist Medical Practitioners"
* #2212 "Specialist Medical Practitioners"
* #222 "Nursing and Midwifery Professionals"
* #2221 "Nursing Professionals"
* #2222 "Midwifery Professionals"

ValueSet: ISCO08ValueSet
Id: ISCO08ValueSet
Title: "ISCO-08 Value Set"
Description: "Extensible value set of ISCO-08 codes for persona classification"
* ^url = "http://smart.who.int/base/ValueSet/ISCO08ValueSet"
* ^status = #active
* ^experimental = false
* include codes from system ISCO08