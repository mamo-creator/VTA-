#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generiert die statischen HTML-Seiten für die Website von
VTA Garmisch-Patenkirchen. Einfach anpassen und erneut ausführen,
um alle Seiten konsistent zu aktualisieren (Nav/Footer an einer Stelle).
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

NAV = [
    ("index.html", "Start"),
    ("verein.html", "Verein"),
    ("mannschaft-1.html", "1. Mannschaft"),
    ("mannschaft-2.html", "2. Mannschaft"),
    ("stadion.html", "Stadion"),
    ("vorstand.html", "Vorstand"),
    ("trainer.html", "Trainer"),
    ("mitglieder.html", "Mitglieder & Fans"),
    ("admin.html", "Admin"),
    ("kontakt.html", "Kontakt"),
]

BASE = """<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} · VTA Garmisch-Patenkirchen</title>
<meta name="description" content="{description}">
<link rel="icon" type="image/png" sizes="32x32" href="assets/favicon-32.png">
<link rel="icon" type="image/png" sizes="16x16" href="assets/favicon-16.png">
<link rel="apple-touch-icon" sizes="180x180" href="assets/favicon-180.png">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<header class="site-header">
  <div class="nav-wrap">
    <a class="brand" href="index.html">
      <img class="crest" src="assets/logo.png" alt="Wappen VTA Garmisch-Patenkirchen">
      VTA Garmisch-Patenkirchen
    </a>
    <nav class="main-nav" aria-label="Hauptnavigation">
      <ul>
{nav_items}
      </ul>
    </nav>
  </div>
</header>

{content}

<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <h4>VTA Garmisch-Patenkirchen</h4>
        <ul>
          <li>Gegründet 1978</li>
          <li>Vereinsfarben: Rot-Weiß</li>
          <li>Bezirk Oberbayern, Kreis Zugspitze</li>
        </ul>
      </div>
      <div>
        <h4>Bereiche</h4>
        <ul>
          <li><a href="vorstand.html">Vorstand</a></li>
          <li><a href="trainer.html">Trainer</a></li>
          <li><a href="mitglieder.html">Mitglieder &amp; Fans</a></li>
          <li><a href="admin.html">Admin</a></li>
        </ul>
      </div>
      <div>
        <h4>Extern</h4>
        <ul>
          <li><a href="https://www.bfv.de/vereine/vta-garmisch-patenkirchen/00ES8GNHI400000HVV0AG08LVUPGND5I" target="_blank" rel="noopener">Vereinsprofil beim BFV</a></li>
          <li><a href="https://www.fussball.de/verein/vta-garmisch-patenkirchen-bayern/-/id/00ES8GNHI400000HVV0AG08LVUPGND5I" target="_blank" rel="noopener">Vereinsprofil auf fussball.de</a></li>
        </ul>
      </div>
      <div>
        <h4>Kontakt</h4>
        <ul>
          <li>zeki28@gmx.de</li>
          <li><a href="kontakt.html">Kontaktseite</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      &copy; <span id="year"></span> VTA Garmisch-Patenkirchen · Diese Seite wird ehrenamtlich gepflegt.
      <a href="admin.html">Hinweise zur Pflege der Website</a>
    </div>
  </div>
</footer>
<script>document.getElementById('year').textContent = new Date().getFullYear();</script>
</body>
</html>
"""

def nav_html(active):
    lines = []
    for href, label in NAV:
        current = ' aria-current="page"' if href == active else ""
        lines.append(f'        <li><a href="{href}"{current}>{label}</a></li>')
    return "\n".join(lines)

def page(filename, title, description, content):
    html = BASE.format(
        title=title,
        description=description,
        nav_items=nav_html(filename),
        content=content,
    )
    with open(os.path.join(ROOT, filename), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"geschrieben: {filename}")


