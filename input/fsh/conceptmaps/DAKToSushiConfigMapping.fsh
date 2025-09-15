// FHIR StructureMap from DAK Logical Model to SushiConfig Logical Model
// This map defines how DAK metadata fields map to SUSHI configuration fields

Instance: DAKToSushiConfigMapping
InstanceOf: StructureMap
Title: "DAK to SUSHI Config Mapping"
Description: "Mapping from DAK logical model metadata to SUSHI configuration logical model for IG generation"
Usage: #definition

* id = "dak-to-sushi-config-mapping"
* url = "http://smart.who.int/base/StructureMap/DAKToSushiConfigMapping"
* version = "0.2.0"
* name = "DAKToSushiConfigMapping"
* title = "DAK to SUSHI Config Mapping"
* status = #draft
* experimental = false
* publisher = "WHO"
* contact.name = "WHO"
* contact.telecom.system = #url
* contact.telecom.value = "http://who.int"
* jurisdiction = urn:iso:std:iso:3166#001 "World"
* description = "Mapping from DAK logical model metadata to SUSHI configuration logical model for IG generation"

// Structure definitions for source and target
* structure[0].url = "http://smart.who.int/base/StructureDefinition/DAK"
* structure[0].mode = #source
* structure[0].alias = "DAK"

* structure[1].url = "http://smart.who.int/base/StructureDefinition/SushiConfigLogicalModel"
* structure[1].mode = #target
* structure[1].alias = "SushiConfigLogicalModel"

// Main mapping group
* group[0].name = "DAKToSushiConfig"
* group[0].input[0].name = "dak"
* group[0].input[0].type = "DAK"
* group[0].input[0].mode = #source
* group[0].input[1].name = "sushiConfig"
* group[0].input[1].type = "SushiConfigLogicalModel"
* group[0].input[1].mode = #target

// Core identity mappings (direct field mappings)
* group[0].rule[0].name = "mapDakIdToSushiId"
* group[0].rule[0].source[0].context = "dak"
* group[0].rule[0].source[0].element = "id"
* group[0].rule[0].target[0].context = "sushiConfig"
* group[0].rule[0].target[0].element = "id"
* group[0].rule[0].target[0].transform = #copy
* group[0].rule[0].documentation = "Map DAK ID to SUSHI config id"

* group[0].rule[1].name = "mapDakPublicationUrlToSushiCanonical"
* group[0].rule[1].source[0].context = "dak"
* group[0].rule[1].source[0].element = "publicationUrl"
* group[0].rule[1].target[0].context = "sushiConfig"
* group[0].rule[1].target[0].element = "canonical"
* group[0].rule[1].target[0].transform = #copy
* group[0].rule[1].documentation = "Map DAK publicationUrl to SUSHI canonical"

* group[0].rule[2].name = "mapDakNameToSushiName"
* group[0].rule[2].source[0].context = "dak"
* group[0].rule[2].source[0].element = "name"
* group[0].rule[2].target[0].context = "sushiConfig"
* group[0].rule[2].target[0].element = "name"
* group[0].rule[2].target[0].transform = #copy
* group[0].rule[2].documentation = "Map DAK name to SUSHI name"

* group[0].rule[3].name = "mapDakTitleToSushiTitle"
* group[0].rule[3].source[0].context = "dak"
* group[0].rule[3].source[0].element = "title"
* group[0].rule[3].target[0].context = "sushiConfig"
* group[0].rule[3].target[0].element = "title"
* group[0].rule[3].target[0].transform = #copy
* group[0].rule[3].documentation = "Map DAK title to SUSHI title"

* group[0].rule[4].name = "mapDakDescriptionToSushiDescription"
* group[0].rule[4].source[0].context = "dak"
* group[0].rule[4].source[0].element = "description"
* group[0].rule[4].target[0].context = "sushiConfig"
* group[0].rule[4].target[0].element = "description"
* group[0].rule[4].target[0].transform = #copy
* group[0].rule[4].documentation = "Map DAK description to SUSHI description"

* group[0].rule[5].name = "mapDakVersionToSushiVersion"
* group[0].rule[5].source[0].context = "dak"
* group[0].rule[5].source[0].element = "version"
* group[0].rule[5].target[0].context = "sushiConfig"
* group[0].rule[5].target[0].element = "version"
* group[0].rule[5].target[0].transform = #copy
* group[0].rule[5].documentation = "Map DAK version to SUSHI version"

* group[0].rule[6].name = "mapDakStatusToSushiStatus"
* group[0].rule[6].source[0].context = "dak"
* group[0].rule[6].source[0].element = "status"
* group[0].rule[6].target[0].context = "sushiConfig"
* group[0].rule[6].target[0].element = "status"
* group[0].rule[6].target[0].transform = #copy
* group[0].rule[6].documentation = "Map DAK status to SUSHI status"

