#!/usr/bin/env python3
"""Import WHO Vaccine PreQual data from the backend API.

Downloads paginated results from the PreQual API and generates:
  - FSH logical model instances (FinishedVaccineProducts)
  - FHIR Product and ProductAuthorization instances
  - CodeSystem and ValueSet FSH files
  - ConceptMap from old CSV MD5-based IDs to authoritative vaccine product IDs

Environment variables:
  PREQUAL_API_ENDPOINT  - API endpoint URL
  PREQUAL_API_USERNAME  - API username
  PREQUAL_API_PASSWORD  - API password

Usage:
  python scripts/import_salesforce.py [--output-dir DIR] [--csv-file FILE]
"""

import argparse
import csv
import hashlib
import json
import logging
import os
import re
import sys
import urllib.request
import urllib.error
import urllib.parse
import base64

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def sanitize_code(text):
    """Remove non-alphanumeric characters from text for use as FSH code."""
    return re.sub(r"[^A-Za-z0-9]", "", text)


def sanitize_alpha(text):
    """Remove non-alpha characters from text."""
    return re.sub(r"[^A-Za-z]", "", text)


def md5hash(text):
    """Compute MD5 hash of text (matching presushi.sh behavior)."""
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def fsh_escape(text):
    """Escape text for use in FSH string literals."""
    if text is None:
        return ""
    return text.replace("\\", "\\\\").replace('"', '\\"')


def read_existing_codes(filepath):
    """Read existing FSH code entries from a CodeSystem file.

    Parses lines matching ``* #<code> "<display>"`` and returns them
    as an ordered dict so that previously generated codes are preserved
    when the file is regenerated with new data.

    Args:
        filepath: Path to the .fsh file.

    Returns:
        OrderedDict mapping code string to full line (including the
        ``* #`` prefix).  Comment lines that immediately precede a
        block of codes (``// Category``) are stored with a key of
        ``__comment__<n>`` so they can be reproduced in order.
    """
    from collections import OrderedDict
    codes = OrderedDict()
    if not os.path.exists(filepath):
        return codes
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                stripped = line.rstrip("\n")
                m = re.match(r'^\* #(\S+)\s', stripped)
                if m:
                    codes[m.group(1)] = stripped
    except OSError:
        pass
    return codes


def fetch_api_page(endpoint, username, password, offset=0, limit=100):
    """Fetch a single page of results from the API using offset/limit pagination.

    The API returns an AdditionalInfo object with OffSet, Limit, and TotalRecords.

    Args:
        endpoint: Base API URL.
        username: API username.
        password: API password.
        offset: Record offset (0-based).
        limit: Maximum number of results to return.

    Returns:
        Parsed JSON response.
    """
    separator = "&" if "?" in endpoint else "?"
    url = f"{endpoint}{separator}offset={offset}&limit={limit}"
    logger.info("Fetching offset=%d limit=%d from %s", offset, limit, url)

    req = urllib.request.Request(url)
    credentials = base64.b64encode(f"{username}:{password}".encode("utf-8")).decode("ascii")
    req.add_header("Authorization", f"Basic {credentials}")
    req.add_header("Accept", "application/json")

    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


def download_all_pages(endpoint, username, password, page_size=100):
    """Download all pages of results from the API using offset/limit pagination.

    Uses AdditionalInfo.TotalRecords from the API response to determine
    when all records have been fetched.

    Args:
        endpoint: Base API URL.
        username: API username.
        password: API password.
        page_size: Number of results per request.

    Returns:
        List of FinishedVaccineProduct records.
    """
    all_products = []
    offset = 0
    total_records = None
    while True:
        data = fetch_api_page(endpoint, username, password, offset, page_size)
        products = data.get("FinishedVaccineProducts", [])
        if not products:
            break
        all_products.extend(products)

        # Use TotalRecords from API response to know when we're done
        additional_info = data.get("AdditionalInfo", {})
        if total_records is None:
            total_records = additional_info.get("TotalRecords")
            if total_records is not None:
                logger.info("API reports %d total records", total_records)

        logger.info("Downloaded %d products (offset=%d)", len(products), offset)
        offset += len(products)

        # Stop if we've fetched all records
        if total_records is not None and offset >= total_records:
            break

    logger.info("Total products downloaded: %d", len(all_products))
    return all_products


def load_json_file(path):
    """Load products from a local JSON file.

    Args:
        path: Path to JSON file.

    Returns:
        List of FinishedVaccineProduct records.
    """
    logger.info("Loading data from local file: %s", path)
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    products = data.get("FinishedVaccineProducts", [])
    logger.info("Loaded %d products from file", len(products))
    return products


def extract_product_fields(product):
    """Extract normalized fields from a single API product record.

    Args:
        product: A single FinishedVaccineProduct record from the API.

    Returns:
        Dictionary with normalized field values.
    """
    details = product.get("ProductDetails", {})
    ident = details.get("Identification", {})
    applicant = details.get("ApplicantOrganization", {})
    applicant_ident = applicant.get("Identification", {})
    applicant_addr = applicant.get("Address", {})
    applicant_contact = applicant.get("Contact", [])
    nra = details.get("NRADetails", {})
    nra_ident = nra.get("Identification", {})
    nra_addr = nra.get("Address", {})
    nra_contact = nra.get("Contact", [])
    vaccine = details.get("VaccineDetails", {})
    vaccine_ident = vaccine.get("Identification", {})
    vaccine_name = vaccine.get("VaccineName", {})
    dosage = details.get("DosageDetails", {})
    storage = details.get("StorageDetails", {})
    consumption = details.get("ConsumptionDetails", {})
    bulk_supplier = details.get("BulkSupplier", {})
    preservative = details.get("PreservativeDetails", {})
    preservative_conc = details.get("PreservativeConcentartionDetails", {})

    # Normalize preservative ID (can be a name like "Thiomersal" or "None" or null)
    preserv_id = preservative.get("Id", "") if preservative else ""
    if preserv_id in (None, "None", ""):
        preserv_id = ""
    preserv_conc_id = preservative_conc.get("Id", "") if preservative_conc else ""
    if preserv_conc_id is None:
        preserv_conc_id = ""

    # Normalize bulk supplier
    bs_id = bulk_supplier.get("Id", "") if bulk_supplier else ""
    if bs_id is None:
        bs_id = ""
    bs_name = bulk_supplier.get("Name", "") if bulk_supplier else ""
    if bs_name is None:
        bs_name = ""

    # Extract packaging, document, site, and ingredient details (raw)
    packaging = product.get("ProductPackaging", []) or []
    documents = product.get("DocumentDetails", []) or []
    sites = product.get("SiteDetails", []) or []
    ingredients = product.get("ProductIngredients", []) or []

    return {
        "sf_product_id": ident.get("Id", ""),
        "sf_product_name": ident.get("Name", ""),
        "product_type": details.get("Type", ""),
        "date_of_prequal": details.get("DateOfPreQualifiedAcceptance", ""),
        "assessment_procedure": details.get("AssessmentProcedure", ""),
        "status": details.get("Status", ""),
        "pharmaceutical_form": details.get("PharmaceuticalForm", ""),
        "presentation": details.get("Presentation", ""),
        "presentation_other": details.get("PresentationOther", ""),
        "num_doses": dosage.get("NoOfDosagesPerPrimaryContainer", ""),
        "vaccine_full_name": vaccine_name.get("FullName", ""),
        "vaccine_abbreviated_name": vaccine_name.get("AbbreviatedName", ""),
        "vaccine_commercial_name": vaccine_name.get("CommercialName", ""),
        "vaccine_type_id": vaccine_ident.get("Id", ""),
        "route_of_administration": vaccine.get("RouteOfAdministrationVx", ""),
        "vial_monitor": vaccine.get("VialMonitor", ""),
        "multidose_vial_policy": vaccine.get("MultidoseVialPolicy", ""),
        "applicant_id": applicant_ident.get("Id", ""),
        "applicant_name": applicant_ident.get("Name", ""),
        "applicant_address_line1": applicant_addr.get("AddressLine1", ""),
        "applicant_city": applicant_addr.get("City", ""),
        "applicant_state": applicant_addr.get("State", ""),
        "applicant_country": applicant_addr.get("Country", ""),
        "applicant_postal_code": applicant_addr.get("PostalCode", ""),
        "applicant_iso_country": applicant_addr.get("ISOCountryCode", ""),
        "applicant_region": applicant_addr.get("Region", ""),
        "applicant_website": applicant_contact[0].get("Website", "") if applicant_contact and isinstance(applicant_contact[0], dict) else "",
        "nra_id": nra_ident.get("Id", ""),
        "nra_name": nra_ident.get("Name", ""),
        "nra_address_line1": nra_addr.get("AddressLine1", ""),
        "nra_country": nra_addr.get("Country", ""),
        "nra_website": nra_contact[0].get("Website", "") if nra_contact and isinstance(nra_contact[0], dict) else "",
        "shelf_life": storage.get("ShelfLife", ""),
        "temperature": storage.get("Temperature", ""),
        "diluent": consumption.get("Diluent", ""),
        "last_publishing_date": details.get("LastPublishingDate", ""),
        "publishing_remarks": details.get("PublishingRemarks", ""),
        "preservative": preserv_id,
        "preservative_concentration": preserv_conc_id,
        "bulk_supplier_id": bs_id,
        "bulk_supplier_name": bs_name,
        "packaging": packaging,
        "documents": documents,
        "sites": sites,
        "ingredients": ingredients,
    }


