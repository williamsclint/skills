# Process Audit Intake: BSA/AML Suspicious Activity Report & Currency Transaction Report Filing

---

## Section 1 — Process Identity

- **Process name:** BSA/AML SAR and CTR Identification, Review, and Filing Process
- **Process owner:** BSA/AML Compliance Officer (reports to Chief Compliance Officer)
- **Frequency:** CTRs are required for any cash transaction exceeding $10,000 in a gaming day — Wynn Las Vegas files approximately 900–1,200 CTRs per month. SARs are discretionary filings triggered by detected suspicious activity — Wynn files approximately 15–35 SARs per month. Both have mandatory FinCEN filing deadlines (CTR: 15 days; SAR: 30 days, or 60 days if no subject identified).
- **How long in current form:** Core process governed by the Bank Secrecy Act and FinCEN requirements; fundamentally unchanged since Wynn's BSA program was formalized. Current software platform (Intapp AML / internal system) implemented in 2020. Process updated in 2022 following an industry-wide review triggered by regulatory scrutiny of Las Vegas casinos.
- **Why being audited now:** FinCEN conducted an examination of Wynn's BSA program in late 2024. Preliminary feedback cited three areas of concern: (1) inconsistent quality of SAR narratives across filing staff; (2) CTR filing deadlines being missed at a rate above FinCEN's informal tolerance threshold; (3) gaps in documentation of the "no file" decision (cases reviewed but determined not to require a SAR filing). Full examination findings are expected in Q2 2025.

---

## Section 2 — Step-by-Step Process Map

**CTR Process:**

| # | Step | Owner | System/Tool | Approx. Time | Manual/Auto | Decision Point? |
|---|---|---|---|---|---|---|
| 1 | Cash transaction recorded at cage or pit | Cage Agent / Pit Supervisor | Aristocrat CMS | Real-time | Semi-auto | — |
| 2 | CMS generates alert when patron's cash-in or cash-out crosses $10,000 threshold in a gaming day | CMS automated alert | Aristocrat CMS | Automatic | Auto | — |
| 3 | Cage supervisor reviews alert; confirms transaction qualifies | Cage Supervisor | CMS | 5–10 min | Manual | Determines if aggregation rules apply; checks for exemptions |
| 4 | Patron identification verified or obtained | Cage Agent | Physical ID; CMS patron record | 5–15 min | Manual | If patron refuses ID, specific protocols apply |
| 5 | CTR data package assembled (patron ID, transaction details) | BSA Coordinator | CMS export + manual data entry into CTR filing system | 20–45 min | Manual | — |
| 6 | CTR reviewed for accuracy | BSA Compliance Officer or Senior Coordinator | CTR filing system | 10–20 min | Manual | — |
| 7 | CTR filed with FinCEN via BSA E-Filing | BSA Coordinator | FinCEN BSA E-Filing portal | 10 min | Manual | Must be filed within 15 calendar days of triggering transaction |
| 8 | Filing confirmation retained in compliance system | BSA Coordinator | Internal compliance system | 5 min | Manual | — |

**SAR Process:**

| # | Step | Owner | System/Tool | Approx. Time | Manual/Auto | Decision Point? |
|---|---|---|---|---|---|---|
| 1 | Suspicious activity identified | Various (cage, pit, surveillance, host, compliance) | No single system — reported via email, verbal, or compliance hotline | Variable | Manual | — |
| 2 | Initial report submitted to BSA Compliance team | Reporting employee | Email or paper form | Same day | Manual | — |
| 3 | BSA Coordinator logs report and opens case | BSA Coordinator | Internal compliance case management system | 1–2 hours | Manual | — |
| 4 | Case reviewed; additional transaction data gathered from CMS | BSA Analyst | CMS + compliance system | 1–3 days | Manual | — |
| 5 | Analyst determines whether SAR is warranted | BSA Analyst | Internal review | 1–3 days | Manual | If no SAR: document "no file" decision and rationale. If SAR: proceed. |
| 6 | SAR narrative drafted | BSA Analyst | Word document; copied into filing system | 2–4 hours | Manual | — |
| 7 | SAR reviewed and approved | BSA Compliance Officer | Internal compliance system | 1–2 days | Manual | High-value or complex SARs reviewed by CCO |
| 8 | SAR filed with FinCEN | BSA Coordinator | FinCEN BSA E-Filing portal | 30 min | Manual | Must file within 30 days of detection; 60 days if no subject ID |
| 9 | Filed SAR and documentation retained | BSA Coordinator | Compliance system | Same day | Manual | 5-year retention requirement |
| 10 | Ongoing monitoring: continuing SAR filed if activity persists | BSA Analyst | Manual calendar reminder | 90-day intervals | Manual | — |

