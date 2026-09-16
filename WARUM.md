# Warum das Modell so aussieht

Entscheidungen über **das Modell selbst** — nicht über ein Projekt, das damit
beschrieben wird. Projektentscheidungen gehören als `ADR-` nach
`modell/entscheidung.md`; diese hier haben dort keinen Platz, weil sie die
Vorlage betreffen und nicht das Vorhaben.

Aufgeschrieben in der Form, die `modell/entscheidung.md` verlangt: was
entschieden wurde, was verworfen, woran es hing, was folgt. Der vollständige
Verlauf steht in den Commit-Nachrichten; hier stehen die Gründe kurz, damit
man sie findet, ohne `git log` zu lesen.

Wo eine Entscheidung erst durch Widerspruch zustande kam, steht das dabei. Für
einen späteren Leser ist das der Unterschied zwischen einem Schluss, der
geprüft wurde, und einem, der nie auf Gegenwehr getroffen ist.

Ein Eintrag, von dem **nichts** mehr gilt, wird entfernt statt durchgestrichen.
Seine Nummer bleibt verbraucht: Die Liste bekommt eine Lücke und nummeriert
nicht nach — wie die IDs im Modell selbst. Ein Eintrag dagegen, den ein
späterer nur in Teilen korrigiert, bleibt stehen; was von ihm gilt, steht in
ihm, und was nicht mehr gilt, steht im späteren unter *Hebt auf*. So trifft
man beim Lesen keine Entscheidung mehr an, die es nicht mehr gibt, und keine
verliert ihre Begründung, weil eine spätere sie an einer Stelle berührt hat.

Stand: 16. September 2026. Restlos überholt ist bisher kein Eintrag; die
Nummern 1 bis 15 sind daher vollständig. Teilweise korrigiert sind 1 und 4
(durch 11), 6 (durch 8) und 8 (durch 13).

---

## 1. `modell/` ist die Wahrheit, `projekt/` wird erzeugt

**Entschieden:** Geschrieben wird nur in den Templates. Alles unter `projekt/`
wird daraus erzeugt, steht nicht im Repository und darf weggeworfen werden.

**Verworfen:** Beides pflegen mit festgelegter Vorfahrt. Und: das Ausgefüllte
gar nicht im Template lassen, sondern nur als Artefakt.

**Woran es hing:** Ob zwei Prosatexte dasselbe sagen, kann kein Werkzeug
feststellen. Eine Regel, die niemand durchsetzen kann, verrottet — und das
widerspricht der Prämisse des Repos, dass geprüft wird, was gilt.

Der Vorschlag kam von außen: Empfohlen hatte ich das Aufteilen, das jetzt unter
„Verworfen" steht, und gegen die Erzeugung argumentiert — zwei meiner Einwände
ließen sich ausräumen, denn der Generator ist das LLM, und `rm -rf .git` regelt
die Wiederverwendbarkeit ohnehin.

**Folgt daraus:** `projekt/` in der `.gitignore`. Der Generator ist das LLM.
Vier Verweisfelder mussten nachgetragen werden, ohne die er den Graphen nicht
bauen kann: `dient`, `verarbeitet`, `zeigt`, `beachtet`.

## 2. Historie in Git, dazu eine `Ausgemustert:`-Zeile

**Entschieden:** Ein aufgegebener Eintrag verschwindet aus dem Template, seine
ID kommt in die Zeile `Ausgemustert:`, mit Nachfolger hinter einem Pfeil.

**Verworfen:** Grabsteine — abgestimmte Artefakte, die nie gelöscht werden.

**Woran es hing:** Die Grabsteine hatten zwei Zwecke. Der erste, dass jeder
Verweis eine Datei trifft, fällt weg, sobald der Generator Platzhalter anlegt.
Der zweite ist Historie, und dafür ist Git da. Übrig blieb nur, IDs freizuhalten
— dafür genügt eine Zeile.

**Folgt daraus:** „ID nie wiederverwendet" ist zum ersten Mal eine Prüfung statt
einer Behauptung. Umnummerieren vor `abgestimmt` widerspricht dem nicht mehr.

## 3. Status wird abgeleitet, nicht gesetzt