def build_csv_md5_key(fields):
    """Build the MD5 hash key that presushi.sh uses for CSV-based IDs.

    The CSV export uses these columns:
      1: Date of Prequalification (DD/MM/YYYY)
      2: Vaccine Type (abbreviated name)
      3: Commercial Name
      4: Presentation
      5: No. of doses
      6: Manufacturer
      7: Responsible NRA

    presushi.sh concatenates all columns (with quotes removed) and computes MD5.

    Args:
        fields: Normalized product fields dict.

    Returns:
        MD5 hash string matching presushi.sh output, or None if matching not possible.
    """
    date_str = fields.get("date_of_prequal", "")
    if date_str and re.match(r"\d{4}-\d{1,2}-\d{1,2}", date_str):
        parts = date_str.split("-")
        date_csv = f"{parts[2]}/{parts[1]}/{parts[0]}"
    else:
        date_csv = date_str

    vax = fields.get("vaccine_abbreviated_name", "") or ""
    commercial = fields.get("vaccine_commercial_name", "") or ""
    presentation = fields.get("presentation", "") or ""
    num_doses = fields.get("num_doses", "") or ""
    manufacturer = fields.get("applicant_name", "") or ""
    nra = fields.get("nra_name", "") or ""

    md5_src = f"{date_csv} {vax} {commercial} {presentation} {num_doses} {manufacturer} {nra}"
    return md5hash(md5_src)


def generate_presentations_codesystem(products, output_dir):
    """Generate presentations CodeSystem and ValueSet FSH files.

    Preserves any existing codes in the file that are not in the current data.

    Args:
        products: List of normalized product field dicts.
        output_dir: Base output directory (e.g. input/fsh).
    """
    cs_path = os.path.join(output_dir, "codesystems", "prequal_presentation.fsh")
    os.makedirs(os.path.dirname(cs_path), exist_ok=True)

    existing = read_existing_codes(cs_path)

    # Build new codes from data
    new_codes = {}
    for p in products:
        pres = p.get("presentation", "")
        if pres:
            code = sanitize_alpha(pres)
            new_codes[code] = f'* #{code} "{fsh_escape(pres)}"'

    # Merge: existing first, then new
    merged = dict(existing)
    for code, line in new_codes.items():
        if code not in merged:
            merged[code] = line

    with open(cs_path, "w", encoding="utf-8") as f:
        f.write('Alias: $presentation = http://smart.who.int/pcmt-vaxprequal/CodeSystem/PreQualPresentation\n')
        f.write("CodeSystem: PreQualPresentation\n")
        f.write('Title : "WHO PreQualificaiton Vaccine Presentations"\n')
        f.write('Description: "WHO PreQualificaiton Vaccine Presentations"\n\n')
        for code in sorted(merged):
            f.write(f'{merged[code]}\n')

    vs_path = os.path.join(output_dir, "valuesets", "prequal_presentation.fsh")
    os.makedirs(os.path.dirname(vs_path), exist_ok=True)

    with open(vs_path, "w", encoding="utf-8") as f:
        f.write('Alias: $preQualPresentation = http://smart.who.int/pcmt-vaxprequal/CodeSystem/PreQualPresentation\n')
        f.write("ValueSet: PreQualPresentation\n")
        f.write('Title : "WHO PreQualificaiton Presentation "\n')
        f.write('Description: "WHO PreQualificaiton Presentation"\n\n\n')
        f.write("* include codes from system $preQualPresentation\n\n")

    logger.info("Generated presentations CodeSystem with %d codes", len(merged))


def generate_vaccine_types_codesystem(products, output_dir):
    """Generate vaccine types CodeSystem and ValueSet FSH files.

    Preserves any existing codes in the file that are not in the current data.

    Args:
        products: List of normalized product field dicts.
        output_dir: Base output directory (e.g. input/fsh).
    """
    cs_path = os.path.join(output_dir, "codesystems", "preQualVaccineTypes.fsh")
    os.makedirs(os.path.dirname(cs_path), exist_ok=True)

    existing = read_existing_codes(cs_path)

    # Build new codes from data
    new_codes = {}
    for p in products:
        vax = p.get("vaccine_abbreviated_name", "")
        if vax:
            code = sanitize_code(vax)
            new_codes[code] = f'* #{code} "{fsh_escape(vax)}"'

    # Merge: existing first, then new
    merged = dict(existing)
    for code, line in new_codes.items():
        if code not in merged:
            merged[code] = line

    with open(cs_path, "w", encoding="utf-8") as f:
        f.write('Alias: $vaccinetype = http://smart.who.int/pcmt-vaxprequal/CodeSystem/PreQualVaccineType\n')
        f.write("CodeSystem: PreQualVaccineType\n")
        f.write('Title : "WHO PreQualificaiton Vaccine VaccineTypes"\n')
        f.write('Description: "WHO PreQualificaiton Vaccine VaccineTypes"\n\n')
        for code in sorted(merged):
            f.write(f'{merged[code]}\n')

    vs_path = os.path.join(output_dir, "valuesets", "PreQualVacccineTypes.fsh")
    os.makedirs(os.path.dirname(vs_path), exist_ok=True)

    with open(vs_path, "w", encoding="utf-8") as f:
        f.write('Alias: $preQualVaccineType = http://smart.who.int/pcmt-vaxprequal/CodeSystem/PreQualVaccineType\n')
        f.write("ValueSet: PreQualVaccineType\n")
        f.write('Title : "WHO PreQualificaiton VaccineType "\n')
        f.write('Description: "WHO PreQualificaiton VaccineType"\n\n\n')
        f.write("* include codes from system $preQualVaccineType\n\n")

    logger.info("Generated vaccine types CodeSystem with %d codes", len(merged))


