document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.querySelector('.v2-topbar__toggle');
  const nav = document.querySelector('.v2-topbar__nav');
  if (!toggle || !nav) return;
  toggle.addEventListener('click', () => {
    const open = toggle.getAttribute('aria-expanded') === 'true';
    toggle.setAttribute('aria-expanded', String(!open));
    nav.classList.toggle('is-open');
  });
});
