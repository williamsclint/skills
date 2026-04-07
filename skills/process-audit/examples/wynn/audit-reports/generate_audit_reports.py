"""
generate_audit_reports.py
Generates 5 formal Wynn Resorts Internal Audit Report .docx files.
Uses wynn_doc_utils from the wynn-doc-format skill for all formatting.
"""

import sys
import os
import requests

sys.path.insert(0, r"C:\Users\clwillia\.claude\skills\wynn-doc-format")
from wynn_doc_utils import (
    new_doc, set_margins, add_letterhead, add_footer,
    add_heading, add_body, add_spacer, add_horizontal_rule,
    add_meta_box, add_exec_summary_block, add_scope_methodology,
    add_findings_summary_table, add_finding_block,
    add_observation_block, add_prior_findings_table, add_sign_off_block,
)

LOGO_URL = "https://images.ctfassets.net/nmhu6zvnbnyf/6OGKMyj2vnB0ROqomayO0E/6e468d63e0f43d47b3c94c64e92ad1ee/image.png"
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

AUDIT_TEAM = [
    {"role": "Lead Auditor",        "name": "Senior Internal Auditor"},
    {"role": "Audit Manager",       "name": "Director of Internal Audit"},
    {"role": "Chief Audit Executive","name": "VP Internal Audit & Compliance"},
]

# =============================================================================
# REPORT 1 — VIP Casino Credit Issuance
# =============================================================================
REPORT_1 = {
    "title":       "VIP Patron Casino Credit Issuance",
    "out":         "01-VIP-Casino-Credit-Issuance-Audit-Report.docx",
    "meta": {
        "AUDIT REFERENCE":    "WR-IA-2025-001",
        "Property":           "Wynn Las Vegas / Encore Las Vegas",
        "Department":         "Casino Credit Operations",
        "Process Owner":      "Director of Casino Credit",
        "Audit Period":       "January – March 2025",
        "Report Date":        "March 25, 2025",
        "Classification":     "Operational & Compliance",
    },
    "exec_summary": {
        "overall_rating": "Needs Improvement",
        "counts": {"Critical": 0, "High": 3, "Medium": 2, "Low": 0},
        "bullets": [
            "A patron with a $400K delinquent marker at Encore Boston Harbor was issued $350K in new credit at Wynn Las Vegas due to the absence of a cross-property credit visibility control.",
            "An undocumented 'relationship exception' pathway allows VIP hosts to bypass financial verification. Approximately 20–25% of credits above $250K involve an undocumented exception; this pathway contributed to the $1.2M patron default in Q3 2024.",
            "All final credit approvals route to a single Director with no documented backup authority. Approval delays of 2–4 days during Director travel periods have been observed.",
            "Financial verification documents are retained in VIP host personal email inboxes with no system of record. An NGCB corrective action finding was issued in 2024 as a result.",
            "Wynn's default rate of 2.1% exceeds the industry benchmark of approximately 1.4%, suggesting systemic weakness in credit quality controls not captured through current management reporting.",
        ],
    },
    "scope":       "This audit reviewed the end-to-end VIP patron casino credit issuance process at Wynn Las Vegas and Encore Las Vegas, including application intake, financial verification, approval workflows, documentation retention, and cross-property credit visibility. The marker collection and default recovery process, and operations at Wynn Macau and Encore Boston Harbor, are outside the scope of this review.",
    "methodology": "Audit procedures included review of the current credit policy and Internal Control Submission (ICS), walkthrough of the credit approval workflow with the Director of Casino Credit and two VIP Hosts, sample testing of 30 credit files approved in Q4 2024 – Q1 2025, review of CMS configuration and reporting capabilities, interview with the NGCB compliance team regarding the 2024 corrective action finding, and review of the Q3 2024 and Q1 2025 incident documentation.",
    "prior_findings": [
        {
            "ref": "WR-IA-2023-007",
            "title": "Relationship exception pathway not documented in ICS",
            "original_rating": "High",
            "status": "NOT REMEDIATED",
            "notes": "Recommendation to formalize exception policy issued 2023. No ICS amendment filed as of report date.",
        },
        {
            "ref": "NGCB-2024-CA-04",
            "title": "Financial verification documents not producible within required timeframe",
            "original_rating": "Regulatory Finding",
            "status": "PARTIALLY REMEDIATED",
            "notes": "Directive issued to hosts; no system of record designated. Personal inbox retention continues.",
        },
    ],
    "findings": [
        {
            "id":    "FIND-01",
            "title": "Cross-Property Credit Visibility Gap",
            "risk":  "High",
            "condition": "Credit history for patrons is maintained independently at each Wynn property with no consolidated view. A patron with an outstanding delinquent balance at one property can receive new credit at another without the issuing property being aware of the delinquency. In Q1 2025, a patron with a $400K marker in collections at Encore Boston Harbor was issued $350K in new credit at Wynn Las Vegas.",
            "criteria": "Effective credit risk management requires that all material credit exposure and delinquency information be available to decision-makers at the point of a new credit decision. Wynn's credit policy requires a comprehensive patron history review prior to issuance. Industry standard practice for multi-property operators is a consolidated patron credit registry.",
            "cause": "The Casino Management System was implemented independently at each property with no cross-property data integration. No procedural control requires the approving Director to query other properties prior to approval. The lack of a consolidated registry was identified but not prioritized during the 2022 CMS integration project.",
            "effect": "The Q1 2025 incident resulted in $350K in new credit exposure to a patron already in default. Total unquantified exposure from this structural gap across all properties is unknown. At the documented 2.1% default rate, continued inability to identify cross-property delinquency is a material credit risk. Each additional default event above the industry benchmark represents estimated losses of $150K–$1.2M based on recent incident data.",
            "recommendations": [
                "Implement a mandatory cross-property credit check as a required, documented step before any credit approval. The check result must be recorded in the patron's CMS credit file.",
                "Establish a shared delinquency registry accessible to all Wynn properties, updated at minimum weekly, containing all patrons with markers in collections or default.",
                "As an immediate interim control, issue a written directive requiring the approving Director to email each other Wynn property's credit team for any approval above $100K, with responses retained in the credit file.",
                "Assign a project owner and completion timeline for cross-property CMS integration; treat as a priority workstream of the stalled 2022 project.",
            ],
            "owner":  "VP Casino Operations / Director of Casino Credit",
            "target": "30 days (procedural); 180 days (system integration)",
            "mgmt_response": "Management acknowledges the finding. An interim procedural control will be implemented within 30 days. A cross-property integration roadmap will be presented to the COO within 60 days.",
        },
        {
            "id":    "FIND-02",
            "title": "Undocumented Relationship Exception Pathway",
            "risk":  "High",
            "condition": "VIP hosts may request a 'relationship exception' from the Director of Casino Credit to bypass or abbreviate the standard verification sequence, including financial document review. These exceptions are approved verbally or via email and are not logged in the CMS, the patron's credit file, or any exception register. An estimated 20–25% of credit approvals above $250K involve an undocumented exception. The $1.2M patron default in Q3 2024 involved a patron whose financial verification was bypassed under this mechanism.",
            "criteria": "Wynn's Internal Control Submission filed with the NGCB documents a single credit approval pathway with no provision for a relationship exception. BSA/AML patron due diligence requirements apply to all high-value credit decisions irrespective of relationship status. All material deviations from documented controls must be logged and auditable per internal policy and regulatory expectation.",
            "cause": "The exception pathway emerged informally as VIP hosts sought to accelerate approvals for high-value patrons. It was never formalized, subjected to oversight controls, or incorporated into the ICS. The Director's authority to grant exceptions has never been formally bounded or documented.",
            "effect": "The undocumented pathway created a direct causal link to the $1.2M default in Q3 2024. Aggregate credit risk exposure from the exception pathway cannot be quantified because exceptions are not tracked. The pathway creates a gap in BSA/AML patron due diligence documentation that could draw regulatory scrutiny. This finding was previously identified in the 2023 internal audit and has not been remediated.",
            "recommendations": [
                "Immediately cease verbal and email-only exception approvals. All exceptions must be documented in the patron's CMS credit file with the specific verification step waived, the business justification, and the approver's identity and date.",
                "Draft and file an ICS amendment with NGCB formalizing an exception pathway, including: eligibility criteria, maximum credit amounts, required documentation, dual approval requirements above $500K, and a quarterly exception report to the VP Casino Operations.",
                "Conduct a retrospective review of all credit approvals in the past 12 months that involved an exception to assess documentation completeness and BSA/AML due diligence adequacy.",
                "Implement a mandatory exception log in the CMS, reported monthly to the Director and quarterly to the VP.",
            ],
            "owner":  "Director of Casino Credit / Chief Compliance Officer",
            "target": "30 days (procedural); 90 days (ICS amendment filing)",
            "mgmt_response": "Management acknowledges the finding. Verbal exception approvals will cease immediately. An ICS amendment will be drafted within 60 days and submitted to NGCB within 90 days.",
        },
        {
            "id":    "FIND-03",
            "title": "Single Approver Dependency — No Documented Backup Authority",
            "risk":  "High",
            "condition": "All final credit approval decisions route exclusively to the Director of Casino Credit. No backup approval authority is designated in writing. During Director travel periods — which occur frequently given the nature of the role — approval requests queue with no documented resolution path. Approval delays of 2–4 business days have been observed and informally acknowledged by the VIP host team.",
            "criteria": "Business continuity principles require that no critical operational or financial approval authority reside exclusively with a single individual. Key approval roles must have documented backup designees with equivalent authority. Wynn's operational risk framework requires identified single points of failure to be mitigated.",
            "cause": "The role was designed as a centralized authority to maintain consistency and accountability in credit decisions. A backup designation was never formalized when the role was established and has not been addressed in subsequent process reviews.",
            "effect": "Approval delays of 2–4 days during Director travel directly impact VIP host ability to serve time-sensitive patron requests. High-value patrons who cannot receive timely credit decisions may choose to play at competing properties. The revenue impact of approval delays has not been measured but is considered material given the ADT profile of patrons in the credit pipeline.",
            "recommendations": [
                "Formally designate a backup credit approval authority — recommended to be the VP Casino Operations or a senior Credit Manager — with documented scope, approval limits, and escalation triggers.",
                "Publish and maintain a coverage calendar for Director travel, updated no less than two weeks in advance, identifying the active backup approver for each period.",
                "Define maximum approval turnaround SLAs (recommended: 48 hours for requests under $250K; 72 hours for requests above) with automated escalation to the backup authority upon breach.",
            ],
            "owner":  "VP Casino Operations",
            "target": "30 days",
            "mgmt_response": "Management acknowledges the finding. A backup authority designation will be documented and communicated within 30 days.",
        },
        {
            "id":    "FIND-04",
            "title": "Financial Verification Documents Not Retained in System of Record",
            "risk":  "Medium",
            "condition": "Financial verification documents submitted by patrons — bank statements, brokerage statements, proof of assets — are received by VIP hosts and retained in personal email inboxes. These documents are not uploaded to a shared system of record. In a 2024 NGCB compliance review, three patron credit files could not be produced within the required timeframe because documents resided in a host's personal inbox. A corrective action finding was issued.",
            "criteria": "Regulatory and internal policy require all documentation supporting a credit decision to be producible upon request within a defined timeframe. Financial documents containing patron personally identifiable information must be protected under applicable privacy and data security standards. Personal email inboxes do not provide the access controls, retention guarantees, or discoverability required for compliance.",
            "cause": "The credit intake process was designed before current document management and privacy requirements were in place. No system has been designated for financial document storage, and hosts have no formal mechanism to share or upload documents outside of email.",
            "effect": "Wynn received a corrective action finding from NGCB in 2024. Failure to remediate increases the risk of a more significant regulatory finding in a future examination. Patron financial data stored in personal email inboxes represents a data privacy and security risk. Upon host departure, patron financial records become inaccessible or unmanaged.",
            "recommendations": [
                "Immediately designate a secure, shared document repository (SharePoint or equivalent) for patron financial documents, with access restricted to the credit team.",
                "Issue a written directive to all VIP hosts requiring upload of patron financial documents within 24 hours of receipt, with confirmation sent to the credit team.",
                "Include document retention compliance in the next VIP host compliance review cycle.",
                "Incorporate a secure document upload mechanism into the CMS as part of the 2022 integration project completion.",
            ],
            "owner":  "Director of Casino Credit / VP Information Technology",
            "target": "30 days (procedural); 90 days (system)",
            "mgmt_response": "Management acknowledges the finding. A SharePoint-based interim solution will be designated and communicated within 30 days.",
        },
        {
            "id":    "FIND-05",
            "title": "No Formal Credit Performance Metrics or SLA Framework",
            "risk":  "Medium",
            "condition": "There is no documented SLA for credit approval turnaround time. Performance metrics — approval cycle time, exception rate, default rate by segment, recovery rate — are not formally tracked or reported. The 2.1% default rate identified in this audit was not previously known to VP Casino Operations and was not visible through any existing management reporting.",
            "criteria": "Effective credit operations require defined performance metrics and regular management reporting to enable oversight, trend identification, and early intervention when performance degrades.",
            "cause": "The credit function was established as a relationship-driven operation with an emphasis on patron experience. Formal performance measurement was not built into the function's governance model.",
            "effect": "Management has had no systematic visibility into credit program performance. The above-industry-average default rate has not been identified as a trend or escalated for management attention. Without baseline metrics, the impact of process changes — including those recommended in this report — cannot be measured.",
            "recommendations": [
                "Define and baseline a credit performance scorecard including: average approval cycle time by patron tier, exception rate by host and segment, default rate by credit tier, and recovery rate on defaulted markers.",
                "Implement monthly reporting of credit metrics to VP Casino Operations, with quarterly trend review.",
                "Set target thresholds for each metric with defined escalation protocols when thresholds are breached.",
            ],
            "owner":  "Director of Casino Credit",
            "target": "60 days",
            "mgmt_response": "Management acknowledges the finding. A draft scorecard will be presented to VP Casino Operations within 45 days.",
        },
    ],
    "observations": [
        {
            "id":     "OBS-01",
            "title":  "CMS Integration Project Incomplete — 12% Data Entry Error Rate",
            "risk":   "Medium",
            "detail": "The 2022 project to enable digital credit application intake directly in the CMS was deployed at one of four cashier stations and was never extended to Encore Las Vegas. All other intake continues via paper form with manual re-entry, producing a documented 12% error rate. The project sponsor has since left the organization and no replacement owner has been assigned.",
            "recommendation": "Assign a new project owner and develop a completion timeline for the CMS integration project. Prioritize deployment to all cashier stations at both properties as part of the broader credit process remediation effort.",
        },
        {
            "id":     "OBS-02",
            "title":  "Foreign Identification Acceptance Standards Inconsistently Applied",
            "risk":   "Low",
            "detail": "A reference list for acceptable foreign identification documents exists but is not consistently consulted by cage agents. Inconsistent application creates patron friction and potential compliance gaps for international patrons, who represent a significant portion of the high-value credit segment.",
            "recommendation": "Laminate and post the foreign ID reference list at each cage station. Include a 15-minute refresher on foreign ID standards in the next cage agent training cycle.",
        },
    ],
}

