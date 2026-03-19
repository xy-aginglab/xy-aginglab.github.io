# Design Philosophy

## Product Posture

- This site is an academic institution site, not a startup landing page.
- The default tone is credible, calm, and translational rather than promotional.
- Visual choices should reinforce scientific seriousness, institutional trust, and readability.
- High-value content should appear before decorative flourishes.
- The public-facing `v3` experience should be legible to international visitors who may know neither Xiangya Hospital nor the Chinese academic system in advance.
- `v3` should feel closer to a strong institutional or editorial website than to an internal project brief or a dense academic memo.
- For the homepage specifically, `v3` may lean toward a very sparse, quiet academic-portfolio feel as long as it remains clearly institutional and not a direct Bloom copy.

## Narrative Priorities

- Lead with the lab's bridge between clinical dermatology and molecular biology.
- Keep the three flagship research directions visible and stable:
  - skin aging
  - hair diseases and hair regeneration
  - inflammatory skin diseases
- Support the research story with publications, team credibility, and clinical context.
- Recruiting and contact should be easy to find, but should not overpower the research narrative.

## Version Strategy

### Version Surface (`/versions/`)

- Purpose: expose the currently available design directions without replacing the main public entry.
- Keep it small and explicit.
- Do not turn the version surface into a full site.

### Version 1 (`/v1/`)

- Purpose: institutional, branded, and more complete.
- Design character:
  - strong hero
  - colored navigation
  - visible section boundaries
  - affiliation/logo reinforcement
  - bilingual coverage
- Use when a change needs fuller institutional storytelling, bilingual support, or stronger brand framing.

### Version 2 (`/v2/`)

- Purpose: retained legacy experiment.
- Status:
  - visible on `/versions/` so the team can compare it directly with `v1` and `v3`
  - preserved for reference, comparison, migration, or selective reuse of interaction ideas
- Do not treat `v2` as a copy source for new public work, but do study what it gets right about restraint, pacing, and first-screen clarity.

### Version 3 (`/v3/`)

- Purpose: preferred end-state public direction, delivered through a minimalist alternative to `v1`.
- Design character:
  - restrained but not anonymous
  - strong editorial typography
  - calmer chrome than `v1`, but more original than `v2`
  - visually distinct from Bloom Lab while preserving an academic homepage feel
  - closer to an institutional publication or annual-report site than a design-forward SaaS landing page
- `v3` should present a clean path for first-time international visitors:
  - who the lab is
  - what it studies
  - why the work is credible
  - where to go next
- The old `v4` homepage experiment is no longer an independent branch. Its visual shell is the approved homepage direction for `v3`.
- The approved merge rule is now explicit:
  - keep the former `v4` homepage implementation in full
  - keep only the former `v3` typewriter implementation as the single approved exception
  - do not maintain `v3` and `v4` as two separate homepage options
- The `v3` homepage should prefer one dominant first-screen statement over split-screen dashboards, stat blocks, or parallel explanation panels.
- The `v3` homepage should be willing to say less. If a section does not change understanding or navigation, remove it.
- If the user explicitly prioritizes maximum simplicity, `v3` homepage may collapse to a pure hero plus a minimal set of exit links.
- In the current reset direction, `v3` homepage should behave as a pure entry page:
  - one hero block
  - one primary action
  - no lower homepage summary sections
- In the stricter final-home direction, `v3` homepage should let the header do the routing work:
  - keep one primary CTA in the hero
  - optionally pair it with one quieter publications CTA when the user wants publications surfaced as a co-equal next step
  - do not repeat a second row of page exits below that CTA if the same destinations are already visible in the top navigation
- The strongest final `v3` homepage should feel more like a decisive editorial cover than a site summary:
  - one memorable statement
  - one short line of scientific focus
  - one short institutional anchor
  - one obvious next action
- Do not let the homepage say the same thing twice in slightly different wording. If the rotating line already carries the research directions, the supporting paragraph should add institutional or methodological context instead of restating the same list.
- When dedicated interior pages exist, do not preview them all on the homepage by default. The homepage should point to them, not compete with them.
- Interior pages should feel like a coherent institutional publication system rather than unrelated standalone pages.
- Shared `v3` page framing may use:
  - a strong editorial masthead
  - a concise lead paragraph
  - optional compact navigation or utility links when they reduce friction
