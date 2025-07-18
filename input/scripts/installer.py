import lxml.etree as ET
from typing import Union
import glob
import re
import os
import shutil
import yaml
from typing import List
from pathlib import Path
import pprint
import sys
from lxml import etree
import hashlib

class installer:
  resources = { 'requirements' : {} ,'codesystems' : {} , 'valuesets' : {} , 'rulesets' : {},
                'actors' : {} , 'instances': {}, 'rulesets' : {}, 'libraries' : {},
                'plandefinitions':{}, 'activitydefinitions':{}}  
  cqls = {}
  codesystems = {}
  codesystem_titles = {}
  codesystem_properties = {}
  pages = {}
  logfile = None
  sushi_config = {}
  multifile_xsd = "includes/multifile.xsd" #relative to the dir containing this file
  sushi_file = "sushi-config.yaml"
  multifile_schema = None  

  xslts = {}
  
  
  def __init__(self):
    logfile_path = Path("temp/DAKExtract.log.txt")
    print("Logging status messages to stderr and: " + str(logfile_path))
    logfile_path.parent.mkdir(exist_ok=True, parents=True)
    self.logfile = open(logfile_path,"w")
    Path("input/dmn").mkdir(exist_ok=True, parents=True)
    Path("input/bpmn").mkdir(exist_ok=True, parents=True)
    Path("input/cql").mkdir(exist_ok=True, parents=True)
    Path("input/fsh").mkdir(exist_ok=True, parents=True)
    Path("input/fsh/actordefinitions").mkdir(exist_ok=True, parents=True)
    Path("input/fsh/activitydefinitions").mkdir(exist_ok=True, parents=True)
    Path("input/fsh/plandefinitions").mkdir(exist_ok=True, parents=True)
    Path("input/pagecontent").mkdir(exist_ok=True, parents=True)
    if not self.load_multifile_schema():
      raise Exception('Could not load multifile xsd')
    if not self.read_sushi_config():
      raise Exception('Could not load sushi-config')
    #self.add_rulesets()

  def load_multifile_schema(self):
    """
        Loads and parses the multifile XML XSD, storing it as self.multifile_schema.
        """
    script_directory = self.get_base_dir() + "/input/scripts" 
    xsd_path = Path(script_directory + "/"  + self.multifile_xsd)
    try:
      with open(xsd_path, "rb") as xsd_file:
        schema_doc = ET.parse(xsd_file)
        self.multifile_schema = ET.XMLSchema(schema_doc)
        self.log(f"Loaded multifile.xsd schema from {xsd_path}")
    except Exception as e:
      self.log(f"FATAL: Could not load multifile.xsd from {xsd_path}: {e}")
      self.multifile_schema = None
      return False
    return True
 
  def get_base_dir(self):
    return os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


  def register_transformer(self,key:str,xsl_file: Union[str,Path],namespaces:dict = {}):
    try:
      script_directory = self.get_base_dir() + "/input/scripts" 
      xsl_file = script_directory + "/" +  xsl_file
      self.log("initializing xslt at " + xsl_file)
      for prefix,namespace in namespaces.items():
        ET.register_namespace(prefix , namespace)
      with open(Path(xsl_file), "rb") as f:
        self.xslts[key] = ET.XSLT(ET.parse(f))

    except BaseException as e:
      self.log("WARNING: Could not find XSLT at " + xsl_file)
      self.log(f"\tError: {e}")
      sys.exit(88)


    
  def read_sushi_config(self):
    try:
        with open(self.sushi_file, 'r') as file:
            self.sushi_config = yaml.safe_load(file)
            if not self.sushi_config:
              self.log("Could not load sushi config")
              return False          
            self.log("Got sushi config:\n\t" + pprint.pformat(self.sushi_config).replace("\n","\n\t"))
            return True
    except FileNotFoundError:
        self.log("Could not find sushi config")
        return False
    except yaml.YAMLError as e:
       self.log("Could not parse sushi config")
       return False
    return True

  def get_ig_config(self):
    return self.sushi_config

  def get_ig_publisher(self):
    if not 'publisher' in self.sushi_config or not 'name' in self.sushi_config['publisher']:
      return "Self Published"
    return self.sushi_config['publisher']['name']
  
  def get_ig_canonical(self):
    return self.sushi_config['canonical']

  def get_ig_name(self):
    return self.sushi_config['name']

  def get_ig_title(self):
    return self.sushi_config['title']

  def get_ig_id(self):
    return self.sushi_config['id']

  def get_ig_version(self):
    return self.sushi_config['version']
  
  def install(self):
    self.install_aliases()
    self.install_resources()
    self.install_dmns()
    self.install_pages()
    self.install_cqls()

  def install_cqls(self):
    for id,cql in self.cqls.items():
      self.install_cql(id,cql)
        
  def install_pages(self):
    for id,page in self.pages.items():
      self.install_page(id,page)


  dmn_tables = {}
  def add_dmn_table(self,dt_id:str,dt_dmn:str):
    if dt_id in self.dmn_tables:
      self.log("**Warning** found duplicated decitiosn table with id=" + dt_id)
    self.log("Added " + dt_id + " with content\n" + str(dt_dmn))
    self.dmn_tables[dt_id] = dt_dmn

  def name_to_lower_id(self,name):
    if ( not (isinstance(name,str))):
      return None
    return self.name_to_id(name.lower())
    
  def name_to_id(self,name):    
    if ( not (isinstance(name,str))):
      return None
    id = re.sub('[^0-9a-zA-Z\\-\\.]+', '', name)
    # to work around jekyll error, make sure there are no trailing periods...
    id = id.rstrip('.')
    if len(id) > 55:
      # make length of an id is 64 characters
      #we need to make use of hashes
      self.log("ERROR: name of id is too long. hashing.: " + id)
      id = self.to_hash(id,55)
      self.log("Escaping id " + name + " to " + id )
    return id


  def to_hash(self,input:str,len:int):
    return input[:len -10] + str(hashlib.shake_256(input.encode()).hexdigest(5))



  def escape_code(self,input):
    original = input
    if ( not (isinstance(input,str))):
        return None
    input = input.strip()
    input = re.sub(r"['\"]","",input)
    #SUSHI BUG on processing codes with double quote.  sushi fails
    #Example \"Bivalent oral polio vaccine (bOPV)–inactivated polio vaccine (IPV)\" schedule (in countries with high vaccination coverage [e.g. 90–95%] and low importation risk [where neighbouring countries and/or countries that share substantial population movement have a similarly high coverage])" 

    input = re.sub(r"\s+"," ",input)
    if len(input) > 245:
       # max filename size is 255, leave space for extensions such as .fsh
      self.log("ERROR: name of id is too long.hashing: " + input)        
      input = self.to_hash(input,245)
      self.log("Escaping code " + original + " to " + input )
    return input

  def xml_escape(self,input):
    if ( not (isinstance(input,str))):
      return ""
    # see https://stackoverflow.com/questions/1546717/escaping-strings-for-use-in-xml
    return input.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\"", "&quot;").replace("'", "&apos;")    
  def escape(self,input):
    if ( not (isinstance(input,str))):
        return None
    return input.replace('"', r'\"')


  def install_dmns(self):
    result = True
    for dt_id,dmn_table in self.dmn_tables.items():
      result &= self.install_dmn(dt_id,dmn_table)
    return result



  def add_rulesets(self):
    return True
    for ruleset_file in glob.glob(self.get_base_dir() + "/input/fsh/rulesets/*fsh"):      
      ruleset_id =  str(os.path.splitext(os.path.basename(ruleset_file))[0])
      with open(ruleset_file, 'r') as file:
        self.log("Opned " + ruleset_file)
        ruleset = str(file.read())
        self.add_resource("rulesets",ruleset_id,ruleset)



    
  alias_file = "input/fsh/Aliases.fsh"
  aliases = []  #should change this to a set...

  def get_base_aliases(self):
    ig_alias_file = self.get_base_dir() + "/" + self.alias_file
    with open(ig_alias_file, 'r') as file:
      return str(file.read()).split("\n")
        
  
  def add_aliases(self , aliases):
    for alias in aliases:
      if alias not in self.aliases:
        self.aliases.append(alias)

  def install_aliases(self):
    try:
        if not os.path.exists(self.alias_file):
            with open(filename, 'w') as file:
                for alias in set(self.aliases):
                    self.log("Adding alias:" + alias)
                    file.write(alias + "\n")
                file.close()
        else:
            with open(self.alias_file, 'r+') as file:
                content = file.read()
                for alias in set(self.aliases):
