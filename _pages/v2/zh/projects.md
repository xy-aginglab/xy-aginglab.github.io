---
layout: v2-page
permalink: /zh/projects/
title: 研究方向
lang: zh
description: 聚焦毛囊皮脂腺相关疾病与皮肤衰老的基础、临床与转化研究。
show_lead: false
---

实验室围绕毛囊皮脂腺相关疾病（玫瑰痤疮、脱发、白发）和皮肤衰老两大方向，开展从分子机制到临床干预的系统性研究。

{% for dir in site.data.research_directions %}
  <article class="v2-program-entry" id="{{ dir.id }}">
    <h2>{{ dir.title_zh }}</h2>
    {% if dir.id == 'skin-aging' %}
    <div class="v2-program-entry__media">
      <img src="{{ '/assets/img/research_skin_aging.png' | relative_url }}" alt="{{ dir.title_zh }}">
    </div>
    {% endif %}
    <div class="v2-program-entry__content">
      {{ dir.narrative_zh }}
    </div>
  </article>
  {% unless forloop.last %}<hr>{% endunless %}
{% endfor %}