**Entschieden:** Drei Werte, alle abgeleitet. `platzhalter` = verwiesen ohne
Eintrag, `entwurf` = Eintrag, `abgestimmt` = Eintrag mit Zeile `Abgestimmt:`.

**Verworfen:** Ein Feld `Status:` je Eintrag. Und: die Abstimmung aus dem
Git-Log ableiten.

**Woran es hing:** „Das LLM darf nur `platzhalter` setzen" war unhaltbar,
sobald das LLM jede Datei schreibt. Die Frage ist nicht, wer tippt, sondern
woher der Wert kommt. Ein Feld, das meistens auf `entwurf` steht, ist Rauschen
und wird vergessen; eine Abstimmung ist ein Akt mit einem Namen daran, kein
„wer hat zuletzt angefasst".

**Folgt daraus:** Nichts, was man pflegen und vergessen kann.

## 4. `überholt` und `ersetzt-durch` fallen weg

**Entschieden:** Beide gestrichen. Zu einer ausgemusterten ID wird nichts
erzeugt.

**Verworfen:** Den Grabstein aus der `Ausgemustert:`-Zeile erzeugen.

**Woran es hing:** Das hätte die Prüfung geschwächt. Sobald die Datei wieder
existiert, ist ein Verweis auf sie kein toter Verweis mehr — der Fehler
verschwände aus dem Bericht, obwohl er einer ist.

**Folgt daraus:** Wer von außen eine ausgemusterte ID sucht, findet eine Zeile
im Template statt einer Datei. Zumutbar, seit `projekt/` ohnehin nicht im
Repository steht.

## 5. `R-`, `NFR-`, `UC-` gestrichen, `ADR-` bekommt ein Template

**Entschieden:** Drei Präfixe raus, `modell/entscheidung.md` dazu — die erste
neue Datei in `modell/` überhaupt.

**Verworfen:** Alle vier behalten und ihnen ein Zuhause bauen. Und: `ADR-`
ebenfalls streichen.

**Woran es hing:** Dieses Modell hat keine Anforderungsschicht zwischen Ziel
und Entwurf; eine vierte Erzählung desselben liefe auseinander.

Bei `ADR-` lag ich zuerst falsch und wollte streichen — das Argument war, ein
ADR hänge in keinem Graphen und sei damit Prosa mit Nummer. Umgestimmt hat
nicht ein besseres Argument, sondern der Blick in einen ausgefüllten Stand:
Dort waren bereits zwei ADRs in Gebrauch, und sie trugen die verworfene
Alternative, die sonst nirgends steht. Entschieden wurde also auf Evidenz aus
der Nutzung. Mein Einwand ließ sich nebenbei ausräumen — mit `entscheidet-ueber`
hängt ein ADR sehr wohl im Graphen.

**Folgt daraus:** Eine nicht-funktionale Eigenschaft wird als `G-` formuliert,
ihr Ausbleiben als `RISK-`, ihre Prüfung als `T-` — feste Rollen, damit dieselbe
Auflage nicht je nach Gesprächsverlauf woanders landet. `entscheidung.md` ist
das einzige Template ohne Ausmusterung: Dort ist Historie der Inhalt.

## 6. `T-` ist eine Gruppe, die Ebene steht im Verweis

**Entschieden:** Ein `T-` sind die Prüfungen zu einem Prüfling, nicht ein Fall.
Unit heißt genau ein `prueft`-Ziel und kein `laeuft-gegen`.

**Verworfen:** `T-` als Einzelfall mit definierten Nummernkreisen. Und
Unter-IDs wie `T-003.1`.

**Woran es hing:** Seit die IDs von Hand in `modell/` stehen, wären Hunderte
Einzelnummern samt Kreisen genau die Buchführung, die überall sonst abgeschafft
wurde. Dass die Defaults keine IDs haben, ergibt nur mit Gruppen einen Sinn.

**Folgt daraus:** Die Nummernkreise entfallen ersatzlos. Dass „unsere Komponente
mit der echten Lib" danach ein Integrationstest ist, steht als bewusste
Unschärfe im Text — die Ebene ist rein beschreibend.

## 7. Screen-Tests erweitern statt streichen

**Entschieden:** Frage 1 fragt nach jedem Prüfling statt nach jeder Komponente,
mit `C-`, `I-`, `S-` als Zielen.