def generate_manufacturers(products, output_dir):
    """Generate manufacturer Organization instances FSH file.

    Args:
        products: List of normalized product field dicts.
        output_dir: Base output directory (e.g. input/fsh).
    """
    seen = {}
    for p in products:
        name = p.get("applicant_name", "")
        sf_id = p.get("applicant_id", "")
        if name and name not in seen:
            seen[name] = sf_id

    path = os.path.join(output_dir, "examples", "prequal_database_manufacturers.fsh")
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        f.write('Alias: $orgType = http://terminology.hl7.org/CodeSystem/organization-type\n')
        for name, sf_id in sorted(seen.items()):
            instance_id = sf_id if sf_id else md5hash(name)
            f.write(f"\nInstance: Manufacturer{sanitize_code(instance_id)}\n")
            f.write("InstanceOf: IHE.mCSD.Organization\n")
            f.write("Usage: #example\n")
            f.write(f'Title: "PreQual Manufacturer: {fsh_escape(name)}"\n')
            f.write(f'Description: "Vaccine Manufacturer Organization: {fsh_escape(name)}"\n')
            f.write("* active = true\n")
            f.write(f'* name = "{fsh_escape(name)}"\n')
            f.write("* type = $orgType#other\n")
            if sf_id:
                f.write(f'* identifier.system = "https://extranet.who.int/prequal/api"\n')
                f.write(f'* identifier.value = "{fsh_escape(sf_id)}"\n')

    logger.info("Generated %d manufacturer instances", len(seen))


def generate_holders(products, output_dir):
    """Generate NRA/holder Organization instances FSH file.

    Args:
        products: List of normalized product field dicts.
        output_dir: Base output directory (e.g. input/fsh).
    """
    seen = {}
    for p in products:
        name = p.get("nra_name", "")
        sf_id = p.get("nra_id", "")
        if name and name not in seen:
            seen[name] = sf_id

    path = os.path.join(output_dir, "examples", "prequal_database_holders.fsh")
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        f.write('Alias: $orgType = http://terminology.hl7.org/CodeSystem/organization-type\n')
        for name, sf_id in sorted(seen.items()):
            instance_id = sf_id if sf_id else md5hash(name)
            f.write(f"\nInstance: Holder{sanitize_code(instance_id)}\n")
            f.write("InstanceOf: IHE.mCSD.Organization\n")
            f.write("Usage: #example\n")
            f.write(f'Title: "PreQual NRA/Holder: {fsh_escape(name)}"\n')
            f.write(f'Description: "National Regulatory Authority: {fsh_escape(name)}"\n')
            f.write("* active = true\n")
            f.write(f'* name = "{fsh_escape(name)}"\n')
            f.write("* type = $orgType#govt\n")
            if sf_id:
                f.write(f'* identifier.system = "https://extranet.who.int/prequal/api"\n')
                f.write(f'* identifier.value = "{fsh_escape(sf_id)}"\n')

    logger.info("Generated %d holder instances", len(seen))


def generate_manufacturer_lm_instances(products, output_dir):
    """Generate PreQualManufacturer logical model instances FSH file.

    Args:
        products: List of normalized product field dicts.
        output_dir: Base output directory (e.g. input/fsh).
    """
    seen = {}
    for p in products:
        name = p.get("applicant_name", "")
        sf_id = p.get("applicant_id", "")
        if name and sf_id and name not in seen:
            seen[name] = p

    path = os.path.join(output_dir, "examples", "prequal_database_manufacturer_lm.fsh")
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        for name, p in sorted(seen.items()):
            sf_id = p.get("applicant_id", "")
            instance_id = sanitize_code(sf_id)
            mfr_org_ref = f"Manufacturer{instance_id}"

            country = p.get("applicant_country", "") or ""
            title_suffix = f" ({country})" if country else ""
            f.write(f"\nInstance: PreQualManufacturer{instance_id}\n")
            f.write("InstanceOf: PreQualManufacturer\n")
            f.write("Usage: #example\n")
            f.write(f'Title: "PreQual Manufacturer: {fsh_escape(name)}"\n')
            f.write(f'Description: "WHO PreQual Manufacturer: {fsh_escape(name)}{fsh_escape(title_suffix)}"\n')
            if sf_id:
                f.write(f'* manufacturerId.system = "https://extranet.who.int/prequal/api"\n')
                f.write(f'* manufacturerId.value = "{fsh_escape(sf_id)}"\n')
            f.write(f'* name = "{fsh_escape(name)}"\n')
            addr = p.get("applicant_address_line1")
            if addr:
                f.write(f'* addressLine1 = "{fsh_escape(addr)}"\n')
            city = p.get("applicant_city")
            if city:
                f.write(f'* city = "{fsh_escape(city)}"\n')
            state = p.get("applicant_state")
            if state:
                f.write(f'* state = "{fsh_escape(state)}"\n')
            country = p.get("applicant_country")
            if country:
                f.write(f'* country = "{fsh_escape(country)}"\n')
            postal = p.get("applicant_postal_code")
            if postal:
                f.write(f'* postalCode = "{fsh_escape(postal)}"\n')
            iso = p.get("applicant_iso_country")
            if iso:
                f.write(f'* isoCountryCode = "{fsh_escape(iso)}"\n')
            region = p.get("applicant_region")
            if region:
                f.write(f'* region = "{fsh_escape(region)}"\n')
            website = p.get("applicant_website")
            if website:
                f.write(f'* website = "{fsh_escape(website)}"\n')
            f.write(f"* organizationReference = Reference({mfr_org_ref})\n")

    logger.info("Generated %d manufacturer LM instances", len(seen))


def generate_nra_lm_instances(products, output_dir):
    """Generate PreQualNRA logical model instances FSH file.

    Args:
        products: List of normalized product field dicts.
        output_dir: Base output directory (e.g. input/fsh).
    """
    seen = {}
    for p in products:
        name = p.get("nra_name", "")
        sf_id = p.get("nra_id", "")
        if name and sf_id and name not in seen:
            seen[name] = p

    path = os.path.join(output_dir, "examples", "prequal_database_nra_lm.fsh")
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        for name, p in sorted(seen.items()):
            sf_id = p.get("nra_id", "")
            instance_id = sanitize_code(sf_id)
            holder_org_ref = f"Holder{instance_id}"

            nra_country = p.get("nra_country", "") or ""
            title_suffix = f" ({nra_country})" if nra_country else ""
            f.write(f"\nInstance: PreQualNRA{instance_id}\n")
            f.write("InstanceOf: PreQualNRA\n")
            f.write("Usage: #example\n")
            f.write(f'Title: "PreQual NRA: {fsh_escape(name)}"\n')
            f.write(f'Description: "WHO PreQual NRA: {fsh_escape(name)}{fsh_escape(title_suffix)}"\n')
            if sf_id:
                f.write(f'* nraId.system = "https://extranet.who.int/prequal/api"\n')
                f.write(f'* nraId.value = "{fsh_escape(sf_id)}"\n')
            f.write(f'* name = "{fsh_escape(name)}"\n')
            addr = p.get("nra_address_line1")
            if addr:
                f.write(f'* addressLine1 = "{fsh_escape(addr)}"\n')
            country = p.get("nra_country")
            if country:
                f.write(f'* country = "{fsh_escape(country)}"\n')
            website = p.get("nra_website")
            if website:
                f.write(f'* website = "{fsh_escape(website)}"\n')
            f.write(f"* organizationReference = Reference({holder_org_ref})\n")

    logger.info("Generated %d NRA LM instances", len(seen))


def generate_vaccine_lm_instances(products, output_dir):
    """Generate PreQualVaccine logical model instances FSH file.

    Args:
        products: List of normalized product field dicts.
        output_dir: Base output directory (e.g. input/fsh).
    """
    seen = {}
    for p in products:
        vax_id = p.get("vaccine_type_id", "")
        if vax_id and vax_id not in seen:
            seen[vax_id] = p

    path = os.path.join(output_dir, "examples", "prequal_database_vaccine_lm.fsh")
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        for vax_id, p in sorted(seen.items()):
            instance_id = sanitize_code(vax_id)

            full_name = p.get("vaccine_full_name", "") or ""
            abbr_name = p.get("vaccine_abbreviated_name", "") or ""
            vax_title = full_name or abbr_name or vax_id
            vax_desc_parts = [full_name, f"({abbr_name})" if abbr_name else ""]
            vax_desc = " ".join(part for part in vax_desc_parts if part).strip()
            f.write(f"\nInstance: PreQualVaccine{instance_id}\n")
            f.write("InstanceOf: PreQualVaccine\n")
            f.write("Usage: #example\n")
            f.write(f'Title: "PreQual Vaccine: {fsh_escape(vax_title)}"\n')
            f.write(f'Description: "WHO PreQual Vaccine: {fsh_escape(vax_desc)}"\n')
            f.write(f'* vaccineId.system = "https://extranet.who.int/prequal/api"\n')
            f.write(f'* vaccineId.value = "{fsh_escape(vax_id)}"\n')
            full_name = p.get("vaccine_full_name")
            if full_name:
                f.write(f'* fullName = "{fsh_escape(full_name)}"\n')
            abbr_name = p.get("vaccine_abbreviated_name")
            if abbr_name:
                f.write(f'* abbreviatedName = "{fsh_escape(abbr_name)}"\n')

    logger.info("Generated %d vaccine LM instances", len(seen))


