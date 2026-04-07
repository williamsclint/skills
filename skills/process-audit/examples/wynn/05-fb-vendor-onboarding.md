# Process Audit Intake: Fine Dining F&B Vendor Onboarding

---

## Section 1 — Process Identity

- **Process name:** Fine Dining Food & Beverage Vendor Onboarding
- **Process owner:** Director of Food & Beverage Procurement
- **Frequency:** Approximately 8–14 new vendor onboardings per quarter across Wynn Las Vegas and Encore properties. Volume spikes when a new restaurant concept launches or an existing restaurant undergoes a menu overhaul. Seasonal menu transitions (spring/fall) also drive onboarding activity.
- **How long in current form:** Current process has been in place since 2019 when Wynn centralized procurement under a unified F&B Procurement team. Prior to 2019, individual restaurant chefs managed their own vendor relationships. The centralization improved contract discipline but added process steps that chefs find slow and bureaucratic.
- **Why being audited now:** Three restaurant openings in 2024 (including the relaunch of a flagship fine dining concept) experienced significant opening-week product gaps — multiple signature menu items could not be served because specialty ingredient vendors were not fully onboarded when the restaurants opened. One vendor (a small-batch caviar supplier) was still pending insurance documentation 11 days after the restaurant opened, requiring a menu substitution. The F&B team and the Procurement team have different explanations for what went wrong.

---

## Section 2 — Step-by-Step Process Map

| # | Step | Owner | System/Tool | Approx. Time | Manual/Auto | Decision Point? |
|---|---|---|---|---|---|---|
| 1 | Chef or restaurant director identifies need for new vendor | Executive Chef / Restaurant Director | — | Variable | Manual | — |
| 2 | Chef submits vendor request form to Procurement | Executive Chef | Email with attached form (PDF) | 1–3 days | Manual | — |
| 3 | Procurement Coordinator confirms request received and opens vendor file | Procurement Coordinator | SharePoint + Excel tracker | 1 day | Manual | — |
| 4 | Vendor invited to submit qualification documents | Procurement Coordinator | Email | 1–2 days to send; 3–14 days for vendor to respond | Manual | If vendor does not respond within 7 days, Coordinator follows up manually |
| 5 | Vendor submits required documents | Vendor | Email | 3–14 days | External | — |
| 6 | Document completeness review | Procurement Coordinator | Manual checklist (Excel) | 1–2 days | Manual | Incomplete submission returned to vendor — process resets |
| 7 | Legal review (contract terms, liability, indemnification) | Legal / outside counsel for complex agreements | Email + Word documents | 3–10 business days | Manual | Standard vendors use Wynn's template (faster); non-standard terms require negotiation |
| 8 | Insurance verification | Risk Management | Certificates of Insurance reviewed manually | 1–3 days | Manual | If COI doesn't meet Wynn's requirements, vendor must update policy |
| 9 | Food safety certification review (ServSafe, USDA, health dept certs) | Food Safety / Quality Assurance | Manual document review | 1–2 days | Manual | Non-compliant vendors rejected or placed on corrective action |
| 10 | Financial / credit check (for vendors with payment terms) | Finance | Third-party credit report | 2–3 days | Semi-auto | Vendors requiring net-30+ terms require Controller approval |
| 11 | Vendor setup in ERP (Oracle Hospitality / Purchasing system) | Finance / AP | Oracle | 1–2 days | Manual | Requires completed vendor master form; errors in setup cause payment delays later |
| 12 | Vendor added to approved vendor list | Procurement Manager | Excel master list | 1 day | Manual | — |
| 13 | Chef notified; first purchase order can be placed | Procurement Coordinator | Email | Same day | Manual | — |

