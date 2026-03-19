#!/usr/bin/env python3
"""Tests for import_salesforce.py"""

import json
import os
import sys
import tempfile
import unittest

# Add scripts directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from import_salesforce import (
    extract_product_fields,
    fsh_escape,
    generate_bulk_supplier_lm_instances,
    generate_concept_map,
    generate_document_lm_instances,
    generate_holders,
    generate_ingredient_lm_instances,
    generate_manufacturer_lm_instances,
    generate_manufacturers,
    generate_metadata_codesystem,
    generate_nra_lm_instances,
    generate_packaging_lm_instances,
    generate_presentations_codesystem,
    generate_products_and_authorizations,
    generate_site_lm_instances,
    generate_vaccine_lm_instances,
    generate_vaccine_types_codesystem,
    load_json_file,
    md5hash,
    read_existing_codes,
    sanitize_alpha,
    sanitize_code,
)


SAMPLE_PRODUCT = {
    "ProductDetails": {
        "Identification": {"Id": "a3K3X000005atRtUAI", "Name": "FVP-P-447"},
        "Type": "Finished Vaccine Product",
        "DateOfPreQualifiedAcceptance": "2023-12-19",
        "AssessmentProcedure": "Prequalification - Standard",
        "ApplicantOrganization": {
            "Identification": {
                "Id": "0013X00003cPkzfQAC",
                "Name": "Serum Institute of India",
            },
            "Address": {
                "AddressLine1": "212/2 Off Soli Poonawala Road",
                "City": "Pune",
                "State": "Maharashtra",
                "Country": "India",
                "PostalCode": "411 028",
                "ISOCountryCode": "IND",
                "Region": "SEARO",
            },
            "Contact": [{"Website": "http://www.seruminstitute.com/"}],
        },
        "BulkSupplier": {"Id": None, "Name": None},
        "ConsumptionDetails": {"Diluent": None},
        "DosageDetails": {"NoOfDosagesPerPrimaryContainer": "2"},
        "StorageDetails": {"ShelfLife": "24 months", "Temperature": "2 - 8\u00b0C"},
        "PharmaceuticalForm": "Liquid: Ready to use",
        "Presentation": "Vial",
        "PresentationOther": None,
        "NRADetails": {
            "Identification": {
                "Id": "0013X0000498p4fQAA",
                "Name": "Central Drugs Standard Control Organization (CDSCO)",
            },
            "Address": {"AddressLine1": None, "Country": "India"},
            "Contact": [{"Website": "www.cdsco.nic.in"}],
        },
        "VaccineDetails": {
            "Identification": {"Id": "a3S3X000003cSpnUAE"},
            "VaccineName": {
                "FullName": "Recombinant malaria vaccine",
                "AbbreviatedName": "Malaria",
                "CommercialName": "CYVAC",
            },
            "RouteOfAdministrationVx": "Intramuscular",
            "VialMonitor": "Type 14",
            "MultidoseVialPolicy": "WHO recommends that opened vials of this vaccine should be discarded 6 hours after opening or at the end of the immunization session, whichever comes first.",
        },
        "Status": "Prequalified",
        "PreservativeDetails": {"Id": "None"},
        "PreservativeConcentartionDetails": {"Id": None},
        "LastPublishingDate": "2024-09-10T14:16:34.000Z",
        "PublishingRemarks": None,
    },
    "ProductPackaging": [
        {
            "Id": "a3HNN0000007wYl2AI",
            "ComponentPacked": "Active (Vaccine)",
            "ShippingContainer": {
                "Configuration": "Shipping box",
                "Volume": "71.5 x 60.5 x 63.5",
                "TotalDoses": "3600",
                "TotalContainers": "1800",
            },
            "FVPPackagingType": "Shipping Container",
        }
    ],
    "DocumentDetails": [
        {
            "Identification": {
                "Id": "069NN000005lDn4YAE",
                "Name": "-FVP-P-446-447_R21Malaria_SIIPL_PI-2023_2",
            },
            "Type": "Product Insert",
            "VersionId": "068NN0000061zZCYAY",
            "FileExtension": "pdf",
            "FileType": "PDF",
        }
    ],
}

