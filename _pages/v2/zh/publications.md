---
layout: v2-page
permalink: /zh/publications/
title: 论文发表
lang: zh
show_lead: false
---
<div class="v2-section">
  <div class="v2-section__intro">
    <h2>代表性论文</h2>
    <p>定义实验室当前研究方向的关键论文。</p>
  </div>
  <div class="v2-pub-featured">
    {% bibliography --group_by none --query @*[selected=true]* %}
  </div>
</div>

<hr>

<div class="v2-section">
  <div class="v2-section__intro">
    <h2>完整列表</h2>
  </div>
  {% include bib_search.liquid %}
  <div class="publications">
    {% bibliography %}
  </div>
</div>
