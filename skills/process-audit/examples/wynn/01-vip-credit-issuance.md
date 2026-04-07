# Process Audit Intake: VIP Patron Casino Credit Issuance

---

## Section 1 — Process Identity

- **Process name:** VIP Patron Casino Credit Issuance
- **Process owner:** Director of Casino Credit
- **Frequency:** Per-event (triggered by new patron application or existing patron requesting a credit line increase)
- **Volume:** Approximately 80–120 new credit applications per month across Wynn Las Vegas and Encore; 30–50 credit line increase requests per month
- **How long in current form:** Core process unchanged since ~2018; a new credit evaluation platform was partially integrated in 2022 but full adoption stalled
- **Why being audited now:** Two recent incidents — a high-value patron defaulted on a $1.2M marker after credit was extended without completing the full verification sequence; separately, a VIP host bypassed the standard review process citing "relationship exception," which was not a documented policy

---

## Section 2 — Step-by-Step Process Map

| # | Step | Owner | System/Tool | Approx. Time | Manual/Auto | Decision Point? |
|---|---|---|---|---|---|---|
| 1 | Patron submits credit application (in-person at cage or via host) | VIP Host or Cage Agent | Paper form + CMS (Casino Management System) | 20 min | Manual | — |
| 2 | Cage agent enters application data into credit system | Cage Agent | Aristocrat CMS / internal credit module | 15 min | Manual | — |
| 3 | Credit team pulls patron's Central Credit report | Credit Analyst | Central Credit (industry bureau) | 10 min | Semi-auto | If no file exists, escalate to Director |
| 4 | Credit analyst reviews gaming history at Wynn properties | Credit Analyst | CMS historical data | 30 min | Manual | If ADT < $25K, lower tier process applies |
| 5 | Credit analyst reviews gaming history at competitor properties | Credit Analyst | Central Credit + direct calls to other properties | 1–3 days | Manual | If unverifiable, flag for Director review |
| 6 | Financial verification (bank statements, brokerage statements requested) | VIP Host | Email / fax / in-person | 2–10 days | Manual | If patron declines to provide, host may request Director exception |
| 7 | Credit recommendation prepared | Credit Analyst | Word document / email | 1 hour | Manual | — |
| 8 | Director of Casino Credit reviews and approves or modifies | Director, Casino Credit | Email + phone | Same day to 3 days | Manual | Amounts over $500K require VP Casino Operations co-sign |
| 9 | Approved credit entered into CMS | Cage Supervisor | Aristocrat CMS | 10 min | Manual | — |
| 10 | Patron notified; marker book activated | VIP Host | Phone / in-person | Same day | Manual | — |
| 11 | Marker issuance begins at table or cage | Cage Agent / Pit Supervisor | CMS + physical marker document | Per visit | Manual | Pit supervisor approves markers over $50K per sitting |

**Exception handling at each step:**
- Step 3: If Central Credit has no file, analyst must call 3 reference properties personally. No documented SLA for this.
- Step 6: Financial verification is technically required but hosts can request a "relationship exception" from the Director. This exception is not logged in the CMS — it exists only in email.
- Step 8: If Director is traveling or unavailable, requests queue with no backup approver defined.
- Step 11: Pit supervisors can approve over-limit markers with a phone call to the cage supervisor — this approval is logged in CMS but not always matched back to the original credit file.

---

## Section 3 — Known Pain Points

- **The relationship exception problem:** VIP hosts have significant informal authority to push credit through faster for high-value patrons. This creates two de facto tracks — one with full verification and one without — but only one is documented. Compliance team has flagged this twice.
- **Financial verification turnaround:** Requesting bank statements from international patrons (particularly from Asia-Pacific) routinely takes 7–14 days. Hosts complain that competitors extend credit faster, and they lose bookings while waiting.
- **No single source of truth:** A patron's credit history across Wynn Las Vegas, Encore, Wynn Macau, and Encore Boston Harbor is not consolidated. Each property runs its own credit check. It is possible (and has happened) for a patron to have a delinquent marker at one property and receive new credit at another.
- **Director as single approver:** All final approvals route to one Director. When that person travels (frequently, given the role), approvals queue for days. There is no defined backup authority.
- **CMS data entry errors:** Manual re-entry of application data from paper forms into CMS produces regular errors. The 2022 integration project was supposed to allow digital form submission directly into CMS but was never fully deployed.

---

## Section 4 — Performance Baselines

