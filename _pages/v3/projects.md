---
layout: v3-page
permalink: /v3/projects/
title: Our Research
description: Pilosebaceous unit diseases and skin aging.
show_lead: false
---
{% assign projects = site.projects | sort: 'importance' %}

<div class="v3-program-stack">
  {% for project in projects %}
    {% assign slug = project.title | slugify %}
    <article id="{{ slug }}" class="v3-program-entry">
      <h2><a href="{{ '/v3/projects/' | append: slug | append: '/' | relative_url }}">{{ project.title }}</a></h2>
      <div class="v3-program-entry__media">
        <img src="{{ project.img | replace: '.svg', '.png' | prepend: '/assets/img/' | relative_url }}" alt="{{ project.title }}">
      </div>
      <div class="v3-program-entry__content">
        {{ project.overview_detail }}
        <div class="v3-program-entry__more">
          <a href="{{ '/v3/projects/' | append: slug | append: '/' | relative_url }}">View publications & details →</a>
        </div>
      </div>
    </article>
  {% endfor %}
</div>
