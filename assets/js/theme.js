// Has to be in the head tag, otherwise a flicker effect will occur.

let determineThemeSetting = () => {
  let themeSetting = localStorage.getItem("theme");
  if (themeSetting != "dark" && themeSetting != "light" && themeSetting != "system") {
    themeSetting = "system";
  }
  return themeSetting;
};

let determineComputedTheme = () => {
  let themeSetting = determineThemeSetting();
  if (themeSetting == "system") {
    const userPref = window.matchMedia;
    if (userPref && userPref("(prefers-color-scheme: dark)").matches) {
      return "dark";
    } else {
      return "light";
    }
  } else {
    return themeSetting;
  }
};

let setThemeSetting = (themeSetting) => {
  localStorage.setItem("theme", themeSetting);
  document.documentElement.setAttribute("data-theme-setting", themeSetting);
  applyTheme();
};

let applyTheme = () => {
  let theme = determineComputedTheme();
  transTheme();
  setHighlight(theme);
  document.documentElement.setAttribute("data-theme", theme);
};

let setHighlight = (theme) => {
  const lightHighlight = document.getElementById("highlight-theme-light");
  const darkHighlight = document.getElementById("highlight-theme-dark");

  if (!lightHighlight || !darkHighlight) {
    return;
  }

  if (theme == "dark") {
    lightHighlight.media = "none";
    darkHighlight.media = "";
  } else {
    darkHighlight.media = "none";
    lightHighlight.media = "";
  }
};

let transTheme = () => {
  document.documentElement.classList.add("transition");
  window.setTimeout(() => {
    document.documentElement.classList.remove("transition");
  }, 500);
};

let toggleThemeSetting = () => {
  let themeSetting = determineThemeSetting();
  if (themeSetting == "system") {
    setThemeSetting("light");
  } else if (themeSetting == "light") {
    setThemeSetting("dark");
  } else {
    setThemeSetting("system");
  }
};

let initTheme = () => {
  let themeSetting = determineThemeSetting();
  setThemeSetting(themeSetting);

  document.addEventListener("DOMContentLoaded", function () {
    const mode_toggle = document.getElementById("light-toggle");
    if (mode_toggle) {
      mode_toggle.addEventListener("click", function () {
        toggleThemeSetting();
      });
    }
  });

  const mediaQuery = window.matchMedia("(prefers-color-scheme: dark)");
  if (mediaQuery && mediaQuery.addEventListener) {
    mediaQuery.addEventListener("change", () => {
      applyTheme();
    });
  }
};

initTheme();
