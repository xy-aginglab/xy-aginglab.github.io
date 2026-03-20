# V3 Homepage Blueprint

## Purpose

- This document defines the likely end-state direction for the `v3` homepage and the supporting visual system around it.
- Use it when making design-level decisions about:
  - homepage structure
  - typography
  - scale hierarchy
  - color direction
  - spacing rhythm
  - `v3` navigation tone
  - the relationship between homepage and utility pages

## External References Reviewed

- Arc Institute
  - https://arcinstitute.org/
  - What it gets right:
    - one strong mission-led opening
    - immediate institutional credibility
    - calm research tone
    - clear routes into research and careers
- Biohub
  - https://biohub.org/
  - What it gets right:
    - explicit top-level navigation
    - a strong mission sentence
    - clear separation between mission, research, news, and recruiting
  - What not to copy:
    - the homepage becomes much denser once multiple large sections stack below the fold
- OpenAI
  - https://openai.com/
  - What it gets right:
    - strong hierarchy from type size and spacing
    - clear CTA handling
    - disciplined use of whitespace
  - What not to copy:
    - the information architecture is too broad for a single lab site
- Apple
  - https://www.apple.com/
  - What it gets right:
    - each hero says one thing
    - each block has a clear job
    - typography scale is decisive
  - What not to copy:
    - product-grid logic is not appropriate for a research lab homepage
- Bloom-inspired local `v2`
  - internal reference only
  - What it gets right:
    - first-screen restraint
    - a memorable rotating research line
    - low cognitive load

## Core Conclusion

- The most attractive final homepage for this project is not the one with the most modules.
- It is the one that creates the clearest first impression in the shortest time:
  - who this lab is
  - what it studies
  - why it is credible
  - where the visitor should go next
- The homepage should feel like an editorial cover page, not a compressed sitemap.

## Final Homepage Formula

The target `v3` homepage should usually contain only:

1. A quiet top navigation
2. One dominant hero block
3. One primary CTA
4. A quiet footer

Everything else belongs on interior pages unless the user explicitly asks for a denser homepage.

If the user explicitly prefers the cleaner homepage treatment, treat that as the homepage baseline for `v3` instead of reinterpreting it. Preserve only the specifically approved `v3` deltas:

- keep the `v3` rotator implementation
- keep the hero free of an extra eyebrow above `Aging Lab.`
- do not restore a secondary link row under the primary CTA
- keep publications as the only allowed secondary CTA when the user asks for it explicitly
- if the user says the previous `v4/D` homepage is the target, copy that homepage directly and isolate homepage styling so shared `v3` interior-page rules cannot drift the homepage away from the approved look

That choice is now active for this repository:

- the homepage follows the former `v4/D` implementation
- the rotating line keeps only the former `v3` implementation because it behaved correctly
- `v3` and the former `v4` are no longer to be presented as two separate homepage candidates

## Hero Content Rules

- The hero should have one dominant headline.
- The hero type scale can be increased slightly if the screen still clears on a MacBook Air class laptop without requiring first-screen scrolling.
- If the hero type scale is increased, preserve the one-screen fit by tightening vertical padding before adding any extra module or secondary copy.
- If the user explicitly asks for one more size step, increase the headline and rotating line together so the hierarchy remains coherent rather than enlarging only one of them.
- On phones, reverse that tradeoff: reduce hero scale and padding together before allowing the first screen to feel oversized or unstable.
- The rotating line should carry the three research directions if it is present.
- The rotating line should not cause homepage reflow while it animates. Reserve a stable slot for the changing phrase so the lead, CTA row, and footer do not jump.
- The supporting paragraph should not restate the rotating line.
- The hero should not add a separate eyebrow above `Aging Lab.` when that line only repeats institutional identity already carried by nav or paragraph copy.
- The supporting paragraph should answer:
  - where the work happens
  - how the work is done
  - why the lab is credible
- The hero should not try to preview research, publications, team, and careers all at once.
- The hero content block should sit near the visual center but slightly to the right of the page midpoint on desktop, rather than reading as a left-anchored column.

## Recommended Content Order

1. Lab name / dominant headline
2. Rotating research-focus line
3. One short institutional-and-method paragraph
4. One primary CTA

## Navigation Model

- Primary navigation:
  - Research
  - Publications
  - Team
- The visible `Aging Lab` brand in the header should serve as the homepage link instead of a duplicated `Home` tab.
- Keep the compact `Aging Lab` label in the top-left nav when it improves header balance, even though the hero also carries `Aging Lab.` as the dominant headline.
- In the active homepage direction, that top-left brand may use the restrained `v2` rust-red accent so it reads as a small mark rather than a second black headline.
- Secondary visible utility navigation:
  - Clinical
  - News
  - Careers
- `Versions` should not appear in the top utility nav when the footer already exposes the version chooser clearly
- Secondary routes should remain visibly discoverable near the top, but they must look lighter than the primary routes through grouping and color, not through smaller font size.

## Typography Direction

### Overall Recommendation

- Prefer one editorial serif for display and one clean sans-serif for UI/body.
- Keep the serif reserved for:
  - homepage headline
  - major page titles
  - section titles where emphasis matters
- Keep the sans-serif for:
  - navigation
  - body copy
  - metadata
  - buttons
  - small utility text

