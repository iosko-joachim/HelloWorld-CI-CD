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
automatisch gebaut und getestet und auf Knopfdruck in die Testschienen von
Google Play und Apple TestFlight eingereicht.

### 2. Was ist die Kernlogik?

Der CI/CD-Workflow ist der Mittelpunkt — GitHub Actions, das Build, Test
und Deployment zu Apple und Google steuert. Die App ist peripher: Sie ist
nur der Träger, an dem die Pipeline sichtbar wird; ihr Inhalt (Hello
World / Hallo Welt) ist absichtlich nebensächlich.

**Entschieden:**
- GitHub (Actions) ist die zentrale CI/CD-Plattform.
- Tech-Stack: Kotlin Multiplatform mit Compose Multiplatform — eine
  Codebasis für Android und iOS.
- Auslöser: Push auf das Repository für Build und Test, Knopfdruck für
  die Einreichung (ADR-004).
- Ziel des Deployments: die Testschienen — Google Play „Interner Test",
  Apple TestFlight —, kein öffentlicher Release (NG-004, ADR-003).
- Zugangsdaten liegen als GitHub Actions Secrets, nicht Geheimes in
  `fastlane/.env.default` (RISK-003).

**Offen:** —

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

#### NG-004 Kein öffentlicher Store-Release

Die App geht nur in die Testschienen (Google Play „Interner Test", Apple
TestFlight) und wird nicht für fremde Nutzer im Store veröffentlicht.

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

#### G-002 Automatische Einreichung in die Testschienen beider Stores

Auf Knopfdruck reicht die Pipeline die App bei Google Play („Interner
Test") und in Apple TestFlight ein — ohne manuellen Zwischenschritt.
Scheitert die Einreichung an einer Vorgabe des Stores, ist die
Fehlermeldung selbst ein Ergebnis: Sie zeigt, dass die Kette bis dorthin
lief.

#### G-003 Sichtbare Source-zu-Gerät-Kette

Eine Änderung auf Source-Ebene (z. B. "Hello World" → "Hallo Welt") ist
nach einem Durchlauf der Pipeline in der App auf dem eigenen Testgerät
zu sehen.

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
