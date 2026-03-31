---
layout: bloom
permalink: /v2/zh/publications/
title: 论文发表
lang: zh
sitemap: false
---

<div class="divide-y divide-gray-200">
  <div class="pt-6 pb-8 space-y-2 md:space-y-5">
    <h1 class="text-3xl leading-9 font-bold text-gray-800 tracking-tight sm:text-4xl sm:leading-10 md:text-6xl md:leading-14">
      论文发表
    </h1>
    <p class="text-xl leading-8 text-gray-800">
      Li Lab 发表论文。
      {% if site.data.socials.scholar_userid %}
        另见 <a href="https://scholar.google.com/citations?user={{ site.data.socials.scholar_userid }}" target="_blank" rel="noopener noreferrer">Google Scholar</a> 获取完整论文列表。
      {% endif %}
    </p>
  </div>

  <div class="all-publications">
    <h2 class="text-3xl leading-8 font-bold text-gray-800 tracking-tight mt-4 mb-4">全部论文</h2>
    {% include bib_search.liquid %}
    <div class="publications">
      {% bibliography %}
    </div>
  </div>
</div>
