# Feature Design

## Site-Level Goals

- Help visitors understand what the lab studies, why it matters, and who is doing the work.
- Make publications and research directions discoverable in a small number of clicks.
- Keep content maintenance straightforward for a Jekyll-based repository.
- On `v3`, prioritize fast comprehension for international academic visitors over exhaustive explanation.

## Page Intent

### Version Surface

- Route users to `v1`, `v2`, and the currently public `v3` branch.
- Present the three directions honestly:
  - `v1` is branded and section-rich
  - `v2` is the restrained minimalist reference
  - `v3` is the newer minimalist/content-first experiment
- Do not add major research or team content here.
- `v2` should be visible again on the version surface when the user wants active comparison.
- While both `v1` and `v3` coexist, `v3` should read as the leading candidate for the site's final public direction.
- Once the user chooses `v3` as the final direction, `/` should favor entry into `v3`, and the version surface should move to a non-root route.

### Home

- Explain the lab's positioning quickly.
- Surface the three research directions.
- Reinforce credibility with featured publications and institutional/contact context.
- In `v1`, the home page is the main institutional landing surface.
- In `v3`, the home page can be more distilled, but it still needs a clear institutional anchor and must not read like a generic PI clone.
- `v3` home should be strong enough to stand as the likely final homepage choice, not just an alternate mockup.
- In `v3`, avoid repeating the same institutional or translational claim in multiple adjacent blocks.
- Prefer fewer sections with clearer jobs over many sections with overlapping explanations.
- In `v3`, the homepage should usually resolve into four core jobs:
  - establish the lab and institution
  - show the three research directions
  - show representative publications
  - route to team, contact, or careers
- `v3` homepage sections should not read like a strategy memo; each section should help the visitor act or understand something specific.
- `v3` homepage may use a very sparse first screen with:
  - one oversized headline
  - one short dynamic focus line
  - one short factual paragraph
  - one primary CTA row
- When the dynamic focus line carries the three research directions, `v3` may present them as a typed rotating phrase with a subtle color background so the changing topic reads as the visual anchor rather than as low-contrast body text.
- If the user explicitly approves direct reuse of the `v2` rotating-text treatment because they authored it, `v3` may reuse the same phrase structure, timing, and highlight behavior for that hero line.
- On `v3`, do not force a homepage side panel, stat card grid, or boxed contact block if they weaken the sense of calm or focus.
- `v3` homepage should usually stop after:
  - the main hero
  - the three research directions
  - a short representative publication block
  - a minimal team/contact exit
- Do not keep adding homepage modules to solve problems that belong on interior pages.
- When the user explicitly asks for an extremely minimal homepage, `v3` may reduce further to:
  - the main hero
  - one CTA
- When dedicated interior pages are already present, prefer the minimal-home mode over homepage summaries.
- A one-page mode is optional and should not be treated as the default final direction.
- In the minimal-home mode, the homepage intro may carry the institutional affiliation once, and the surrounding chrome should stay short.
- In `v3`, the shared footer should support navigation and institutional identification, not restate the homepage research summary.
- In `v3`, the shared interior footer should prioritize contact utility and version discovery, not duplicate destinations that are already visible in the header navigation.
- In the current `v3` reset mode, the homepage should stop at:
  - the main hero
  - one primary CTA
- If the user explicitly wants publications surfaced on the first screen, the hero may use a two-button CTA row:
  - primary: research
  - secondary: publications
- `Clinical`, `News`, and `Careers` should not be summarized again below the fold on the homepage when they already have dedicated routes.
- For the likely final `v3` homepage, the content jobs should resolve in this order:
  - identify the lab
  - state the scientific focus
  - establish institutional credibility once
  - send the visitor to research or publications
- The supporting paragraph on the homepage should usually answer `where and how this work happens`, not repeat `what we study` if the rotating line already covers that.
- Homepage should not duplicate routing that is already handled cleanly by the header. If primary and utility nav are visible, the hero may stop at one CTA without a secondary exit row.
- If a cleaner homepage treatment is chosen for `v3`, implement it directly in `v3` instead of maintaining a separate experiment route.
- If the user explicitly asks to copy the previous `v4/D` homepage because it looked better, treat that request literally: reproduce that homepage inside `v3`, and only preserve the specifically approved `v3` difference of the typewriter behavior.
- This decision is now chosen for the active homepage direction:
  - `v3` homepage uses the former `v4` homepage implementation
  - `v3` homepage keeps only the former `v3` typewriter behavior
  - there should not be a second competing `v4` homepage route for comparison

