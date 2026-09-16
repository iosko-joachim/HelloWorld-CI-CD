---
id: RISK-004
titel: Ungewollte Einreichung durch jeden Push
projektion: risiko
status: entwurf
description: Ein Push könnte ungewollt einreichen — vermieden durch Einreichung per Knopfdruck.
betrifft: G-002, C-001
---

Löste jeder Push auf `main` eine Einreichung aus ([[G-001]], [[I-001]]),
ginge auch ein nicht dafür gedachter Commit an die Tester.
Wahrscheinlichkeit mittel, Wirkung niedrig. Umgang: vermeiden — ein Push
baut und testet nur, eingereicht wird per Knopfdruck ([[ADR-004]]).
