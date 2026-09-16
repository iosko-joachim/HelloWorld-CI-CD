---
description: Welche Daten das System festhält. Laden bei Datenmodell, bei
  Schlüsseln, bei der Frage "was steht wo und wie lange".
---

# Daten

**Was hält das System fest, und wie lange?**

Nicht die Tabellen, nicht die Technik. Nur: Welche Dinge gibt es, woran
erkennt man eins, und wann verschwindet es wieder.

## Fragen

### 1. Welche Datenentitäten gibt es?

Für jede:
- **ID**
- **Name**
- **Was sie festhält** — in einem Satz
- **Wer sie hält** — welche Komponente aus `struktur.md` (`C-`)
- **Beachtet** — welches Nicht-Ziel begrenzt sie? (`NG-`, wenn eines)

Eine Entität ist etwas, das man zählen kann und das einen Schlüssel hat.
Ein abgeleiteter Wert ist keine Entität — er gehört in Frage 5.

### 2. Welche Felder hat jede, und was ist der Schlüssel?

Für jede:
- **Schlüssel** — woran erkennt man genau dieses eine?
- **Felder** — was steht drin?
- **Abgeleitet** — was steht nicht drin, sondern wird berechnet?

Ein Schlüssel, den ein Mensch tippen muss, ist ein anderer als einer, den
nur das System liest. Sag welchen du meinst.

### 3. Wie hängen sie zusammen?

Welche Entität verweist auf welche? Als Diagramm.

Die Richtung sagt, wer von wem abhängt — mehr nicht. Was geschieht, wenn das
Ziel verschwindet, ist eine eigene Entscheidung. Für jeden Verweis eine von
drei Antworten:

| Verschwindet das Ziel | Heißt |
|---|---|
| **verhindern** | Das Ziel kann nicht weg, solange jemand darauf zeigt |
| **mitlöschen** | Geht das Ziel, geht auch, was darauf zeigt |
| **loslassen** | Der Verweisende bleibt, ohne Ziel |

**Verschwinden** heißt beides: jemand entfernt es, oder es endet von selbst
(Frage 4). Ist das Ziel flüchtig, fällt „verhindern" weg — ein Ereignis
lässt sich nicht mit einem Veto belegen; dann bleiben zwei.

Ob eine Bestellung ohne Kunden sinnlos oder bloß unvollständig ist, folgt
aus nichts anderem im Modell — das muss hier stehen. Wie es später
geschrieben wird, steht nicht hier: Das ist Technik.

### 4. Wie lange lebt jede?

Für jede eine von zwei Lebensdauern:

| Lebensdauer | Heißt |
|---|---|
| **dauerhaft** | bleibt, bis jemand sie ausdrücklich entfernt |
| **flüchtig** | endet an einem benannten Ereignis oder einer Bedingung |

Bei jeder flüchtigen Entität: **woran genau** endet sie? „Nach dem Lauf"
ist keine Antwort, wenn sie den Lauf überdauern kann.

„Abgeleitet" ist keine Lebensdauer, sondern eine Herkunft — und keine
Entität (Frage 1). Es gehört in Frage 5.

### 5. Was wird ausdrücklich nicht gespeichert?

Was könnte man naheliegenderweise festhalten und tut es bewusst nicht?

Das sind **Nicht-Ziele**, also `NG-`, und die entstehen in `ziel.md`
Frage 3 — gefragt wird hier, geschrieben wird dort. Sonst bliebe die
Antwort Fließtext ohne ID, und die Entität, die sie begrenzt, könnte mit
`beachtet` nicht darauf zeigen (Frage 1).

Abgeleitete Werte gehören hierher: Was berechnet wird, wird nicht
gespeichert — sonst laufen die beiden auseinander.

## Was hier entsteht

- `D-` Datenentitäten

Ordner: `projekt/daten/`

Ein abgestimmter Eintrag trägt darunter die Zeile
`Abgestimmt: <wer>, <wann>` — ab dann ist seine ID verbraucht und wird bei
Aufgabe ausgemustert statt umnummeriert (`metamodell.md`).

Ausgemustert: —

## Querverweise

- **Geht aus:** `gehalten-von` → C-, `verweist-auf` → D-, `beachtet` → NG-
- **Kommt an:** `verweist-auf` von D-, `verarbeitet` von C-,
  `betrifft` von RISK-, `entscheidet-ueber` von ADR-

## Was hier nicht entsteht

- Tabellen, Schemata, Migrationen (das ist Technik)
- Komponenten (die stehen in `struktur.md`)
- Tests (die stehen in `tests.md`)

## Zustand

- [ ] Welche Datenentitäten gibt es?
- [ ] Welche Felder hat jede, und was ist der Schlüssel?
- [ ] Wie hängen sie zusammen?
- [ ] Wie lange lebt jede?
- [ ] Was wird ausdrücklich nicht gespeichert?

## Notizen
