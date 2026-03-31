---
layout: bloom
title: Li Lab
permalink: /v2/zh/
lang: zh
sitemap: false
---

<div class="mx-auto max-w-4xl px-4 text-left flex flex-col">
  <div class="flex-grow">
    <h1 class="text-4xl sm:text-5xl md:text-7xl lg:text-8xl text-gray-800 select-none">
      欢迎来到 <span class="block font-bold">Li Lab</span>
    </h1>
    <p class="text-base sm:text-xl md:text-2xl lg:text-3xl text-gray-600 mt-2 lg:mt-4 select-none sm:whitespace-nowrap">
      我们研究
      <span id="rotating-text" class="italic" style="color:#a72126;background:rgba(167,33,38,0.1)">毛囊皮脂腺相关疾病</span>
      的机制
    </p>
    <p class="text-sm md:text-base lg:text-lg text-gray-500 mt-4 md:mt-6 lg:mt-12">
      <strong>Li Lab</strong> 聚焦毛囊皮脂腺相关疾病和皮肤衰老，利用实验与计算技术探究毛发疾病、炎症性皮肤病和衰老的分子机制，并将成果转化为临床应用。
    </p>
    <p class="text-sm md:text-base lg:text-lg text-gray-500 mt-2 md:mt-4 lg:mt-6">
      实验室隶属于<a href="https://www.csu.edu.cn/">中南大学</a><a href="https://www.xiangya.com.cn/">湘雅医院皮肤科</a>，同时依托国家老年疾病临床医学研究中心。实验室主任为李吉教授。
    </p>
  </div>
  <div class="text-center mt-8 md:mt-12 mb-2">
    <a href="/v2/zh/projects/"
      class="no-underline text-gray-600 hover:text-gray-600 hover:shadow-md hover:shadow-custom-orange rounded-lg bg-custom-soft p-2 overflow-hidden transition-shadow duration-200 ease-in-out text-sm md:text-base lg:text-lg">了解更多科研方向</a>
  </div>
</div>

<script>
(function() {
  var items = [
    { text: '毛囊皮脂腺相关疾病', color: '#a72126', bg: 'rgba(167,33,38,0.1)' },
    { text: '皮肤衰老', color: '#15803d', bg: 'rgba(22,163,74,0.1)' }
  ];
  var el = document.getElementById('rotating-text');
  if (!el) return;
  var index = 0;
  var charIndex = 0;
  var deleting = false;
  var pauseEnd = 0;

  function tick() {
    var now = Date.now();
    if (now < pauseEnd) { requestAnimationFrame(tick); return; }

    var item = items[index];
    if (!deleting) {
      charIndex++;
      el.textContent = item.text.substring(0, charIndex);
      el.style.color = item.color;
      el.style.background = item.bg;
      if (charIndex === item.text.length) {
        deleting = true;
        pauseEnd = now + 2000;
      }
    } else {
      charIndex--;
      el.textContent = item.text.substring(0, charIndex);
      if (charIndex === 0) {
        deleting = false;
        index = (index + 1) % items.length;
      }
    }
    setTimeout(tick, deleting ? 30 : 60);
  }
  pauseEnd = Date.now() + 1500;
  tick();
})();
</script>
