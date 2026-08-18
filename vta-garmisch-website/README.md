# VTA Garmisch-Patenkirchen – Vereinswebsite

Statische Website für den VTA Garmisch-Patenkirchen (Fußballverein, gegründet 1978,
Vereinsfarben Rot-Weiß). Kein Server nötig, komplett kostenlos über **GitHub Pages** hostbar.

## Was ist enthalten?

| Seite | Inhalt |
|---|---|
| `index.html` | Startseite mit Überblick über alle Bereiche |
| `verein.html` | Vereinsgeschichte & -daten |
| `mannschaft-1.html` | 1. Mannschaft (B-Klasse Gruppe 6) inkl. Platz für BFV-Live-Daten |
| `mannschaft-2.html` | 2. Mannschaft (C-Klasse Gruppe 4) inkl. Platz für BFV-Live-Daten |
| `stadion.html` | Sportplatz & Anfahrt |
| `vorstand.html` | Vorstandsbereich (Vereinsführung, Satzung, Protokolle) |
| `trainer.html` | Trainerbereich (Trainingszeiten, Trainerteams, Materialien) |
| `mitglieder.html` | Für Spieler, Mitglieder & Fans (Mitgliedschaft, Fanbereich) |
| `admin.html` | Admin-Bereich: wie die Seite gepflegt wird |
| `kontakt.html` | Kontaktdaten |

Alle Seiten teilen sich Navigation & Footer, die zentral in `build.py` gepflegt werden.

## Schritt für Schritt: Kostenlos auf GitHub veröffentlichen

**1. GitHub-Konto erstellen** (falls noch nicht vorhanden): auf [github.com](https://github.com)
kostenlos registrieren.

**2. Neues Repository anlegen**
- Auf GitHub oben rechts auf **„+“ → „New repository“** klicken
- Name z. B. `vta-garmisch-website`
- Sichtbarkeit: **Public** (öffentlich) lassen – das ist Voraussetzung für kostenloses
  GitHub Pages
- „Create repository“ klicken

**3. Dateien hochladen**
- Im neuen Repository auf **„Add file“ → „Upload files“** klicken
- Alle Dateien und Ordner aus diesem Projekt hineinziehen (`index.html`, alle anderen
  `.html`-Dateien, den Ordner `css/`, den Ordner `assets/`, `build.py`, `README.md`)
- Unten „Commit changes“ klicken

**4. GitHub Pages aktivieren**
- Im Repository auf **„Settings“ → „Pages“** (linkes Menü) gehen
- Unter „Build and deployment“ → „Source“ auf **„Deploy from a branch“** stellen
- Branch: `main`, Ordner: `/ (root)` auswählen, dann „Save“
- Nach 1–2 Minuten ist die Seite unter einer Adresse wie
  `https://<dein-github-name>.github.io/vta-garmisch-website/` erreichbar

**5. (Optional) Eigene Domain verbinden**
- Domain bei einem Anbieter kaufen (z. B. `vta-garmisch.de`, ca. 10–15 €/Jahr)
- In „Settings → Pages → Custom domain“ die Domain eintragen
- Beim Domain-Anbieter einen CNAME-Eintrag auf `<dein-github-name>.github.io` setzen
  (Details in der [GitHub-Doku](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site))

Damit ist die Seite live – **komplett kostenlos**, solange das Repository öffentlich bleibt.

## BFV-Live-Daten einbinden (Tabelle, Ergebnisse, Spielplan)

Der Bayerische Fußball-Verband (BFV) bietet kostenlose Widgets an, die automatisch aktuelle
Daten anzeigen:

1. [bfv.de/bfv-widgets](https://www.bfv.de/bfv-widgets) öffnen und „VTA Garmisch-Patenkirchen“
   suchen/auswählen
2. Gewünschtes Widget wählen (Tabelle, Ergebnisse, Spielplan, Liveticker) und Farben an
   Rot-Weiß anpassen
3. Generierten Einbettungscode kopieren
4. In der passenden HTML-Datei (z. B. `mannschaft-1.html`) den grau gestrichelten
   Platzhalter-Block „Platzhalter für BFV-Widget“ durch den Code ersetzen
5. Datei speichern, auf GitHub hochladen – fertig, die Daten aktualisieren sich künftig
   automatisch

Eine Kurzanleitung steht auch direkt auf der Seite unter `admin.html`.

## Inhalte anpassen

Alle Texte sind direkt in den `.html`-Dateien enthalten und mit `[Platzhalter]` bzw. gelben
Hinweiskästen markiert, wo noch echte Daten fehlen (z. B. Vorstandsnamen, Trainingszeiten,
genaue Sportplatzadresse, Mitgliedsbeiträge).

Wer die Navigation oder den Footer ändern möchte, sollte das zentral in `build.py` tun und das
Skript danach neu ausführen:

```bash
python3 build.py
```

Das schreibt alle HTML-Seiten neu und hält Navigation/Footer auf allen Seiten konsistent.
Wer sich mit Python nicht auskennt, kann Navigation/Footer aber auch einfach direkt in jeder
`.html`-Datei von Hand anpassen (Copy & Paste in alle Dateien).

## Wichtiger Sicherheitshinweis

Diese Website hat **kein echtes Login-System** – Vorstands-, Trainer- und Mitgliederbereiche
sind eigene Seiten, aber öffentlich einsehbar (auch der Code auf GitHub ist öffentlich, da
kostenloses GitHub Pages ein öffentliches Repository voraussetzt). Bitte deshalb **keine**
sensiblen personenbezogenen Daten veröffentlichen (private Adressen, Geburtsdaten,
Kontodaten, Fotos von Minderjährigen ohne Einverständnis usw.).

Falls später ein echter, passwortgeschützter Bereich gewünscht ist (z. B. für interne
Vorstandsprotokolle), ist das technisch mit einem zusätzlichen, meist ebenfalls kostenlosen
Baustein (z. B. Supabase oder Firebase) möglich – dafür einfach erneut melden.
