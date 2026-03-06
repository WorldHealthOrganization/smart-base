# DAK BPMN Constraints

When authoring or editing BPMN for a WHO Digital Adaptation Kit (DAK):

1. **Standard BPMN 2.0 only** — no Zeebe, Camunda, or other vendor extensions.
   The root element must be `<bpmn:definitions xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL">`.

2. **Swimlane rules:**
   - Every process must have at least one `<laneSet>` with at least one `<lane>`.
   - Innermost lanes (lanes with no `<childLaneSet>`) represent DAK **personas** and map to FHIR `ActorDefinition` instances.
   - `<lane id="X">` — the `id` attribute is the **bare FSH instance identifier**. It must match `[A-Za-z0-9\-\.]`.
   - `<lane name="Y">` — the `name` attribute becomes the human-readable `Title:` in the generated FSH.
   - Every `<task>`, `<userTask>`, `<serviceTask>`, etc., must be referenced by exactly one lane via `<flowNodeRef>`.

3. **No orphan tasks** — every flow node inside a process must appear in a lane's `<flowNodeRef>` list.

4. **No duplicate IDs** — all `id` attributes across the BPMN document must be unique.

5. **File location:** BPMN files are stored in `input/business-processes/*.bpmn`.
