---
layout: v3-page
permalink: /v3/zh/contact/
title: 关于与联系
lang: zh
description: 关于李实验室及联系方式。
show_lead: false
---
<div class="v3-utility">
  <section class="v3-utility-section">
    <h2>关于实验室</h2>
    <p>李实验室依托<strong>衰老生物学湖南省重点实验室</strong>，位于中南大学湘雅医院。研究方向涵盖皮肤衰老、毛囊皮脂腺相关疾病和炎症性皮肤病，致力于临床皮肤科学与分子生物学的交叉融合。</p>
    <p>实验室由李吉教授领衔，整合长寿人群队列、多组学分析、器官培养模型和转化临床研究，推动基础发现向临床应用的转化。</p>
  </section>

  <section class="v3-utility-section">
    <h2>电子邮件</h2>
    <p><a href="mailto:{{ site.data.socials.email }}">{{ site.data.socials.email }}</a></p>
  </section>

  <section class="v3-utility-section">
    <h2>地址</h2>
    <p><a href="https://uri.amap.com/search?keyword=中南大学湘雅医院&city=长沙" target="_blank" rel="noopener noreferrer">皮肤科<br>
    中南大学湘雅医院<br>
    湖南省长沙市开福区湘雅路87号<br>
    邮编：410008</a></p>
  </section>

  {% if site.data.socials.github or site.data.socials.researchgate %}
  <section class="v3-utility-section">
    <h2>网络主页</h2>
    <div class="v3-utility-list">
      {% if site.data.socials.github %}
      <article>
        <h3>GitHub</h3>
        <p><a href="https://github.com/{{ site.data.socials.github }}" target="_blank" rel="noopener noreferrer">github.com/{{ site.data.socials.github }}</a></p>
      </article>
      {% endif %}
      {% if site.data.socials.researchgate %}
      <article>
        <h3>ResearchGate</h3>
        <p><a href="https://www.researchgate.net/profile/{{ site.data.socials.researchgate }}" target="_blank" rel="noopener noreferrer">ResearchGate 主页</a></p>
      </article>
      {% endif %}
    </div>
  </section>
  {% endif %}
</div>
