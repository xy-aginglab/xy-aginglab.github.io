---
layout: v2-page
permalink: /zh/contact/
title: 联系我们
lang: zh
description: 中南大学湘雅医院皮肤科，衰老生物学湖南省重点实验室联系方式。
show_lead: false
---

### 联系邮箱

<a href="mailto:{{ site.data.socials.email }}" style="text-decoration:none;">{{ site.data.socials.email }}</a>

### 通讯地址

中南大学湘雅医院皮肤科<br>
湖南省长沙市开福区湘雅路87号 410008

<a href="https://maps.apple.com/?q=28.2028,112.9690" target="_blank" rel="noopener noreferrer"><i class="fas fa-map-location-dot"></i> 查看地图</a>

{% if site.data.socials.github or site.data.socials.researchgate %}
### 学术主页

{% if site.data.socials.github %}- **GitHub**: [github.com/{{ site.data.socials.github }}](https://github.com/{{ site.data.socials.github }}){% endif %}
{% if site.data.socials.researchgate %}- **ResearchGate**: [ResearchGate 主页](https://www.researchgate.net/profile/{{ site.data.socials.researchgate }}){% endif %}
{% endif %}