**Verworfen:** Screens gar nicht maschinell prüfen und stattdessen vier Stellen
zurücknehmen, die von Screen-Tests ausgehen.

**Woran es hing:** Das Mockup prüft das Aussehen, ein Test prüft das Ergebnis —
sie prüfen Verschiedenes, also ist es keine Doppelung. Dasselbe Loch traf
nebenbei Unit-Tests von Schnittstellen.

**Folgt daraus:** Kein dritter Fragenblock nötig; seit die Ebene abgeleitet
wird, ist ein Screen-Test einfach ein `T-` mit einem `S-` als Ziel.

## 8. Externe im Test: ersetzt oder beteiligt

**Entschieden:** Eine externe Komponente wird im Test ersetzt (`mockt`) oder
beteiligt (`laeuft-gegen`). Die Art aus `extern.md` Frage 1 legt nahe, was
passt; der gewählte Weg wird begründet.

**Verworfen:** Nur mocken. Und: eine fehlende Echtprüfung generell als Lücke
melden.

**Woran es hing:** Ein Mock ist unsere Annahme über die andere Seite — jeder
Test dagegen prüft unseren Code gegen unsere eigene Vorstellung.

Zwei Korrekturen kamen von außen, nicht aus der Analyse. Ich hatte den Mock
als Behelf und die Echtprüfung als das Bessere dargestellt und wollte ihr
Fehlen generell als Lücke melden; der Einwand war, dass beide dasselbe prüfen —
das Zusammenspiel — und dass die Art der externen Komponente entscheidet,
welcher Weg passt. Bei einer Lib wäre die Warnung richtig, bei einem
kostenpflichtigen Dienst wäre sie Rauschen. Und dass ein Echtlauf kein
Unit-Test sein kann, habe ich nicht selbst bemerkt.

**Folgt daraus:** Die Ebenenregel aus 6 war seither unvollständig und musste
ergänzt werden — ein Echtlauf prüft das Zusammenspiel und ist Integration, auch
bei nur einem Ziel.

## 9. Löschverhalten wird gefragt, nicht abgeleitet

**Entschieden:** Je Verweis eine von drei Antworten — verhindern, mitlöschen,
loslassen.

**Verworfen:** Die Behauptung, die Richtung des Verweises entscheide es. Und:
es als Technik ganz zu streichen.

**Woran es hing:** Bei derselben Richtung sind alle drei möglich. Und anders
als bei Status, Ebene und Mock-Liste gibt es hier nichts, woraus es folgte: Ob
eine Bestellung ohne Kunden sinnlos oder bloß unvollständig ist, ist eine
Aussage über die Sache selbst.

**Folgt daraus:** „Verschwinden" deckt Löschen und Ablaufen ab. Ist das Ziel
flüchtig, fällt „verhindern" weg — ein Ereignis lässt sich nicht mit einem Veto
belegen.

## 10. Frontmatter bleibt bei Identität, Abstimmung, Verweisen

**Entschieden:** Keine Einstufungen im Frontmatter. Neun Kandidaten geprüft,
keiner aufgenommen.

**Verworfen:** die vier Felder `lebensdauer:`, `umgang:`, `wahrscheinlich:`
und `wirkung:` aufzunehmen, aus denen drei Prüfungen gefolgt wären.

**Woran es hing:** Nicht an einer Analyse — ich hatte ein Kriterium
vorgeschlagen und wollte weitermachen. Gestoppt hat der Einwand, dass es
langsam kleinteilig wird, und der trifft zu: Es ist kein Widerspruch, sondern
Ausbau. Die übrigen neun waren ein Widerspruch oder eine Lücke im Bestehenden;
diese hier hätte nur Prüfungen hinzugefügt, die niemand vermisst hat. Solange
kein Projekt sie braucht, sind vier Felder plus Vokabular plus Generatorarbeit
zu viel.

Dass ich die Frage überhaupt aufgemacht habe, war ein schlechter Grund: Ich
hatte sie dreimal abgelehnt und das Wiederkehren für ein Argument gehalten.
Dreimal abgelehnt heißt eher, dass der Zustand jedes Mal in Ordnung war.

**Folgt daraus:** Wenn ein Projekt den Risikobericht will, ist das der Moment
für `umgang:` — zusammen mit der Prüfung im selben Zug.

