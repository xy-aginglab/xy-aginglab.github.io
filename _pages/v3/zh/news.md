---
layout: v3-page
permalink: /v3/zh/news/
title: 新闻动态
lang: zh
description: 实验室最新动态与成果。
show_lead: false
content_offset_right: true
---
<div class="v3-utility">
  {% if site.news != blank %}
    <section class="v3-utility-section">
      <div class="news">
        {% include news.liquid %}
      </div>
    </section>
  {% else %}
    <section class="v3-utility-section">
      <p class="v3-utility-note">暂无新闻。请浏览<a href="{{ '/v3/zh/publications/' | relative_url }}">论文发表</a>或<a href="{{ '/v3/zh/careers/' | relative_url }}">招聘信息</a>获取最新动态。</p>
    </section>
  {% endif %}
</div>
