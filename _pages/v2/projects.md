---
layout: v2-page
permalink: /projects/
title: Our Research
description: Rosacea & hidradenitis suppurativa, hair disorders & regeneration, and skin aging.
show_lead: false
---
{% for dir in site.data.research_directions %}
  <article class="v2-program-entry" id="{{ dir.id }}">
    <h2>{{ dir.title }}</h2>
    {% if dir.id == 'rosacea' %}
    <div class="v2-program-entry__media">
      <img src="{{ '/assets/img/research_rosacea.png' | relative_url }}" alt="{{ dir.title }}">
    </div>
    {% elsif dir.id == 'hair' %}
    <div class="v2-program-entry__media">
      <img src="{{ '/assets/img/research_hair_follicle.png' | relative_url }}" alt="{{ dir.title }}">
    </div>
    {% elsif dir.id == 'skin-aging' %}
    <div class="v2-program-entry__media">
      <img src="{{ '/assets/img/research_skin_aging.png' | relative_url }}" alt="{{ dir.title }}">
    </div>
    {% endif %}
    <div class="v2-program-entry__content">
      {{ dir.narrative }}
    </div>
  </article>
  {% unless forloop.last %}<hr>{% endunless %}
{% endfor %}
