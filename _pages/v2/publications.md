---
layout: bloom
permalink: /v2/publications/
title: Papers
---

<!-- Papers.vue: divide-y divide-gray-200 -->
<div class="divide-y divide-gray-200">
  <!-- Header: pt-6 pb-8 space-y-2 md:space-y-5 -->
  <div class="pt-6 pb-8 space-y-2 md:space-y-5">
    <h1 class="text-3xl leading-9 font-bold text-gray-800 tracking-tight sm:text-4xl sm:leading-10 md:text-6xl md:leading-14">
      Papers
    </h1>
    <p class="text-xl leading-8 text-gray-800">
      Papers from the Aging Biology Lab.
    </p>
  </div>

  <!-- All publications -->
  <div class="all-publications">
    {% include bib_search.liquid %}
    <div class="publications">
      {% bibliography %}
    </div>
  </div>
</div>
