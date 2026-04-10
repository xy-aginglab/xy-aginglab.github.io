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
      <h1 class="v2-lab-header__name" translate="no">Li Lab</h1>
    </div>
    <div class="v2-lab-header__logo">
      <img src="{{ '/assets/img/logos/xiangya.png' | relative_url }}" alt="湘雅医院">
      <img src="{{ '/assets/img/logos/csu.png' | relative_url }}" alt="中南大学">
    </div>
  </div>

  <div class="v2-about">
    <div class="v2-about__pi">
      <img src="{{ '/assets/img/members/lj.png' | relative_url }}" alt="李吉教授">
      <div>
        <p class="v2-about__pi-name">李吉 教授</p>
        <p class="v2-about__pi-title"><span translate="no">Li Lab</span> 主任</p>
      </div>
    </div>
    <div class="v2-about__mission">
      <p>实验室致力于临床皮肤病学与基础及转化医学的深度融合，聚焦<em style="font-style:normal;font-weight:700;">毛囊皮脂腺相关疾病</em>，重点涵盖<em style="font-style:normal;">玫瑰痤疮</em>、<em style="font-style:normal;">脱发</em>及<em style="font-style:normal;">白发</em>。依托丰富的临床病例资源，将临床实践与疾病规律、自然病程及疗效评价的临床研究深度结合，并开展系统的机制探索。通过建立患者队列，运用多组学技术、疾病模型及转化研究手段，阐明发病机制，推动靶向治疗策略开发，包括创新药物与疗法的临床试验。</p>
      <p>实验室同时探索<em style="font-style:normal;font-weight:700;">皮肤衰老</em>的核心机制，寻求新型抗衰老干预手段。融合临床经验、生物学发现与治疗创新，推动皮肤病精准诊疗发展。</p>
      <p>相关成果发表于 <em>Cell</em>、<em>BMJ</em>、<em>Nature Medicine</em>、<em>Nature Communications</em>、<em>Developmental Cell</em>、<em>Science Advances</em>、<em>JAMA Dermatology</em>、<em>JAAD</em> 及 <em>JID</em> 等期刊。</p>
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
