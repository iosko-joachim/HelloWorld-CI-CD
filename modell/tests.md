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

#### T-001

- **Prüft:** C-002.
- **Was wird geprüft?** Dass das gemeinsame Kotlin-Multiplatform-Modul
  den Begrüßungstext aus dem Source korrekt bereitstellt, unabhängig
  von Android- oder iOS-Rendering.
- **Womit?** Reiner Kotlin-Unit-Test auf den gemeinsamen Code, keine
  externe Komponente beteiligt.
- **Was wird erwartet?** Der bereitgestellte Text entspricht exakt dem
  Source-String (z. B. "Hello World" bzw. nach Änderung "Hallo Welt").
- **Fehlerfall:** Text weicht vom Source-String ab oder ist leer.
- **Defaults:** Happy Case = Text vorhanden und korrekt. Leere Eingabe =
  Source-String leer → Test schlägt fehl (kein `NG-001`-Verstoß, aber
  falsches Verhalten). Ungültiger Wert — passt nicht, der String ist
  frei, keine Liste. Fehlende Verbindung — passt nicht, keine externe
  Abhängigkeit.

#### T-002

- **Prüft:** I-004.
- **Was wird geprüft?** Dass der Screen beim Start den Text aus C-002
  tatsächlich rendert — auf Android und auf iOS über Compose
  Multiplatform.
- **Womit?** Compose-Multiplatform-UI-Test, keine externe Komponente.
- **Was wird erwartet?** Text ist im gerenderten UI-Baum sichtbar.
- **Fehlerfall:** App stürzt beim Start ab, oder der Text fehlt.
- **Defaults:** Happy Case = Text sichtbar nach Start. Leere Eingabe =
  leerer Text aus C-002 → Screen bleibt leer, kein Absturz erwartet.
  Ungültiger Wert — passt nicht. Fehlende Verbindung — passt nicht,
  I-004 hat keine externe Abhängigkeit.

#### T-003

- **Prüft:** S-001.
- **Was wird geprüft?** Das Ergebnis aus `ui.md` — dass nach der
  Anzeige nichts weiter passiert.
- **Womit?** UI-Test, prüft Abwesenheit von Navigation oder
  Zustandswechsel nach dem Start.
- **Was wird erwartet?** App bleibt auf S-001, keine Navigation wird
  ausgelöst.
- **Fehlerfall:** unerwartete Navigation oder Absturz.
- **Defaults:** Happy Case = Screen bleibt stabil. Leere Eingabe,
  ungültiger Wert, fehlende Verbindung — passt nicht, S-001 nimmt keine
  Eingabe entgegen.

#### T-004

- **Prüft:** C-001.
- **mockt:** X-001, X-002, X-003, X-004.
- **Was wird geprüft?** Dass der Workflow die Stufen Build → Test →
  Android-Einreichung → iOS-Einreichung in der richtigen Reihenfolge
  durchläuft und bei einem Fehlschlag abbricht.
- **Womit?** Lokale Simulation der Workflow-Definition (z. B. mit
  `act`), alle externen Komponenten gemockt, damit der Workflow allein
  im Fokus steht.
- **Was wird erwartet?** Stufenreihenfolge eingehalten; ein Fehlschlag
  in einer Stufe verhindert die nachfolgenden.
- **Fehlerfall:** Build oder Test schlägt fehl → keine Einreichung wird
  ausgelöst.
- **Defaults:** Happy Case = alle Stufen laufen durch. Leere Eingabe =
  Push ohne Änderungen → Workflow läuft trotzdem (kein Sonderfall).
  Ungültiger Wert = Code kompiliert nicht → Abbruch in der
  Build-Stufe. Fehlende Verbindung = X-001 selbst nicht erreichbar —
  passt nicht, das ist die Ausführungsplattform selbst, kein Aufruf von
  C-001 aus.

#### T-005

- **Prüft:** I-001.
- **mockt:** X-001.
- **Was wird geprüft?** Dass ein simulierter Push-Event den Workflow
  auslöst und den richtigen Commit-Stand übernimmt.
- **Womit?** Lokale Simulation des Trigger-Events.
- **Was wird erwartet?** Workflow startet mit dem Source-Stand des
  simulierten Commits.
- **Fehlerfall:** kein Push-Event ankommt.
- **Defaults:** Happy Case = Workflow startet mit korrektem Commit.
  Leere Eingabe = Push ohne Dateiänderung → Workflow startet trotzdem,
  passt zum Modell (jeder Push ist ein Auslöser). Ungültiger Wert —
  passt nicht. Fehlende Verbindung = kein Push-Event → Pipeline bleibt
  inaktiv, das ist der Ausgangszustand, kein Fehlerfall.

#### T-006

- **Prüft:** I-002.
- **mockt:** X-002.
- **laeuft-gegen:** X-004.
- **Was wird geprüft?** Dass C-001 ein Android-Build-Artefakt über
  Fastlane korrekt an die (gemockte) Google Play Console übergibt.