## 11. `projekt/` steht mit im Repository

**Entschieden:** `modell/` und `projekt/` liegen beide im Repository.
`projekt/` bleibt Erzeugnis — jederzeit neu erzeugbar, beim nächsten Lauf
überschrieben, und eine Aussage, die nur dort steht, gilt nicht. Es darf
etwas mehr enthalten als das Erzeugte; das verantwortet der Mensch, und das
Skript meldet es, statt es zu verbieten.

**Hebt auf:** aus 1 den Halbsatz „steht nicht im Repository und darf
weggeworfen werden" samt „Folgt daraus: `projekt/` in der `.gitignore`". Der
Kern von 1 bleibt: Vorfahrt hat `modell/`, weil kein Werkzeug zwei
Prosatexte vergleichen kann — daran ändert Einchecken nichts. Aus 4 fällt
die Begründung des letzten Satzes weg; die Entscheidung selbst trägt sich
weiter aus dem ersten Argument, dass ein erzeugter Grabstein die Prüfung
schwächt.

**Verworfen:** Die `.gitignore` lassen und vor jedem Commit erzeugen — dann
müsste ein LLM gelaufen sein, bevor man committen darf. Und: den Anspruch
senken, `pruefe.py` nur noch als Werkzeug für die Sitzung führen und den
Commit-Hook aus der README streichen.

**Woran es hing:** Was im Repository lag, war ungeprüft; was geprüft wurde,
lag nicht im Repository. `pruefe.py` liest den Graphen allein aus `projekt/`,
und nach einem Klon gibt es den Ordner nicht — null Artefakte,
Rückgabewert 0. Entschieden hat es ein Vergleich: `modell/` ist Quelltext,
`projekt/` sind Objektdateien — nur nicht ganz, denn dort darf etwas mehr
stehen, und diese Restverantwortung soll beim Menschen bleiben, statt
wegdefiniert zu werden. Der Vorschlag kam von außen; empfohlen hatte ich das
Absenken des Anspruchs, das jetzt unter „Verworfen" steht.

**Folgt daraus:** `projekt/` raus aus der `.gitignore`, vier Textstellen
nachgezogen (`README.md`, `modell/_index.md`, `modell/metamodell.md`, der
Docstring von `pruefe.py`). Der Satz aus 1 musste dabei geschärft werden:
aus „Was nur dort steht, gilt nicht" wurde „Eine **Aussage**, die nur dort
steht" — sonst träfe die Regel den Platzhalter, der per Definition nur in
`projekt/` steht und zugleich die To-do-Liste des Projekts ist. Nachgetragen:
Der Ordner lag danach im Repository noch gar nicht, weil Git keine leeren
Ordner trägt — jetzt hält ihn `projekt/.gitkeep`. Dass schon erzeugt wurde,
erkennt `pruefe.py` seither am Inhalt und nicht am Ordner; sonst hätte der
leere Ordner die Nachfolgerprüfung scharf gemacht, bevor es etwas zu prüfen
gibt.

## 12. Die Redundanz zwischen `metamodell.md` und `pruefe.py` bleibt

**Entschieden:** Sie bleibt, ungefixt und hier benannt. Sechs Bestände stehen
doppelt: die Verweisarten (Tabelle gegen `ERLAUBT`), die Präfixe (Tabelle
gegen `PRAEFIXE`), Präfix→Ordner (sogar dreifach — Regel, `Ordner:`-Zeile je
Template, `ORDNER`), die Pflichtfelder, die Statuswerte und die ID-Form. Wer
eine der Tabellen erweitert und das Skript vergisst, bekommt keinen Fehler,
sondern stille Nachsicht. Das ist bekannt und hingenommen.

**Verworfen:** Das Skript die Tabellen aus `metamodell.md` **auslesen**
lassen — dann ist ein kaputter Parser eine leere Regelmenge, also genau die
stille Nachsicht, die abgestellt werden sollte. Und: die Tabellen auslesen und
mit den Konstanten **vergleichen**, Abweichung als harter Fehler — das scheitert
nicht still, kostet aber einen Parser für zwei Tabellen und bindet
`metamodell.md` an eine Spaltenordnung, die sie nicht ändern darf. Die
übrigen vier Bestände stehen ohnehin als Prosa da und wären von beiden Wegen
nicht erreicht worden. Beide Vorschläge kamen von mir, in zwei Anläufen; abgelehnt hat sie der
Mensch.