def generate_metadata_codesystem(products, output_dir):
    """Generate PreQualDatabaseMetadata CodeSystem and ValueSet FSH files.

    Collects all unique coded values from the data for:
    ProductDetails.Type, AssessmentProcedure, Status, PharmaceuticalForm,
    RouteOfAdministration, PackagingType, ComponentPacked, DocumentType,
    SiteActivity, SiteStatus, IngredientType, ProductComponentType.

    Preserves any existing codes in the file that are not in the current data.

    Args:
        products: List of normalized product field dicts.
        output_dir: Base output directory (e.g. input/fsh).
    """
    # Collect unique values from all products
    product_types = set()
    assessment_procedures = set()
    statuses = set()
    pharmaceutical_forms = set()
    routes = set()
    packaging_types = set()
    component_packed = set()
    document_types = set()
    site_activities = set()
    site_statuses = set()
    ingredient_types = set()
    product_component_types = set()

    for p in products:
        pt = p.get("product_type", "")
        if pt:
            product_types.add(pt)
        ap = p.get("assessment_procedure", "")
        if ap:
            assessment_procedures.add(ap)
        s = p.get("status", "")
        if s:
            statuses.add(s)
        pf = p.get("pharmaceutical_form", "")
        if pf:
            pharmaceutical_forms.add(pf)
        ra = p.get("route_of_administration", "")
        if ra:
            routes.add(ra)
        for pkg in p.get("packaging", []) or []:
            pkgt = pkg.get("FVPPackagingType", "")
            if pkgt:
                packaging_types.add(pkgt)
            cp = pkg.get("ComponentPacked", "")
            if cp:
                component_packed.add(cp)
        for doc in p.get("documents", []) or []:
            dt = doc.get("Type", "")
            if dt:
                document_types.add(dt)
        for site in p.get("sites", []) or []:
            sa = site.get("SiteActivity", "")
            if sa:
                site_activities.add(sa)
            ss = site.get("Status", "")
            if ss:
                site_statuses.add(ss)
        for ing in p.get("ingredients", []) or []:
            it = ing.get("Type", "")
            if it:
                ingredient_types.add(it)
            pct = ing.get("ProductComponentType", "")
            if pct:
                product_component_types.add(pct)

    cs_path = os.path.join(output_dir, "codesystems", "prequal_database_metadata.fsh")
    os.makedirs(os.path.dirname(cs_path), exist_ok=True)

    existing = read_existing_codes(cs_path)

    categories = [
        ("ProductType", sorted(product_types)),
        ("AssessmentProcedure", sorted(assessment_procedures)),
        ("Status", sorted(statuses)),
        ("PharmaceuticalForm", sorted(pharmaceutical_forms)),
        ("RouteOfAdministration", sorted(routes)),
        ("PackagingType", sorted(packaging_types)),
        ("ComponentPacked", sorted(component_packed)),
        ("DocumentType", sorted(document_types)),
        ("SiteActivity", sorted(site_activities)),
        ("SiteStatus", sorted(site_statuses)),
        ("IngredientType", sorted(ingredient_types)),
        ("ProductComponentType", sorted(product_component_types)),
    ]

    # Build new codes from data, organized by category
    new_codes = {}
    for category, values in categories:
        for val in values:
            code = sanitize_code(val)
            new_codes[code] = f'* #{code} "{fsh_escape(val)}"'

    # Merge: existing codes preserved, new codes added
    merged = dict(existing)
    for code, line in new_codes.items():
        if code not in merged:
            merged[code] = line

    # Build category membership for output formatting
    code_to_category = {}
    for category, values in categories:
        for val in values:
            code = sanitize_code(val)
            code_to_category[code] = category
    # For existing codes not in new data, try to preserve category from file
    # (they'll go into an "Other" section if not matched)

    total_codes = 0
    with open(cs_path, "w", encoding="utf-8") as f:
        f.write('Alias: $prequal-metadata = http://smart.who.int/pcmt-vaxprequal/CodeSystem/PreQualDatabaseMetadata\n')
        f.write("CodeSystem: PreQualDatabaseMetadata\n")
        f.write('Title: "WHO PreQualification Database Metadata"\n')
        f.write('Description: "Coded metadata values from the WHO PreQualification database"\n')
        f.write("* ^experimental = true\n")
        f.write("* ^caseSensitive = true\n")
        f.write('* ^name = "PreQualDatabaseMetadata"\n')
        f.write("* ^status = #active\n\n")

        # Write codes organized by category
        written_codes = set()
        for category, values in categories:
            # Collect codes for this category, skipping duplicates from earlier categories
            cat_codes = {}
            for val in values:
                code = sanitize_code(val)
                if code not in written_codes:
                    cat_codes[code] = merged[code]

            if cat_codes:
                f.write(f"// {category}\n")
                for code in sorted(cat_codes):
                    f.write(f'{cat_codes[code]}\n')
                    written_codes.add(code)
                    total_codes += 1
                f.write("\n")

        # Write any existing codes that weren't categorized
        uncategorized = {c: l for c, l in merged.items() if c not in written_codes}
        if uncategorized:
            f.write("// Other\n")
            for code in sorted(uncategorized):
                f.write(f'{uncategorized[code]}\n')
                total_codes += 1
            f.write("\n")

    vs_path = os.path.join(output_dir, "valuesets", "prequal_database_metadata.fsh")
    os.makedirs(os.path.dirname(vs_path), exist_ok=True)

    with open(vs_path, "w", encoding="utf-8") as f:
        f.write('Alias: $prequal-metadata = http://smart.who.int/pcmt-vaxprequal/CodeSystem/PreQualDatabaseMetadata\n')
        f.write("ValueSet: PreQualDatabaseMetadata\n")
        f.write('Title: "WHO PreQualification Database Metadata"\n')
        f.write('Description: "Coded metadata values from the WHO PreQualification database"\n\n')
        f.write("* include codes from system $prequal-metadata\n")

    logger.info("Generated metadata CodeSystem with %d codes", total_codes)


def generate_bulk_supplier_lm_instances(products, output_dir):
    """Generate PreQualBulkSupplier logical model instances FSH file.

    Args:
        products: List of normalized product field dicts.
        output_dir: Base output directory (e.g. input/fsh).
    """
    seen = {}
    for p in products:
        bs_id = p.get("bulk_supplier_id", "")
        bs_name = p.get("bulk_supplier_name", "")
        if bs_id and bs_id not in seen:
            seen[bs_id] = bs_name

    if not seen:
        logger.info("No bulk supplier LM instances to generate")
        return

    path = os.path.join(output_dir, "examples", "prequal_database_bulk_supplier_lm.fsh")
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        for bs_id, bs_name in sorted(seen.items()):
            instance_id = sanitize_code(bs_id)
            bs_title = bs_name or bs_id
            f.write(f"\nInstance: PreQualBulkSupplier{instance_id}\n")
            f.write("InstanceOf: PreQualBulkSupplier\n")
            f.write("Usage: #example\n")
            f.write(f'Title: "PreQual Bulk Supplier: {fsh_escape(bs_title)}"\n')
            f.write(f'Description: "WHO PreQual Bulk Supplier: {fsh_escape(bs_title)}"\n')
            f.write(f'* bulkSupplierId.system = "https://extranet.who.int/prequal/api"\n')
            f.write(f'* bulkSupplierId.value = "{fsh_escape(bs_id)}"\n')
            if bs_name:
                f.write(f'* name = "{fsh_escape(bs_name)}"\n')

    logger.info("Generated %d bulk supplier LM instances", len(seen))


