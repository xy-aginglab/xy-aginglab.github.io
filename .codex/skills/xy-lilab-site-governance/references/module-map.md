# Module Map

## Core Site Identity And Build

- `_config.yml`
  - global site identity, URLs, Jekyll behavior, scholar behavior, plugin toggles
  - changes here can affect the entire site and often require a skill update
- `_plugins/`
  - custom Liquid and scholar helpers
  - treat as infrastructure, not page-level content

## Source Of Truth: Structured Content

- `_data/i18n/en.yml`
  - English shared UI copy for `v1`
- `_data/i18n/zh.yml`
  - Chinese shared UI copy for `v1`
- `_data/members.yml`
  - team roster, role grouping, bios, photos, profile links
- `_data/socials.yml`
  - social/contact endpoints used on the site
- `_projects/*.md`
  - research-direction detail pages and project-card metadata
  - may also carry concise overview fields used by `v3` research listings, such as short highlight arrays
- `_bibliography/papers.bib`
  - publication metadata and category linking
- `assets/img/publication_preview/*`
  - publication thumbnails referenced from bibliography entries

## Version 1 Surface

- `_layouts/default.liquid`
  - primary `v1` shell, bilingual navigation, footer, language switching, theme toggle
  - note: English navigation is page-driven; Chinese navigation is manually enumerated here
- `_layouts/about.liquid`
  - `v1` home structure
- `_layouts/page.liquid`
  - shared `v1` interior page frame
- `_layouts/people.liquid`
  - `v1` team page
- `_includes/head.liquid`
  - common head assets for `v1`
- `_includes/projects.liquid`
  - project card rendering
- `_includes/selected_papers.liquid`
  - featured publication block
- `_layouts/bib.liquid`
  - shared bibliography list-item renderer used by scholar-driven publication listings
  - must stay version-neutral and must not preserve `v2` / Bloom-specific presentation assumptions
- `_includes/scripts.liquid`
  - lightweight shared scripts
- `_sass/_custom.scss`
  - main `v1` custom design system and component styling
- `_sass/_themes.scss`
  - theme tokens and dark/light behavior
- `_sass/_publications.scss`
  - bibliography styling
- `assets/css/main.scss`
  - imports the `v1` style stack
- `assets/js/theme.js`
  - `v1` theme behavior
- `assets/js/bib-toggle.js`
  - bibliography expand/collapse interactions

## Version 2 Surface

- `_layouts/bloom.liquid`
  - main `v2` shell and navigation
- `_layouts/bloom-page.liquid`
  - `v2` interior content page wrapper
- `_layouts/bloom-people.liquid`
  - `v2` team page
- `_layouts/paper-detail.html`
  - publication detail pages currently rendered in the `v2` visual language
- `_pages/v2*.md` and `_pages/v2/*.md`
  - `v2` routes and content
- `assets/css/bloom.css`
  - local CSS supporting chooser and `v2`-style pieces

## Version 3 Surface

- `_layouts/v3-home.liquid`
  - dedicated `v3` homepage shell
  - exists so the approved homepage treatment can live at `/v3/` without being distorted by shared interior-page rules
- `_layouts/v3.liquid`
  - main `v3` shell and navigation
  - shared `v3` interior shell and navigation
- `_layouts/v3-page.liquid`
  - `v3` interior content page wrapper
  - owns the shared editorial masthead for `v3` interior pages
  - may render page front matter such as eyebrow, description, lead, and optional compact next-step links
  - should not assume every page needs a fact rail or sidebar
- `_layouts/v3-people.liquid`
  - `v3` team page
  - owns the simplified team-page masthead and any lightweight team count summary
- `_layouts/v3-paper-detail.html`
  - `v3` publication detail presentation when routed through the minimalist branch
  - should prefer a simple bibliographic header and reading-first detail view over card-heavy metadata treatment
- `_pages/v3*.md` and `_pages/v3/*.md`
  - `v3` routes and content
- `assets/css/v3.css`
  - local CSS dedicated to the `v3` visual language
  - primary frontier for `v3` interior-page design work
- `assets/css/v3-home.css`
  - homepage-only CSS for the approved cleaner shell now mapped directly onto `/v3/`
- `assets/js/v3.js`
  - `v3` navigation interactions and the homepage rotating-text behavior

## Chooser Surface

- `_pages/home.md`
  - root redirect / handoff into the chosen public branch
- `_pages/chooser.md`
  - version-comparison route
- `_layouts/chooser.liquid`
  - version-surface rendering and design-direction framing

## Ownership Rules

- If the change is mostly copy or structured data, edit `_data`, `_projects`, or `_bibliography` first.
- If the change is page structure inside `v1`, prefer `_layouts/about.liquid`, `_layouts/page.liquid`, `_layouts/people.liquid`, and `_sass/_custom.scss`.
- If the change is page structure inside `v2`, prefer the `bloom*` layouts and `assets/css/bloom.css`.
- If the change is page structure inside `v3`, prefer the `v3*` layouts and `assets/css/v3.css`.
- If the change is a design-forward refinement and no version is specified, prefer implementing it in `v3`.
- If the change is a navigation taxonomy change:
  - update page front matter where English `v1` nav depends on it
  - update `_layouts/default.liquid` for Chinese `v1` nav
  - update `_layouts/bloom.liquid` for `v2` nav if the legacy branch still needs it
  - update `_layouts/v3.liquid` for `v3` nav
  - update the skill first

## Skill-First Structural Triggers

- Moving content responsibility between layouts and data files
- Introducing a shared component across `v1` and `v2`
- Introducing a shared component across `v1`, `v2`, and `v3`
- Changing how bibliography detail pages are themed or routed
- Changing member roles or research categories
- Changing bilingual coverage rules
- Changing which files own navigation, homepage narrative, or contact data
