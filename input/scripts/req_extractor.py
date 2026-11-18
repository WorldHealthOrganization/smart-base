"""
Requirements Extractor for SMART Guidelines

This module provides functionality to extract and process functional requirements
from structured documents for the SMART guidelines system. It handles requirements
specifications and converts them into FHIR-compatible resources for implementation
and traceability.

The extractor processes requirements documents to ensure proper integration
with the broader SMART guidelines clinical decision support framework.

Author: SMART Guidelines Team
"""
from typing import List
import os
import glob
import re
import pandas as pd

import stringer
from extractor import extractor
from installer import installer


class req_extractor(extractor):
    """
    Extractor for functional requirements processing.

    This extractor processes requirements documents and specifications,
    converting them into appropriate FHIR resources for use in clinical
    decision support implementations.
    """

    def __init__(self, installer: installer) -> None:
        super().__init__(installer)

    def find_files(self) -> List[str]:
        return glob.glob("input/system-requirements/*xlsx")

        # def usage():
        #   print("Usage: scans input/system-requirements for excel sheets ")
        #   print("where the referenced excel contains a sheet entitled 'Non-functional'")
        #   print("and one entitled 'Functional' which contain the requirements.")
        #   print("The header row of the 'Non-functional' sheet should contain: ")
        #   print("   " , ', '.join(nonfunctional_headers))
        #   print("The header row of the 'Functional' sheet should contain: ")
        #   print("   " , ', '.join(nonfunctional_headers))
        #   print("OPTIONS:")
        #   print(" none")
        #   print("--help|h : print this information")
        #   sys.exit(2)

    def extract_file(self):
        try:
            self.extract_resources()
        except ValueError as e:
            self.logger.info(
                "Could not process: " +
                self.inputfile_name +
                "\n")
            self.logger.info(f"\tError: {e}")
            return False
        return True

    def extract_resources(self):
        functional_column_maps = {
            'reqid': ["Requirement ID", "Requirement"],
            'activityid-and-name': ["Activity ID and name", "Activity ID and description"],
            'as-a': ["As a"],
            'i-want': ["I want", "I want to"],
            'so-that': ["So that"]
        }
        sheet_names = ['Functional']
        functional = self.retrieve_data_frame_by_headers(
            functional_column_maps, sheet_names)

        if (not self.extract_functional_requirements_to_resources(functional)):
            self.logger.info(
                "Could not extract functional requirements from: " +
                self.inputfile_name)
            return False

        nonfunctional_column_maps = {
            'reqid': [
                "Requirement",
                "Requirement ID"],
            'category': [
                "Category",
                "Category ID"],
            'requirement': [
                "Non-functional requirement",
                "Non-functional requirements",
                "Nonfunctional requirements",
                "nonfunctional requirement"]}
        sheet_names = ['Non-Functional', 'Non-functional']
        nonfunctional = self.retrieve_data_frame_by_headers(
            nonfunctional_column_maps, sheet_names)

        if (not self.extract_nonfunctional_requirements_to_resources(nonfunctional)):
            self.logger.info(
                "Could not extract non-functional requirements from: " +
                self.inputfile_name)
            return False
        return True

    def extract_nonfunctional_requirements_to_resources(
            self, nonfunctional: pd.DataFrame) -> bool:
        self.logger.info("Reading non-functional requirements")
        if nonfunctional is None:
            return False
        nonfunctional.drop(index=0)

        categories = {}
        cat_cs = 'FXREQCategories'
        classification = ""
        classification_codes = []

        for index, row in nonfunctional.iterrows():
            if "reqid" not in row or not isinstance(row["reqid"], str):
                self.logger.info("// skipping row " +
                                 str(index + 1) + ": no reqid")
                continue
            reqid = stringer.name_to_id(row["reqid"])

            self.logger.info(
                "\tRow:\n" +
                "\t\t" +
                row.to_string().replace(
                    "\n",
                    "\n\t\t"))

            # check if this is setting up the classifications
            if (row["reqid"].strip().lower().startswith(
                    "classification of digital health interventions")):
                classification = row["reqid"].strip()
                classification_codes = re.findall(r'\b\d+(?:\.\d+)*\b', classification)
                self.logger.info(
                    "\tFound classification text: " +
                    classification)
                self.logger.info(
                    "\tFound classification codes: " + str(classification_codes))
                continue

            if "category" not in row or not isinstance(row["category"], str):
                self.logger.info("// skipping row " +
                                 str(index + 1) + ": no category")
                continue
            if "requirement" not in row or not isinstance(
                    row["requirement"], str):
                self.logger.info("// skipping row " +
                                 str(index + 1) + ": no requirement")
                continue

            cat = row["category"].strip()
            catid = stringer.name_to_id(cat)
            categories[catid] = cat  # OK to overwrite existing

            nfreq = row["requirement"].strip()

            lm_id = "LM." + reqid
            lm = "Instance: " + stringer.escape(lm_id) + '\n'
            lm += 'InstanceOf: NonFunctionalRequirement\n'
            lm += 'Description: "' + stringer.escape(nfreq) + '"\n'
            lm += 'Usage: #definition\n'
            lm += '* id = "' + stringer.escape(lm_id) + '"\n'
            lm += '* requirement = "' + stringer.escape(nfreq) + '"\n'
            if (catid):
                lm += '* category = ' + \
                    stringer.escape(cat_cs) + '#' + stringer.escape(catid) + '\n'
            for classification_code in classification_codes:
                lm += '* classification[+] = ' + stringer.escape(self.class_cs) + '#' \
                    + stringer.escape(classification_code) + '\n'

            instance = "//non-functional requirment instance generated from row " + \
                str(index + 1) + "\n"
            instance += "Instance: " + reqid + "\n"
            instance += "InstanceOf: SGRequirements\n"
            instance += "Usage: #definition" + "\n"
            instance += '* title = "' + stringer.escape(nfreq) + '"\n'
            instance += '* status = $pubStatus#active\n'
            instance += '* name = "' + stringer.escape(nfreq) + '"\n'
            instance += '* publisher = "WHO"\n'
            instance += '* experimental = true\n'
            description = '*Category*: ' + \
                stringer.escape(cat) + "\n" + stringer.escape(nfreq)
            description = '* description = """\n' + description + '\n"""\n\n'
            instance += description + "\n"
            self.installer.add_resource('instances', lm_id, lm)
            self.installer.add_resource('requirements', reqid, instance)

        self.logger.info(
            "Read " + str(len(nonfunctional)) +
            " non-functional requirement row(s)")

        self.installer.generate_cs_and_vs_from_dict(
            cat_cs, 'Functional Requirement Categories', categories)
        return True

    def extract_functional_requirements_to_resources(
            self, functional: pd.DataFrame) -> bool:
        self.logger.info("Reading functional requirements")
        if functional is None:
            return False
        businessprocess_code = ""
        businessprocess_name = ""
        businessprocess_codes = {}
        classification = ""
        classification_codes = []
        bpid = "FXREQBusinessProcesses"

        functional.drop(index=0)

        for index, row in functional.iterrows():
            if "reqid" not in row or not isinstance(row["reqid"], str):
                self.logger.info("// skipping row " +
                                 str(index + 1) + ": no reqid")
                continue
            reqid = stringer.name_to_id(row["reqid"])

            self.logger.info(
                "\tRow:\n" +
                "\t\t" +
                row.to_string().replace(
                    "\n",
                    "\n\t\t"))

            # check if this is setting up the classifications
            if (row["reqid"].strip().lower().startswith(
                    "classification of digital health interventions")):
                classification = row["reqid"].strip()
                classification_codes = re.findall(r'\b\d+(?:\.\d+)*\b', classification)
                self.logger.info(
                    "\tFound classification text: " +
                    classification)
                self.logger.info(
                    "\tFound classification codes: " + str(classification_codes))
                continue

            if (row["reqid"].strip().lower().startswith("business process")):
                businessprocess = row["reqid"].strip()[16:].strip()
                self.logger.info("\tFound business process row " +
                                 str(index + 1) + ": " + businessprocess)
                parts = businessprocess.split(":", 2)
                if (len(parts) == 2):
                    businessprocess_code = parts[0].strip()
                    businessprocess_name = parts[1].strip()
                    self.logger.info(
                        "\tFound business process code (" +
                        businessprocess_code +
                        ") associated to " +
                        businessprocess_name)
                    businessprocess_codes[businessprocess_code] = businessprocess_name

            if (businessprocess_code):
                reqid = reqid + "." + businessprocess_code

            if "activityid-and-name" not in row or not isinstance(
                    row["activityid-and-name"], str):
                self.logger.info("\t*warning* skipping row " +
                                 str(index + 1) + ": no activityid-and-name")
                continue

            if "as-a" not in row or not isinstance(row["as-a"], str):
                self.logger.info("\t*warning* skipping row " +
                                 str(index + 1) + ": no as-a")
                continue

            if "i-want" not in row or not isinstance(row["i-want"], str):
                self.logger.info("\t*warning* skipping row " +
                                 str(index + 1) + ": no i-want")
                continue

            if "so-that" not in row or not isinstance(row["so-that"], str):
                self.logger.info("\t*warning* skipping row " +
                                 str(index + 1) + ": no so-that")
                continue

            components = row["activityid-and-name"].split(".")
            activityid = ".".join(components[:-1])
            activity_name = components[-1]

            actor_name = row["as-a"].strip()
            actor_id = stringer.name_to_id(actor_name)
            actor_instance = "Instance: " + stringer.escape(actor_id) + "\n"
            actor_instance += "InstanceOf: $SGActor\n"
            actor_instance += "Usage: #definition\n"
            actor_instance += '* name = "' + stringer.escape(actor_name) + '"\n'
            actor_instance += '* title = "' + stringer.escape(actor_name) + '"\n'
            actor_instance += '* description = "Actor ' + \
                stringer.escape(actor_name) + ' from Function Requirements"\n'
            actor_instance += '* status = $pubStatus#active\n'
            actor_instance += '* experimental = true\n'
            actor_instance += '* publisher = "WHO"\n'
            actor_instance += '* type = $actorType#person\n'
            self.installer.add_resource(
                'actors', actor_id, actor_instance)  # ok to overwrite
            actorlink = '<a href="ActorDefinition-' + \
                stringer.escape(actor_id) + '.html">' + stringer.escape(actor_name) + '</a>'

            description = 'Activity: ' + activity_name + ':\n' + "As a " + actorlink + ", I want to:\n>" + \
                stringer.escape(row['i-want']) + '\n\nso that\n\n>' + stringer.escape(row['so-that'])
            if (businessprocess_name):
                if (businessprocess_code):
                    description = "*Business process* (" + stringer.escape(businessprocess_code) + ") "  \
                        + stringer.escape(businessprocess_name) + ":\n" + description
                else:
                    description = "*Business process* " + \
                        stringer.escape(businessprocess_name) + ":\n\n" + description

            lm_id = "LM." + reqid
            lm = "Instance: " + stringer.escape(lm_id) + '\n'
            lm += 'InstanceOf: FunctionalRequirement\n'
            lm += 'Description: """' + description + '"""\n'
            lm += 'Usage: #definition\n'
            lm += '* id = "' + stringer.escape(lm_id) + '"\n'
            lm += '* activity = "' + stringer.escape(activity_name) + '"\n'
            lm += '* actor[+] = Reference(' + stringer.escape(actor_id) + ')\n'
            lm += '* capabilityMarkdown = "' + stringer.escape(row['i-want']) + '"\n'
            lm += '* benefitMarkdown = "' + stringer.escape(row['so-that']) + '"\n'
            if (businessprocess_code):
                lm += '* classification[+] = ' + bpid + '#' + \
                    stringer.escape(businessprocess_code) + '\n'
            for classification_code in classification_codes:
                lm += '* classification[+] = ' + stringer.escape(self.class_cs) + '#' \
                    + stringer.escape(classification_code) + '\n'
            self.installer.add_resource('instances', lm_id, lm)

            instance = "//functional requirment instance generated from row " + \
                str(index + 1) + "\n"
            instance += "Instance: " + stringer.escape(reqid) + "\n"
            instance += "InstanceOf: SGRequirements\n"
            instance += "Usage: #definition" + "\n"
            instance += '* title = "' + stringer.escape(activity_name) + '"\n'
            instance += '* status = $pubStatus#active\n'
            instance += '* name = "' + stringer.escape(activity_name) + '"\n'
            instance += '* publisher = "WHO"\n'
            instance += '* experimental = true\n'
            instance += '* actor[+] = Canonical(' + \
                stringer.escape(actor_id) + ')\n'
            instance += '* extension[userstory].extension[capability].valueString = "' + \
                stringer.escape(row['i-want']) + '"\n'
            instance += '* extension[userstory].extension[benefit].valueString = "' + \
                stringer.escape(row['so-that']) + '"\n'
            description = '* description = """\n' + description + '\n"""\n\n'
            instance += description + "\n"
            self.installer.add_resource('requirements', reqid, instance)

        self.logger.info(
            "Read " + str(len(functional)) +
            " functional requirement row(s)")
        self.logger.info("Business Process Codes:\n\t" + str(businessprocess_codes))
        self.installer.generate_cs_and_vs_from_dict(
            bpid, 'Functional Requirements Business Processes', businessprocess_codes)
        return True
