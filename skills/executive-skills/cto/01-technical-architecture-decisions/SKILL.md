# Technical Architecture Decision-Making

**Persona:** CTO / Head of IT
**Classification:** STRICTLY CONFIDENTIAL
**Department:** Office of the CTO | Enterprise Architecture

## Description
This skill supports the CTO in making high-quality, well-documented architectural decisions that are grounded in Wynn Resorts' current system landscape, technical debt profile, and long-term technology strategy. It synthesizes the system inventory, architecture decision records, and technical debt backlog to evaluate options, surface hidden dependencies, and produce Architecture Decision Records (ADRs) that are traceable and defensible. The skill ensures that major technical choices account for integration complexity, cost of ownership, and business criticality of affected systems.

## When to Use
- When a major platform selection or architectural change decision is pending (cloud migration, database modernization, API gateway selection)
- When a new technology investment is being evaluated and its integration impact on existing systems must be assessed
- When the CTO must present an architectural recommendation to the CEO, board, or investment committee
- When a system is approaching end-of-life and a succession decision needs structured analysis
- When accumulated technical debt threatens delivery velocity or security posture and a remediation strategy must be sequenced

## Input Files Expected
| # | Document Name | Purpose |
|---|---------------|---------|
| 1 | Enterprise Technology System Inventory & Architecture Overview | Maps all production systems, their hosting models, costs, end-of-life dates, and integration counts to reveal dependencies and constraints |
| 2 | Architecture Decision Record Log (FY2023–FY2025) | Provides precedent decisions, rationale, and outcomes to ensure consistency and avoid repeating past mistakes |
| 3 | Technical Debt Backlog Assessment (Q1 2025) | Identifies which systems carry the heaviest remediation burden, enabling architecture decisions to account for debt exposure |

## Output
A structured Architecture Decision Record (ADR) including: problem statement and decision context, options considered with pros/cons and cost/timeline estimates, recommended option with rationale, alternatives rejected and reasons, implications for existing systems (integration impact, debt creation/reduction), and a review/revisit date. Also includes a one-page CTO briefing summary for executive communication.

## Example Prompt
> "We're deciding whether to migrate our property management system from the on-premise Oracle OPERA environment to a cloud-native SaaS platform. Use the system inventory, past ADRs, and the technical debt backlog to help me build the decision record and recommend an approach."
