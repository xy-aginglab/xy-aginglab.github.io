---
layout: bloom-page
permalink: /v2/projects/
title: Research
description: Research directions of the Hunan Key Laboratory of Aging Biology
---

<div class="projects">
{% assign sorted_projects = site.projects | sort: "importance" %}
<div class="grid">
  {% for project in sorted_projects %}
    {% include projects.liquid %}
  {% endfor %}
</div>
</div>