* group[0].rule[7].name = "mapDakLicenseToSushiLicense"
* group[0].rule[7].source[0].context = "dak"
* group[0].rule[7].source[0].element = "license"
* group[0].rule[7].target[0].context = "sushiConfig"
* group[0].rule[7].target[0].element = "license"
* group[0].rule[7].target[0].transform = #copy
* group[0].rule[7].documentation = "Map DAK license to SUSHI license"

* group[0].rule[8].name = "mapDakCopyrightYearToSushiCopyrightYear"
* group[0].rule[8].source[0].context = "dak"
* group[0].rule[8].source[0].element = "copyrightYear"
* group[0].rule[8].target[0].context = "sushiConfig"
* group[0].rule[8].target[0].element = "copyrightYear"
* group[0].rule[8].target[0].transform = #copy
* group[0].rule[8].documentation = "Map DAK copyright year to SUSHI copyright year"

* group[0].rule[9].name = "mapDakExperimentalToSushiExperimental"
* group[0].rule[9].source[0].context = "dak"
* group[0].rule[9].source[0].element = "experimental"
* group[0].rule[9].target[0].context = "sushiConfig"
* group[0].rule[9].target[0].element = "experimental"
* group[0].rule[9].target[0].transform = #copy
* group[0].rule[9].documentation = "Map DAK experimental flag to SUSHI experimental"

* group[0].rule[10].name = "mapDakFhirVersionToSushiFhirVersion"
* group[0].rule[10].source[0].context = "dak"
* group[0].rule[10].source[0].element = "fhirVersion"
* group[0].rule[10].target[0].context = "sushiConfig"
* group[0].rule[10].target[0].element = "fhirVersion"
* group[0].rule[10].target[0].transform = #copy
* group[0].rule[10].documentation = "Map DAK FHIR version to SUSHI FHIR version"

* group[0].rule[11].name = "mapDakReleaseLabelToSushiReleaseLabel"
* group[0].rule[11].source[0].context = "dak"
* group[0].rule[11].source[0].element = "releaseLabel"
* group[0].rule[11].target[0].context = "sushiConfig"
* group[0].rule[11].target[0].element = "releaseLabel"
* group[0].rule[11].target[0].transform = #copy
* group[0].rule[11].documentation = "Map DAK release label to SUSHI release label"

// Publisher mapping (complex object)
* group[0].rule[12].name = "mapDakPublisherToSushiPublisher"
* group[0].rule[12].source[0].context = "dak"
* group[0].rule[12].source[0].element = "publisher"
* group[0].rule[12].source[0].variable = "dakPublisher"
* group[0].rule[12].target[0].context = "sushiConfig"
* group[0].rule[12].target[0].element = "publisher"
* group[0].rule[12].target[0].variable = "sushiPublisher"
* group[0].rule[12].target[0].transform = #create
* group[0].rule[12].target[0].parameter[0].valueString = "BackboneElement"
* group[0].rule[12].documentation = "Map DAK publisher to SUSHI publisher"

// Publisher name mapping
* group[0].rule[12].rule[0].name = "mapPublisherName"
* group[0].rule[12].rule[0].source[0].context = "dakPublisher"
* group[0].rule[12].rule[0].source[0].element = "name"
* group[0].rule[12].rule[0].target[0].context = "sushiPublisher"
* group[0].rule[12].rule[0].target[0].element = "name"
* group[0].rule[12].rule[0].target[0].transform = #copy
* group[0].rule[12].rule[0].documentation = "Map publisher name"

// Publisher URL mapping
* group[0].rule[12].rule[1].name = "mapPublisherUrl"
* group[0].rule[12].rule[1].source[0].context = "dakPublisher"
* group[0].rule[12].rule[1].source[0].element = "url"
* group[0].rule[12].rule[1].target[0].context = "sushiPublisher"
* group[0].rule[12].rule[1].target[0].element = "url"
* group[0].rule[12].rule[1].target[0].transform = #copy
* group[0].rule[12].rule[1].documentation = "Map publisher URL"

// Contact mapping
* group[0].rule[13].name = "mapDakContactToSushiContact"
* group[0].rule[13].source[0].context = "dak"
* group[0].rule[13].source[0].element = "contact"
* group[0].rule[13].target[0].context = "sushiConfig"
* group[0].rule[13].target[0].element = "contact"
* group[0].rule[13].target[0].transform = #copy
* group[0].rule[13].documentation = "Map DAK contact to SUSHI contact"

