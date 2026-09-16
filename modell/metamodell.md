---
description: Gemeinsame Begriffe und Regeln. Laden, wenn ein Begriff unklar ist
  oder wenn zwei Templates dasselbe anders benutzen.
---

# Metamodell

Die gemeinsamen Begriffe. Alle anderen Templates benutzen sie und definieren
sie nicht neu.

## Begriffe

**Projektion**
Eine Perspektive auf das System. Träger: ein Ordner unter `projekt/`.

**Artefakt**
Eine Aussage über das System. Träger: eine Datei im Ordner seiner Projektion,
also genau eine Ebene unter `projekt/`, benannt nach ihrer ID
(`projekt/struktur/C-003.md`). Erzeugt aus einem Template, nicht von Hand
geschrieben. Was direkt in `projekt/` oder tiefer liegt, ist kein Artefakt
und wird nicht geprüft.

**ID**
Stabile Kennung eines Artefakts. Form: `<PRÄFIX>-<NNN>`.
Nie wiederverwendet.

**Status**
Reifegrad eines Artefakts:
`platzhalter` | `entwurf` | `abgestimmt`.

Kein eigenes Feld im Template. Der Status fällt aus dem ab, was der Mensch
ohnehin tut — schreiben und unterschreiben:

| Status | Woraus |
|---|---|
| `platzhalter` | verwiesen, aber kein Eintrag im Template |
| `entwurf` | Eintrag da, keine Abstimmungszeile |
| `abgestimmt` | Eintrag da, `Abgestimmt:` darunter |

Das LLM schreibt den Wert in die Datei, aber es entscheidet ihn nicht — es
schreibt ihn ab. Kein Erzeugnis kann eine Abstimmung behaupten, die nicht
in `modell/` steht.

Wozu `abgestimmt` da ist, in zwei Sätzen. Der Grund ist die Unterschrift:
Jemand hat sich auf diesen Eintrag festgelegt, mit Namen und Datum. Die
Folge ist die Nummernfestschreibung — ab `abgestimmt` ist die ID verbraucht
und wird bei Aufgabe ausgemustert statt umnummeriert (siehe *Verweise*).
Diese Folge ist die einzige Regel im Modell, die den Wert liest; wer ihn
strichte, müsste ihr einen neuen Auslöser geben.

**Platzhalter**
Ein Artefakt mit den Pflichtfeldern und leerem Text. Wird erzeugt, nicht
geschrieben: Ein Verweis nennt eine ID, zu der es im Template keinen Eintrag
gibt, also entsteht die Datei leer. Er zählt nie als erledigt — eine
Zustands-Liste darf ihn nicht mitzählen. `status: platzhalter` ist damit die
To-do-Liste des Projekts: nicht geschätzt, sondern aus den Verweisen
abgefragt. Ein Platzhalter steht nie in `modell/`; ihn aufzulösen heißt, den
Eintrag zu schreiben.

**Akteur**
Wer im System handelt, ohne gebaut zu werden. Kein Code, also keine
Komponente. Innerhalb der Systemgrenze, also nicht extern.

Ein Akteur ist eine **Rolle**, keine Person: das, was jemand im System tun
darf und muss. Es kann mehrere geben, und zwei Akteure können dieselbe
Person sein — das ist dann eine Annahme, die man aufschreibt, keine
Selbstverständlichkeit. Wo zwei Rollen auseinanderfallen können, wird aus
Selbstdisziplin eine Übergabe, und die Risiken ändern ihre Gestalt.

**Kernlogik**
Die Rolle einer Komponente, eines Akteurs oder einer Komposition aus
beidem, um die sich die peripheren Komponenten drehen. Die peripheren sind da, um die Kernlogik zu ermöglichen.
Was Kernlogik ist, ergibt sich aus dem Verhältnis — nicht aus der Komponente
selbst. Kernlogik muss nicht neu sein; Standardkomponenten können Kernlogik
sein, wenn die anderen auf sie ausgerichtet sind.

