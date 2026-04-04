---
layout: v3-page
permalink: /v3/zh/contact/
title: 联系我们
lang: zh
description: 欢迎与李实验室取得联系。
show_lead: false
---
<div class="v3-utility">
  <section class="v3-utility-section">
    <h2>电子邮件</h2>
    <p><a href="mailto:{{ site.data.socials.email }}">{{ site.data.socials.email }}</a></p>
  </section>

  <section class="v3-utility-section">
    <h2>地址</h2>
    <p>皮肤科<br>
    中南大学湘雅医院<br>
    湖南省长沙市开福区湘雅路87号<br>
    邮编：410008</p>
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
