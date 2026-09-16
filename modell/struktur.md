---
description: Aus welchen Komponenten besteht das Projekt. Laden bei Zerlegung,
  bei Architektur, bei der Frage "woraus besteht das Ganze".
---

# Struktur

Die statische Struktur. **Aus welchen Komponenten besteht das Ganze?**

Keine Abläufe. Keine Reihenfolgen. Nur: Was ist da, und wie hängt es zusammen.

## So arbeitest du mit diesem Template

Der Text hier ist der **Anker**. Das Diagramm ist die **Überprüfung**.

1. Beschreibe die Komponenten textuell.
2. Lass das Diagramm generieren (Mermaid oder echtes Bild).
3. Schau es an.
4. Ändere den Text, wenn nötig.
5. Wiederhole 2–4, bis es passt.

Der Kreislauf endet, wenn **du** sagst: „So passt es."

## Fragen

### 1. Welche Komponenten gibt es?

Für jede Komponente:
- **ID**
- **Name**
- **Aufgabe** — was tut sie, in einem Satz?
- **Rolle** — zentral oder peripher? (siehe Frage 5)
- **Dient** — welchem Ziel? (`G-`)
- **Verarbeitet** — welche Entitäten aus `daten.md`? (`D-`, wenn welche)
- **Beachtet** — welches Nicht-Ziel begrenzt sie? (`NG-`, wenn eines)

### 2. Wie hängen die Komponenten zusammen?

Welche Komponente ruft welche auf? Welche liefert Daten an welche?

Als Diagramm. (Mermaid.)

### 3. Welche Interfaces hat jede Komponente?

Für jedes Interface:
- **ID**
- **Gehört zu** — welche Komponente? (`C-`)
- **Eingabe** — was bekommt sie?
- **Ausgabe** — was liefert sie?
- **Empfänger** — wer bekommt die Ausgabe? (nicht „Aufrufer": bei einer
  Datenhaltung ruft niemand auf, dort wird geschrieben und gelesen)
- **Was wird übergeben?** — Format, Inhalt
- **Bei Erfolg** — was passiert danach?
- **Bei Fehler** — was passiert daneben?

### 4. Welche Komponenten sind extern?

Nur die Namen. Die Details kommen in `extern.md`.

### 5. Was ist die Kernlogik in der Struktur?

Die Kernlogik ist das, **um das die peripheren Komponenten herum sind**.

- Welche Komponente oder welcher **Akteur** ist der **Mittelpunkt**?
- Welche Komponenten sind **peripher**?
- Wenn kein einzelnes Artefakt der Mittelpunkt ist: **Welche Komposition**
  aus Komponenten und Akteuren ist der Mittelpunkt?

### 6. Wer handelt im System, ohne gebaut zu werden?

Die Akteure. Für jeden:
- **ID**
- **Rolle** — was darf und muss er tun?
- **Was er bedient** — Screens, Schnittstellen
- **Was das System von ihm erwartet** — und was passiert, wenn er es nicht tut

Ein Akteur ist eine Rolle, keine Person. Fallen zwei Rollen auf dieselbe
Person, schreib das als Annahme auf — sie kann sich ändern.

Akteure sind **nicht** extern: Sie stehen innerhalb der Systemgrenze.
Extern ist, was das System benutzt; ein Akteur ist, wer es benutzt.

## Was hier entsteht

- `C-` Komponenten
- `I-` Interfaces
- `A-` Akteure

Ordner: `projekt/struktur/`

Ein abgestimmter Eintrag trägt darunter die Zeile
`Abgestimmt: <wer>, <wann>` — ab dann ist seine ID verbraucht und wird bei
Aufgabe ausgemustert statt umnummeriert (`metamodell.md`).

Ausgemustert: —

## Querverweise

Dieses Template erzeugt **drei** Artefaktarten, deshalb je Art getrennt:

- **A- geht aus:** `bedient` → S-, I-
- **A- kommt an:** `betrifft` von RISK-, `entscheidet-ueber` von ADR-
- **C- geht aus:** `dient` → G-, `beachtet` → NG-, `verarbeitet` → D-
- **C- kommt an:** `gehoert-zu` von I-, `zeigt` von S-, `prueft` von T-,
  `benutzt-von` von X-, `gehalten-von` von D-, `betrifft` von RISK-,
  `entscheidet-ueber` von ADR-
- **I- geht aus:** `gehoert-zu` → C-
- **I- kommt an:** `bedient` von A-, `prueft` von T-, `betrifft` von RISK-,
  `entscheidet-ueber` von ADR-

## Was hier nicht entsteht

- Abläufe und Reihenfolgen (die kommen in `ui.md`)
- Datenmodell (das steht in `daten.md`)
- Tests (die kommen in `tests.md`)

## Zustand

- [ ] Welche Komponenten gibt es?
- [ ] Wie hängen die Komponenten zusammen?
- [ ] Welche Interfaces hat jede Komponente?
- [ ] Welche Komponenten sind extern?
- [ ] Was ist die Kernlogik in der Struktur?
- [ ] Wer handelt im System, ohne gebaut zu werden?

## Notizen

- Alle Komponenten werden später unit-getestet — zentrale und periphere.
  Testbarkeit ist kein Merkmal von Zentralität.
