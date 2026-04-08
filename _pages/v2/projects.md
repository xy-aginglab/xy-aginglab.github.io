---
layout: v2-page
permalink: /v2/projects/
title: Our Research
description: Pilosebaceous unit diseases and skin aging.
show_lead: false
---
{% assign projects = site.projects | sort: 'importance' %}

{% for project in projects %}
  {% assign slug = project.title | slugify %}
  <article class="v2-program-entry" id="{{ slug }}">
    <h2>{{ project.title }}</h2>
    <div class="v2-program-entry__media">
      <img src="{{ project.img | replace: '.svg', '.png' | prepend: '/assets/img/' | relative_url }}" alt="{{ project.title }}">
    </div>
    <div class="v2-program-entry__content">
      {{ project.overview_detail }}
      <div class="v2-program-entry__more">
        <a href="{{ '/v2/projects/' | append: slug | append: '/' | relative_url }}">View publications & details &rarr;</a>
      </div>
    </div>
  </article>
{% endfor %}
