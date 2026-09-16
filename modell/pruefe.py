#!/usr/bin/env python3
"""Prüft das Projektwissen.

Liegt in `modell/` und findet alles relativ zu sich selbst — egal, aus
welchem Verzeichnis es gestartet wird:

    modell/     die Templates — der Stand des Projekts
    projekt/    die Artefakte — daraus erzeugt, jederzeit neu erzeugbar

Zwei Hälften:

1. Der Graph — die Artefakte unter `projekt/*/` gegen die Regeln aus
   `modell/metamodell.md`. Nur Frontmatter. Harte Fehler, dazu zwei
   Warnungen: unbekanntes Feld und Komponente ohne Prüfung.
2. Der Fließtext — tote `[[Verweise]]`, in den Templates wie in den
   Artefakten, und je Template die Fragen gegen die Zustandspunkte. Nur
   Warnungen.

Ein Artefakt liegt genau eine Ebene tief, in seiner Projektion. Was direkt
in `projekt/` oder tiefer liegt, sieht dieses Skript nicht.
"""
import collections
import pathlib
import re
import sys

MODELL = pathlib.Path(__file__).resolve().parent
WURZEL = MODELL.parent
ARTEFAKTE = WURZEL / "projekt"

ERLAUBT = {                      # Feldname: (erlaubte Quell-Präfixe, erlaubte Ziel-Präfixe)
    "dient":       ({"C"},   {"G"}),
    "gehoert-zu":  ({"I"},   {"C"}),
    "zeigt":       ({"S"},   {"C"}),
    "beachtet":    ({"C", "S", "D"}, {"NG"}),
    "verarbeitet": ({"C"},   {"D"}),
    "gehalten-von": ({"D"},  {"C"}),
    "verweist-auf": ({"D"},  {"D"}),
    "bedient":     ({"A"},   {"S", "I"}),
    "prueft":      ({"T"},   {"C", "I", "S"}),
    "mockt":       ({"T"},   {"X"}),
    "laeuft-gegen": ({"T"},  {"X"}),
    "benutzt-von": ({"X"},   {"C"}),
    "betrifft":    ({"RISK"}, {"G", "NG", "C", "I", "X", "S", "A", "D"}),
    "entscheidet-ueber": ({"ADR"}, {"G", "NG", "C", "I", "X", "S", "A", "D"}),
}
PFLICHT = ("id", "titel", "projektion", "status")
STATUS = {"platzhalter", "entwurf", "abgestimmt"}
PRAEFIXE = {"G", "NG", "S", "C", "A", "D", "I", "T", "X", "RISK", "ADR"}
ID_FORM = re.compile(r"^[A-Z]+-\d+$")
# Welches Template in welchen Ordner erzeugt.
ORDNER = {"G": "ziel", "NG": "ziel", "S": "ui", "C": "struktur",
          "I": "struktur", "A": "struktur", "D": "daten", "T": "tests",
          "X": "extern", "RISK": "risiko", "ADR": "entscheidung"}
FELDER = {"id", "titel", "projektion", "status", "description",
          "abgestimmt-von", "abgestimmt-am"}   # alles andere ist ein Verweis
# Worauf nur `betrifft` oder `entscheidet-ueber` zeigen kann, kann nicht
# verwaisen — ein Akteur etwa wird von niemandem referenziert, außer
# zufällig von einem Risiko oder einer Entscheidung.
OHNE_EINGANG = PRAEFIXE - {p for feld, (_, nach) in ERLAUBT.items()
                           if feld not in ("betrifft", "entscheidet-ueber")
                           for p in nach}


def praefix(aid):
    return aid.rsplit("-", 1)[0]


def frontmatter(text):
    """Eine Zeile je Feld: `name: wert`. Keine Blöcke, keine Listen, keine
    Fortsetzungszeilen — mehr braucht ein Artefakt im Frontmatter nicht."""
    return dict(re.findall(r"^([a-zäöüA-Z-]+):[^\S\n]*(.*)$",
                           text.split("---")[1], re.M))


artefakte, fehler, warnungen, verweise = {}, [], [], []