# Product with bulk supplier, sites, and ingredients
SAMPLE_PRODUCT_WITH_EXTRAS = {
    "ProductDetails": {
        "Identification": {"Id": "a3K3X000006MihtUAC", "Name": "FVP-P-63"},
        "Type": "Finished Vaccine Product",
        "DateOfPreQualifiedAcceptance": "2008-12-01",
        "AssessmentProcedure": "Prequalification - Standard",
        "ApplicantOrganization": {
            "Identification": {
                "Id": "0013X0000498p2wQAA",
                "Name": "Haffkine Bio Pharmaceutical Corporation Ltd",
            },
            "Address": {"City": "Mumbai", "Country": "India"},
            "Contact": [],
        },
        "BulkSupplier": {"Id": "0013X0000498p3IQAQ", "Name": "PT Bio Farma (Persero)"},
        "ConsumptionDetails": {"Diluent": None},
        "DosageDetails": {"NoOfDosagesPerPrimaryContainer": "20"},
        "StorageDetails": {"ShelfLife": "24 months", "Temperature": "2 - 8\u00b0C"},
        "PharmaceuticalForm": "Liquid: Ready to use",
        "Presentation": "Vial",
        "NRADetails": {
            "Identification": {
                "Id": "0013X0000498p4bQAA",
                "Name": "Central Drugs Standard Control Organization (CDSCO)",
            },
            "Address": {"Country": "India"},
            "Contact": [],
        },
        "VaccineDetails": {
            "Identification": {"Id": "a3S3X000003cSogUAE"},
            "VaccineName": {
                "FullName": "BCG Vaccine",
                "AbbreviatedName": "BCG",
                "CommercialName": "BCG Vaccine",
            },
            "RouteOfAdministrationVx": "Intradermal",
        },
        "Status": "Prequalified",
        "PreservativeDetails": {"Id": "None"},
        "PreservativeConcentartionDetails": {"Id": None},
    },
    "SiteDetails": [
        {
            "Organization": {
                "Identification": {
                    "Id": "0013X0000498p2wQAA",
                    "Name": "Haffkine Bio Pharmaceutical Corporation Ltd",
                },
                "Address": {
                    "AddressLine1": "Acharya Donde Marg, Parel",
                    "City": "Mumbai",
                    "Country": "India",
                },
            },
            "Status": "Accepted",
            "SiteActivity": "FVP Manufacture",
        }
    ],
    "ProductIngredients": [
        {
            "Identification": {"Id": None},
            "Type": "Vx FVP",
            "Unit": "%",
            "Product": "a3K3X000006MihtUAC",
            "ProductComponentType": "Diluent",
            "Function": None,
        }
    ],
}


class TestSanitizers(unittest.TestCase):
    def test_sanitize_code(self):
        self.assertEqual(sanitize_code("Hello World!"), "HelloWorld")
        self.assertEqual(sanitize_code("BCG (Danish)"), "BCGDanish")

    def test_sanitize_alpha(self):
        self.assertEqual(sanitize_alpha("Two vial set"), "Twovialset")
        self.assertEqual(sanitize_alpha("Vial"), "Vial")

    def test_md5hash(self):
        result = md5hash("test")
        self.assertEqual(len(result), 32)
        self.assertEqual(result, "098f6bcd4621d373cade4e832627b4f6")

    def test_fsh_escape(self):
        self.assertEqual(fsh_escape(None), "")
        self.assertEqual(fsh_escape('Hello "World"'), 'Hello \\"World\\"')
        self.assertEqual(fsh_escape("back\\slash"), "back\\\\slash")


