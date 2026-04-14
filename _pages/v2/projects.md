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
    <div class="v2-program-entry__content">
      {{ dir.narrative }}
    </div>
  </article>
  {% unless forloop.last %}<hr>{% endunless %}
{% endfor %}
