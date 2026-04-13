# Li Lab — Xiangya Hospital, Central South University

Official website for the Li Lab, Department of Dermatology, Xiangya Hospital, Central South University.

**https://xy-lilab.github.io**

## Research

The lab focuses on three major directions:

- **Rosacea and Hidradenitis Suppurativa** — pathogenesis, multi-omics, and clinical trials
- **Hair Disorders & Regeneration** — alopecia mechanisms, hair follicle biology, and regenerative strategies
- **Skin Aging** — aging mechanisms, longevity cohorts, and anti-aging interventions

## Features

- Bilingual (English / Chinese) with independent content for each language
- 150+ publications with multi-dimensional filtering (direction, subtype, paper type, basic/clinical)
- Research narrative pages with inline graphical abstracts and DOI-linked citations
- Team member profiles with detail pages
- Google Analytics integration
- Open Graph / Twitter Card for social sharing previews
- JSON-LD structured data for search engine indexing
- Print-optimized stylesheet
- Responsive design for desktop and mobile

## Tech Stack

- [Jekyll](https://jekyllrb.com/) static site generator
- [Jekyll-Scholar](https://github.com/inukshuk/jekyll-scholar) for BibTeX-based publication management
- [GitHub Pages](https://pages.github.com/) hosting with automated deployment
- Google Fonts: Merriweather, Source Serif 4, Source Sans 3, Noto Serif SC, Noto Sans SC

## Project Structure

```
_includes/          Shared components (head, nav, footer)
_layouts/           Page templates (home, page, people, member-detail, paper-detail)
_pages/v2/          English pages
_pages/v2/zh/       Chinese pages
_data/              Structured data (members, research directions, i18n strings)
_bibliography/      BibTeX publication database (papers.bib)
assets/css/         Stylesheets (v2-home.css, v2-pages.css, v2-print.css)
assets/js/          Scripts (navigation, bibliography search)
assets/img/         Images (logos, research figures, publication previews)
```

## Design

- Color palette: Xiangya Red (`#a72126`) + CSU Blue (`#0852a2`)
- Typography hierarchy: serif titles (Merriweather) + serif body (Source Serif 4) + sans-serif UI (Source Sans 3)
- Chinese typography: Noto Serif SC (titles) + Noto Sans SC (body), with first-line indent and justified text
- CSS design tokens for global consistency (colors, fonts, spacing managed via CSS variables)
- Academic typography features: oldstyle numerals, automatic hyphenation, orphan/widow control

## License

[MIT](LICENSE)