**Exception handling at each step:**
- CTR Step 3: Aggregation across multiple transactions in a gaming day requires manual judgment. The CMS alerts on single transactions but does not automatically aggregate across cage, pit, and slots for the same patron on the same day. Cross-department aggregation is done manually by the cage supervisor.
- CTR Step 4: International patrons sometimes present foreign identification. Acceptability of specific foreign ID types is inconsistently applied across shifts. A reference list exists but is not consistently consulted.
- SAR Step 1: Suspicious activity is identified by multiple departments using different channels. Pit supervisors call compliance directly; hosts sometimes handle it internally first; surveillance sends written reports; cage agents use a paper form. There is no single intake channel.
- SAR Step 5: The "no file" decision and its rationale are supposed to be documented in the case management system. In practice, documentation quality is inconsistent — some cases have detailed rationale, others have a single line.
- SAR Step 10: Continuing SAR monitoring is tracked via individual analyst calendar reminders. There is no automated 90-day review trigger in the case management system.

---

## Section 3 — Known Pain Points

- **SAR narrative quality variance:** There are four analysts who write SAR narratives. Quality varies significantly. Two analysts write detailed, well-structured narratives. Two write minimal narratives that technically describe the activity but lack the "why suspicious" reasoning FinCEN looks for. There is no narrative quality standard or peer review process.
- **CTR deadline misses:** The 15-day deadline is missed on approximately 4–6% of CTRs. Root causes vary: CMS alert not acted on promptly; patron ID not obtained at time of transaction (patron left); coordinator workload backlog; alerts generated over weekends when the BSA team is reduced to one person.
- **Cross-department aggregation gap:** The CMS does not automatically aggregate cash transactions across casino departments (cage, pit, slots) for the same patron in the same gaming day. This is a structural gap — a patron could transact $7,000 at the cage and $5,000 at a pit buy-in, triggering a $12,000 aggregated total that requires a CTR, but the cage supervisor only sees $7,000 and does not file. This is a known FinCEN vulnerability.
- **The "no file" documentation gap:** FinCEN increasingly scrutinizes not just what was filed, but what was reviewed and not filed. Cases where the compliance team considered a SAR and decided against it should be documented as thoroughly as filed SARs. Current documentation is inconsistent and would not withstand a targeted examination.
- **Weekend staffing:** The BSA team operates with a single coordinator on weekends. CTR alerts generated Friday through Sunday are often not processed until Monday, increasing the risk of deadline misses for transactions occurring late in the week.

---

## Section 4 — Performance Baselines

- **CTR volume:** 900–1,200 per month
- **CTR on-time filing rate:** ~94–96% (FinCEN informal tolerance is typically >99%)
- **SAR volume:** 15–35 per month
- **SAR on-time filing rate:** ~98% (strong; deadline misses are rare for SARs due to longer window)
- **"No file" documentation completeness:** Estimated 60–70% of cases have adequate rationale documentation (internal estimate; not formally measured)
- **Average SAR investigation-to-filing time:** 12–18 days (well within the 30-day window but with little buffer for complex cases)
- **BSA team size:** 1 BSA Compliance Officer, 4 analysts, 2 coordinators (1 FTE dedicated to weekend coverage but shared with other compliance functions)

---

## Section 5 — Systems & Integrations