#                    self.log("Checking alias:" + alias)
                    if alias not in content:
                        self.log("Adding alias:" + alias)
                        file.write('\n' + alias + '\n')
                file.close()
    except IOError as e:
        self.log("Could not insert aliases")
        self.log(f"\tError: {e}")



  def install_page(self,id,page:str):
    try:
      file_path = "input/pagecontent/" + id + ".md"
      file = open(file_path,"w")
      print (page,file=file)
      file.close()
      self.log("Installed " + file_path)
    except IOError as e:
      self.log("Could not save page with id: " + id + "\n")
      self.log(f"\tError: {e}")
    return True
    

        
  def install_cql(self,id,cql:str):
    try:
      file_path = "input/cql/" + id + ".cql"
      file = open(file_path,"w")
      print (cql,file=file)
      file.close()
      self.log("Installed " + file_path)
    except IOError as e:
      self.log("Could not save CQL with id: " + id + "\n")
      self.log(f"\tError: {e}")
    return True


  def process_multifile_xml(self, multifile_xml: Union[str, ET.Element]) -> bool:
    """
        Parses a multi-file XML bundle and writes each file to disk according to its 'name' attribute.
        This is for XML of the form:
        <files>
          <file name="path/to/file.ext" mime-type="..."><![CDATA[...]]></file>
          ...
        </files>

        Args:
            multifile_xml: XML as string or lxml.etree.Element/ElementTree

        Returns:
            True on success, False on error (with logging).
    """
    try:
      # Parse input if it's a string
      if isinstance(multifile_xml, str):
        try:
          root = ET.fromstring(multifile_xml)
        except Exception as e:
          self.log(f"ERROR: Could not parse multifile_xml string: {e}")
          return False
      elif isinstance(multifile_xml, (ET._Element, ET.ElementBase)):
        root = multifile_xml
      elif hasattr(multifile_xml, "getroot"):  # ElementTree
        root = multifile_xml.getroot()
      else:
        self.log(f"ERROR: multifile_xml is not a recognized XML type: {type(multifile_xml)}")
        return False
      self.log(f"Multifile={ET.tostring(multifile_xml)}")


      # Validate XML against schema
      if not self.multifile_schema.validate(xml_doc):
        self.log("XML failed XSD validation!")
        for error in self.multifile_schema.error_log:
          self.log(f"XSD validation error: {error}")
        return False
      
      if root.tag != "files":
        self.log(f"ERROR: Expected root element <files>, got <{root.tag}> instead.")
        return False
      file_elements = root.findall("file")
      if not file_elements:
        self.log("WARNING: No <file> elements found in multifile XML.")
        return False
      for file_elem in file_elements:
        file_path = file_elem.get("name")
        self.log("Extracting "  + file_path)
        mime_type = file_elem.get("mime-type", "text/plain")
        #content = etree.XML(file_elem.text) or ""
        content = file_elem.text
        if not file_path:
          self.log("ERROR: <file> element missing 'name' attribute, skipping.")
          continue
        
        try:
          os.makedirs(os.path.dirname(file_path), exist_ok=True)
          with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
            self.log(f"Created file: {file_path} (mime-type: {mime_type}, {len(content)} bytes) with content:" + str(content))
        except Exception as fe:
          self.log(f"ERROR: Could not write to file '{file_path}': {fe}")
          return False          

    except Exception as ex:
      self.log(f"FATAL ERROR in process_multifile_xml: {ex}")
      return False

    return True
  
  def transform_xml(self,prefix:str,xml:Union[str,ET.ElementTree],out_path:Union[str,Path,bool] = False , process_multiline = False):
    if not prefix in self.xslts:
      self.log("trying to transform unregistered thing "  + prefix)
      return False
    self.log("B0")
    if isinstance(xml,ET._ElementTree) or isinstance(xml,ET._Element):
      self.log("B1")
      xml_tree = xml
    elif isinstance(xml,str):
      self.log("B2")
      xml = re.sub(r'<\?xml[^>]+\?>', '', xml)
      try:        
        xml_tree = ET.XML(xml)
        self.log("B3")
        ET.indent(xml_tree)
        self.log("B4")
      except BaseException as e:
        self.log("ERROR: Generated invalid XML for " + prefix + "\n" +  f"\tError: {e}\n" )
        return False
    else:
      self.log("invalid xml sent to transformer=" + str(xml))
      return False
    self.log("B5")
    
    try:
      self.log("B5.1")
      out = self.xslts[prefix](xml_tree)
      if out_path:
        self.log("B5.2")
        self.log("Transforming " + prefix + " to " + str(out_path))
        self.log("B5.2.1")
        out = str(ET.tostring(out.getroot() , encoding="unicode",pretty_print=True, doctype=None))
        self.log("B5.3")
        out_file = open(out_path, "w")
        out_file.write(out)
        out_file.close()
      elif process_multiline:
        self.log("B6")
        return self.process_multifile_xml(out)
      else:
        self.log("B7")
        return out
    except BaseException as e:
      self.log("Could not process " + prefix + " in " + str(xml_tree))
      self.log(f"\tError: {e}")
      return False
    
    return True


  
  def install_dmn(self,id,dmn:str):
    try:
      dmn_tree = ET.XML(dmn)
      ET.indent(dmn_tree)
    except BaseException as e:
      self.log("ERROR: Generated invalid XML for DMN id " + id +"\n" +  f"\tError: {e}\n" )
      return False
    
    try:
      dmn_path = Path("input/dmn/") /  f"{id}.dmn"
      dmn_file = open(dmn_path,"w")
      #self.log(ET.tostring(dmn_tree,encoding="unicode"))
      dmn_file.write(ET.tostring(dmn_tree,encoding="unicode"))
      #print(ET.tostring(dmn_tree,encoding="unicode"),file=dmn_file)
      dmn_file.close()
      self.log("Installed " + str(dmn_path))
    except IOError as e:
      self.log("Could not save DMN with id: " + id + "\n")
      log(f"\tERROR: {e}")
      return False

    html_path = Path("input/pagecontent/") / f"{id}.xml"
    return self.transform_xml("dmn",dmn_tree,out_path = html_path )
    
      
  
  def install_resources(self):
    result = True
    for directory, instances in self.resources.items() :
      for id,resource in instances.items() :
        try:
          file_path = "input/fsh/" + directory + "/" + id + ".fsh"
          Path("input/fsh/" + directory).mkdir(exist_ok=True, parents=True)
          file = open(file_path,"w")
          print(resource,file=file)
          file.close()
          self.log("Installed " + file_path)
        except IOError as e:
          result = False
          self.log("Could not save resource of type: " + directory + "  with id: " + id + "\n")
          self.log(f"\tError: {e}")
    return result

  def render_codesystem(self,id:str):
    if (not id in self.codesystems) or (not id in self.codesystem_titles):
      self.log("Trying to render absent codesystem " + id)
      return ""
    title = self.codesystem_titles[id]
    codesystem = 'CodeSystem: ' + self.escape(id) + '\n'
    codesystem += 'Title: "' + self.escape(title) + '"\n'
    codesystem += 'Description:  "CodeSystem for ' + self.escape(title) + '. Autogenerated from DAK artifacts"\n'
    codesystem += '* ^experimental = false\n'
    codesystem += '* ^caseSensitive = false\n'
    codesystem += '* ^status = #active\n'
    for code,vals in self.codesystem_properties[id].items():
      codesystem += '* ^property[+].code = #"' + self.escape_code(code) + '"\n'
      for k,v in vals.items():
        codesystem += '* ^property[=].' + k + ' = ' + v + "\n" # user is responsible for content

    for code,val in self.codesystems[id].items():
      self.log("Attempting to add " + str(code) )
      if isinstance(val,str):
        codesystem += '* #"' + self.escape_code(code) +  '" "' + self.escape(name) + '"\n'
      elif isinstance(val,dict)  and 'display' in val:
        codesystem += '* #"' + self.escape_code(code) +  '" "' + self.escape(val['display']) + '"\n'
        if 'definition' in val:
          codesystem += '  * ^definition = """' + val['definition'] + '\n"""\n'
        if 'designation' in val and isinstance(val['designation'],list):
          for d_val in val['designation']:
            if not isinstance(d_val,dict) or not 'value' in d_val:
              continue
            codesystem += '  * ^designation[+].value = ' + d_val['value'] + "\n"
            d_val.pop('value')
            for k,v in d_val.items():
              codesystem += '  * ^designation[=].' + k + " = " + v + "\n"
            
        if 'propertyString' in val and isinstance(val['propertyString'],dict):
          for p_code,p_val in val['propertyString'].items():
            codesystem += '  * ^property[+].code = #"' + self.escape(p_code) +  '"\n'
            codesystem += '  * ^property[=].valueString = "' + self.escape(p_val) +  '"\n'
      else:
        self.log("  failed to add code (expected string or dict with 'display' property)" + str(code))
        self.log(pprint.pp(val))

    return codesystem



  def initialize_codesystem(self,codesystem_id:str,title:str):
    if codesystem_id in self.codesystems:
      self.log("WARNING: reinitializing codesystem " + codesystem_id)
    self.codesystems[codesystem_id] = {}
    self.codesystem_titles[codesystem_id] = title
    self.codesystem_properties[codesystem_id] = {}
    # need to replace this type of logic with exception handling probably
    return True


  def add_codesystem_properties(self,codesystem_id:str,vals:dict):
    for k,v in vals.items():
      self.add_codesystem_property(codesystem_id,k,v)
      
  def add_codesystem_property(self,codesystem_id:str,k:str,v):
    self.codesystem_properties[codesystem_id][k] = v

  def add_dict_to_codesystem(self,codesystem_id:str,inputs:dict):
    result = True
    for code,expr in inputs.items():
      result &= self.add_to_codesystem(codesystem_id,code,expr)
    return result
    
  def add_to_codesystem(self,codesystem_id:str,code:str,expr:str):
    if not codesystem_id in self.codesystems:
      self.log("ERROR: Code system not initialized " + codesystem_id)
      return False

    if code in self.codesystems[codesystem_id] and expr != self.codesystems[codesystem_id][code]:
        # want this to be a structured ERROR for quality control back to the L2 authors
        self.log("ERROR: non-matching definitions for code " + code + " in code system " + codesystem_id)
        return False
      
    self.codesystems[codesystem_id][code] = expr
    return True


  def generate_vs_from_list(self,id:str, codesystem_id:str, title:str, codes):
        
    valueset = 'ValueSet: ' + self.escape(id) + '\n'
    valueset += 'Title: "' + self.escape(title) + '"\n'
    valueset += 'Description:  "Value Set for ' + self.escape(title) + '. Autogenerated from DAK artifacts"\n'
    valueset += '* ^status = #active\n'
    valueset += '* ^experimental = false\n'
    for code in codes:
      valueset += '* include ' + self.escape(codesystem_id) + '#"' + self.escape_code(code) + '"\n'
    
    self.add_resource('valuesets',id, valueset)

    return True

  

  def generate_cs_and_vs_from_dict(self,id:str, title:str, codelist:dict , properties:dict = {}):
    if not self.initialize_codesystem(id,title):
      self.log("Skipping CS and VS for " + str + " could not initialize")
      return False
    if not self.add_dict_to_codesystem(id,codelist):
      self.log("Skipping CS and VS for " + str + " could not add dictionary")
      return False
    self.add_codesystem_properties(id,properties)

    codesystem = self.render_codesystem(id)
    
    valueset = 'ValueSet: ' + self.escape(id) + '\n'
    valueset += 'Title: "' + self.escape(title) + '"\n'
    valueset += 'Description:  "Value Set for ' + self.escape(title) + '. Autogenerated from DAK artifacts"\n'
    valueset += '* ^status = #active\n'
    valueset += '* ^experimental = false\n'
    valueset += '* include codes from system ' + self.escape(id) + '\n'

    self.add_resource('codesystems',id,codesystem)
    self.add_resource('valuesets',id, valueset)
    return True
  
  def add_resource(self,dir,id,resource:str):
    self.resources[dir][id]=resource


  def add_cql(self,id,cql:str):
    self.cqls[id]=cql

  def add_page(self,id,page:str):
    self.pages[id]=page


  def create_cql_library(self,lib_name,cql_codes:dict ={}, properties:dict = {}):
    lib_id = self.name_to_id(lib_name)
    cql =  "/*\n"
    cql += "@libname: " + lib_name + "\n"
    cql += "@libid: " + lib_id + "\n"
    for k,v in properties.items():
      cql += '@' + k + ': ' + v + "\n"
    cql += "*/\n"
    cql += "library " + lib_id + "\n"
    #cql += "using FHIR version '4.0.1'\n"
    #cql += "include FHIRHelpers version '4.0.1'\n" #do we want to include some common libraries?
    cql += "\ncontext Patient\n"

    if not isinstance(cql_codes,dict):
      self.log("Invalid CQL code definitions for " + lib_name)
      sys.exit()
      return False
    
    for name,val in cql_codes.items():
      if isinstance(val,str):
        cql += "\n/*\n"
        cql += "@name: " + name + "\n"
        cql += "@pseudocode: " + val + "\n"
        cql += " */\n"
        cql += "define \"" + self.escape(name) + "\":\n"
        cql += "  //CQL AUTHORS: you need to insert stuff here\n"
      elif isinstance(val,dict):
        cql += "\n/*\n"
        cql += "Autogenerated documentation from DAK\n"
        cql += "@name: " + name + "\n"
        for k,v in val.items():
          cql += "@" + k + ": " + str(v) + "\n"            
        cql += " */\n"
        cql += "define \"" + self.escape(name) + "\":\n"
        cql += "  //CQL AUTHORS: you need to insert stuff here\n"
        if 'pseudocode' in val:
          cql += "  // " + "\n   // ".join(val['pseudocode'].splitlines(True)) + "\n"
          
    self.add_cql(lib_id,cql)
    
    library = "Instance: " + lib_id + "\n"
    library += "InstanceOf: Library\n"
    library += "Title: \"" + self.escape(lib_name) + "\"\n"
    library += "Description: \"This library defines context-independent elements for "  + lib_name + "\"\n"
    library += "Usage: #definition\n"
    library += "* insert LogicLibrary( " + lib_id + " )\n"    
    self.add_resource("libraries",lib_id,library)

    
  def log(self,*statements):
    for statement in statements:
      print(str(statement) ,  file=sys.stderr)
      self.logfile.write(str(statement) + "\n")
    self.logfile.flush()


    
