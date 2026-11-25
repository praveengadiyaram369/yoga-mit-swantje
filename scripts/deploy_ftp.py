#!/usr/bin/env python3
"""YoMaNa – Website per FTP (verschlüsselt, FTPS) zu manitu hochladen.

Zugangsdaten: in der Datei ftp.yml im Projektordner (Vorlage: ftp.example.yml).
ftp.yml steht in .gitignore und wird NIE hochgeladen.

Aufruf (im Projektordner, im eigenen Terminal):
    python3 scripts/deploy_ftp.py              # Daten aus ftp.yml
    python3 scripts/deploy_ftp.py --dry-run    # nur Dateiliste anzeigen
Einzelne Werte lassen sich mit --host / --user / --dir überschreiben.
Steht kein Passwort in ftp.yml, wird es beim Start abgefragt.
Hochgeladen werden NUR die Dateien der Website (siehe INCLUDE). Nie: kunde/, images/, scripts/,
entwuerfe/, .git, README.md, AGENTS.md.
"""
import argparse
import getpass
import os
import sys
from ftplib import FTP_TLS, error_perm

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Einzelne Dateien im Hauptordner + ganze Ordner
INCLUDE_FILES = [
    "index.html", "ueber-mich.html", "angebot.html", "erste-stunde.html", "kontakt.html",
    "impressum.html", "datenschutz.html", "404.html",
    "favicon.ico", "robots.txt", "sitemap.xml", ".htaccess",
]
INCLUDE_DIRS = ["assets"]
SKIP_NAMES = {".DS_Store", ".gitkeep"}


def collect():
    files = []
    for f in INCLUDE_FILES:
        p = os.path.join(ROOT, f)
        if not os.path.isfile(p):
            sys.exit(f"Fehlt: {f}")
        files.append(f)
    for d in INCLUDE_DIRS:
        for base, dirs, names in os.walk(os.path.join(ROOT, d)):
            dirs[:] = [x for x in dirs if not x.startswith(".")]
            for n in names:
                if n in SKIP_NAMES or n.startswith("."):
                    continue
                files.append(os.path.relpath(os.path.join(base, n), ROOT))
    return sorted(files)


def read_config(path):
    """Liest einfache „schlüssel: wert“-Zeilen (YAML-Teilmenge, ohne Zusatzpaket)."""
    cfg = {}
    if not os.path.isfile(path):
        return cfg
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#") or ":" not in line:
                continue
            key, val = line.split(":", 1)
            val = val.strip()
            if val[:1] in ("\"", "'"):
                # Wert in Anführungszeichen: alles bis zum schließenden Zeichen (darf # enthalten)
                end = val.find(val[0], 1)
                val = val[1:end] if end != -1 else val[1:]
            else:
                # Kommentar am Zeilenende entfernen: „wert   # kommentar“
                val = val.split(" #", 1)[0].strip()
            cfg[key.strip()] = val
    return cfg


def ensure_dir(ftp, path, made):
    parts = [p for p in path.split("/") if p]
    cur = ""
    for p in parts:
        cur += "/" + p
        if cur in made:
            continue
        try:
            ftp.mkd(cur.lstrip("/"))
        except error_perm:
            pass  # existiert schon
        made.add(cur)


def main():
    ap = argparse.ArgumentParser(description="YoMaNa per FTPS hochladen")
    ap.add_argument("--config", default=os.path.join(ROOT, "ftp.yml"), help="Datei mit Zugangsdaten (Standard: ftp.yml)")
    ap.add_argument("--host", help="FTP-Server (überschreibt ftp.yml)")
    ap.add_argument("--user", help="FTP-Benutzername (überschreibt ftp.yml)")
    ap.add_argument("--dir", help="Zielordner auf dem Server (überschreibt ftp.yml)")
    ap.add_argument("--dry-run", action="store_true", help="Nur anzeigen, was hochgeladen würde")
    args = ap.parse_args()

    cfg = read_config(args.config)
    host = args.host or cfg.get("host", "")
    user = args.user or cfg.get("user", "")
    remote_dir = args.dir if args.dir is not None else cfg.get("dir", "")
    password = cfg.get("password", "")
    if not args.dry_run and (not host or not user):
        sys.exit("Bitte host und user in ftp.yml eintragen (Vorlage: ftp.example.yml) oder --host/--user angeben.")
    if host in ("FTP-SERVER", "ftp.example.de"):
        sys.exit("In ftp.yml steht noch der Beispiel-Server. Bitte den echten FTP-Server von manitu eintragen.")

    files = collect()
    print(f"{len(files)} Dateien werden hochgeladen:")
    for f in files:
        print("  ", f)
    if args.dry_run:
        return

    pw = password or getpass.getpass(f"FTP-Passwort für {user}@{host}: ")
    print(f"Verbinde mit {host} …")
    ftp = FTP_TLS(host, timeout=60)
    ftp.login(user, pw)
    ftp.prot_p()  # Datenverbindung verschlüsseln
    if remote_dir:
        ftp.cwd(remote_dir)
    made = set()
    for i, f in enumerate(files, 1):
        remote = f.replace(os.sep, "/")
        if "/" in remote:
            ensure_dir(ftp, remote.rsplit("/", 1)[0], made)
        with open(os.path.join(ROOT, f), "rb") as fh:
            ftp.storbinary(f"STOR {remote}", fh)
        print(f"[{i}/{len(files)}] {remote}")
    ftp.quit()
    print("Fertig. Bitte https://www.yomana.de im Browser prüfen.")


if __name__ == "__main__":
    main()
