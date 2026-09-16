---
description: Was soll das Projekt machen. Laden am Anfang, bei unklarem Zweck,
  bei Zielkonflikten, bei der Frage "wofür das alles".
---

# Ziel

Die grobe Antwort auf: **Was soll das Projekt machen?**

Darf grob sein. Wird später verfeinert.

## Fragen

### 1. Was soll das Projekt machen?

Das Projekt demonstriert die CI/CD-Fähigkeiten von GitHub im Zusammenspiel
mit einem Apple- und einem Google-Entwicklerkonto: eine minimale mobile App
(Kotlin Multiplatform mit Compose Multiplatform) wird bei jedem Push
automatisch gebaut, getestet und in den Apple App Store und bei Google Play
veröffentlicht.

### 2. Was ist die Kernlogik?

Der CI/CD-Workflow ist der Mittelpunkt — GitHub Actions, das Build, Test
und Deployment zu Apple und Google steuert. Die App ist peripher: Sie ist
nur der Träger, an dem die Pipeline sichtbar wird; ihr Inhalt (Hello
World / Hallo Welt) ist absichtlich nebensächlich.

**Entschieden:**
- GitHub (Actions) ist die zentrale CI/CD-Plattform.
- Tech-Stack: Kotlin Multiplatform mit Compose Multiplatform — eine
  Codebasis für Android und iOS.
- Auslöser: Push auf das Repository.
- Ziel des Deployments: öffentlicher Store-Release, sowohl Google Play
  als auch Apple App Store.

**Offen:**
- Wie Signierung/Zertifikate (Apple) und Keystore (Google) als Secrets in
  GitHub Actions abgelegt werden.
- Ob Apples Review (Guideline 4.2, Mindestfunktionalität) eine triviale
  Hello-World-App überhaupt durchlässt — siehe `risiko.md`.
- Release-Strategie: jeder Push ein neuer Store-Release, oder nur bei
  Tags/Versionsbump?

### 3. Was ist ausdrücklich nicht das Ziel?

Die Nicht-Ziele. Genauso wichtig wie die Ziele.

Hierher gehören auch die Nicht-Ziele auf Datenebene — was bewusst nicht
gespeichert wird. Gefragt wird das in `daten.md` Frage 5, wenn es zur
Sprache kommt; das `NG-` entsteht hier.

#### NG-001 Keine echte App-Funktionalität

Die App zeigt nur "Hello World" bzw. nach Änderung "Hallo Welt" an. Kein
Funktionsumfang darüber hinaus, kein Anspruch an UI-Design.

#### NG-002 Kein Backend, keine Datenhaltung

Es gibt keine serverseitige Logik und keine gespeicherten Nutzerdaten.

#### NG-003 Keine manuellen Build- oder Deployment-Schritte

Build, Signierung und Einreichung laufen über die Pipeline, nicht über
manuelles Bauen, Signieren oder Hochladen in App Store Connect oder der
Play Console.

### 4. Woran erkennt man, dass es funktioniert?

Keine Metriken. Nur: Woran würdest du merken, dass es das Richtige tut?

Hierher gehören auch die nicht-funktionalen Eigenschaften — schnell genug,
offline, zumutbar. Sie bekommen kein eigenes Präfix: Die Eigenschaft wird
als `G-` formuliert, ihr Ausbleiben als `RISK-`, ihre Prüfung als `T-`. Drei
Artefakte, ein Sachverhalt, feste Rollen — sonst steht dieselbe Auflage je
nach Gesprächsverlauf mal als Ziel, mal als Risiko, mal als Test da.

#### G-001 Automatischer Build und Test bei jedem Push

Ein Push auf das Repository löst automatisch einen GitHub-Actions-Workflow
aus, der die App für Android und iOS baut und testet.

#### G-002 Automatische Einreichung bei beiden Stores

Bei erfolgreichem Build reicht die Pipeline die App automatisch bei
Google Play und im Apple App Store ein — ohne manuellen Zwischenschritt.
Ziel ist die automatische Einreichung bis zum Ende der Pipeline; ob die
Store-Prüfung die Veröffentlichung freigibt, steht außerhalb der
Kontrolle des Projekts. Eine Ablehnung (z. B. Apple Guideline 4.2) ist
kein Scheitern der Pipeline, sondern selbst ein Ergebnis — mindestens
eine Fehlermeldung an der Stelle, die zeigt, dass die Kette bis dorthin
lief.

#### G-003 Sichtbare Source-zu-Store-Kette

Eine Änderung auf Source-Ebene (z. B. "Hello World" → "Hallo Welt") ist
nach einem Durchlauf der Pipeline im eingereichten bzw. veröffentlichten
Artefakt nachvollziehbar.

## Was hier entsteht

- `G-` Ziele
- `NG-` Nicht-Ziele

Ordner: `projekt/ziel/`

Ein abgestimmter Eintrag trägt darunter die Zeile
`Abgestimmt: <wer>, <wann>` — ab dann ist seine ID verbraucht und wird bei
Aufgabe ausgemustert statt umnummeriert (`metamodell.md`).

Ausgemustert: —

## Querverweise

- **Geht aus:** keine (Ziele referenzieren nichts)
- **Kommt an:** `dient` von C- (auf G-), `beachtet` von C-, S- und D-
  (auf NG-), `betrifft` von RISK-, `entscheidet-ueber` von ADR-

Ein Nicht-Ziel ist ein vollwertiges Artefakt, keine Auslassung: Es grenzt
ab, und andere Artefakte berufen sich darauf.

## Was hier nicht entsteht

- Architektur (die kommt später)
- Tests (die kommen später)

## Zustand

- [x] Was soll das Projekt machen?
- [x] Was ist die Kernlogik?
- [x] Was ist nicht das Ziel?
- [x] Woran erkennt man, dass es funktioniert?

## Notizen
