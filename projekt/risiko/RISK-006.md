---
id: RISK-006
titel: TestFlight-Update zeigt auf dem iPhone den alten Stand
projektion: risiko
status: entwurf
description: Nach dem TestFlight-Update zeigte die App den alten Text, erst Neuinstallation half — hingenommen.
betrifft: G-003, X-003
---

Nach dem Update über TestFlight meldet das iPhone den neuen Build, die
App zeigt aber weiter den alten Text; erst Löschen und Neuinstallieren
bringt den neuen Stand. Beobachtet am 2026-09-16 mit Build 24 (iOS 27,
kurz nach dem Systemupdate): „Hallo Welt" statt „Здравей, свят!", während
Android aus demselben Lauf richtig war. Ursache ungeklärt.

Wahrscheinlichkeit mittel, Wirkung niedrig. Umgang: hinnehmen — das
Projekt soll zeigen, dass GitHub für beide Plattformen bauen und
ausliefern kann ([[G-003]]); einem Detailproblem der Aktualisierung wird
bewusst nicht nachgegangen, Löschen und Neuinstallieren reicht.