def generate_packaging_lm_instances(products, output_dir):
    """Generate PreQualProductPackaging logical model instances FSH file.

    Args:
        products: List of normalized product field dicts.
        output_dir: Base output directory (e.g. input/fsh).
    """
    all_pkgs = []
    for p in products:
        for pkg in p.get("packaging", []) or []:
            pkg_id = pkg.get("Id", "")
            if pkg_id:
                all_pkgs.append(pkg)

    if not all_pkgs:
        logger.info("No packaging LM instances to generate")
        return

    path = os.path.join(output_dir, "examples", "prequal_database_packaging_lm.fsh")
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        for pkg in all_pkgs:
            pkg_id = pkg["Id"]
            instance_id = sanitize_code(pkg_id)
            pkg_type = pkg.get("FVPPackagingType", "")
            component = pkg.get("ComponentPacked", "")
            cold_chain = pkg.get("ColdChainVolume", "")

            # Extract packaging details from the appropriate level
            secondary = pkg.get("SecondaryPackaging", {}) or {}
            tertiary = pkg.get("TertiaryPackaging", {}) or {}
            shipping = pkg.get("ShippingContainer", {}) or {}
            # Merge: take whatever detail level is present
            detail = {}
            for src in [secondary, tertiary, shipping]:
                for k, v in src.items():
                    if v and k not in detail:
                        detail[k] = v

            # Build title from packaging details
            pkg_desc_text = detail.get("Description", "")
            pkg_title = pkg_desc_text or pkg_type or "Packaging"
            f.write(f"\nInstance: PreQualPackaging{instance_id}\n")
            f.write("InstanceOf: PreQualProductPackaging\n")
            f.write("Usage: #example\n")
            f.write(f'Title: "PreQual Packaging: {fsh_escape(pkg_title)}"\n')
            f.write(f'Description: "WHO PreQual Product Packaging: {fsh_escape(pkg_title)}"\n')
            f.write(f'* packagingId.system = "https://extranet.who.int/prequal/api"\n')
            f.write(f'* packagingId.value = "{fsh_escape(pkg_id)}"\n')
            if pkg_type:
                f.write(f"* packagingType = #{sanitize_code(pkg_type)}\n")
            if component:
                f.write(f"* componentPacked = #{sanitize_code(component)}\n")
            if cold_chain:
                f.write(f'* coldChainVolume = "{fsh_escape(cold_chain)}"\n')
            desc = detail.get("Description", "")
            if desc:
                f.write(f'* description = "{fsh_escape(desc)}"\n')
            vol = detail.get("Volume", "")
            if vol:
                f.write(f'* volume = "{fsh_escape(vol)}"\n')
            td = detail.get("TotalDoses", "")
            if td:
                f.write(f'* totalDoses = "{fsh_escape(td)}"\n')
            tc = detail.get("TotalContainers", "")
            if tc:
                f.write(f'* totalContainers = "{fsh_escape(tc)}"\n')
            h = detail.get("Height", "")
            if h:
                f.write(f'* height = "{fsh_escape(h)}"\n')
            le = detail.get("Length", "")
            if le:
                f.write(f'* length = "{fsh_escape(le)}"\n')
            w = detail.get("Width", "")
            if w:
                f.write(f'* width = "{fsh_escape(w)}"\n')
            pc = detail.get("PrimaryContainers", "")
            if pc:
                f.write(f'* primaryContainers = "{fsh_escape(pc)}"\n')

    logger.info("Generated %d packaging LM instances", len(all_pkgs))


def generate_document_lm_instances(products, output_dir):
    """Generate PreQualDocumentDetail logical model instances FSH file.

    Args:
        products: List of normalized product field dicts.
        output_dir: Base output directory (e.g. input/fsh).
    """
    all_docs = []
    for p in products:
        for doc in p.get("documents", []) or []:
            doc_ident = doc.get("Identification", {})
            doc_id = doc_ident.get("Id", "")
            if doc_id:
                all_docs.append(doc)

    if not all_docs:
        logger.info("No document LM instances to generate")
        return

    path = os.path.join(output_dir, "examples", "prequal_database_document_lm.fsh")
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        for doc in all_docs:
            doc_ident = doc.get("Identification", {})
            doc_id = doc_ident.get("Id", "")
            doc_name = doc_ident.get("Name", "")
            instance_id = sanitize_code(doc_id)

            doc_type_val = doc.get("Type", "")
            doc_title = doc_name or doc_id
            doc_type_label = f" ({doc_type_val})" if doc_type_val else ""
            f.write(f"\nInstance: PreQualDocument{instance_id}\n")
            f.write("InstanceOf: PreQualDocumentDetail\n")
            f.write("Usage: #example\n")
            f.write(f'Title: "PreQual Document: {fsh_escape(doc_title)}"\n')
            f.write(f'Description: "WHO PreQual Document: {fsh_escape(doc_title)}{fsh_escape(doc_type_label)}"\n')
            f.write(f'* documentId.system = "https://extranet.who.int/prequal/api"\n')
            f.write(f'* documentId.value = "{fsh_escape(doc_id)}"\n')
            if doc_name:
                f.write(f'* documentName = "{fsh_escape(doc_name)}"\n')
            doc_type = doc.get("Type", "")
            if doc_type:
                f.write(f"* documentType = #{sanitize_code(doc_type)}\n")
            version_id = doc.get("VersionId", "")
            if version_id:
                f.write(f'* versionId = "{fsh_escape(version_id)}"\n')
            ext = doc.get("FileExtension", "")
            if ext:
                f.write(f'* fileExtension = "{fsh_escape(ext)}"\n')
            ft = doc.get("FileType", "")
            if ft:
                f.write(f'* fileType = "{fsh_escape(ft)}"\n')

    logger.info("Generated %d document LM instances", len(all_docs))


def generate_site_lm_instances(products, output_dir):
    """Generate PreQualSiteDetail logical model instances FSH file.

    Args:
        products: List of normalized product field dicts.
        output_dir: Base output directory (e.g. input/fsh).
    """
    all_sites = []
    seen_ids = set()
    for p in products:
        for site in p.get("sites", []) or []:
            org = site.get("Organization", {})
            org_ident = org.get("Identification", {})
            org_id = org_ident.get("Id", "")
            if org_id and org_id not in seen_ids:
                seen_ids.add(org_id)
                all_sites.append(site)

    if not all_sites:
        logger.info("No site LM instances to generate")
        return

    path = os.path.join(output_dir, "examples", "prequal_database_site_lm.fsh")
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        for site in all_sites:
            org = site.get("Organization", {})
            org_ident = org.get("Identification", {})
            org_id = org_ident.get("Id", "")
            org_name = org_ident.get("Name", "")
            org_addr = org.get("Address", {})
            instance_id = sanitize_code(org_id)

            site_country = org_addr.get("Country", "") or ""
            site_title = org_name or org_id
            site_suffix = f" ({site_country})" if site_country else ""
            f.write(f"\nInstance: PreQualSite{instance_id}\n")
            f.write("InstanceOf: PreQualSiteDetail\n")
            f.write("Usage: #example\n")
            f.write(f'Title: "PreQual Site: {fsh_escape(site_title)}"\n')
            f.write(f'Description: "WHO PreQual Manufacturing Site: {fsh_escape(site_title)}{fsh_escape(site_suffix)}"\n')
            f.write(f'* siteOrganizationId.system = "https://extranet.who.int/prequal/api"\n')
            f.write(f'* siteOrganizationId.value = "{fsh_escape(org_id)}"\n')
            if org_name:
                f.write(f'* siteOrganizationName = "{fsh_escape(org_name)}"\n')
            addr = org_addr.get("AddressLine1", "")
            if addr:
                f.write(f'* addressLine1 = "{fsh_escape(addr)}"\n')
            city = org_addr.get("City", "")
            if city:
                f.write(f'* city = "{fsh_escape(city)}"\n')
            state = org_addr.get("State", "")
            if state:
                f.write(f'* state = "{fsh_escape(state)}"\n')
            country = org_addr.get("Country", "")
            if country:
                f.write(f'* country = "{fsh_escape(country)}"\n')
            postal = org_addr.get("PostalCode", "")
            if postal:
                f.write(f'* postalCode = "{fsh_escape(postal)}"\n')
            status = site.get("Status", "")
            if status:
                f.write(f"* siteStatus = #{sanitize_code(status)}\n")
            activity = site.get("SiteActivity", "")
            if activity:
                f.write(f"* siteActivity = #{sanitize_code(activity)}\n")

    logger.info("Generated %d site LM instances", len(all_sites))