class TestExtractProductFields(unittest.TestCase):
    def test_basic_extraction(self):
        fields = extract_product_fields(SAMPLE_PRODUCT)
        self.assertEqual(fields["sf_product_id"], "a3K3X000005atRtUAI")
        self.assertEqual(fields["sf_product_name"], "FVP-P-447")
        self.assertEqual(fields["product_type"], "Finished Vaccine Product")
        self.assertEqual(fields["date_of_prequal"], "2023-12-19")
        self.assertEqual(fields["presentation"], "Vial")
        self.assertEqual(fields["num_doses"], "2")
        self.assertEqual(fields["applicant_name"], "Serum Institute of India")
        self.assertEqual(
            fields["nra_name"],
            "Central Drugs Standard Control Organization (CDSCO)",
        )
        self.assertEqual(fields["vaccine_commercial_name"], "CYVAC")
        self.assertEqual(fields["vaccine_abbreviated_name"], "Malaria")
        self.assertEqual(fields["vaccine_full_name"], "Recombinant malaria vaccine")
        self.assertEqual(fields["status"], "Prequalified")
        self.assertEqual(fields["pharmaceutical_form"], "Liquid: Ready to use")
        self.assertEqual(fields["assessment_procedure"], "Prequalification - Standard")
        self.assertEqual(fields["route_of_administration"], "Intramuscular")
        self.assertEqual(fields["vial_monitor"], "Type 14")
        self.assertIn("WHO recommends", fields["multidose_vial_policy"])
        # Referenced object fields
        self.assertEqual(fields["applicant_website"], "http://www.seruminstitute.com/")
        self.assertEqual(fields["applicant_city"], "Pune")
        self.assertEqual(fields["applicant_state"], "Maharashtra")
        self.assertEqual(fields["nra_website"], "www.cdsco.nic.in")
        self.assertEqual(fields["nra_country"], "India")
        self.assertEqual(fields["vaccine_type_id"], "a3S3X000003cSpnUAE")
        # Preservative fields (None -> empty string)
        self.assertEqual(fields["preservative"], "")
        self.assertEqual(fields["preservative_concentration"], "")
        # Bulk supplier fields (None -> empty string)
        self.assertEqual(fields["bulk_supplier_id"], "")
        self.assertEqual(fields["bulk_supplier_name"], "")
        # Packaging/document lists
        self.assertEqual(len(fields["packaging"]), 1)
        self.assertEqual(len(fields["documents"]), 1)

    def test_product_with_extras(self):
        fields = extract_product_fields(SAMPLE_PRODUCT_WITH_EXTRAS)
        self.assertEqual(fields["bulk_supplier_id"], "0013X0000498p3IQAQ")
        self.assertEqual(fields["bulk_supplier_name"], "PT Bio Farma (Persero)")
        self.assertEqual(len(fields["sites"]), 1)
        self.assertEqual(len(fields["ingredients"]), 1)

    def test_empty_product(self):
        fields = extract_product_fields({})
        self.assertEqual(fields["sf_product_id"], "")
        self.assertEqual(fields["presentation"], "")
        self.assertEqual(fields["product_type"], "")


