---
name: md-to-docx
description: Convert a markdown (.md) file to a professionally formatted Word document (.docx). Use whenever the user asks to create a Word doc, convert markdown to docx, or make a document "shareable." Handles headings, tables, bullet lists, bold/italic, blockquotes, and code blocks.
user-invocable: true
allowed-tools: Read, Write, Bash
---

# Markdown → Word Document Converter

Convert any `.md` file into a clean, professional `.docx` using python-docx.

## When to Use
- User says "make this a Word doc," "convert to docx," "create a shareable document"
- User has a `.md` file and needs a `.docx` version
- User asks you to generate a document and wants Word format

## How to Execute

### Step 1: Identify the Source
- If the user specifies a `.md` file, use that
- If the user points to content in chat, save as `.md` first, then convert
- Output `.docx` goes in the same directory as the source, with the same base name

### Step 2: Run the Converter
Use the Python conversion script at `${CLAUDE_SKILL_DIR}/md_to_docx.py`:

```bash
python "${CLAUDE_SKILL_DIR}/md_to_docx.py" "<input.md>" "<output.docx>"
```

If the script isn't available or fails, fall back to writing inline python-docx code.

### Step 3: Confirm
- Verify the file was created
- Report the output path to the user

## Formatting Standards

### Typography
- **Font:** Calibri throughout
- **Body text:** 11pt
- **Heading 1:** 16pt bold, dark blue (#003366)
- **Heading 2:** 14pt bold, dark blue
- **Heading 3:** 12pt bold, dark blue
- **Table text:** 10pt

### Layout
- **Margins:** 2.5cm left/right, 2cm top/bottom
- **Tables:** Use "Light Grid Accent 1" style, centered
- **Bullet lists:** Use built-in "List Bullet" style
- **Blockquotes:** Indent with left-border accent bar (via shading or indent)
- **Code blocks:** Use Consolas 9pt with light gray background

### Metadata
- If the markdown contains author/date/status in the header, render them centered below the title
- If a `---` separator appears after the title block, treat it as a visual break

## Markdown Parsing Rules
1. `# Heading` → Heading 1
2. `## Heading` → Heading 2
3. `### Heading` → Heading 3
4. `**bold**` → bold run
5. `*italic*` → italic run
6. `- item` or `* item` → bullet list
7. `| col | col |` → table (parse pipe-delimited tables)
8. `> quote` → blockquote (indented, styled)
9. `` ```code``` `` → code block (Consolas, gray background)
10. `---` → page break or horizontal rule (context-dependent)

## Dependencies
- `python-docx` (install with `python -m pip install python-docx` if missing)
