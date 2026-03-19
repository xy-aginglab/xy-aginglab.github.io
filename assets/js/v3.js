document.addEventListener("DOMContentLoaded", function () {
  var toggle = document.querySelector("[data-v3-nav-toggle]");
  var menu = document.querySelector("[data-v3-nav-menu]");
  var nav = document.querySelector("[data-v3-nav]");
  var prefersReducedMotion =
    window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var mobileQuery =
    window.matchMedia && window.matchMedia("(max-width: 860px)");

  function syncMenuAccessibility() {
    if (!menu || !toggle) return;
    var isMobile = mobileQuery ? mobileQuery.matches : window.innerWidth <= 860;
    var isOpen = menu.classList.contains("is-open");
    menu.setAttribute("aria-hidden", isMobile && !isOpen ? "true" : "false");
    toggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
  }

  function closeMenu() {
    if (!menu || !toggle || !nav) return;
    menu.classList.remove("is-open");
    nav.classList.remove("is-open");
    syncMenuAccessibility();
  }

  if (toggle && menu && nav) {
    syncMenuAccessibility();

    toggle.addEventListener("click", function () {
      var isOpen = menu.classList.toggle("is-open");
      nav.classList.toggle("is-open", isOpen);
      syncMenuAccessibility();
    });

    menu.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", closeMenu);
    });

    document.addEventListener("click", function (event) {
      if (!nav.contains(event.target)) {
        closeMenu();
      }
    });

    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape") {
        closeMenu();
      }
    });

    if (mobileQuery && mobileQuery.addEventListener) {
      mobileQuery.addEventListener("change", function () {
        if (!mobileQuery.matches) {
          menu.classList.remove("is-open");
          nav.classList.remove("is-open");
        }
        syncMenuAccessibility();
      });
    } else {
      window.addEventListener("resize", syncMenuAccessibility);
    }
  }

  document.querySelectorAll("[data-v3-rotator]").forEach(function (el) {
    var phrases = (el.getAttribute("data-v3-rotator") || "")
      .split("|")
      .map(function (item) {
        return item.trim();
      })
      .filter(Boolean);
    var colors = (el.getAttribute("data-v3-rotator-colors") || "")
      .split("|")
      .map(function (item) {
        return item.trim();
      });
    var backgrounds = (el.getAttribute("data-v3-rotator-backgrounds") || "")
      .split("|")
      .map(function (item) {
        return item.trim();
      });

    if (!phrases.length) return;

    var items = phrases.map(function (text, index) {
      return {
        text: text,
        color: colors[index] || "",
        background: backgrounds[index] || "",
      };
    });

    function applyTheme(item) {
      el.style.setProperty("--v3-rotator-color", item.color);
      el.style.setProperty("--v3-rotator-bg", item.background);
      el.style.color = item.color;
      el.style.background = item.background;
    }

    applyTheme(items[0]);
    el.textContent = items[0].text;

    if (items.length < 2 || prefersReducedMotion) {
      return;
    }

    var index = 0;
    var charIndex = 0;
    var deleting = false;
    var pauseEnd = Date.now() + 1500;

    function tick() {
      var now = Date.now();
      if (now < pauseEnd) {
        window.requestAnimationFrame(tick);
        return;
      }

      var item = items[index];
      applyTheme(item);

      if (!deleting) {
        charIndex += 1;
        el.textContent = item.text.substring(0, charIndex);
        if (charIndex === item.text.length) {
          deleting = true;
          pauseEnd = now + 2000;
        }
      } else {
        charIndex -= 1;
        el.textContent = item.text.substring(0, charIndex);
        if (charIndex === 0) {
          deleting = false;
          index = (index + 1) % items.length;
          applyTheme(items[index]);
        }
      }

      window.setTimeout(tick, deleting ? 30 : 60);
    }

    tick();
  });
});
