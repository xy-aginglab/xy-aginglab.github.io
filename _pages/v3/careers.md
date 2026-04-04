---
layout: v3-page
permalink: /v3/contact/
title: About & Contact
description: About the Li Lab and how to get in touch.
show_lead: false
---
<div class="v3-utility">
  <section class="v3-utility-section">
    <h2>About the Lab</h2>
    <p>The Li Lab is based at the <strong>Hunan Key Laboratory of Aging Biology</strong>, Xiangya Hospital, Central South University. Our research sits at the intersection of clinical dermatology and molecular biology, with three major directions: skin aging, pilosebaceous-related diseases, and inflammatory skin diseases.</p>
    <p>Led by Prof. Ji Li, the lab integrates longevity population cohorts, multi-omics approaches, organ culture models, and translational clinical studies to bridge bench discovery with bedside application.</p>
  </section>

  <section class="v3-utility-section">
    <h2>Email</h2>
    <p><a href="mailto:{{ site.data.socials.email }}">{{ site.data.socials.email }}</a></p>
  </section>

  <section class="v3-utility-section">
    <h2>Address</h2>
    <p><a href="https://www.google.com/maps/search/Xiangya+Hospital,+Central+South+University,+87+Xiangya+Road,+Changsha" target="_blank" rel="noopener noreferrer">Department of Dermatology<br>
    Xiangya Hospital, Central South University<br>
    87 Xiangya Road, Kaifu District<br>
    Changsha, Hunan, China 410008</a></p>
  </section>

  {% if site.data.socials.github or site.data.socials.researchgate %}
  <section class="v3-utility-section">
    <h2>Online</h2>
    <div class="v3-utility-list">
      {% if site.data.socials.github %}
      <article>
        <h3>GitHub</h3>
        <p><a href="https://github.com/{{ site.data.socials.github }}" target="_blank" rel="noopener noreferrer">github.com/{{ site.data.socials.github }}</a></p>
      </article>
      {% endif %}
      {% if site.data.socials.researchgate %}
      <article>
        <h3>ResearchGate</h3>
        <p><a href="https://www.researchgate.net/profile/{{ site.data.socials.researchgate }}" target="_blank" rel="noopener noreferrer">ResearchGate profile</a></p>
      </article>
      {% endif %}
    </div>
  </section>
  {% endif %}
</div>
