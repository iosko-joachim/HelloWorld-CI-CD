---
description: Was soll das Projekt machen. Laden am Anfang, bei unklarem Zweck,
  bei Zielkonflikten, bei der Frage "wofür das alles".
---

# Ziel

Die grobe Antwort auf: **Was soll das Projekt machen?**

Darf grob sein. Wird später verfeinert.

## Fragen

### 1. Was soll das Projekt machen?

In einem Satz. Keine Details.

### 2. Was ist die Kernlogik?

Die Rolle einer Komponente, eines Akteurs oder einer Komposition aus
beidem, um die sich die peripheren Komponenten drehen. Was ist der
Mittelpunkt? Was ist peripher?

**Entschieden:** Was ist schon klar?
**Offen:** Was ist noch unklar?

### 3. Was ist ausdrücklich nicht das Ziel?

Die Nicht-Ziele. Genauso wichtig wie die Ziele.

Hierher gehören auch die Nicht-Ziele auf Datenebene — was bewusst nicht
gespeichert wird. Gefragt wird das in `daten.md` Frage 5, wenn es zur
Sprache kommt; das `NG-` entsteht hier.

### 4. Woran erkennt man, dass es funktioniert?

Keine Metriken. Nur: Woran würdest du merken, dass es das Richtige tut?

Hierher gehören auch die nicht-funktionalen Eigenschaften — schnell genug,
offline, zumutbar. Sie bekommen kein eigenes Präfix: Die Eigenschaft wird
als `G-` formuliert, ihr Ausbleiben als `RISK-`, ihre Prüfung als `T-`. Drei
Artefakte, ein Sachverhalt, feste Rollen — sonst steht dieselbe Auflage je
nach Gesprächsverlauf mal als Ziel, mal als Risiko, mal als Test da.

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

- [ ] Was soll das Projekt machen?
- [ ] Was ist die Kernlogik?
- [ ] Was ist nicht das Ziel?
- [ ] Woran erkennt man, dass es funktioniert?

## Notizen
