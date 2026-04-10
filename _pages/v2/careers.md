---
layout: v2-page
permalink: /contact/
title: Contact
show_lead: false
---

<div class="v2-contact-grid">
  <div class="v2-contact-card">
    <h3><i class="fas fa-envelope"></i> Email</h3>
    <p><a href="mailto:{{ site.data.socials.email }}">{{ site.data.socials.email }}</a></p>
  </div>
  <div class="v2-contact-card">
    <h3><i class="fas fa-location-dot"></i> Address</h3>
    <p>
      Department of Dermatology<br>
      Xiangya Hospital, Central South University<br>
      87 Xiangya Road, Kaifu District<br>
      Changsha, Hunan, China 410008
    </p>
    <a href="https://maps.apple.com/?q=28.2028,112.9690" target="_blank" rel="noopener noreferrer" class="v2-contact-map-link"><i class="fas fa-map-location-dot"></i> View on Map</a>
  </div>
  {% if site.data.socials.github or site.data.socials.researchgate %}
  <div class="v2-contact-card">
    <h3><i class="fas fa-globe"></i> Online</h3>
    <p>
      {% if site.data.socials.github %}<a href="https://github.com/{{ site.data.socials.github }}" target="_blank" rel="noopener noreferrer"><i class="fab fa-github"></i> GitHub</a><br>{% endif %}
      {% if site.data.socials.researchgate %}<a href="https://www.researchgate.net/profile/{{ site.data.socials.researchgate }}" target="_blank" rel="noopener noreferrer"><i class="ai ai-researchgate"></i> ResearchGate</a>{% endif %}
    </p>
  </div>
  {% endif %}
</div>
