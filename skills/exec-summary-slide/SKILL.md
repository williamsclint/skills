---
name: exec-summary-slide
description: Generate Clint's monthly Executive Summary slide for the ROB deck. Two-column layout — left side has flexible narrative sections (Highlights, Headwinds, etc.), right side has the FY engagement progress table from John Wheat's FDE/CAD deck. Uses WorkIQ to pre-populate content from M365 activity since last ROB. Use when Clint asks for his "exec summary," "ROB slide," "monthly update slide," or "executive overview."
user-invocable: true
allowed-tools: Read, Write, Bash, WorkIQ
---

# Executive Summary Slide Generator

Generate the monthly Executive Summary slide for Clint Williams's ROB (Rhythm of Business) deck.

## When to Use
- Clint asks for his "exec summary," "monthly update," "ROB slide," or "executive overview"
- Beginning of each month when preparing the monthly ROB deck
- Any time Clint needs to update his leadership on org status

## Scoping — What Belongs on This Slide

This slide represents **Clint Williams's direct org and owned workstreams only**. Apply these filters when curating WorkIQ results:

**IN scope:**
- Work Clint's team directly owns or drives (FDE, Depth, HPA, ACT engagements)
- Customer outcomes from engagements Clint's people ran or co-led
- Risks/blockers that directly impact Clint's deliverables or timelines
- Org changes *within* Clint's reporting chain (direct reports, their teams)
- Milestones and shipped work Clint is DRI or co-DRI for

**OUT of scope (do not include unless Clint adds them):**
- Org changes 3+ levels above Clint (e.g., BIC reorgs, CAPE Chief of Staff hires)
- Broader platform wins Clint's team didn't directly drive (e.g., Helix re-architecture)
- Generic program metrics Clint doesn't own (e.g., total CAD pipeline numbers without team attribution)
- Customer engagements owned entirely by peer teams
- Company-wide announcements, newsletters, or events unless Clint played a named role

**When in doubt:** Leave it out. Clint will add anything missing during the curation step.

## Workflow

### Phase 1: Gather Content via WorkIQ

Search M365 data for activity **since the last ROB deck** (approximately the past month). Ask Clint for the date of the last ROB if unclear.

**WorkIQ queries to run (parallel where possible):**

1. **Highlights / wins:**
   - "What are the recent wins, milestones, and accomplishments from Clint Williams's team (FDE, Depth, HPA) in the past month?"
   - "What customer engagements has Clint Williams's org progressed or delivered recently?"
   - Search for emails/Teams messages about: launches, shipped, published, milestone, kudos, win, success

2. **Headwinds / challenges:**
   - "What blockers, risks, or challenges has Clint Williams's team discussed in the past month?"
   - "Any resource constraints, timeline risks, or escalations discussed recently that affect Clint's org?"
   - Search for: blocked, risk, delay, concern, challenge, headwind, slow

3. **Engagement funnel data:**
   - "Find the most recent FDE/CAD update deck from John Wheat"
   - "What are the latest engagement funnel numbers for Depth and FDE teams?"
   - Look for: engagement progress, customer pipeline, envision/build/deploy/adopt counts

### Phase 2: Propose & Curate Bullets

**This is a mandatory human-in-the-loop step.** Do NOT skip it or go straight to the full draft.

After gathering WorkIQ data, **filter results through the scoping rules above**, then present proposed bullets as a numbered list for each section. Format:

```
## Proposed Highlights
1. [bullet text]
2. [bullet text]
3. [bullet text]
...

## Proposed Headwinds
1. [bullet text]
2. [bullet text]
3. [bullet text]
...
```

Then ask Clint:
> "Here are the proposed bullets from M365 activity. Tell me which numbers to keep, any edits, and any points you want to add. You can also suggest additional sections beyond Highlights/Headwinds (e.g., Asks, Focus Areas, Next Steps)."

**Wait for Clint's response.** He will:
- Confirm which numbered bullets to keep (e.g., "keep 1, 3, 5")
- Edit wording on specific bullets
- Add his own bullets that WorkIQ didn't surface
- Remove entire sections or add new ones
- Provide engagement funnel data if not found automatically

### Phase 3: Compile Final Draft

After Clint confirms the curated bullets, compile the **final draft** in chat:

