# Template System Documentation

This folder contains a complete presentation template system with 52 self-documenting HTML files that can be used as starting points for creating new slides.

## File Structure

```
300-templates/
├── 100-basic.html                  # Universal starter template
├── 200-light/                      # 26 light-theme templates
│   ├── 001-design-system.html      # Light theme guide & colour palette reference
│   ├── 010-classic-title.html      # through
│   └── 250-full-bleed-solid.html   # Classic title to full-bleed (25 patterns)
├── 300-dark/                       # 26 dark-theme templates
│   ├── 001-design-system.html      # Dark theme guide & colour palette reference
│   ├── 010-classic-title.html      # through
│   └── 250-full-bleed-solid.html   # (same 25 patterns, dark version)
└── TEMPLATE-SYSTEM.md              # This file
```

## Template Metadata

**Every template file (51 total) includes a TEMPLATE METADATA comment block** at the top that documents:

- **Name**: Layout type and template purpose
- **Layout**: Description of structure (e.g., "Two-column", "Centred title with divider")
- **Colour Theme**: Hex codes for background, text, and accent colours
- **Typography**: Font stack and sizing information
- **Use Cases**: When to use this template
- **Customization**: How to adapt it for your needs
- **Accent Colour**: Primary accent hex code(s)
- **Responsive**: How the layout adapts to different screen sizes

### Example Metadata:

```html
<!--
TEMPLATE METADATA:
Name: Three Columns / Pillars Layout
Layout: Three equal-width cards in a responsive grid
Light Theme: background #ffffff, card bg #f8fafc, accent #f97316 (orange)
Typography: system-ui; card title 1.2rem weight 700; icon emoji 3.2rem
Use Cases: Feature highlights, capability showcase
Customization: Replace emoji, update titles and descriptions
Accent Colour: #f97316 (orange) in card title underlines
Responsive: Grid auto-fits: 3 cols desktop, 1 on mobile
-->
```

## How to Create New Slides

### Step 1: Choose a Template

Review the 25 layout patterns available:

| #   | Light            | Dark             | Description                            |
| --- | ---------------- | ---------------- | -------------------------------------- |
| 001 | Design System    | Design System    | Reference guide with colour palette    |
| 010 | Classic Title    | Classic Title    | Centred title with eyebrow and divider |
| 020 | Title + Body     | Title + Body     | Title with rule, content below         |
| 030 | Split Diagram    | Split Diagram    | Left image, right text                 |
| 040 | Image Focus      | Image Focus      | Full-screen image with caption         |
| 050 | Three Columns    | Three Columns    | Three-card grid (pillars)              |
| 060 | Big Quote        | Big Quote        | Large quote with attribution           |
| 070 | Stats Numbers    | Stats Numbers    | Grid of key metrics                    |
| 080 | Section Header   | Section Header   | Minimal section divider                |
| 090 | Agenda           | Agenda           | Numbered checklist                     |
| 100 | Comparison       | Comparison       | Two-column contrast                    |
| 110 | Timeline         | Timeline         | Vertical or horizontal milestones      |
| 120 | Code Snippet     | Code Snippet     | Syntax-highlighted code block          |
| 130 | Image Overlay    | Image Overlay    | Image with text overlay                |
| 140 | 2×2 Grid         | 2×2 Grid         | Four-card grid                         |
| 150 | Consulting Style | Consulting Style | Split panel with accent bar            |
| 160 | Bold Statement   | Bold Statement   | Large text with accent line            |
| 170 | Data Table       | Data Table       | Structured table with header           |
| 180 | Band Split       | Band Split       | Horizontal two-band layout             |
| 190 | Sidebar          | Sidebar          | Coloured sidebar + main content        |
| 200 | Gradient/Glass   | Gradient/Glass   | Gradient BG + frosted overlay          |
| 210 | Diagonal Split   | Diagonal Split   | Diagonal division of space             |
| 220 | Top Accent       | Top Accent       | Coloured top band + content            |
| 230 | Minimal Type     | Minimal Type     | Zen aesthetic, text-focused            |
| 240 | Pyramid          | Pyramid          | Hierarchical tiers                     |
| 250 | Full Bleed       | Full Bleed       | Single solid colour, full screen       |

### Step 2: Copy the Template

```bash
# Copy from light theme (for light presentations)
cp 300-templates/200-light/050-three-column.html my-slides/slide05.html

# OR copy from dark theme (for dark presentations)
cp 300-templates/300-dark/050-three-column.html my-slides/slide05.html
```

### Step 3: Update Content

Open the copied file and:

1. Replace title, headings, and body text
2. Update the `<aside class="notes">...</aside>` section with speaker notes
3. Keep CSS unchanged unless you need customisation

### Step 4: Optional Customisation

To change accent colours or background:

1. Open the `<style>` section in your template
2. Find colour hex codes (documented in the metadata comment)
3. Replace hex values (e.g., `#f97316` → `#2563eb`) for different accents
4. CSS Variables are pre-defined for common properties like accent and background