**Exception handling at each step:**
- Step 2: The vendor request form is a PDF. Chefs frequently email the request without attaching the form, or attach the form with incomplete information. No digital form with required fields.
- Step 4–5: Small artisan vendors (common in fine dining — small farms, specialty producers, boutique importers) frequently lack standard corporate documentation. They may not carry the required liability insurance limits or may not have formal food safety certifications. These cases require manual negotiation and exception approvals.
- Step 7: Legal uses Wynn's standard template for most vendors. When a vendor pushes back on terms, the negotiation loop between Legal and the vendor can extend 2–4 weeks. There is no escalation path or timeline commitment from Legal.
- Step 8: Risk Management has a minimum COI requirement ($2M general liability). Several specialty small vendors cannot meet this threshold. The process for approving exceptions (requiring a risk waiver from the CFO) is not documented and has been handled inconsistently.
- Step 11: Oracle vendor setup requires a completed vendor master form. The form is separate from all prior documentation and must be filled out by the vendor. It is often sent late in the process, adding 2–3 days at the end when the chef is expecting the vendor to be ready.

---

## Section 3 — Known Pain Points

- **The speed vs. standards tension:** Wynn's fine dining chefs work with highly specialized, often small or boutique vendors — farms, foragers, small importers, artisan producers. These vendors are not accustomed to enterprise procurement requirements. They don't have certificates of insurance at Wynn's required limits, they don't have formal food safety certification programs, and they're not set up for net payment terms. Every specialty vendor requires manual exception handling, which the Procurement team was not designed to accommodate at scale.
- **No parallel processing:** The onboarding steps are run sequentially by a single coordinator. Legal review does not start until documents are complete. Insurance review does not start until legal review is done. In practice, there is no technical dependency between these steps — they could run simultaneously.
- **The ERP setup lag:** Oracle vendor setup is the last step. The vendor master form is sent to the vendor at the end of the process, which adds 2–3 days of wait time at the finish line. If the setup is incorrect (wrong bank details, wrong payment terms), the first invoice cannot be processed and the vendor relationship starts with a payment dispute.
- **No timeline visibility for the chef:** Once the chef submits a vendor request, they have no visibility into where the vendor is in the process. They email the Procurement Coordinator, who checks the Excel tracker. On complex vendors, the chef may not know about a document gap or insurance issue until they ask — which is often when they're placing their first order and the vendor isn't approved yet.
- **The approved vendor list is static:** The Excel master list is updated manually. There is no way for a chef to search it in real-time to see if a vendor they want is already approved, already being reviewed, or was previously rejected and why.

---

## Section 4 — Performance Baselines

- **Average onboarding cycle time (request to first approved PO):** 22–35 days for standard vendors; 45–70 days for specialty/small vendors
- **Target cycle time:** No formally documented target. Chefs informally expect 2 weeks. Procurement informally targets 3 weeks.
- **Document resubmission rate:** Approximately 45% of vendor submissions have at least one document gap requiring resubmission
- **Exception rate (insurance or certification gaps):** Approximately 30% of fine dining vendor requests involve some form of insurance or food safety exception
- **ERP setup error rate:** Approximately 15% of new vendor setups in Oracle contain at least one error requiring correction (typically bank account or payment terms)
- **Vendor attrition during onboarding:** Small vendors sometimes abandon the process — estimated 10–12% of initiated onboardings are abandoned before completion, primarily small artisan vendors

---

## Section 5 — Systems & Integrations

| System | Role in Process | Known Limitations / Workarounds |
|---|---|---|
| Oracle Hospitality / Procurement module | Approved vendor master, PO issuance, invoice processing | Vendor setup requires separate vendor master form sent at end of process. No integration with onboarding workflow. Cannot place a PO for a vendor not set up in Oracle. |
| SharePoint | Document storage for vendor qualification packages | Documents stored in individual vendor folders. No workflow automation. No version control. Coordinators manually track document completeness in a separate Excel sheet. |
| Excel (Approved Vendor List) | Master list of approved vendors | Static file maintained by Procurement Manager. Not searchable in real-time by chefs. Does not show vendors in process or previously rejected. Updated manually after each approval. |
| Email | All communication with vendors and internal reviewers | No structured intake. Documents arrive in various formats and email threads. Coordinator manually monitors and follows up. |
| PDF vendor request form | Initial chef request | Not a fillable digital form. Chefs print, fill by hand or in Acrobat, scan or photograph, and email. Common source of errors and missing information. |
| Wynn contract template (Word) | Standard vendor agreement | Used for most vendors. Non-standard terms require tracked-changes negotiation in Word via email. No contract lifecycle management system. |

