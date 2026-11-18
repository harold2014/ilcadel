/* =========================================================
   ILCADEL — Interacciones del sitio
   ========================================================= */
(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Año del footer ---------- */
  var year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();

  /* ---------- Header: sombra y logo compacto al hacer scroll ---------- */
  var header = document.getElementById('header');
  function onScroll() {
    if (header) header.classList.toggle('is-scrolled', window.scrollY > 36);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ---------- Menú móvil ---------- */
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('nav');

  function closeMenu() {
    if (!nav || !toggle) return;
    nav.classList.remove('is-open');
    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-label', 'Abrir menú');
  }

  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', String(open));
      toggle.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
    });
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) closeMenu();
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('is-open')) {
        closeMenu();
        toggle.focus();
      }
    });
    window.addEventListener('resize', function () {
      if (window.innerWidth > 1080) closeMenu();
    });
  }

  /* ---------- Enlace activo del menú según la sección visible ---------- */
  var navLinks = nav ? Array.prototype.slice.call(nav.querySelectorAll('a[href^="#"]')) : [];
  var sectionIds = navLinks
    .map(function (a) { return a.getAttribute('href').slice(1); })
    .filter(function (id, i, arr) { return id && arr.indexOf(id) === i; });

  if ('IntersectionObserver' in window && sectionIds.length) {
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var id = entry.target.id;
        navLinks.forEach(function (a) {
          a.classList.toggle('is-active', a.getAttribute('href') === '#' + id);
        });
      });
    }, { rootMargin: '-45% 0px -50% 0px' });

    sectionIds.forEach(function (id) {
      var el = document.getElementById(id);
      if (el) spy.observe(el);
    });
  }

  /* ---------- Revelado de elementos al hacer scroll ---------- */
  var reveals = document.querySelectorAll('.reveal');
  if (reduceMotion || !('IntersectionObserver' in window)) {
    reveals.forEach(function (el) { el.classList.add('is-visible'); });
  } else {
    var revealObs = new IntersectionObserver(function (entries, obs) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var siblings = Array.prototype.slice.call(entry.target.parentElement.children)
          .filter(function (el) { return el.classList.contains('reveal'); });
        var index = siblings.indexOf(entry.target);
        entry.target.style.transitionDelay = Math.min(index, 5) * 75 + 'ms';
        entry.target.classList.add('is-visible');
        obs.unobserve(entry.target);
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -36px 0px' });
    reveals.forEach(function (el) { revealObs.observe(el); });
  }

  /* ---------- Contador animado de las cifras del hero ---------- */
  var counters = document.querySelectorAll('[data-count]');
  function animateCount(el) {
    var target = parseInt(el.getAttribute('data-count'), 10);
    var duration = 1400;
    var start = null;
    function step(ts) {
      if (!start) start = ts;
      var p = Math.min((ts - start) / duration, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(target * eased);
      if (p < 1) requestAnimationFrame(step);
    }
    el.textContent = '0';
    requestAnimationFrame(step);
  }
  if (!reduceMotion && counters.length) {
    setTimeout(function () { counters.forEach(animateCount); }, 650);
  }

  /* ---------- Copiar cláusula arbitral ---------- */
  document.querySelectorAll('.clause-copy').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var box = btn.closest('.clause-box');
      var clause = box ? box.querySelector('.clause') : null;
      if (!clause || !navigator.clipboard) return;
      var original = btn.textContent;
      navigator.clipboard.writeText(clause.textContent.trim()).then(function () {
        btn.textContent = '¡Cláusula copiada!';
        setTimeout(function () { btn.textContent = original; }, 2200);
      });
    });
  });

  /* ---------- Lightbox para la galería ---------- */
  var galleryFigures = document.querySelectorAll('.gallery figure');
  if (galleryFigures.length) {
    var lb = document.createElement('div');
    lb.className = 'lightbox';
    lb.hidden = true;
    lb.setAttribute('role', 'dialog');
    lb.setAttribute('aria-label', 'Vista ampliada de imagen');
    lb.innerHTML = '<button type="button" class="lightbox__close" aria-label="Cerrar imagen">×</button><img class="lightbox__img" src="" alt="">';
    document.body.appendChild(lb);

    var lbImg = lb.querySelector('.lightbox__img');
    var lbClose = lb.querySelector('.lightbox__close');

    function closeLb() {
      lb.hidden = true;
      lbImg.src = '';
    }

    galleryFigures.forEach(function (fig) {
      var img = fig.querySelector('img');
      if (!img) return;
      fig.addEventListener('click', function () {
        lbImg.src = img.src;
        lbImg.alt = img.alt || 'Imagen institucional ILCADEL';
        lb.hidden = false;
        lbClose.focus();
      });
    });

    lbClose.addEventListener('click', closeLb);
    lb.addEventListener('click', function (e) {
      if (e.target === lb) closeLb();
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && !lb.hidden) closeLb();
    });
  }

  /* ---------- Formularios (contacto, mesa de partes, reclamaciones) ---------- */
  document.querySelectorAll('form.form').forEach(function (form) {
    var status = form.querySelector('.form__status');

    var messages = {
      nombre: 'Ingresa tu nombre completo.',
      telefono: 'Ingresa un teléfono válido (mínimo 7 dígitos).',
      correo: 'Ingresa un correo electrónico válido.',
      mensaje: 'Cuéntanos brevemente tu consulta.'
    };

    function validateField(input) {
      var field = input.closest('.field');
      var error = field ? field.querySelector('.field__error') : null;
      var value = input.value.trim();
      var ok = true;

      if (input.required && !value) ok = false;
      if (ok && input.type === 'email') ok = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(value);
      if (ok && input.type === 'tel') ok = value.replace(/\D/g, '').length >= 7;
      if (ok && input.type === 'file') ok = input.files && input.files.length > 0;
      if (ok && input.pattern) {
        try { ok = new RegExp('^(?:' + input.pattern + ')$').test(value); }
        catch (err) { ok = true; }
      }

      if (field) field.classList.toggle('has-error', !ok);
      if (error) error.textContent = ok ? '' : (messages[input.name] || 'Campo obligatorio.');
      input.setAttribute('aria-invalid', String(!ok));
      return ok;
    }

    var inputs = form.querySelectorAll('input[required], textarea[required]');
    inputs.forEach(function (input) {
      input.addEventListener('blur', function () { validateField(input); });
      input.addEventListener('input', function () {
        if (input.closest('.field').classList.contains('has-error')) validateField(input);
      });
    });

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (status) status.textContent = '';

      var firstInvalid = null;
      inputs.forEach(function (input) {
        if (!validateField(input) && !firstInvalid) firstInvalid = input;
      });
      if (firstInvalid) {
        firstInvalid.focus();
        return;
      }

      var btn = form.querySelector('button[type="submit"]');
      var label = btn.textContent;
      var done = form.getAttribute('data-success') || 'Gracias. Recibimos tu consulta y te contactaremos a la brevedad.';
      var token = document.querySelector('meta[name="csrf-token"]');
      var endpoint = form.getAttribute('data-endpoint');
      btn.disabled = true;
      btn.textContent = 'Enviando…';

      if (token && endpoint) {
        fetch(endpoint, {
          method: 'POST',
          headers: {
            'X-CSRF-TOKEN': token.getAttribute('content'),
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest'
          },
          body: new FormData(form)
        }).then(function (res) {
          return res.json().then(function (body) {
            return { ok: res.ok, body: body };
          }).catch(function () {
            return { ok: false, body: {} };
          });
        }).then(function (result) {
          btn.disabled = false;
          btn.textContent = label;
          if (!result.ok) {
            if (status) status.textContent = (result.body && result.body.message) || 'No se pudo registrar el reclamo. Inténtalo de nuevo.';
            return;
          }
          form.reset();
          if (status) status.textContent = (result.body && result.body.message) || done;
        }).catch(function () {
          btn.disabled = false;
          btn.textContent = label;
          if (status) status.textContent = 'No se pudo registrar el reclamo. Inténtalo de nuevo.';
        });
        return;
      }

      setTimeout(function () {
        btn.disabled = false;
        btn.textContent = label;
        form.reset();
        if (status) status.textContent = done;
      }, 900);
    });
  });

  /* ---------- Calculadora de costos arbitrales ---------- */
  var calcAmount = document.getElementById('calc-amount');
  if (calcAmount) {
    var calcMode = 'populares';
    var calcTitles = {
      populares: 'Arbitrajes populares',
      mayor: 'Mayor cuantía y contrataciones con el Estado',
      emergencia: 'Arbitraje de emergencia'
    };
    var calcTitle = document.getElementById('calc-title');
    var calcError = document.getElementById('calc-error');
    var calcResults = document.getElementById('calc-results');
    var calcSecretaryRow = document.getElementById('calc-secretary-row');

    function money(value) {
      return 'S/ ' + value.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
    }

    function quote(amount, mode) {
      if (mode === 'populares') {
        if (amount >= 1000 && amount <= 15000) return { admin: 3500, arbiter: 1500, secretary: 850 };
        if (amount > 15000 && amount <= 45000) return { admin: 6000, arbiter: 4000, secretary: 1800 };
        if (amount > 45000 && amount <= 150000) return { admin: 8500, arbiter: 6500, secretary: 2500 };
      }
      if (mode === 'mayor') {
        if (amount >= 500000 && amount <= 3000000) return { admin: 25500, arbiter: 20000, secretary: 7500 };
        if (amount > 3000000 && amount <= 10000000) return { admin: 45000, arbiter: 35000, secretary: 6500 };
        if (amount > 10000000 && amount <= 50000000) return { admin: 80500, arbiter: 74500, secretary: 10500 };
      }
      if (mode === 'emergencia' && amount >= 500000 && amount <= 3000000) {
        return { admin: 15000, arbiter: 25000, secretary: 0, subtotal: 35000, hideSecretary: true };
      }
      return null;
    }

    function renderCalc() {
      var amount = parseFloat(calcAmount.value);
      var row = Number.isFinite(amount) ? quote(amount, calcMode) : null;
      if (!row) {
        calcResults.hidden = true;
        calcError.hidden = !(amount > 0);
        return;
      }
      var subtotal = row.subtotal || (row.admin + row.arbiter + row.secretary);
      var igv = subtotal * 0.18;
      document.getElementById('calc-admin').textContent = money(row.admin);
      document.getElementById('calc-arbiter').textContent = money(row.arbiter);
      document.getElementById('calc-secretary').textContent = money(row.secretary);
      document.getElementById('calc-subtotal').textContent = money(subtotal);
      document.getElementById('calc-igv').textContent = money(igv);
      document.getElementById('calc-total').textContent = money(subtotal + igv);
      calcSecretaryRow.hidden = !!row.hideSecretary;
      calcError.hidden = true;
      calcResults.hidden = false;
    }

    document.querySelectorAll('.calc__tab').forEach(function (tab) {
      tab.addEventListener('click', function () {
        calcMode = tab.getAttribute('data-mode');
        document.querySelectorAll('.calc__tab').forEach(function (item) {
          var on = item === tab;
          item.classList.toggle('is-active', on);
          item.setAttribute('aria-selected', String(on));
        });
        calcTitle.textContent = calcTitles[calcMode];
        calcAmount.value = '';
        renderCalc();
      });
    });
    calcAmount.addEventListener('input', renderCalc);
  }

  /* ---------- WhatsApp: elegir entre los números publicados ---------- */
  var trigger = document.querySelector('.wa-float');
  if (trigger) {
    var greeting = encodeURIComponent('Hola ILCADEL, quisiera hacer una consulta.');
    var agents = [
      { mark: 'DG', role: 'Dirección General', phone: '+51 999 835 661', href: 'https://wa.me/51999835661?text=' + greeting },
      { mark: 'SG', role: 'Secretaría General', phone: '+51 987 298 765', href: 'https://wa.me/51987298765?text=' + greeting },
      { mark: 'CA', role: 'Sede Canadá', phone: '+1 825 747 5773', href: 'https://wa.me/18257475773?text=' + greeting }
    ];
    var bubble = '<svg aria-hidden="true" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5.2 16.2 4 20l3.8-1.1A8.2 8.2 0 1 0 5.2 16.2Z"/><path d="M8.8 10.6h6.4M8.8 13.6h3.6"/></svg>';
    var cross = '<svg aria-hidden="true" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M6 6l12 12M18 6 6 18"/></svg>';
    trigger.innerHTML = '<span class="wa-float__mark" aria-hidden="true">' + bubble + '</span><span class="wa-float__text"><span class="wa-float__kicker">WhatsApp</span><span class="wa-float__label">Escríbenos</span></span>';

    var dock = document.createElement('div');
    dock.className = 'wa-dock';
    var panel = document.createElement('div');
    panel.className = 'wa-panel';
    panel.id = 'wa-panel';
    panel.hidden = true;
    panel.setAttribute('role', 'dialog');
    panel.setAttribute('aria-label', 'Elegir un WhatsApp de ILCADEL');

    var head = document.createElement('div');
    head.className = 'wa-panel__head';
    head.innerHTML = '<div><div class="wa-panel__kicker">Atención inmediata</div><p class="wa-panel__title">Elige con quién hablar</p></div>';
    var closeBtn = document.createElement('button');
    closeBtn.type = 'button';
    closeBtn.className = 'wa-panel__close';
    closeBtn.setAttribute('aria-label', 'Cerrar');
    closeBtn.textContent = '×';
    head.appendChild(closeBtn);

    var list = document.createElement('div');
    list.className = 'wa-panel__list';
    agents.forEach(function (agent) {
      var link = document.createElement('a');
      link.className = 'wa-agent';
      link.href = agent.href;
      link.target = '_blank';
      link.rel = 'noopener';
      link.innerHTML = '<span class="wa-agent__mark">' + agent.mark + '</span>'
        + '<span class="wa-agent__body"><span class="wa-agent__role">' + agent.role + '</span>'
        + '<span class="wa-agent__phone">' + agent.phone + '</span></span>'
        + '<span class="wa-agent__go">Escribir</span>';
      list.appendChild(link);
    });

    panel.appendChild(head);
    panel.appendChild(list);
    trigger.parentNode.insertBefore(dock, trigger);
    dock.appendChild(panel);
    dock.appendChild(trigger);
    trigger.setAttribute('aria-expanded', 'false');
    trigger.setAttribute('aria-controls', 'wa-panel');
    trigger.setAttribute('aria-label', 'Abrir los WhatsApp de ILCADEL');

    function setOpen(open) {
      dock.classList.toggle('is-open', open);
      panel.hidden = !open;
      trigger.setAttribute('aria-expanded', String(open));
      trigger.setAttribute('aria-label', open ? 'Cerrar los WhatsApp de ILCADEL' : 'Abrir los WhatsApp de ILCADEL');
      var mark = trigger.querySelector('.wa-float__mark');
      var label = trigger.querySelector('.wa-float__label');
      if (mark) mark.innerHTML = open ? cross : bubble;
      if (label) label.textContent = open ? 'Cerrar' : 'Escríbenos';
    }

    trigger.addEventListener('click', function (e) {
      e.preventDefault();
      setOpen(panel.hidden);
    });
    closeBtn.addEventListener('click', function () {
      setOpen(false);
      trigger.focus();
    });
    document.addEventListener('click', function (e) {
      if (!panel.hidden && !dock.contains(e.target)) setOpen(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && !panel.hidden) {
        setOpen(false);
        trigger.focus();
      }
    });
  }
})();