# ---------------------------------------------------------------
# INDEX
# ---------------------------------------------------------------
page(
    "index.html",
    "Start",
    "Offizielle Website des VTA Garmisch-Patenkirchen – Fußballverein aus Garmisch-Partenkirchen, gegründet 1978.",
    """
<section class="hero">
  <div class="container hero-flex">
    <img class="hero-logo" src="assets/logo.png" alt="Wappen VTA Garmisch-Patenkirchen">
    <div>
      <span class="badge">Fußball seit 1978</span>
      <h1>VTA Garmisch-Patenkirchen</h1>
      <p class="lead">Willkommen auf der offiziellen Website unseres Vereins – Heimat für Spieler, Mitglieder,
      Trainer, Vorstand und alle Fans des VTA Garmisch-Patenkirchen.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="mannschaft-1.html">Zur 1. Mannschaft</a>
        <a class="btn btn-outline" href="mitglieder.html">Mitglied werden</a>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <h2>Unsere Bereiche</h2>
    <div class="grid grid-4">
      <a class="area-card card" href="vorstand.html">
        <span class="badge">Vorstand</span>
        <h3>Vorstandsbereich</h3>
        <p>Vereinsführung, Satzung, Protokolle und Ansprechpartner.</p>
      </a>
      <a class="area-card card" href="trainer.html">
        <span class="badge">Trainer</span>
        <h3>Trainerbereich</h3>
        <p>Trainingszeiten, Trainingspläne und Kontakte der Trainerteams.</p>
      </a>
      <a class="area-card card" href="mitglieder.html">
        <span class="badge">Mitglieder</span>
        <h3>Spieler, Mitglieder &amp; Fans</h3>
        <p>Alles rund um Mannschaften, Mitgliedschaft und Fanleben.</p>
      </a>
      <a class="area-card card" href="admin.html">
        <span class="badge">Admin</span>
        <h3>Admin-Bereich</h3>
        <p>Wie diese Website gepflegt und aktualisiert wird.</p>
      </a>
    </div>
  </div>
</section>

<section class="alt">
  <div class="container">
    <h2>Unsere Mannschaften</h2>
    <div class="grid grid-2">
      <div class="card">
        <h3>1. Mannschaft</h3>
        <p>Spielt in der <strong>B-Klasse, Gruppe 6</strong> (Kreis Zugspitze).</p>
        <p><a href="mannschaft-1.html">Zur Mannschaftsseite &rarr;</a></p>
      </div>
      <div class="card">
        <h3>2. Mannschaft</h3>
        <p>Spielt in der <strong>C-Klasse, Gruppe 4</strong> (Kreis Zugspitze).</p>
        <p><a href="mannschaft-2.html">Zur Mannschaftsseite &rarr;</a></p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <h2>Aktuelles</h2>
    <div class="widget-slot">
      <strong>Platzhalter: Spielplan / Live-Ticker</strong><br>
      Hier kann das kostenlose BFV-Widget für Spieltage und Ergebnisse eingebunden werden.
      Details siehe <a href="admin.html#bfv-widgets">Admin-Bereich</a>.
    </div>
  </div>
</section>
""",
)

# ---------------------------------------------------------------
# VEREIN
# ---------------------------------------------------------------
page(
    "verein.html",
    "Verein",
    "Geschichte und Daten des VTA Garmisch-Patenkirchen.",
    """
<section class="hero">
  <div class="container">
    <h1>Unser Verein</h1>
    <p class="lead">Der VTA Garmisch-Patenkirchen wurde 1978 gegründet und ist im Bezirk Oberbayern,
    Kreis Zugspitze des Bayerischen Fußball-Verbands (BFV) beheimatet.</p>
  </div>
</section>

<section>
  <div class="container">
    <h2>Vereinsdaten</h2>
    <div class="grid grid-2">
      <table>
        <tr><th>Vereinsname</th><td>VTA Garmisch-Patenkirchen</td></tr>
        <tr><th>Gegründet</th><td>1978</td></tr>
        <tr><th>Vereinsfarben</th><td>Rot-Weiß</td></tr>
        <tr><th>Bezirk / Kreis</th><td>Oberbayern / Zugspitze</td></tr>
        <tr><th>Verband</th><td>Bayerischer Fußball-Verband (BFV)</td></tr>
        <tr><th>Vereinsadresse</th><td>Marienplatz 11, 82467 Garmisch-Partenkirchen</td></tr>
      </table>
      <div class="note">
        <strong>Hinweis zum Anpassen:</strong> Die obigen Daten stammen aus dem öffentlichen
        BFV-Vereinsprofil. Vereinsgeschichte, Wappen-Bedeutung, Ehrenmitglieder und weitere
        Details bitte hier ergänzen – am besten direkt in dieser Datei (<code>verein.html</code>)
        oder über den <a href="admin.html">Admin-Bereich</a>.
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="container">
    <h2>Weiterführende Links</h2>
    <ul>
      <li><a href="https://www.bfv.de/vereine/vta-garmisch-patenkirchen/00ES8GNHI400000HVV0AG08LVUPGND5I" target="_blank" rel="noopener">Offizielles Vereinsprofil beim BFV</a></li>
      <li><a href="https://www.fussball.de/verein/vta-garmisch-patenkirchen-bayern/-/id/00ES8GNHI400000HVV0AG08LVUPGND5I" target="_blank" rel="noopener">Vereinsprofil auf fussball.de</a></li>
    </ul>
  </div>
</section>
""",
)

