# Process Audit Intake: New Gaming Employee Licensing & Onboarding

---

## Section 1 — Process Identity

- **Process name:** New Gaming Employee Licensing & Onboarding (Nevada)
- **Process owner:** Director of Human Resources — Gaming Compliance
- **Frequency:** Ongoing. Wynn Las Vegas and Encore collectively hire approximately 80–120 new gaming employees per month (dealers, pit supervisors, cage agents, slot technicians, keno runners). Volume spikes ahead of major events and when new table game offerings launch.
- **How long in current form:** Core regulatory requirements set by Nevada Gaming Control Board (NGCB) and unchanged structurally; internal workflow last revised in 2021 when Wynn moved from a paper-based application system to a partially digitized one. Full digitization was not completed.
- **Why being audited now:** Time-to-floor (from accepted offer to first shift on the gaming floor) is averaging 47 days against a target of 30 days. Candidate attrition during the licensing process has increased — approximately 18% of accepted gaming offers are withdrawn before the candidate reaches the floor, with "slow process" cited in exit surveys as the top reason. Two competitors (MGM and Caesars) are reportedly achieving 28–32 day average times.

---

## Section 2 — Step-by-Step Process Map

| # | Step | Owner | System/Tool | Approx. Time | Manual/Auto | Decision Point? |
|---|---|---|---|---|---|---|
| 1 | Offer extended and accepted | Recruiter | Workday ATS | Day 0 | Semi-auto | — |
| 2 | Candidate directed to complete NGCB gaming license application (Form GCB-8) | HR Coordinator | Email instructions + NGCB online portal | 1–3 days (candidate-dependent) | Manual | — |
| 3 | HR Coordinator reviews application for completeness before submission | HR Coordinator | Manual review of printed or emailed form | 1–2 days | Manual | Incomplete forms returned to candidate — adds 3–5 days |
| 4 | Fingerprinting scheduled and completed (NGCB-approved vendor) | HR Coordinator + Candidate | Third-party scheduling system (no integration with Wynn systems) | Scheduling: 1–3 days; appointment: varies by vendor availability | Manual | — |
| 5 | Drug screening scheduled and completed | HR Coordinator + Candidate | Third-party vendor (separate from fingerprinting vendor) | 1–3 days scheduling; 1 day for results | Manual | Positive result = immediate disqualification |
| 6 | Background check initiated (separate from NGCB investigation) | HR Coordinator | Sterling Talent Solutions (third-party) | 3–7 business days | Semi-auto | Results reviewed by HR Compliance; escalations to Legal |
| 7 | NGCB investigates candidate and issues gaming work permit | NGCB (external) | NGCB internal system; Wynn has no visibility | 14–21 days (standard); up to 45 days for candidates with complex histories | External | If denied, candidate cannot work on gaming floor |
| 8 | Gaming work permit received and recorded | HR Coordinator | Scanned and emailed; filed in SharePoint | 1 day | Manual | — |
| 9 | I-9 and new hire paperwork completed | HR Coordinator | Workday | 1–2 days | Semi-auto | — |
| 10 | Uniform fitting and issuance | HR / Uniform Room | Spreadsheet-based inventory system | 1–2 days (scheduling dependent) | Manual | If uniform not in stock, order lead time is 5–10 days |
| 11 | Property access badge issued | Security | Lenel access control system | 1 day | Manual | Requires gaming work permit to be in file first |
| 12 | Table games or department-specific training | Training Department | In-person + LMS (Cornerstone) | 3–10 days depending on role | Manual | Must pass dealing proficiency test to advance |
| 13 | Schedule assigned; first shift confirmed | Scheduling / Floor Manager | Kronos | 1–2 days | Semi-auto | — |

**Exception handling at each step:**
- Step 3: No digital validation of form completeness before submission. Reviewer catches errors manually. Common errors: missing employment history gaps, incomplete residential history, unsigned sections.
- Step 4: Fingerprinting and drug screening use two different vendors. Candidates sometimes complete one and not the other, requiring follow-up. No unified scheduling or tracking.
- Step 7: Wynn has zero visibility into NGCB investigation status. HR Coordinators call the NGCB periodically to check status — there is no API or status portal. Candidates ask HR for updates; HR has no answer.
- Step 10: Uniform inventory is managed by the Uniform Room on a separate spreadsheet. HR does not have visibility into stock levels until the fitting appointment. Out-of-stock situations are discovered at the appointment, not before.
- Step 12: If a candidate fails the dealing proficiency test twice, there is no documented policy on next steps. In practice, some are given additional training time; some are let go. Inconsistent.

---

## Section 3 — Known Pain Points

- **The NGCB black box:** The single largest time sink and the one Wynn cannot control directly. The NGCB investigation takes 14–21 days as a baseline and there is no status visibility. This window is where most candidate attrition occurs — candidates accept competing offers while waiting.
- **Sequential scheduling of parallel steps:** Fingerprinting, drug screening, and background check can all run simultaneously, but coordinators often schedule them sequentially because tracking across three vendors with no integration is difficult. This adds 3–5 days unnecessarily.
- **Coordinator workload:** Each HR Coordinator manages 25–40 active candidates in the pipeline simultaneously with no unified tracking dashboard. Status is tracked in individual spreadsheets. When a coordinator is out, handoffs are done via email and things fall through.
- **The uniform bottleneck:** Uniform fittings are scheduled without checking stock first. Out-of-stock uniforms — particularly for less common sizes — add 5–10 days at the end of the process when the candidate is otherwise ready to start.
- **No candidate-facing visibility:** Candidates have no portal or status tracker. All communication is via email from their coordinator. Candidates in the NGCB window often feel they've been forgotten and accept other offers.

