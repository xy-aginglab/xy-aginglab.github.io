---
layout: v2-page
permalink: /zh/clinical/
title: 临床研究
lang: zh
description: 连接湘雅医院临床资源与机制发现的临床项目。
show_lead: false
---
<div class="v2-utility-list">
  <div class="v2-utility-card">
    <h3>皮肤衰老队列</h3>
    <p>结合分子谱分析、生物标志物发现和衰老时钟开发的纵向表型追踪。</p>
  </div>
  <div class="v2-utility-card">
    <h3>毛发疾病</h3>
    <p>临床材料与器官培养和再生策略相结合，研究脱发和白发问题。</p>
  </div>
  <div class="v2-utility-card">
    <h3>炎症性皮肤病</h3>
    <p>基于患者来源样本，聚焦玫瑰痤疮、痤疮等炎症性皮肤病研究。</p>
  </div>
</div>

### 临床合作

如需就队列、样本或转化皮肤病学研究进行合作，请联系 [{{ site.data.socials.email }}](mailto:{{ site.data.socials.email }})。

<hr>

<div class="v2-section">
  <div class="v2-section__intro">
    <h2>相关论文</h2>
  </div>
  {% include bib_search.liquid %}
  <div class="publications">
    {% bibliography --query @*[clinical=true]* %}
  </div>
</div>