```
## Final Draft — Executive Summary — [Month Year]

### Left Column

#### [Section 1 Title] (e.g., Highlights)
• [confirmed/edited bullet]
• [Clint's added bullet]
...

#### [Section 2 Title] (e.g., Headwinds)
• [confirmed/edited bullet]
...

### Right Column — FY Engagement Progress

| Team | Envision | Build | Deploy | Adopt | Total |
|------|----------|-------|--------|-------|-------|
| Depth | [names] | [names] | [names] | [names] | [count] |
| FDE | [names] | [names] | [names] | [names] | [count] |
| **WH Total** | [n] | [n] | [n] | [n] | **[N]** |
```

Ask for a **final confirmation** before generating. This is a quick "looks good" check, not another full edit round.

### Phase 4: Generate Slide

After Clint approves the final draft, generate the `.pptx` using the layout spec below.

**Output:** `Executive-Summary-[MonthYear].pptx` in the current working directory.

## Slide Layout Specification

### Dimensions
- **Widescreen:** 13.333" × 7.5" (16:9)

### Visual Theme
- **Left/right decorative borders:** Purple-to-blue gradient strips (~0.4" wide) on both edges
- **Background:** White center area
- **Footer:** "Classified as Microsoft Confidential" in small gray text, bottom-left

### Color Palette
| Name | Hex | Usage |
|------|-----|-------|
| Title Blue | #4472C4 | "Executive Summary" title, engagement table title |
| Section Blue | #2F5496 | Section subheadings (Highlights, Headwinds) |
| Body Black | #333333 | Bullet text, table content |
| Table Header BG | #D6E4F0 | Light blue header row background |
| Table Border | #8FAADC | Table cell borders |
| Gradient Purple | #7B68AE | Decorative border (left edge) |
| Gradient Blue | #5B9BD5 | Decorative border (right edge) |
| Footer Gray | #808080 | Confidential footer text |

### Typography
| Element | Font | Size | Style |
|---------|------|------|-------|
| "Executive Summary" | Calibri | 32pt | Bold, Title Blue |
| Section headings (Highlights, etc.) | Calibri | 22pt | Bold, Section Blue |
| Engagement table title | Calibri | 22pt | Bold, Title Blue |
| Bullet text (level 1) | Calibri | 12pt | Regular |
| Bullet text (level 2) | Calibri | 11pt | Regular |
| Bullet lead-in labels | Calibri | 12pt | Underlined + Bold |
| Table header text | Calibri | 11pt | Bold |
| Table body text | Calibri | 10pt | Regular |
| Team labels (Depth, FDE) | Calibri | 12pt | Bold |
| Total counts | Calibri | 14pt | Bold |
| Footer | Calibri | 8pt | Regular, gray |

### Two-Column Layout

**Left column** (x: 0.6" to 6.5", width: ~5.9"):
- "Executive Summary" title at top (~0.3" from top)
- Flexible sections below, each with:
  - Section subheading (bold, blue, slightly larger)
  - Bulleted content with support for:
    - Level 1 bullets (•)
    - Level 2 sub-bullets (•, indented)
    - **Underlined lead-in pattern:** `Lead-in:` text where the lead-in is underlined+bold and the rest is regular
- Sections stack vertically with ~0.3" gap between them

**Right column** (x: 6.8" to 12.8", width: ~6.0"):
- "FY[XX] Engagement Progress" title at top
- Table below with columns: Team | Envision | Build | Deploy | Adopt | Total
- Each cell contains a vertical list of customer names (one per line, small text)
- Team rows: Depth, FDE (or whatever teams are current)
- Bottom summary row: "WH Total" with numeric counts per stage and bold grand total
- Customer names flow in columns within each cell to fit

### Content Rules
- **Max ~8 level-1 bullets per section** to keep readable
- **Underlined lead-in labels** are used for notable items in the highlights (e.g., "Discovery refresh:", "Channel Mode:", "Evals:")
- **Right-side table** should auto-size row heights based on customer count
- If content overflows, reduce font size slightly (min 9pt) rather than clipping

## Data Sources
- **WorkIQ MCP** — M365 emails, meetings, documents, Teams messages, people
- **John Wheat's FDE/CAD update deck** — engagement funnel data (found via WorkIQ search)

## Dependencies
- `python-pptx` (install with `python -m pip install python-pptx` if missing)
- WorkIQ MCP server must be connected and authenticated

## Notes
- This is a **monthly** recurring artifact
- Sections on the left are **flexible** — not always Highlights + Headwinds. Clint may add Asks, Next Steps, Focus Areas, etc.
- Always draft in chat first, then generate after approval
- The engagement progress table structure (teams × stages) is stable for the foreseeable future but may evolve