# ---------------------------------------------------------------
# MANNSCHAFT TEMPLATE
# ---------------------------------------------------------------
def mannschaft_page(filename, title, liga, description):
    content = f"""
<section class="hero">
  <div class="container">
    <span class="badge">{liga}</span>
    <h1>{title}</h1>
    <p class="lead">Alle Infos, Ergebnisse und Tabellenstände zur {title} des VTA Garmisch-Patenkirchen.</p>
  </div>
</section>

<section>
  <div class="container">
    <h2>Tabelle &amp; Ergebnisse (BFV-Live-Daten)</h2>
    <div class="widget-slot" id="bfv-tabelle">
      <strong>Platzhalter für BFV-Widget: Live-Tabelle &amp; Ergebnisse</strong><br>
      Hier den Einbettungscode (iframe) aus dem
      <a href="https://www.bfv.de/bfv-widgets" target="_blank" rel="noopener">BFV-Widget-Generator</a>
      für „{title}“ einfügen. Anleitung dazu im <a href="admin.html#bfv-widgets">Admin-Bereich</a>.
    </div>
  </div>
</section>

<section class="alt">
  <div class="container">
    <h2>Spielplan</h2>
    <div class="widget-slot">
      <strong>Platzhalter für BFV-Widget: Spielplan</strong><br>
      Zeigt automatisch alle kommenden und vergangenen Spiele, sobald das Widget eingebunden ist.
    </div>
  </div>
</section>

<section>
  <div class="container">
    <h2>Kader &amp; Trainerteam</h2>
    <div class="note">
      <strong>Platzhalter:</strong> Kaderliste und Trainerteam der {title} hier ergänzen
      (Name, Position, Trikotnummer). Trainingszeiten stehen im <a href="trainer.html">Trainerbereich</a>.
    </div>
  </div>
</section>
"""
    page(filename, title, description, content)


mannschaft_page(
    "mannschaft-1.html",
    "1. Mannschaft",
    "B-Klasse Gruppe 6",
    "1. Mannschaft des VTA Garmisch-Patenkirchen – B-Klasse Gruppe 6.",
)
mannschaft_page(
    "mannschaft-2.html",
    "2. Mannschaft",
    "C-Klasse Gruppe 4",
    "2. Mannschaft des VTA Garmisch-Patenkirchen – C-Klasse Gruppe 4.",
)

# ---------------------------------------------------------------
# STADION
# ---------------------------------------------------------------
page(
    "stadion.html",
    "Stadion",
    "Sportplatz und Anfahrt des VTA Garmisch-Patenkirchen.",
    """
<section class="hero">
  <div class="container">
    <h1>Unser Sportplatz</h1>
    <p class="lead">Hier trainieren und spielen unsere Mannschaften.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="note">
      <strong>Bitte prüfen &amp; ergänzen:</strong> Als Vereinsanschrift ist beim BFV
      „Marienplatz 11, 82467 Garmisch-Partenkirchen“ hinterlegt – das ist vermutlich die
      Postanschrift des Vereins/Vorstands, nicht zwingend die Adresse des Sportplatzes.
      Bitte den tatsächlichen Namen und die Adresse des Sportplatzes (z.&nbsp;B. „Sportgelände …straße“)
      hier eintragen.
    </div>

    <div class="grid grid-2" style="margin-top:24px;">
      <div class="card">
        <h3>Adresse</h3>
        <p>[Name des Sportplatzes]<br>[Straße Hausnummer]<br>82467 Garmisch-Partenkirchen</p>
      </div>
      <div class="card">
        <h3>Anfahrt</h3>
        <p>Hier können Hinweise zu Parkplätzen, ÖPNV-Anbindung (Bahnhof Garmisch-Partenkirchen)
        und Anfahrt mit dem Auto ergänzt werden.</p>
      </div>
    </div>

    <div class="widget-slot" style="margin-top:24px;">
      <strong>Platzhalter: Karte</strong><br>
      Hier kann eine Google-Maps- oder OpenStreetMap-Einbettung mit der echten Adresse
      des Sportplatzes eingefügt werden.
    </div>
  </div>
</section>
""",
)

