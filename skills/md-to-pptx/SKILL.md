---
name: md-to-pptx
description: Convert a markdown (.md) file to a professionally formatted PowerPoint presentation (.pptx). Use whenever the user asks to create a slide deck, convert markdown to slides, or make a presentation. Maps headings to slides, tables to formatted tables, and bullets to slide content.
user-invocable: true
allowed-tools: Read, Write, Bash
---

# Markdown → PowerPoint Converter

Convert any `.md` file into a clean, professional `.pptx` using python-pptx.

## When to Use
- User says "make this a slide deck," "convert to pptx," "create a presentation"
- User has a `.md` file and needs a `.pptx` version
- User asks you to generate a presentation from existing content

## How to Execute

### Step 1: Identify the Source
- If the user specifies a `.md` file, use that
- If the user points to content in chat, save as `.md` first, then convert
- Output `.pptx` goes in the same directory as the source, with the same base name

### Step 2: Run the Converter
Use the Python conversion script at `${CLAUDE_SKILL_DIR}/md_to_pptx.py`:

```bash
python "${CLAUDE_SKILL_DIR}/md_to_pptx.py" "<input.md>" "<output.pptx>"
```

If the script isn't available or fails, fall back to writing inline python-pptx code.

### Step 3: Confirm
- Verify the file was created
- Report the output path and slide count to the user

## Slide Mapping Rules

### Structure
- `# Title` → **Title slide** (dark blue background, white text, centered)
- `## Section` → **New content slide** (section becomes slide title)
- `### Subsection` → **New content slide** or subheading within current slide (use judgment based on content volume)
- Bullets under a heading → slide body content
- Tables under a heading → formatted table on slide
- Blockquotes → callout box with accent bar

### Slide Design Standards

#### Dimensions
- **Widescreen:** 13.333" × 7.5" (16:9)

#### Color Palette
| Name | Hex | Usage |
|------|-----|-------|
| Dark Blue | #003366 | Title backgrounds, heading text, table headers |
| Accent Blue | #0078D4 | Accent bars, card tops, highlights |
| White | #FFFFFF | Title slide text, card backgrounds |
| Light Gray | #F5F5F5 | Alternating table rows, card backgrounds |
| Dark Gray | #333333 | Body text |
| Medium Gray | #808080 | Descriptions, secondary text |

#### Typography
- **Font:** Calibri throughout
- **Title slide:** 42pt bold (title), 28pt (subtitle)
- **Slide titles:** 28pt bold, dark blue, with accent bar
- **Body text:** 16-18pt
- **Table text:** 12-13pt
- **Bullets:** Use Unicode bullet character (•) via XML buChar

#### Layout Patterns
- **Title slide:** Dark blue background, left-aligned, accent bar separator
- **Content slides:** White background, title at top with accent bar, content below
- **Section dividers:** Dark blue background (use for "Ask" / "Summary" type slides)
- **Tables:** Dark blue headers with white text, alternating light gray / white rows
- **Callout boxes:** Light gray background with left accent bar (blue)
- **Card layouts:** For 3-5 items, use equal-width cards in a row with accent-colored top borders

### Content Density
- **Max 6 bullets per slide** — if more, split across slides
- **Max 1 table per slide** — keep tables readable (5-6 rows max)
- **Prefer visual layouts** (cards, split columns) over text-heavy slides
- **Every slide should have whitespace** — don't pack content edge to edge

## Dependencies
- `python-pptx` (install with `python -m pip install python-pptx` if missing)
