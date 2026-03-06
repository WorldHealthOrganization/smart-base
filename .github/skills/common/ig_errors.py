"""
IG Publisher error-level constants and formatting helpers.

All DAK skill validators report findings using these severity levels,
matching the IG Publisher output format.

Usage:
    from common.ig_errors import error, warning, info, fatal, format_issuess

    issues = []
    issues.append(error("BPMN-001", "Zeebe namespace detected", file="test.bpmn"))
    issues.append(warning("SWIM-002", "Lane has no tasks"))
    print(format_issues(issues))
"""

from dataclasses import dataclass, field
from typing import List, Optional


# Severity constants (match IG Publisher levels)
FATAL = "FATAL"
ERROR = "ERROR"
WARNING = "WARNING"
INFORMATION = "INFORMATION"


@dataclass
class Issue:
    """A single validation finding."""

    severity: str
    code: str
    message: str
    file: Optional[str] = None
    line: Optional[int] = None

    def __str__(self) -> str:
        location = ""
        if self.file:
            location = f" ({self.file}"
            if self.line:
                location += f":{self.line}"
            location += ")"
        return f"[{self.severity}] {self.code}: {self.message}{location}"


def fatal(code: str, message: str, **kwargs) -> Issue:
    """Create a FATAL issue."""
    return Issue(severity=FATAL, code=code, message=message, **kwargs)


def error(code: str, message: str, **kwargs) -> Issue:
    """Create an ERROR issue."""
    return Issue(severity=ERROR, code=code, message=message, **kwargs)


def warning(code: str, message: str, **kwargs) -> Issue:
    """Create a WARNING issue."""
    return Issue(severity=WARNING, code=code, message=message, **kwargs)


def info(code: str, message: str, **kwargs) -> Issue:
    """Create an INFORMATION issue."""
    return Issue(severity=INFORMATION, code=code, message=message, **kwargs)


def format_issues(issues: List[Issue]) -> str:
    """Format a list of issues as a multi-line string."""
    if not issues:
        return "✅ No issues found."
    return "\n".join(str(i) for i in issues)


def has_errors(issues: List[Issue]) -> bool:
    """Return True if any issue is FATAL or ERROR."""
    return any(i.severity in (FATAL, ERROR) for i in issues)
