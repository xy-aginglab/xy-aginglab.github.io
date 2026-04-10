---
layout: v2-page
permalink: /zh/contact/
title: 联系我们
lang: zh
show_lead: false
---

<div class="v2-contact-grid">
  <div class="v2-contact-card">
    <h3><i class="fas fa-envelope"></i> 邮箱</h3>
    <p><a href="mailto:{{ site.data.socials.email }}">{{ site.data.socials.email }}</a></p>
  </div>
  <div class="v2-contact-card">
    <h3><i class="fas fa-location-dot"></i> 地址</h3>
    <p>
      中南大学湘雅医院皮肤科<br>
      湖南省长沙市开福区湘雅路87号<br>
      410008
    </p>
    <a href="https://maps.apple.com/?q=28.2028,112.9690" target="_blank" rel="noopener noreferrer" class="v2-contact-map-link"><i class="fas fa-map-location-dot"></i> 查看地图</a>
  </div>
  {% if site.data.socials.github or site.data.socials.researchgate %}
  <div class="v2-contact-card">
    <h3><i class="fas fa-globe"></i> 在线</h3>
    <p>
      {% if site.data.socials.github %}<a href="https://github.com/{{ site.data.socials.github }}" target="_blank" rel="noopener noreferrer"><i class="fab fa-github"></i> GitHub</a><br>{% endif %}
      {% if site.data.socials.researchgate %}<a href="https://www.researchgate.net/profile/{{ site.data.socials.researchgate }}" target="_blank" rel="noopener noreferrer"><i class="ai ai-researchgate"></i> ResearchGate</a>{% endif %}
    </p>
  </div>
  {% endif %}
</div>