### Step 5: Test in Viewer

Open the slide in [100-viewer.html](../100-viewer.html) by selecting your slide folder and confirming the slide renders correctly.

## Design System Reference

### Light Theme Colour Palette

| Usage          | Hex       | Name      |
| -------------- | --------- | --------- |
| Background     | `#ffffff` | White     |
| Text Primary   | `#1e293b` | Slate 900 |
| Text Secondary | `#64748b` | Slate 500 |
| Accent Primary | `#2563eb` | Blue 600  |
| Accent Teal    | `#06b6d4` | Cyan 500  |
| Accent Amber   | `#d97706` | Amber 600 |
| Border/Divider | `#e2e8f0` | Slate 200 |

**Use these colours consistently** when creating new templates or variations.

### Dark Theme Colour Palette

| Usage          | Hex       | Name      |
| -------------- | --------- | --------- |
| Background     | `#0f172a` | Navy 900  |
| Text Primary   | `#f1f5f9` | Slate 100 |
| Text Secondary | `#94a3b8` | Slate 400 |
| Accent Cyan    | `#06b6d4` | Cyan 500  |
| Accent Light   | `#22d3ee` | Cyan 300  |
| Accent Green   | `#4ade80` | Green 400 |
| Border/Divider | `#1e293b` | Slate 800 |

### Typography System

All templates use `system-ui` font stack for cross-platform compatibility:

```css
font-family:
  system-ui,
  -apple-system,
  BlinkMacSystemFont,
  "Segoe UI",
  sans-serif;
```

**Common Sizing:**

- **H1 / Titles**: `clamp(2rem, 5vw, 3.8rem)` weight 800
- **H2 / Headings**: `1.1–2rem` weight 700
- **Body Text**: `0.95–1.1rem` weight 400–500, line-height 1.6–1.8
- **Labels**: `0.75–0.9rem` weight 600–700, uppercase, letter-spaced

### Responsive Design Patterns

All templates include responsive CSS using:

1. **CSS Grid with `auto-fit`**: Cards reflow automatically based on viewport
2. **Flexbox**: Stacks content vertically on mobile, horizontally on desktop
3. **`clamp()` for Typography**: Text scales fluidly between min–max sizes
4. **Media Queries**: Breakpoint at 768px for mobile/tablet/desktop transitions

## Creating Your Own Template

To create a new template pattern:

1. **Start from 100-basic.html** or an existing template
2. **Design the layout** using flexbox or CSS grid
3. **Choose or define your colour palette** (see guides in 001-design-system.html)
4. **Add TEMPLATE METADATA comment** at the top (copy the format from any template)
5. **Include speaker notes**: `<aside class="notes">...</aside>`
6. **Test responsive design** on mobile, tablet, and desktop
7. **Add to the appropriate folder**: 200-light/ or 300-dark/
8. **Number sequentially** (e.g., 260, 270) if adding beyond 250

## Integration with 100-viewer.html

All templates are designed to work seamlessly with the main presentation viewer. The viewer:

- Loads slides in `<iframe>` elements (file isolation)
- Provides keyboard shortcuts (arrow keys, N for notes, etc.)
- Uses localStorage to remember theme and last slide
- Does NOT require build tools, servers, or external dependencies

## Tips for Consistency

✓ **Do use** the colour palette from 001-design-system.html
✓ **Do reuse** CSS patterns (clamp(), grid auto-fit, flex layouts)
✓ **Do include** speaker notes in every slide
✓ **Do test** on multiple screen sizes
✗ **Don't add** external stylesheets or CDN fonts
✗ **Don't use** JavaScript beyond vanilla browser APIs
✗ **Don't break** file isolation (avoid cross-iframe communication)

## Template Metadata at a Glance

Every template documents:

1. **What it's for** (use case)
2. **How it looks** (layout structure)
3. **What colours it uses** (hex codes)
4. **What fonts** are applied
5. **How to customize** it
6. **How it responds** to different screen sizes

**This makes it easy to:**

- Pick the right template for your content
- Create colour variations by swapping hex codes
- Understand the design system and extend it
- Generate new slides consistently

## File Counts

- **1** Basic starter template (100-basic.html)
- **26** Light theme templates (001–250, 200-light/)
- **26** Dark theme templates (001–250, 300-dark/)
- **53 total** self-documenting HTML files

All files validated for:

- ✓ Valid HTML5 DOCTYPE
- ✓ Speaker notes structure (`<aside class="notes">...</aside>`)
- ✓ CSS rule hiding notes by default
- ✓ Responsive design patterns
- ✓ No external dependencies
- ✓ Standalone iframe-compatible structure

---

**Last Updated**: June 2026
**Status**: All 52 templates include design metadata comments
**Next Steps**: Copy templates, customise content, load in 100-viewer.html
