Instance: CDHIv1toCDHIv2
InstanceOf: ConceptMap
Description: """
Mapping from the Classification of Digital Health Interventions v1 (CDHI v1, 2018)
to the Classification of Digital Interventions, Services and Applications in Health v2
(CDISAH v2, 2023).

Key structural changes reflected in this map:
- User group labels updated throughout (e.g. 'Clients' → 'Persons',
  'Health workers' → 'Healthcare providers', 'Health system managers' →
  'Health management and support personnel').
- Civil Registration and Vital Statistics (CRVS) consolidated: six v1 codes
  (3.4.1–3.4.6) merged into two v2 codes (3.4.1, 3.4.2).
- Health financing section restructured: v1 3.5.1 (insurance membership) and
  3.5.2 (billing) updated; v1 3.5.3–3.5.6 shifted by one (now 3.5.4–3.5.6 + new 3.5.3).
- Data services (group 4) substantially revised: 4.1.1 changed scope,
  4.3 expanded from 4 to 5 codes, 4.4 split from 1 to 3 codes, 4.5 is entirely new.
- New v2 categories with no v1 equivalent are listed as 'unmatched' targets.
"""
Usage: #definition
* name = "CDHIv1toCDHIv2"
* title = "Mapping from CDHI v1 to CDISAH v2"
* status = #draft
* experimental = true
* sourceCanonical = Canonical(CDHIv1)
* targetCanonical = Canonical(CDHIv2)
* group[+]
  * source = Canonical(CDHIv1)
  * target = Canonical(CDHIv2)

  // ── Group headers ─────────────────────────────────────────────────────────
  * insert ElementMapComment( 1.0, 1, equivalent, "Renamed: 'Clients' → 'Persons'")
  * insert ElementMapComment( 2.0, 2, equivalent, "Renamed: 'Health workers' → 'Healthcare providers'")
  * insert ElementMapComment( 3.0, 3, equivalent, "Renamed: 'Health system managers' → 'Health management and support personnel'")
  * insert ElementMap( 4.0, 4, equivalent)

  // ── Group 1: Persons (formerly Clients) ───────────────────────────────────
  * insert ElementMapComment( 1.1,   1.1,   equivalent, "Renamed: 'Targeted client communication' → 'Targeted communication to Persons'")
  * insert ElementMap( 1.1.1, 1.1.1, equivalent)
  * insert ElementMapComment( 1.1.2, 1.1.2, equivalent, "Renamed: 'client[s]' → 'person[s]'")
  * insert ElementMap( 1.1.3, 1.1.3, equivalent)
  * insert ElementMap( 1.1.4, 1.1.4, equivalent)
  * insert ElementMapComment( 1.2,   1.2,   equivalent, "Renamed: 'Untargeted client communication' → 'Untargeted communication to Persons'")
  * insert ElementMap( 1.2.1, 1.2.1, equivalent)
  * insert ElementMap( 1.2.2, 1.2.2, equivalent)
  * insert ElementMapComment( 1.3,   1.3,   equivalent, "Renamed: 'Client to client communication' → 'Person to Person communication'")
  * insert ElementMapComment( 1.3.1, 1.3.1, equivalent, "Renamed: 'Peer group for clients' → 'Peer group for individuals'")
  * insert ElementMapComment( 1.4,   1.4,   equivalent, "Renamed: 'Personal health tracking' [unchanged]")
  * insert ElementMapComment( 1.4.1, 1.4.1, equivalent, "Renamed: 'Access by client' → 'Access by the individual'")
  * insert ElementMapComment( 1.4.2, 1.4.2, equivalent, "Renamed: 'Self monitoring of health... by client' → '...by the individual'")
  * insert ElementMapComment( 1.4.3, 1.4.3, equivalent, "Renamed: 'Active data capture/documentation by client' → '...by an individual'")
  * insert ElementMapComment( 1.5,   1.5,   equivalent, "Renamed: 'Citizen-based reporting' → 'Person based reporting'")
  * insert ElementMapComment( 1.5.1, 1.5.1, equivalent, "Renamed: 'by clients' → 'by persons'")
  * insert ElementMap( 1.5.2, 1.5.2, equivalent)
  * insert ElementMapComment( 1.6,   1.6,   equivalent, "Renamed: 'On-demand information services to clients' → 'On demand communication with persons'")
  * insert ElementMapComment( 1.6.1, 1.6.1, equivalent, "Renamed: 'Client look-up of health information' → 'Look-up of information on health and health services by individuals'")
  * insert ElementMapComment( 1.7,   1.7,   equivalent, "Renamed: 'Client financial transactions' → 'Person-centred financial transactions'")
  * insert ElementMapComment( 1.7.1, 1.7.1, equivalent, "Renamed: 'by client[s]' → 'by individuals'")
  * insert ElementMapComment( 1.7.2, 1.7.2, equivalent, "Renamed: 'to client[s]' → 'to individuals'")
  * insert ElementMapComment( 1.7.3, 1.7.3, equivalent, "Renamed: 'to client[s]' → 'to individuals'")

  // ── Group 2: Healthcare providers (formerly Health workers) ───────────────
  * insert ElementMapComment( 2.1,   2.1,   equivalent, "Renamed: 'Client identification and registration' → 'Identification and registration of persons'")
  * insert ElementMapComment( 2.1.1, 2.1.1, equivalent, "Renamed: 'Verify client unique identity' → 'Verify a person's unique identity'")
  * insert ElementMapComment( 2.1.2, 2.1.2, equivalent, "Renamed: 'client' → 'person[s]'")
  * insert ElementMapComment( 2.2,   2.2,   equivalent, "Renamed: 'Client health records' → 'Person-centred health records'")
  * insert ElementMapComment( 2.2.1, 2.2.1, equivalent, "Renamed: 'clients' → 'person's'")
  * insert ElementMapComment( 2.2.2, 2.2.2, equivalent, "Renamed: 'client's' → 'person-centred'")
  * insert ElementMapComment( 2.2.3, 2.2.3, equivalent, "Renamed: 'client's' → 'person-centred'; now explicitly includes examples [notes; images; documents]")
  * insert ElementMap( 2.2.4, 2.2.4, equivalent)
  * insert ElementMapComment( 2.3,   2.3,   equivalent, "Renamed: 'Health worker decision support' → 'Healthcare provider decision support'")
  * insert ElementMap( 2.3.1, 2.3.1, equivalent)
  * insert ElementMap( 2.3.2, 2.3.2, equivalent)
  * insert ElementMapComment( 2.3.3, 2.3.3, equivalent, "Renamed: 'clients' → 'persons'")
  * insert ElementMap( 2.4,   2.4,   equivalent)
  * insert ElementMapComment( 2.4.1, 2.4.1, equivalent, "Renamed: 'client' → 'person'")
  * insert ElementMapComment( 2.4.2, 2.4.2, equivalent, "Renamed: 'client' → 'person's'")
  * insert ElementMapComment( 2.4.3, 2.4.3, equivalent, "Expanded: now explicitly lists examples [images; notes; videos]")
  * insert ElementMapComment( 2.4.4, 2.4.4, equivalent, "Renamed: 'health worker[s]' → 'healthcare providers'")
  * insert ElementMapComment( 2.5,   2.5,   equivalent, "Renamed: 'Health worker communication' → 'Healthcare provider communication'")
  * insert ElementMapComment( 2.5.1, 2.5.1, equivalent, "Renamed: 'health worker[s]' → 'healthcare provider'")
  * insert ElementMapComment( 2.5.2, 2.5.2, equivalent, "Renamed: 'health worker[s]' → 'healthcare provider[s]'")
  * insert ElementMapComment( 2.5.3, 2.5.3, equivalent, "Renamed: 'health worker[s]' → 'healthcare provider[s]'")
  * insert ElementMapComment( 2.5.4, 2.5.4, equivalent, "Renamed: 'health worker[s]' → 'healthcare provider[s]'")
  * insert ElementMapComment( 2.5.5, 2.5.5, equivalent, "Renamed: 'Peer group for health workers' → 'Peer group for healthcare providers'")
  * insert ElementMap( 2.6,   2.6,   equivalent)
  * insert ElementMap( 2.6.1, 2.6.1, equivalent)
  * insert ElementMap( 2.6.2, 2.6.2, equivalent)
  * insert ElementMapComment( 2.6.3, 2.6.3, wider, "Scope expanded: v2 explicitly includes social services; police; justice; economic support schemes")
  * insert ElementMapComment( 2.7,   2.7,   equivalent, "Renamed: 'Health worker activity planning' → 'Scheduling and activity planning for healthcare providers'")
  * insert ElementMapComment( 2.7.1, 2.7.1, equivalent, "Renamed: 'client[s]' → 'persons'")
  * insert ElementMapComment( 2.7.2, 2.7.2, equivalent, "Renamed: 'health worker's' → 'healthcare provider's'")
  * insert ElementMapComment( 2.8,   2.8,   equivalent, "Renamed: 'Health worker training' → 'Healthcare provider training'")
  * insert ElementMapComment( 2.8.1, 2.8.1, equivalent, "Renamed: 'health worker[s]' → 'healthcare provider[s]'")
  * insert ElementMapComment( 2.8.2, 2.8.2, equivalent, "Renamed: 'health worker[s]' → 'healthcare provider[s]'")
  * insert ElementMap( 2.9,   2.9,   equivalent)
  * insert ElementMap( 2.9.1, 2.9.1, equivalent)
  * insert ElementMapComment( 2.9.2, 2.9.2, equivalent, "Renamed: 'client's' → 'individual's'")
  * insert ElementMapComment( 2.9.3, 2.9.3, equivalent, "Renamed: 'adverse drug events' → 'adverse drug effects'")
  * insert ElementMapComment( 2.10,  2.10,  equivalent, "Renamed: 'health worker' → 'healthcare provider'")
  * insert ElementMapComment( 2.10.1, 2.10.1, equivalent, "Renamed: 'Transmit diagnostic result to health worker' → 'Transmit person's diagnostic result to healthcare provider'")
  * insert ElementMap( 2.10.2, 2.10.2, equivalent)
  * insert ElementMap( 2.10.3, 2.10.3, equivalent)
  * insert ElementMap( 2.10.4, 2.10.4, equivalent)

  // ── Group 3: Health management and support personnel ───────────────────────
  * insert ElementMap( 3.1,   3.1,   equivalent)
  * insert ElementMap( 3.1.1, 3.1.1, equivalent)
  * insert ElementMapComment( 3.1.2, 3.1.2, equivalent, "Renamed: 'health worker[s]' → 'healthcare provider[s]'")
  * insert ElementMapComment( 3.1.3, 3.1.3, equivalent, "Renamed: 'health worker[s]' → 'healthcare provider[s]'")
  * insert ElementMapComment( 3.1.4, 3.1.4, equivalent, "Renamed: 'health worker[s]' → 'healthcare provider[s]'")
  * insert ElementMap( 3.2,   3.2,   equivalent)
  * insert ElementMap( 3.2.1, 3.2.1, equivalent)
  * insert ElementMap( 3.2.2, 3.2.2, equivalent)
  * insert ElementMap( 3.2.3, 3.2.3, equivalent)
  * insert ElementMap( 3.2.4, 3.2.4, equivalent)
  * insert ElementMap( 3.2.5, 3.2.5, equivalent)
  * insert ElementMapComment( 3.2.6, 3.2.6, equivalent, "Renamed: 'by clients' → 'by persons'")
  * insert ElementMap( 3.3,   3.3,   equivalent)
  * insert ElementMap( 3.3.1, 3.3.1, equivalent)

  // CRVS consolidation: v1 had 6 separate codes; v2 merges into 2
  * insert ElementMapComment( 3.4,   3.4,   equivalent, "Renamed: 'Civil Registration and Vital Statistics' [same concept]")
  * insert ElementMapComment( 3.4.1, 3.4.1, wider, "Consolidated: v1 'Notify birth event' merged with v1 3.4.2 [register] and 3.4.3 [certify] into v2 3.4.1 'Notify; register and certify birth event'")
  * insert ElementMapComment( 3.4.2, 3.4.1, wider, "Consolidated: v1 'Register birth event' merged into v2 3.4.1 'Notify; register and certify birth event'")
  * insert ElementMapComment( 3.4.3, 3.4.1, wider, "Consolidated: v1 'Certify birth event' merged into v2 3.4.1 'Notify; register and certify birth event'")
  * insert ElementMapComment( 3.4.4, 3.4.2, wider, "Consolidated: v1 'Notify death event' merged with v1 3.4.5 [register] and 3.4.6 [certify] into v2 3.4.2 'Notify; register and certify death event'")
  * insert ElementMapComment( 3.4.5, 3.4.2, wider, "Consolidated: v1 'Register death event' merged into v2 3.4.2 'Notify; register and certify death event'")
  * insert ElementMapComment( 3.4.6, 3.4.2, wider, "Consolidated: v1 'Certify death event' merged into v2 3.4.2 'Notify; register and certify death event'")

  // Health financing: some reordering and new codes
  * insert ElementMapComment( 3.5,   3.5,   equivalent, "Renamed: 'Health financing' → 'Health system financial management'")
  * insert ElementMapComment( 3.5.1, 3.5.1, equivalent, "Updated wording: now covers all coverage schemes; not only insurance")
  * insert ElementMapComment( 3.5.2, 3.5.2, equivalent, "Updated wording: 'Track insurance billing and claims submission' → 'Track and manage insurance billing and claims processes'")
  * insert ElementMapComment( 3.5.4, 3.5.4, equivalent, "Renumbered from v1 3.5.4; health worker → healthcare provider")
  * insert ElementMapComment( 3.5.5, 3.5.5, equivalent, "Renumbered from v1 3.5.5; health worker → healthcare provider")
  * insert ElementMapComment( 3.5.6, 3.5.6, equivalent, "Renumbered from v1 3.5.6; reworded to include revenue and expenditures")

  * insert ElementMap( 3.6,   3.6,   equivalent)
  * insert ElementMapComment( 3.6.1, 3.6.1, equivalent, "Expanded: 'Monitor status' → 'Monitor status and maintenance'")
  * insert ElementMap( 3.6.2, 3.6.2, equivalent)
  * insert ElementMap( 3.7,   3.7,   equivalent)
  * insert ElementMap( 3.7.1, 3.7.1, equivalent)
  * insert ElementMap( 3.7.2, 3.7.2, equivalent)

  // ── Group 4: Data services ─────────────────────────────────────────────────
  * insert ElementMapComment( 4.1,   4.1,   equivalent, "Renamed: 'Data collection; management; and use' → 'Data Management'")
  * insert ElementMapComment( 4.1.1, 4.1.1, inexact, "v1: 'Non-routine data collection and management'; v2: 'Form creation for data acquisition' — overlapping but distinct scope")
  * insert ElementMap( 4.1.2, 4.1.2, equivalent)
  * insert ElementMapComment( 4.1.3, 4.1.3, equivalent, "Renamed: 'visualisation' → 'visualizations'")
  * insert ElementMapComment( 4.1.4, 4.1.4, equivalent, "Scope extended to explicitly include AI and machine learning")
  * insert ElementMap( 4.2,   4.2,   equivalent)
  * insert ElementMap( 4.2.1, 4.2.1, equivalent)
  * insert ElementMap( 4.2.2, 4.2.2, equivalent)
  * insert ElementMap( 4.2.3, 4.2.3, equivalent)
  * insert ElementMapComment( 4.3,   4.3,   equivalent, "Renamed: 'Location mapping' → 'Geo spatial information management'; expanded from 4 to 5 sub-codes")
  * insert ElementMapComment( 4.3.1, 4.3.1, equivalent, "Expanded: 'Map location of health facilities/structures' → '...and households'")
  * insert ElementMapComment( 4.3.2, 4.3.2, equivalent, "Renamed: 'Map location of health events' → 'Map location of health event'")
  * insert ElementMapComment( 4.3.3, 4.3.3, equivalent, "Renamed: 'clients and households' → 'persons and settlements'")
  * insert ElementMapComment( 4.3.4, 4.3.4, equivalent, "Renamed: 'health worker' → 'healthcare provider[s]'")
  * insert ElementMapComment( 4.4,   4.4,   equivalent, "Renamed: 'Data exchange and interoperability'; split from 1 leaf code into 3 in v2")
  * insert ElementMapComment( 4.4.1, 4.4.1, wider, "v1 'Data exchange across systems' is broader; v2 4.4.1 covers only point-to-point integration. See also v2 4.4.2 [standards-compliant] and 4.4.3 [message routing].")
  * insert ElementMapComment( 4.4.1, 4.4.2, wider, "v2 4.4.2 'Standards-compliant interoperability' partially covers the broader v1 4.4.1 concept")
  * insert ElementMapComment( 4.4.1, 4.4.3, wider, "v2 4.4.3 'Message routing' partially covers the broader v1 4.4.1 concept")