# ---------------------------------------------------------------
# VORSTAND
# ---------------------------------------------------------------
page(
    "vorstand.html",
    "Vorstand",
    "Vorstandsbereich des VTA Garmisch-Patenkirchen.",
    """
<section class="hero">
  <div class="container">
    <span class="badge">Vorstandsbereich</span>
    <h1>Vorstand</h1>
    <p class="lead">Informationen für und über die Vereinsführung des VTA Garmisch-Patenkirchen.</p>
  </div>
</section>

<section>
  <div class="container">
    <h2>Vorstandsmitglieder</h2>
    <div class="grid grid-3">
      <div class="card"><h3>[1. Vorsitzende/r]</h3><p>Name ergänzen</p></div>
      <div class="card"><h3>[2. Vorsitzende/r]</h3><p>Name ergänzen</p></div>
      <div class="card"><h3>[Kassier/in]</h3><p>Name ergänzen</p></div>
      <div class="card"><h3>[Schriftführer/in]</h3><p>Name ergänzen</p></div>
      <div class="card"><h3>[Jugendleiter/in]</h3><p>Name ergänzen</p></div>
      <div class="card"><h3>[Sportlicher Leiter/in]</h3><p>Name ergänzen</p></div>
    </div>
    <p style="margin-top:16px;">Bekannter Ansprechpartner laut Vereinsregister: <strong>Zeki Serdaroglu</strong>
    (<a href="mailto:zeki28@gmx.de">zeki28@gmx.de</a>).</p>
  </div>
</section>

<section class="alt">
  <div class="container">
    <h2>Satzung &amp; Protokolle</h2>
    <div class="note">
      <strong>Platzhalter:</strong> Hier können die Vereinssatzung, Protokolle von
      Mitgliederversammlungen und Beschlüsse als PDF-Downloads verlinkt werden, z.&nbsp;B.:
    </div>
    <ul style="margin-top:16px;">
      <li><a href="#">Vereinssatzung (PDF) – noch einzufügen</a></li>
      <li><a href="#">Protokoll Mitgliederversammlung 2026 (PDF) – noch einzufügen</a></li>
    </ul>
    <p><em>Hinweis: Sensible/interne Dokumente sollten nicht öffentlich verlinkt werden,
    solange die Seite kein echtes Login besitzt – siehe <a href="admin.html">Admin-Bereich</a>.</em></p>
  </div>
</section>
""",
)

