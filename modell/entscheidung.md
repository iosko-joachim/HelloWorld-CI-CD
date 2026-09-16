---
description: Was gewählt wurde und wogegen. Laden bei Weichenstellungen, die
  mehr als ein Artefakt betreffen, und bei der Frage "warum eigentlich so und
  nicht anders".
---

# Entscheidung

**Was haben wir gewählt, und wogegen?**

Das Ergebnis einer Entscheidung steht schon in den anderen Templates: welche
Komponenten es gibt, welche Bibliothek benutzt wird. Was dort nicht steht,
ist die verworfene Alternative. Ohne sie sieht das Ergebnis in drei Monaten
alternativlos aus, und die Abwägung beginnt von vorn.

Betrifft eine Entscheidung genau ein Artefakt, gehört sie in dessen Template.
Betrifft sie mehrere oder das Ganze, ist sie ein `ADR-`.

## Fragen

### 1. Was wurde entschieden?

In einem Satz. Das Ergebnis, nicht der Weg dorthin.

### 2. Was wurde verworfen, und warum?

Die Alternativen, die ernsthaft im Raum standen. Ohne sie ist es kein ADR,
sondern eine Notiz.

Löst diese Entscheidung eine frühere ab, nenne sie hier im Fließtext, als
`[[…]]`-Verweis — nicht im Frontmatter. Sonst gälte jeder ADR, den noch
keiner abgelöst hat, als verwaist.

### 3. Woran hing es?

Das Kriterium, das den Ausschlag gab. Daran erkennt man später, ob die
Entscheidung noch trägt: Gilt das Kriterium nicht mehr, gehört sie auf den
Tisch.

### 4. Was folgt daraus?

Welche Artefakte sind so, wie sie sind, wegen dieser Entscheidung?

## Was hier entsteht

- `ADR-` Entscheidungen

Ordner: `projekt/entscheidung/`

Ein abgestimmter Eintrag trägt darunter die Zeile
`Abgestimmt: <wer>, <wann>` — ab dann ist seine ID verbraucht und wird bei
Aufgabe ausgemustert statt umnummeriert (`metamodell.md`).

Dieses Template hat als einziges **keine Zeile `Ausgemustert:`**. Ein
abgelöster ADR bleibt stehen: Dass eine Entscheidung nicht mehr gilt, ist
selbst eine Entscheidung und wird als neuer ADR geschrieben. Überall sonst
liegt die Historie in Git — hier ist sie der Inhalt.

## Querverweise

- **Geht aus:** `entscheidet-ueber` → G-, NG-, C-, I-, X-, S-, A-, D-
- **Kommt an:** keine

## Was hier nicht entsteht

- Änderungsprotokolle (die trägt Git)
- Risiken (die stehen in `risiko.md`)
- Beschreibungen des Gebauten (die stehen in den anderen Templates)

## Zustand

- [ ] Was wurde entschieden?
- [ ] Was wurde verworfen, und warum?
- [ ] Woran hing es?
- [ ] Was folgt daraus?

## Notizen
