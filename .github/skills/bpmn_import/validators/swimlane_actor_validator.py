"""
Swimlane → ActorDefinition validator.

Checks that every innermost ``<lane id="X">`` in BPMN files has a
corresponding ``input/fsh/actors/ActorDefinition-DAK.X.fsh`` file.
"""

import os
from typing import List
from lxml import etree

from common.ig_errors import Issue, error, warning, info
from common.fsh_utils import instance_exists

BPMN_NS = "http://www.omg.org/spec/BPMN/20100524/MODEL"


def _is_innermost_lane(lane: etree._Element) -> bool:
    """Return True if the lane has no nested childLaneSet."""
    return lane.find(f"{{{BPMN_NS}}}childLaneSet") is None


def validate_swimlane_actors(
    bpmn_content: str,
    *,
    ig_root: str = ".",
    filename: str = "unknown.bpmn",
) -> List[Issue]:
    """Validate that every innermost lane has a matching ActorDefinition FSH file.

    Args:
        bpmn_content: BPMN XML as a string.
        ig_root: Path to the IG root directory.
        filename: Source filename for issue reporting.

    Returns:
        List of validation issues.
    """
    issues: List[Issue] = []

    try:
        tree = etree.fromstring(bpmn_content.encode("utf-8"))
    except etree.XMLSyntaxError as exc:
        issues.append(error("ACTOR-001", f"Cannot parse BPMN XML: {exc}", file=filename))
        return issues

    for lane in tree.iter(f"{{{BPMN_NS}}}lane"):
        if not _is_innermost_lane(lane):
            continue

        lane_id = lane.get("id", "")
        lane_name = lane.get("name", lane_id)

        if not lane_id:
            issues.append(warning(
                "ACTOR-002",
                f"Lane without id attribute (name='{lane_name}')",
                file=filename,
            ))
            continue

        if not instance_exists(ig_root, lane_id):
            issues.append(error(
                "ACTOR-003",
                f"No ActorDefinition FSH file for lane '{lane_id}' "
                f"(expected: input/fsh/actors/ActorDefinition-DAK.{lane_id}.fsh)",
                file=filename,
            ))

    if not issues:
        issues.append(info("ACTOR-000", "All lanes map to ActorDefinition files", file=filename))

    return issues
