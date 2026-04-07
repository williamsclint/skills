# Process Audit Quick Checklist

Use this checklist to ensure comprehensive coverage before finalizing an audit.

## Scope Completeness
- [ ] All steps in the process are mapped end-to-end (not just the "happy path")
- [ ] Exception handling and edge cases are accounted for
- [ ] All roles and systems involved are identified
- [ ] Frequency/volume of the process is noted (daily, weekly, per-transaction)

## Bottleneck Check
- [ ] Checked for approval or review gates
- [ ] Checked for upstream dependency delays
- [ ] Checked for volume/capacity mismatches
- [ ] Checked for manual steps that could be parallelized

## SPOF Check
- [ ] Checked for single-person knowledge dependencies
- [ ] Checked for single-system dependencies with no fallback
- [ ] Checked for undocumented tribal knowledge
- [ ] Checked for steps with no backup coverage plan

## Handoff Check
- [ ] Every step has a clear owner
- [ ] Transitions between teams/systems are explicitly tracked
- [ ] SLAs or turnaround expectations exist for each handoff
- [ ] Escalation path is defined for delays or failures

## Compliance Check
- [ ] Audit trail exists for all material decisions
- [ ] No single person both initiates and approves the same transaction
- [ ] Data handling steps reviewed for privacy/regulatory alignment
- [ ] Exception handling is documented and authorized

## Automation Readiness
- [ ] Rule-based steps are clearly defined (yes/no logic)
- [ ] Data inputs are structured and consistent
- [ ] Volume justifies automation investment
- [ ] Tooling exists or is available to automate

## Recommendation Quality
- [ ] Each finding has a specific, actionable recommendation
- [ ] Recommendations are separated into quick wins vs. strategic fixes
- [ ] Priority matrix accounts for both impact and effort
- [ ] Owner(s) are suggested for each recommendation