- **Womit?** Echtes Fastlane (Lib, läuft im selben Prozess), simulierte
  Play-Developer-API-Antwort.
- **Was wird erwartet?** AAB + Metadaten werden mit korrektem Format
  übergeben, gemockte Antwort "erfolgreich eingereicht" wird
  weitergereicht.
- **Fehlerfall:** gemockte Fehlerantwort der Play Console → I-002
  meldet Fehlschlag, Workflow bricht in dieser Stufe ab.
- **Defaults:** Happy Case = Einreichung erfolgreich. Leere Eingabe =
  kein Build-Artefakt vorhanden → Stufe bricht vor dem Aufruf ab.
  Ungültiger Wert = fehlerhaftes AAB → Fastlane meldet Validierungsfehler.
  Fehlende Verbindung = gemockter Verbindungsfehler zur Play Console →
  Stufe schlägt fehl, sichtbar im Actions-Log.
- **Hinweis:** Läuft echt gegen Fastlane, deshalb per Modell-Definition
  Integration trotz einem `prueft`-Ziel — siehe `extern.md` X-004 und
  die Unschärfe oben im Text.

#### T-007

- **Prüft:** I-003.
- **mockt:** X-003.
- **laeuft-gegen:** X-004.
- **Was wird geprüft?** Dass C-001 ein iOS-Build-Artefakt über Fastlane
  korrekt an das (gemockte) App Store Connect übergibt.
- **Womit?** Echtes Fastlane, simulierte App-Store-Connect-API-Antwort.
- **Was wird erwartet?** IPA + Metadaten werden mit korrektem Format
  übergeben, gemockte Antwort "eingereicht, in Prüfung" wird
  weitergereicht.
- **Fehlerfall:** gemockte Ablehnung (z. B. Guideline 4.2) oder
  Upload-Fehler → I-003 meldet Fehlschlag, gilt selbst als Ergebnis
  (G-002).
- **Defaults:** Happy Case = Einreichung erfolgreich, "in Prüfung".
  Leere Eingabe = kein Build-Artefakt → Stufe bricht vor dem Aufruf ab.
  Ungültiger Wert = fehlerhaftes IPA/Signatur → Fastlane meldet
  Validierungsfehler. Fehlende Verbindung = gemockter Verbindungsfehler
  zu App Store Connect → Stufe schlägt fehl, sichtbar im Actions-Log.
- **Hinweis:** wie T-006 per Modell-Definition Integration trotz einem
  `prueft`-Ziel.

### 2. Integrationstests

**Explizit gewählte Subsets.** Nicht alle Kombinationen — nur die, die
für das System entscheidend sind.

Für jeden Test:
- **ID**
- **Prüft** — das Subset (`C-`, `I-`, `S-`)
- **Warum dieses Subset?** — die Begründung.
- **Was wird geprüft?**
- **Nicht-trivialer Fehlerfall**

#### T-008

- **Prüft:** C-001, C-002, I-001, I-002, I-003.
- **mockt:** X-001, X-002, X-003.
- **laeuft-gegen:** X-004.
- **Warum dieses Subset?** Das ist der eigentliche Zweck des Projekts
  (G-003): Erst im Zusammenspiel zeigt sich, dass eine Source-Änderung
  tatsächlich bis zur Store-Einreichung durchläuft — jeder Einzeltest
  davor prüft nur ein Glied der Kette.
- **Was wird geprüft?** Eine geänderte Zeichenkette in C-002 (z. B.
  "Hello World" → "Hallo Welt") ist nach einem simulierten Lauf im
  eingereichten Artefakt für Android und iOS wiederzufinden.
- **Nicht-trivialer Fehlerfall:** eine mittlere Stufe (z. B.
  Android-Einreichung) schlägt fehl, während die andere (iOS) erfolgreich
  ist — die Kette muss das als Teilerfolg sichtbar machen, nicht als
  Gesamterfolg melden.
- **Defaults:** Happy Case = geänderter Text erreicht beide Stores.
  Leere Eingabe — passt nicht, ein Push ohne Änderung ist kein
  Sonderfall (siehe T-005). Ungültiger Wert = nicht kompilierender Code
  → Kette bricht in der Build-Stufe ab, vor jeder Einreichung. Fehlende
  Verbindung = eine der beiden Store-Verbindungen gemockt nicht
  erreichbar → die andere Stufe läuft unabhängig weiter (siehe
  nicht-trivialer Fehlerfall).

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

Beantwortet bei jedem `T-` oben (T-001 bis T-008), je mit Begründung, wo
ein Punkt nicht passt.

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

Nicht getestet: A-001 — ein Akteur ist kein Code. Geprüft wird, was er
bedient: I-001 (T-005). X-001 bis X-004 werden nie selbst getestet —
geprüft wird, wie C-001 mit ihnen umgeht (T-004, T-006, T-007, T-008).

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

- [x] Unit-Tests pro Prüfling
- [x] Integrationstests (explizit gewählt)
- [x] Defaults (Happy Case, triviale Fehlerfälle)
- [x] Was wird nicht getestet?

## Notizen