**Prüfling**
Was ein `T-` prüft: eine Komponente, eine Schnittstelle, ein Screen — oder
ein Zusammenspiel aus mehreren. Nicht der Test und nicht der Fall, sondern
das Geprüfte.

**Visuelles Artefakt**
Ein Bild, das aus einem Text erzeugt wird, um ihn zu überprüfen.
Beispiele: Mockup, Screenshot, Diagramm. Abgeleitet, nicht Quelle.
Kann verlorengehen und neu erzeugt werden.

Kein Artefakt im obigen Sinn: keine ID, keine Pflichtfelder, nicht im
Graphen. Das Wort sagt nur, woher das Bild kommt.

**Kreislauf**
Ein wiederholtes Verfahren, das Text und Bild verbindet: Text → Bild →
Text → … bis der Mensch sagt: „So passt es." Der Text ist der Anker,
das Bild die Überprüfung. Der Kreislauf hat keine feste Länge.

## Wahrheit und Erzeugnis

Die Templates in `modell/` sind der Stand des Projekts. Alles unter
`projekt/` wird daraus erzeugt — von einem LLM, im Gespräch, nicht von einem
Skript. `pruefe.py` prüft das Ergebnis, es stellt es nicht her.

- Geschrieben wird **nur** in `modell/`. Eine **Aussage**, die nicht dort
  steht, gilt nicht.
- `projekt/` verhält sich zu `modell/` wie Objektdateien zum Quelltext:
  jederzeit neu erzeugbar, und beim nächsten Erzeugen überschrieben. Steht
  eine Aussage nur dort, gilt sie nicht — und ist beim nächsten Lauf weg.
- Ganz so ist es nicht: In `projekt/` darf etwas mehr stehen als das
  Erzeugte. Das verantwortet der Mensch. Das Skript meldet es, es verbietet
  es nicht.
- Beides steht im Repository, `modell/` wie `projekt/`. Die Historie trägt
  Git.

Der Text ist der Anker, das Erzeugte die Überprüfung — für Artefakte wie
für Mockups und Diagramme. Ein Prinzip, nicht zwei.

## Regeln

- Jedes Artefakt hat die Pflichtfelder `id`, `titel`, `projektion`, `status`.
- `projektion:` ist immer der Ordnername.
- Der Dateiname eines Artefakts ist seine ID.
- Jedes Template erzeugt in genau einen Ordner unter `projekt/`; er steht
  unter *Was hier entsteht*.
- Ein Artefakt ohne Pflichtfelder ist kein Artefakt.
- Ein abgestimmter Eintrag trägt im Template die Zeile
  `Abgestimmt: <wer>, <wann>`. Sie ist die einzige Angabe zum Status, die
  von Hand geschrieben wird; daraus werden `status: abgestimmt`,
  `abgestimmt-von:` und `abgestimmt-am:`.

## Verweisarten

Verweise stehen im Frontmatter. Sie verbinden Artefakte.

| Von | Nach | Feldname | Bedeutung |
|---|---|---|---|
| C- | G- | `dient` | welchem Ziel dient die Komponente |
| I- | C- | `gehoert-zu` | welche Komponente hat dieses Interface |
| S- | C- | `zeigt` | welche Komponente zeigt der Screen |
| C-, S-, D- | NG- | `beachtet` | welches Nicht-Ziel begrenzt dieses Artefakt |
| A- | S-, I- | `bedient` | was dieser Akteur bedient |
| C- | D- | `verarbeitet` | welche Entität benutzt die Komponente |
| D- | C- | `gehalten-von` | welche Komponente hält diese Entität |
| D- | D- | `verweist-auf` | welche andere Entität wird referenziert |
| T- | C-, I-, S- | `prueft` | was wird getestet |
| T- | X- | `mockt` | welche externe Komponente wird im Test ersetzt |
| T- | X- | `laeuft-gegen` | gegen welche echte externe Komponente läuft der Test |
| X- | C- | `benutzt-von` | welche Komponente nutzt die externe |
| RISK- | G-, NG-, C-, I-, X-, S-, A-, D- | `betrifft` | welches Artefakt ist betroffen |
| ADR- | G-, NG-, C-, I-, X-, S-, A-, D- | `entscheidet-ueber` | welches Artefakt ist so, weil es so entschieden wurde |