**Woran es hing:** Wo keine Änderungen sind, können keine Fehler entstehen.
Das Modell ist fertig, die Tabellen ändern sich nicht mehr, und ein Wächter,
der eine Bewegung bewacht, die niemand macht, ist Aufwand ohne Gegenwert.
Kommen später doch Änderungen, sind sie die Sache dessen, der sie macht —
diese Notiz sagt ihm, wo er nachziehen muss. Das Thema wurde vorher zweimal
aufgeschoben; die dritte Vorlage hat es nicht besser gemacht, sondern nur
zeigen können, dass es dabei bleiben soll.

**Folgt daraus:** Nichts am Code. Ein LLM, das hier anfängt, darf die
Redundanz jederzeit nachprüfen und melden — beheben soll es sie nicht.

Auch die Sätze in `README.md` und `modell/_index.md`, die sagen, `pruefe.py`
prüfe gegen `metamodell.md`, bleiben stehen. Sie beschreiben die Sache
richtig: Die Regeln des Metamodells sind in die Python-Datei hinübergewandert
und gelten dort weiter. Falsch ist nur der Mechanismus, den man hineinliest —
das Skript liest die Datei nicht. Wer nachprüft, findet hier den Grund und
nicht noch einen Befund.

## 13. Ersetzt oder beteiligt gehört zum Test, nicht zur externen Komponente

**Entschieden:** Der Weg — `mockt` oder `laeuft-gegen` — ist eine Eigenschaft
des Tests. Dieselbe `X-` darf in einem `T-` ersetzt und in einem anderen
beteiligt sein; nur innerhalb eines `T-` nie beides.

**Hebt auf:** aus 8 den Satz „Eine externe Komponente wird im Test ersetzt
oder beteiligt", soweit er einen Weg je Komponente meint. Der Rest von 8
bleibt und trägt weiter: Ein Mock ist unsere Annahme über die andere Seite,
die Art aus `extern.md` Frage 1 legt nahe, was passt, und der gewählte Weg
wird begründet.

**Verworfen:** Die Ein-Weg-Regel ernst nehmen und im Skript durchsetzen — zu
einer `X-` nie beide Verweisarten, über alle `T-` hinweg. Das hätte eine
verbreitete und sinnvolle Testpraxis verboten, um einen Satz zu retten. Und:
nichts ändern, weil die Templates leer sind und der Fall nie eintritt.

**Woran es hing:** Die Vorlage kann es nicht wissen. Ein reines Rechenstück
lässt sich einbeziehen; bei einem Gerät, das beim Testen nicht dasteht,
bleibt nur der Mock — und dazwischen liegt alles andere. Das entscheidet,
wer die Komponente vor sich hat, nicht die Vorlage, die sie nie sieht.

Aufgefallen ist es als Widerspruch innerhalb einer einzigen Frage:
`extern.md` Frage 3 verlangte einen Weg je Komponente und erwartete drei
Zeilen später mit „beziehungsweise" beide Listen zur selben `X-`; `pruefe.py`
verbietet beides nur innerhalb eines `T-`. Die Empfehlung war meine, der
tragende Grund nicht: Ich hatte mit der Tabelle der Arten argumentiert, der
Einwand von außen war, dass es an der Komponente hängt und derjenige
entscheidet, der sie zusammenstellt — das ist der allgemeinere Satz.

**Folgt daraus:** `extern.md` Frage 3 fragt „Ersetzt, beteiligt oder beides?",
`tests.md` sagt „innerhalb eines `T-` nie beides zur selben externen". Die
Ebenenregel aus 6 und 8 bleibt unberührt: Ein `laeuft-gegen` macht den Test
zur Integration, gleichgültig wie viele andere Tests dieselbe `X-` mocken.

## 14. Nicht-Ziele auf Datenebene werden `NG-` und entstehen in `ziel.md`

**Entschieden:** Was `daten.md` Frage 5 zutage fördert — was bewusst nicht
gespeichert wird —, ist ein Nicht-Ziel wie jedes andere. Gefragt wird es
dort, geschrieben wird es in `ziel.md` Frage 3, und das `NG-` entsteht im
Ordner `projekt/ziel/`.

