/* Folio – main.js */

// ── Client-side book search filter ─────────────────────────────────────
const searchInput = document.getElementById('bookSearch');
if (searchInput) {
  searchInput.addEventListener('input', () => {
    const q = searchInput.value.toLowerCase().trim();
    const items = document.querySelectorAll('.book-item');
    let visible = 0;
    items.forEach(item => {
      const match = item.dataset.title.includes(q) || item.dataset.author.includes(q);
      item.style.display = match ? '' : 'none';
      if (match) visible++;
    });
    const noResults = document.getElementById('noResults');
    if (noResults) noResults.classList.toggle('d-none', visible > 0);
  });
}

// ── Auto-dismiss flash messages after 5 s ──────────────────────────────
document.querySelectorAll('.alert').forEach(el => {
  setTimeout(() => {
    const bsAlert = bootstrap.Alert.getOrCreateInstance(el);
    bsAlert.close();
  }, 5000);
});

// ── Smooth navbar background on scroll ────────────────────────────────
const nav = document.getElementById('mainNav');
if (nav) {
  window.addEventListener('scroll', () => {
    nav.style.boxShadow = window.scrollY > 20 ? '0 2px 20px rgba(0,0,0,.3)' : 'none';
  });
}
