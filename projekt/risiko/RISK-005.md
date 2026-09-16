---
id: RISK-005
titel: iOS-Build braucht einen macOS-Runner
projektion: risiko
status: entwurf
description: KMP baut iOS nur auf macOS — Wirkung mittel, wird abgefedert.
betrifft: C-002, C-001, I-003
---

Kotlin Multiplatform mit Compose Multiplatform baut das iOS-Target nur
auf macOS (Xcode-Toolchain) — GitHub-gehostete macOS-Runner sind knapper
und teurer als Linux-Runner. Wahrscheinlichkeit mittel, Wirkung mittel.
Umgang: abfedern — macOS-Runner explizit für die iOS-Stufe im Workflow
einplanen. Folge aus [[ADR-001]].
