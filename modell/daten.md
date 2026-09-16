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

Keine. Das System hält keine Daten fest — es beachtet NG-002 (kein
Backend, keine Datenhaltung). Was während eines Laufs entsteht — die
Build-Artefakte AAB und IPA aus C-002 — ist ein flüchtiges
Zwischenerzeugnis der Pipeline (C-001), keine Entität mit eigenem
Lebenszyklus: Es wird erzeugt, an I-002/I-003 übergeben und danach nicht
weiter gehalten.

### 2. Welche Felder hat jede, und was ist der Schlüssel?

Für jede:
- **Schlüssel** — woran erkennt man genau dieses eine?
- **Felder** — was steht drin?
- **Abgeleitet** — was steht nicht drin, sondern wird berechnet?

Ein Schlüssel, den ein Mensch tippen muss, ist ein anderer als einer, den
nur das System liest. Sag welchen du meinst.

Entfällt — keine Entität aus Frage 1.

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

Entfällt — keine Entität, also kein Verweis.

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

Entfällt — keine Entität mit Lebensdauer. Das flüchtige Zwischenerzeugnis
aus Frage 1 (AAB/IPA) ist keine Entität, deshalb keine Lebensdauer im
Sinn dieser Frage.

### 5. Was wird ausdrücklich nicht gespeichert?

Was könnte man naheliegenderweise festhalten und tut es bewusst nicht?

Das sind **Nicht-Ziele**, also `NG-`, und die entstehen in `ziel.md`
Frage 3 — gefragt wird hier, geschrieben wird dort. Sonst bliebe die
Antwort Fließtext ohne ID, und die Entität, die sie begrenzt, könnte mit
`beachtet` nicht darauf zeigen (Frage 1).

Abgeleitete Werte gehören hierher: Was berechnet wird, wird nicht
gespeichert — sonst laufen die beiden auseinander.

Nutzerdaten, Analytics, Absturzberichte — alles, was eine echte App
naheliegenderweise sammeln würde. Steht als NG-002 in `ziel.md`
(„Kein Backend, keine Datenhaltung"). Version- und Build-Nummern für die
Stores werden nicht als eigener Zustand gehalten, sondern bei jedem Lauf
aus dem Commit/Zähler von C-001 abgeleitet.

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

- [x] Welche Datenentitäten gibt es?
- [x] Welche Felder hat jede, und was ist der Schlüssel?
- [x] Wie hängen sie zusammen?
- [x] Wie lange lebt jede?
- [x] Was wird ausdrücklich nicht gespeichert?

## Notizen
