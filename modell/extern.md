---
description: Externe Komponenten und ihre Integration. Laden bei Abhängigkeiten,
  bei der Frage "was benutzen wir von außen".
---

# Extern

**Was benutzen wir, das wir nicht selbst bauen?**

Externe Komponenten sind die Grenze zwischen „was wir bauen" und „was wir
benutzen". Sie sind nicht Teil des Projekts, aber sie sind Teil des Systems.

Nicht zu verwechseln mit den **Akteuren** aus `struktur.md`: Beide werden
nicht gebaut, aber extern ist, was das System *benutzt* — ein Akteur ist,
wer es benutzt.

## Fragen

### 1. Welche externen Komponenten gibt es?

Für jede:
- **ID**
- **Name**
- **Art** — Lib, Dienst, Gerät, Datenbank
- **Wofür benutzt** — welche Komponente aus `struktur.md` nutzt sie
- **Besitzer** — wir, ein Dritter

### 2. Was, wenn sie ausfällt?

Für jede:
- **Fällt aus?** — ja/nein. Auch eine Lib kann Fehler liefern, hängen
  oder abstürzen; „nein" braucht eine Begründung.
- **Fallback** — gibt es einen Ersatz?
- **Fehlerverhalten** — was tut das System?
- **Sichtbar für den Menschen?** — merkt der Mensch es?

### 3. Wie wird sie im Test behandelt?

Geprüft wird nie die externe Komponente selbst, sondern wie **unsere** mit
ihr umgeht. Dafür wird sie im Test entweder **ersetzt** oder **beteiligt**,
und die Art aus Frage 1 entscheidet, was passt:

| Art | Naheliegend |
|---|---|
| Lib | echt — sie läuft im selben Prozess, ein Mock wäre Mehrarbeit für weniger Aussage |
| Datenbank | echt, gegen eine Testinstanz |
| Dienst | Mock, wenn er Geld kostet, Limits hat oder nicht uns gehört |
| Gerät | Mock, wenn es beim Testen nicht dasteht |

Für jede:
- **Ersetzt, beteiligt oder beides?** — Mock (`mockt`), echt
  (`laeuft-gegen`), oder je nach Test das eine und das andere
- **Warum so?** — mit Blick auf die Art. Ein reines Rechenstück kann man
  einbeziehen; bei einem Gerät, das beim Testen nicht dasteht, bleibt nur
  der Mock. Das entscheidet, wer die Komponente vor sich hat — die Tabelle
  oben legt nahe, sie schreibt nicht vor.
- **Wenn ersetzt: wie sieht der Mock aus?** — was liefert er?
- **Welche Tests?** — abgeleitet: alle `T-` mit `mockt: X-…` beziehungsweise
  `laeuft-gegen: X-…`. Diese Listen werden nicht gepflegt, sondern
  abgefragt — sonst veralten sie, sobald ein Test dazukommt.

**Ersetzt** heißt: Der Prüfling bleibt allein, der Test ist ein Unit-Test,
geprüft wird die Nutzung gegen unsere Annahme. **Beteiligt** heißt: Der Test
ist ein Integrationstest und prüft nebenbei, ob die Annahme noch stimmt —
ein Mock kann nicht bemerken, wenn die externe Komponente sich ändert. Wer
ersetzt, nimmt das in Kauf, und das gehört in die Begründung.

### 4. Ist sie austauschbar?

Für jede:
- **Austauschbar?** — ja/nein
- **Wenn ja:** wodurch?
- **Wenn nein:** warum nicht?

## Was hier entsteht

- `X-` externe Komponenten

Ordner: `projekt/extern/`

Ein abgestimmter Eintrag trägt darunter die Zeile
`Abgestimmt: <wer>, <wann>` — ab dann ist seine ID verbraucht und wird bei
Aufgabe ausgemustert statt umnummeriert (`metamodell.md`).

Ausgemustert: —

## Querverweise

- **Geht aus:** `benutzt-von` → C-
- **Kommt an:** `mockt` von T-, `laeuft-gegen` von T-, `betrifft` von RISK-,
  `entscheidet-ueber` von ADR-

## Was hier nicht entsteht

- Die Nutzung im Detail (die steht in `struktur.md`)
- Tests (die stehen in `tests.md`)

## Zustand

- [ ] Welche externen Komponenten gibt es?
- [ ] Was, wenn sie ausfällt?
- [ ] Wie wird sie im Test behandelt?
- [ ] Ist sie austauschbar?

## Notizen
