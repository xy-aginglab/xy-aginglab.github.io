---
layout: v3-page
permalink: /v3/projects/
title: Our Research
description: Skin aging, hair diseases and regeneration, and inflammatory skin disease.
show_lead: false
---
{% assign projects = site.projects | sort: 'importance' %}

<div class="v3-program-stack">
  {% for project in projects %}
    {% assign project_overview = project.content | split: '<p><strong>Key Areas:</strong></p>' | first %}
    <article id="{{ project.title | slugify }}" class="v3-program-entry">
      <h2>{{ project.title }}</h2>
      <div class="v3-program-entry__media">
        <img src="{{ project.img | replace: '.svg', '.png' | prepend: '/assets/img/' | relative_url }}" alt="{{ project.title }}">
      </div>
      <div class="v3-program-entry__content">
        {{ project_overview }}
        {% if project.overview_detail %}
          <p>{{ project.overview_detail }}</p>
        {% endif %}
      </div>
    </article>
  {% endfor %}
</div>
