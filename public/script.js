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

// Contact form handler.
//
// If the form's `action` still contains REPLACE_WITH_FORMSPREE_ID, fall back
// to opening the user's mail client. Once you sign up at formspree.io and
// paste the real form ID into the `action` URL, the form will POST natively
// (no JS needed) and Alondra will get an email with the submission.
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
  // Formspree is configured — let the browser POST the form natively.
  return true;
}
