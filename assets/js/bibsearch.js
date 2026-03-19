const initBibSearch = () => {
  const input = document.getElementById("bibsearch");
  if (!input) return;

  const groups = Array.from(document.querySelectorAll(".publications ol.bibliography"));
  if (!groups.length) return;

  const cache = groups.map((group) => {
    const heading = group.previousElementSibling?.matches("h2.bibliography")
      ? group.previousElementSibling
      : null;
    const items = Array.from(group.querySelectorAll(":scope > li")).map((item) => ({
      node: item,
      text: item.textContent.toLowerCase(),
    }));

    return { heading, group, items };
  });

  const render = () => {
    const query = input.value.trim().toLowerCase();

    cache.forEach(({ heading, group, items }) => {
      let visibleCount = 0;

      items.forEach(({ node, text }) => {
        const visible = !query || text.includes(query);
        node.hidden = !visible;
        if (visible) visibleCount += 1;
      });

      const hasVisibleItems = visibleCount > 0;
      group.hidden = !hasVisibleItems;
      if (heading) heading.hidden = !hasVisibleItems;
    });
  };

  input.addEventListener("input", render);
  render();
};

document.addEventListener("DOMContentLoaded", initBibSearch);
