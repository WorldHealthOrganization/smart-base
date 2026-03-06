# BPMN 2.0 XML Schema Reference

Standard BPMN 2.0 XML structure for DAK workflows:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<bpmn:definitions xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL"
                  xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI"
                  xmlns:dc="http://www.omg.org/spec/DD/20100524/DC"
                  xmlns:di="http://www.omg.org/spec/DD/20100524/DI"
                  id="Definitions_1"
                  targetNamespace="http://bpmn.io/schema/bpmn">

  <bpmn:collaboration id="Collaboration_1">
    <bpmn:participant id="Participant_1" name="Process Name" processRef="Process_1" />
  </bpmn:collaboration>

  <bpmn:process id="Process_1" isExecutable="false">
    <bpmn:laneSet id="LaneSet_1">
      <bpmn:lane id="HealthWorker" name="Health Worker">
        <bpmn:flowNodeRef>Task_1</bpmn:flowNodeRef>
      </bpmn:lane>
      <bpmn:lane id="Client" name="Client">
        <bpmn:flowNodeRef>Task_2</bpmn:flowNodeRef>
      </bpmn:lane>
    </bpmn:laneSet>

    <bpmn:startEvent id="StartEvent_1" />
    <bpmn:task id="Task_1" name="Perform assessment" />
    <bpmn:task id="Task_2" name="Receive results" />
    <bpmn:endEvent id="EndEvent_1" />

    <bpmn:sequenceFlow id="Flow_1" sourceRef="StartEvent_1" targetRef="Task_1" />
    <bpmn:sequenceFlow id="Flow_2" sourceRef="Task_1" targetRef="Task_2" />
    <bpmn:sequenceFlow id="Flow_3" sourceRef="Task_2" targetRef="EndEvent_1" />
  </bpmn:process>

</bpmn:definitions>
```

## Key elements

| Element | Purpose |
|---|---|
| `<bpmn:collaboration>` | Top-level container for participants (pools) |
| `<bpmn:participant>` | A pool — references a `<bpmn:process>` |
| `<bpmn:process>` | Contains lanes, tasks, events, gateways, flows |
| `<bpmn:laneSet>` | Container for lanes within a process |
| `<bpmn:lane>` | Swimlane — innermost lanes = DAK personas |
| `<bpmn:task>` | Generic task |
| `<bpmn:userTask>` | Human-performed task |
| `<bpmn:serviceTask>` | System-performed task |
| `<bpmn:exclusiveGateway>` | XOR decision point |
| `<bpmn:parallelGateway>` | AND fork/join |
| `<bpmn:startEvent>` | Process entry point |
| `<bpmn:endEvent>` | Process termination point |
| `<bpmn:sequenceFlow>` | Directed edge between flow nodes |