- `v3` should favor a smaller primary navigation and move secondary or lower-frequency pages into footer-level discovery when that improves focus.
- `v3` should keep the core primary navigation small, but secondary pages that remain part of the active public surface should still be visibly discoverable near the top of the page.
- Do not make `Clinical`, `News`, or `Careers` footer-only if they are meant to function as real visitor destinations in the active `v3` experience.
- During the current design-comparison phase, `Versions` may live in the footer only. Do not repeat it in the top utility navigation when the footer already exposes the version surface clearly.
- In `v3`, the visible nav brand may use a short public label such as `Aging Lab` when the full institutional name creates clutter.
- If the short brand is used in nav, keep the full institutional identity elsewhere on the page or in footer/meta rather than stacking it into the corner mark.
- When the visible `Aging Lab` brand already links to `/v3/`, do not repeat `Home` as a separate top-nav tab.
- On `v3`, do not repeat the institution in the nav, hero eyebrow, and support line at the same time. Mention it once in the homepage intro if needed.
- On `v3`, if the short brand `Aging Lab` already appears in the header and headline, do not add a separate institutional eyebrow above the headline unless it introduces information that does not already exist elsewhere on the first screen.
- On `v3`, the footer should stay quiet and utilitarian. Do not repeat the homepage research-direction summary in the footer when the page has already established it.
- A single-page `v3` is an exception, not the default. Use it only when the user explicitly wants that tradeoff and accepts the added density.
- Use when a change should favor reading flow, minimal framing, and a modern institutional research presentation without direct Bloom mimicry.
- `v3` should be polished as a complete, production-quality institutional site rather than left as a visual experiment.
- The root route `/` should send visitors into `v3` rather than back to version comparison once the direction is chosen.

## Cross-Version Rules

- Do not assume a design rule from `v1` automatically applies to `v2` or `v3`, or vice versa.
- If a request should affect both versions, implement each version in its own native system instead of forcing a shared component abstraction by default.
- If both versions are diverging enough that a new governance rule is needed, update the skill first.
- `v2` may remain publicly comparable on `/versions/` without becoming the root entry by default.
- `v3` can remain the root-bound experimental public branch while `v2` is surfaced again for comparison.
- If a design or UX investment decision has to favor one public branch, prefer `v3` unless the user explicitly prioritizes `v1`.

## Visual Rules

- Prefer clarity over novelty.
- Keep imagery relevant to research areas, publications, or institutional identity.
- Motion should support emphasis, orientation, or polish. Avoid decorative animation that competes with scientific content.
- Typography changes must preserve legibility on desktop and mobile.
- Color changes must preserve academic tone and sufficient contrast. Avoid turning the site into a generic tech-brand palette.
- For `v3`, avoid glassmorphism, oversized pill treatments, loud background textures, and large-radius card stacks when they make the site feel ornamental instead of institutional.
- `v3` should prefer quieter page planes, sharper hierarchy, restrained accents, and a more paper-like or editorial sense of structure.
- In `v3`, design hierarchy should come primarily from scale, spacing, alignment, and contrast, not from multiplying cards, labels, or decorative containers.
- Keep the number of major homepage sections low enough that the page can be scanned in one pass.
- On the `v3` homepage, favor open space, restrained navigation, and quiet section transitions over boxed panels and card-heavy layouts.
- Avoid turning the first screen of `v3` into a two-column dashboard unless the second column is truly necessary.
- For `v3`, primary structure should come from sequence and whitespace before it comes from components.
- A one-page `v3` should still feel calm: use a small number of clear sections rather than trying to dump every detail at once.
- On the `v3` homepage, the rotating research-direction line may borrow the restraint of `v2` by using a typewriter-like cadence and a soft color-backed highlight, as long as the rest of the hero remains original and uncluttered.
- If the user explicitly says the `v2` rotating-text treatment is their own authored work and wants it reused, `v3` may directly reuse that `v2` hero-line implementation instead of approximating it.
- If a cleaner homepage shell proves stronger, fold it directly into `v3` instead of preserving a parallel experimental branch.
- If the user explicitly says the previous cleaner `v4/D` homepage is the target, copy that homepage directly into `v3` instead of reinterpreting it. In that case, the only approved delta is the user-requested `v3` typewriter implementation.
- If `v3` uses a large homepage headline, the measure and line breaks must feel intentional. Avoid oversized titles that wrap awkwardly or create empty-feeling whitespace.
- On `v3`, the research index should read as a clean program overview. Do not stack full project articles, nested publication archives, or repeated heading hierarchies inside the overview page when a concise summary will do.
- On `v3`, the research index should favor a plain editorial structure over card UI:
  - section title
  - one research image
  - one or two short paragraphs
  - quiet dividers
