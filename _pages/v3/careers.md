---
layout: v3-page
permalink: /v3/contact/
title: Contact Us
description: Get in touch with the Li Lab.
show_lead: false
---
<div class="v3-utility">
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
