---
layout: v3-page
permalink: /v3/zh/publications/
title: 论文发表
lang: zh
description: Li Lab 发表论文列表。
show_eyebrow: false
show_lead: false
hide_publication_thumbnails: true
---
<div class="v3-stack">
  <section class="v3-section">
    <div class="v3-section__intro">
      <h2>代表性论文</h2>
      <p>代表实验室当前核心研究方向的关键论文。</p>
    </div>
    <div class="v3-pub-featured">
      {% bibliography --group_by none --query @*[selected=true]* %}
    </div>
  </section>

  <hr class="v3-divider">

  <section class="v3-section">
    <div class="v3-section__intro">
      <h2>全部论文</h2>
    </div>
    <div class="v3-surface v3-publication-surface">
      {% include bib_search.liquid %}
      <div class="publications">
        {% bibliography %}
      </div>
    </div>
  </section>
</div>
