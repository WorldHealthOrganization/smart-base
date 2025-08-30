<?xml version="1.0" encoding="UTF-8"?>
<sch:schema xmlns:sch="http://purl.oclc.org/dsdl/schematron" queryBinding="xslt2">
  <sch:ns prefix="f" uri="http://hl7.org/fhir"/>
  <sch:ns prefix="h" uri="http://www.w3.org/1999/xhtml"/>
  <!-- 
    This file contains just the constraints for the profile SGGraphDefinition
    It includes the base constraints for the resource as well.
    Because of the way that schematrons and containment work, 
    you may need to use this schematron fragment to build a, 
    single schematron that validates contained resources (if you have any) 
  -->
  <sch:pattern>
    <sch:title>f:GraphDefinition</sch:title>
    <sch:rule context="f:GraphDefinition">
      <sch:assert test="count(f:node) &lt;= 2">node: maximum cardinality of 'node' is 2</sch:assert>
      <sch:assert test="count(f:link) &lt;= 1">link: maximum cardinality of 'link' is 1</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern>
    <sch:title>f:GraphDefinition/f:link</sch:title>
    <sch:rule context="f:GraphDefinition/f:link">
      <sch:assert test="count(f:extension[@url = 'http://smart.who.int/base/StructureDefinition/Sgcode']) &gt;= 1">extension with URL = 'http://smart.who.int/base/StructureDefinition/Sgcode': minimum cardinality of 'extension' is 1</sch:assert>
      <sch:assert test="count(f:extension[@url = 'http://smart.who.int/base/StructureDefinition/Sgcode']) &lt;= 1">extension with URL = 'http://smart.who.int/base/StructureDefinition/Sgcode': maximum cardinality of 'extension' is 1</sch:assert>
      <sch:assert test="count(f:extension[@url = 'http://smart.who.int/base/StructureDefinition/Markdown']) &gt;= 1">extension with URL = 'http://smart.who.int/base/StructureDefinition/Markdown': minimum cardinality of 'extension' is 1</sch:assert>
      <sch:assert test="count(f:extension[@url = 'http://smart.who.int/base/StructureDefinition/Markdown']) &lt;= 1">extension with URL = 'http://smart.who.int/base/StructureDefinition/Markdown': maximum cardinality of 'extension' is 1</sch:assert>
      <sch:assert test="count(f:extension[@url = 'http://smart.who.int/base/StructureDefinition/Markdown']) &gt;= 1">extension with URL = 'http://smart.who.int/base/StructureDefinition/Markdown': minimum cardinality of 'extension' is 1</sch:assert>
      <sch:assert test="count(f:extension[@url = 'http://smart.who.int/base/StructureDefinition/Markdown']) &lt;= 1">extension with URL = 'http://smart.who.int/base/StructureDefinition/Markdown': maximum cardinality of 'extension' is 1</sch:assert>
      <sch:assert test="count(f:extension[@url = 'http://smart.who.int/base/StructureDefinition/Markdown']) &gt;= 1">extension with URL = 'http://smart.who.int/base/StructureDefinition/Markdown': minimum cardinality of 'extension' is 1</sch:assert>
      <sch:assert test="count(f:extension[@url = 'http://smart.who.int/base/StructureDefinition/Markdown']) &lt;= 1">extension with URL = 'http://smart.who.int/base/StructureDefinition/Markdown': maximum cardinality of 'extension' is 1</sch:assert>
    </sch:rule>
  </sch:pattern>
</sch:schema>
