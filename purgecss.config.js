module.exports = {
  content: ["_site/**/*.html", "_site/**/*.js"],
  css: ["_site/assets/css/*.css"],
  output: "_site/assets/css/",
  skippedContentGlobs: ["_site/assets/**/*.html"],
  safelist: {
    standard: [/^lab-/, "a", "body", "img", "h1", "h2", "h3", "h4", "h5", "h6"],
    deep: [/^lab-/],
    greedy: [/^lab-/],
  },
};
