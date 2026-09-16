---
description: Externe Komponenten und ihre Integration. Laden bei Abhängigkeiten,
  bei der Frage "was benutzen wir von außen".
---

# Extern

**Was benutzen wir, das wir nicht selbst bauen?**

Externe Komponenten sind die Grenze zwischen „was wir bauen" und „was wir
benutzen". Sie sind nicht Teil des Projekts, aber sie sind Teil des Systems.

Nicht zu verwechseln mit den **Akteuren** aus `struktur.md`: Beide werden
nicht gebaut, aber extern ist, was das System *benutzt* — ein Akteur ist,
wer es benutzt.

## Fragen

### 1. Welche externen Komponenten gibt es?

Für jede:
- **ID**
- **Name**
- **Art** — Lib, Dienst, Gerät, Datenbank
- **Wofür benutzt** — welche Komponente aus `struktur.md` nutzt sie
- **Besitzer** — wir, ein Dritter

#### X-001 GitHub Actions

- **Art:** Dienst (CI/CD-Ausführungsplattform).
- **Wofür benutzt:** C-001 — führt den Workflow aus, der I-001 bis
  I-003 durchläuft.
- **Besitzer:** Dritter (GitHub).

#### X-002 Google Play Console

- **Art:** Dienst (Play Developer API).
- **Wofür benutzt:** C-001, Stufe I-002 (Android-Einreichung), über
  X-004.
- **Besitzer:** Dritter (Google).

#### X-003 Apple App Store Connect

- **Art:** Dienst (App Store Connect API).
- **Wofür benutzt:** C-001, Stufe I-003 (iOS-Einreichung), über X-004.
- **Besitzer:** Dritter (Apple).

#### X-004 Fastlane

- **Art:** Lib (CLI-Tool, läuft als Prozess innerhalb der Pipeline).
- **Wofür benutzt:** C-001, kapselt Signierung und Upload für I-002 und
  I-003.
- **Besitzer:** Dritter (Open-Source-Community).

### 2. Was, wenn sie ausfällt?

Für jede:
- **Fällt aus?** — ja/nein. Auch eine Lib kann Fehler liefern, hängen
  oder abstürzen; „nein" braucht eine Begründung.
- **Fallback** — gibt es einen Ersatz?
- **Fehlerverhalten** — was tut das System?
- **Sichtbar für den Menschen?** — merkt der Mensch es?

#### X-001 GitHub Actions

- **Fällt aus?** Ja — Wartungsfenster, Störungen, Minuten-Limit
  überschritten.
- **Fallback:** keiner. Kein zweiter CI-Anbieter vorgesehen.
- **Fehlerverhalten:** Der Workflow startet nicht oder bricht ab; kein
  Build, keine Einreichung.
- **Sichtbar für den Menschen?** Ja — am fehlenden oder roten
  Workflow-Lauf in GitHub.

#### X-002 Google Play Console

- **Fällt aus?** Ja — Störung oder API-Fehler bei Google.
- **Fallback:** keiner. Einreichung verzögert sich bis zum nächsten
  erfolgreichen Lauf.
- **Fehlerverhalten:** I-002 schlägt fehl, Workflow bricht in dieser
  Stufe ab, Fehlermeldung im Actions-Log.
- **Sichtbar für den Menschen?** Ja.

#### X-003 Apple App Store Connect

- **Fällt aus?** Ja — Störung oder API-Fehler bei Apple.
- **Fallback:** keiner.
- **Fehlerverhalten:** I-003 schlägt fehl, Fehlermeldung im Actions-Log;
  oder der Build bleibt in TestFlight hängen (RISK-001).
- **Sichtbar für den Menschen?** Ja.

#### X-004 Fastlane

- **Fällt aus?** Ja — Bug, Breaking Change in einer neuen Version,
  inkompatible Plugin-Version.
- **Fallback:** Versions-Pinning auf eine getestete Fastlane-Version;
  kein Ersatz-Tool vorgesehen.
- **Fehlerverhalten:** der jeweilige Workflow-Schritt (I-002 oder I-003)
  schlägt fehl.
- **Sichtbar für den Menschen?** Ja.

### 3. Wie wird sie im Test behandelt?

Geprüft wird nie die externe Komponente selbst, sondern wie **unsere** mit
ihr umgeht. Dafür wird sie im Test entweder **ersetzt** oder **beteiligt**,
und die Art aus Frage 1 entscheidet, was passt:

