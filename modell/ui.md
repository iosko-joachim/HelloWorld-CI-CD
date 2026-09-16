---
description: Screens und ihre Reihenfolge. Laden bei UI-Fragen, bei der
  Beschreibung von Oberflächen, bei der Frage "wie sieht das aus".
---

# UI

Die Oberfläche. **Welche Screens gibt es, und in welcher Reihenfolge?**

## So arbeitest du mit diesem Template

Der Text hier ist der **Anker**. Das Mockup ist die **Überprüfung**.

1. Wähle einen Screen.
2. Beschreibe ihn textuell (Zweck, Ablauf, Ergebnis).
3. Lass ihn generieren (Mockup).
4. Schau ihn an.
5. Ändere den Text, wenn nötig.
6. Wiederhole 3–5, bis es passt.
7. Mach weiter mit dem nächsten Screen.

Der Kreislauf endet, wenn **du** sagst: „So passt es."
Es gibt keine andere Abbruchbedingung.

## Fragen

### 1. Welche Screens gibt es?

Für jeden Screen:
- **ID**
- **Name**
- **Zweck** — was tut der Mensch hier?
- **Ablauf** — was passiert?
- **Ergebnis** — was ist danach anders?
- **Rolle** — zentral oder peripher?
- **Zeigt** — welche Komponente? (`C-`)
- **Beachtet** — welches Nicht-Ziel begrenzt ihn? (`NG-`, wenn eines)

Keine Layout-Details. Keine Farben. Keine Positionen. Das kommt im Mockup.

### 2. In welcher Reihenfolge werden die Screens durchlaufen?

Als Diagramm. (Mermaid.)

### 3. Welche Screens sind zentral?

Zentral heißt: Der Screen gehört zur Kernlogik.
Peripher heißt: Er ist da, um die Kernlogik zu ermöglichen.

## Was hier entsteht

- `S-` Screens

Ordner: `projekt/ui/`

Ein abgestimmter Eintrag trägt darunter die Zeile
`Abgestimmt: <wer>, <wann>` — ab dann ist seine ID verbraucht und wird bei
Aufgabe ausgemustert statt umnummeriert (`metamodell.md`).

Ausgemustert: —

## Querverweise

- **Geht aus:** `zeigt` → C-, `beachtet` → NG-
- **Kommt an:** `bedient` von A-, `prueft` von T-, `betrifft` von RISK-,
  `entscheidet-ueber` von ADR-

## Was hier nicht entsteht

- Mockups (die entstehen im Kreislauf, separat)
- Layout-Details (die kommen im Mockup)
- Technische Umsetzung (die kommt später)

## Zustand

- [ ] Welche Screens gibt es?
- [ ] In welcher Reihenfolge werden die Screens durchlaufen?
- [ ] Welche Screens sind zentral?

## Notizen