# ── 0. Ausgemusterte IDs ───────────────────────────────────────────────────
# Eine Zeile je Template: `Ausgemustert: C-004 → C-012, I-002` — oder ein
# Gedankenstrich. Diese Nummern sind verbraucht und dürfen nicht wieder
# auftauchen; der Pfeil nennt den Nachfolger, wo es einen gibt.
ausgemustert, nachfolger = {}, {}
for f in sorted(MODELL.glob("*.md")):
    for zeile in re.findall(r"^Ausgemustert:(.*)$", f.read_text(encoding="utf-8"), re.M):
        for eintrag in [z.strip() for z in zeile.split(",") if z.strip() not in ("", "—")]:
            aid, _, nach = (x.strip() for x in eintrag.partition("→"))
            if not ID_FORM.match(aid):
                fehler.append(f"modell/{f.name}: '{aid}' in Ausgemustert ist keine ID")
                continue
            ausgemustert[aid] = f.name
            if not nach:
                continue
            if not ID_FORM.match(nach):
                fehler.append(f"modell/{f.name}: Nachfolger '{nach}' von {aid} ist keine ID")
            else:
                nachfolger[aid] = (nach, f.name)

# ── 1. Der Graph ───────────────────────────────────────────────────────────
for f in sorted(ARTEFAKTE.glob("*/*.md")):
    rel = f.relative_to(WURZEL)
    text = f.read_text(encoding="utf-8")
    if not text.startswith("---"):
        fehler.append(f"{rel}: kein Frontmatter — kein Artefakt")
        continue
    kopf = frontmatter(text)
    for p in PFLICHT:
        if p not in kopf:
            fehler.append(f"{rel}: Pflichtfeld '{p}' fehlt")
        elif not kopf[p].strip():
            fehler.append(f"{rel}: Pflichtfeld '{p}' ist leer")
    for feld in kopf:
        if feld not in FELDER and feld not in ERLAUBT:
            warnungen.append(f"{rel}: unbekanntes Feld '{feld}'")
    aid = kopf.get("id", "").strip()
    if not ID_FORM.match(aid):
        fehler.append(f"{rel}: id '{aid}' hat nicht die Form <PRÄFIX>-<NNN>")
        continue
    if praefix(aid) not in PRAEFIXE:
        fehler.append(f"{rel}: '{praefix(aid)}-' ist kein bekanntes Präfix")
        continue
    if aid in artefakte:
        fehler.append(f"{aid}: ID doppelt — schon vergeben in {artefakte[aid][0]}")
        continue
    if aid in ausgemustert:
        fehler.append(f"{aid}: ausgemustert in modell/{ausgemustert[aid]} — "
                      f"die Nummer wird nicht neu vergeben")
        continue
    artefakte[aid] = (rel, kopf)
    if f.stem != aid:
        fehler.append(f"{aid}: Dateiname '{f.name}' ist nicht die ID")
    soll = ORDNER.get(praefix(aid))
    if soll and f.parent.name != soll:
        fehler.append(f"{aid}: liegt in '{f.parent.name}/', gehört nach '{soll}/'")
    if kopf.get("projektion") != f.parent.name:
        fehler.append(f"{aid}: projektion '{kopf.get('projektion')}' ≠ Ordner '{f.parent.name}'")
    if kopf.get("status") not in STATUS:
        fehler.append(f"{aid}: Status '{kopf.get('status')}' ist keiner der drei")
    if kopf.get("status") == "abgestimmt" and not all(
            kopf.get(f, "").strip() for f in ("abgestimmt-von", "abgestimmt-am")):
        fehler.append(f"{aid}: abgestimmt ohne abgestimmt-von/-am")
    for feld, (von, nach) in ERLAUBT.items():
        if feld not in kopf:
            continue
        if praefix(aid) not in von:
            fehler.append(f"{aid}: trägt '{feld}', das nur {'/'.join(sorted(von))}- zusteht")
        for ziel in [z.strip() for z in kopf[feld].split(",") if z.strip()]:
            if not ID_FORM.match(ziel):
                fehler.append(f"{aid} {feld}: '{ziel}' ist keine ID")
                continue
            verweise.append((aid, feld, ziel))
            if praefix(ziel) not in nach:
                fehler.append(f"{aid} {feld}: {ziel} — {praefix(ziel)}- ist kein erlaubtes Ziel")

