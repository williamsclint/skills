# Process Audit Intake: Gaming Table Chip Fill & Credit Process

---

## Section 1 — Process Identity

- **Process name:** Gaming Table Chip Fill & Credit (Table Inventory Replenishment)
- **Process owner:** Cage Manager / Shift Manager, Casino Operations
- **Frequency:** Continuous during gaming operations (~18–22 hours/day). Fill requests occur approximately 400–600 times per 24-hour period across all table games at Wynn Las Vegas and Encore combined.
- **Volume:** Each fill averages $15K–$80K in chip value. On peak nights (New Year's Eve, major boxing events, Formula 1 weekend), volume spikes 3–4x normal.
- **How long in current form:** Core process governed by NGCB Regulation 12; fundamental structure unchanged for decades. Internal workflow last updated in 2019 when a new pit management system was partially introduced.
- **Why being audited now:** Two back-to-back busy weekends (Formula 1 2024, New Year's Eve 2024) exposed significant delays in fill fulfillment — dealers were idle at tables waiting for chips, resulting in lost gaming revenue estimated at $200K–$400K over those two events. Separately, surveillance flagged an irregularity in a fill documentation sequence that required a 6-hour internal investigation to resolve.

---

## Section 2 — Step-by-Step Process Map

| # | Step | Owner | System/Tool | Approx. Time | Manual/Auto | Decision Point? |
|---|---|---|---|---|---|---|
| 1 | Pit supervisor observes table chip inventory below threshold | Pit Supervisor | Visual observation | Continuous | Manual | — |
| 2 | Pit supervisor calls or radios cage to request fill | Pit Supervisor | Radio / phone | 2–5 min | Manual | Supervisor determines amount needed (judgment call) |
| 3 | Cage prepares fill — counts and bags requested chip denominations | Cage Agent | Physical chip count | 5–15 min | Manual | — |
| 4 | Fill slip generated (3-part form: cage copy, pit copy, soft count copy) | Cage Agent | CMS — Aristocrat cage module | 3–5 min | Semi-auto | — |
| 5 | Security officer escorts chip carrier from cage to table | Security / Cage Runner | Physical escort | 3–10 min (varies by distance) | Manual | — |
| 6 | Chips and fill slip presented to pit supervisor at table | Cage Runner | Physical | 1 min | Manual | — |
| 7 | Pit supervisor verifies chip count at table, signs fill slip | Pit Supervisor | Visual count + physical signature | 3–5 min | Manual | If count discrepancy, halt and call supervisor |
| 8 | Dealer spreads chips for camera verification, inserts into tray | Dealer | Physical | 1–2 min | Manual | Surveillance must have clear camera view |
| 9 | Surveillance logs fill in surveillance system | Surveillance Operator | Surveillance management system | 2–3 min | Manual | — |
| 10 | Signed fill slip returned to cage; cage copy filed | Cage Agent | Physical filing | End of shift | Manual | — |
| 11 | All fills reconciled against opening/closing table inventory count | Soft Count Team | CMS + physical count | End of shift | Manual | Discrepancies escalated to Cage Manager |

**Exception handling at each step:**
- Step 2: No formal threshold triggers the fill request — it is entirely the pit supervisor's judgment. Different supervisors call fills at different levels, creating inconsistency.
- Step 3: During peak periods, the cage has one fill window. If multiple pit supervisors call fills simultaneously, requests queue verbally with no tracking system.
- Step 5: Security escort distance varies significantly — some tables are 90 seconds from the cage; some high-limit rooms are 8+ minutes away.
- Step 7: If pit supervisor is occupied with a player dispute or comp request, the cage runner must wait at the table with the chips, holding up the escort and the cage.
- Step 8: Camera angle issues at certain tables (particularly older pit layouts) require the dealer to reposition chips multiple times for a clean surveillance view. This is a known issue that has not been structurally resolved.
- Step 9: Surveillance logging is manual and relies on the operator noticing the fill on camera. During high-volume periods, fills can be missed in the log, requiring retroactive reconciliation from CMS.

---

## Section 3 — Known Pain Points

- **The queue problem during peaks:** There is no queuing or ticketing system for fill requests. During Formula 1 weekend, the cage received 14 simultaneous fill requests at one point. Pit supervisors were calling the cage repeatedly to check status. The cage team was working from memory and handwritten notes. At least two fills were prepared out of priority order.
- **The escort bottleneck:** Security staffing for fills is based on average volume, not peak volume. During special events, the security team is also supporting crowd management, VIP arrivals, and perimeter coverage. Fill escorts are deprioritized. On New Year's Eve 2024, average escort wait time was estimated at 18–22 minutes vs. a normal 5–8 minutes.
- **Surveillance logging lag:** The surveillance team logs fills manually while also monitoring all other floor activity. During peaks, fills get logged in batches rather than real-time, which creates a documentation sequencing problem if a discrepancy occurs mid-shift.
- **No demand forecasting:** Fill frequency is not modeled against expected gaming volume. Cage staffing, chip inventory levels per table, and security escort staffing are set based on standard weekday/weekend levels. Event-specific scaling is informal and ad hoc.
- **Chip inventory visibility:** There is no real-time visibility into chip levels across all tables. The pit supervisor walks the pit to assess. On a 20-table pit, a supervisor may not notice a low table until a dealer flags it.

---

## Section 4 — Performance Baselines

- **Average fill cycle time (request to chips in tray):** 12–18 minutes on normal nights; 25–45 minutes during peak events
- **Target/SLA:** NGCB requires fills be documented accurately; there is no regulatory SLA on speed. Internal service expectation is "under 15 minutes" but this is not formally tracked.
- **Fill request volume — normal night:** 400–600 fills per 24-hour period
- **Fill request volume — peak event:** 1,200–1,800 fills per 24-hour period
- **Discrepancy rate:** Approximately 0.3% of fills result in a count discrepancy requiring investigation. During peak events this rises to approximately 1.1%.
- **Revenue impact of delays (estimated):** $200K–$400K in lost table time during the two events that triggered this audit (idle tables, players leaving)

---

## Section 5 — Systems & Integrations

| System | Role in Process | Known Limitations / Workarounds |
|---|---|---|
| Aristocrat CMS (cage module) | Generates fill slips, records fill transactions | No queuing or prioritization feature. Cannot display real-time fill request status to cage or pit. Fill slips are generated one at a time. |
| Pit management system (2019 partial deployment) | Was intended to allow digital fill requests from pit supervisor terminals | Only deployed in two of six pit areas. Supervisors in undeployed areas still use radio/phone. The two deployed areas use it inconsistently. |
| Surveillance management system | Logs fill events with timestamp and camera reference | Manual entry by operator. No integration with CMS — surveillance logs and CMS fill records must be manually matched during reconciliation. |
| Radio system | Primary communication between pit and cage for fill requests | Shared channel with security and floor management. During peaks, fill requests compete with other communications. A dedicated fill channel was proposed in 2023 but not implemented. |
| Physical fill slips (3-part paper) | Regulatory documentation of each fill | Cannot be digitized without NGCB approval for process change. Paper forms are a permanent fixture of the process. |

---

## Section 6 — Compliance & Control Context

- **Regulatory requirements:** NGCB Regulation 12 (Table Game Fill and Credit Procedures) mandates specific documentation, dual verification, and surveillance coverage for every fill. Any deviation is a potential regulatory violation. The paper fill slip process is codified in Wynn's Internal Control Submission (ICS) filed with the NGCB — changes require a formal ICS amendment and NGCB approval.
- **Dual control requirement:** Every fill must be physically verified by both the cage runner and the pit supervisor. This cannot be eliminated or shortened.
- **Surveillance requirement:** Camera coverage of the fill at the table is mandatory. The camera angle issues at certain tables are a compliance risk — if a fill is not clearly captured, the documentation is incomplete.
- **Existing audit trail:** Paper fill slips + CMS records + surveillance logs. The three-system reconciliation is manual and time-consuming.
- **Prior compliance reviews:** NGCB routine examination in 2023 noted the surveillance logging lag as an observation (not a finding). Wynn committed to exploring a more integrated logging solution. No structural change implemented.
- **Segregation of duties:** Strong. The cage prepares, security transports, the pit supervisor verifies, and surveillance records independently. The dual-control structure is sound.

---

## Section 7 — Recent Incidents or Near-Misses

**Incident 1 — Surveillance irregularity flag (Q4 2024)**
During post-event reconciliation after Formula 1 weekend, surveillance identified a fill slip in the CMS that did not have a corresponding surveillance log entry within the expected time window. The fill slip was properly signed. A 6-hour investigation traced the gap to a surveillance operator who had batched several fill log entries at the end of a surveillance rotation and entered an incorrect timestamp on one. No chip discrepancy. No theft. However, the investigation consumed significant management time and created uncertainty for several hours about whether a regulatory report was required.

**Incident 2 — Revenue loss from fill delays (New Year's Eve 2024)**
During the peak window (10pm–2am), three high-limit baccarat tables were effectively idle for a combined 47 minutes waiting for fills. Two tables had a minimum bet of $10,000. One high-value patron ($2M+ ADT) left the floor and did not return, citing frustration. The estimated lost gaming revenue from table downtime and patron departure was reported to the COO.

**Near-miss — Chip count discrepancy (Q3 2024)**
A fill arrived at a table short by $5,000 in $100 chips (50 chips). The pit supervisor caught the discrepancy at Step 7. Investigation revealed a cage agent had miscounted during preparation — the chips were found on the cage counter. Resolution took 35 minutes during which the table was closed. The root cause was a cage agent working alone during a shift gap (second cage agent called out sick, no backfill was called in).

---

## Section 8 — Audit Scope & Constraints

- **Out of scope:** The soft count process (end-of-shift chip reconciliation) is a separate audit. Table game opening/closing inventory counts are out of scope.
- **Regulatory constraint:** The paper fill slip and dual-control verification steps cannot be eliminated without an ICS amendment and NGCB approval. Any recommendations that touch these steps must be framed as "ICS amendment candidates" with a realistic timeline of 6–18 months for regulatory approval.
- **Appetite for change:** High. The revenue impact from the two peak events has executive attention. There is appetite for both near-term operational improvements and longer-term system changes.
- **Technology constraint:** Any integration between the pit management system and CMS requires Aristocrat involvement. A lighter-weight solution (tablet-based fill request queue visible to cage and pit simultaneously) has been informally discussed and is considered feasible without a full CMS change.
