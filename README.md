# Yoga mit Swantje · Website

Website für **Yoga mit Swantje**, Yogalehrerin in Montabaur (Westerwald).
Statisches HTML/CSS/JS ohne Framework und ohne Build-Schritt, gehostet bei **manitu** (Deployment per `git push`).

**Status:** Erster Demo-Entwurf zur Abstimmung mit der Kundin (November 2026). Swantje hat noch keine Fotos und Texte.
Der Entwurf soll ihr zeigen, wie die Seite aussehen kann, welche Inhalte sie liefern muss und welche Entscheidungen anstehen.
**Domain:** `www.yomana.de` (Yoga · Massage · Namaste) *(steht in canonical, OG-Tags, JSON-LD, sitemap.xml, robots.txt)*

---

## Projektstruktur

```
yoga-mit-swantje/
├── index.html              ← Startseite (One-Pager mit allen Sektionen)
├── impressum.html          ← Impressum (§ 5 DDG, § 18 Abs. 2 MStV) – Entwurf
├── datenschutz.html        ← Datenschutzerklärung (DSGVO) – Entwurf
├── 404.html                ← Fehlerseite (absolute Pfade /assets/…, da Cloudflare sie unter jeder URL ausliefert)
├── favicon.ico             ← bleibt im Hauptordner (Browser fragen /favicon.ico direkt ab)
├── robots.txt · sitemap.xml
├── README.md · AGENTS.md   ← Dokumentation (werden nicht veröffentlicht, siehe .assetsignore)
│
├── assets/
│   ├── css/style.css       ← gesamtes Design (Farben & Schriften als Variablen ganz oben)
│   ├── js/main.js          ← Menü, Einblenden, E-Mail-Links (Spam-Schutz)
│   ├── fonts/              ← Fraunces + Figtree als woff2, lokal (keine Google-Server)
│   └── img/
│       ├── logo/           ← logo-zeichen.svg (Bildmarke Entwurf A)
│       ├── fotos/          ← hier kommen Swantjes Fotos hin (noch leer)
│       ├── icons/          ← favicon.svg, favicon-32.png, apple-touch-icon.png, icon-512.png
│       └── social/         ← og-image.jpg (1200×630, Vorschaubild beim Teilen)
│
├── entwuerfe/
│   └── logo-entwuerfe.html ← 3 Logo-Ideen für Swantje (nicht verlinkt, noindex)
│
├── scripts/
│   └── push_changes.sh     ← Änderungen committen + pushen
│
└── kunde/                  ← Kundenunterlagen – NICHT auf GitHub, NICHT online (.gitignore + .assetsignore)
```

## Seitenaufbau (index.html)

1. Demo-Hinweisleiste (nur mit `class="demo"`)
2. Navigation: Bildmarke + Schriftzug, CTA „Probestunde anfragen“
3. **Hero**: „Yoga in deinem Tempo.“ + Atemkreis (atmet langsam: 4 s ein, 1 s halten, 5 s aus)
4. **Über mich**: Foto-Slot (Porträt), Text, Steckbrief (Ausbildung etc. als Platzhalter), 3 Werte
5. **Angebot**: Kurse in der Gruppe, Einzelstunden, Workshops & Retreats, Yoga für Unternehmen, Online + Yogastile (Beispiele)
6. **Stundenplan**: Beispielwoche (alle Zeiten erfunden & markiert) + Platz für Buchungstool-Link
7. **Preise**: Probestunde · 10er-Karte · Einzelstunde (alle Preise Platzhalter) + Hinweis § 19 UStG / Krankenkasse
8. **Ort & Anfahrt**: gezeichnete Karte (kein Embed), Adresse, Parken/Bahn/Mitbringen, OpenStreetMap-Link
9. **Deine erste Stunde**: 3 Schritte + FAQ (aufklappbar, `<details>`)
10. **Stimmen**: 3 Karten, sichtbar als „Beispiel“ gekennzeichnet
11. **Kontakt**: E-Mail groß + drei E-Mail-Buttons mit vorbereitetem Betreff
    (**bewusst kein Formular und keine Telefonnummer**: frühere Formulare wurden zugespammt)
12. Footer mit Ornamentband

## Designidee: „Pflaume & Abendlicht“

Warmes, helles Grundpapier, tiefe Pflaume für Text, Navigation und dunkle Flächen, Abendlicht/Ton
und Aprikose als warme Akzente. Das wiederkehrende Motiv sind **Ringe** (Atemkreise), dazu ein
Ornamentband als Trenner. Die Fotos (Herbstwiese, Holzskulptur, Klangschalen) tragen die Seite.