dangling = sorted({z for _, _, z in verweise if z not in artefakte})
ziel_von = collections.Counter(z for _, _, z in verweise)
verwaist = sorted(a for a in artefakte if ziel_von[a] == 0 and praefix(a) not in OHNE_EINGANG)
platz = sorted(a for a, (_, k) in artefakte.items() if k.get("status") == "platzhalter")

# `tests.md` sagt zu: alle Komponenten werden unit-getestet, nicht nur die
# zentralen. Hier wird es nachgehalten — als Warnung, denn im Entwurf ist
# eine Lücke normal. Platzhalter bleiben aus: Da steht noch nichts zu prüfen.
# Ein Test laeuft gegen die echte externe Komponente oder gegen einen Mock,
# nie beides zur selben — das waere zwei Antworten auf dieselbe Frage.
for a, (_, kopf) in sorted(artefakte.items()):
    beides = {z.strip() for z in kopf.get("mockt", "").split(",")} & \
             {z.strip() for z in kopf.get("laeuft-gegen", "").split(",")}
    for z in sorted(beides - {""}):
        fehler.append(f"{a}: {z} wird gemockt und echt zugleich")

geprueft = {z for _, feld, z in verweise if feld == "prueft"}
for a, (_, kopf) in sorted(artefakte.items()):
    if (praefix(a) == "C" and a not in geprueft
            and kopf.get("status") != "platzhalter"):
        warnungen.append(f"{a}: kein T- prüft diese Komponente")

# Der Nachfolger muss es geben. Ist er selbst ausgemustert, existiert er
# nicht — dann schlägt das hier an und zwingt die Kette auf den lebenden.
if artefakte:
    for aid, (nach, datei) in sorted(nachfolger.items()):
        if nach not in artefakte:
            fehler.append(f"modell/{datei}: Nachfolger {nach} von {aid} gibt es nicht")

# ── 2. Die Templates ───────────────────────────────────────────────────────
templates = sorted(MODELL.glob("*.md"))

# (a) Tote [[Verweise]] im Fließtext. Nur was der ID-Form folgt zählt, damit
#     `[[Verweise]]` im Regeltext von metamodell.md kein Treffer ist.
for f in sorted(list(ARTEFAKTE.glob("*/*.md")) + templates):
    for ziel in sorted(set(re.findall(r"\[\[([A-Z]+-\d+)\]\]", f.read_text(encoding="utf-8")))):
        if ziel not in artefakte:
            warnungen.append(f"{f.relative_to(WURZEL)}: [[{ziel}]] zeigt ins Leere")

# (b) Fragen gegen Zustandspunkte.
for f in templates:
    text = f.read_text(encoding="utf-8")
    fragen = len(re.findall(r"^### ", text, re.M))
    zustand = text.split("## Zustand")[-1].split("## Notizen")[0] if "## Zustand" in text else ""
    haken = len(re.findall(r"^- \[", zustand, re.M))
    if fragen and fragen != haken:
        warnungen.append(f"{f.relative_to(WURZEL)}: {fragen} Fragen, aber {haken} Zustandspunkte")

# ── Bericht ────────────────────────────────────────────────────────────────
if not artefakte:
    print(f"{ARTEFAKTE.relative_to(WURZEL)}/ ist leer — noch nichts erzeugt; "
          f"nur die Templates werden geprüft.\n")
print(f"{len(artefakte)} Artefakte, {len(verweise)} Verweise, "
      f"{len(templates)} Dateien in modell/\n")
for titel, liste, hart in (
        ("FEHLER", fehler, True),
        ("DANGLING (Ziel fehlt — Platzhalter nicht erzeugt)", dangling, True),
        ("VERWAIST (niemand verweist darauf)", verwaist, False),
        ("PLATZHALTER (To-do)", platz, False),
        ("WARNUNGEN", warnungen, False)):
    print(f"── {titel}: {len(liste)}{'  ← blockiert' if hart and liste else ''}")
    for e in liste:
        print(f"   {e}")
    print()

if fehler or dangling:
    print("Rückgabewert 1 — harte Fehler: Der Graph passt nicht zum Metamodell.")
    sys.exit(1)
print("Rückgabewert 0 — nichts Hartes gefunden. Das heißt nicht vollständig\n"
      "und nicht abgestimmt: Platzhalter, Verwaiste und Warnungen stehen oben.")
