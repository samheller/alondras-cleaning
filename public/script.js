// Mobile nav toggle
(function () {
  const toggle = document.getElementById('navToggle');
  const nav = document.getElementById('primaryNav');
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }
  const yr = document.getElementById('yr');
  if (yr) yr.textContent = new Date().getFullYear();
})();

// Auto-save form drafts to localStorage so partial answers survive
// closing the tab, refreshing, or losing battery. One key per form.
(function () {
  document.querySelectorAll('form.contact-form').forEach(form => {
    const KEY = 'draft:' + (form.getAttribute('action') || location.pathname);
    const status = form.querySelector('.save-status');
    const setStatus = (txt) => { if (status) status.textContent = txt; };

    // Restore any saved draft
    try {
      const saved = JSON.parse(localStorage.getItem(KEY) || '{}');
      Object.entries(saved).forEach(([name, value]) => {
        const el = form.elements.namedItem(name);
        if (el && !el.value) el.value = value;
      });
      if (Object.keys(saved).length) setStatus('Tu progreso se restauró ✓');
    } catch (_) {}

    // Save on every keystroke (debounced)
    let t;
    form.addEventListener('input', () => {
      clearTimeout(t);
      t = setTimeout(() => {
        const data = {};
        Array.from(form.elements).forEach(el => {
          if (el.name && !el.name.startsWith('_') && el.type !== 'submit' && el.value) {
            data[el.name] = el.value;
          }
        });
        try {
          localStorage.setItem(KEY, JSON.stringify(data));
          setStatus('Guardado automáticamente ✓');
        } catch (_) {}
      }, 300);
    });

    // Clear draft on successful submit
    form.addEventListener('submit', () => {
      try { localStorage.removeItem(KEY); } catch (_) {}
    });
  });
})();

// Feedback page: bundle all answers and open Sam's mail client (lazy fallback).
function emailToSam(form) {
  const labelFor = (el) => {
    const lbl = form.querySelector(`label[for="${el.id}"]`);
    return lbl ? lbl.textContent.trim() : el.name;
  };
  const lines = [];
  Array.from(form.elements).forEach(el => {
    if (!el.name || el.name.startsWith('_') || el.type === 'submit' || el.type === 'button') return;
    const v = (el.value || '').trim();
    if (!v) return;
    lines.push(`${labelFor(el)}\n${v}\n`);
  });
  if (!lines.length) {
    alert('Todavía no has escrito nada — escribe algo primero.');
    return;
  }
  const subject = 'Respuestas de Alondra — sitio web';
  const body = lines.join('\n---\n\n');
  window.location.href =
    'mailto:samkheller@gmail.com'
    + '?subject=' + encodeURIComponent(subject)
    + '&body=' + encodeURIComponent(body);
}

// Contact form (Formspree fallback to mailto). Used by the public contact page.
function handleContactSubmit(e) {
  const f = e.target;
  if (!f.action || f.action.includes('REPLACE_WITH_FORMSPREE_ID')) {
    e.preventDefault();
    const get = id => (f.querySelector('#' + id) || {}).value || '';
    const subject = `Cleaning quote — ${get('name')}`;
    const body =
`Name: ${get('name')}
Phone: ${get('phone')}
Email: ${get('email')}
Service: ${get('service')}
Frequency: ${get('frequency')}

${get('message')}`;
    window.location.href =
      'mailto:alondrascleaningservicesllc@gmail.com'
      + '?subject=' + encodeURIComponent(subject)
      + '&body=' + encodeURIComponent(body);
    return false;
  }
  return true;
}
