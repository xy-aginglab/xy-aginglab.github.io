---
layout: page
title: 科研方向
permalink: /v1/zh/projects/
lang: zh
---

{% assign sorted_projects = site.projects | sort: "importance" %}
<div class="projects">
  <div class="grid">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
</div>
