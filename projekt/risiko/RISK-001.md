---
id: RISK-001
titel: TestFlight-Build hängt an fehlender Export-Compliance
projektion: risiko
status: entwurf
description: Ohne Verschlüsselungs-Angabe gibt Apple den Build nicht an Tester frei — vermieden über Info.plist.
betrifft: G-002, X-003
---

Apple gibt einen hochgeladenen Build erst an Tester frei, wenn die Frage
nach Verschlüsselung beantwortet ist; sonst steht er auf „Missing
Compliance", obwohl [[I-003]] Erfolg meldet. Wahrscheinlichkeit hoch,
Wirkung mittel. Umgang: vermeiden — `ITSAppUsesNonExemptEncryption =
false` in `Info.plist`.