---

## Section 4 — Performance Baselines

- **Average time-to-floor:** 47 days (target: 30 days)
- **Candidate attrition during process:** ~18% of accepted gaming offers (up from ~9% in 2021)
- **Application error/return rate:** Approximately 35% of GCB-8 applications submitted by candidates have at least one error or missing section requiring correction
- **NGCB approval rate:** ~94% of submitted candidates receive work permits; ~6% are denied or withdraw during investigation
- **Uniform out-of-stock rate:** Approximately 22% of uniform fittings result in at least one item needing to be ordered
- **Training pass rate (first attempt):** ~78% pass dealing proficiency on first attempt; ~15% pass on second; ~7% do not pass

---

## Section 5 — Systems & Integrations

| System | Role in Process | Known Limitations / Workarounds |
|---|---|---|
| Workday | Offer management, I-9, new hire paperwork | Does not integrate with NGCB portal, fingerprinting vendor, or drug screening vendor. Onboarding checklist in Workday is not enforced — coordinators use it inconsistently. |
| NGCB Online Portal | Candidate submits GCB-8 application | No API. No status webhook. No employer-facing status dashboard. Wynn interacts with it only by submitting and then calling to follow up. |
| Sterling Talent Solutions | Background check | Results returned via Sterling portal (separate login). Not integrated with Workday. Results manually reviewed and filed. |
| Third-party fingerprinting vendor (Identix) | NGCB-required fingerprinting | Scheduling handled through vendor's own portal. No integration with Wynn systems. Completion confirmation sent via email. |
| Third-party drug screening vendor (Quest Diagnostics) | Pre-employment drug screen | Separate scheduling portal from fingerprinting. Results returned via Quest portal. Manual check required. |
| Cornerstone LMS | Training content and completion tracking | Used by Training Department. Not integrated with Workday onboarding checklist. Training completion does not automatically update HR systems. |
| Kronos | Scheduling | Cannot schedule an employee until all prior steps are complete and verified in Workday. Manual notification from HR to scheduling manager required. |
| Spreadsheet (HR Coordinator) | Pipeline tracking | Individual coordinator spreadsheets. No shared view. No alerts or SLA tracking. |

---

## Section 6 — Compliance & Control Context

- **Regulatory requirements:** Nevada Gaming Control Board Regulations require a valid gaming work permit before any employee may perform gaming duties. Allowing an employee to work on the gaming floor without a valid permit is a regulatory violation subject to fines and disciplinary action.
- **I-9 compliance:** Standard federal requirement; currently handled in Workday. No known gaps.
- **Drug screening:** Required pre-employment under Wynn's Internal Control Submission. Results must be retained for a minimum period.
- **Gaming work permit renewals:** Work permits require annual renewal. The renewal process is a separate workflow and is not in scope for this audit, but the onboarding system should be designed with renewal tracking in mind.
- **Prior compliance reviews:** One instance in 2023 where an employee began training (non-gaming floor) before their work permit was received — technically permissible but flagged by Gaming Compliance as a process risk. No regulatory action taken.
- **Segregation of duties:** HR Compliance reviews background check results separately from the recruiting team that extended the offer. Escalations go to Legal. This structure is sound.

---

## Section 7 — Recent Incidents or Near-Misses

**Incident 1 — Candidate attrition spike (Q2 2024)**
Following the opening of a new poker room expansion, Wynn initiated a hiring push for 40 new poker dealers. 28 accepted offers. By the time work permits were received, 9 of the 28 had accepted positions at competing properties. Three cited the wait time explicitly in their withdrawals. The poker room opened understaffed and ran reduced tables for the first three weeks.

**Incident 2 — Uniform stockout (Q3 2024)**
During a hiring push for 22 new baccarat dealers, 8 required a uniform size (men's 46L jacket) that was out of stock. Lead time from the uniform supplier was 12 days. The 8 dealers were ready to start in all other respects but could not be placed on the floor without complete uniforms (Wynn's standard). They were placed in paid waiting status for 12 days, costing approximately $14,400 in wages with no corresponding gaming floor contribution.

**Near-miss — Permit expiration oversight (Q1 2025)**
An annual work permit renewal was missed for one existing employee (not a new hire — discovered during an unrelated audit). The employee had worked for 19 days on an expired permit. Wynn self-reported to NGCB and received a notice of violation. Fine was minimal but the incident highlighted that the renewal tracking process is manual and subject to the same gaps as the onboarding tracking process.

---

## Section 8 — Audit Scope & Constraints

- **Out of scope:** Gaming work permit renewals (will be audited separately). Non-gaming employee onboarding (different regulatory requirements). Macau and Boston Harbor onboarding (different jurisdictions).
- **Appetite for change:** High. The attrition rate has direct financial and operational impact. HR leadership has budget approval to invest in tooling if ROI is demonstrated.
- **Regulatory constraint:** The NGCB investigation step cannot be shortened or modified by Wynn. However, Wynn can reduce the time candidates spend in the pre-submission steps, and can improve the experience during the waiting period to reduce attrition.
- **Technology constraint:** Full Workday integration with all vendors would require implementation effort. A lighter-weight candidate portal (status tracker) is considered feasible with existing tools and is the preferred near-term target.
