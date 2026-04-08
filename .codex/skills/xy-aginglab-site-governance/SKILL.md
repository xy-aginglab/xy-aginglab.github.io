---
name: xy-aginglab-site-governance
description: Use when working in the xy-aginglab.github.io repository for the Hunan Key Laboratory of Aging Biology. Covers project goals, governance rules, version strategy, bilingual content behavior, and module ownership for layout, style, data, and publication changes.
---

# XY AgingLab Site Governance

## Start Every Task Here

- Re-open this file from disk at the start of every task in this repository. This skill is intentionally stored inside the project so it can be updated at runtime.
- If the requested change affects design philosophy, information architecture, source-of-truth rules, feature behavior, module boundaries, styling systems, bilingual strategy, or version strategy, update the relevant reference file first and then implement the code change.
- If the code and this skill disagree, stop and reconcile the difference instead of assuming the code is the source of truth.

## Project Intent

- This repository is the public website for the Hunan Key Laboratory of Aging Biology at Xiangya Hospital, Central South University.
- The site must present the lab as credible, translational, academically serious, and easy to maintain as a static site.
- The core public story is stable: the lab sits at the intersection of clinical dermatology and molecular biology, with three major research directions:
  - skin aging
  - hair diseases and hair regeneration
  - inflammatory skin diseases
- The site must make it easy to discover research, publications, team members, clinical programs, and recruiting information.

## Current Product Shape

- `/` is the primary public entry and displays the version chooser so visitors can pick a version.
- `/versions/` also renders the same chooser layout and remains a valid alias.
- `/v1/` is the fuller institutional surface:
  - branded and section-driven
  - bilingual (`en` plus `zh`)
  - Jekyll/al-folio based with a custom SCSS design system
- `/v2/` is a research-narrative surface built on the v3 design system:
  - shares v3 typography, color tokens, dark mode, and base CSS
  - has its own `v2-*` layout files (copied from v3, URLs adjusted) for version isolation
  - homepage features detailed research-direction narratives with inline high-impact-factor paper citations (inspired by qichen-lab.info)
  - homepage structure: hero + research highlights (2 directions with paper evidence) + research direction summary cards
  - research narrative content lives in `_data/research_directions.yml` (bilingual)
  - interior pages reuse the same content patterns as v3 with v2-prefixed layouts
  - all Bloom-specific naming (`bloom*`) is retired; no Tailwind CDN dependency
- `/v3/` is the canonical final-design branch behind the primary public entry:
  - content-first and typography-led
  - must be visually distinct from Bloom Lab even if it preserves a calm academic homepage feel
  - may reuse lightweight utility styling, but must not preserve Bloom-specific page skeletons, naming, or component mimicry
  - is the preferred end-state public direction and should receive the highest design and product-quality investment
  - its homepage should now follow the former `v4` implementation in full, with only one approved exception: keep the bug-free `v3` typewriter behavior
  - `v3` and the former `v4` homepage experiment should not be treated as parallel public options anymore
- `v1` can remain publicly accessible during transition work, but new design-level decisions should default toward strengthening `v3` unless the user explicitly asks for `v1`
- Preserve this split unless the user explicitly requests a product-level consolidation and the skill is updated first.

## Required Workflow

1. Re-open this `SKILL.md`.
2. Read only the reference file(s) needed for the task:
   - design, branding, tone, version direction: `references/design-philosophy.md`
   - page purpose, feature behavior, UX expectations: `references/feature-design.md`
   - `v3` homepage and visual-system decisions: `references/v3-homepage-blueprint.md`
   - file ownership, module boundaries, source-of-truth mapping: `references/module-map.md`
3. If the task changes any documented rule in those references, update the reference file first.
4. Implement the code or content change.
5. Verify that the final code still matches the documented rules.

## Hard Guardrails

- Do not mix `v1` SCSS components and `v2`/`v3` utility-style patterns inside the same user-facing surface unless the skill is updated to define a shared pattern.
- Do not hard-code repeated institutional, research, team, or contact content inside layouts when an existing data/content source already exists.
- Do not collapse chooser, `v1`, `v2`, and `v3` into one surface as a side effect of a local cleanup.
- Do not change navigation taxonomy, page hierarchy, or routing conventions without updating the skill first.
- Do not introduce a new build dependency or app framework as an incidental implementation choice. The default assumption is Jekyll + Liquid + SCSS + lightweight JavaScript, plus Tailwind CDN only where the repository already uses it.
- Do not make structural design changes in only one language when the affected surface is meant to stay bilingual.
- Do not carry Bloom-specific naming, comments, or near-copy layout structures into new public-facing versions.

## When The Skill Must Be Updated First

- New or removed top-level page categories, routes, or navigation items
- Changes to the chooser / `v1` / `v2` / `v3` relationship
- Changes to visual identity, typography, color systems, motion rules, or interaction style
- Changes to where core copy or structured content lives
- Changes to data schemas in `_data`, `_projects`, or bibliography-driven page patterns
- Changes to publication presentation patterns or paper detail behavior
- Changes to team-role taxonomy, research-direction taxonomy, or bilingual coverage policy
- Refactors that move responsibility across layouts, includes, stylesheets, scripts, or data files

## When The Skill Usually Does Not Need Updates

- Isolated copy edits that do not change page purpose or source-of-truth rules
- Adding or correcting a member profile inside the existing schema
- Adding publications, preview images, or news items inside the existing pattern
- Asset swaps that do not change layout behavior or design rules
- Small bug fixes that preserve the documented design and module boundaries

## Task Defaults

- If the user does not specify a version, change only the minimum affected surface and avoid cross-version propagation unless the request is clearly cross-version.
- If a request touches shared scientific messaging, keep the three research directions aligned with the existing framing unless the user explicitly changes the lab narrative.
- Prefer data-driven edits over template-level duplication.

## References

- `references/design-philosophy.md`
- `references/feature-design.md`
- `references/v3-homepage-blueprint.md`
- `references/module-map.md`
