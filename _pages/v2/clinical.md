---
layout: v2-page
permalink: /clinical/
title: Clinical Research
description: Clinical programs connecting Xiangya Hospital resources to mechanistic discovery.
show_lead: false
---
<div class="v2-utility-list">
  <div class="v2-utility-card">
    <h3>Skin aging cohorts</h3>
    <p>Longitudinal phenotyping linked to molecular profiling, biomarker discovery, and aging-clock development.</p>
  </div>
  <div class="v2-utility-card">
    <h3>Hair disorders</h3>
    <p>Clinical material paired with organ culture and regenerative strategies for alopecia and hair graying.</p>
  </div>
  <div class="v2-utility-card">
    <h3>Inflammatory skin disease</h3>
    <p>Patient-derived samples and disease-facing studies focused on rosacea, acne, and related conditions.</p>
  </div>
</div>

### Clinical collaboration

For collaboration related to cohorts, samples, or translational dermatology studies, contact [{{ site.data.socials.email }}](mailto:{{ site.data.socials.email }}).

<hr>

<div class="v2-section">
  <div class="v2-section__intro">
    <h2>Related publications</h2>
  </div>
  {% include bib_search.liquid %}
  <div class="publications">
    {% bibliography --query @*[clinical=true]* %}
  </div>
</div>
