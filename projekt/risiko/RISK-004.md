---
id: RISK-004
titel: Ungewollter Store-Release durch jeden Push
projektion: risiko
status: entwurf
description: Jeder Push auf main löst einen Release aus — wird beobachtet.
betrifft: G-002, C-001
---

Da jeder Push auf `main` einen Store-Release auslöst ([[G-001]],
[[I-001]]), kann ein nicht dafür gedachter Commit einen echten Release
erzeugen. Wahrscheinlichkeit mittel, Wirkung niedrig. Umgang: beobachten
— die Release-Strategie ist noch offen, vorerst nur `main` als Auslöser.
