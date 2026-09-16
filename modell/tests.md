---
description: Unit-, Integrations- und Screen-Tests. Laden bei Testfragen, bei
  Isolierung, bei der Frage "wie prüfen wir das".
---

# Tests

**Wie wird geprüft, dass die Komponenten tun, was sie sollen?**

Zwei Ebenen:

- **Unit** — eine Komponente allein.
- **Integration** — ein explizit gewähltes Subset von Komponenten.

Dazu die **Defaults** — Happy Case und triviale Fehlerfälle. Keine eigene
Ebene, sondern was zu jedem `T-` dazukommt (Frage 3).

Alle Komponenten werden unit-getestet. Nicht nur die zentralen.

Ein `T-` ist kein einzelner Fall, sondern die **Prüfungen zu einem
Prüfling**: was an dieser Komponente, dieser Schnittstelle, diesem Screen
oder diesem Zusammenspiel geprüft wird. Die einzelnen Szenarien stehen in
seinem Text und tragen keine Nummer — das Modell sagt, was geprüft werden
muss, nicht was gerade durchfällt. Wer einen einzelnen Fall benennen will,
benennt ihn im Testlauf, nicht hier.

Welche Ebene ein `T-` hat, trägt man nirgends ein. Es steht im Verweis:

    prueft: C-003                        → Unit
    prueft: C-003  mockt: X-002          → Unit, die externe ist ersetzt
    prueft: C-003  laeuft-gegen: X-002   → Integration, sie ist beteiligt
    prueft: C-003, C-007, I-002          → Integration, ein Subset

**Unit heißt: genau ein `prueft`-Ziel und kein `laeuft-gegen`.** Der Mock
ist dabei kein Behelf, sondern gerade das, was den Test zum Unit-Test macht —
er hält den Prüfling allein.

Deshalb gibt es auch keine Nummernkreise. Die Ebene wird abgefragt, nicht
gepflegt.

Eine Unschärfe, bewusst in Kauf genommen: Danach ist „unsere Komponente mit
der echten Lib" ein Integrationstest, obwohl das jeder einen Unit-Test
nennen würde. Die Ebene ist rein beschreibend — nichts im Modell hängt an
ihr, sie ordnet nur die Fragen. Sauber unterscheiden ließe sie sich erst,
wenn die **Art** aus `extern.md` im Frontmatter der `X-` stünde, und dafür
ist ein Etikett zu wenig.

## Fragen

### 1. Unit-Tests

Für jeden Prüfling — jede Komponente, dazu jede Schnittstelle und jeden
Screen, an dem etwas zu prüfen ist:

- **ID**
- **Prüft** — Komponente, Schnittstelle oder Screen (`C-`, `I-`, `S-`)
- **Was wird geprüft?**
- **Womit?** — Eingabe (externe Komponenten werden gemockt, sonst ist es
  kein Unit-Test)
- **Was wird erwartet?**
- **Fehlerfall**

Ein Screen-Test prüft das **Ergebnis** aus `ui.md` Frage 1 — was ist danach
anders? — nicht das Aussehen. Das Aussehen prüft der Mockup-Kreislauf. Die
beiden prüfen Verschiedenes, das eine ersetzt das andere nicht.

### 2. Integrationstests

**Explizit gewählte Subsets.** Nicht alle Kombinationen — nur die, die
für das System entscheidend sind.

Für jeden Test:
- **ID**
- **Prüft** — das Subset (`C-`, `I-`, `S-`)
- **Warum dieses Subset?** — die Begründung.
- **Was wird geprüft?**
- **Nicht-trivialer Fehlerfall**

### 3. Defaults

Diese gehören zu **jedem** `T-`, nicht nur zu den Integrationstests. Jeder
Punkt wird beantwortet — oder mit Begründung ausgelassen:

- **Happy Case** — alles erfolgreich.
- **Leere Eingabe** — was passiert, wenn nichts kommt?
- **Ungültiger Wert** — was passiert bei einem Wert außerhalb der Liste?
- **Fehlende Verbindung** — was passiert, wenn das nächste Glied nicht
  erreichbar ist?

„Passt hier nicht" ist eine gültige Antwort, nichts hinzuschreiben nicht.
Am Ende einer Kette gibt es keine nächste Komponente, bei freiem Text keinen
Wert außerhalb der Liste — ohne den hingeschriebenen Grund sieht später
niemand den Unterschied zwischen *nicht anwendbar* und *vergessen*.

Die Defaults sind **generisch** und bekommen keine eigenen IDs: Sie sind
Szenarien innerhalb des `T-`, das sie mitbringt, keine eigenen Artefakte.

### 4. Was wird nicht getestet?

Was bleibt bewusst ungeprüft? (z. B. externe Komponenten selbst, die Akteure.)

Ein Akteur wird nie getestet — er ist kein Code. Geprüft wird, was er
bedient: die Schnittstelle, die seine Entscheidung aufnimmt, und der
Screen, der sie ihm abverlangt.

Die externe Komponente selbst wird nie geprüft. Geprüft wird, wie unsere
Komponente mit ihr umgeht — und dafür gibt es zwei Wege, die Verschiedenes
prüfen:

- **Ersetzt** (`mockt:`) — die **Nutzung** gegen unsere Annahme über die
  externe: die Aufrufe, die Behandlung der Antworten, isoliert. Unit.
- **Beteiligt** (`laeuft-gegen:`) — das **Zusammenspiel** selbst, samt der
  Frage, ob die Annahme noch stimmt. Integration.

Welcher Weg passt, hängt an der Art der externen Komponente und steht in
`extern.md` Frage 3. Beides trägt der Test selbst, nicht die externe
Komponente — und **innerhalb eines `T-`** nie beides zur selben externen.
Über mehrere `T-` hinweg ist beides normal: Der eine mockt sie, um den
Prüfling allein zu halten, der andere lässt sie mitlaufen, um die Annahme
zu prüfen.

## Was hier entsteht

- `T-` Testfälle

Ordner: `projekt/tests/`

Ein abgestimmter Eintrag trägt darunter die Zeile
`Abgestimmt: <wer>, <wann>` — ab dann ist seine ID verbraucht und wird bei
Aufgabe ausgemustert statt umnummeriert (`metamodell.md`).

Ausgemustert: —

## Querverweise

- **Geht aus:** `prueft` → C-, I-, S-; `mockt` → X-; `laeuft-gegen` → X-
- **Kommt an:** keine

## Was hier nicht entsteht

- Testcode (der kommt später)
- Testdaten (die kommen später)

## Zustand

- [ ] Unit-Tests pro Prüfling
- [ ] Integrationstests (explizit gewählt)
- [ ] Defaults (Happy Case, triviale Fehlerfälle)
- [ ] Was wird nicht getestet?

## Notizen
