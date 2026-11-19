"""Shared safe lxml XMLParser helper (resolve_entities=False, no_network=True, huge_tree=False)."""

from lxml import etree


def safe_xml_parser(*, recover: bool = False) -> etree.XMLParser:
    """Return an lxml XMLParser with entity resolution, network access, and huge trees disabled."""
    return etree.XMLParser(
        resolve_entities=False,
        no_network=True,
        huge_tree=False,
        recover=recover,
    )