- When the user asks to align the research presentation with `v2`, reuse the simpler `v2` image placement logic rather than inventing a new card/grid treatment.
- On `v3`, publication list pages may suppress preview thumbnails when they make scanning slower or more decorative than useful.
- On `v3`, publications pages should not repeat helper paragraphs, topic pills, or decorative labels when the page title and the publication list already make the purpose obvious.
- On `v3`, publication detail pages should prefer straightforward bibliographic presentation over dashboard-like fact cards, repeated metadata boxes, or prominent gallery treatment.
- On `v3`, interior mastheads should stay minimal. Avoid ornamental eyebrows, secondary link rows, or duplicated lead copy unless they solve a real orientation problem on that specific page.
- On `v3`, the team page should read like a calm people directory:
  - one short intro
  - one visually distinct PI block
  - simple grouped member grids
- On `v3`, secondary member portraits should stay modest. Headshots are there to support recognition, not to dominate the directory like a gallery wall.
- On `v3`, avoid team statistics strips, repeated department labels on every card, and long bios inside secondary member cards when they make the page feel busier than the content requires.
- On `v3`, if many members do not have portraits, render them as a compact roster rather than forcing placeholder-style cards or equally weighted empty-image blocks.
- On `v3`, keep the PI block editorial but not oversized: one short bio paragraph is usually enough unless the user explicitly wants a fuller profile.
- On `v3`, utility pages such as `Clinical`, `News`, and `Careers` should read as light editorial pages:
  - short masthead
  - single-column body
  - divided sections or lists instead of card matrices
- On `v3`, selected quiet interior pages such as `Team`, `Clinical`, `News`, and `Careers` may use a slightly right-shifted desktop content axis when the default left alignment feels visually heavy.
- Avoid turning these utility pages into dashboards of tiles, process boxes, or explanatory frameworks unless the content truly requires them.
- On `v3`, utility pages should err on the side of under-explaining rather than over-explaining:
  - remove generic framing copy
  - keep only the sections that change a visitor's understanding or next action
  - tighten vertical spacing so these pages feel like concise notes, not mini-homepages
- For final-homepage quality, prioritize:
  - rhythm
  - restraint
  - hierarchy
  - recognizability on first glance
- Do not chase impact by adding modules. The homepage becomes more striking when each remaining element has a clear visual job.
- `v3` should use one shared typographic system across homepage and interior pages:
  - display serif: `Newsreader`
  - UI and body sans: `Manrope`
  - no opportunistic font swaps between homepage and interior templates
- `v3` hierarchy should come from a deliberate size ladder rather than component decoration:
  - nav brand: about 20px to 22px
  - primary nav: about 15px
  - utility nav: match the primary nav size in the current `v3` direction; distinguish it through grouping and lighter color rather than smaller type
  - homepage hero title: about 88px to 104px
  - rotating line: about 28px to 34px
  - page title: about 52px to 64px
  - lead paragraph: about 21px to 24px
  - body copy: about 18px to 19px
  - small metadata and footer text: about 14px to 15px
- `v3` spacing should feel open but not luxury-brand loose:
  - tighter nav and chrome
  - generous masthead spacing
  - comfortable paragraph leading
  - quiet footer
- Avoid using heavy shadows, thick borders, or card stacks to compensate for weak typographic hierarchy.

## Content Strategy Rules

- Repeated scientific statements should come from data/content files where practical, not from multiple disconnected layout fragments.
- For `v3`, prefer short, concrete, literal copy over abstract framing language.
- Avoid meta-writing about the website itself when a direct statement about the lab, the research, or the opportunity would be clearer.
- Avoid stacking multiple high-level abstractions in one paragraph; readers should understand the sentence on the first pass.
- For `v3`, homepage copy should explain the lab in one short headline and one short supporting paragraph before moving into research, publications, team, or contact.
- For `v3`, do not add a new explanatory section if an existing section already covers the same claim.
- International-facing `v3` copy should prefer globally legible academic language over institution-internal phrasing or translated bureaucratic wording.
- For `v3`, the strongest homepage mode is often:
  - one strong headline
  - one short dynamic or secondary line
  - one or two short factual paragraphs
  - one clear CTA row
- In that maximum-simplicity mode, publications, team credibility, and contact can move off the homepage and be represented only through lightweight exit links.
- If a homepage preview cannot feel complete, remove it and rely on the dedicated page instead.
- Bilingual `v1` surfaces should remain semantically aligned across English and Chinese even if the exact wording differs.
- Current asymmetry is allowed:
  - `v1` is bilingual
  - `v2` is legacy and not a full bilingual mirror
  - `v3` may launch English-first if the scope is explicitly limited
- Do not silently expand or shrink bilingual coverage without updating the skill first.
