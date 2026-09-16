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

#### RISK-001 TestFlight-Build hängt an fehlender Export-Compliance

- **Risiko:** Apple gibt einen hochgeladenen Build erst an Tester frei,
  wenn die Frage nach Verschlüsselung beantwortet ist. Fehlt die Angabe,
  bleibt der Build auf „Fehlende Compliance" stehen, und die Kette endet
  vor dem Gerät.
- **Betrifft:** G-002, X-003.
- **Woran man es merkt:** Build steht in App Store Connect auf „Missing
  Compliance", I-003 selbst meldet Erfolg.

#### RISK-002 Google lässt auch den internen Test noch nicht zu

- **Risiko:** Solange die App bei Google Play als Entwurf gilt oder ihre
  Einrichtung unvollständig ist, lehnt die Play Console auch
  Releases im internen Test ab oder erlaubt nur Entwurfs-Releases.
- **Betrifft:** G-002, X-002.
- **Woran man es merkt:** I-002 schlägt mit einem „Google Api Error" fehl,
  obwohl das AAB angenommen wurde.

#### RISK-003 Signierung/Secrets falsch gehandhabt

- **Risiko:** Apple-Zertifikate/Provisioning-Profile oder der
  Android-Keystore werden falsch abgelegt — im Klartext im Repository,
  oder mit zu weiten Zugriffsrechten in GitHub Actions.
- **Betrifft:** C-001, X-001.
- **Woran man es merkt:** Secret taucht im Diff, im Log oder in der
  Historie auf; im schlimmsten Fall Missbrauch der Entwickler-Konten.

#### RISK-004 Ungewollte Einreichung durch jeden Push

- **Risiko:** Löste jeder Push auf `main` eine Einreichung aus (G-001,
  I-001), ginge auch ein nicht dafür gedachter Commit an die Tester.
- **Betrifft:** G-002, C-001.
- **Woran man es merkt:** neuer Build in Play Console/TestFlight nach
  einem Push, der nicht dafür gedacht war.

#### RISK-005 iOS-Build braucht einen macOS-Runner

- **Risiko:** Kotlin Multiplatform mit Compose Multiplatform baut das
  iOS-Target nur auf macOS (Xcode-Toolchain) — GitHub-gehostete
  macOS-Runner sind knapper und teurer als Linux-Runner.
- **Betrifft:** C-002, C-001, I-003.
- **Woran man es merkt:** Build-Stufe für iOS schlägt auf einem
  Linux-Runner fehl, oder das Minutenkontingent für macOS-Runner ist
  erschöpft.

#### RISK-006 TestFlight-Update zeigt auf dem iPhone den alten Stand

- **Risiko:** Nach dem Update über TestFlight meldet das iPhone den
  neuen Build, die App zeigt aber weiter den alten Text; erst Löschen und
  Neuinstallieren bringt den neuen Stand.
- **Betrifft:** G-003, X-003.
- **Woran man es merkt:** TestFlight nennt den neuen Build, die App zeigt
  den Text des vorigen. Beobachtet am 2026-09-16 mit Build 24 (iOS 27,
  kurz nach dem Systemupdate): „Hallo Welt" statt „Здравей, свят!",
  während Android aus demselben Lauf richtig war. Ursache ungeklärt.

### 2. Wie wahrscheinlich, wie schlimm?

Für jedes Risiko:
- **Wahrscheinlich** — niedrig, mittel, hoch
- **Wirkung** — niedrig, mittel, hoch

| ID | Wahrscheinlich | Wirkung |
|---|---|---|
| RISK-001 | hoch | mittel |
| RISK-002 | mittel | mittel |
| RISK-003 | mittel | hoch |
| RISK-004 | mittel | niedrig |
| RISK-005 | mittel | mittel |
| RISK-006 | mittel | niedrig |

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
| RISK-001 | vermeiden — `ITSAppUsesNonExemptEncryption = false` in `Info.plist`, die App verschlüsselt nichts |
| RISK-002 | beobachten — die Annotation von I-002 in der Lauf-Zusammenfassung zeigt die Meldung; ggf. Einrichtung in der Play Console nachholen |
| RISK-003 | vermeiden — GitHub Secrets, keine Zertifikate/Keystores im Repository; iOS-Zertifikate verwaltet Apple selbst (Cloud-Signing, ADR-005) |
| RISK-004 | vermeiden — Einreichung nur per Knopfdruck, ein Push baut und testet nur (ADR-004) |
| RISK-005 | abfedern — macOS-Runner explizit für die iOS-Stufe im Workflow einplanen |
| RISK-006 | hinnehmen — App löschen und neu installieren |

### 4. Was nehmen wir bewusst hin?

Welche Risiken bleiben, obwohl wir sie kennen? Und warum?

Die Liste selbst wird nicht geführt — sie ist abgeleitet: alle Risiken mit
Umgang `hinnehmen` aus Frage 3. Gepflegt wird nur das **Warum**; sonst
veraltet sie, sobald ein Risiko seinen Umgang ändert.

**Warum bei RISK-006:** Das Projekt soll zeigen, dass GitHub für beide
Plattformen bauen und ausliefern kann (G-001 bis G-003). Das ist
gezeigt; einem Detailproblem der Aktualisierung auf dem iPhone wird
bewusst nicht nachgegangen, Löschen und Neuinstallieren reicht.

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
