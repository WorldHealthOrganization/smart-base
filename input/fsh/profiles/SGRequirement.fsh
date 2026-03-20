// SGRequirements profile is defined as a pre-built StructureDefinition with
// snapshot in input/resources/StructureDefinition-SGRequirements.json because
// the Requirements resource type is from R5 and SUSHI cannot resolve it in
// an R4 IG context. Do not re-enable this FSH definition.
//
// Profile: SGRequirements
// Parent: Requirements
// Description: "Smart Guidelines Requirements"
//
// * status MS
// * name 1..1
// * title 1..1
// * experimental 1..1
// * description 1..1
// * statement.label 1..1
// * extension contains $SatisfiesExt named satisfies 0..