### Recommended Default Pair

- Display serif:
  - `Newsreader`
  - reference: https://productiontype.com/font/newsreader
- Body/UI sans:
  - `Manrope`
  - reference: https://fonts.google.com/specimen/Manrope

### Why This Pair Works

- `Newsreader` gives the homepage a warmer editorial character without feeling like a luxury brand.
- `Manrope` keeps UI and body copy clean, modern, and readable.
- The pair is open, practical, and already fits the project stack.

### Acceptable Alternative Directions

- More institutional / less fashionable:
  - `Source Serif 4` + `Inter` or `IBM Plex Sans`
- More design-forward, use carefully:
  - `Instrument Serif` + `Inter`

Do not switch typefaces casually once the visual direction stabilizes.

## Type Scale

Use this as the default target range for desktop:

- Brand / small nav label:
  - 18px to 22px
- Primary nav:
  - 15px to 16px
- Secondary utility nav:
  - 13px to 14px
- Hero headline:
  - 84px to 104px
- Rotating focus line:
  - 28px to 36px
- Hero paragraph:
  - 19px to 22px
- Interior page titles:
  - 48px to 64px
- Section titles:
  - 28px to 36px
- Body copy:
  - 17px to 19px
- Metadata / helper text:
  - 13px to 15px

The key is not absolute size but decisive separation between levels.

For the active `v3` implementation, keep homepage and interior pages on one shared practical ladder:

- nav brand:
  - 20px to 22px
- primary nav:
  - about 15px
- utility nav:
  - match the primary nav size, with lower visual weight handled by color and grouping
- hero title:
  - 88px to 104px
- rotating line:
  - 28px to 34px
- hero lead:
  - 21px to 24px
- page title:
  - 52px to 64px
- page lead:
  - 21px to 24px
- body copy:
  - 18px to 19px
- footer / metadata:
  - 14px to 15px

The homepage may still feel more dramatic than interior pages, but it must not read as a different typographic system.

## Layout And Spacing

- Outer content width:
  - around 1120px to 1200px
- Hero text measure:
  - around 760px to 860px
- Avoid forcing the hero into a narrow left rail unless a second column is genuinely needed.
- Do not create empty right-side space just because the content is arbitrarily width-limited.
- Let whitespace come from top and bottom breathing room, not from marooning content in one thin column.
- In the approved former `v4/D` homepage treatment, the hero block should not hug the left edge of the container. It should sit nearer the visual center, with a slight rightward bias rather than a left-rail composition.

### Desired Rhythm

- Nav to hero:
  - compact but not cramped
- Headline to rotating line:
  - tight enough to feel connected
- Rotating line to paragraph:
  - enough space to reset the eye
- Paragraph to CTA:
  - clear pause
- CTA to footer or next page transition:
  - clean stop, no redundant link cluster if the header already exposes the rest of the site
- On the approved `v3` homepage, do not repeat `Clinical`, `News`, or `Careers` as a second row of exits in the footer when those destinations are already visible in the top navigation.
- If the hero needs optical balance, bias it slightly to the right, but keep the shift subtle rather than turning the page back into a left-rail composition.
- Keep navigation and footer spacing taut; let the main breathing room happen in the hero and interior mastheads instead of in the chrome.
- On phone-sized screens, the homepage should feel controlled rather than monumental:
  - smaller hero title
  - tighter top and bottom padding
  - buttons that stack cleanly without creating excessive dead space
- On phone-sized screens, the homepage footer should stack into a calm vertical rhythm rather than forcing copyright, contact, and version links into one compressed row.

## Color Direction

- Background:
  - warm off-white, not pure white and not beige enough to feel muddy
- Text:
  - dark charcoal, not pure black
- Accent:
  - one restrained terracotta / rust accent
- Supporting separators:
  - thin low-contrast lines
- Rotating line:
  - may keep the three `v2` topic colors because the user authored that treatment

### Palette Intent

- calm
- academic
- warm
- internationally legible
- minimal but not sterile

Do not rely on:

- large color blocks
- gradients as the main identity
- shadows as the main hierarchy mechanism

## UI Rules

- Buttons should feel simple and confident:
  - low radius
  - no heavy shadows
  - clear contrast
- Do not add a secondary link row beneath the hero CTA when those same destinations are already discoverable in the header.
- Footer should be utilitarian, not expressive.
- Interior utility pages should prefer:
  - single-column sections
  - divided lists
  - short subheads
  - quiet contact lines

## Anti-Patterns To Avoid

- Repeating the same research-direction list in the rotating line and the paragraph
- Repeating page navigation in both the header and under the hero CTA
- Repeating homepage copy again in the footer
- Turning utility pages into card dashboards
- Hiding important routes only in the footer
- Using oversized decorative containers to fake hierarchy
- Adding homepage sections because the page feels empty
- Using empty right-side space as a substitute for real restraint
- Mixing multiple visual languages on the same page

## Tomorrow's Build Priorities

1. Finalize the homepage hero copy so each line has a unique job
2. Tighten the nav hierarchy between primary and utility links
3. Decide whether the body/UI font should remain `Manrope` or shift closer to `Inter`
4. Re-check the hero spacing and line lengths visually
5. Bring `Research` and `Publications` into the same calmer editorial system