def generate_ingredient_lm_instances(products, output_dir):
    """Generate PreQualProductIngredient logical model instances FSH file.

    Args:
        products: List of normalized product field dicts.
        output_dir: Base output directory (e.g. input/fsh).
    """
    all_ingredients = []
    for p in products:
        sf_id = p.get("sf_product_id", "")
        per_product_idx = 0
        for ing in p.get("ingredients", []) or []:
            ing_ident = ing.get("Identification", {})
            ing_id = ing_ident.get("Id", "")
            # Some ingredients don't have IDs, use product+index as fallback
            per_product_idx += 1
            all_ingredients.append((sf_id, per_product_idx, ing_id, ing))

    if not all_ingredients:
        logger.info("No ingredient LM instances to generate")
        return

    path = os.path.join(output_dir, "examples", "prequal_database_ingredient_lm.fsh")
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        for sf_id, idx, ing_id, ing in all_ingredients:
            if ing_id:
                instance_id = sanitize_code(ing_id)
            else:
                instance_id = f"{sanitize_code(sf_id)}Ing{idx}"

            ing_type_val = ing.get("Type", "")
            ing_func = ing.get("Function", "")
            ing_title = ing_func or ing_type_val or f"Ingredient {idx}"
            ing_pct = ing.get("ProductComponentType", "")
            ing_desc_parts = [ing_title]
            if ing_pct:
                ing_desc_parts.append(f"({ing_pct})")
            ing_desc = " ".join(ing_desc_parts)
            f.write(f"\nInstance: PreQualIngredient{instance_id}\n")
            f.write("InstanceOf: PreQualProductIngredient\n")
            f.write("Usage: #example\n")
            f.write(f'Title: "PreQual Ingredient: {fsh_escape(ing_title)}"\n')
            f.write(f'Description: "WHO PreQual Product Ingredient: {fsh_escape(ing_desc)}"\n')
            if ing_id:
                f.write(f'* ingredientId.system = "https://extranet.who.int/prequal/api"\n')
                f.write(f'* ingredientId.value = "{fsh_escape(ing_id)}"\n')
            ing_type = ing.get("Type", "")
            if ing_type:
                f.write(f"* ingredientType = #{sanitize_code(ing_type)}\n")
            unit = ing.get("Unit", "")
            if unit:
                f.write(f'* unit = "{fsh_escape(unit)}"\n')
            product_ref = ing.get("Product", "")
            if product_ref:
                f.write(f'* product = "{fsh_escape(product_ref)}"\n')
            pct = ing.get("ProductComponentType", "")
            if pct:
                f.write(f"* productComponentType = #{sanitize_code(pct)}\n")
            func = ing.get("Function", "")
            if func:
                f.write(f'* function = "{fsh_escape(func)}"\n')

    logger.info("Generated %d ingredient LM instances", len(all_ingredients))


