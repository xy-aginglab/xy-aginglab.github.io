---
layout: page
title: 科研方向
permalink: /zh/projects/
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
