// Toggle abstract / bibtex / award hidden blocks in publications
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".bib-btn").forEach(function (btn) {
    btn.addEventListener("click", function (e) {
      e.preventDefault();
      var parent = this.closest(".bib-content") || this.closest("li");
      if (!parent) return;

      var types = ["abstract", "bibtex", "award"];
      var clickedType = null;

      for (var i = 0; i < types.length; i++) {
        if (this.classList.contains(types[i])) {
          clickedType = types[i];
          break;
        }
      }
      if (!clickedType) return;

      var block = parent.querySelector("div." + clickedType + ".bib-hidden");
      if (!block) return;

      var isOpen = block.classList.contains("open");

      // Close all open blocks in this entry first
      types.forEach(function (type) {
        var b = parent.querySelector("div." + type + ".bib-hidden");
        if (b) b.classList.remove("open");
        var otherBtn = parent.querySelector(".bib-btn." + type);
        if (otherBtn) otherBtn.classList.remove("bib-btn--active");
      });

      // Toggle clicked block
      if (!isOpen) {
        block.classList.add("open");
        this.classList.add("bib-btn--active");
      }
    });
  });
});