// Use context mapping
* group[0].rule[14].name = "mapDakUseContextToSushiUseContext"
* group[0].rule[14].source[0].context = "dak"
* group[0].rule[14].source[0].element = "useContext"
* group[0].rule[14].target[0].context = "sushiConfig"
* group[0].rule[14].target[0].element = "useContext"
* group[0].rule[14].target[0].transform = #copy
* group[0].rule[14].documentation = "Map DAK use context to SUSHI use context"

// Jurisdiction mapping
* group[0].rule[15].name = "mapDakJurisdictionToSushiJurisdiction"
* group[0].rule[15].source[0].context = "dak"
* group[0].rule[15].source[0].element = "jurisdiction"
* group[0].rule[15].target[0].context = "sushiConfig"
* group[0].rule[15].target[0].element = "jurisdiction"
* group[0].rule[15].target[0].transform = #copy
* group[0].rule[15].documentation = "Map DAK jurisdiction to SUSHI jurisdiction"

// Dependencies mapping (array transformation)
* group[0].rule[16].name = "mapDakDependenciesToSushiDependencies"
* group[0].rule[16].source[0].context = "dak"
* group[0].rule[16].source[0].element = "dependencies"
* group[0].rule[16].source[0].variable = "dakDep"
* group[0].rule[16].target[0].context = "sushiConfig"
* group[0].rule[16].target[0].element = "dependencies"
* group[0].rule[16].target[0].variable = "sushiDep"
* group[0].rule[16].target[0].transform = #create
* group[0].rule[16].target[0].parameter[0].valueString = "BackboneElement"
* group[0].rule[16].documentation = "Map DAK dependencies to SUSHI dependencies"

// Dependency fields mapping
* group[0].rule[16].rule[0].name = "mapDependencyId"
* group[0].rule[16].rule[0].source[0].context = "dakDep"
* group[0].rule[16].rule[0].source[0].element = "id"
* group[0].rule[16].rule[0].target[0].context = "sushiDep"
* group[0].rule[16].rule[0].target[0].element = "id"
* group[0].rule[16].rule[0].target[0].transform = #copy
* group[0].rule[16].rule[0].documentation = "Map dependency ID"

* group[0].rule[16].rule[1].name = "mapDependencyVersion"
* group[0].rule[16].rule[1].source[0].context = "dakDep"
* group[0].rule[16].rule[1].source[0].element = "version"
* group[0].rule[16].rule[1].target[0].context = "sushiDep"
* group[0].rule[16].rule[1].target[0].element = "version"
* group[0].rule[16].rule[1].target[0].transform = #copy
* group[0].rule[16].rule[1].documentation = "Map dependency version"

* group[0].rule[16].rule[2].name = "mapDependencyReason"
* group[0].rule[16].rule[2].source[0].context = "dakDep"
* group[0].rule[16].rule[2].source[0].element = "reason"
* group[0].rule[16].rule[2].target[0].context = "sushiDep"
* group[0].rule[16].rule[2].target[0].element = "reason"
* group[0].rule[16].rule[2].target[0].transform = #copy
* group[0].rule[16].rule[2].documentation = "Map dependency reason"

// Pages mapping (array transformation)
* group[0].rule[17].name = "mapDakPagesToSushiPages"
* group[0].rule[17].source[0].context = "dak"
* group[0].rule[17].source[0].element = "pages"
* group[0].rule[17].source[0].variable = "dakPage"
* group[0].rule[17].target[0].context = "sushiConfig"
* group[0].rule[17].target[0].element = "pages"
* group[0].rule[17].target[0].variable = "sushiPage"
* group[0].rule[17].target[0].transform = #create
* group[0].rule[17].target[0].parameter[0].valueString = "BackboneElement"
* group[0].rule[17].documentation = "Map DAK pages to SUSHI pages"

// Page fields mapping
* group[0].rule[17].rule[0].name = "mapPageFilename"
* group[0].rule[17].rule[0].source[0].context = "dakPage"
* group[0].rule[17].rule[0].source[0].element = "filename"
* group[0].rule[17].rule[0].target[0].context = "sushiPage"
* group[0].rule[17].rule[0].target[0].element = "filename"
* group[0].rule[17].rule[0].target[0].transform = #copy
* group[0].rule[17].rule[0].documentation = "Map page filename"

* group[0].rule[17].rule[1].name = "mapPageTitle"
* group[0].rule[17].rule[1].source[0].context = "dakPage"
* group[0].rule[17].rule[1].source[0].element = "title"
* group[0].rule[17].rule[1].target[0].context = "sushiPage"
* group[0].rule[17].rule[1].target[0].element = "title"
* group[0].rule[17].rule[1].target[0].transform = #copy
* group[0].rule[17].rule[1].documentation = "Map page title"