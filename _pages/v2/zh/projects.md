---
layout: v2-page
permalink: /zh/projects/
title: 研究方向
lang: zh
description: 聚焦玫瑰痤疮与化脓性汗腺炎、毛发疾病与再生、皮肤衰老三大方向的基础、临床与转化研究。
show_lead: false
---

实验室围绕玫瑰痤疮与化脓性汗腺炎、毛发疾病与再生、皮肤衰老三大方向，开展从分子机制到临床干预的系统性研究。

{% for dir in site.data.research_directions %}
  <article class="v2-program-entry" id="{{ dir.id }}">
    <h2>{{ dir.title_zh }}</h2>
    <div class="v2-program-entry__content">
      {{ dir.narrative_zh }}
    </div>
  </article>
  {% unless forloop.last %}<hr>{% endunless %}
{% endfor %}
