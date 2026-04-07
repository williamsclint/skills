---
name: process-audit
description: Conduct a structured process audit to identify bottlenecks, single points of failure, handoff gaps, compliance risks, and automation candidates. Produces a formal audit report with risk-rated findings, root cause analysis, recommendations, management response placeholders, and a sign-off block. Use when reviewing an operational workflow, approval chain, onboarding process, or recurring business procedure. Output follows Wynn Resorts document formatting standards (see wynn-doc-format skill).
argument-hint: "process name, description, or path to intake document"
---

Conduct a formal process audit based on the following input:

**Process to audit:** $ARGUMENTS

If $ARGUMENTS is a file path, read that file first. If it's a description, work from that. If no input is provided, ask the user to describe the process before proceeding.

Use `audit-checklist.md` to verify completeness before finalizing findings.

---

## Audit Report Structure

Produce a formal audit report with the following sections, in order:

---

### 1. Document Metadata

Present as a key-value table:
- Audit Reference Number (format: WR-IA-YYYY-NNN)
- Property / Business Unit
- Department / Process Owner
- Audit Period
- Report Date
- Audit Classification (Operational / Compliance / Financial / IT)
- Distribution (list of roles)

---

### 2. Executive Summary

**Overall Rating** — assign one of:
- **Satisfactory**: Controls are adequate with minor exceptions
- **Needs Improvement**: Material control gaps requiring remediation
- **Unsatisfactory**: Significant failures requiring immediate action

**Finding Count Summary** — table of: Critical / High / Medium / Low counts

**Key Findings** — 4–6 bullets summarizing the most important findings for an executive reader. Quantify impact where possible.

---

### 3. Audit Scope & Methodology

One paragraph each for:
- **Scope**: What was reviewed, what was explicitly out of scope
- **Methodology**: Evidence reviewed (document review, interviews, system testing, process observation, transaction testing)

---

### 4. Summary of Findings Table

Table with columns: Finding ID | Title | Risk Rating | Owner | Target Date

---

### 5. Detailed Findings

For each finding, structure as:

**Finding ID and Title** (e.g., FIND-01: Cross-Property Credit Visibility Gap)
**Risk Rating**: CRITICAL / HIGH / MEDIUM / LOW

| Field | Content |
|---|---|
| **CONDITION** | What was observed — specific, factual, referenced to evidence |
| **CRITERIA** | The standard, policy, or expectation that was not met |
| **CAUSE** | Root cause — why the gap exists |
| **EFFECT** | Actual or potential impact — quantify in dollars, time, or regulatory exposure where possible |

**Recommendations** (3–5 specific, actionable steps)

**Responsible Owner** | **Target Date** | **Management Response** (placeholder)

---

### 6. Observations

Lower-severity items that do not rise to the level of a formal finding. Use the same structure but abbreviated — no condition/criteria/cause/effect grid. One paragraph per observation, with a single recommendation.

---

### 7. Prior Audit Findings — Status Update

Table showing any prior findings relevant to this process and their current remediation status. If this is a first-time audit of the process, note that explicitly.

---

### 8. Sign-Off Block

Table for: Lead Auditor | Audit Manager | Chief Audit Executive — with signature lines and date.

Distribution list.

Standard disclaimer.

---

## Drafting Standards

- **Be specific**: Name systems, roles, dollar amounts, timelines. Generic observations are not useful.
- **Quantify impact**: Every High and Critical finding should have a quantified or estimated impact.
- **Root cause, not symptom**: The Cause field should identify why the gap exists, not restate the condition.
- **Actionable recommendations**: Each recommendation should be specific enough to be assigned to an owner with a due date.
- **Calibrate risk ratings**:
  - CRITICAL: Regulatory violation, material financial loss, or imminent operational failure
  - HIGH: Significant control gap with clear risk of material impact
  - MEDIUM: Control weakness requiring remediation but not posing immediate material risk
  - LOW: Minor gap or efficiency improvement opportunity

---

## Output Format

Deliver the audit report as a formatted document. If the user requests a `.docx` file, reference the `wynn-doc-format` skill and use `wynn_doc_utils.py` to generate a properly branded document.

Save output as `audit-report-[process-name]-[date].md` (or `.docx`) if the user requests it.