---

## Section 6 — Compliance & Control Context

- **Food safety requirements:** Nevada food safety regulations and Clark County Health Department requirements apply to all food vendors. Vendors must hold valid food handler certifications and maintain HACCP (Hazard Analysis Critical Control Point) compliance. Wynn's fine dining standards exceed regulatory minimums.
- **Liability insurance:** Wynn's standard requirement is $2M general liability. This is a Risk Management policy, not a regulatory mandate. The threshold was set for large commercial vendors and creates friction with small artisan vendors.
- **Alcohol vendors:** Wine and spirits distributors are subject to Nevada liquor licensing requirements — they must hold valid distributor licenses. This is verified during onboarding but the license renewal monitoring after onboarding is not in scope for this audit.
- **PCI/payment security:** Vendor bank account information collected during Oracle setup is sensitive. The current process sends a PDF bank form via email — this is a data security concern.
- **Segregation of duties:** The chef who requests the vendor has no role in the approval decision. Procurement, Legal, Risk Management, and Finance all have independent review steps. This structure is sound.
- **Prior compliance reviews:** A 2023 internal audit flagged the bank account collection via email as a security risk. No corrective action has been implemented.

---

## Section 7 — Recent Incidents or Near-Misses

**Incident 1 — Flagship restaurant opening week product gaps (Q2 2024)**
For the relaunch of a flagship fine dining restaurant, 6 specialty vendors were in the onboarding process at the time of opening. Three were approved within 48 hours of opening (acceptable). Two were approved 5–8 days after opening (the relevant menu items were substituted). One — a caviar supplier — was still pending insurance documentation 11 days after opening. The chef had to substitute a different caviar product for 11 days. This vendor was recommended by the incoming Executive Chef and had been submitted 6 weeks before opening, which should have been sufficient time. Investigation revealed the vendor's insurance broker had sent a non-compliant COI, and the back-and-forth between Risk Management, the vendor, and the broker was not escalated despite the restaurant opening date.

**Incident 2 — Oracle setup error causing payment dispute (Q3 2024)**
A specialty mushroom forager was onboarded correctly through all qualification steps but had an error in their Oracle vendor setup (wrong ACH routing number). Their first three invoices were processed but the payments were sent to the wrong bank account. The error was not discovered for 6 weeks, during which the vendor stopped fulfilling orders believing they weren't being paid. The chef had to source mushrooms from a backup supplier for 3 weeks while the payment error was investigated and resolved. The ACH funds were eventually recovered, but the vendor relationship required personal outreach from the Executive Chef to repair.

**Near-miss — Rejected vendor resubmitted (Q1 2025)**
A produce vendor that had been rejected in 2023 for failing food safety inspection was resubmitted as a new vendor request by a different chef at Encore who was unaware of the prior rejection. The coordinator who processed the original rejection had left. Because the approved vendor list does not include rejection history, the vendor was nearly approved before a senior Procurement Manager recognized the company name and found the prior rejection in archived emails.

---

## Section 8 — Audit Scope & Constraints

- **Out of scope:** Existing vendor performance management and annual vendor reviews. Beverage and alcohol purchasing (managed under a separate liquor purchasing process). Vendor onboarding at Wynn Macau and Encore Boston Harbor (different supply chain structures).
- **Appetite for change:** High from both F&B leadership and Procurement. The opening-week product gap incidents have created urgency. There is appetite for a dedicated vendor portal and digital intake process.
- **Technology constraint:** Oracle is the system of record for vendor payments and cannot be replaced. Any new intake or workflow tool must ultimately feed Oracle, not replace it.
- **Relationship consideration:** Several specialty vendors (small farms, foragers, artisan producers) are personal relationships of the Executive Chefs. Any process changes must be communicated carefully — chefs are protective of these relationships and will resist changes that feel like bureaucracy imposed on their culinary vision.
- **Data security:** The bank account collection via email issue should be addressed as part of any process redesign. A secure vendor portal for document submission is the preferred solution.
