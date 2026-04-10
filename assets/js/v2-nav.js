document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.querySelector('.v2-topbar__toggle');
  const nav = document.querySelector('.v2-topbar__nav');
  if (!toggle || !nav) return;

  const close = () => {
    toggle.setAttribute('aria-expanded', 'false');
    nav.classList.remove('is-open');
  };

  toggle.addEventListener('click', (e) => {
    e.stopPropagation();
    const open = toggle.getAttribute('aria-expanded') === 'true';
    toggle.setAttribute('aria-expanded', String(!open));
    nav.classList.toggle('is-open');
  });

  // Close when clicking outside the nav
  document.addEventListener('click', (e) => {
    if (nav.classList.contains('is-open') && !nav.contains(e.target) && !toggle.contains(e.target)) {
      close();
    }
  });

  // Close when clicking a nav link
  nav.addEventListener('click', (e) => {
    if (e.target.tagName === 'A') {
      close();
    }
  });
});
