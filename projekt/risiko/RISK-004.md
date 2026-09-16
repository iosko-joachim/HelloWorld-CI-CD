---
id: RISK-004
titel: Ungewollter Store-Release durch jeden Push
projektion: risiko
status: entwurf
description: Ein Push könnte ungewollt veröffentlichen — vermieden durch Einreichung per Knopfdruck.
betrifft: G-002, C-001
---

Würde jeder Push auf `main` einen Store-Release auslösen ([[G-001]],
[[I-001]]), könnte ein nicht dafür gedachter Commit einen echten Release
erzeugen. Wahrscheinlichkeit mittel, Wirkung niedrig. Umgang: vermeiden
— ein Push baut und testet nur, eingereicht wird per Knopfdruck
([[ADR-004]]).
