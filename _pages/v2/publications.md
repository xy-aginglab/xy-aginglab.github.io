---
layout: bloom
permalink: /v2/publications/
title: Papers
sitemap: false
---

<div class="divide-y divide-gray-200">
  <div class="pt-6 pb-8 space-y-2 md:space-y-5">
    <h1 class="text-3xl leading-9 font-bold text-gray-800 tracking-tight sm:text-4xl sm:leading-10 md:text-6xl md:leading-14">
      Papers
    </h1>
    <p class="text-xl leading-8 text-gray-800">
      Papers from the Li Lab.
      {% if site.data.socials.scholar_userid %}
        See also <a href="https://scholar.google.com/citations?user={{ site.data.socials.scholar_userid }}" target="_blank" rel="noopener noreferrer">Google Scholar</a> for a complete list of publications.
      {% endif %}
    </p>
  </div>

  <div class="selected-publications mb-8">
    <h2 class="text-3xl leading-8 font-bold text-gray-800 tracking-tight mt-4 mb-4">Key Papers</h2>
    <h3 class="text-lg leading-7 text-gray-600 tracking-tight mt-4 mb-4">These papers exemplify key current areas of research in the lab.</h3>
    <div class="grid grid-cols-2 gap-4">

      <div class="hover:shadow-lg hover:shadow-custom-orange flex flex-col gap-px rounded-lg w-full h-full overflow-hidden transition-shadow duration-300 ease-in-out">
        <a href="https://doi.org/10.1016/j.cell.2026.01.036" target="_blank" rel="noopener noreferrer" class="flex-grow bg-custom-soft no-underline p-4">
          <h3 class="m-0 text-gray-800 font-semibold text-lg leading-6 ease-in-out pb-2">Metabolite-gated vascular contractility switch: OXGR1 activation mechanism</h3>
          <span class="m-0 font-medium text-gray-600 pt-1 text-base">Cell. 2026</span>
        </a>
      </div>

      <div class="hover:shadow-lg hover:shadow-custom-orange flex flex-col gap-px rounded-lg w-full h-full overflow-hidden transition-shadow duration-300 ease-in-out">
        <a href="https://doi.org/10.1038/s41467-026-70153-4" target="_blank" rel="noopener noreferrer" class="flex-grow bg-custom-soft no-underline p-4">
          <h3 class="m-0 text-gray-800 font-semibold text-lg leading-6 ease-in-out pb-2">Single-cell transcriptomics reveals hair growth retardation in androgenetic alopecia</h3>
          <span class="m-0 font-medium text-gray-600 pt-1 text-base">Nature Communications. 2026</span>
        </a>
      </div>

      <div class="hover:shadow-lg hover:shadow-custom-orange flex flex-col gap-px rounded-lg w-full h-full overflow-hidden transition-shadow duration-300 ease-in-out">
        <a href="https://doi.org/10.1038/s43587-025-00935-w" target="_blank" rel="noopener noreferrer" class="flex-grow bg-custom-soft no-underline p-4">
          <h3 class="m-0 text-gray-800 font-semibold text-lg leading-6 ease-in-out pb-2">The X-Age Project to construct a Chinese aging clock</h3>
          <span class="m-0 font-medium text-gray-600 pt-1 text-base">Nature Aging. 2025</span>
        </a>
      </div>

      <div class="hover:shadow-lg hover:shadow-custom-orange flex flex-col gap-px rounded-lg w-full h-full overflow-hidden transition-shadow duration-300 ease-in-out">
        <a href="https://doi.org/10.1038/s41467-024-52946-7" target="_blank" rel="noopener noreferrer" class="flex-grow bg-custom-soft no-underline p-4">
          <h3 class="m-0 text-gray-800 font-semibold text-lg leading-6 ease-in-out pb-2">Single-cell transcriptomics reveals aberrant skin cells and fibroblasts in rosacea</h3>
          <span class="m-0 font-medium text-gray-600 pt-1 text-base">Nature Communications. 2024</span>
        </a>
      </div>

      <div class="hover:shadow-lg hover:shadow-custom-orange flex flex-col gap-px rounded-lg w-full h-full overflow-hidden transition-shadow duration-300 ease-in-out">
        <a href="https://doi.org/10.1038/s41467-024-50970-1" target="_blank" rel="noopener noreferrer" class="flex-grow bg-custom-soft no-underline p-4">
          <h3 class="m-0 text-gray-800 font-semibold text-lg leading-6 ease-in-out pb-2">High-sensitive sensory neurons exacerbate rosacea-like dermatitis by activating gamma-delta T cells</h3>
          <span class="m-0 font-medium text-gray-600 pt-1 text-base">Nature Communications. 2024</span>
        </a>
      </div>

      <div class="hover:shadow-lg hover:shadow-custom-orange flex flex-col gap-px rounded-lg w-full h-full overflow-hidden transition-shadow duration-300 ease-in-out">
        <a href="https://doi.org/10.1038/s41467-023-39761-2" target="_blank" rel="noopener noreferrer" class="flex-grow bg-custom-soft no-underline p-4">
          <h3 class="m-0 text-gray-800 font-semibold text-lg leading-6 ease-in-out pb-2">Whole genome sequencing identifies genetic variants associated with neurogenic inflammation in rosacea</h3>
          <span class="m-0 font-medium text-gray-600 pt-1 text-base">Nature Communications. 2023</span>
        </a>
      </div>

      <div class="hover:shadow-lg hover:shadow-custom-orange flex flex-col gap-px rounded-lg w-full h-full overflow-hidden transition-shadow duration-300 ease-in-out">
        <a href="https://doi.org/10.1126/sciadv.abf2017" target="_blank" rel="noopener noreferrer" class="flex-grow bg-custom-soft no-underline p-4">
          <h3 class="m-0 text-gray-800 font-semibold text-lg leading-6 ease-in-out pb-2">ETS1 acts as a regulator of human healthy aging via decreasing ribosomal activity</h3>
          <span class="m-0 font-medium text-gray-600 pt-1 text-base">Science Advances. 2022</span>
        </a>
      </div>

    </div>
  </div>

  <div class="all-publications">
    <h2 class="text-3xl leading-8 font-bold text-gray-800 tracking-tight mt-4 mb-4">All Papers</h2>
    <h3 class="text-lg leading-7 text-gray-600 tracking-tight mt-4 mb-4">Below is a complete list of primary research papers from our group.</h3>
    {% include bib_search.liquid %}
    <div class="publications">
      {% bibliography %}
    </div>
  </div>
</div>
