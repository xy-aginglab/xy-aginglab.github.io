---
layout: v3-page
permalink: /v3/zh/projects/
title: 科研方向
lang: zh
description: 毛囊皮脂腺相关疾病与皮肤衰老。
show_lead: false
---
{% assign projects = site.projects | sort: 'importance' %}

<div class="v3-program-stack">
  {% for project in projects %}
    {% assign slug = project.title | slugify %}
    <article id="{{ slug }}" class="v3-program-entry">
      <h2><a href="{{ '/v3/zh/projects/' | append: slug | append: '/' | relative_url }}">{{ project.title_zh | default: project.title }}</a></h2>
      <div class="v3-program-entry__media">
        <img src="{{ project.img | replace: '.svg', '.png' | prepend: '/assets/img/' | relative_url }}" alt="{{ project.title_zh | default: project.title }}">
      </div>
      <div class="v3-program-entry__content">
        <p>{{ project.overview_detail_zh | default: project.overview_detail }}</p>
      </div>
    </article>
  {% endfor %}
</div>
