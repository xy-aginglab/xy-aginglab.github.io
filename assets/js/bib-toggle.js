// Toggle abstract / bibtex / award hidden blocks in publications
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".bib-btn").forEach(function (btn) {
    btn.addEventListener("click", function (e) {
      e.preventDefault();
      // Find the matching hidden block by class name (abstract, bibtex, award)
      var classes = this.classList;
      var parent = this.closest(".bib-content") || this.closest("li");
      if (!parent) return;

      ["abstract", "bibtex", "award"].forEach(function (type) {
        if (classes.contains(type)) {
          var block = parent.querySelector("div." + type + ".bib-hidden");
          if (block) {
            block.classList.toggle("open");
          }
        }
      });
    });
  });
});