- **Average cycle time (application to approved credit):** 4–7 business days for domestic patrons; 10–18 business days for international
- **Target/SLA:** No formal SLA exists. Hosts informally expect 48–72 hours for established patrons.
- **Error rate:** Approximately 12% of new applications require at least one re-entry correction after data is in CMS
- **Default rate:** Approximately 2.1% of outstanding markers annually (industry average is ~1.4%)
- **Exception rate:** Estimated 20–25% of high-value approvals ($250K+) include some form of undocumented exception

---

## Section 5 — Systems & Integrations

| System | Role in Process | Known Limitations / Workarounds |
|---|---|---|
| Aristocrat CMS | Core patron and credit record system | Cannot accept digital form input; all data entered manually by cage staff. Credit module is underutilized — most analysts work from exported spreadsheets. |
| Central Credit | Industry credit bureau for gaming patron history | Only covers properties that subscribe and report. Many international properties do not participate. Analysts fill gaps with phone calls. |
| Internal credit module (2022 partial deployment) | Was intended to digitize application intake and route approvals | Only deployed at one of four cashier stations at Wynn Las Vegas. No deployment at Encore. Adoption stalled after the project sponsor left. |
| Email | Carries financial documents from patrons, exception approvals, inter-property credit checks | No standardized folder structure. Financial documents sent by patrons sit in individual host inboxes, not a shared system. |
| Excel | Used by credit analysts to track in-progress applications | Each analyst maintains their own spreadsheet. No shared pipeline view. |

---

## Section 6 — Compliance & Control Context

- **Regulatory requirements:** Nevada Gaming Control Board Regulation 6 governs credit issuance. Wynn is required to maintain accurate records of all markers issued and collected. IRS Form W-2G and CTR (Currency Transaction Report) requirements apply to certain payout scenarios.
- **Anti-money laundering (AML):** Casino credit is a high-risk area for money laundering. BSA/AML program requires patron due diligence for credit above certain thresholds. The relationship exception pathway creates a gap in this due diligence documentation.
- **Existing audit trails:** Marker issuance is logged in CMS. Credit approvals are logged via email — not in a system of record.
- **Prior compliance reviews:** Internal audit flagged the "relationship exception" practice in 2023. Recommendation was to formalize the exception policy. As of this audit, that recommendation has not been fully implemented.
- **Segregation of duties:** VIP hosts who initiate the credit request also communicate the outcome to patrons and sometimes enter supporting data. The host has economic incentive (commission) tied to patron gaming activity, creating a conflict of interest in the verification process.

---

## Section 7 — Recent Incidents or Near-Misses

**Incident 1 — $1.2M default (Q3 2024)**
A patron was extended $1.2M in credit after Step 6 (financial verification) was bypassed under a relationship exception. The patron's financial documents were never reviewed. The patron defaulted 90 days after the credit was issued. Investigation revealed the patron had a delinquent marker at Wynn Macau that was not visible to the Las Vegas credit team. Resolution: marker placed in collections; partial recovery expected. Root cause not structurally addressed.

**Incident 2 — Cross-property credit duplication (Q1 2025)**
A patron with an outstanding $400K marker at Encore Boston Harbor (in default, in collections) was issued $350K in new credit at Wynn Las Vegas. The Las Vegas credit team had no visibility into the Boston Harbor delinquency because the systems are not integrated. Discovered during a quarterly marker reconciliation. Credit was frozen retroactively. No loss incurred, but the gap was identified.

**Near-miss — AML documentation gap (Q4 2024)**
During a routine NGCB compliance review, an examiner found three high-value credit files where financial verification documents were held in a host's personal email inbox and had not been uploaded to any system of record. The patron files were technically complete but could not be produced within the required timeframe. The examiner issued a finding requiring corrective action within 60 days.

---

## Section 8 — Audit Scope & Constraints

- **Out of scope:** The marker collection and default recovery process (separate audit in planning)
- **Appetite for change:** Open to redesign, including system changes. The 2022 integration project is considered incomplete, not abandoned — there is appetite to finish it.
- **Known constraints:** Any changes to the CMS require a change order with Aristocrat. Lead times are 6–12 months for significant module changes. Lightweight workarounds (web forms, middleware) are preferred in the near term.
- **Regulatory constraint:** Any new approval workflow must be documentable and producible for NGCB review on short notice. Informal approval paths (phone calls, verbal approvals) are specifically problematic.
