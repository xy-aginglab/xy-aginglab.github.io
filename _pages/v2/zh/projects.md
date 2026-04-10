---
layout: v2-page
permalink: /zh/projects/
title: 科研方向
lang: zh
show_lead: false
---
{% for dir in site.data.research_directions %}
  <article class="v2-program-entry" id="{{ dir.id }}">
    <h2>{{ dir.title_zh }}</h2>
    {% if dir.id == 'pilosebaceous' %}
    <div class="v2-program-entry__media">
      <img src="{{ '/assets/img/research_hair_follicle.png' | relative_url }}" alt="{{ dir.title_zh }}">
    </div>
    {% elsif dir.id == 'skin-aging' %}
    <div class="v2-program-entry__media">
      <img src="{{ '/assets/img/research_skin_aging.png' | relative_url }}" alt="{{ dir.title_zh }}">
    </div>
    {% endif %}
    <div class="v2-program-entry__content">
      {{ dir.narrative_zh }}
    </div>
  </article>
  {% unless forloop.last %}<hr style="margin:1.5rem 0;">{% endunless %}
{% endfor %}