# =============================================================================
# REPORT 2 — Gaming Table Chip Fill & Credit
# =============================================================================
REPORT_2 = {
    "title":       "Gaming Table Chip Fill & Credit Process",
    "out":         "02-Gaming-Table-Fill-Credit-Audit-Report.docx",
    "meta": {
        "AUDIT REFERENCE":    "WR-IA-2025-002",
        "Property":           "Wynn Las Vegas / Encore Las Vegas",
        "Department":         "Casino Operations — Table Games",
        "Process Owner":      "Cage Manager / Shift Manager, Casino Operations",
        "Audit Period":       "January – March 2025",
        "Report Date":        "March 25, 2025",
        "Classification":     "Operational & Compliance",
    },
    "exec_summary": {
        "overall_rating": "Needs Improvement",
        "counts": {"Critical": 0, "High": 2, "Medium": 3, "Low": 0},
        "bullets": [
            "Fill request delays during peak events (Formula 1 2024, New Year's Eve 2024) resulted in estimated lost gaming revenue of $200K–$400K. Three high-limit baccarat tables were idle for a combined 47 minutes on New Year's Eve due to fill queue congestion.",
            "There is no electronic queuing or tracking system for fill requests. During peak events, the cage received up to 14 simultaneous requests managed via handwritten notes and verbal memory, resulting in out-of-order fulfillment.",
            "Surveillance fill logging is manual and was documented as lagging during high-volume periods, creating a documentation sequencing gap. A 6-hour internal investigation was required to resolve a single surveillance log irregularity during Formula 1 2024.",
            "Security escort staffing for fills is set at average-volume levels with no event-specific scaling model. Average escort wait time reached 18–22 minutes on New Year's Eve versus a normal 5–8 minutes.",
            "There is no real-time visibility into chip inventory levels across gaming tables. Pit supervisors assess levels by walking the pit, creating reactive rather than predictive fill management.",
        ],
    },
    "scope":       "This audit reviewed the end-to-end gaming table chip fill and credit process at Wynn Las Vegas and Encore Las Vegas, including fill request initiation, cage preparation, security escort, pit verification, surveillance documentation, and end-of-shift reconciliation. The broader soft count and table game opening/closing inventory processes are out of scope.",
    "methodology": "Audit procedures included walkthrough of the fill process across two shifts at Wynn Las Vegas, review of CMS fill transaction records for Q4 2024 – Q1 2025, interview with Cage Manager, Shift Manager, and Surveillance Supervisor, review of Formula 1 2024 and New Year's Eve 2024 incident documentation, observation of a fill request sequence during a weekend operating shift, and review of NGCB Regulation 12 compliance requirements and Wynn's Internal Control Submission.",
    "prior_findings": [
        {
            "ref": "NGCB-2023-OBS-11",
            "title": "Surveillance fill logging lag noted as observation",
            "original_rating": "Regulatory Observation",
            "status": "NOT REMEDIATED",
            "notes": "Wynn committed to exploring integrated logging. No structural change implemented as of report date.",
        },
    ],
    "findings": [
        {
            "id":    "FIND-01",
            "title": "No Fill Request Queue — Revenue Loss During Peak Events",
            "risk":  "High",
            "condition": "There is no electronic queuing or prioritization system for fill requests. During peak events, pit supervisors submit requests via radio and phone to a single cage window. The cage team manages concurrent requests via verbal communication and handwritten notes. During Formula 1 2024, 14 simultaneous fill requests were received at one point. During New Year's Eve 2024, three high-limit baccarat tables were idle for a combined 47 minutes due to fill delays; one patron with a $2M+ ADT left the floor and did not return.",
            "criteria": "Casino operations require that fill requests be fulfilled within a defined service window to avoid table downtime and patron disruption. Wynn's informal internal expectation is sub-15 minutes; no formal SLA is documented. NGCB Regulation 12 requires that all fills be documented accurately; the absence of a queue system creates documentation sequencing risk.",
            "cause": "The fill request process relies on legacy radio/phone communication designed for average operating volume. No digital request tracking was implemented when the 2019 pit management system was partially deployed. Event-specific fill capacity planning has never been formalized.",
            "effect": "Estimated lost gaming revenue from fill-related table downtime was $200K–$400K across the two peak events examined. The high-limit patron departure on New Year's Eve represents an additional unquantified loss from a patron with $2M+ ADT. At the observed frequency of 2–3 major events per quarter, annualized impact is material.",
            "recommendations": [
                "Deploy a tablet-based or terminal-based fill request queue visible simultaneously to the cage and all pit supervisors, showing request time, table number, amount requested, and fulfillment status.",
                "Define a formal fill SLA (recommended: 12 minutes for standard tables, 8 minutes for high-limit) and measure against it during every shift.",
                "Create an event-specific fill capacity plan for each designated special event, including pre-staged chip levels at high-volume tables, additional cage staffing at the fill window, and a dedicated fill escort security detail.",
                "Assign a project owner for pit management system full deployment to the remaining four pit areas.",
            ],
            "owner":  "VP Casino Operations / Cage Manager",
            "target": "60 days (queue system); 30 days (event capacity plan)",
            "mgmt_response": "Management acknowledges the finding. A tablet-based queue solution will be evaluated within 30 days. Event capacity planning will be formalized before the next major event.",
        },
        {
            "id":    "FIND-02",
            "title": "Surveillance Fill Logging Lag — Compliance Documentation Risk",
            "risk":  "High",
            "condition": "Surveillance fill logging is performed manually by surveillance operators who must also monitor all other floor activity simultaneously. During peak periods, fills are logged in batches rather than in real time, and are occasionally logged with incorrect timestamps. During Formula 1 2024, a fill slip in the CMS had no corresponding surveillance log entry within the expected time window, triggering a 6-hour internal investigation. The NGCB noted this as an observation in a 2023 routine examination.",
            "criteria": "NGCB Regulation 12 requires that surveillance documentation of each fill be maintained with an accurate timestamp, linked to the corresponding CMS fill record. Documentation must be producible for regulatory review. Batch logging with timestamp errors creates a compliance gap that could be interpreted as a documentation failure during an examination.",
            "cause": "The surveillance management system and CMS are not integrated. Surveillance operators must manually cross-reference and log fills from camera observation while simultaneously managing all other surveillance responsibilities. No automated notification from CMS to surveillance occurs when a fill is initiated.",
            "effect": "The Formula 1 2024 incident consumed 6 hours of management and compliance time to resolve. If a documentation gap were identified during an NGCB examination rather than through internal review, it could result in a formal regulatory finding with potential financial penalties. The risk is heightened during peak periods when fill volume is 3–4x normal.",
            "recommendations": [
                "Implement an automated alert from CMS to the surveillance management system when each fill slip is generated, providing table number, fill amount, and expected time window for camera logging.",
                "Establish a real-time fill notification queue on surveillance workstations during high-volume periods, staffed by a dedicated operator on major event nights.",
                "Conduct a quarterly reconciliation of CMS fill records against surveillance logs to identify and remediate documentation gaps proactively.",
                "File an ICS amendment to formalize the automated notification workflow once implemented.",
            ],
            "owner":  "Surveillance Manager / VP Information Technology",
            "target": "90 days (system integration); 30 days (procedural reconciliation)",
            "mgmt_response": "Management acknowledges the finding. A requirements review for CMS-surveillance integration will begin within 30 days.",
        },
        {
            "id":    "FIND-03",
            "title": "Security Escort Staffing Not Scaled for Special Events",
            "risk":  "Medium",
            "condition": "Security staffing for chip fill escorts is based on standard operating volume and is not adjusted for special events. During Formula 1 2024 and New Year's Eve 2024, the security team was simultaneously supporting crowd management, VIP arrivals, and perimeter coverage. Fill escorts were deprioritized. Average escort wait time reached 18–22 minutes on New Year's Eve versus a normal baseline of 5–8 minutes.",
            "criteria": "Fill escort timeliness is a key operational dependency. Extended escort wait times directly cause table downtime. Security staffing models should account for all concurrent security demands during high-volume events.",
            "cause": "Event security planning is managed by the Security department with input from Casino Operations for crowd and VIP needs, but fill escort demand is not a formal input to event security staffing models. The two planning processes are siloed.",
            "effect": "Extended escort times were a primary contributor to the $200K–$400K revenue loss identified in FIND-01. On New Year's Eve, escort delays accounted for approximately 40% of total fill cycle time.",
            "recommendations": [
                "Include estimated fill escort demand in the security staffing model for all designated special events, based on projected gaming volume and historical fill frequency data.",
                "Designate a minimum of two dedicated fill escort officers for any event where projected gaming volume exceeds 150% of the standard weekday baseline.",
                "Establish a cross-functional event planning review between Casino Operations and Security for all major events, at minimum 14 days in advance.",
            ],
            "owner":  "Director of Security / VP Casino Operations",
            "target": "45 days",
            "mgmt_response": "Management acknowledges the finding and will incorporate fill escort demand into the next major event staffing plan.",
        },
        {
            "id":    "FIND-04",
            "title": "No Real-Time Table Chip Inventory Visibility",
            "risk":  "Medium",
            "condition": "There is no electronic or automated visibility into chip inventory levels across gaming tables. Pit supervisors assess tray levels by physically walking the pit area. On a 20-table pit, a supervisor may not identify a low-inventory table until a dealer signals or until a fill request creates a service gap. Fill request thresholds are set by individual supervisor judgment with no standardized minimum levels.",
            "criteria": "Proactive fill management requires that inventory levels be monitored against defined thresholds, with fill requests initiated before inventory reaches critical levels. Reactive fill requests — initiated after inventory is already insufficient — create higher risk of table downtime.",
            "cause": "The CMS does not provide real-time tray-level data. Tray inventory is only recorded at opening and closing and via fill transactions. RFID chip tracking, which would enable real-time inventory visibility, has not been implemented.",
            "effect": "Reactive fill requests contributed to queue congestion during peak events. Standardizing fill thresholds and moving to proactive monitoring would reduce fill frequency and urgency during high-volume periods.",
            "recommendations": [
                "Define and document standard chip inventory threshold levels by table type and limit, at which a fill request should be initiated proactively.",
                "Train all pit supervisors on threshold-based fill management; include in standard pit supervisor certification.",
                "Evaluate RFID chip tracking as a medium-term investment to enable real-time tray-level monitoring from the pit supervisor terminal.",
            ],
            "owner":  "Director of Table Games / VP Casino Operations",
            "target": "45 days (procedural thresholds); 12 months (RFID evaluation)",
            "mgmt_response": "Management acknowledges the finding. Standardized threshold guidelines will be developed and distributed within 45 days.",
        },
        {
            "id":    "FIND-05",
            "title": "Fill Request Communication on Shared Radio Channel",
            "risk":  "Medium",
            "condition": "Fill requests are submitted via a radio channel shared with security, floor management, and other operational communications. During peak events, fill requests compete with other communications. At least two fills during Formula 1 2024 were confirmed to have been received out of order by the cage, partly due to radio congestion. A dedicated fill request channel was proposed in 2023 and not implemented.",
            "criteria": "Operational communication channels for time-sensitive, regulated processes should be isolated from competing traffic to ensure accuracy and timeliness. Fill requests involve financial amounts and specific table locations that must be transmitted and received accurately.",
            "cause": "A dedicated fill channel was not implemented due to radio hardware limitations and the prioritization of other technology investments.",
            "effect": "Radio congestion contributed to the out-of-order fill fulfillment during Formula 1 2024. Misheard fill amounts or table numbers could result in incorrect fills requiring investigation and delay.",
            "recommendations": [
                "Implement a dedicated digital fill request channel — either a separate radio channel or, preferably, the tablet-based queue system recommended in FIND-01 — to isolate fill communications from general floor traffic.",
                "As an immediate interim measure, establish a standard fill request communication protocol (table number, denomination, amount) to reduce transmission errors on the shared channel.",
            ],
            "owner":  "Cage Manager / Director of Security",
            "target": "30 days (protocol); 60 days (digital channel)",
            "mgmt_response": "Management acknowledges the finding. A standardized communication protocol will be issued immediately.",
        },
    ],
    "observations": [
        {
            "id":     "OBS-01",
            "title":  "Camera Angle Limitations at Select Table Positions",
            "risk":   "Medium",
            "detail": "At certain tables in the older pit configurations, the camera angle requires dealers to reposition chips multiple times during a fill to achieve a clear surveillance view. This is a known issue that has not been structurally resolved. Each repositioning adds 1–2 minutes to fill cycle time and creates additional handling of chips outside the tray.",
            "recommendation": "Commission a camera coverage audit for all tables where angle issues have been documented. Prioritize camera repositioning or supplemental camera installation at the highest-volume tables where the issue most frequently causes delay.",
        },
    ],
}