| Token | Wert | Verwendung |
|---|---|---|
| `--paper` | `#f5eee9` | Seitenhintergrund |
| `--paper-2` | `#ece0da` | abgesetzte Sektionen |
| `--card` | `#fcf7f4` | Karten |
| `--ink` | `#2a1c2b` | Überschriften, dunkle Flächen |
| `--accent` | `#7b4a6f` | Pflaume (Markenfarbe, Links, Labels) |
| `--clay` | `#b06a40` | Abendlicht/Ton (kursive Wörter, Punkte) |
| `--clay-lt` | `#f0c19f` | Aprikose (auf dunklem Grund, Atemkreis) |
| Schriften | Fraunces 300/400 (+ kursiv) für Überschriften, Figtree 400/500/600 für Text |

Die Farbwelt ist final (Swantjes Wahl). Farben nur in `:root` in `style.css` ändern.

Animationen sind dezent (Einblenden, Atemkreis) und werden bei `prefers-reduced-motion` komplett abgeschaltet.

## Bilder

Es gibt noch **keine Fotos**. Bewusst wurden **keine Stockfotos** verwendet: Ein fremdes Gesicht auf der
Seite einer Einzelperson wirkt schnell wie Swantje selbst und wäre irreführend. Stattdessen gibt es einen
gestalteten Foto-Slot, der ohne Foto als Grafik funktioniert und im Demo-Modus eine Foto-Notiz zeigt.

**Fotoliste für Swantje** (Handy reicht, wenn Licht gut ist; Tageslicht, kein Blitz):

| Wofür | Motiv | Format |
|---|---|---|
| Über mich | Porträt, freundlich, Blick in die Kamera, ruhiger Hintergrund | Hochformat 4:5 |
| Über mich (optional) | Swantje in einer einfachen Haltung, ganzer Körper | Hochformat |
| Angebot | Kursraum leer, aufgeräumt, Matten ausgelegt | Querformat 3:2 |
| Angebot (optional) | Hände/Details: Matte, Decke, Klangschale, Tee | Quer- oder Hochformat |
| Ort | Eingang/Hausfront, damit man den Ort wiedererkennt | Querformat |
| Kurs (nur mit Einverständnis!) | Gruppe von hinten oder seitlich, keine erkennbaren Gesichter ohne Zustimmung | Querformat |

Fotos einbauen: Datei nach `assets/img/fotos/` (max. ~1600 px Breite, JPG/WebP), dann im
entsprechenden `<figure class="slot">` die Zeile `<svg class="slot-art">…</svg>` durch
`<img src="assets/img/fotos/portraet.jpg" alt="Swantje im Kursraum" width="1200" height="1500" loading="lazy">` ersetzen
und `<figcaption class="slot-note">` löschen. Fotograf/in im Impressum unter „Bildnachweis“ nennen.

## Logo

Swantje hat noch kein Logo. In `entwuerfe/logo-entwuerfe.html` liegen drei Ideen
(A Atemkreis · B Krug · C Bogen & S). Die Demo nutzt **A**. Die Seite ist nicht verlinkt und `noindex`;
Link für Swantje nach dem Deployment: `https://<projekt>.pages.dev/entwuerfe/logo-entwuerfe.html`.

---

## ⚠️ Vor dem Livegang

Fehlende Angaben sind auf der Seite **gelb gestrichelt** markiert (`<span class="ph" title="…">`;
der `title` erklärt beim Darüberfahren, was fehlt). Wenn alles ergänzt ist:
in **allen** HTML-Dateien `<body class="demo">` → `<body>` ändern. Damit verschwinden auch Demo-Leiste,
Foto-Notizen und Hinweisboxen.

- [ ] Nachname, ladungsfähige Anschrift (Impressum, Datenschutz, Footer)
- [x] E-Mail-Adresse: `info@yomana.de` (`data-u="info"` + `data-d="yomana.de"`)
- [ ] du oder Sie? (aktuell durchgehend „du“)
- [ ] Texte „Über mich“, Ausbildung, Unterrichtserfahrung
- [ ] Angebot: welche der 5 Angebote bleiben? Welche Yogastile?
- [ ] Stundenplan: echte Tage, Zeiten, Kursnamen, Ort; Ferienregelung
- [ ] Preise, Gültigkeit Karten, Absageregel, Kleinunternehmerin (§ 19 UStG) oder USt-IdNr.
- [ ] Krankenkassen-Satz nur bei zertifiziertem Präventionskurs (§ 20 SGB V), sonst löschen
- [ ] Adresse Kursraum, Parken, ÖPNV, Leihmatten
- [x] Buchung: Gruppenkurse über Yogaresa (Link), Einzelstunden und Massagen persönlich per E-Mail
- [ ] Instagram o. Ä. (nur als einfacher Link, kein eingebetteter Feed)
- [x] Fotos, Farbwelt (Pflaume & Abendlicht)
- [ ] Logo-Entscheidung
- [ ] Echte Stimmen mit Einverständnis, sonst Sektion „Stimmen“ löschen
- [ ] Impressum & Datenschutz final prüfen lassen, E-Mail-Anbieter in Datenschutz eintragen
- [ ] Domain registrieren, Platzhalter-Domain prüfen (`grep -r "yomana.de" .`)
- [ ] OG-Bild ggf. mit Foto/finalem Logo neu erstellen

