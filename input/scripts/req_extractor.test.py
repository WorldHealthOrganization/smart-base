#!/usr/bin/env python3
"""
Run req_extractor over a small DAK requirements workbook and check that every
element it writes on a FunctionalRequirement or NonFunctionalRequirement
instance is one the logical model declares.

FunctionalRequirement.capability[x] and benefit[x] are `markdown or Coding`,
so an instance sets `capabilityMarkdown`/`benefitMarkdown`. The extractor used
to write `capabilityString`/`benefitString`, which SUSHI rejects, so every DAK
regenerated from its spreadsheet failed to build against smart.who.int.base.
This test reads the element names and their types from the logical models'
FSH, beside this IG, rather than hard-coding them, so a later change to a
model that the extractor does not follow fails here.

Run: python3 input/scripts/req_extractor.test.py
"""

from __future__ import annotations

import logging
import os
import re
import sys
import tempfile

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
MODELS = os.path.join(REPO, "input", "fsh", "models")
sys.path.insert(0, HERE)

from req_extractor import req_extractor  # noqa: E402

# FHIR type code -> the suffix a choice element takes for that type
CHOICE_SUFFIX = {"markdown": "Markdown", "Coding": "Coding", "string": "String",
                 "uri": "Uri", "id": "Id", "code": "Code"}


def model_paths(name: str) -> set:
    """The top-level paths an instance of the logical model may set."""
    paths = set()
    with open(os.path.join(MODELS, name + ".fsh"), encoding="utf-8") as f:
        for line in f:
            m = re.match(r"\* (\w+)(\[x\])? \S+ ([^\"]+?) \"", line)
            if not m:
                continue
            element, choice, types = m.groups()
            if not choice:
                paths.add(element)
                continue
            for t in re.split(r"\s+or\s+", types.strip()):
                paths.add(element + CHOICE_SUFFIX[t.split("(")[0]])
    return paths


class StubInstaller:
    def __init__(self) -> None:
        self.resources: dict = {}
        self.code_systems: dict = {}

    def get_base_aliases(self) -> list:
        return []

    def add_aliases(self, aliases: list) -> None:
        pass

    def add_resource(self, dir: str, id: str, resource: str) -> bool:
        self.resources.setdefault(dir, {})[id] = resource
        return True

    def generate_cs_and_vs_from_dict(self, cs_id: str, title: str, codes: dict) -> bool:
        self.code_systems[cs_id] = dict(codes)
        return True


def write_workbook(path: str) -> None:
    functional = pd.DataFrame([
        ["Classification of digital health interventions 1.1.1, 2.3", None, None, None, None],
        ["Business process A: Registration", None, None, None, None],
        ["IMMZ.FXNREQ.001", "IMMZ.A1.Register client", "health worker",
         'record the client\'s "details"', "the client is registered"],
    ], columns=["Requirement ID", "Activity ID and name", "As a", "I want to", "So that"])
    nonfunctional = pd.DataFrame([
        ["IMMZ.NFXNREQ.001", "Accessibility", "The system must be usable offline"],
    ], columns=["Requirement ID", "Category", "Non-functional requirement"])
    with pd.ExcelWriter(path) as w:
        functional.to_excel(w, sheet_name="Functional", index=False)
        nonfunctional.to_excel(w, sheet_name="Non-functional", index=False)


def instance_paths(fsh: str) -> set:
    return {m.group(1) for m in re.finditer(r"^\* (\w+)", fsh, re.M)}


def main() -> int:
    logging.basicConfig(level=logging.WARNING)
    failures = []

    def check(cond: bool, msg: str) -> None:
        if not cond:
            failures.append(msg)

    with tempfile.TemporaryDirectory() as tmp:
        book = os.path.join(tmp, "requirements.xlsx")
        write_workbook(book)
        inst = StubInstaller()
        ex = req_extractor(inst)
        ex.inputfile_name = book
        check(ex.extract_file() is True, "extract_file did not return True")

    instances = inst.resources.get("instances", {})
    requirements = inst.resources.get("requirements", {})
    fxn = {k: v for k, v in instances.items() if "InstanceOf: FunctionalRequirement" in v}
    nfxn = {k: v for k, v in instances.items() if "InstanceOf: NonFunctionalRequirement" in v}
    check(len(fxn) == 1, f"expected 1 FunctionalRequirement instance, got {len(fxn)}")
    check(len(nfxn) == 1, f"expected 1 NonFunctionalRequirement instance, got {len(nfxn)}")
    check(len(requirements) == 2, f"expected 2 SGRequirements instances, got {len(requirements)}")

    allowed = {"FunctionalRequirement": model_paths("FunctionalRequirement"),
               "NonFunctionalRequirement": model_paths("NonFunctionalRequirement")}
    for model, group in (("FunctionalRequirement", fxn), ("NonFunctionalRequirement", nfxn)):
        for id, fsh in group.items():
            stray = instance_paths(fsh) - allowed[model]
            check(not stray, f"{id} sets {sorted(stray)}, not in {model}: {sorted(allowed[model])}")

    for id, fsh in fxn.items():
        check('* capabilityMarkdown = "record the client\'s \\"details\\""' in fsh,
              f"{id} has no capabilityMarkdown:\n{fsh}")
        check('* benefitMarkdown = "the client is registered"' in fsh,
              f"{id} has no benefitMarkdown:\n{fsh}")
        check("http://smart.who.int/base/CodeSystem/CDHIv1#1.1.1" in fsh,
              f"{id} lacks the DHI classification:\n{fsh}")
        check("* classification[+] = FXREQBusinessProcesses#A" in fsh,
              f"{id} lacks the business-process classification:\n{fsh}")

    # SGRequirements has no classification slice (only task, satisfies,
    # userstory): the codes live on the LM.<reqid> instances' classification
    # (and category for non-functional), so the Requirements instance must
    # not repeat them as an extension.
    for id, fsh in requirements.items():
        check("InstanceOf: SGRequirements" in fsh, f"{id} is not an SGRequirements instance")
        check("extension[classification]" not in fsh,
              f"{id} sets extension[classification], which SGRequirements does not slice:\n{fsh}")
    for id, fsh in nfxn.items():
        check("* category = FXREQCategories#Accessibility" in fsh,
              f"{id} lacks its category:\n{fsh}")

    check("FXREQBusinessProcesses" in inst.code_systems, "no business-process code system")
    check("FXREQCategories" in inst.code_systems, "no non-functional category code system")

    for f in failures:
        print("FAIL:", f)
    print(f"{'FAILED' if failures else 'OK'}: req_extractor ({len(failures)} failure(s))")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
