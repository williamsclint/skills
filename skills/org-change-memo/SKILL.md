---
name: org-change-memo
description: Draft a change communication memo for an organizational change — reorg, leadership transition, team restructure, role elimination, process change, or policy update. Produces a clear, empathetic memo with context, rationale, what's changing, what's not, FAQ, and next steps.
argument-hint: "brief description of the change"
disable-model-invocation: true
---

Draft an organizational change communication memo based on the following:

**Change description:** $ARGUMENTS

If $ARGUMENTS is a file path, read that file first. If no arguments are provided, ask the user to describe the change before proceeding.

Before drafting, ask for any missing details that would materially affect the memo (see checklist below). If the user has provided enough context, proceed directly to drafting.

---

## Information to Gather (if not provided)

Ask for any of the following that are missing:
- What is changing? (structure, roles, leadership, process, policy)
- What is NOT changing? (often just as important for reducing anxiety)
- Why is this happening? (honest rationale — cost, strategy, growth, underperformance)
- Who is affected, and how? (specific teams, roles, or individuals)
- When does it take effect?
- Who is the author/sender of the memo? (CEO, COO, CHRO, manager)
- What is the audience? (all-company, specific team, managers only)
- Tone: formal/professional, warm/human, or matter-of-fact?
- Are there any sensitive elements to handle carefully? (layoffs, performance issues, legal constraints)

---

## Memo Structure

Draft the memo using this structure. Adapt tone and length to the audience and situation.

### [SUBJECT LINE]
Clear, specific, not vague. Examples:
- "Update on [Team Name] Structure — Effective [Date]"
- "Leadership Transition in [Department]"
- "Changes to [Process/Policy] — What You Need to Know"

### Opening (1–2 sentences)
State the change directly. Don't bury the lead or open with pleasantries.

### Background / Context (2–4 sentences)
Explain the environment or circumstances that led to this decision. This is where you earn trust by being honest about the "why."

### What Is Changing
Use bullet points or a short paragraph. Be specific. Name teams, roles, reporting lines, timelines.

### What Is NOT Changing
Explicitly list what stays the same. This is often the most important section for reducing rumor and anxiety.

### Why We're Making This Change
Honest, direct rationale. Avoid corporate speak ("synergies," "right-sizing"). If it's a hard decision, acknowledge it.

### What This Means for You
Segment by audience if needed (e.g., "For members of [Team A]..." / "For everyone else..."). State clearly what action, if any, is required.

### Timeline
Key dates and milestones. When does the change take effect? When will more information be shared?

### FAQ
Anticipate the 5–8 questions people will actually ask. Include uncomfortable ones. See faq-guide.md for common categories.

### Closing
Who to contact with questions. Reaffirm commitment. Keep it brief and genuine — not performative.

---

## Drafting Principles

Reference tone-guide.md for detailed guidance. Key principles:

1. **Lead with the news, not the framing.** People want to know what happened first.
2. **Be honest about hard decisions.** Euphemisms erode trust faster than the news itself.
3. **Address the emotional reality.** Acknowledge if this is disruptive or difficult.
4. **Separate facts from spin.** State what is true; don't oversell.
5. **Anticipate the skeptical reader.** Write for the person who is worried, not the person who is fine.
6. **One voice, one message.** The memo should be consistent with what managers will say in follow-up conversations.

---

## Output

Produce a ready-to-send memo draft. Then offer:
- An alternative subject line option
- A shorter version (for Slack/email preview)
- A list of follow-up talking points for managers

Save the output as `org-change-memo-[topic]-[date].md` if the user asks for it to be saved.
