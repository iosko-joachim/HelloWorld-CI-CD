---
description: Die Landkarte über alle Dateien in `modell/`. Zuerst laden, wenn
  unklar ist, welche Datei zu der Frage passt, die gerade ansteht.
---

# Projektwissen — Index

Diese Datei ist die Landkarte. Sie sagt, welche Templates es gibt und wann man
sie lädt.

## Templates

| Datei | Wofür | Wann laden |
|---|---|---|
| `metamodell.md` | Gemeinsame Begriffe und Regeln | Wenn ein Begriff unklar ist |
| `ziel.md` | Was soll das Projekt machen | Am Anfang, bei unklarem Zweck |
| `ui.md` | Screens und ihre Reihenfolge | Bei UI-Fragen |
| `struktur.md` | Komponenten, Interfaces, Diagramme | Bei Zerlegung, bei Architektur |
| `daten.md` | Was das System festhält, und wie lange | Bei Datenmodell, bei Schlüsseln |
| `tests.md` | Unit-, Integrations- und Screen-Tests | Bei Testfragen |
| `extern.md` | Externe Komponenten | Bei Abhängigkeiten |
| `risiko.md` | Was schiefgehen kann | Bei Risiken, bei Abwägungen |
| `entscheidung.md` | Was gewählt wurde, und wogegen | Bei Weichenstellungen, bei „warum so" |

## Wie man ein Template benutzt

1. Zieh diese Datei in den Chat.
2. Sag, worüber du reden willst.
3. Das LLM sieht in der Tabelle, welches Template passt.
4. Zieh das Template nach — oder lass es danach fragen.

## Wie ein Projekt daraus entsteht

    mein-projekt/
    ├── modell/     diese Dateien — der Stand des Projekts
    └── projekt/    die Artefakte — daraus erzeugt

Die Templates in `modell/` werden **an Ort und Stelle** ausgefüllt, nicht
kopiert. Sie sind der Stand des Projekts: Geschrieben wird hier und nur
hier. Was daraus entsteht — Ziele, Komponenten, Screens, Prüfungen — wird
nach `projekt/` erzeugt, je Projektion ein Ordner.

`projekt/` ist Erzeugnis: Es darf jederzeit neu erzeugt werden, und eine
Änderung, die nur dort steht, gilt nicht — beim nächsten Erzeugen ist sie
weg. Im Repository steht es trotzdem, neben `modell/`: So ist der Stand
mitgeliefert, mit dem gearbeitet wurde, und prüfbar, ohne ihn erst
herzustellen. `modell/` bekommt dafür keine neuen Dateien und keine neuen
Ordner.

## Prüfen

    python3 modell/pruefe.py

Prüft den Artefakt-Graphen gegen `metamodell.md`, dazu den Fließtext auf
tote `[[Verweise]]` — in den Artefakten wie in den Templates — und je
Template die Fragen gegen die Zustandspunkte. Findet seine Pfade aus dem eigenen Ort, läuft also aus jedem
Verzeichnis. Rückgabewert 1 nur bei harten Fehlern — Platzhalter,
Verwaiste und Warnungen stehen im Bericht und blockieren nicht.

## Was der Index nicht ist

Kein Inhaltsverzeichnis, kein Projektwissen. Die Regeln des Modells stehen
in `metamodell.md`, der Inhalt in den Templates. Hier steht nur, wie man
anfängt und welches Template wofür da ist.
