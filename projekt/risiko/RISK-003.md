---
id: RISK-003
titel: Signierung/Secrets falsch gehandhabt
projektion: risiko
status: entwurf
description: Zertifikate/Keystore falsch abgelegt — Wirkung hoch, wird vermieden.
betrifft: C-001, X-001
---

Apple-Zertifikate/Provisioning-Profile oder der Android-Keystore werden
falsch abgelegt — im Klartext im Repository, oder mit zu weiten
Zugriffsrechten in GitHub Actions. Wahrscheinlichkeit mittel, Wirkung
hoch. Umgang: vermeiden — GitHub Secrets, keine Zertifikate/Keystores im
Repository, Fastlane `match` (oder vergleichbar) zur verschlüsselten
Verwaltung.
