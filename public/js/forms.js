// Web3Forms handler
// Webflow intercepts forms inside .w-form via event delegation.
// We removed .w-form from these wrappers so Webflow ignores them entirely.
(function () {
  function handleForm(form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();

      var wrapper = form.parentElement;
      var successEl = wrapper && wrapper.querySelector('.w-form-done');
      var errorEl = wrapper && wrapper.querySelector('.w-form-fail');

      if (successEl) successEl.style.display = 'none';
      if (errorEl) errorEl.style.display = 'none';

      var btn = form.querySelector('[type="submit"]');
      var originalVal = btn && (btn.value || btn.textContent);
      if (btn) { btn.value = btn.dataset.wait || 'Sending…'; btn.disabled = true; }

      fetch('https://api.web3forms.com/submit', {
        method: 'POST',
        body: new FormData(form)
      })
        .then(function (r) { return r.json(); })
        .then(function (data) {
          if (data.success) {
            form.style.display = 'none';
            if (successEl) successEl.style.display = 'block';
          } else {
            if (errorEl) errorEl.style.display = 'block';
            if (btn) { btn.value = originalVal; btn.disabled = false; }
          }
        })
        .catch(function () {
          if (errorEl) errorEl.style.display = 'block';
          if (btn) { btn.value = originalVal; btn.disabled = false; }
        });
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    ['wf-form-Newsletter', 'wf-form-Contact'].forEach(function (id) {
      var form = document.getElementById(id);
      if (form) handleForm(form);
    });
  });
})();