## E-Mail-Schutz

Die E-Mail-Adresse steht nirgends im HTML-Quelltext. Links haben die Klasse `js-mail` mit
`data-u="info"` und `data-d="yomana.de"`, optional `data-subject="Anfrage Probestunde"`.
`assets/js/main.js` setzt daraus den `mailto:`-Link zusammen. Ohne JavaScript steht dort „info [at] yomana.de“.

## Lokal ansehen

```bash
python3 -m http.server 8000   # → http://localhost:8000
```
(Die 404-Seite nutzt absolute Pfade und sieht nur über einen Server richtig aus.)

---

## Veröffentlichen bei manitu

1. Einmalig: `cp ftp.example.yml ftp.yml` und in `ftp.yml` Server, Benutzer (und optional Passwort) aus dem
   manitu-Kundenmenü eintragen. `ftp.yml` steht in `.gitignore` und wird nie hochgeladen.
2. `python3 scripts/deploy_ftp.py --dry-run` zeigt die Dateiliste, `python3 scripts/deploy_ftp.py` lädt hoch.
3. Vorher bei manitu: SSL-Zertifikat für `yomana.de` und `www.yomana.de` aktivieren
   (die `.htaccess` leitet alles auf `https://www.yomana.de` um) und den Auftragsverarbeitungsvertrag (AVV) abschließen.

### Alte Variante: GitHub + Cloudflare (nicht mehr genutzt)


Git im Terminal ist Version 2.23 (conda): `git init -b main` funktioniert **nicht**. Das Repo ist bereits
vorbereitet mit `git init && git symbolic-ref HEAD refs/heads/main`.

### 1. GitHub-Repository
1. Auf github.com → **New repository** → Name `yoga-mit-swantje`, *Private* oder *Public*,
   **leer anlegen** (kein README, keine .gitignore, keine Lizenz).
2. Im Projektordner:
   ```bash
   git add .
   git commit -m "Erster Demo-Entwurf"
   git remote add origin https://github.com/<BENUTZERNAME>/yoga-mit-swantje.git
   git push -u origin main
   ```

### 2. Cloudflare (Demo-Link)
1. dash.cloudflare.com → **Workers & Pages** → **Create** → **Import a repository** → GitHub verbinden → `yoga-mit-swantje` wählen.
2. Build-Einstellungen: **kein Build-Befehl**, Ausgabeverzeichnis **`/`**.
3. **Deploy** → nach ca. 1 Minute gibt es einen Link `https://yoga-mit-swantje.<…>.pages.dev` (bzw. `*.workers.dev`).
   Diesen Link an Swantje schicken, dazu `…/entwuerfe/logo-entwuerfe.html`.
   `.assetsignore` sorgt dafür, dass `kunde/`, `scripts/`, README usw. nicht veröffentlicht werden.

### 3. Später: eigene Domain
1. Domain `yoga-mit-swantje.de` registrieren (oder vorhandene Domain nutzen).
2. Cloudflare → **Add a domain** → Cloudflare liest die bestehenden DNS-Einträge ein.
3. ⚠️ **Wenn Swantje E-Mail über ihren Domain-Anbieter nutzt** (z. B. IONOS, Strato): **vor** dem Umstellen
   der Nameserver prüfen, dass alle **MX**- und **TXT**-Einträge (SPF, DKIM, DMARC) korrekt übernommen wurden.
   Sonst kommen keine E-Mails mehr an.
4. Nameserver beim Domain-Anbieter auf die beiden Cloudflare-Nameserver ändern.
5. Im Projekt → **Custom domains** → `www.yoga-mit-swantje.de` (und `yoga-mit-swantje.de`) hinzufügen.
   *Alternative ohne Nameserver-Umzug:* beim bisherigen Anbieter nur einen **CNAME** für `www` auf die
   `pages.dev`-Adresse setzen; E-Mail bleibt unberührt.

### 4. Änderungen veröffentlichen
```bash
./scripts/push_changes.sh                      # Standard-Nachricht „Website aktualisiert“
./scripts/push_changes.sh "Stundenplan Winter" # eigene Nachricht
```
Nach ca. 1 Minute ist die Änderung online.
