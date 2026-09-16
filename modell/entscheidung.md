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

#### ADR-001 Kotlin Multiplatform mit Compose Multiplatform, ein Modul

Die App ist ein einziges Kotlin-Multiplatform-Modul mit Compose
Multiplatform für Android und iOS — kein natives Projekt je Plattform,
keine getrennten Build-Komponenten.

#### ADR-002 Fastlane für die Store-Einreichung

Fastlane kapselt Signierung und Upload für Android- und
iOS-Einreichung, statt die Store-APIs direkt aus dem Workflow
anzusprechen.

#### ADR-003 Einreichung nur in die Testschienen

Die Pipeline reicht bis in die Testschienen der Stores — Google Play
„Interner Test", Apple TestFlight mit internen Testern —, nicht in einen
öffentlichen Store-Release (NG-004).

#### ADR-004 Einreichung per Knopfdruck statt bei jedem Push

Ein Push löst nur Build und Test aus. Die Einreichung bei Google Play
und/oder Apple TestFlight startet von Hand über „Run workflow" in
GitHub Actions, mit Wahl des Ziels (Google, Apple, beide).

### 2. Was wurde verworfen, und warum?

Die Alternativen, die ernsthaft im Raum standen. Ohne sie ist es kein ADR,
sondern eine Notiz.

Löst diese Entscheidung eine frühere ab, nenne sie hier im Fließtext, als
`[[…]]`-Verweis — nicht im Frontmatter. Sonst gälte jeder ADR, den noch
keiner abgelöst hat, als verwaist.

#### ADR-001

- **Getrennte native Projekte** (Swift/iOS + Kotlin/Android) — zeigt
  beide Plattform-Toolchains echter, aber doppelte Pflege für eine
  App, deren Inhalt bewusst trivial bleibt (NG-001).
- **Anderes Cross-Platform-Framework** (z. B. Flutter, React Native) —
  liefert ebenfalls eine gemeinsame Codebasis, aber Kotlin Multiplatform
  bleibt näher am nativen Android-Code.
- **Getrennte Android-/iOS-Build-Komponenten trotz gemeinsamem Code** —
  hätte zwei Komponenten für etwas erzeugt, dessen Quelle ohnehin
  identisch ist.

#### ADR-002

- **Google Play Developer API und App Store Connect API direkt** —
  spart die Fastlane-Abhängigkeit, bedeutet aber deutlich mehr
  Pipeline-Code für Signierung, Upload und Metadaten je Plattform.

#### ADR-003

- **Öffentlicher Store-Release** (Google Play Produktion, Apple App
  Store) — war nie Ziel des Projekts. Braucht die Store-Prüfung (bei
  Apple droht Ablehnung einer trivialen App nach Guideline 4.2) und bei
  Google für neue Konten erst einen geschlossenen Test; der erste Lauf
  gegen Produktion (2026-09-16) endete mit „Google Api Error: Invalid
  request - Precondition check failed".

#### ADR-004

- **Einreichung bei jedem Push** (ursprünglich G-002) — solange Konten
  und Secrets fehlen, schlägt jeder Push fehl, und ein fertig
  eingerichteter Zustand würde jeden Commit einreichen (RISK-004).
- **Nur Google per Knopfdruck, Apple weiter bei jedem Push** — jeder
  Push bliebe rot, bis die Apple-Konten eingerichtet sind.

### 3. Woran hing es?

Das Kriterium, das den Ausschlag gab. Daran erkennt man später, ob die
Entscheidung noch trägt: Gilt das Kriterium nicht mehr, gehört sie auf den
Tisch.

#### ADR-001

Die App ist nur Träger, nicht das Ziel (NG-001) — der Aufwand auf der
App-Seite soll minimal bleiben, damit die Pipeline (C-001) im Zentrum
steht.

#### ADR-002

Fastlane ist Standard-Tooling für genau diesen Fall — beide Stores aus
einer CI-Pipeline heraus. Das Projekt soll die Demonstration zeigen,
nicht eine eigene Store-API-Integration bauen.

#### ADR-003

Gezeigt werden soll die Kette von der Source-Änderung bis auf das eigene
Gerät (G-003), nicht die Veröffentlichung für fremde Nutzer. Die
Testschienen kommen ohne Store-Prüfung aus.

#### ADR-004

Die Store-Konten und Secrets werden Schritt für Schritt eingerichtet;
bis dahin soll ein Push nicht an fehlenden Zugangsdaten scheitern, und
eingereicht wird nur, wenn der Mensch es auslöst. Sind alle Konten
eingerichtet, gehört die Entscheidung wieder auf den Tisch.

### 4. Was folgt daraus?

Welche Artefakte sind so, wie sie sind, wegen dieser Entscheidung?

#### ADR-001

C-002 als ein Modul, I-004 als eine Schnittstelle, T-001/T-002 als je
ein Unit-Test statt mehrerer, RISK-005 (macOS-Runner nötig für das
iOS-Target).

#### ADR-002

X-004 als externe Komponente, I-002 und I-003 laufen über sie, T-006
und T-007 lassen X-004 echt mitlaufen (`laeuft-gegen`) statt sie zu
mocken.

#### ADR-003

NG-004; G-002 als Einreichung in die Testschienen; I-002 reicht in den
Track „internal" ein, I-003 lädt nach TestFlight hoch statt zur
App-Store-Prüfung.

#### ADR-004

G-002 wird nicht mehr bei jedem Push erfüllt, sondern auf Knopfdruck;
I-002 und I-003 laufen nur bei manuellem Start. RISK-004 wird damit
vermieden statt beobachtet.

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

- [x] Was wurde entschieden?
- [x] Was wurde verworfen, und warum?
- [x] Woran hing es?
- [x] Was folgt daraus?

## Notizen
