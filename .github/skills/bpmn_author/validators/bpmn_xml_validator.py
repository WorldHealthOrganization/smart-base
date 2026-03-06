"""
BPMN XML structural validator.

Validates that a BPMN file is well-formed XML, uses standard BPMN 2.0
namespaces (no Zeebe/Camunda extensions), and follows basic structural rules.
"""

from typing import List
from lxml import etree

from common.ig_errors import Issue, error, warning, info

BPMN_NS = "http://www.omg.org/spec/BPMN/20100524/MODEL"

# Vendor namespaces that must NOT appear in DAK BPMN
_FORBIDDEN_NAMESPACES = {
    "http://camunda.org/schema/zeebe/1.0": "Zeebe",
    "http://camunda.org/schema/1.0/bpmn": "Camunda",
    "http://camunda.org/schema/modeler/1.0": "Camunda Modeler",
}


def validate_bpmn_xml(bpmn_content: str, *, filename: str = "unknown.bpmn") -> List[Issue]:
    """Validate BPMN XML content and return a list of issues.

    Checks:
        1. Well-formed XML
        2. Root element is bpmn:definitions
        3. No forbidden vendor namespaces
        4. At least one process element
        5. No duplicate id attributes
    """
    issues: List[Issue] = []

    # 1. Well-formed XML
    try:
        tree = etree.fromstring(bpmn_content.encode("utf-8"))
    except etree.XMLSyntaxError as exc:
        issues.append(error("BPMN-001", f"Malformed XML: {exc}", file=filename))
        return issues  # Can't continue

    # 2. Root element check
    expected_tag = f"{{{BPMN_NS}}}definitions"
    if tree.tag != expected_tag:
        issues.append(error(
            "BPMN-002",
            f"Root element must be <bpmn:definitions>, got <{tree.tag}>",
            file=filename,
        ))

    # 3. Forbidden vendor namespaces (check all unique namespace URIs in document)
    seen_ns: set = set()
    for elem in tree.iter():
        for uri in (elem.nsmap or {}).values():
            seen_ns.add(uri)
    for uri, vendor in _FORBIDDEN_NAMESPACES.items():
        if uri in seen_ns:
            issues.append(error(
                "BPMN-003",
                f"Forbidden {vendor} namespace detected: {uri}",
                file=filename,
            ))

    # 4. At least one process
    processes = tree.findall(f"{{{BPMN_NS}}}process")
    if not processes:
        issues.append(error(
            "BPMN-004",
            "No <bpmn:process> element found",
            file=filename,
        ))

    # 5. Duplicate IDs
    all_ids: dict = {}
    for elem in tree.iter():
        eid = elem.get("id")
        if eid:
            if eid in all_ids:
                issues.append(error(
                    "BPMN-005",
                    f"Duplicate id '{eid}' (first seen on <{all_ids[eid]}>)",
                    file=filename,
                ))
            else:
                all_ids[eid] = elem.tag

    if not issues:
        issues.append(info("BPMN-000", "BPMN XML structure is valid", file=filename))

    return issues
