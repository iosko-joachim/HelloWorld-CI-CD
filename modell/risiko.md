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

### 2. Wie wahrscheinlich, wie schlimm?

Für jedes Risiko:
- **Wahrscheinlich** — niedrig, mittel, hoch
- **Wirkung** — niedrig, mittel, hoch

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

### 4. Was nehmen wir bewusst hin?

Welche Risiken bleiben, obwohl wir sie kennen? Und warum?

Die Liste selbst wird nicht geführt — sie ist abgeleitet: alle Risiken mit
Umgang `hinnehmen` aus Frage 3. Gepflegt wird nur das **Warum**; sonst
veraltet sie, sobald ein Risiko seinen Umgang ändert.

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

- [ ] Welche Risiken gibt es?
- [ ] Wie wahrscheinlich, wie schlimm?
- [ ] Was tun wir dagegen?
- [ ] Was nehmen wir bewusst hin?

## Notizen