**Verworfen:** Es als Fließtext in `daten.md` stehen lassen. Und: `daten.md`
ein zweites Präfix geben.

**Woran es hing:** Die Frage nannte ihre Antworten selbst „Nicht-Ziele",
erzeugte aber nur `D-`. Als Fließtext hätte die Antwort keine ID, und die
Entität, die sie begrenzt, könnte mit `beachtet` nicht auf sie zeigen —
obwohl Frage 1 derselben Datei genau das anbietet. Ein zweites Präfix wäre
an der Regel gescheitert, dass jedes Template in genau einen Ordner erzeugt.

**Folgt daraus:** Das erste Mal, dass eine Frage bewusst woanders hin
schreibt, als sie steht. Beide Enden sagen es jetzt: `daten.md` verweist auf
`ziel.md`, `ziel.md` nimmt die Datenebene ausdrücklich auf.

## 15. Der Status `abgestimmt` bleibt

**Entschieden:** Er bleibt, und `metamodell.md` sagt jetzt, wozu. Der Grund
ist die Unterschrift: Jemand hat sich mit Namen und Datum auf den Eintrag
festgelegt. Die Folge ist die Nummernfestschreibung — ab `abgestimmt` ist
die ID verbraucht. Diese Folge ist die einzige Regel im Modell, die den Wert
liest.

**Verworfen:** Ihn streichen, weil ihn sonst niemand liest — dann stünde die
Ausmusterungsregel ohne Auslöser da, und die beiden naheliegenden Ersatz-
auslöser sind in 2. und 3. schon verworfen. Und: ihn samt Ausmusterung
streichen, also IDs ab dem ersten Hinschreiben verbrauchen — das ist der
Friedhof, den 2. nicht zahlen wollte, nur als Zeile statt als Datei.

**Woran es hing:** Die Frage kam von außen und war berechtigt: In den
Templates stand die Zeile `Abgestimmt:` nirgends, obwohl `metamodell.md` sie
an zwei Stellen verlangt und `pruefe.py` sie hart prüft. Die einzige Angabe,
die ein Mensch von Hand schreibt, hatte in der Vorlage keinen Ort — da liegt
der Verdacht nahe, sie sei überflüssig. Nicht der Status war das Problem,
sondern sein fehlender Platz.

**Folgt daraus:** Alle acht Templates kündigen die Zeile unter *Was hier
entsteht* an, direkt über `Ausgemustert:`. Als Satz formuliert, nicht als
Zeile, die mit `Abgestimmt:` beginnt — sonst liest ein Generator die
Ankündigung als Unterschrift. Der README beschrieb bis dahin die Welt ohne
diesen Schalter und versprach darum, eine Nummer sei ab dem Hinschreiben
verbraucht; das ist mitkorrigiert.

---

## Zwei Kriterien, die sich herausgeschält haben

**Ein Präfix bekommt nur, was im Graphen hängt.** Alles andere ist Fließtext
und gehört in die Notizen des Templates, das es betrifft. Das entschied 5 —
und nur 5. Für 10 hatte ich das sinngemäß gleiche Kriterium vorgeschlagen
(„eine Einstufung kommt ins Frontmatter, wenn eine Prüfung daran hängt"); es
wurde als zu kleinteilig verworfen. Dort gilt also **kein** Kriterium, sondern
der schlichte Zustand: keine Einstufungen.

**Nicht pflegen, sondern abfragen.** Was sich aus den Artefakten ergibt, wird
nicht daneben nochmal hingeschrieben. Der Satz stand schon in `extern.md` bei
der Mock-Liste; er entschied 3 und 6 und zuletzt die Liste der hingenommenen
Risiken in `risiko.md` Frage 4. Bei 1 passt er im Nachhinein, gab aber nicht
den Ausschlag — dort war es die Einsicht, dass kein Werkzeug zwei Prosatexte
vergleichen kann.

Beide Kriterien sind aus Einzelfällen gewachsen, nicht vorher aufgestellt. Wer
sie auf einen neuen Fall anwendet, sollte prüfen, ob er wirklich derselbe ist.
