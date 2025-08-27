Profile: SGid
Parent: id
Title: "SMART Guidelines ID"
Description: "A SMART Guidelines ID (sgid) is an FHIR primitive id data type which can only use up to 64 letters, numbers, hyphens and periods. Ids must be combination of letters, numbers, hyphens, and periods. Must be at least 1 character long but does not exceed 64 characters in length."
* ^status = #active
* . ^short = "SMART Guidelines identifier"
* . ^definition = "A SMART Guidelines ID (sgid) that can only contain letters, numbers, hyphens and periods, with length 1-64 characters"
* . ^constraint[+].key = "sgid-1"
* . ^constraint[=].severity = #error
* . ^constraint[=].human = "SGid must only contain letters, numbers, hyphens and periods and be 1-64 characters long"
* . ^constraint[=].expression = "matches('[A-Za-z0-9\\-\\.]{1,64}')"