def generate_products_and_authorizations(products, output_dir):
    """Generate Product, ProductAuthorization, and LM instance FSH files.

    Also generates the product identifiers CodeSystem and ValueSet.

    Args:
        products: List of normalized product field dicts.
        output_dir: Base output directory (e.g. input/fsh).
    """
    examples_path = os.path.join(output_dir, "examples", "prequal_database_products.fsh")
    cs_path = os.path.join(output_dir, "codesystems", "prequal_database_products_identifiers.fsh")
    vs_path = os.path.join(output_dir, "valuesets", "prequal_database_products_identifiers.fsh")

    os.makedirs(os.path.dirname(examples_path), exist_ok=True)
    os.makedirs(os.path.dirname(cs_path), exist_ok=True)
    os.makedirs(os.path.dirname(vs_path), exist_ok=True)

    cs_entries = []
    generated_count = 0

    with open(examples_path, "w", encoding="utf-8") as f:
        for i, p in enumerate(products, 1):
            sf_id = p["sf_product_id"]
            sf_name = p["sf_product_name"]
            date = p["date_of_prequal"]
            vax = p.get("vaccine_abbreviated_name", "") or ""
            vax_type = sanitize_code(vax)[:24]
            commercial_name = p["vaccine_commercial_name"]
            presentation = p["presentation"]
            pres_code = sanitize_alpha(presentation)
            num_doses = p["num_doses"]
            manufacturer = p["applicant_name"]
            manufacturer_sf_id = p.get("applicant_id", "")
            holder = p["nra_name"]
            holder_sf_id = p.get("nra_id", "")

            # Skip products with missing essential data (e.g. withdrawn products)
            if not commercial_name and not manufacturer and not holder:
                logger.info("Skipping product %s (%s): missing essential data", sf_id, sf_name)
                continue

            safe_sf_id = sanitize_code(sf_id) if sf_id else md5hash(str(i))
            mfr_ref_id = sanitize_code(manufacturer_sf_id) if manufacturer_sf_id else md5hash(manufacturer)
            holder_ref_id = sanitize_code(holder_sf_id) if holder_sf_id else md5hash(holder)

            f.write(f"\n// Source Record Row //: {i}\n")
            f.write(f'//  Vaccine Product ID: ({sf_id})\n')
            f.write(f'//  Product Name: ({sf_name})\n')
            f.write(f'//  Date of Prequalification: ({date})\n')
            f.write(f'//  Vaccine Type: ({vax})\n')
            f.write(f'//  Commercial Name: ({commercial_name})\n')
            f.write(f'//  Presentation: ({presentation})\n')
            f.write(f'//  No. of doses: ({num_doses})\n')
            f.write(f'//  Manufacturer: ({manufacturer})\n')
            f.write(f'//  Responsible NRA: ({holder})\n')
            f.write(f"//\n\n")

            # LM Instance
            status = p.get("status", "") or "Prequalified"
            product_type = p.get("product_type", "")
            assessment = p.get("assessment_procedure", "")
            pharm_form = p.get("pharmaceutical_form", "")
            route = p.get("route_of_administration", "")
            preservative = p.get("preservative", "")
            preservative_conc = p.get("preservative_concentration", "")
            vial_monitor = p.get("vial_monitor", "") or ""
            multidose_policy = p.get("multidose_vial_policy", "") or ""
            presentation_other = p.get("presentation_other", "") or ""
            shelf_life = p.get("shelf_life", "") or ""
            temperature = p.get("temperature", "") or ""
            diluent_val = p.get("diluent", "") or ""
            last_pub_date = p.get("last_publishing_date", "") or ""
            pub_remarks = p.get("publishing_remarks", "") or ""
            nra_country = p.get("nra_country", "") or ""

            product_title = f"{commercial_name} - {vax}" if commercial_name and vax else commercial_name or sf_name
            product_desc = f"{commercial_name} ({vax}) by {manufacturer}" if commercial_name else sf_name
            f.write(f"Instance: PreQualDB{safe_sf_id}\n")
            f.write("InstanceOf: FinishedVaccineProducts\n")
            f.write("Usage: #example\n")
            f.write(f'Title: "PreQual Product: {fsh_escape(product_title)}"\n')
            f.write(f'Description: "{fsh_escape(product_desc)}"\n')
            if product_type:
                f.write(f"* productType = #{sanitize_code(product_type)}\n")
            if date:
                f.write(f"* dateOfPrequal = {date}\n")
            if assessment:
                f.write(f"* assessmentProcedure = #{sanitize_code(assessment)}\n")
            f.write(f"* status = #{sanitize_code(status)}\n")
            if pharm_form:
                f.write(f"* pharmaceuticalForm = #{sanitize_code(pharm_form)}\n")
            if pres_code:
                f.write(f'* presentation.coding.system = "https://extranet.who.int/prequal/vaccines/prequalified-vaccines"\n')
                f.write(f"* presentation.coding.code = #{pres_code}\n")
                f.write(f'* presentation.coding.display = "{fsh_escape(presentation)}"\n')
            if presentation_other:
                f.write(f'* presentationOther = "{fsh_escape(presentation_other)}"\n')
            if num_doses:
                f.write(f"* numDoses = {num_doses}\n")
            f.write(f'* productId.system = "https://extranet.who.int/prequal/api"\n')
            f.write(f'* productId.value = "{fsh_escape(sf_id)}"\n')
            f.write(f'* productName = "{fsh_escape(sf_name)}"\n')
            if p.get("vaccine_full_name"):
                f.write(f'* vaccineFullName = "{fsh_escape(p["vaccine_full_name"])}"\n')
            if p.get("vaccine_abbreviated_name"):
                f.write(f'* vaccineAbbreviatedName = "{fsh_escape(p["vaccine_abbreviated_name"])}"\n')
            f.write(f'* vaccineCommercialName = "{fsh_escape(commercial_name)}"\n')
            vax_type_id = p.get("vaccine_type_id", "")
            if vax_type_id:
                f.write(f'* vaccineTypeId.system = "https://extranet.who.int/prequal/api"\n')
                f.write(f'* vaccineTypeId.value = "{fsh_escape(vax_type_id)}"\n')
            if route:
                f.write(f"* routeOfAdministration = #{sanitize_code(route)}\n")
            if vial_monitor and vial_monitor.lower() != "none":
                f.write(f'* vialMonitor = "{fsh_escape(vial_monitor)}"\n')
            if multidose_policy and multidose_policy.lower() != "not applicable":
                f.write(f'* multidoseVialPolicy = "{fsh_escape(multidose_policy)}"\n')
            if manufacturer_sf_id:
                f.write(f'* applicantId.system = "https://extranet.who.int/prequal/api"\n')
                f.write(f'* applicantId.value = "{fsh_escape(manufacturer_sf_id)}"\n')
            f.write(f'* applicantName = "{fsh_escape(manufacturer)}"\n')
            if holder_sf_id:
                f.write(f'* nraId.system = "https://extranet.who.int/prequal/api"\n')
                f.write(f'* nraId.value = "{fsh_escape(holder_sf_id)}"\n')
            f.write(f'* nraName = "{fsh_escape(holder)}"\n')
            if nra_country:
                f.write(f'* nraCountry = "{fsh_escape(nra_country)}"\n')
            if shelf_life:
                f.write(f'* shelfLife = "{fsh_escape(shelf_life)}"\n')
            if temperature:
                f.write(f'* storageTemperature = "{fsh_escape(temperature)}"\n')
            if diluent_val and diluent_val.upper() != "N/A":
                f.write(f'* diluent = "{fsh_escape(diluent_val)}"\n')
            if last_pub_date:
                # Trim timestamp to date only if it has a T
                pub_date = last_pub_date.split("T")[0] if "T" in last_pub_date else last_pub_date
                f.write(f"* lastPublishingDate = {pub_date}\n")
            if pub_remarks:
                f.write(f'* publishingRemarks = "{fsh_escape(pub_remarks)}"\n')
            if preservative:
                f.write(f'* preservative = "{fsh_escape(preservative)}"\n')
            if preservative_conc:
                f.write(f'* preservativeConcentration = "{fsh_escape(preservative_conc)}"\n')
            f.write(f"* manufacturerReference = Reference(Manufacturer{mfr_ref_id})\n")
            f.write(f"* responsibleNRAReference = Reference(Holder{holder_ref_id}) // {fsh_escape(holder)}\n")

            # LM instance references (only when sub-object has a non-null ID)
            if manufacturer_sf_id:
                f.write(f"* manufacturerLM = Reference(PreQualManufacturer{mfr_ref_id})\n")
            if holder_sf_id:
                f.write(f"* nraLM = Reference(PreQualNRA{holder_ref_id})\n")
            if vax_type_id:
                vax_lm_ref_id = sanitize_code(vax_type_id)
                f.write(f"* vaccineLM = Reference(PreQualVaccine{vax_lm_ref_id})\n")

            # Bulk supplier LM reference
            bs_id = p.get("bulk_supplier_id", "")
            if bs_id:
                f.write(f"* bulkSupplierLM = Reference(PreQualBulkSupplier{sanitize_code(bs_id)})\n")

            # Packaging LM references
            for pkg in p.get("packaging", []) or []:
                pkg_id = pkg.get("Id", "")
                if pkg_id:
                    f.write(f"* packagingLM = Reference(PreQualPackaging{sanitize_code(pkg_id)})\n")

            # Document LM references
            for doc in p.get("documents", []) or []:
                doc_ident = doc.get("Identification", {})
                doc_id = doc_ident.get("Id", "")
                if doc_id:
                    f.write(f"* documentLM = Reference(PreQualDocument{sanitize_code(doc_id)})\n")

            # Site LM references
            for site in p.get("sites", []) or []:
                org = site.get("Organization", {})
                org_ident = org.get("Identification", {})
                org_id = org_ident.get("Id", "")
                if org_id:
                    f.write(f"* siteLM = Reference(PreQualSite{sanitize_code(org_id)})\n")

            # Ingredient LM references
            ing_idx = 0
            for ing in p.get("ingredients", []) or []:
                ing_ident = ing.get("Identification", {})
                ing_id = ing_ident.get("Id", "")
                ing_idx += 1
                if ing_id:
                    f.write(f"* ingredientLM = Reference(PreQualIngredient{sanitize_code(ing_id)})\n")
                else:
                    f.write(f"* ingredientLM = Reference(PreQualIngredient{sanitize_code(sf_id)}Ing{ing_idx})\n")

            f.write("\n")

            generated_count += 1
            cs_entries.append((safe_sf_id, sf_id, sf_name))

    # CodeSystem for product identifiers (additive — preserve existing codes)
    existing_ids = read_existing_codes(cs_path)
    new_id_codes = {}
    for entry_id, sf_id, sf_name in cs_entries:
        new_id_codes[entry_id] = f'* #{entry_id} "{fsh_escape(sf_name)} ({fsh_escape(sf_id)})"'

    merged_ids = dict(existing_ids)
    for code, line in new_id_codes.items():
        if code not in merged_ids:
            merged_ids[code] = line

    with open(cs_path, "w", encoding="utf-8") as f:
        f.write("\n")
        f.write("Alias: $PreQualProductIds = http://smart.who.int/pcmt-vaxprequal/CodeSystem/PreQualProductIds\n")
        f.write("CodeSystem: PreQualProductIds\n")
        f.write('Title : "WHO PreQualificaiton Vaccine Product Ids"\n')
        f.write('Description: "WHO PreQualificaiton Vaccine Product Ids"\n')
        f.write("* ^experimental = true\n")
        f.write("* ^caseSensitive = false\n")
        f.write('* ^name = "PreQualProductIds"\n')
        f.write("* ^status = #active\n\n\n")
        for code in sorted(merged_ids):
            f.write(f'{merged_ids[code]}\n')

    # ValueSet for product identifiers
    with open(vs_path, "w", encoding="utf-8") as f:
        f.write("\n")
        f.write("Alias: $PreQualProductIds = http://smart.who.int/pcmt-vaxprequal/CodeSystem/PreQualProductIds\n")
        f.write("ValueSet: PreQualProductIds\n")
        f.write('Title : "WHO PreQualificaiton Vaccine Product Ids"\n')
        f.write('Description: "WHO PreQualificaiton Vaccine Product Ids"\n')
        f.write("* include codes from system $PreQualProductIds\n")

    logger.info("Generated %d product instances", generated_count)


