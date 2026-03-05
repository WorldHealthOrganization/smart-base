"""
BPMN swimlane validator.

Validates DAK swimlane constraints:
- Lanes must be present in every process
- No orphan tasks (every flow node referenced by a lane)
- No duplicate lane IDs
- Lane IDs are valid FSH identifiers
"""

import re
from typing import List
from lxml import etree

from common.ig_errors import Issue, error, warning, info

BPMN_NS = "http://www.omg.org/spec/BPMN/20100524/MODEL"

# Valid FSH identifier pattern
_FSH_ID_RE = re.compile(r"^[A-Za-z0-9.\-]+$")

# Flow node types that should be assigned to a lane
_FLOW_NODE_TAGS = {
    f"{{{BPMN_NS}}}{tag}"
    for tag in (
        "task", "userTask", "serviceTask", "sendTask", "receiveTask",
        "manualTask", "businessRuleTask", "scriptTask", "callActivity",
        "subProcess", "startEvent", "endEvent", "intermediateThrowEvent",
        "intermediateCatchEvent", "boundaryEvent",
        "exclusiveGateway", "parallelGateway", "inclusiveGateway",
        "eventBasedGateway", "complexGateway",
    )
}


def validate_swimlanes(bpmn_content: str, *, filename: str = "unknown.bpmn") -> List[Issue]:
    """Validate BPMN swimlane structure and return a list of issues.

    Checks:
        1. Every process has a laneSet
        2. Lane IDs are valid FSH identifiers
        3. No orphan flow nodes (every node referenced by a lane)
        4. No duplicate lane IDs across the document
    """
    issues: List[Issue] = []

    try:
        tree = etree.fromstring(bpmn_content.encode("utf-8"))
    except etree.XMLSyntaxError:
        issues.append(error("SWIM-001", "Cannot parse XML", file=filename))
        return issues

    # Collect all lane IDs for duplicate check
    seen_lane_ids: dict = {}

    processes = tree.findall(f"{{{BPMN_NS}}}process")
    for proc in processes:
        proc_id = proc.get("id", "?")

        # 1. laneSet present?
        lane_sets = proc.findall(f"{{{BPMN_NS}}}laneSet")
        if not lane_sets:
            issues.append(error(
                "SWIM-002",
                f"Process '{proc_id}' has no <laneSet>",
                file=filename,
            ))
            continue

        # Collect all flowNodeRefs from lanes
        all_refs: set = set()
        for lane_set in lane_sets:
            for lane in lane_set.iter(f"{{{BPMN_NS}}}lane"):
                lane_id = lane.get("id", "")

                # 2. Valid FSH ID?
                if lane_id and not _FSH_ID_RE.match(lane_id):
                    issues.append(warning(
                        "SWIM-003",
                        f"Lane id '{lane_id}' contains characters invalid for FSH identifiers "
                        f"(allowed: A-Z, a-z, 0-9, '-', '.')",
                        file=filename,
                    ))

                # Duplicate lane ID?
                if lane_id:
                    if lane_id in seen_lane_ids:
                        issues.append(error(
                            "SWIM-004",
                            f"Duplicate lane id '{lane_id}'",
                            file=filename,
                        ))
                    else:
                        seen_lane_ids[lane_id] = True

                for ref in lane.findall(f"{{{BPMN_NS}}}flowNodeRef"):
                    if ref.text:
                        all_refs.add(ref.text.strip())

        # 3. Orphan flow nodes?
        for child in proc:
            if child.tag in _FLOW_NODE_TAGS:
                node_id = child.get("id", "")
                if node_id and node_id not in all_refs:
                    issues.append(warning(
                        "SWIM-005",
                        f"Flow node '{node_id}' ({child.tag.split('}')[-1]}) "
                        f"is not referenced by any lane in process '{proc_id}'",
                        file=filename,
                    ))

    if not issues:
        issues.append(info("SWIM-000", "Swimlane structure is valid", file=filename))

    return issues
