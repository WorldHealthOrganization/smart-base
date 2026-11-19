# Actor Context

When working with BPMN lanes and DAK personas, the following mapping applies:

## Lane ID → ActorDefinition Mapping

```
BPMN:  <lane id="X" name="Some Name">
FSH:   Instance: X
       InstanceOf: $SGActor
       Title: "Some Name"
```

- The lane `@id` is the bare FSH instance identifier — **no `DAK.` prefix** on the lane itself.
- `bpmn2fhirfsh.xsl` generates the file as `ActorDefinition-DAK.{@id}.fsh`
  and sets `* id = "DAK.{@id}"` inside the FSH.
- The lane `@id` in BPMN = the bare instance name.

## Existing Actors

{actor_list}

## Valid Lane ID Characters

Lane IDs must match `[A-Za-z0-9\-\.]` to be valid FSH instance identifiers.