| System | Role in Process | Known Limitations / Workarounds |
|---|---|---|
| Aristocrat CMS | Source of transaction data for CTR triggers and SAR investigation | Alerts on individual transactions; does not auto-aggregate across departments for the same patron on the same gaming day. Cross-department aggregation is manual. |
| Internal compliance case management system | SAR case tracking, "no file" documentation, filing history | Basic workflow capability. No automated 90-day continuing SAR reminder. Narrative quality cannot be benchmarked or compared across analysts. |
| FinCEN BSA E-Filing portal | Official filing system for CTRs and SARs | External government system. No API — all filings are manual data entry into the portal. Confirmation numbers returned manually and filed by coordinator. |
| Microsoft Word | SAR narrative drafting | Analysts draft narratives in Word and paste into the filing system. No templates. No version control. No quality checklist. |
| Email | Suspicious activity intake from multiple departments | No structured intake form. Reports arrive in various formats. Some are forwarded chains. BSA Coordinator must parse and log manually. |
| Excel / Outlook calendar | Continuing SAR monitoring | Individual analyst calendars. No centralized visibility. If analyst leaves, monitoring reminders leave with them. |

---

## Section 6 — Compliance & Control Context

- **Regulatory requirements:** Bank Secrecy Act (31 U.S.C. § 5311 et seq.) and FinCEN regulations (31 CFR Chapter X) require casinos with gaming revenue above $1M to file CTRs and SARs. Violations can result in civil money penalties (CMPs) — FinCEN has issued penalties to casinos exceeding $100M for BSA program failures.
- **FinCEN examination in progress:** Preliminary findings already received (see Section 1). Final report expected Q2 2025. Three cited areas are the direct trigger for this audit.
- **SAR confidentiality:** SARs are strictly confidential. The subject of a SAR cannot be notified that one has been filed. This constraint affects how the team communicates internally about cases.
- **Retention requirements:** CTRs and SARs must be retained for 5 years. Current retention is in the internal compliance system plus physical filing for selected cases.
- **Tipping off prohibition:** Staff who are aware of a SAR filing are prohibited from tipping off the subject. Training on this prohibition is part of annual BSA training but its coverage in operational departments (pit, cage) is inconsistent.
- **Prior regulatory action:** No prior FinCEN enforcement action against Wynn Las Vegas. The 2024 examination is the first to raise these specific concerns.

---

## Section 7 — Recent Incidents or Near-Misses

**Incident 1 — Cross-department aggregation miss (Q3 2024)**
A patron conducted a $6,500 cash buy-in at a baccarat table and a $5,200 cash transaction at the cage on the same gaming day. Aggregated total: $11,700. A CTR was required. The cage supervisor only saw the $5,200 transaction and did not file. The gap was identified during a monthly QA review by the BSA Compliance Officer. A late CTR was filed. FinCEN was notified of the late filing per policy. This is a direct example of the cross-department aggregation gap.

**Incident 2 — SAR narrative flagged during examination (Q4 2024)**
During the FinCEN examination, an examiner reviewed 12 SAR filings and identified three with "inadequate narrative descriptions." The examiner's specific criticism: the narratives described what happened but did not explain why the activity was suspicious relative to the patron's known profile or expected activity pattern. FinCEN's guidance on SAR narratives explicitly requires this context. This is the primary driver of the narrative quality finding.

**Near-miss — Continuing SAR missed (Q2 2024)**
A patron with an active SAR (filed Q4 2023) was due for a 90-day continuing SAR review in Q1 2024. The review was not conducted because the analyst who had set the calendar reminder left the company. The patron continued transacting. The gap was discovered when the patron was flagged by a different analyst for separate activity in Q2 2024. A 180-day gap in monitoring was retroactively documented. No regulatory report was required, but the incident was included in the internal BSA program review.

---

## Section 8 — Audit Scope & Constraints

- **Out of scope:** The broader AML customer due diligence (CDD) program for VIP patrons is a separate review. Slot machine jackpot tax reporting (W-2G) is not in scope.
- **Regulatory urgency:** This audit has direct regulatory stakes — the FinCEN examination findings are expected in Q2 2025. Recommendations that can be implemented before the final report or before any follow-up examination are prioritized.
- **Appetite for change:** High, given regulatory exposure. BSA Compliance Officer has executive support for process changes and is open to technology investment.
- **Operational constraint:** SAR confidentiality rules limit how broadly process changes can be communicated. Training on new procedures must be scoped carefully to avoid inadvertently disclosing SAR-related information to unauthorized staff.
- **Staffing constraint:** Hiring additional BSA analysts is under discussion but subject to budget approval. Near-term recommendations should be achievable with current headcount.
