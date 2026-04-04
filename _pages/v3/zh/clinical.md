---
layout: v3-page
permalink: /v3/zh/clinical/
title: 临床研究
lang: zh
description: 连接湘雅医院临床资源与机制发现和干预设计的临床项目。
show_lead: false
---
<div class="v3-utility">
  <section class="v3-utility-section">
    <div class="v3-utility-list">
      <article>
        <h3>皮肤衰老队列</h3>
        <p>结合分子分析、生物标志物发现和衰老时钟开发的纵向表型研究。</p>
      </article>
      <article>
        <h3>毛发疾病</h3>
        <p>临床样本结合器官培养和再生策略，研究脱发与白发。</p>
      </article>
      <article>
        <h3>炎症性皮肤病</h3>
        <p>聚焦玫瑰痤疮、痤疮等损容性皮肤病的患者来源样本与疾病导向研究。</p>
      </article>
    </div>
  </section>

  <section class="v3-utility-section">
    <h2>临床合作</h2>
    <p>如需队列、样本或转化皮肤病学研究合作，请联系 <a href="mailto:{{ site.data.socials.email }}">{{ site.data.socials.email }}</a>。</p>
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
