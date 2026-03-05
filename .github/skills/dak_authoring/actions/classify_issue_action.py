"""
Issue classifier — applies content:L1/L2/L3/translation labels.
Uses LLM when DAK_LLM_API_KEY is set; falls back to keyword matching.
Both paths use the same label application logic.
"""

import os
import sys
from pathlib import Path

_SKILLS_ROOT = Path(__file__).resolve().parent.parent.parent
if str(_SKILLS_ROOT) not in sys.path:
    sys.path.insert(0, str(_SKILLS_ROOT))

# ── Keyword lists ──────────────────────────────────────────────────────────

L1_KEYWORDS = [
    # WHO guideline source
    "recommendation", "who recommendation", "guideline", "who guideline",
    "clinical guideline", "evidence", "evidence base", "evidence-based",
    "narrative", "who narrative", "source content", "who document",
    # Sections of WHO guideline documents
    "section 2", "section 3", "section 4", "annex", "appendix",
    "executive summary", "background", "scope", "target population",
    # Clinical content
    "clinical", "intervention", "outcome", "efficacy", "safety",
    "contraindication", "dosage", "dose", "regimen", "protocol",
    "screening", "diagnosis", "treatment", "management", "referral",
    "counselling", "counseling", "antenatal", "postnatal", "maternal",
    "newborn", "child", "adolescent", "immunization", "vaccination",
    # Process
    "new recommendation", "update recommendation", "change guideline",
    "outdated", "superseded", "retracted",
]

L2_KEYWORDS = [
    # BPMN / process
    "bpmn", "business process", "swimlane", "swim lane", "workflow",
    "process diagram", "process model", "process flow", "flow diagram",
    "lane", "pool", "gateway", "sequence flow", "start event", "end event",
    "user task", "service task", "business rule", "send task", "receive task",
    # Personas / actors
    "persona", "actor", "actordefinition", "actor definition",
    "health worker", "healthcare worker", "community health worker", "chw",
    "clinician", "nurse", "midwife", "physician", "doctor", "pharmacist",
    "supervisor", "facility", "patient", "client", "caregiver",
    # FHIR resources / FSH
    "fhir", "fsh", "sushi", "profile", "instance", "extension",
    "codesystem", "code system", "valueset", "value set", "conceptmap",
    "structuredefinition", "logical model", "implementation guide", "ig",
    # DAK components
    "questionnaire", "data element", "data dictionary", "decision table",
    "decision logic", "cql", "clinical quality language", "library",
    "plandefinition", "activitydefinition", "measure",
    "requirement", "non-functional", "functional requirement",
    # DAK L2 editorial
    "dak", "digital adaptation kit", "l2", "component 2", "component 3",
    "component 4", "component 5", "component 6", "component 7", "component 8",
    "business process", "generic persona", "related persona",
    "core data element", "decision support", "scheduling logic",
    "indicator", "performance indicator",
]

L3_KEYWORDS = [
    # Geographic / organizational scope
    "national", "country", "country-specific", "country adaptation",
    "local", "regional", "district", "sub-national",
    "program", "programme", "program-level", "programme-level",
    # Adaptation process
    "adaptation", "adapt", "localize", "localise", "contextualize",
    "contextualise", "customise", "customize", "context-specific",
    "l3", "layer 3", "implementation guide", "conformance",
    # System / interoperability
    "system", "ehr", "emr", "electronic health record",
    "health information system", "his", "dhis2", "openemr", "openmrs",
    "mapping", "terminology mapping", "code mapping",
    "interoperability", "integration", "api", "openapi",
    "capability statement",
]

TRANSLATION_KEYWORDS = [
    # Languages
    "translation", "translate", "translated", "translating",
    "arabic", "\u0639\u0631\u0628\u064a", "ar",
    "chinese", "mandarin", "\u4e2d\u6587", "zh",
    "french", "fran\u00e7ais", "francais", "fr",
    "russian", "\u0440\u0443\u0441\u0441\u043a\u0438\u0439", "ru",
    "spanish", "espa\u00f1ol", "espanol", "es",
    "portuguese", "portugu\u00eas", "pt",
    # Translation tooling
    "weblate", "po file", ".po", "pot file", ".pot", "gettext",
    "msgstr", "msgid", "locale", "localization", "localisation",
    "i18n", "l10n", "internationalization",
    # Translation issues
    "mistranslation", "mistranslated", "wrong translation",
    "translation error", "translation review", "translation update",
    "string", "untranslated", "missing translation",
]


def classify_by_keywords(title: str, body: str) -> list:
    """Keyword-based fallback classifier. Case-insensitive. No LLM needed."""
    text = (title + " " + (body or "")).lower()
    labels = []
    if any(k in text for k in L1_KEYWORDS):
        labels.append("content:L1")
    if any(k in text for k in L2_KEYWORDS):
        labels.append("content:L2")
    if any(k in text for k in L3_KEYWORDS):
        labels.append("content:L3")
    if any(k in text for k in TRANSLATION_KEYWORDS):
        labels.append("content:translation")
    return labels


def apply_labels(issue_number: int, labels: list) -> None:
    """Apply labels to issue via GitHub REST API using GITHUB_TOKEN."""
    import requests

    token = os.environ["GITHUB_TOKEN"]
    repo = os.environ["GITHUB_REPOSITORY"]
    if not labels:
        return
    r = requests.post(
        f"https://api.github.com/repos/{repo}/issues/{issue_number}/labels",
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
        },
        json={"labels": labels},
        timeout=10,
    )
    r.raise_for_status()
    print(f"\u2705 Applied labels: {labels}")


def main():
    from common.prompts import load_prompt
    from common.smart_llm_facade import SmartLLMFacade

    issue_number = int(os.environ["ISSUE_NUMBER"])
    title = os.environ.get("ISSUE_TITLE", "")
    body = os.environ.get("ISSUE_BODY", "")
    api_key = os.environ.get("DAK_LLM_API_KEY", "")

    if api_key:
        # LLM path
        prompt = load_prompt(
            "dak_authoring", "classify_issue",
            issue_title=title, issue_body=body[:4000],
        )
        llm = SmartLLMFacade(
            api_key=api_key,
            model=os.environ.get("DAK_LLM_MODEL", "gpt-4o-mini"),
        )
        result = llm.call(prompt, structured_output=True)
        labels = result.get("labels", [])
        print(f"LLM classification: {result.get('reasoning')}")
    else:
        # Keyword fallback — no LLM cost
        labels = classify_by_keywords(title, body)
        print(f"\u26a0\ufe0f  No LLM key \u2014 keyword fallback used. Labels: {labels}")

    apply_labels(issue_number, labels)


if __name__ == "__main__":
    main()
