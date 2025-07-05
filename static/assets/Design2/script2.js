// script.js

// Smooth scroll (optional enhancement)
document.querySelectorAll('nav a').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    if (this.getAttribute('href').startsWith('#')) {
      e.preventDefault();
      const section = document.querySelector(this.getAttribute('href'));
      if (section) {
        section.scrollIntoView({ behavior: 'smooth' });
      }
    }
  });
});