# =============================================================================
# REPORT 3 — Gaming Employee Licensing & Onboarding
# =============================================================================
REPORT_3 = {
    "title":       "New Gaming Employee Licensing & Onboarding",
    "out":         "03-Gaming-License-Onboarding-Audit-Report.docx",
    "meta": {
        "AUDIT REFERENCE":    "WR-IA-2025-003",
        "Property":           "Wynn Las Vegas / Encore Las Vegas",
        "Department":         "Human Resources — Gaming Compliance",
        "Process Owner":      "Director of Human Resources, Gaming Compliance",
        "Audit Period":       "January – March 2025",
        "Report Date":        "March 25, 2025",
        "Classification":     "Operational & Compliance",
    },
    "exec_summary": {
        "overall_rating": "Needs Improvement",
        "counts": {"Critical": 0, "High": 3, "Medium": 2, "Low": 0},
        "bullets": [
            "Time-to-floor averages 47 days against a 30-day target. Competitor properties are achieving 28–32 days. The gap is driven by sequential scheduling of steps that could run in parallel, adding an estimated 5–8 days unnecessarily.",
            "Candidate attrition during the onboarding process has reached 18% of accepted gaming offers — double the 2021 rate of 9%. The NGCB investigation window (14–21 days) with no candidate-facing status visibility is the primary attrition driver.",
            "A gaming work permit renewal was missed for one existing employee, who worked for 19 days on an expired permit. Wynn self-reported a violation to NGCB. Renewal tracking relies entirely on individual coordinator calendar reminders with no system-level controls.",
            "Uniform inventory is not checked before scheduling fitting appointments. Out-of-stock uniforms placed 8 new hires in paid waiting status for 12 days at a cost of $14,400 in wages with no corresponding floor contribution.",
            "When coordinators leave, active pipeline tracking and permit renewal reminders leave with them. No shared dashboard or system-enforced handoff process exists.",
        ],
    },
    "scope":       "This audit reviewed the end-to-end new gaming employee onboarding process at Wynn Las Vegas and Encore Las Vegas, from accepted offer through first scheduled gaming floor shift. This includes application intake, NGCB licensing, background screening, I-9 compliance, uniform issuance, and training certification. Gaming work permit renewals for existing employees and non-gaming employee onboarding are out of scope.",
    "methodology": "Audit procedures included walkthrough of the onboarding process with two HR Coordinators and the Director of HR Gaming Compliance, review of 40 onboarding files completed in Q3–Q4 2024, analysis of time-to-floor metrics from Workday data, review of exit survey data citing process reasons for offer withdrawal, interview with the Training Department and Uniform Room management, and review of the NGCB notice of violation issued in Q1 2025.",
    "prior_findings": [
        {
            "ref": "NGCB-2025-NOV-02",
            "title": "Employee worked 19 days on expired gaming work permit",
            "original_rating": "Regulatory Violation",
            "status": "CORRECTIVE ACTION IN PROGRESS",
            "notes": "Wynn self-reported. Corrective action plan submitted. Full remediation required by Q2 2025.",
        },
    ],
    "findings": [
        {
            "id":    "FIND-01",
            "title": "Sequential Scheduling Adds 5–8 Days to Time-to-Floor",
            "risk":  "High",
            "condition": "Fingerprinting, drug screening, and background check — three steps with no technical dependency on each other — are routinely scheduled sequentially by HR Coordinators rather than simultaneously. Fingerprinting is typically scheduled first; drug screening is scheduled after the fingerprinting appointment is confirmed; background check is initiated after the drug screening is scheduled. This sequential approach adds an estimated 5–8 business days to the pre-submission window.",
            "criteria": "Process efficiency principles require that independent workflow steps be executed in parallel where no dependency exists. Reducing time-to-floor is a stated operational objective, and the 30-day target cannot be achieved without parallel execution of the pre-submission steps.",
            "cause": "Coordinators manage 25–40 active candidates simultaneously using individual spreadsheets with no shared dashboard. Tracking three concurrent vendor engagements per candidate without a unified system is cognitively complex, leading to sequential scheduling as a simplification strategy. No standard operating procedure requires or instructs parallel scheduling.",
            "effect": "Sequential scheduling adds 5–8 days to an average process already 17 days over target. At 18% candidate attrition and 100 new hires per month, each week of unnecessary delay exposes approximately 18 additional candidates to competitor offers. The Q2 2024 poker room opening resulted in 9 of 28 accepted candidates leaving during the process, with 3 citing wait time explicitly.",
            "recommendations": [
                "Update the standard operating procedure to require simultaneous initiation of fingerprinting, drug screening, and background check on the day the offer is accepted.",
                "Create a unified candidate tracking dashboard (recommended: Smartsheet or an enhanced Workday onboarding checklist) showing all three vendor statuses per candidate in a single view.",
                "Assign each coordinator a maximum active pipeline of 20 candidates to reduce the cognitive load that drives sequential scheduling as a coping mechanism.",
            ],
            "owner":  "Director of HR, Gaming Compliance",
            "target": "30 days (SOP update); 60 days (dashboard)",
            "mgmt_response": "Management acknowledges the finding. The SOP will be updated to require parallel scheduling immediately. A dashboard solution will be piloted within 60 days.",
        },
        {
            "id":    "FIND-02",
            "title": "Candidate Attrition During NGCB Investigation — No Status Visibility",
            "risk":  "High",
            "condition": "The NGCB investigation window (14–21 days standard; up to 45 days for complex histories) is the longest single phase of the onboarding process. During this period, candidates receive no status updates because Wynn has no visibility into investigation progress — there is no NGCB status portal, API, or notification system. Candidates must rely entirely on their coordinator, who has no information to share. Candidate attrition has increased from 9% in 2021 to 18% in 2024, with the NGCB waiting period cited as the primary driver.",
            "criteria": "Effective talent acquisition requires proactive candidate engagement throughout the onboarding process to prevent attrition to competing employers. Industry benchmark for gaming employee onboarding attrition is below 10%.",
            "cause": "Wynn has no control over NGCB investigation timelines or visibility. However, no structured candidate engagement program has been developed for the investigation window. Communication defaults to silence unless the candidate reaches out.",
            "effect": "At 18% attrition on approximately 100 accepted offers per month, Wynn loses approximately 18 candidates per month during onboarding. Replacing each lost candidate requires re-posting, re-interviewing, and restarting the onboarding process — estimated at $3,000–$5,000 in recruiting and administrative cost per replacement, plus the operational cost of running understaffed. Annualized estimated attrition cost: $650K–$1.1M.",
            "recommendations": [
                "Implement a structured candidate engagement calendar for the NGCB waiting period: a welcome message on Day 1 of the wait, a check-in call on Day 7, and a status email on Day 14 with an estimated completion range.",
                "Build a simple candidate-facing status portal (email-linked, no login required) showing completed steps, current step, and estimated remaining timeline — excluding the NGCB step, which cannot be tracked.",
                "Train coordinators to proactively offer competitive context to candidates during the wait period (benefits summary, team introductions, floor tour scheduling) to maintain engagement.",
                "Track attrition rate by stage monthly and report to VP Human Resources as a talent pipeline health metric.",
            ],
            "owner":  "Director of HR, Gaming Compliance / VP Human Resources",
            "target": "45 days",
            "mgmt_response": "Management acknowledges the finding. A candidate engagement protocol will be drafted and piloted within 45 days.",
        },
        {
            "id":    "FIND-03",
            "title": "No Centralized Coordinator Dashboard — SPOF on Permit Tracking",
            "risk":  "High",
            "condition": "Each HR Coordinator maintains onboarding pipeline tracking and gaming work permit renewal reminders in individual personal spreadsheets and calendar applications. When a coordinator leaves, their active pipeline tracking and all associated renewal reminders leave with them. The Q1 2025 NGCB violation — an employee who worked 19 days on an expired permit — was directly caused by a renewal reminder being held in a departed coordinator's calendar.",
            "criteria": "Regulatory compliance tracking for gaming work permits must be maintained in a system of record that is independent of individual employee tenure. NGCB regulations prohibit gaming floor work without a valid permit. A single missed renewal constitutes a regulatory violation subject to notice and potential fine.",
            "effect": "Wynn received a Notice of Violation in Q1 2025 and submitted a corrective action plan. Continued reliance on individual coordinator calendars creates ongoing risk of additional violations. With approximately 1,500+ active gaming employees across both properties, the renewal tracking workload requires a system-level solution, not a manual one.",
            "criteria": "A centralized, system-maintained permit expiry registry with automated alerts is the minimum expected control for a property of Wynn's size and regulatory profile.",
            "cause": "Permit renewal tracking was designed as a coordinator responsibility when the workforce was smaller. The process was never migrated to a system-managed workflow as the property scaled.",
            "recommendations": [
                "Implement a permit expiry registry in Workday (or equivalent HRIS) with automated email alerts to the coordinator and their manager at 90 days, 60 days, and 30 days before each permit expiration.",
                "Require immediate upload of all gaming work permit expiration dates into the new registry as a remediation action for the Q1 2025 NGCB corrective action plan.",
                "Designate a backup coordinator for each active portfolio so that permit reminders are never held by a single individual.",
                "Conduct a full audit of all active gaming employee permit expiration dates within 30 days to identify any additional near-expiry permits.",
            ],
            "owner":  "Director of HR, Gaming Compliance / VP Information Technology",
            "target": "30 days (manual audit and registry population); 60 days (automated alerts)",
            "mgmt_response": "Management acknowledges the finding. A full permit expiry audit will begin immediately. Workday configuration for automated alerts is being scoped.",
        },
        {
            "id":    "FIND-04",
            "title": "Uniform Inventory Not Verified Before Fitting Appointments",
            "risk":  "Medium",
            "condition": "Uniform fitting appointments are scheduled without first verifying stock availability for the candidate's likely size. Out-of-stock situations are discovered at the fitting appointment, after all other onboarding steps are complete. In Q3 2024, 8 of 22 new baccarat dealers required a uniform size (men's 46L jacket) that was out of stock. Lead time from the supplier was 12 days. The 8 dealers were placed in paid waiting status for 12 days — costing $14,400 in wages with no gaming floor contribution.",
            "criteria": "Operational process design requires that resource availability be verified before scheduling dependent steps. Uniform availability is a prerequisite to gaming floor deployment; out-of-stock situations at the point of fitting represent a preventable last-mile delay.",
            "cause": "The Uniform Room maintains stock on a separate spreadsheet not accessible to HR Coordinators. There is no integration between Workday (where candidate information is held) and the Uniform Room inventory system. HR has no mechanism to check stock levels in advance.",
            "effect": "The Q3 2024 incident cost $14,400 in idle wages. With a hiring rate of 100 employees per month and a 22% out-of-stock rate, similar incidents are recurring. Annualized estimated cost of uniform-related idle wage expense: $60K–$80K.",
            "recommendations": [
                "Require HR Coordinators to query the Uniform Room for stock availability of the candidate's estimated size range at least 5 business days before the scheduled fitting appointment.",
                "If stock is unavailable at the time of query, initiate the supplier order immediately rather than waiting for the fitting appointment.",
                "Publish the Uniform Room inventory spreadsheet as a read-only shared file accessible to all HR Coordinators.",
                "Establish a minimum stock level for all standard sizes, with automatic reorder when stock falls below that level.",
            ],
            "owner":  "Director of HR / Uniform Room Manager",
            "target": "30 days",
            "mgmt_response": "Management acknowledges the finding. A shared inventory visibility process will be implemented within 30 days.",
        },
        {
            "id":    "FIND-05",
            "title": "No Documented Policy for Dealing Proficiency Test Failures",
            "risk":  "Medium",
            "condition": "Approximately 7% of new dealer candidates do not pass the dealing proficiency test within two attempts. There is no documented policy defining the outcome: in practice, some candidates are given additional training time and retested, while others are separated. The decision is made at the discretion of the Training Manager. Inconsistent outcomes for similar performance profiles have been observed in the sample of onboarding files reviewed.",
            "criteria": "HR policy and labor relations best practice require that standards for employment continuation or separation following a skills assessment failure be documented, consistently applied, and communicated to candidates at the time of hire.",
            "cause": "The proficiency test failure scenario was never formally incorporated into the onboarding policy documentation. The Training Manager has operated on informal precedent.",
            "effect": "Inconsistent application creates legal exposure for claims of disparate treatment. Candidates who are unclear about the policy may feel the process is arbitrary, contributing to a negative onboarding experience even for those who ultimately pass.",
            "recommendations": [
                "Define and document a clear policy for proficiency test outcomes: maximum number of attempts, remediation training available between attempts, and the outcome upon final failure.",
                "Communicate the policy to candidates at the time the training phase begins.",
                "Apply the policy consistently across all training cohorts, with the Training Manager documenting the rationale for any discretionary decisions.",
            ],
            "owner":  "Director of HR, Gaming Compliance / Training Manager",
            "target": "45 days",
            "mgmt_response": "Management acknowledges the finding. A draft policy will be reviewed with HR leadership within 45 days.",
        },
    ],
    "observations": [
        {
            "id":     "OBS-01",
            "title":  "Workday Onboarding Checklist Not Enforced",
            "risk":   "Low",
            "detail": "The Workday onboarding checklist exists but is used inconsistently by coordinators. Some coordinators complete it in real time; others complete it retrospectively after steps are done. As a result, the checklist does not provide a reliable real-time view of candidate status and cannot be used for management oversight.",
            "recommendation": "Configure Workday to require checklist step completion before the system allows progression to dependent steps. This is a configuration change rather than a development effort and can be implemented without additional investment.",
        },
    ],
}

