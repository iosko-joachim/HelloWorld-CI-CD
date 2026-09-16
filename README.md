# projekt_template

Vorlagen für Projektwissen: acht Templates, die man im Gespräch mit einem
LLM ausfüllt, ein Metamodell, das die gemeinsamen Begriffe festlegt, und ein
Prüfskript, das den entstehenden Artefakt-Graphen gegen dieses Metamodell
hält.

## Benutzen

    git clone ssh://git@forgejo.codeclair.cc:2223/eu-schmiede/projekt_template mein-projekt
    cd mein-projekt
    rm -rf .git && git init

Dann `modell/_index.md` in den Chat ziehen und sagen, worüber du reden
willst. Das LLM sieht in der Tabelle, welches Template passt.

## Aufbau

    mein-projekt/
    ├── modell/     die Templates — hier wird ausgefüllt
    │   ├── _index.md       die Landkarte: welches Template wofür
    │   ├── metamodell.md   Begriffe, Regeln, Präfixe, Verweisarten
    │   ├── ziel.md         was soll das Projekt machen
    │   ├── struktur.md     Komponenten, Schnittstellen, Akteure
    │   ├── ui.md           Screens und ihre Reihenfolge
    │   ├── daten.md        was wird festgehalten, und wie lange
    │   ├── tests.md        Unit-, Integrations- und Screen-Tests
    │   ├── extern.md       was wir benutzen, ohne es zu bauen
    │   ├── risiko.md       was schiefgehen kann, und was wir damit tun
    │   ├── entscheidung.md was gewählt wurde, und wogegen
    │   └── pruefe.py       die Konsistenzprüfung
    └── projekt/    die Artefakte — erzeugt, je Projektion ein Ordner

`modell/` bekommt keine neuen Dateien und keine neuen Ordner. Ausgefüllt
wird an Ort und Stelle — und nur dort. `projekt/` wird daraus erzeugt
und darf jederzeit neu erzeugt werden — steht aber mit im Repository, wie
die Objektdateien neben dem Quelltext.

## Prüfen

    python3 modell/pruefe.py

Findet seine Pfade aus dem eigenen Ort und läuft aus jedem Verzeichnis.

Rückgabewert 1 gibt es nur bei **harten Fehlern**: Der Graph passt nicht zum
Metamodell. Verwaiste Artefakte, offene Platzhalter und Warnungen stehen im
Bericht, blockieren aber nicht — sonst schlüge ein Commit-Hook bei jedem
normalen Arbeitsstand zu. Rückgabewert 0 heißt darum „nichts Hartes
gefunden", nicht „vollständig" und nicht „abgestimmt".

Geprüft wird: Pflichtfelder und ob sie gefüllt sind, ID-Form und bekannte
Präfixe, doppelte und ausgemusterte IDs, Nachfolger ausgemusterter IDs,
Dateiname gegen ID, Präfix gegen den Ordner, in den sein Template erzeugt,
`projektion` gegen den Ordnernamen, gültige Statuswerte, `abgestimmt` ohne
`abgestimmt-von`/`-am`, erlaubte Quell- und Zielpräfixe je Verweisart,
Verweise ins Leere, verwaiste Artefakte, Komponenten ohne Prüfung, externe
Komponenten, die zugleich gemockt und echt geprüft werden, offene
Platzhalter, unbekannte Frontmatter-Felder, tote `[[Verweise]]` im
Fließtext, und ob jedes Template so viele Zustandspunkte hat wie Fragen.

## Der Gedanke dahinter

Der Text ist der Anker, das Bild die Überprüfung. Artefakte tragen stabile
IDs und verweisen einander im Frontmatter — daraus wird ein Graph, den man
prüfen kann. Was im Fließtext steht, erklärt; was im Frontmatter steht,
gilt.

Geschrieben wird in `modell/`, erzeugt wird nach `projekt/`. Eine Richtung,
nie beide — sonst stehen nach drei Monaten zwei Stände da und keiner weiß,
welcher der richtige ist. Die Artefakte sind damit dasselbe wie die
Mockups: abgeleitet, überprüfend, jederzeit ersetzbar.

Ab dem Moment, in dem sich jemand auf einen Eintrag festlegt, bekommt seine
Nummer kein zweiter mehr. Die Festlegung ist die Zeile `Abgestimmt: <wer>,
<wann>` unter dem Eintrag — die einzige Angabe zum Status, die von Hand
geschrieben wird; `status`, `abgestimmt-von` und `abgestimmt-am` fallen
daraus ab. Vorher, im Entwurf, darf umnummeriert werden: Auf einen Entwurf
hat sich noch niemand berufen, und sonst wäre der Stand nach zwei Sitzungen
ein Friedhof.

Aufgegebene IDs stehen danach in der Zeile *Ausgemustert* ihres Templates;
das Prüfskript hält sie frei. Wurde ein Eintrag ersetzt, steht der Nachfolger
daneben (`C-004 → C-012`), und das Skript prüft, dass es ihn gibt. Einzige
Ausnahme ist `entscheidung.md`: Dort wird nicht ausgemustert, weil ein
abgelöster `ADR-` stehen bleibt — dass eine Entscheidung nicht mehr gilt,
ist selbst eine Entscheidung.

Warum das Modell so aussieht — und was dabei verworfen wurde — steht in
[`WARUM.md`](WARUM.md). Das sind Entscheidungen über die Vorlage selbst;
Entscheidungen über ein Projekt gehören als `ADR-` nach
`modell/entscheidung.md`.