| Art | Naheliegend |
|---|---|
| Lib | echt — sie läuft im selben Prozess, ein Mock wäre Mehrarbeit für weniger Aussage |
| Datenbank | echt, gegen eine Testinstanz |
| Dienst | Mock, wenn er Geld kostet, Limits hat oder nicht uns gehört |
| Gerät | Mock, wenn es beim Testen nicht dasteht |

Für jede:
- **Ersetzt, beteiligt oder beides?** — Mock (`mockt`), echt
  (`laeuft-gegen`), oder je nach Test das eine und das andere
- **Warum so?** — mit Blick auf die Art. Ein reines Rechenstück kann man
  einbeziehen; bei einem Gerät, das beim Testen nicht dasteht, bleibt nur
  der Mock. Das entscheidet, wer die Komponente vor sich hat — die Tabelle
  oben legt nahe, sie schreibt nicht vor.
- **Wenn ersetzt: wie sieht der Mock aus?** — was liefert er?
- **Welche Tests?** — abgeleitet: alle `T-` mit `mockt: X-…` beziehungsweise
  `laeuft-gegen: X-…`. Diese Listen werden nicht gepflegt, sondern
  abgefragt — sonst veralten sie, sobald ein Test dazukommt.

#### X-001 GitHub Actions

- **Ersetzt.**
- **Warum so:** ein echter Lauf verbraucht Minuten und hat Limits;
  Workflow-Logik lässt sich lokal simulieren.
- **Mock:** lokale Ausführung der einzelnen Schritte/Skripte (z. B. mit
  `act`) statt eines echten GitHub-Runners.

#### X-002 Google Play Console

- **Ersetzt.**
- **Warum so:** Dienst eines Dritten mit Limits/Kosten, gehört nicht
  uns.
- **Mock:** simulierte Play-Developer-API-Antwort (Erfolg, typischer
  Fehlerfall).

#### X-003 Apple App Store Connect

- **Ersetzt.**
- **Warum so:** Dienst eines Dritten mit Limits/Kosten, gehört nicht
  uns.
- **Mock:** simulierte App-Store-Connect-API-Antwort (Erfolg,
  Upload-Fehler).

#### X-004 Fastlane

- **Beteiligt (echt).**
- **Warum so:** Lib, läuft im selben Prozess wie die Pipeline — ein
  Mock wäre Mehrarbeit für weniger Aussage.

**Ersetzt** heißt: Der Prüfling bleibt allein, der Test ist ein Unit-Test,
geprüft wird die Nutzung gegen unsere Annahme. **Beteiligt** heißt: Der Test
ist ein Integrationstest und prüft nebenbei, ob die Annahme noch stimmt —
ein Mock kann nicht bemerken, wenn die externe Komponente sich ändert. Wer
ersetzt, nimmt das in Kauf, und das gehört in die Begründung.

### 4. Ist sie austauschbar?

Für jede:
- **Austauschbar?** — ja/nein
- **Wenn ja:** wodurch?
- **Wenn nein:** warum nicht?

#### X-001 GitHub Actions

- **Austauschbar?** Nein. G-001 verlangt ausdrücklich GitHub — das ist
  der Gegenstand der Demonstration.

#### X-002 Google Play Console

- **Austauschbar?** Nein. G-002 verlangt ausdrücklich Google Play als
  Android-Ziel.

#### X-003 Apple App Store Connect

- **Austauschbar?** Nein. G-002 verlangt ausdrücklich Apple TestFlight
  als iOS-Ziel.

#### X-004 Fastlane

- **Austauschbar?** Ja — durch die Store-APIs/CLIs direkt (Google Play
  Developer API, App Store Connect API), mit mehr Pipeline-Code.

## Was hier entsteht

- `X-` externe Komponenten

Ordner: `projekt/extern/`

Ein abgestimmter Eintrag trägt darunter die Zeile
`Abgestimmt: <wer>, <wann>` — ab dann ist seine ID verbraucht und wird bei
Aufgabe ausgemustert statt umnummeriert (`metamodell.md`).

Ausgemustert: —

## Querverweise

- **Geht aus:** `benutzt-von` → C-
- **Kommt an:** `mockt` von T-, `laeuft-gegen` von T-, `betrifft` von RISK-,
  `entscheidet-ueber` von ADR-

## Was hier nicht entsteht

- Die Nutzung im Detail (die steht in `struktur.md`)
- Tests (die stehen in `tests.md`)

## Zustand

- [x] Welche externen Komponenten gibt es?
- [x] Was, wenn sie ausfällt?
- [x] Wie wird sie im Test behandelt?
- [x] Ist sie austauschbar?

## Notizen