# =============================================================================
# REPORT 4 — BSA/AML SAR & CTR Filing
# =============================================================================
REPORT_4 = {
    "title":       "BSA/AML Suspicious Activity Report & Currency Transaction Report Filing",
    "out":         "04-BSA-AML-SAR-CTR-Filing-Audit-Report.docx",
    "meta": {
        "AUDIT REFERENCE":    "WR-IA-2025-004",
        "Property":           "Wynn Las Vegas",
        "Department":         "BSA/AML Compliance",
        "Process Owner":      "BSA/AML Compliance Officer",
        "Audit Period":       "January – March 2025",
        "Report Date":        "March 25, 2025",
        "Classification":     "Regulatory Compliance",
    },
    "exec_summary": {
        "overall_rating": "Unsatisfactory",
        "counts": {"Critical": 1, "High": 3, "Medium": 1, "Low": 0},
        "bullets": [
            "A structural gap in cross-department cash transaction aggregation resulted in a missed CTR filing in Q3 2024. The CMS does not automatically aggregate transactions across the cage, pit, and slots for the same patron on the same gaming day. This finding is CRITICAL given active FinCEN examination proceedings.",
            "CTR on-time filing rate of 94–96% is materially below FinCEN's informal tolerance threshold of >99%. The gap is driven by weekend staffing at a single coordinator and an unmanaged alert queue over Saturday–Sunday.",
            "FinCEN's preliminary examination findings cited SAR narrative quality as inadequate in three of twelve reviewed filings. Narratives describe activity but do not explain why it is suspicious relative to the patron's known profile — a specific FinCEN requirement.",
            "'No file' decision documentation is incomplete in an estimated 30–40% of reviewed cases. FinCEN increasingly scrutinizes cases where a SAR was considered but not filed. Inadequate rationale documentation is a second examination finding.",
            "Continuing SAR monitoring (90-day intervals) is tracked entirely via individual analyst calendar reminders. A 180-day monitoring gap occurred in Q2 2024 when an analyst departed without transferring reminders.",
        ],
    },
    "scope":       "This audit reviewed the end-to-end BSA/AML CTR and SAR identification, investigation, and filing process at Wynn Las Vegas. The audit was conducted in direct response to FinCEN preliminary examination findings received in Q4 2024 and is intended to support Wynn's preparation for the final examination report expected in Q2 2025. The broader patron due diligence (CDD) program and W-2G jackpot tax reporting processes are out of scope.",
    "methodology": "Audit procedures included review of 60 CTR filings and 25 SAR filings from Q3 2024 – Q1 2025, including 10 'no file' cases, walkthrough of the CTR and SAR processes with the BSA Compliance Officer and all four BSA Analysts, review of FinCEN preliminary examination feedback documentation, testing of CMS aggregation logic across a sample of multi-department patron transactions, review of the Q3 2024 aggregation miss incident documentation, and benchmarking against FinCEN SAR narrative guidance (FIN-2003-G001).",
    "prior_findings": [
        {
            "ref": "FinCEN-2024-EXAM",
            "title": "SAR narrative quality inadequate — 3 of 12 reviewed filings",
            "original_rating": "Examination Finding (Preliminary)",
            "status": "IN REMEDIATION",
            "notes": "Final examination report expected Q2 2025. This audit addresses root cause.",
        },
        {
            "ref": "FinCEN-2024-EXAM",
            "title": "'No file' decision documentation inadequate",
            "original_rating": "Examination Finding (Preliminary)",
            "status": "IN REMEDIATION",
            "notes": "Final examination report expected Q2 2025. This audit addresses root cause.",
        },
    ],
    "findings": [
        {
            "id":    "FIND-01",
            "title": "Cross-Department CTR Aggregation Gap — Structural Regulatory Risk",
            "risk":  "Critical",
            "condition": "The CMS generates CTR alerts on individual transaction amounts but does not automatically aggregate cash transactions across the cage, pit, and slots for the same patron within the same gaming day. A patron who conducts a $6,500 cash buy-in at a baccarat table and a $5,200 cash transaction at the cage on the same day — aggregated total $11,700 — triggers a CTR requirement that neither department's supervisor sees independently. In Q3 2024, this gap resulted in a missed CTR filing that was discovered during a monthly QA review and filed late. FinCEN was notified.",
            "criteria": "31 CFR §1021.311 requires casinos to file CTRs for cash-in or cash-out transactions by a patron that, in aggregate, exceed $10,000 during a gaming day. The aggregation requirement explicitly covers transactions across all areas of the casino. Failure to aggregate and file constitutes a BSA violation subject to civil money penalties.",
            "cause": "The Aristocrat CMS was configured to alert on single-transaction thresholds only. Cross-department aggregation requires manual reconciliation by the cage supervisor, who has no visibility into pit or slots transactions for the same patron in real time. This is a known CMS limitation that was identified but not resolved during the 2020 compliance platform implementation.",
            "effect": "The Q3 2024 incident resulted in a late CTR filing and FinCEN notification. Each BSA violation carries a potential civil money penalty of up to $25,000 per day per violation. Repeated violations or evidence of systemic failure can trigger penalties in the millions of dollars — FinCEN has assessed penalties exceeding $100M against casino operators for BSA program failures. With 900–1,200 CTRs filed monthly and an unknown number of missed aggregated transactions, the full extent of historical exposure cannot be determined without a comprehensive look-back review.",
            "recommendations": [
                "Commission an immediate technical review with Aristocrat to determine the feasibility of implementing real-time cross-department patron transaction aggregation within the CMS, with a CTR alert triggered when the aggregate threshold is crossed.",
                "Pending a system solution, implement a manual daily aggregation control: designate a BSA Coordinator to query CMS for all patrons with single-department transactions between $7,000 and $9,999 each gaming day and manually cross-reference across departments.",
                "Conduct a retrospective look-back review of the past 24 months of patron transaction data to identify any additional missed aggregated CTR transactions, file any required late CTRs, and assess total historical exposure.",
                "Escalate this finding to the Chief Compliance Officer and General Counsel immediately given active FinCEN examination proceedings.",
            ],
            "owner":  "BSA/AML Compliance Officer / Chief Compliance Officer / VP IT",
            "target": "Immediate (escalation and manual control); 90 days (system review); 120 days (look-back)",
            "mgmt_response": "Management acknowledges this as a critical finding. The CCO has been notified. A manual aggregation control will be implemented by end of week. Legal counsel has been engaged regarding FinCEN examination implications.",
        },
        {
            "id":    "FIND-02",
            "title": "CTR On-Time Filing Rate Materially Below FinCEN Threshold",
            "risk":  "High",
            "condition": "Wynn's CTR on-time filing rate is approximately 94–96%, meaning 4–6% of CTRs (approximately 45–70 per month) are filed after the 15-calendar-day deadline. Root causes include: CMS alerts not acted on within the same shift, patron ID not obtained at time of transaction, coordinator workload backlog, and a single coordinator covering the weekend shift with no backup.",
            "criteria": "31 CFR §1021.311 requires CTR filing within 15 calendar days of the transaction. FinCEN's informal compliance threshold for large casino operators is >99% on-time. Wynn's current rate of 94–96% would be considered a material program deficiency in the context of an active examination.",
            "cause": "Weekend coverage relies on a single BSA Coordinator who also covers other compliance functions. CTR alerts generated Friday through Sunday queue until Monday, creating a backlog that pushes some transactions past the 15-day window. There is no automated deadline tracking or escalation alert.",
            "effect": "At 45–70 late filings per month, Wynn is filing approximately 540–840 late CTRs annually. In the context of the active FinCEN examination, this rate is likely to be cited as a material program deficiency. Civil money penalty exposure per late filing is up to $25,000.",
            "recommendations": [
                "Assign a second BSA Coordinator to weekend CTR processing, or designate a rotating on-call coordinator from the team for weekend alert review.",
                "Implement an automated deadline tracker in the compliance case management system that flags any CTR alert not actioned within 5 days, escalating to the BSA Compliance Officer at 10 days.",
                "Conduct a 90-day review of all CTRs filed to measure on-time rate by root cause category and target each category individually.",
            ],
            "owner":  "BSA/AML Compliance Officer",
            "target": "30 days (staffing); 45 days (deadline tracker)",
            "mgmt_response": "Management acknowledges the finding. Weekend staffing options will be evaluated within 30 days. A deadline tracking solution will be implemented within 45 days.",
        },
        {
            "id":    "FIND-03",
            "title": "SAR Narrative Quality Inconsistent — FinCEN Examination Finding",
            "risk":  "High",
            "condition": "Of the four BSA Analysts who draft SAR narratives, two consistently produce detailed narratives explaining both the activity observed and why it is suspicious relative to the patron's known profile and expected transaction patterns. Two analysts produce minimal narratives that describe the activity accurately but do not provide the 'why suspicious' context that FinCEN guidance requires. Three of twelve SARs reviewed by FinCEN examiners were cited for inadequate narratives. There is no narrative quality standard, peer review process, or template.",
            "criteria": "FinCEN guidance (FIN-2003-G001) requires SAR narratives to include: a clear description of the suspicious activity, the reason the activity is considered suspicious (i.e., how it deviates from expected patron behavior), and any additional context that would assist law enforcement. Narratives that only describe what happened without explaining why it is suspicious do not meet this standard.",
            "cause": "SAR narratives are drafted in Microsoft Word with no template, quality checklist, or structured review process. Analyst quality variance reflects differences in individual training and interpretation of the FinCEN narrative standard. No peer review or supervisory narrative review step exists prior to filing.",
            "effect": "Three SAR narratives were cited as inadequate during the FinCEN examination. Continued quality inconsistency risks additional examination findings in the final report and could be cited as a program weakness requiring remediation under a formal supervisory action.",
            "recommendations": [
                "Develop a SAR narrative template aligned to FinCEN guidance, including required sections: activity description, why suspicious (patron profile deviation), supporting transaction data, and law enforcement utility statement.",
                "Implement a mandatory peer review step: all SAR narratives must be reviewed by a second analyst or the BSA Compliance Officer before filing.",
                "Conduct a calibration session with all four analysts using de-identified examples of strong and weak narratives from the FinCEN-reviewed sample.",
                "Implement a quarterly narrative quality review by the BSA Compliance Officer, with results reported to the Chief Compliance Officer.",
            ],
            "owner":  "BSA/AML Compliance Officer",
            "target": "30 days (template and peer review); 60 days (calibration training)",
            "mgmt_response": "Management acknowledges the finding. A narrative template and peer review requirement will be in place within 30 days, in advance of the final FinCEN examination report.",
        },
        {
            "id":    "FIND-04",
            "title": "'No File' Decision Documentation Inadequate",
            "risk":  "High",
            "condition": "When a suspicious activity report is considered but the team determines no SAR is warranted, the 'no file' decision and its rationale should be documented as thoroughly as a filed SAR. Review of 10 'no file' cases found that 3 had detailed rationale documentation, 4 had single-sentence rationale, and 3 had no documentation of the review or decision at all. This documentation gap was cited in FinCEN's preliminary examination findings.",
            "criteria": "FinCEN examination standards require that 'no file' decisions be documented with sufficient detail to demonstrate that the review was conducted systematically and that the decision not to file was a considered, reasonable judgment. Undocumented 'no file' decisions are indistinguishable from cases that were never reviewed.",
            "cause": "The 'no file' documentation requirement has not been consistently communicated or enforced. Analysts who complete a review and conclude no filing is required have historically moved on to the next case without documenting the conclusion. The case management system has a rationale field for 'no file' decisions but its completion is not enforced.",
            "effect": "Three 'no file' cases reviewed by FinCEN examiners could not demonstrate that a systematic review was conducted. This is a direct examination finding. In enforcement contexts, undocumented 'no file' decisions can be treated as evidence of a deficient compliance program regardless of whether a SAR was actually warranted.",
            "recommendations": [
                "Configure the compliance case management system to require completion of the rationale field before a case can be closed as 'no file.' The rationale must address: the activity reviewed, the patron's expected transaction profile, the reason the activity was not deemed suspicious, and the analyst's name and date.",
                "Immediately retroactively document rationale for all open 'no file' cases with incomplete records.",
                "Include 'no file' documentation quality in the quarterly narrative quality review.",
            ],
            "owner":  "BSA/AML Compliance Officer",
            "target": "Immediate (retroactive documentation); 30 days (system configuration)",
            "mgmt_response": "Management acknowledges the finding. Retroactive documentation of open cases will begin immediately. System configuration will be implemented within 30 days.",
        },
        {
            "id":    "FIND-05",
            "title": "Continuing SAR Monitoring Relies on Personal Calendar Reminders",
            "risk":  "Medium",
            "condition": "Patrons for whom a SAR has been filed require ongoing monitoring at 90-day intervals, with a continuing SAR filed if the suspicious activity persists. These monitoring reminders are set as calendar entries in individual analyst Outlook calendars. When an analyst leaves, their monitoring reminders leave with them. In Q2 2024, a 180-day gap in monitoring occurred when an analyst departed and their reminders were not transferred. The patron continued transacting during the gap.",
            "criteria": "FinCEN guidance requires ongoing monitoring of subjects of filed SARs. The monitoring cadence must be maintained independent of individual employee tenure. Single-person calendar reminders do not constitute a system of record for regulatory compliance tracking.",
            "cause": "The compliance case management system does not have an automated 90-day monitoring trigger. The calendar reminder approach was implemented as a workaround when the system was deployed and was never replaced with a system-level solution.",
            "effect": "The Q2 2024 incident resulted in a 180-day monitoring gap that required retroactive documentation. If a monitoring gap occurred during an active FinCEN examination period or for a high-priority subject, it could constitute a material program failure.",
            "recommendations": [
                "Configure the compliance case management system to automatically generate a monitoring task at 90-day intervals for all open SAR subjects, assigned to the case's lead analyst with escalation to the BSA Compliance Officer if not completed within 5 days of the due date.",
                "Conduct an immediate audit of all active SAR subjects to confirm that no current monitoring tasks have been missed.",
                "Implement a monthly open SAR monitoring report reviewed by the BSA Compliance Officer.",
            ],
            "owner":  "BSA/AML Compliance Officer / VP Information Technology",
            "target": "30 days (system configuration); Immediate (active subject audit)",
            "mgmt_response": "Management acknowledges the finding. An immediate audit of active SAR subjects will begin within 48 hours. System configuration is being scoped.",
        },
    ],
    "observations": [
        {
            "id":     "OBS-01",
            "title":  "Patron Bank Account Data Collected via Unencrypted Email",
            "risk":   "Medium",
            "detail": "Bank account information collected from vendors and certain patrons for payment and refund processing is transmitted via unencrypted email attachments (PDF forms). This was flagged as a data security concern in the 2023 internal audit. No corrective action has been implemented. This is a data privacy and PCI-adjacent risk that falls partially within the BSA team's document handling practices.",
            "recommendation": "Implement a secure document submission portal (SharePoint with access controls, or a secure file transfer solution) for any document containing patron financial account data. Discontinue collection of account data via standard email immediately.",
        },
    ],
}