### Primary Navigation For `v3`

- Keep the primary navigation small.
- Keep the visible nav brand small as well; do not stack a long institutional eyebrow and a long title in the corner if a short lab name is enough.
- Default first-line `v3` navigation should prioritize:
  - Research
  - Publications
  - Team
- The nav brand itself should serve as the homepage route for `v3`; do not duplicate it with a `Home` tab unless the user explicitly asks for one.
- Clinical, Careers, and News may remain routable, but should move to secondary discovery if reducing the primary nav improves clarity.
- When `Clinical`, `Careers`, and `News` are present in the active `v3` surface, keep them in a visible secondary header navigation or similarly discoverable top-level utility area rather than burying them only in the footer.
- In the default minimal-home mode, the primary nav should continue to point to dedicated pages rather than homepage anchors.
- On mobile, the closed `v3` menu must not remain visibly rendered beneath the nav bar. The toggle should be the only visible control until the menu opens.

### Shared `v3` Interior Page Pattern

- `v3` interior pages should prefer a shared editorial masthead rather than ad hoc page intros.
- The shared interior pattern may support an optional desktop content offset for quieter pages that need a less left-heavy reading axis.
- On mobile, the shared interior pattern should compress rather than preserve desktop spacing one-to-one:
  - smaller page titles
  - tighter masthead spacing
  - denser grouped listings
  - section headings that visibly step down from the page title instead of staying near-title size
- The masthead can include:
  - eyebrow
  - title
  - short lead / description
  - optional compact next-step links when genuinely useful
- This pattern should support pages such as research, publications, clinical, news, and careers without forcing identical body content.
- The masthead should reduce repetition inside the body rather than creating redundant copy.
- If the masthead already explains the page clearly, do not add another section that restates the same idea in more abstract language.
- Fact rails and card-heavy sidebars are optional, not the default. Omit them when they make the page feel busier without improving orientation.
- On `v3`, mastheads should be allowed to get lighter on a page-by-page basis:
  - omit eyebrow when it adds no new information
  - omit lead when the title alone is sufficient
  - omit related-link rows unless they materially reduce navigation friction
  - enable the optional content offset only on pages where a more centered-right reading axis improves balance

### Research / Projects

- Each research direction should map to a dedicated project page backed by `_projects/*.md`.
- The research taxonomy should stay stable unless the lab's scientific framing changes.
- Project pages should connect the narrative summary to bibliography-driven evidence.
- The `v3` research index should stay scannable:
  - summarize each program with image, title, short description, and a small number of key points
  - do not inline the full project markdown body and full bibliography archive for every program
- When the user prefers the `v2` research-page feel, the `v3` research index should present each direction as:
  - an underlined heading
  - a half-width image on desktop
  - one or two short paragraphs
  - a clear divider before the next direction
- In that research index, the program heading should feel like an internal section title, not like a second page title.
- If `v3` needs cleaner research-overview copy than the full project body, store that concise overview data in `_projects/*.md` front matter rather than hard-coding it in the layout.

### Publications

- Publications are a core credibility feature, not a secondary archive.
- List pages should support scanning by title, venue, year, preview image, and detail access.
- Detail pages should stay content-first and easy to read.
- For `v3`, detail pages may add a compact metadata/fact treatment and clear primary actions as long as the page remains reading-first rather than dashboard-like.
- For `v3`, publication list pages may choose the simpler scanning mode:
  - hide thumbnails
  - show title, authors, venue, year, and detail link in one compact block
  - place the detail link in the natural text flow rather than in a detached side column
- For `v3`, the publications index should avoid auxiliary clutter:
  - no decorative eyebrow if the page title already says `Publications`
  - no topic pills if those destinations are already covered by the research page
  - no explanatory intro copy above every section when a short heading is enough
- In `v3`, section labels such as `Selected papers` and `Complete list` should be visibly subordinate to the page title on both desktop and mobile.
- For `v3`, publication detail pages should usually collapse to:
  - title
  - authors
  - venue / year / category / doi
  - optional outward publisher link
  - abstract
