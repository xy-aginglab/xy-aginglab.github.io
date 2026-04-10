---
layout: v2-home
title: Li Lab
permalink: /zh/
lang: zh
description: 湖南省衰老生物学重点实验室 — 中南大学湘雅医院。
---
<div class="v2-home">

  <div class="v2-lab-header">
    <div>
      <h1 class="v2-lab-header__name">Li Lab</h1>
    </div>
    <div class="v2-lab-header__logo">
      <img src="{{ '/assets/img/logos/xiangya.png' | relative_url }}" alt="湘雅医院">
      <img src="{{ '/assets/img/logos/csu.png' | relative_url }}" alt="中南大学">
    </div>
  </div>

  <div class="v2-about">
    <div class="v2-about__mission">
      <p>本实验室立足<strong>临床皮肤病学</strong>与<strong>分子生物学</strong>的交叉领域，系统解码毛囊皮脂腺相关疾病（玫瑰痤疮、脱发、白发）的发病机制，并探索皮肤衰老的基本规律。通过整合患者队列、多组学分析、疾病模型与转化实验，开发靶向治疗策略，实现从基础发现到临床应用的转化。</p>
      <p>在 <em>Cell</em>、<em>Nature Medicine</em>、<em>Nature Communications</em>、<em>Science Advances</em>、<em>JAAD</em> 等期刊发表的高影响力论文，推动了我们在两大研究方向上从分子机制到临床干预的系统性进展。</p>
    </div>
    <div class="v2-about__pi">
      <img src="{{ '/assets/img/members/lj.png' | relative_url }}" alt="李吉教授">
      <div>
        <p class="v2-about__pi-name">李吉 教授</p>
        <p class="v2-about__pi-title">Li Lab 主任</p>
      </div>
    </div>
  </div>

  {% for dir in site.data.research_directions %}
  <div class="v2-topic v2-clearfix" id="{{ dir.id }}">
    <div class="v2-topic__header">
      <h2 class="v2-topic__title">{{ dir.title_zh }}</h2>
    </div>
    {% if dir.id == 'pilosebaceous' %}
    <div class="v2-topic__figure">
      <img src="{{ '/assets/img/research_hair_follicle.png' | relative_url }}" alt="毛囊皮脂腺相关疾病研究">
    </div>
    {% elsif dir.id == 'skin-aging' %}
    <div class="v2-topic__figure">
      <img src="{{ '/assets/img/research_skin_aging.png' | relative_url }}" alt="皮肤衰老研究">
    </div>
    {% endif %}
    <div class="v2-topic__body">
      {{ dir.intro_zh }}
    </div>
    <a class="v2-readmore" href="{{ dir.link_zh | default: dir.link | relative_url }}">了解更多 &rarr;</a>
  </div>
  {% endfor %}

  <div class="v2-dir-overview">
    <h2 class="v2-dir-overview__title">当前研究方向</h2>
    <div class="v2-dir-grid">
      {% for dir in site.data.research_directions %}
      <div class="v2-dir-card">
        <h3>{{ dir.title_zh }}</h3>
        <p>{{ dir.summary_zh }}</p>
        <a href="{{ dir.link_zh | default: dir.link | relative_url }}">查看详情 &rarr;</a>
      </div>
      {% endfor %}
    </div>
  </div>

  <div class="v2-footer-info">
    <div>中南大学湘雅医院皮肤科<br>湖南省长沙市开福区湘雅路87号 410008</div>
    <div>邮箱：<a href="mailto:{{ site.data.socials.email }}">{{ site.data.socials.email }}</a></div>
  </div>

</div>
