---
name: wynn-doc-format
description: Apply Wynn Resorts corporate document formatting standards when generating .docx files. Use whenever creating an official Wynn document — audit reports, memos, board packs, executive summaries, or any document intended for internal or external distribution under the Wynn brand. References the shared Python utility library at wynn_doc_utils.py.
user-invocable: false
allowed-tools: Read, Write, Bash
---

When generating a Wynn-branded .docx document, apply the following standards. The shared Python utility library is at `${CLAUDE_SKILL_DIR}/wynn_doc_utils.py` — import it for all document generation tasks.

---

## Brand Standards

### Colors
| Name | Hex | Usage |
|---|---|---|
| Wynn Gold | #B89655 | Accent rules, header elements, callout borders |
| Dark Navy | #1A1A2E | Headings, table headers, primary text blocks |
| Body Text | #1A1A1A | Standard body copy |
| Mid Grey | #6B6B6B | Subheadings, captions, footer text |
| Light Grey | #F5F5F5 | Alternating table row fill |
| White | #FFFFFF | Alternating table row fill, backgrounds |
| Alert Red | #C0392B | CONFIDENTIAL label, Critical risk ratings |
| Alert Orange | #E67E22 | High risk ratings |
| Alert Amber | #F39C12 | Medium risk ratings |
| Alert Green | #27AE60 | Low risk ratings |

### Typography
- **Primary font:** Garamond (headings and body)
- **Heading 1:** Garamond 15pt Bold, Dark Navy, with 2pt Gold rule below
- **Heading 2:** Garamond 12pt Bold, Dark Navy, with 1pt Grey rule below
- **Heading 3:** Garamond 11pt Bold Italic, Dark Navy
- **Body:** Garamond 10pt, Body Text color
- **Table header:** Garamond 9pt Bold, White on Dark Navy
- **Table body:** Garamond 9pt, Body Text, alternating Light Grey / White rows
- **Footer:** Garamond 7.5pt Italic, Mid Grey

### Margins
- Top: 0.85 in, Bottom: 0.85 in, Left: 1.0 in, Right: 1.0 in

---

## Letterhead Structure

Every Wynn document opens with:

1. **Gold accent bar** — full-width, 0.35cm height, hex #B89655
2. **Two-column header table:**
   - Left (2.0 in): Wynn logo at 1.7 in width
   - Right (5.5 in): "WYNN RESORTS" in 9pt Gold Bold, department line in 8pt Grey Italic, classification label (e.g., CONFIDENTIAL) in 7.5pt Red Bold
3. **2pt Gold horizontal rule**
4. **Document title block:** Document type label in 9pt Grey Bold, document title in 18pt Navy Bold

---

## Document Classification Labels

Use one of the following on every document:
- `CONFIDENTIAL` — Internal documents not for external distribution
- `STRICTLY CONFIDENTIAL` — Audit reports, legal matters, board materials
- `INTERNAL USE ONLY` — Standard operational documents
- `PRIVILEGED & CONFIDENTIAL` — Legal or attorney-client privileged materials

---

## Table Standards

- All tables use "Table Grid" style
- Header row: Dark Navy fill (#1A1A2E), White 9pt Bold text, centered
- Data rows: Alternating #F5F5F5 / #FFFFFF
- Text: 9pt Garamond, Body Text color

---

## Footer Standard

Every page footer:
`[Company Name] | [Classification] | [Filename] | Do not distribute without authorization`

---

## Risk Rating Colors (for Audit Documents)

| Rating | Background Hex | Text |
|---|---|---|
| CRITICAL | #C0392B | White Bold |
| HIGH | #E67E22 | White Bold |
| MEDIUM | #F39C12 | White Bold |
| LOW | #27AE60 | White Bold |

---

## Using the Utility Library

```python
import sys
sys.path.insert(0, r"C:\Users\clwillia\.claude\skills\wynn-doc-format")
from wynn_doc_utils import (
    new_doc, add_letterhead, add_footer, set_margins,
    add_heading, add_body, add_bullet, add_horizontal_rule,
    add_markdown_table, add_meta_box,
    add_risk_badge, add_finding_block, add_observation_block,
    add_findings_summary_table, add_exec_summary_block, add_sign_off_block
)
```

All functions are documented inline in `wynn_doc_utils.py`.