# ---------------------------------------------------------------
# TRAINER
# ---------------------------------------------------------------
page(
    "trainer.html",
    "Trainer",
    "Trainerbereich des VTA Garmisch-Patenkirchen.",
    """
<section class="hero">
  <div class="container">
    <span class="badge">Trainerbereich</span>
    <h1>Trainer</h1>
    <p class="lead">Trainingszeiten, Trainerteams und Materialien für alle Mannschaften.</p>
  </div>
</section>

<section>
  <div class="container">
    <h2>Trainingszeiten</h2>
    <table>
      <tr><th>Mannschaft</th><th>Tag</th><th>Uhrzeit</th><th>Ort</th></tr>
      <tr><td>1. Mannschaft</td><td>[Wochentag]</td><td>[Uhrzeit]</td><td>[Sportplatz]</td></tr>
      <tr><td>2. Mannschaft</td><td>[Wochentag]</td><td>[Uhrzeit]</td><td>[Sportplatz]</td></tr>
    </table>
    <div class="note" style="margin-top:16px;">
      <strong>Platzhalter:</strong> Bitte die echten Trainingstage/-zeiten eintragen.
    </div>
  </div>
</section>

<section class="alt">
  <div class="container">
    <h2>Trainerteam</h2>
    <div class="grid grid-2">
      <div class="card"><h3>1. Mannschaft</h3><p>Trainer: [Name]<br>Co-Trainer: [Name]</p></div>
      <div class="card"><h3>2. Mannschaft</h3><p>Trainer: [Name]<br>Co-Trainer: [Name]</p></div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <h2>Materialien</h2>
    <div class="note">
      <strong>Platzhalter:</strong> Hier können Trainingspläne, Übungssammlungen oder
      Formulare (z.&nbsp;B. Spielberichte) als Download verlinkt werden.
    </div>
  </div>
</section>
""",
)

# ---------------------------------------------------------------
# MITGLIEDER / SPIELER / FANS
# ---------------------------------------------------------------
page(
    "mitglieder.html",
    "Mitglieder & Fans",
    "Für Spieler, Mitglieder und Fans des VTA Garmisch-Patenkirchen.",
    """
<section class="hero">
  <div class="container">
    <span class="badge">Für alle</span>
    <h1>Spieler, Mitglieder &amp; Fans</h1>
    <p class="lead">Dieser Bereich ist für alle da, die den VTA Garmisch-Patenkirchen lieben –
    ob aktiver Spieler, Vereinsmitglied oder treuer Fan.</p>
  </div>
</section>

<section>
  <div class="container">
    <h2>Mitglied werden</h2>
    <div class="grid grid-2">
      <div class="card">
        <h3>Aufnahmeantrag</h3>
        <p>Interesse an einer Mitgliedschaft? Meldet euch gerne bei uns.</p>
        <p><a class="btn btn-primary" href="kontakt.html">Kontakt aufnehmen</a></p>
      </div>
      <div class="card">
        <h3>Mitgliedsbeitrag</h3>
        <p class="note">Platzhalter: Höhe des Jahresbeitrags für Erwachsene/Jugendliche/Familien hier ergänzen.</p>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="container">
    <h2>Für unsere Fans</h2>
    <p>Kommt vorbei und unterstützt uns bei Heimspielen! Aktuelle Spieltermine findet ihr auf den
    Mannschaftsseiten (<a href="mannschaft-1.html">1. Mannschaft</a>,
    <a href="mannschaft-2.html">2. Mannschaft</a>) sowie über die BFV-Live-Daten.</p>
    <div class="note">
      <strong>Platzhalter:</strong> Hier können Fotos, Social-Media-Links oder ein
      Fan-Newsletter-Anmeldeformular ergänzt werden.
    </div>
  </div>
</section>

<section>
  <div class="container">
    <h2>Für unsere Spieler</h2>
    <p>Alle wichtigen Infos zu Training und Spielen findet ihr im
    <a href="trainer.html">Trainerbereich</a> sowie auf eurer jeweiligen Mannschaftsseite.</p>
  </div>
</section>
""",
)

