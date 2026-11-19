Extension: SGUserStory
Description: "Smart Guidelines extension to support structured User Stories (As a `Actor` I want to `capability` so that `benefit`) extension"
// capability and benefit are inline sub-extensions, so their urls are
// "capability" and "benefit" and a validator can tell the two slices apart.
// They used to both be SGString, which gave both slices the same url: every
// user story with both values then matched more than one slice.
* extension contains capability 1..1 and benefit 1..1
* extension[capability] ^short = "I want to (capability)"
* extension[capability].value[x] only string
* extension[capability].valueString 1..1 MS
* extension[benefit] ^short = "So that (benefit)"
* extension[benefit].value[x] only string
* extension[benefit].valueString 1..1 MS


// No longer used by SGUserStory. SGString is published in
// smart.who.int.base 0.2.0 and 1.0.0, so it stays, retired, for anything that
// names it.
Extension: SGString
Description: "Smart Guidelines (required) string extension for use in a complex extension. Retired: SGUserStory now uses inline `capability` and `benefit` sub-extensions, because two slices of one extension definition cannot be told apart."
* ^status = #retired
* value[x] only string
* valueString 1..1 MS