def load_csv_products(csv_path):
    """Load products from CSV file for concept map generation.

    Args:
        csv_path: Path to prequalified_vaccines.csv.

    Returns:
        List of dicts with CSV column values.
    """
    csv_products = []
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            if len(row) < 7:
                continue
            csv_products.append({
                "date": row[0].strip(),
                "vaccine_type": row[1].strip(),
                "commercial_name": row[2].strip(),
                "presentation": row[3].strip(),
                "num_doses": row[4].strip(),
                "manufacturer": row[5].strip(),
                "responsible_nra": row[6].strip(),
            })
    return csv_products


def compute_csv_md5(csv_row):
    """Compute MD5 hash matching presushi.sh for a CSV row.

    presushi.sh concatenates the fields with spaces after stripping quotes,
    then pipes through md5sum.  The AWK code is:
        MD5SRC=gensub(/"/, "", "g", $1) VAX COMMERCIALNAME PRESENTATION $5 MANUFACTURER HOLDER

    This concatenates with space separator in AWK (fields separated by OFS which is comma,
    but the AWK string concatenation with space is used).

    Args:
        csv_row: Dict with CSV column values.

    Returns:
        MD5 hash string.
    """
    md5_src = " ".join([
        csv_row["date"],
        csv_row["vaccine_type"],
        csv_row["commercial_name"],
        csv_row["presentation"],
        csv_row["num_doses"],
        csv_row["manufacturer"],
        csv_row["responsible_nra"],
    ])
    return md5hash(md5_src)


def generate_concept_map(api_products, csv_path, output_dir):
    """Generate ConceptMap from old CSV MD5-based IDs to authoritative vaccine product IDs.

    This attempts to match API products to CSV rows by comparing key fields
    (vaccine type, commercial name, manufacturer, presentation, doses).

    Args:
        api_products: List of normalized product field dicts from API.
        csv_path: Path to the CSV file.
        output_dir: Base output directory (e.g. input/fsh).
    """
    if not os.path.exists(csv_path):
        logger.warning("CSV file not found at %s, skipping concept map generation", csv_path)
        return

    csv_rows = load_csv_products(csv_path)

    # Build lookup from CSV rows by a matching key
    csv_by_key = {}
    for row in csv_rows:
        md5_id = compute_csv_md5(row)
        key = (
            row["commercial_name"].lower().strip(),
            row["manufacturer"].lower().strip(),
            row["num_doses"].strip(),
        )
        csv_by_key.setdefault(key, []).append((md5_id, row))

    mappings = []
    for p in api_products:
        commercial = (p.get("vaccine_commercial_name", "") or "").lower().strip()
        manufacturer = (p.get("applicant_name", "") or "").lower().strip()
        doses = (p.get("num_doses", "") or "").strip()

        key = (commercial, manufacturer, doses)
        if key in csv_by_key:
            for csv_md5, csv_row in csv_by_key[key]:
                sf_id = p.get("sf_product_id", "")
                sf_name = p.get("sf_product_name", "")
                if sf_id:
                    mappings.append((csv_md5, sf_id, sf_name, csv_row))

    cm_path = os.path.join(output_dir, "concept_maps", "prequal_csv_to_api.fsh")
    os.makedirs(os.path.dirname(cm_path), exist_ok=True)

    with open(cm_path, "w", encoding="utf-8") as f:
        f.write('Instance: PreQualCSVtoAPIConceptMap\n')
        f.write("InstanceOf: ConceptMap\n")
        f.write("Usage: #definition\n")
        f.write('* name = "PreQualCSVtoAPIConceptMap"\n')
        f.write('* title = "PreQual CSV to Vaccine Product ID Concept Map"\n')
        f.write('* description = "Maps old CSV export MD5-based identifiers to authoritative vaccine product IDs"\n')
        f.write("* status = #draft\n")
        f.write("* experimental = true\n")
        f.write('* sourceScopeUri = "http://smart.who.int/pcmt-vaxprequal/CodeSystem/PreQualProductIds"\n')
        f.write('* targetScopeUri = "https://extranet.who.int/prequal/api"\n')
        f.write("* group\n")
        f.write('  * source = "http://smart.who.int/pcmt-vaxprequal/CodeSystem/PreQualProductIds"\n')
        f.write('  * target = "https://extranet.who.int/prequal/api"\n')
        for csv_md5, sf_id, sf_name, csv_row in mappings:
            display = f'{csv_row["commercial_name"]} - {csv_row["manufacturer"]}'
            f.write(f'  * element\n')
            f.write(f'    * code = #{csv_md5}\n')
            f.write(f'    * display = "{fsh_escape(display)}"\n')
            f.write(f'    * target\n')
            f.write(f'      * code = #{sanitize_code(sf_id)}\n')
            f.write(f'      * display = "{fsh_escape(sf_name)}"\n')
            f.write(f'      * relationship = #equivalent\n')

    logger.info("Generated concept map with %d mappings", len(mappings))


def main():
    parser = argparse.ArgumentParser(
        description="Import WHO Vaccine PreQual data from the backend API"
    )
    parser.add_argument(
        "--output-dir",
        default="input/fsh",
        help="Output directory for generated FSH files (default: input/fsh)",
    )
    parser.add_argument(
        "--csv-file",
        default="data/prequalified_vaccines.csv",
        help="Path to CSV export for concept map generation (default: data/prequalified_vaccines.csv)",
    )
    parser.add_argument(
        "--json-file",
        default=None,
        help="Path to a local JSON file to use instead of the API (for testing/offline use)",
    )
    parser.add_argument(
        "--page-size",
        type=int,
        default=100,
        help="Number of records per API page (default: 100)",
    )
    args = parser.parse_args()

    # Load data from API or local file
    if args.json_file:
        raw_products = load_json_file(args.json_file)
    else:
        endpoint = os.environ.get("PREQUAL_API_ENDPOINT")
        username = os.environ.get("PREQUAL_API_USERNAME")
        password = os.environ.get("PREQUAL_API_PASSWORD")

        if not endpoint:
            logger.error("PREQUAL_API_ENDPOINT environment variable is required")
            sys.exit(1)
        if not username or not password:
            logger.error("PREQUAL_API_USERNAME and PREQUAL_API_PASSWORD environment variables are required")
            sys.exit(1)

        raw_products = download_all_pages(endpoint, username, password, args.page_size)

    if not raw_products:
        logger.error("No products found")
        sys.exit(1)

    # Extract normalized fields
    products = [extract_product_fields(p) for p in raw_products]

    # Generate all FSH outputs
    os.makedirs(args.output_dir, exist_ok=True)

    generate_metadata_codesystem(products, args.output_dir)
    generate_presentations_codesystem(products, args.output_dir)
    generate_vaccine_types_codesystem(products, args.output_dir)
    generate_manufacturers(products, args.output_dir)
    generate_holders(products, args.output_dir)
    generate_manufacturer_lm_instances(products, args.output_dir)
    generate_nra_lm_instances(products, args.output_dir)
    generate_vaccine_lm_instances(products, args.output_dir)
    generate_bulk_supplier_lm_instances(products, args.output_dir)
    generate_packaging_lm_instances(products, args.output_dir)
    generate_document_lm_instances(products, args.output_dir)
    generate_site_lm_instances(products, args.output_dir)
    generate_ingredient_lm_instances(products, args.output_dir)
    generate_products_and_authorizations(products, args.output_dir)

    # Generate concept map from old CSV IDs to authoritative vaccine product IDs
    generate_concept_map(products, args.csv_file, args.output_dir)

    logger.info("All FSH files generated successfully in %s", args.output_dir)


if __name__ == "__main__":
    main()
