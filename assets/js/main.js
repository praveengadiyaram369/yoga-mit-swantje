/* Yoga mit Swantje – kleine, abhängigkeitsfreie Interaktionen */
(function () {
  'use strict';
  var root = document.documentElement;
  root.classList.remove('no-js');
  root.classList.add('js');

  /* --- Navigation: Hintergrund beim Scrollen --- */
  var nav = document.getElementById('nav');
  function onScroll() { if (nav) nav.classList.toggle('scrolled', window.scrollY > 10); }
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  /* --- Mobiles Menü --- */
  var burger = document.getElementById('burger');
  var menu = document.getElementById('menu');
  if (burger && menu) {
    var setMenu = function (open) {
      menu.classList.toggle('open', open);
      document.body.classList.toggle('menu-open', open);
      burger.setAttribute('aria-expanded', String(open));
      burger.setAttribute('aria-label', open ? 'Menü schließen' : 'Menü öffnen');
    };
    burger.addEventListener('click', function () { setMenu(!menu.classList.contains('open')); });
    menu.addEventListener('click', function (e) { if (e.target.closest('a')) setMenu(false); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setMenu(false); });
  }

  /* --- Aktiver Menüpunkt --- */
  var links = document.querySelectorAll('.nav-links a[href^="#"]:not(.btn)');
  if ('IntersectionObserver' in window && links.length) {
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        links.forEach(function (a) { a.classList.toggle('active', a.getAttribute('href') === '#' + en.target.id); });
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    links.forEach(function (a) { var s = document.querySelector(a.getAttribute('href')); if (s) spy.observe(s); });
  }

  /* --- Einblenden beim Scrollen (.reveal / .reveal-stagger) --- */
  var revealEls = document.querySelectorAll('.reveal, .reveal-stagger');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        en.target.classList.add('in');
        io.unobserve(en.target);
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add('in'); });
  }

  /* --- E-Mail-Links (Spam-Schutz): Die Adresse steht nicht im HTML, sondern wird hier aus
         data-u (Name) + data-d (Domain) zusammengesetzt. Optional: data-subject = Betreff. --- */
  document.querySelectorAll('.js-mail').forEach(function (el) {
    var addr = el.getAttribute('data-u') + '@' + el.getAttribute('data-d');
    var subj = el.getAttribute('data-subject');
    el.href = 'mailto:' + addr + (subj ? '?subject=' + encodeURIComponent(subj) : '');
    if (el.textContent.indexOf('[at]') !== -1) el.textContent = addr;
  });

  /* --- Farbwelt-Umschalter (nur Demo, wird nicht gespeichert) --- */
  document.querySelectorAll('.theme-switch button').forEach(function (btn, _, all) {
    btn.addEventListener('click', function () {
      var t = btn.getAttribute('data-set');
      if (t === 'ton') root.removeAttribute('data-theme'); else root.setAttribute('data-theme', t);
      all.forEach(function (b) { b.setAttribute('aria-pressed', String(b === btn)); });
    });
  });

  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();
})();