## Verweise

- Ein Verweis zeigt immer auf ein **existierendes** Artefakt.
  Dangling-Referenzen gibt es nicht.
- Fehlt das Ziel, entsteht es als **Platzhalter** — mit Pflichtfeldern,
  ohne Text, `status: platzhalter`.
- Wird ein Eintrag aufgegeben, verschwindet er aus dem Template, und seine
  ID kommt in die Zeile **Ausgemustert** desselben Templates. Steht dort ein
  Nachfolger (`C-004 → C-012`), wurde der Eintrag ersetzt; steht keiner, ist
  er ersatzlos weggefallen. Die Nummer ist in beiden Fällen verbraucht, und
  erzeugt wird zu ihr nichts mehr — kein Grabstein. Ein Verweis, der noch
  auf sie zeigt, ist ein Fehler und soll einer bleiben. Was der Eintrag
  einmal sagte, steht in Git.
- **Vor** `abgestimmt` darf umnummeriert werden, ohne auszumustern — auf
  einen Entwurf hat sich noch niemand berufen. Ab `abgestimmt` kostet jede
  aufgegebene ID eine Zeile. Sonst wäre der Entwurfsstand nach zwei
  Sitzungen ein Friedhof, und „ID nie wiederverwendet" bliebe eine
  Behauptung statt einer Prüfung.
- Ausnahme `entscheidung.md`: Dort wird nicht ausgemustert. Ein abgelöster
  ADR bleibt stehen — dass eine Entscheidung nicht mehr gilt, ist selbst eine
  Entscheidung und wird als neuer ADR geschrieben. Überall sonst liegt die
  Historie in Git; dort ist sie der Inhalt.
- Nur **Frontmatter**-Verweise erzeugen Platzhalter und bilden den Graphen.
  `[[Verweise]]` im Text sind Erläuterung; sie dürfen auf jede Art von
  Artefakt zeigen, ohne Rücksicht auf die Verweisarten, und legen nichts an.
  Was es nicht gibt, dürfen sie nicht nennen: Ein `[[…]]` ohne Artefakt ist
  eine Warnung — er legt keinen Platzhalter an, also bliebe er sonst für
  immer ein Verweis auf nichts.
- Ein Verweis ist **nackt** im Frontmatter, **erklärt** im Text.

## Präfixe

| Präfix | Bedeutung |
|---|---|
| G- | Ziel |
| NG- | Nicht-Ziel |
| S- | Screen |
| C- | Komponente |
| A- | Akteur |
| D- | Datenentität |
| I- | Schnittstelle |
| T- | Prüfungen zu einem Prüfling oder Zusammenspiel |
| X- | externe Komponente |
| RISK- | Risiko |
| ADR- | Entscheidung |

**Kein `F-` für Fehlerfälle.** Ein Fehlerfall ist kein eigenes Artefakt: Er
gehört in die Schnittstelle, die ihn behandelt (`I-`, Punkt *Bei Fehler*).
Was getragen statt behandelt wird, ist ein Risiko (`RISK-`).

**Kein `R-`, `NFR-`, `UC-`.** Dieses Modell hat keine Anforderungsschicht
zwischen Ziel und Entwurf. Was das System tun soll, steht als `G-`, als `S-`
und als `T-`; eine nicht-funktionale Eigenschaft als `G-` plus `RISK-` plus
`T-` (siehe `ziel.md`, Frage 4); ein Ablauf als Diagramm und als Kette von
`S-`. Eine vierte Erzählung desselben würde davon auseinanderlaufen.
