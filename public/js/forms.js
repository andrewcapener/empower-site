// Web3Forms handler — capture phase fires before Webflow's form intercept
(function () {
  function handleForm(form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      e.stopImmediatePropagation();

      var wrapper = form.closest('.w-form');
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
    }, true); // capture phase — beats Webflow's bubble-phase listener
  }

  document.addEventListener('DOMContentLoaded', function () {
    ['wf-form-Newsletter', 'wf-form-Contact'].forEach(function (id) {
      var form = document.getElementById(id);
      if (form) handleForm(form);
    });
  });
})();
