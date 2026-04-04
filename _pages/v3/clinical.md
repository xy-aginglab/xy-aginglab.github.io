---
layout: v3-page
permalink: /v3/clinical/
title: Our Clinical Research
description: Clinical programs that connect Xiangya Hospital resources to mechanistic discovery and intervention design.
show_lead: false
---
<div class="v3-utility">
  <section class="v3-utility-section">
    <div class="v3-utility-list">
      <article>
        <h3>Skin aging cohorts</h3>
        <p>Longitudinal phenotyping linked to molecular profiling, biomarker discovery, and aging-clock development.</p>
      </article>
      <article>
        <h3>Hair disorders</h3>
        <p>Clinical material paired with organ culture and regenerative strategies for alopecia and hair graying.</p>
      </article>
      <article>
        <h3>Inflammatory skin disease</h3>
        <p>Patient-derived samples and disease-facing studies focused on rosacea, acne, and related disfiguring conditions.</p>
      </article>
    </div>
  </section>

  <section class="v3-utility-section">
    <h2>Clinical collaboration</h2>
    <p>For collaboration related to cohorts, samples, or translational dermatology studies, contact <a href="mailto:{{ site.data.socials.email }}">{{ site.data.socials.email }}</a>.</p>
  </section>
</div>

<hr class="v3-divider">

<section class="v3-section">
  <div class="v3-section__intro">
    <h2>Related publications</h2>
  </div>
  <div class="v3-surface v3-publication-surface">
    <div class="publications">
      {% bibliography --query @*[clinical=true]* %}
    </div>
  </div>
</section>