# =============================================================================
# REPORT 5 — Fine Dining F&B Vendor Onboarding
# =============================================================================
REPORT_5 = {
    "title":       "Fine Dining Food & Beverage Vendor Onboarding",
    "out":         "05-Fine-Dining-FB-Vendor-Onboarding-Audit-Report.docx",
    "meta": {
        "AUDIT REFERENCE":    "WR-IA-2025-005",
        "Property":           "Wynn Las Vegas / Encore Las Vegas",
        "Department":         "Food & Beverage Procurement",
        "Process Owner":      "Director of F&B Procurement",
        "Audit Period":       "January – March 2025",
        "Report Date":        "March 25, 2025",
        "Classification":     "Operational",
    },
    "exec_summary": {
        "overall_rating": "Needs Improvement",
        "counts": {"Critical": 0, "High": 3, "Medium": 2, "Low": 0},
        "bullets": [
            "A vendor rejected in 2023 for failing food safety inspection was resubmitted and nearly approved by a different chef, because rejection history is not retained in the approved vendor list. A food safety incident resulting from an approved-but-unsafe vendor could carry significant reputational and regulatory consequences.",
            "Average onboarding cycle time is 22–35 days for standard vendors and 45–70 days for specialty vendors. For the relaunch of a flagship fine dining restaurant, one specialty vendor (caviar supplier) was still pending 11 days after opening, requiring a menu substitution.",
            "Bank account data is collected via unencrypted email PDF forms — a practice flagged by Internal Audit in 2023 that has not been remediated. An ACH routing error caused by a setup error resulted in $0 payments to a mushroom forager for 6 weeks and a 3-week supply disruption.",
            "All five review steps (legal, insurance, food safety, financial, Oracle setup) run sequentially despite having no technical dependencies on each other. Parallel execution would reduce cycle time by an estimated 8–12 business days.",
            "45% of vendor document submissions contain at least one error or omission requiring resubmission, driven by a paper-based PDF intake form with no validation.",
        ],
    },
    "scope":       "This audit reviewed the end-to-end F&B vendor onboarding process for fine dining venues at Wynn Las Vegas and Encore Las Vegas, from initial chef request through first approved purchase order. Existing vendor performance management, annual vendor reviews, beverage and alcohol purchasing (managed under a separate process), and operations at Wynn Macau and Encore Boston Harbor are out of scope.",
    "methodology": "Audit procedures included walkthrough of the onboarding process with the Director of F&B Procurement and two Procurement Coordinators, review of 25 vendor onboarding files completed in 2024 including the three restaurant opening cohorts, interview with three Executive Chefs and the Legal and Risk Management teams, review of the Q2 2024 restaurant opening incident documentation and the Q3 2024 ACH payment error investigation, and review of the 2023 internal audit finding on bank account data security.",
    "prior_findings": [
        {
            "ref": "WR-IA-2023-012",
            "title": "Patron/vendor bank account data collected via unencrypted email",
            "original_rating": "High",
            "status": "NOT REMEDIATED",
            "notes": "Recommendation issued 2023. No secure submission portal implemented as of report date.",
        },
    ],
    "findings": [
        {
            "id":    "FIND-01",
            "title": "Rejected Vendor History Not Retained — Food Safety Risk",
            "risk":  "High",
            "condition": "The approved vendor list is a static Excel spreadsheet that contains only currently approved vendors. Vendors rejected during onboarding — including those rejected for food safety failures, insurance non-compliance, or financial instability — are not retained in any accessible record. In Q1 2025, a produce vendor rejected in 2023 for failing a food safety inspection was resubmitted by a different chef at Encore Las Vegas. The coordinator who processed the original rejection had left. The vendor was nearly approved before a senior Procurement Manager recognized the company name and located the prior rejection in archived personal emails.",
            "criteria": "Vendor management best practice requires that rejection history, including the reason for rejection, be maintained in a permanent, searchable record. Food safety rejections in particular must be flagged for any future resubmission to prevent inadvertent approval of a non-compliant supplier.",
            "cause": "The approved vendor list was designed to reflect current approved suppliers only. No rejected vendor registry was established when the list was created. Institutional memory about rejected vendors resides with individual coordinators rather than in a system.",
            "effect": "A food safety incident caused by an inadvertently re-approved vendor could result in guest illness, regulatory action, reputational damage to Wynn's fine dining brand, and significant liability. The Q1 2025 near-miss was caught by institutional memory — a control that is not reliable as the organization grows and staff turns over.",
            "recommendations": [
                "Immediately create a rejected vendor registry as a separate tab or linked database in the vendor management system, capturing: vendor name, date of rejection, reason for rejection, and the name of the reviewer who made the determination.",
                "Update the onboarding intake process to require a mandatory check against the rejected vendor registry before opening a new onboarding file.",
                "For any vendor previously rejected for food safety reasons, require CCO and Director of F&B approval — in addition to standard review — before onboarding can proceed.",
                "Migrate vendor management from Excel to a structured database or procurement platform that supports vendor status history as a core feature.",
            ],
            "owner":  "Director of F&B Procurement",
            "target": "14 days (rejected registry); 90 days (platform migration planning)",
            "mgmt_response": "Management acknowledges the finding. A rejected vendor registry will be created within 14 days. All coordinators will be briefed on the mandatory pre-check requirement.",
        },
        {
            "id":    "FIND-02",
            "title": "Sequential Review Steps Add 8–12 Days to Onboarding Cycle",
            "risk":  "High",
            "condition": "Five review steps — legal contract review, insurance verification, food safety certification review, financial/credit check, and Oracle vendor setup — are executed sequentially by a single coordinator. Legal review does not begin until documents are confirmed complete; insurance review does not begin until legal completes. None of these steps have technical dependencies on each other. For the Q2 2024 flagship restaurant relaunch, a caviar supplier submitted all documents 6 weeks before opening but was still pending insurance documentation at day 11 post-opening because the insurance review had not been initiated until legal review was complete.",
            "criteria": "Process efficiency requires that independent review steps be executed in parallel. A 30-day onboarding cycle target is not achievable while running five independent steps sequentially. The industry benchmark for enterprise vendor onboarding is 14–21 days for standard vendors.",
            "cause": "The coordinator model assigns one person to manage all review steps for each vendor. Coordinating five parallel reviews is more complex than managing them sequentially, and no workflow system exists to support parallel tracking. The sequential approach is a coping mechanism, not a deliberate design.",
            "effect": "Average onboarding cycle time for specialty vendors is 45–70 days — 2–3x the target. The Q2 2024 restaurant opening was materially impacted by onboarding delays, resulting in 11 days of menu substitutions for a signature item. Each restaurant opening with pre-approved vendor requirements creates a deadline-sensitive parallel path that the current sequential model cannot reliably serve.",
            "recommendations": [
                "Redesign the onboarding workflow to initiate all five review steps simultaneously upon confirmation of document completeness, with each reviewer working in parallel.",
                "Implement a shared workflow tracker (recommended: Smartsheet or an enhanced SharePoint site) showing all five review statuses per vendor in a single view, visible to the coordinator, all reviewers, and the requesting chef.",
                "For restaurant openings, create a dedicated opening-critical vendor track with a designated project manager, weekly status reviews, and escalation to the Director if any review step is not completed within 10 days of initiation.",
                "Define maximum review SLAs for each step: Legal (5 business days standard; 3 for opening-critical), Insurance (2 days), Food Safety (2 days), Finance (3 days).",
            ],
            "owner":  "Director of F&B Procurement / VP Legal",
            "target": "45 days",
            "mgmt_response": "Management acknowledges the finding. A parallel review workflow will be designed and piloted for the next restaurant opening cohort.",
        },
        {
            "id":    "FIND-03",
            "title": "Vendor Bank Account Data Collected via Unencrypted Email — Not Remediated",
            "risk":  "High",
            "condition": "Bank account information required for Oracle vendor setup is collected via a PDF form sent and returned via standard unencrypted email. This practice was identified and flagged in the 2023 Internal Audit (WR-IA-2023-012) with a High risk rating. No corrective action has been implemented. In Q3 2024, an ACH routing number entered incorrectly from an emailed PDF form resulted in three invoices being processed to the wrong bank account. The error was undetected for 6 weeks, causing the vendor to stop fulfilling orders and creating a 3-week supply disruption at the affected restaurant.",
            "criteria": "PCI DSS guidance and Wynn's own data security policy require that financial account data be transmitted through encrypted, access-controlled channels. Personal email does not meet this standard. Additionally, this is a repeat finding from the 2023 audit with no remediation — escalation is required.",
            "cause": "No secure document submission portal has been implemented. The Oracle onboarding form was designed for email distribution before current security standards were established. The 2023 audit recommendation was not assigned an owner with a firm deadline.",
            "effect": "The Q3 2024 payment error caused a 3-week supply disruption and required personal intervention by an Executive Chef to repair the vendor relationship. Unencrypted transmission of bank account data exposes Wynn to data breach risk, potential regulatory penalties under applicable privacy laws, and reputational harm. This is a repeat finding — its continued presence after a prior High-rated recommendation reflects a gap in audit finding remediation governance.",
            "recommendations": [
                "Implement a secure vendor document submission portal — recommended: a SharePoint site with access controlled by invitation link, or a dedicated secure file transfer solution — within 30 days.",
                "Immediately cease collection of bank account data via standard email. All pending vendors in the pipeline must use the new portal before Oracle setup proceeds.",
                "Implement a two-person verification step for all new Oracle bank account entries: the coordinator enters the data, and a Finance AP team member independently verifies the account number against the original submission before the vendor is activated.",
                "Establish a formal audit finding remediation tracking process with assigned owners and mandatory status reporting to the Chief Audit Executive for all High-rated findings.",
            ],
            "owner":  "Director of F&B Procurement / VP Information Technology / Chief Audit Executive",
            "target": "30 days",
            "mgmt_response": "Management acknowledges the finding and the failure to remediate the 2023 recommendation. A secure portal will be implemented within 30 days. Two-person verification will begin immediately.",
        },
        {
            "id":    "FIND-04",
            "title": "Oracle Vendor Setup Initiated at End of Process",
            "risk":  "Medium",
            "condition": "The Oracle vendor master setup form — required before any purchase order can be placed — is sent to the vendor as the final step of the onboarding process, after all reviews are complete. The form requires bank account details and payment terms that could be collected earlier. Vendors frequently take 2–3 additional days to return the completed form. If the form contains errors (15% of setups contain at least one error), correction adds further delay. The Oracle setup step is effectively the last-mile bottleneck even for vendors who have completed all substantive reviews.",
            "criteria": "Process design should minimize unnecessary end-of-process delays. The Oracle vendor master form contains information (vendor name, address, tax ID, payment terms) that can be collected during the document intake phase, separating only the bank account fields pending secure collection infrastructure.",
            "cause": "The Oracle setup form was designed as a final administrative step. No one assessed whether portions of the form could be collected earlier in the process. The bank account security issue (FIND-03) creates a legitimate constraint on collecting those fields earlier, but all non-financial fields could be collected during intake.",
            "effect": "Oracle setup delays add 2–5 days to average cycle time for vendors who are otherwise fully approved. On the Oracle error rate of 15%, setup errors add a further 1–3 days for correction — often after the chef has already been notified the vendor is approved.",
            "recommendations": [
                "Split the Oracle vendor setup form: collect all non-financial fields (name, address, tax ID, payment terms preference, contact details) as part of the initial document intake package.",
                "Collect bank account fields separately via the secure portal recommended in FIND-03, initiated in parallel with legal and insurance review rather than at the end.",
                "Implement a pre-submission validation checklist for Oracle forms to catch the most common errors (missing routing number format, tax ID format) before submission to the AP team.",
            ],
            "owner":  "Director of F&B Procurement / Finance AP Manager",
            "target": "45 days",
            "mgmt_response": "Management acknowledges the finding. The Oracle form split will be designed in conjunction with the secure portal implementation.",
        },
        {
            "id":    "FIND-05",
            "title": "No Real-Time Vendor Pipeline Visibility for Requesting Chefs",
            "risk":  "Medium",
            "condition": "Once a chef submits a vendor request, they receive no visibility into the onboarding status until the coordinator proactively communicates — which occurs inconsistently. Chefs email or call coordinators to check status, consuming coordinator time and creating friction. More significantly, chefs with no visibility into pipeline status cannot plan menus, opening timelines, or supply alternatives when a vendor is delayed. During the Q2 2024 restaurant opening, chefs were not informed of the caviar vendor's insurance delay until Day 8 post-opening, having assumed the vendor was approved.",
            "criteria": "Internal service recipients should have access to the status of requests they have submitted, without requiring manual coordinator intervention to provide updates. This is a standard expectation in any modern procurement workflow.",
            "cause": "The current system — a coordinator-maintained Excel spreadsheet — has no mechanism to share real-time status with requesters. SharePoint or equivalent tools that would enable read-only status sharing have not been implemented.",
            "effect": "Lack of chef visibility delays contingency planning when vendors are held up. On the Q2 2024 opening, an 8-day notification lag meant the chef had no time to source an alternative product before the opening night menu had to be finalized. Earlier visibility would have allowed a planned substitution rather than an emergency one.",
            "recommendations": [
                "Implement a shared vendor pipeline tracker (SharePoint, Smartsheet, or similar) with a read-only chef view showing: vendor name, date submitted, current stage, any blocking issues, and estimated completion date.",
                "Configure automatic email notifications to the requesting chef when a vendor moves to a new stage, when a blocking issue is identified, and when the vendor is approved.",
                "Include vendor pipeline status in the weekly F&B operations meeting for all active restaurant opening cohorts.",
            ],
            "owner":  "Director of F&B Procurement",
            "target": "45 days",
            "mgmt_response": "Management acknowledges the finding. A shared pipeline tracker will be implemented as part of the broader workflow redesign.",
        },
    ],
    "observations": [
        {
            "id":     "OBS-01",
            "title":  "PDF Intake Form Driving 45% Resubmission Rate",
            "risk":   "Medium",
            "detail": "The vendor request form is a static PDF that chefs print, complete by hand or in Acrobat, and email to Procurement. Approximately 45% of submissions have at least one error or missing field requiring follow-up. The most common errors are: missing employment history sections, no signature, and incomplete product category descriptions. Each resubmission adds 3–5 days to the onboarding timeline.",
            "recommendation": "Replace the PDF intake form with a digital form (Microsoft Forms, Typeform, or equivalent) with required fields, dropdown menus for product categories, and automatic submission to the coordinator upon completion. This is a low-cost, high-impact change that can be implemented within 2 weeks.",
        },
        {
            "id":     "OBS-02",
            "title":  "Small Vendor Insurance Waiver Process Undocumented",
            "risk":   "Medium",
            "detail": "Approximately 30% of fine dining vendors — particularly small farms, foragers, and artisan producers — cannot meet Wynn's standard $2M general liability insurance requirement. Risk Management processes waivers for these vendors, but the waiver criteria, approval chain, and documentation requirements are not written down. Waiver decisions have been inconsistently applied and in one case a waiver was granted verbally without any documentation in the vendor file.",
            "recommendation": "Document the small vendor insurance waiver process: define eligibility criteria (vendor size, product type, transaction volume), required documentation, approval authority (Risk Management Director, with CFO sign-off above a defined threshold), and retention requirements. File the written policy in the approved vendor list and reference it in the onboarding coordinator SOP.",
        },
    ],
}

