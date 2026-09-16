---
description: Was schiefgehen kann und was wir damit tun. Laden bei Risiken,
  bei Abwägungen, bei der Frage "was ist der Preis dieser Entscheidung".
---

# Risiko

**Was kann schiefgehen, und was tun wir damit?**

Ein Risiko ist kein Fehlerfall. Der Fehlerfall steht in der Schnittstelle
und wird behandelt; über das Risiko wird hier entschieden — vermeiden,
abfedern, beobachten oder hinnehmen.

## Fragen

### 1. Welche Risiken gibt es?

Für jedes Risiko:
- **ID**
- **Risiko** — was kann schiefgehen?
- **Betrifft** — welches Artefakt? (G-, NG-, C-, I-, X-, S-, A-, D-)
- **Woran man es merkt** — die messbare Spur

#### RISK-001 Apple-Review lehnt die App ab

- **Risiko:** Guideline 4.2 (Minimum Functionality) — Apple lehnt eine
  App ab, die nur "Hello World"/"Hallo Welt" zeigt.
- **Betrifft:** G-002, X-003.
- **Woran man es merkt:** Ablehnungsnachricht in App Store Connect,
  I-003 schlägt fehl.

#### RISK-002 Google Play verlangt eine Testphase vor Produktions-Release

- **Risiko:** Google Play verlangt für neue Entwicklerkonten häufig
  eine geschlossene Testphase mit einer Mindestzahl an Testern über
  eine Mindestdauer, bevor ein Produktions-Release möglich ist —
  automatischer Direkt-Release scheitert dann beim ersten Versuch.
- **Betrifft:** G-002, X-002.
- **Woran man es merkt:** Play Console verweigert den
  Produktions-Rollout, I-002 schlägt fehl oder landet nur in einer
  Testschiene.

#### RISK-003 Signierung/Secrets falsch gehandhabt

- **Risiko:** Apple-Zertifikate/Provisioning-Profile oder der
  Android-Keystore werden falsch abgelegt — im Klartext im Repository,
  oder mit zu weiten Zugriffsrechten in GitHub Actions.
- **Betrifft:** C-001, X-001.
- **Woran man es merkt:** Secret taucht im Diff, im Log oder in der
  Historie auf; im schlimmsten Fall Missbrauch der Entwickler-Konten.

#### RISK-004 Ungewollter Store-Release durch jeden Push

- **Risiko:** Da jeder Push auf `main` einen Store-Release auslöst
  (G-001, I-001), kann ein nicht dafür gedachter Commit einen echten
  Release erzeugen.
- **Betrifft:** G-002, C-001.
- **Woran man es merkt:** neuer Release in Play Console/App Store
  Connect nach einem Push, der nicht dafür gedacht war.

#### RISK-005 iOS-Build braucht einen macOS-Runner

- **Risiko:** Kotlin Multiplatform mit Compose Multiplatform baut das
  iOS-Target nur auf macOS (Xcode-Toolchain) — GitHub-gehostete
  macOS-Runner sind knapper und teurer als Linux-Runner.
- **Betrifft:** C-002, C-001, I-003.
- **Woran man es merkt:** Build-Stufe für iOS schlägt auf einem
  Linux-Runner fehl, oder das Minutenkontingent für macOS-Runner ist
  erschöpft.

### 2. Wie wahrscheinlich, wie schlimm?

Für jedes Risiko:
- **Wahrscheinlich** — niedrig, mittel, hoch
- **Wirkung** — niedrig, mittel, hoch

| ID | Wahrscheinlich | Wirkung |
|---|---|---|
| RISK-001 | mittel | mittel |
| RISK-002 | hoch | mittel |
| RISK-003 | mittel | hoch |
| RISK-004 | mittel | niedrig |
| RISK-005 | mittel | mittel |

### 3. Was tun wir dagegen?

Für jedes Risiko eine von vier Umgangsarten, nicht mehr:

| Umgang | Heißt |
|---|---|
| **vermeiden** | Das System ist so gebaut, dass es nicht eintritt |
| **abfedern** | Es tritt ein, aber es tut weniger weh |
| **beobachten** | Wir messen es und entscheiden später |
| **hinnehmen** | Wir tun nichts |

„Beobachten" ist nur ehrlich, wenn die messbare Spur aus Frage 1 wirklich
gemessen wird. Sonst ist es ein höfliches Wort für „hinnehmen".

| ID | Umgang |
|---|---|
| RISK-001 | hinnehmen |
| RISK-002 | hinnehmen |
| RISK-003 | vermeiden — GitHub Secrets, keine Zertifikate/Keystores im Repository, Fastlane `match` (oder vergleichbar) zur verschlüsselten Verwaltung |
| RISK-004 | beobachten — Release-Strategie ist noch offen (`ziel.md`); vorerst nur `main` als Auslöser, ein zusätzliches Gate wird entschieden, sobald es einmal gestört hat |
| RISK-005 | abfedern — macOS-Runner explizit für die iOS-Stufe im Workflow einplanen |

### 4. Was nehmen wir bewusst hin?

Welche Risiken bleiben, obwohl wir sie kennen? Und warum?

Die Liste selbst wird nicht geführt — sie ist abgeleitet: alle Risiken mit
Umgang `hinnehmen` aus Frage 3. Gepflegt wird nur das **Warum**; sonst
veraltet sie, sobald ein Risiko seinen Umgang ändert.

**Warum bei RISK-001 und RISK-002:** Das Ziel des Projekts ist die
automatische Einreichung bis zum Ende der Pipeline (G-002), nicht die
Garantie einer dauerhaften Veröffentlichung. Eine Ablehnung durch Apple
oder eine verlangte Testphase bei Google ist selbst ein Ergebnis — sie
zeigt, dass die Kette bis dorthin gelaufen ist — und keine Störung des
Ziels.

## Was hier entsteht

- `RISK-` Risiken

Ordner: `projekt/risiko/`

Ein abgestimmter Eintrag trägt darunter die Zeile
`Abgestimmt: <wer>, <wann>` — ab dann ist seine ID verbraucht und wird bei
Aufgabe ausgemustert statt umnummeriert (`metamodell.md`).

Ausgemustert: —

## Querverweise

- **Geht aus:** `betrifft` → G-, NG-, C-, I-, X-, S-, A-, D-
- **Kommt an:** keine

## Was hier nicht entsteht

- Fehlerfälle (die stehen in den `I-`)
- Maßnahmen mit Terminen (das ist Planung, nicht Struktur)
- Tests (die stehen in `tests.md`)

## Zustand

- [x] Welche Risiken gibt es?
- [x] Wie wahrscheinlich, wie schlimm?
- [x] Was tun wir dagegen?
- [x] Was nehmen wir bewusst hin?

## Notizen
