---
layout: v2-page
permalink: /v2/zh/projects/
title: 科研方向
lang: zh
show_lead: false
---
{% assign projects = site.projects | sort: 'importance' %}

{% for project in projects %}
  {% assign slug = project.title | slugify %}
  <article class="v2-program-entry" id="{{ slug }}">
    <h2>{% if project.title_zh %}{{ project.title_zh }}{% else %}{{ project.title }}{% endif %}</h2>
    <div class="v2-program-entry__media">
      <img src="{{ project.img | replace: '.svg', '.png' | prepend: '/assets/img/' | relative_url }}" alt="{{ project.title }}">
    </div>
    <div class="v2-program-entry__content">
      {% if project.overview_detail_zh %}{{ project.overview_detail_zh }}{% else %}{{ project.overview_detail }}{% endif %}
      <div class="v2-program-entry__more">
        <a href="{{ '/v2/zh/projects/' | append: slug | append: '/' | relative_url }}">查看论文与详情 &rarr;</a>
      </div>
    </div>
  </article>
{% endfor %}
