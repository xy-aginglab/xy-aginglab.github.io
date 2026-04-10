---
layout: v3-page
permalink: /v3/zh/clinical/
title: 临床研究
lang: zh
description: 依托湘雅医院临床资源，开展机制探索与干预策略研究。
show_lead: false
---
<div class="v3-utility">
  <section class="v3-utility-section">
    <div class="v3-utility-list">
      <article>
        <h3>皮肤衰老队列</h3>
        <p>基于长寿人群的纵向表型研究，结合分子分析与生物标志物发现，推动衰老时钟的开发与验证。</p>
      </article>
      <article>
        <h3>毛发疾病</h3>
        <p>整合临床样本、器官培养与再生策略，系统研究脱发及白发的发病机制与治疗方案。</p>
      </article>
      <article>
        <h3>炎症性皮肤病</h3>
        <p>以患者来源样本为基础，围绕玫瑰痤疮、痤疮等损容性皮肤病开展疾病导向的机制与转化研究。</p>
      </article>
    </div>
  </section>

  <section class="v3-utility-section">
    <h2>临床合作</h2>
    <p>如有队列、样本或转化皮肤病学方面的合作意向，欢迎联系 <a href="mailto:{{ site.data.socials.email }}">{{ site.data.socials.email }}</a>。</p>
  </section>
</div>

<hr class="v3-divider">

<section class="v3-section">
  <div class="v3-section__intro">
    <h2>相关论文</h2>
  </div>
  <div class="v3-surface v3-publication-surface">
    <div class="publications">
      {% bibliography --query @*[clinical=true]* %}
    </div>
  </div>
</section>
