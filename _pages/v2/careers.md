---
layout: v2-page
permalink: /contact/
title: Contact Us
show_lead: false
---

### Email

<a href="mailto:{{ site.data.socials.email }}" style="text-decoration:none;">{{ site.data.socials.email }}</a>

### Address

Department of Dermatology<br>
Xiangya Hospital, Central South University<br>
87 Xiangya Road, Kaifu District<br>
Changsha, Hunan, China 410008

<a href="https://maps.apple.com/?q=28.2028,112.9690" target="_blank" rel="noopener noreferrer"><i class="fas fa-map-location-dot"></i> View on Map</a>

{% if site.data.socials.github or site.data.socials.researchgate %}
### Online

{% if site.data.socials.github %}- **GitHub**: [github.com/{{ site.data.socials.github }}](https://github.com/{{ site.data.socials.github }}){% endif %}
{% if site.data.socials.researchgate %}- **ResearchGate**: [ResearchGate profile](https://www.researchgate.net/profile/{{ site.data.socials.researchgate }}){% endif %}
{% endif %}
