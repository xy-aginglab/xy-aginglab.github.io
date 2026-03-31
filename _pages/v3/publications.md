---
layout: v3-page
permalink: /v3/publications/
title: Publications
description: Selected and complete publications from the Li Lab.
show_eyebrow: false
show_lead: false
hide_publication_thumbnails: true
---
<div class="v3-stack">
  <section class="v3-section">
    <div class="v3-section__intro">
      <h2>Selected papers</h2>
    </div>
    <div class="v3-surface v3-publication-surface">
      <div class="publications">
        {% bibliography --group_by none --query @*[selected=true]* %}
      </div>
    </div>
  </section>

  <section class="v3-section">
    <div class="v3-section__intro">
      <h2>Complete list</h2>
    </div>
    <div class="v3-surface v3-publication-surface">
      {% include bib_search.liquid %}
      <div class="publications">
        {% bibliography %}
      </div>
    </div>
  </section>
</div>