class TestGenerateFSH(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()
        self.products = [extract_product_fields(SAMPLE_PRODUCT)]

    def test_generate_presentations(self):
        generate_presentations_codesystem(self.products, self.tmpdir)
        cs_path = os.path.join(self.tmpdir, "codesystems", "prequal_presentation.fsh")
        self.assertTrue(os.path.exists(cs_path))
        content = open(cs_path).read()
        self.assertIn("CodeSystem: PreQualPresentation", content)
        self.assertIn('#Vial "Vial"', content)

    def test_generate_vaccine_types(self):
        generate_vaccine_types_codesystem(self.products, self.tmpdir)
        cs_path = os.path.join(
            self.tmpdir, "codesystems", "preQualVaccineTypes.fsh"
        )
        self.assertTrue(os.path.exists(cs_path))
        content = open(cs_path).read()
        self.assertIn("CodeSystem: PreQualVaccineType", content)
        self.assertIn('#Malaria "Malaria"', content)

    def test_generate_manufacturers(self):
        generate_manufacturers(self.products, self.tmpdir)
        path = os.path.join(
            self.tmpdir, "examples", "prequal_database_manufacturers.fsh"
        )
        self.assertTrue(os.path.exists(path))
        content = open(path).read()
        self.assertIn("Serum Institute of India", content)
        self.assertIn("IHE.mCSD.Organization", content)
        self.assertIn("0013X00003cPkzfQAC", content)

    def test_generate_holders(self):
        generate_holders(self.products, self.tmpdir)
        path = os.path.join(
            self.tmpdir, "examples", "prequal_database_holders.fsh"
        )
        self.assertTrue(os.path.exists(path))
        content = open(path).read()
        self.assertIn("Central Drugs Standard Control Organization (CDSCO)", content)
        self.assertIn("$orgType#govt", content)

    def test_generate_products_and_authorizations(self):
        generate_products_and_authorizations(self.products, self.tmpdir)
        examples_path = os.path.join(
            self.tmpdir, "examples", "prequal_database_products.fsh"
        )
        cs_path = os.path.join(
            self.tmpdir,
            "codesystems",
            "prequal_database_products_identifiers.fsh",
        )
        vs_path = os.path.join(
            self.tmpdir,
            "valuesets",
            "prequal_database_products_identifiers.fsh",
        )

        self.assertTrue(os.path.exists(examples_path))
        self.assertTrue(os.path.exists(cs_path))
        self.assertTrue(os.path.exists(vs_path))

        content = open(examples_path).read()
        self.assertIn("InstanceOf: FinishedVaccineProducts", content)
        self.assertIn("a3K3X000005atRtUAI", content)
        self.assertIn("CYVAC", content)

        # Verify coded metadata fields use code syntax (not string)
        self.assertIn("productType = #FinishedVaccineProduct", content)
        self.assertIn("status = #Prequalified", content)
        self.assertIn("assessmentProcedure = #PrequalificationStandard", content)
        self.assertIn("pharmaceuticalForm = #LiquidReadytouse", content)
        self.assertIn("routeOfAdministration = #Intramuscular", content)

        # Verify string fields still use string syntax
        self.assertIn('applicantName = "Serum Institute of India"', content)
        self.assertIn('nraName = "Central Drugs Standard Control Organization (CDSCO)"', content)

        # Verify new fields are written
        self.assertIn('vialMonitor = "Type 14"', content)
        self.assertIn('multidoseVialPolicy = "WHO recommends', content)
        self.assertIn('shelfLife = "24 months"', content)
        self.assertIn('nraCountry = "India"', content)
        self.assertIn("lastPublishingDate = 2024-09-10", content)
        self.assertIn('vaccineTypeId.value = "a3S3X000003cSpnUAE"', content)
        self.assertIn('applicantId.value = "0013X00003cPkzfQAC"', content)
        self.assertIn('nraId.value = "0013X0000498p4fQAA"', content)

        # Verify old CSV-model fields are NOT present
        self.assertNotIn("vaccineType.coding", content)
        self.assertNotIn("commercialName", content)
        self.assertNotIn("manufacturer.text", content)
        self.assertNotIn("responsibleNRA.text", content)

        # Verify $Product and $ProductAuthorization instances are NOT generated
        self.assertNotIn("InstanceOf: $Product", content)
        self.assertNotIn("InstanceOf: $ProductAuthorization", content)

        # Verify LM linkages
        self.assertIn("manufacturerLM = Reference(PreQualManufacturer", content)
        self.assertIn("nraLM = Reference(PreQualNRA", content)
        self.assertIn("vaccineLM = Reference(PreQualVaccine", content)

        # Verify packaging and document LM linkages
        self.assertIn("packagingLM = Reference(PreQualPackaging", content)
        self.assertIn("documentLM = Reference(PreQualDocument", content)

        cs_content = open(cs_path).read()
        self.assertIn("CodeSystem: PreQualProductIds", cs_content)

        vs_content = open(vs_path).read()
        self.assertIn("ValueSet: PreQualProductIds", vs_content)


class TestGenerateMetadataCodeSystem(unittest.TestCase):
    def test_generate_metadata_codesystem(self):
        tmpdir = tempfile.mkdtemp()
        products = [extract_product_fields(SAMPLE_PRODUCT)]
        generate_metadata_codesystem(products, tmpdir)

        cs_path = os.path.join(tmpdir, "codesystems", "prequal_database_metadata.fsh")
        self.assertTrue(os.path.exists(cs_path))
        content = open(cs_path).read()
        self.assertIn("CodeSystem: PreQualDatabaseMetadata", content)
        self.assertIn('#FinishedVaccineProduct "Finished Vaccine Product"', content)
        self.assertIn('#PrequalificationStandard "Prequalification - Standard"', content)
        self.assertIn('#Prequalified "Prequalified"', content)
        self.assertIn('#LiquidReadytouse "Liquid: Ready to use"', content)
        self.assertIn('#Intramuscular "Intramuscular"', content)
        self.assertIn('#ShippingContainer "Shipping Container"', content)
        self.assertIn('#ActiveVaccine "Active (Vaccine)"', content)
        self.assertIn('#ProductInsert "Product Insert"', content)

        vs_path = os.path.join(tmpdir, "valuesets", "prequal_database_metadata.fsh")
        self.assertTrue(os.path.exists(vs_path))
        vs_content = open(vs_path).read()
        self.assertIn("ValueSet: PreQualDatabaseMetadata", vs_content)


class TestGenerateLMInstances(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()
        self.products = [extract_product_fields(SAMPLE_PRODUCT)]

    def test_generate_manufacturer_lm_instances(self):
        generate_manufacturer_lm_instances(self.products, self.tmpdir)
        path = os.path.join(
            self.tmpdir, "examples", "prequal_database_manufacturer_lm.fsh"
        )
        self.assertTrue(os.path.exists(path))
        content = open(path).read()
        self.assertIn("InstanceOf: PreQualManufacturer", content)
        self.assertIn("Serum Institute of India", content)
        self.assertIn("0013X00003cPkzfQAC", content)
        self.assertIn('city = "Pune"', content)
        self.assertIn('state = "Maharashtra"', content)
        self.assertIn('country = "India"', content)
        self.assertIn('website = "http://www.seruminstitute.com/"', content)
        self.assertIn("organizationReference = Reference(Manufacturer", content)

    def test_generate_nra_lm_instances(self):
        generate_nra_lm_instances(self.products, self.tmpdir)
        path = os.path.join(
            self.tmpdir, "examples", "prequal_database_nra_lm.fsh"
        )
        self.assertTrue(os.path.exists(path))
        content = open(path).read()
        self.assertIn("InstanceOf: PreQualNRA", content)
        self.assertIn("Central Drugs Standard Control Organization (CDSCO)", content)
        self.assertIn("0013X0000498p4fQAA", content)
        self.assertIn('country = "India"', content)
        self.assertIn('website = "www.cdsco.nic.in"', content)
        self.assertIn("organizationReference = Reference(Holder", content)

    def test_generate_vaccine_lm_instances(self):
        generate_vaccine_lm_instances(self.products, self.tmpdir)
        path = os.path.join(
            self.tmpdir, "examples", "prequal_database_vaccine_lm.fsh"
        )
        self.assertTrue(os.path.exists(path))
        content = open(path).read()
        self.assertIn("InstanceOf: PreQualVaccine", content)
        self.assertIn("a3S3X000003cSpnUAE", content)
        self.assertIn('fullName = "Recombinant malaria vaccine"', content)
        self.assertIn('abbreviatedName = "Malaria"', content)

    def test_generate_packaging_lm_instances(self):
        generate_packaging_lm_instances(self.products, self.tmpdir)
        path = os.path.join(
            self.tmpdir, "examples", "prequal_database_packaging_lm.fsh"
        )
        self.assertTrue(os.path.exists(path))
        content = open(path).read()
        self.assertIn("InstanceOf: PreQualProductPackaging", content)
        self.assertIn("a3HNN0000007wYl2AI", content)
        self.assertIn("packagingType = #ShippingContainer", content)
        self.assertIn("componentPacked = #ActiveVaccine", content)

    def test_generate_document_lm_instances(self):
        generate_document_lm_instances(self.products, self.tmpdir)
        path = os.path.join(
            self.tmpdir, "examples", "prequal_database_document_lm.fsh"
        )
        self.assertTrue(os.path.exists(path))
        content = open(path).read()
        self.assertIn("InstanceOf: PreQualDocumentDetail", content)
        self.assertIn("069NN000005lDn4YAE", content)
        self.assertIn("documentType = #ProductInsert", content)
        self.assertIn('fileExtension = "pdf"', content)

    def test_generate_bulk_supplier_lm_instances(self):
        products = [extract_product_fields(SAMPLE_PRODUCT_WITH_EXTRAS)]
        generate_bulk_supplier_lm_instances(products, self.tmpdir)
        path = os.path.join(
            self.tmpdir, "examples", "prequal_database_bulk_supplier_lm.fsh"
        )
        self.assertTrue(os.path.exists(path))
        content = open(path).read()
        self.assertIn("InstanceOf: PreQualBulkSupplier", content)
        self.assertIn("0013X0000498p3IQAQ", content)
        self.assertIn('name = "PT Bio Farma (Persero)"', content)

    def test_generate_site_lm_instances(self):
        products = [extract_product_fields(SAMPLE_PRODUCT_WITH_EXTRAS)]
        generate_site_lm_instances(products, self.tmpdir)
        path = os.path.join(
            self.tmpdir, "examples", "prequal_database_site_lm.fsh"
        )
        self.assertTrue(os.path.exists(path))
        content = open(path).read()
        self.assertIn("InstanceOf: PreQualSiteDetail", content)
        self.assertIn("0013X0000498p2wQAA", content)
        self.assertIn('siteOrganizationName = "Haffkine Bio Pharmaceutical Corporation Ltd"', content)
        self.assertIn("siteStatus = #Accepted", content)
        self.assertIn("siteActivity = #FVPManufacture", content)

    def test_generate_ingredient_lm_instances(self):
        products = [extract_product_fields(SAMPLE_PRODUCT_WITH_EXTRAS)]
        generate_ingredient_lm_instances(products, self.tmpdir)
        path = os.path.join(
            self.tmpdir, "examples", "prequal_database_ingredient_lm.fsh"
        )
        self.assertTrue(os.path.exists(path))
        content = open(path).read()
        self.assertIn("InstanceOf: PreQualProductIngredient", content)
        self.assertIn("ingredientType = #VxFVP", content)
        self.assertIn("productComponentType = #Diluent", content)


class TestLoadJsonFile(unittest.TestCase):
    def test_load_json(self):
        test_data = {
            "FinishedVaccineProducts": [SAMPLE_PRODUCT, SAMPLE_PRODUCT]
        }
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False
        ) as f:
            json.dump(test_data, f)
            tmp_path = f.name

        try:
            products = load_json_file(tmp_path)
            self.assertEqual(len(products), 2)
        finally:
            os.unlink(tmp_path)


class TestConceptMap(unittest.TestCase):
    def test_generate_concept_map(self):
        tmpdir = tempfile.mkdtemp()
        # Create a minimal CSV matching the sample product
        csv_path = os.path.join(tmpdir, "test.csv")
        with open(csv_path, "w") as f:
            f.write('"Date of Prequalification ","Vaccine Type","Commercial Name",Presentation,"No. of doses",Manufacturer,"Responsible NRA"\n')
            f.write('19/12/2023,Malaria,CYVAC,Vial,2,"Serum Institute of India","Central Drugs Standard Control Organization (CDSCO)"\n')

        products = [extract_product_fields(SAMPLE_PRODUCT)]
        generate_concept_map(products, csv_path, tmpdir)

        cm_path = os.path.join(
            tmpdir, "concept_maps", "prequal_csv_to_api.fsh"
        )
        self.assertTrue(os.path.exists(cm_path))
        content = open(cm_path).read()
        self.assertIn("ConceptMap", content)
        self.assertIn("PreQualCSVtoAPIConceptMap", content)

        # Verify FHIR R5 syntax is used (not R4)
        self.assertIn("sourceScopeUri", content)
        self.assertIn("targetScopeUri", content)
        self.assertIn("relationship = #equivalent", content)
        self.assertNotIn("sourceUri", content)
        self.assertNotIn("targetUri", content)
        self.assertNotIn("equivalence", content)


class TestSkipWithdrawnProducts(unittest.TestCase):
    def test_skip_products_with_missing_essential_data(self):
        """Products with empty commercial name, applicant, and NRA should be skipped."""
        tmpdir = tempfile.mkdtemp()
        # Create a withdrawn product with all essential fields empty
        withdrawn = extract_product_fields({
            "ProductDetails": {
                "Identification": {"Id": "a3K3X000006MihzUAC", "Name": "FVP-P-27"},
                "Status": "Withdrawn: Was Prequalified",
                "VaccineDetails": {"VaccineName": {}},
                "ApplicantOrganization": {"Identification": {}},
                "NRADetails": {"Identification": {}},
            }
        })
        normal = extract_product_fields(SAMPLE_PRODUCT)
        products = [withdrawn, normal]

        generate_products_and_authorizations(products, tmpdir)

        examples_path = os.path.join(
            tmpdir, "examples", "prequal_database_products.fsh"
        )
        content = open(examples_path).read()
        # The withdrawn product should be skipped
        self.assertNotIn("a3K3X000006MihzUAC", content)
        # The normal product should still be present
        self.assertIn("a3K3X000005atRtUAI", content)


class TestNullSubObjectIds(unittest.TestCase):
    """When a sub-object's Identification.Id is null, don't generate or link to its LM instance."""

    def test_manufacturer_lm_not_generated_without_id(self):
        """Manufacturer LM instances should only be generated when applicant ID is non-null."""
        tmpdir = tempfile.mkdtemp()
        product_no_id = extract_product_fields({
            "ProductDetails": {
                "Identification": {"Id": "PROD1", "Name": "Test"},
                "ApplicantOrganization": {
                    "Identification": {"Id": None, "Name": "NoIdManufacturer"},
                },
                "NRADetails": {"Identification": {}},
                "VaccineDetails": {"VaccineName": {}},
            }
        })
        products = [product_no_id]
        generate_manufacturer_lm_instances(products, tmpdir)
        path = os.path.join(tmpdir, "examples", "prequal_database_manufacturer_lm.fsh")
        # File should be empty (no instances) since the only manufacturer has no ID
        content = open(path).read()
        self.assertNotIn("InstanceOf: PreQualManufacturer", content)

    def test_nra_lm_not_generated_without_id(self):
        """NRA LM instances should only be generated when NRA ID is non-null."""
        tmpdir = tempfile.mkdtemp()
        product_no_id = extract_product_fields({
            "ProductDetails": {
                "Identification": {"Id": "PROD1", "Name": "Test"},
                "ApplicantOrganization": {"Identification": {}},
                "NRADetails": {
                    "Identification": {"Id": None, "Name": "NoIdNRA"},
                },
                "VaccineDetails": {"VaccineName": {}},
            }
        })
        products = [product_no_id]
        generate_nra_lm_instances(products, tmpdir)
        path = os.path.join(tmpdir, "examples", "prequal_database_nra_lm.fsh")
        content = open(path).read()
        self.assertNotIn("InstanceOf: PreQualNRA", content)

    def test_product_does_not_link_null_id_lm(self):
        """Product instances should not link to LMs when sub-object IDs are null."""
        tmpdir = tempfile.mkdtemp()
        product_null_ids = extract_product_fields({
            "ProductDetails": {
                "Identification": {"Id": "a3K_NULL_TEST", "Name": "FVP-NULL"},
                "Type": "Finished Vaccine Product",
                "DateOfPreQualifiedAcceptance": "2024-01-01",
                "Status": "Prequalified",
                "ApplicantOrganization": {
                    "Identification": {"Id": None, "Name": "SomeManufacturer"},
                },
                "NRADetails": {
                    "Identification": {"Id": None, "Name": "SomeNRA"},
                },
                "VaccineDetails": {
                    "Identification": {"Id": None},
                    "VaccineName": {"CommercialName": "TestVax"},
                },
            }
        })
        generate_products_and_authorizations([product_null_ids], tmpdir)
        path = os.path.join(tmpdir, "examples", "prequal_database_products.fsh")
        content = open(path).read()
        # Product should exist
        self.assertIn("a3K_NULL_TEST", content)
        # But should NOT link to manufacturer/NRA/vaccine LMs
        self.assertNotIn("manufacturerLM", content)
        self.assertNotIn("nraLM", content)
        self.assertNotIn("vaccineLM", content)
        # Should still have FHIR Organization references (those use md5 fallback)
        self.assertIn("manufacturerReference = Reference(Manufacturer", content)
        self.assertIn("responsibleNRAReference = Reference(Holder", content)


class TestAdditiveCodeSystems(unittest.TestCase):
    """CodeSystem generation must preserve existing codes that are not in current data."""

    def test_read_existing_codes(self):
        tmpdir = tempfile.mkdtemp()
        cs_path = os.path.join(tmpdir, "test.fsh")
        with open(cs_path, "w") as f:
            f.write('CodeSystem: Test\n')
            f.write('* #Foo "Foo label"\n')
            f.write('* #Bar "Bar label"\n')
        codes = read_existing_codes(cs_path)
        self.assertIn("Foo", codes)
        self.assertIn("Bar", codes)
        self.assertEqual(codes["Foo"], '* #Foo "Foo label"')

    def test_read_existing_codes_nonexistent_file(self):
        codes = read_existing_codes("/tmp/nonexistent_file_xyz.fsh")
        self.assertEqual(len(codes), 0)

    def test_presentations_preserves_existing_codes(self):
        tmpdir = tempfile.mkdtemp()
        os.makedirs(os.path.join(tmpdir, "codesystems"), exist_ok=True)
        os.makedirs(os.path.join(tmpdir, "valuesets"), exist_ok=True)
        # Pre-populate with extra code not in current data
        cs_path = os.path.join(tmpdir, "codesystems", "prequal_presentation.fsh")
        with open(cs_path, "w") as f:
            f.write('CodeSystem: PreQualPresentation\n')
            f.write('* #Vial "Vial"\n')
            f.write('* #Syringe "Pre-filled Syringe"\n')  # not in sample data

        products = [extract_product_fields(SAMPLE_PRODUCT)]
        generate_presentations_codesystem(products, tmpdir)
        content = open(cs_path).read()
        # Existing code preserved
        self.assertIn('#Syringe "Pre-filled Syringe"', content)
        # New/current code still present
        self.assertIn('#Vial "Vial"', content)

    def test_vaccine_types_preserves_existing_codes(self):
        tmpdir = tempfile.mkdtemp()
        os.makedirs(os.path.join(tmpdir, "codesystems"), exist_ok=True)
        os.makedirs(os.path.join(tmpdir, "valuesets"), exist_ok=True)
        cs_path = os.path.join(tmpdir, "codesystems", "preQualVaccineTypes.fsh")
        with open(cs_path, "w") as f:
            f.write('CodeSystem: PreQualVaccineType\n')
            f.write('* #Malaria "Malaria"\n')
            f.write('* #COVID19 "COVID-19"\n')  # not in sample data

        products = [extract_product_fields(SAMPLE_PRODUCT)]
        generate_vaccine_types_codesystem(products, tmpdir)
        content = open(cs_path).read()
        self.assertIn('#COVID19 "COVID-19"', content)
        self.assertIn('#Malaria "Malaria"', content)

    def test_metadata_preserves_existing_codes(self):
        tmpdir = tempfile.mkdtemp()
        os.makedirs(os.path.join(tmpdir, "codesystems"), exist_ok=True)
        os.makedirs(os.path.join(tmpdir, "valuesets"), exist_ok=True)
        cs_path = os.path.join(tmpdir, "codesystems", "prequal_database_metadata.fsh")
        with open(cs_path, "w") as f:
            f.write('CodeSystem: PreQualDatabaseMetadata\n')
            f.write('* #Prequalified "Prequalified"\n')
            f.write('* #OldLegacyCode "Some old value"\n')  # not in sample data

        products = [extract_product_fields(SAMPLE_PRODUCT)]
        generate_metadata_codesystem(products, tmpdir)
        content = open(cs_path).read()
        self.assertIn('#OldLegacyCode "Some old value"', content)
        self.assertIn('#Prequalified "Prequalified"', content)

    def test_product_ids_preserves_existing_codes(self):
        tmpdir = tempfile.mkdtemp()
        os.makedirs(os.path.join(tmpdir, "codesystems"), exist_ok=True)
        os.makedirs(os.path.join(tmpdir, "valuesets"), exist_ok=True)
        os.makedirs(os.path.join(tmpdir, "examples"), exist_ok=True)
        cs_path = os.path.join(tmpdir, "codesystems", "prequal_database_products_identifiers.fsh")
        with open(cs_path, "w") as f:
            f.write('CodeSystem: PreQualProductIds\n')
            f.write('* #a3K3X000005atRtUAI "FVP-P-447 (a3K3X000005atRtUAI)"\n')
            f.write('* #OldRemovedProduct "Old Product (OldRemovedProduct)"\n')

        products = [extract_product_fields(SAMPLE_PRODUCT)]
        generate_products_and_authorizations(products, tmpdir)
        content = open(cs_path).read()
        self.assertIn('#OldRemovedProduct "Old Product (OldRemovedProduct)"', content)
        self.assertIn("a3K3X000005atRtUAI", content)


if __name__ == "__main__":
    unittest.main()