# =============================================================================
# Report renderer
# =============================================================================

ALL_REPORTS = [REPORT_1, REPORT_2, REPORT_3, REPORT_4, REPORT_5]


def build_report(data: dict, logo_bytes: bytes):
    doc = new_doc()
    set_margins(doc)

    add_letterhead(doc, logo_bytes, data["title"],
                   department="Internal Audit  |  Office of the Chief Audit Executive",
                   classification="STRICTLY CONFIDENTIAL")

    # Metadata box
    add_meta_box(doc, data["meta"])

    # Exec summary
    es = data["exec_summary"]
    add_exec_summary_block(doc, es["overall_rating"], es["counts"], es["bullets"])

    # Scope & methodology
    add_scope_methodology(doc, data["scope"], data["methodology"])

    # Prior findings
    add_prior_findings_table(doc, data.get("prior_findings", []))

    # Summary table
    add_findings_summary_table(doc, data["findings"])

    # Detailed findings
    add_heading(doc, "Detailed Findings", 1)
    for f in data["findings"]:
        add_finding_block(doc, f)

    # Observations
    if data.get("observations"):
        add_heading(doc, "Observations", 1)
        for o in data["observations"]:
            add_observation_block(doc, o)

    # Sign-off
    add_sign_off_block(doc, AUDIT_TEAM,
                       list(data["meta"].values())[:1] + [
                           "Chief Operating Officer",
                           "Chief Compliance Officer",
                           "VP Casino Operations",
                           "Board Audit Committee",
                       ],
                       data["meta"].get("Report Date", "March 25, 2025"))

    add_footer(doc, data["out"])
    return doc


def main():
    print("Downloading Wynn logo...")
    resp = requests.get(LOGO_URL, timeout=15)
    resp.raise_for_status()
    logo_bytes = resp.content
    print(f"  Logo: {len(logo_bytes):,} bytes")

    for report in ALL_REPORTS:
        out_path = os.path.join(OUT_DIR, report["out"])
        print(f"\nBuilding: {report['out']}")
        doc = build_report(report, logo_bytes)
        doc.save(out_path)
        print(f"  Saved -> {out_path}")

    print("\nAll 5 audit reports generated.")


if __name__ == "__main__":
    main()
