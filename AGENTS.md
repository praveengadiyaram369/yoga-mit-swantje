# AGENTS.md – Hinweise für KI-Assistenten (Website „YoMaNa“)

Diese Datei zuerst lesen (bzw. an den Anfang eines Chats kopieren), bevor an der Website gearbeitet wird.

## Projekt
- **Kundin:** Swantje Aller, Yogalehrerin in Montabaur (Westerwald, Rheinland-Pfalz)
- **Marke:** „YoMaNa“ = **Yo**ga · **Ma**ssage · **Na**maste, Wortmarke `Yo<em>Ma</em>Na`. Domain `www.yomana.de`.
  E-Mail-Adresse: `info@yomana.de` (bestätigt).
- **Buchung:** Gruppenkurse laufen über Yogaresa (Montabaur): nur verlinken auf https://yogaresa.de/kurse/
  (Zeiten, Preise, Anmeldung macht Yogaresa). Massagen (in der Hebammen Praxis Montabaur) buchbar über
  https://yogaresa.de/massagen/ oder persönlich. Einzelstunden: persönlich per E-Mail / Kontaktseite.
  Keine Online-Stunden. Instagram: @Yo_Ma_Na (instagram.com/yo_ma_na). E-Mail-Postfach bei manitu.
  Kein eigener Stundenplan, keine Preisliste, kein Buchungs-Widget auf der Website.
- **Zielgruppe:** Menschen aus Montabaur und Umgebung, viele Einsteiger, außerdem Firmen (Firmenyoga)
- **Hosting:** manitu (Apache, FTP/FTPS), kein Build-Schritt. Hochladen: `python3 scripts/deploy_ftp.py` (Zugangsdaten in `ftp.yml`,
  nur lokal, in .gitignore; Vorlage `ftp.example.yml`; lädt nur Website-Dateien). Server-Einstellungen in `.htaccess`. Kein Cloudflare.
- **Status:** Live-Fassung (Demo-Modus entfernt). Fotos vorhanden (Herbst, draußen; Originale in `images/`, nicht veröffentlicht), Texte fehlen noch.

## Seiten
- `index.html` (Start: Hero, Name, Kurz-Über-mich, Angebots-Teaser, Einblicke) · `ueber-mich.html` (Geschichte, Privat-Fotos)
  · `angebot.html` (alle Angebote inkl. Massagen) · `erste-stunde.html` (Schritte, FAQ) · `kontakt.html` (Kontakt, Anfahrt)
  · `impressum.html` · `datenschutz.html` · `404.html`
- Kein Build: **Navigation, Footer, SVG-Symbole und Probestunde-Band (`.cta-band`) sind in jeder Seite kopiert.**
  Änderungen daran in ALLEN Seiten machen. Aktuelle Seite im Menü: `aria-current="page"`.

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
  `<a class="js-mail" data-u="info" data-d="yomana.de" data-subject="Anfrage Probestunde">info [at] yomana.de</a>`
- `404.html` nutzt root-absolute Pfade (`/assets/...`). Alle anderen Seiten relative Pfade.
- `kunde/` enthält private Unterlagen: nie verlinken, nie aus `.gitignore` / `.assetsignore` entfernen.
- Neue Unterseiten in `sitemap.xml` eintragen. `entwuerfe/` bleibt unverlinkt und `noindex`.
- Bewegung immer mit `prefers-reduced-motion` abschalten (globaler Block am Ende von style.css).
- Mobile first; jede Änderung bei 390 px Breite prüfen.

## Design-System „Ton & Atem“ (assets/css/style.css → :root)
- Farbwelt „Pflaume & Abendlicht“ (final, von Swantje gewählt) + Ringe (Atemkreise) als Motiv.
- Farben: `--paper #f5eee9`, `--paper-2 #ece0da`, `--card #fcf7f4`, `--stone #d7c6c0`, `--ink #2a1c2b`,
  `--text #33282f`, `--muted #6a5d65`, `--accent #7b4a6f` (Pflaume), `--accent-lt #e0b5d4`,
  `--clay #b06a40` (Abendlicht/Ton), `--clay-lt #f0c19f` (Aprikose), `--line rgba(42,28,43,.13)`
- Favicon, Logo-Datei und OG-Bild sind in diesen Farben. Es gibt keinen Farbwelt-Umschalter mehr.
- Immer Variablen verwenden, nie Hex-Werte direkt in Komponenten (Farben nur in `:root` ändern).
- Schriften: `--f-display` Fraunces 300 (Überschriften; ein Wort kursiv mit `<em>` → Tonfarbe),
  `--f-text` Figtree 400/500/600 (Fließtext, Buttons, Labels).
- Sektion: `<section class="section">` (hell) / `section alt` (abgesetzt) / `section on-dark` (Nachtblau).
- Sektionskopf: `<div class="section-head"><span class="eyebrow">Titel</span><h2>… <em>Wort</em></h2><p>…</p></div>`
- Buttons: `btn btn-primary` · `btn btn-ghost` · auf dunkel `btn btn-light` / `btn btn-line-light`; Textlink `link-arrow`.
- Einblenden: `reveal` (Element) bzw. `reveal-stagger` (Kinder nacheinander).
- SVG-Bausteine sind oben in `index.html` als `<symbol>` definiert: `#i-mark` (Logo), `#i-rings`, `#i-slot`, `#i-cam`, `#i-arrow`.
  Inhalte von `<use>` erben CSS-Variablen, lassen sich aber nicht per Selektor stylen.
- Ornamentband: `<div class="ornament" aria-hidden="true"></div>` (CSS-Maske, färbt sich mit `--accent`).

## Demo-Modus
- `<body class="demo">` zeigt: gelbe Platzhalter (`.ph`), Demo-Leiste, Foto-Notizen (`.slot-note`),
  Hinweisboxen (`.note-demo`).
- Livegang: `class="demo"` in allen HTML-Dateien entfernen; vorher alle `.ph` ersetzen
  (`grep -n 'class="ph\|ph"' *.html`).

## Häufige Aufgaben
- **Fotos aufbereiten:** Original in `images/` ablegen, mit PIL je 600 px und 1200 px breit als JPEG nach
  `assets/img/fotos/NAME-600.jpg` / `NAME-1200.jpg` speichern (ohne EXIF), im HTML per `srcset` einbinden.
- **Galerie „Einblicke“:** `<ul class="gallery">` in index.html; `g-tall` = 2 Zeilen hoch, `g-wide` = 2 Spalten breit (Desktop-Mosaik).
- **Foto einsetzen:** Datei nach `assets/img/fotos/`; im `<figure class="slot …">` das `<svg class="slot-art">` durch
  `<img src="assets/img/fotos/NAME.jpg" alt="…" width="…" height="…" loading="lazy">` ersetzen, `figcaption.slot-note` löschen,
  Fotograf/in im Impressum (Bildnachweis) nennen.
- **Angebot entfernen:** `<article class="offer">` löschen; im Desktop-Raster (`.offers`, 6 Spalten) ggf. `wide` anpassen.
- **E-Mail ändern:** `data-u` / `data-d` aller `.js-mail`-Links in index.html, impressum.html, datenschutz.html.
- **Domain ändern:** `yomana.de` in index.html (canonical, OG, JSON-LD), robots.txt, sitemap.xml ersetzen.
- **Favicon/OG-Bild neu:** `assets/img/icons/favicon.svg` ist die Quelle; PNGs/ICO daraus rendern (z. B. Headless Chrome + Python PIL).
