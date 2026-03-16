// create element for copy button in code blocks
const EXCLUDED_LANGUAGES = ["chartjs", "diff2html", "echarts", "geojson", "mermaid", "plotly", "vega_lite"];

var codeBlocks = document.querySelectorAll("pre");
codeBlocks.forEach(function (codeBlock) {
  var hasCode = codeBlock.querySelector("pre:not(.lineno)") || codeBlock.querySelector("code");
  if (!hasCode) return;

  var isExcluded = EXCLUDED_LANGUAGES.some(function (lang) {
    return codeBlock.querySelector("code.language-" + lang);
  });
  if (isExcluded) return;

  // create copy button
  var copyButton = document.createElement("button");
  copyButton.className = "copy";
  copyButton.type = "button";
  copyButton.ariaLabel = "Copy code to clipboard";
  copyButton.innerHTML = '<i class="fa-solid fa-clipboard"></i>';

  // get code from code block and copy to clipboard
  copyButton.addEventListener("click", function () {
    // check if code block has line numbers
    var codeElem = codeBlock.querySelector("pre:not(.lineno)") || codeBlock.querySelector("code");
    var code = codeElem.innerText.trim();

    window.navigator.clipboard.writeText(code);
    copyButton.innerHTML = '<i class="fa-solid fa-clipboard-check"></i>';

    setTimeout(function () {
      copyButton.innerHTML = '<i class="fa-solid fa-clipboard"></i>';
    }, 3000);
  });

  // create wrapper div
  var wrapper = document.createElement("div");
  wrapper.className = "code-display-wrapper";

  var parent = codeBlock.parentElement;
  parent.insertBefore(wrapper, codeBlock);
  wrapper.append(codeBlock);
  wrapper.append(copyButton);
});