- Changes to bibliography rendering or paper-detail UX require a skill update first.

### Team / People

- Team pages should emphasize people as research contributors, not generic profile cards.
- The PI should remain visually distinct from grouped member listings unless the design philosophy changes.
- Role groupings come from the existing member taxonomy and should not be changed casually.
- For `v3`, the team page should foreground recognizable names, titles, and roles before explanatory copy about team structure.
- For `v3`, prefer the simpler directory pattern:
  - a direct title and short lead
  - one PI section with concise profile text
  - grouped member listings that prioritize photo, name, title, and optional contact icons
- For `v3`, grouped member photos should read as compact headshots inside the directory rather than large gallery tiles.
- On mobile, grouped member photos should shrink further so names and titles remain the dominant reading signal.
- For `v3`, omit team-count summaries, repeated department lines, and long secondary-card bios unless the user explicitly asks for a denser profile page.
- For `v3`, secondary member groups may split into:
  - portrait grid for members with real photos
  - compact text roster for members without photos
- For `v3`, PI copy should default to one short paragraph on the index page. Longer biography belongs in data for possible future dedicated profile use.

### Clinical

- Explain how the lab's science translates into real clinical programs and resources.
- Keep this page focused on translational value rather than duplicating the entire research page.
- Prefer concrete research/clinical interfaces such as cohorts, samples, disease focus, and therapeutic questions over abstract language about translation.
- On `v3`, prefer a small number of clear single-column sections or divided lists over multi-card grids and numbered process panels.
- On `v3`, the clinical page should usually collapse to:
  - the current interfaces
  - one contact or collaboration route

### Careers

- Support recruiting with clear role expectations and lab environment signals.
- Preserve an academically serious tone; avoid generic corporate recruiting language.
- Lead with who should apply and how to apply, not with abstract statements about recruiting philosophy.
- On `v3`, keep the careers page concise and practical.
- On `v3`, careers should read like a direct recruiting note:
  - who should apply
  - how to apply
  - one clear email/contact route
- On `v3`, careers should avoid repeating role philosophy and application instructions in multiple sections. One compact roles section plus one compact application section is usually enough.

### News

- News is supportive context, not the site's primary identity.
- Updates should feel lightweight and chronological.
- Avoid opening the news page with meta-explanations about what the page is or is not unless they materially help the visitor.
- If the feed is quiet, the fallback state should direct visitors to publications or careers without apologetic or self-referential copy.
- On `v3`, the news page should stay especially sparse: a short lead, then the feed or a minimal empty-state note.
- On `v3`, if the news page already has a clear title, the masthead lead may be omitted entirely.
- On phone-sized `v3` utility pages, the mobile typography should compress with clearer separation than desktop:
  - page title remains prominent
  - section headings step down noticeably
  - item headings step down again
  - body text and line length stay comfortable for scanning

### Version Surface Mobile Behavior

- On phones, the version chooser should stack cleanly and reduce outer padding.
- Preview cards should remain tappable, but preview mockups and descriptive copy should compress so the page does not feel oversized before the first choice.

## Bilingual Expectations

- For `v1`, adding a new core page or changing page purpose usually requires updating the `zh` counterpart or the shared i18n strings.
- `v3` may be English-first while it is incubating, but that asymmetry must stay deliberate rather than accidental.
- If a change is intentionally English-only, make that explicit in the skill before normalizing the asymmetry.

## New Feature Checklist

- Decide which surface(s) the feature belongs to: chooser, `v1`, `v2`, `v3`, or shared content only.
- Identify the source of truth:
  - page front matter
  - `_data`
  - `_projects`
  - `_bibliography`
  - layout-only presentation logic
- Check whether navigation, bilingual coverage, or publication detail behavior changes.
- Update the skill first if the feature changes a reusable pattern or ownership rule.
- If the request is ambiguous between `v1` and `v3`, and it concerns design refinement rather than bilingual parity, bias toward improving `v3`.

## Avoid

- Adding a feature to both versions by default when the request only requires one.
- Hiding scientific substance behind oversized interface treatments.
- Putting structured content into layout files when a data/content file is the better source of truth.
