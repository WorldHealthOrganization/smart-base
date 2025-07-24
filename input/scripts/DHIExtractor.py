"""
DHI Extractor for processing digital health intervention classifications.
Extracts classifications and interventions from text files.
"""
import installer
from extractor import extractor

class DHIExtractor(extractor):

  def __init__(self, installer):
    super().__init__(installer)

  def find_files(self):
      return ['input/data/system_categories.txt','input/data/dhi_v1.txt']
    
  def extract_to_resources(self, inputfile_name, resources):
    if (inputfile_name == 'input/data/system_categories.txt'):
      self.extract_categories(inputfile_name, resources)
    if (inputfile_name == 'input/data/dhi_v1.txt'):
      self.extract_interventions(inputfile_name, resources)
    
    
  def extract_categories(self, filename, resources):
    cdhi_id = 'CDHIv1'
    cdhsc_id = 'CDSCv1'
    cm_id = "CDHIv1Hierarchy"

    print ("System Categories")
    interventions = {}
    for line in open(filename, 'r'):
      parts = line.strip().split(' ',1)
      if (len(parts) < 2):
          continue
      code = parts[0].strip().rstrip(".")
      intervention = parts[1].strip()
      print ("\t" + intervention + ' = ' + code)
      interventions[code] = intervention
    
    self.installer.generate_cs_and_vs_from_dict(cdhsc_id, 'Classification of Digital Health System Categories v1', interventions, resources)

  def extract_interventions(self, filename, resources):
    cdhi_id = 'CDHIv1'
    print ("Interventions")
    interventions = {}
    parent_map = {}

    for line in open(filename, 'r'):
      parts = line.strip().split(' ',1)
      if (len(parts) < 2):
          continue
      codes = parts[0].strip().split('.')
      code = ".".join(codes)
      parent_code = ".".join(codes[:-1])
      intervention = parts[1].strip()
      print ("\t" + intervention + ' = ' + code)
      interventions[code] = intervention
      if (parent_code):
          parent_map[code] = parent_code        
    self.installer.generate_cs_and_vs_from_dict(cdhi_id, 'Classification of Digital Health Interventions v1', interventions, resources)

    if (len(parent_map) > 0): 
      title = "Hierarchy of the Classification of Digital Health Interventions v1"
      cm = "Instance:  " + self.escape(cm_id) + '\n'
      cm += "InstanceOf:   ConceptMap\n"
      cm += "Description:  \"Mapping to represent hierarchy within " + title + ".\"\n"
      cm += "Usage:        #definition\n"
      cm += "* name = \"" + self.escape(cm_id) + "\"\n"
      cm += "* title = \"" + self.escape(title) + "\"\n"
      cm += "* status = #active\n"
      cm += "* experimental = false\n"
      cm += "* sourceCanonical = Canonical(" + cdhi_id + ")\n"
      cm += "* targetCanonical = Canonical(" + cdhi_id + ")\n"
      cm += "* group[+]\n"
      cm += "  * source = Canonical(" + cdhi_id + ")\n"
      cm += "  * target = Canonical(" + cdhi_id + ")\n"
      for code,parent_code in parent_map.items():
          cm += "  * insert ElementMap( " +  code + ", " + parent_code + ", narrower)\n"
      resources.setdefault('conceptmaps', {})[cm_id] = cm
