# AGENTS.md – Hinweise für KI-Assistenten (Website „Yoga mit Swantje“)

Diese Datei zuerst lesen (bzw. an den Anfang eines Chats kopieren), bevor an der Website gearbeitet wird.

## Projekt
- **Kundin:** Swantje *(Nachname noch offen)*, Yogalehrerin in Montabaur (Westerwald, Rheinland-Pfalz)
- **Marke:** „Yoga mit Swantje“, geplante Domain `www.yoga-mit-swantje.de` (noch Platzhalter)
- **Zielgruppe:** Menschen aus Montabaur und Umgebung, viele Einsteiger, außerdem Firmen (Firmenyoga)
- **Hosting:** Cloudflare (Workers & Pages) über GitHub, kein Build-Schritt
- **Status:** Demo-Entwurf. Swantje hat noch keine Fotos und Texte.

## Regeln
- Alle sichtbaren Inhalte auf **Deutsch**, korrekte Umlaute und ß. Anrede **„du“** (bis Swantje anders entscheidet).
- Ton: warm, ruhig, persönlich, konkret. Keine Yoga-Klischees („Finde deine innere Mitte“, „Namaste“-Kitsch).
- **Keine Fakten erfinden**: keine Ausbildungen/Zertifikate, Jahre, Preise, Zeiten, Adressen, Bewertungen.
  Unbekanntes als Platzhalter: `<span class="ph" title="Was fehlt / Frage an Swantje">[Platzhalter]</span>`.
- Beispiel-Stimmen immer sichtbar mit `<span class="tag tag-example">Beispiel</span>` kennzeichnen.
- **Keine externen Ressourcen**: keine Google Fonts, kein CDN, keine Tracker, keine Karten-/Video-Embeds,
  keine Social-Media-Plugins. Einfache Links nach außen sind ok. Sonst `datenschutz.html` anpassen.
- Keine Frameworks, kein npm: nur HTML + `assets/css/style.css` + `assets/js/main.js`.
- **Kein Kontaktformular und keine Telefonnummer** (Spam). E-Mail-Adressen nie im Klartext:
  `<a class="js-mail" data-u="hallo" data-d="yoga-mit-swantje.de" data-subject="Anfrage Probestunde">hallo [at] yoga-mit-swantje.de</a>`
- `404.html` nutzt root-absolute Pfade (`/assets/...`). Alle anderen Seiten relative Pfade.
- `kunde/` enthält private Unterlagen: nie verlinken, nie aus `.gitignore` / `.assetsignore` entfernen.
- Neue Unterseiten in `sitemap.xml` eintragen. `entwuerfe/` bleibt unverlinkt und `noindex`.
- Bewegung immer mit `prefers-reduced-motion` abschalten (globaler Block am Ende von style.css).
- Mobile first; jede Änderung bei 390 px Breite prüfen.

## Design-System „Ton & Atem“ (assets/css/style.css → :root)
- Idee: Westerwälder Steinzeug (Creme, Kobaltblau, gebrannter Ton) + Ringe (Drehrillen / Atemkreise).
- Farben: `--paper #f4efe7`, `--paper-2 #ebe4d8`, `--card #fbf8f3`, `--stone #cfc8bc`, `--ink #1c2240`,
  `--text #2b2d38`, `--muted #686873`, `--accent #2f4c9c` (Kobalt), `--accent-lt #a9b9ea`,
  `--clay #b4623b` (Ton), `--clay-lt #e9b796`, `--line rgba(28,34,64,.13)`
- Immer Variablen verwenden, nie Hex-Werte direkt in Komponenten (sonst funktionieren die Farbwelten nicht).
- Schriften: `--f-display` Fraunces 300 (Überschriften; ein Wort kursiv mit `<em>` → Tonfarbe),
  `--f-text` Figtree 400/500/600 (Fließtext, Buttons, Labels).
- Sektion: `<section class="section">` (hell) / `section alt` (abgesetzt) / `section on-dark` (Nachtblau).
- Sektionskopf: `<div class="section-head"><span class="eyebrow">Titel</span><h2>… <em>Wort</em></h2><p>…</p></div>`
- Buttons: `btn btn-primary` · `btn btn-ghost` · auf dunkel `btn btn-light` / `btn btn-line-light`; Textlink `link-arrow`.
- Einblenden: `reveal` (Element) bzw. `reveal-stagger` (Kinder nacheinander).
- SVG-Bausteine sind oben in `index.html` als `<symbol>` definiert: `#i-mark` (Logo), `#i-rings`, `#i-slot`, `#i-cam`, `#i-arrow`, `#i-quote`.
  Inhalte von `<use>` erben CSS-Variablen, lassen sich aber nicht per Selektor stylen.
- Ornamentband: `<div class="ornament" aria-hidden="true"></div>` (CSS-Maske, färbt sich mit `--accent`).

## Demo-Modus
- `<body class="demo">` zeigt: gelbe Platzhalter (`.ph`), Demo-Leiste, Foto-Notizen (`.slot-note`),
  Hinweisboxen (`.note-demo`), Farbwelt-Umschalter (`.theme-switch`).
- Livegang: `class="demo"` in allen HTML-Dateien entfernen; vorher alle `.ph` ersetzen
  (`grep -n 'class="ph\|ph"' *.html`).

## Häufige Aufgaben
- **Foto einsetzen:** Datei nach `assets/img/fotos/`; im `<figure class="slot …">` das `<svg class="slot-art">` durch
  `<img src="assets/img/fotos/NAME.jpg" alt="…" width="…" height="…" loading="lazy">` ersetzen, `figcaption.slot-note` löschen,
  Fotograf/in im Impressum (Bildnachweis) nennen.
- **Kurs im Stundenplan:** im passenden `.day` einen `<div class="class">` kopieren (time, b, `.level` mit `data-l="1|2|3"`, small).
  Neuer Tag: ganzen `.day`-Block kopieren.
- **Preis ändern:** `#preise` → `.price` → `.amount`.
- **Angebot entfernen:** `<article class="offer">` löschen; im Desktop-Raster (`.offers`, 6 Spalten) ggf. `wide` anpassen.
- **Buchungstool verlinken:** in `.booking` und `.contact-more` den Platzhalter durch einen normalen Link
  (`target="_blank" rel="noopener"`) ersetzen. **Kein Widget einbetten.** Abschnitt in `datenschutz.html` (Punkt 5) ergänzen.
- **Farbwelt festlegen:** Werte des gewählten `[data-theme]`-Blocks in `:root` übernehmen, Alternativen + `.theme-switch` (HTML, CSS, JS) löschen.
- **E-Mail ändern:** `data-u` / `data-d` aller `.js-mail`-Links in index.html, impressum.html, datenschutz.html.
- **Domain ändern:** `yoga-mit-swantje.de` in index.html (canonical, OG, JSON-LD), robots.txt, sitemap.xml ersetzen.
- **Favicon/OG-Bild neu:** `assets/img/icons/favicon.svg` ist die Quelle; PNGs/ICO daraus rendern (z. B. Headless Chrome + Python PIL).