# ---------------------------------------------------------------
# ADMIN
# ---------------------------------------------------------------
page(
    "admin.html",
    "Admin",
    "Admin-Bereich: Wie die Website des VTA Garmisch-Patenkirchen gepflegt wird.",
    """
<section class="hero">
  <div class="container">
    <span class="badge">Admin-Bereich</span>
    <h1>Website pflegen &amp; aktualisieren</h1>
    <p class="lead">Diese Seite ist eine reine HTML/CSS-Website ohne eigenen Server – daher gibt es
    kein klassisches Login-Adminpanel. Stattdessen wird die Seite direkt über GitHub gepflegt.
    Das ist kostenlos, sicher genug für öffentliche Vereinsinhalte und für jeden im
    Vorstandsteam erlernbar.</p>
  </div>
</section>

<section>
  <div class="container">
    <h2>Wer darf die Seite bearbeiten?</h2>
    <div class="note">
      <strong>Platzhalter:</strong> Hier eintragen, wer als Webmaster/in Zugriff auf das
      GitHub-Repository hat (z.&nbsp;B. Name, Kontakt). Aktuell bekannt: Ansprechpartner laut
      Vereinsregister ist <strong>Zeki Serdaroglu</strong> (<a href="mailto:zeki28@gmx.de">zeki28@gmx.de</a>).
    </div>
  </div>
</section>

<section class="alt" id="bfv-widgets">
  <div class="container">
    <h2>BFV-Widgets einbinden (Tabelle, Ergebnisse, Spielplan)</h2>
    <ol>
      <li>Auf <a href="https://www.bfv.de/bfv-widgets" target="_blank" rel="noopener">bfv.de/bfv-widgets</a>
      öffnen und „VTA Garmisch-Patenkirchen“ auswählen.</li>
      <li>Gewünschten Widget-Typ wählen (z.&nbsp;B. Tabelle, Ergebnisse, Spielplan, Liveticker) und
      Farben an die Vereinsfarben (Rot-Weiß) anpassen.</li>
      <li>Den generierten Einbettungscode (iframe) kopieren.</li>
      <li>In der jeweiligen HTML-Datei (z.&nbsp;B. <code>mannschaft-1.html</code>) den Platzhalter-Block
      mit der Überschrift „Platzhalter für BFV-Widget“ durch den kopierten Code ersetzen.</li>
      <li>Änderungen speichern und auf GitHub hochladen (siehe README.md) – fertig.</li>
    </ol>
    <p>Die Widgets aktualisieren sich danach automatisch mit den offiziellen BFV-Daten,
    ganz ohne weiteren Aufwand.</p>
  </div>
</section>

<section>
  <div class="container">
    <h2>Inhalte ändern</h2>
    <p>Alle Texte stehen direkt in den HTML-Dateien bzw. werden über <code>build.py</code>
    zentral verwaltet (Navigation und Footer). Wer sich das nicht zutraut, kann auch einfach
    jemanden bitten, kleinere Änderungen über GitHub vorzunehmen – eine ausführliche
    Schritt-für-Schritt-Anleitung steht in der Datei <code>README.md</code> im Projekt.</p>
  </div>
</section>

<section class="alt">
  <div class="container">
    <h2>Sicherheitshinweis</h2>
    <div class="note">
      <strong>Wichtig:</strong> Diese Website ist öffentlich einsehbar (auch der Quellcode auf
      GitHub). Bitte keine sensiblen personenbezogenen Daten (z.&nbsp;B. private Adressen,
      Geburtsdaten, Kontodaten von Mitgliedern) hier veröffentlichen. Für wirklich geschützte
      Bereiche mit echtem Login wäre eine technische Erweiterung nötig (siehe Gespräch mit
      der Vereins-IT/Website-Betreuung).
    </div>
  </div>
</section>
""",
)

# ---------------------------------------------------------------
# KONTAKT
# ---------------------------------------------------------------
page(
    "kontakt.html",
    "Kontakt",
    "Kontakt zum VTA Garmisch-Patenkirchen.",
    """
<section class="hero">
  <div class="container">
    <h1>Kontakt</h1>
    <p class="lead">Wir freuen uns über Nachrichten von Spielern, Eltern, Sponsoren und Fans.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="grid grid-2">
      <div class="card">
        <h3>Ansprechpartner</h3>
        <p><strong>Zeki Serdaroglu</strong><br>
        E-Mail: <a href="mailto:zeki28@gmx.de">zeki28@gmx.de</a></p>
        <p class="note">Platzhalter: Telefonnummer und weitere Ansprechpartner
        (z.&nbsp;B. Jugendabteilung, Pressewart) hier ergänzen.</p>
      </div>
      <div class="card">
        <h3>Vereinsanschrift</h3>
        <p>VTA Garmisch-Patenkirchen<br>
        Marienplatz 11<br>
        82467 Garmisch-Partenkirchen</p>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="container">
    <h2>Social Media</h2>
    <div class="note">
      <strong>Platzhalter:</strong> Links zu Instagram/Facebook/WhatsApp-Gruppe hier ergänzen,
      falls vorhanden.
    </div>
  </div>
</section>
""",
)

print("\nAlle Seiten wurden erstellt.")
