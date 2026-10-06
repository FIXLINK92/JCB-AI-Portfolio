# TAG Armored Vehicle QC

## Overview

TAG Armored Vehicle QC is a private, offline-first Android quality-control system for armored-vehicle inspection workflows. It is designed around controlled inspection progression, photographic evidence, signatures, recheck/backjob handling, and a review chain of **Inspector → QCM → QAM**.

## Business Problem

Paper-heavy vehicle quality-control processes create avoidable risks:

- lost or incomplete inspection evidence
- inconsistent checklist execution
- difficult traceability across rework/recheck cycles
- manual photo handling
- weak revision history
- slow final-report preparation

The project digitizes the workflow while preserving auditability and controlled approvals.

## My Role

- Product owner and workflow designer
- Converted real inspection/PDI/FIR source material into structured digital requirements
- Defined roles, approval states, recheck/backjob behavior, evidence capture, signing, and report expectations
- Directed milestone-gated implementation and validation
- Required offline-first operation and backend-enforced security

## Workflow Scope

The source workflow contains a large structured inspection surface, including staged vehicle progression, PDI and FIR checklists, fields, evidence photos, and manager review.

Core user flow:

```text
Inspector → Complete inspection → Sign/submit → QCM review → QAM review → Final approved record/report
                         ↘ Recheck / Need rework ↙
```

## Architecture / Technologies

- Kotlin
- Jetpack Compose
- Room / encrypted local database strategy
- SQLCipher-oriented encrypted storage design
- CameraX for evidence capture
- NestJS backend
- PostgreSQL
- Docker/private deployment direction
- Android tablet landscape-first UI

## Security / Record Controls

Design requirements include:

- encrypted local storage
- immutable signed revisions
- audit history
- controlled synchronization
- trusted-device concepts
- OTP / authentication controls
- backend-enforced authorization
- private rather than public deployment

## Validation Evidence

Validated milestone work has included:

- clean Android builds and debug APK generation
- emulator-based Pixel Tablet/API 34 testing
- backend migrations and automated backend tests
- Android unit/lint/debug validation
- Room instrumentation build validation
- authentication/trusted-device hardening work

The project remains milestone-gated; later production and company-pilot capabilities are not represented as complete until they have passed their respective gates.

## What This Project Demonstrates

- digitizing a complex paper workflow
- Android application architecture
- offline-first thinking
- evidence/photo workflows
- role-based approvals
- security-conscious local storage
- backend/API planning
- immutable/auditable record concepts
- test-driven milestone acceptance

## Portfolio Evidence

Recommended screenshots:

- `screenshots/tag-qc-01-inspector-dashboard.png`
- `screenshots/tag-qc-02-unit-workflow.png`
- `screenshots/tag-qc-03-checklist.png`
- `screenshots/tag-qc-04-photo-evidence.png`
- `screenshots/tag-qc-05-review-state.png`

Architecture: [`../architecture/armored-vehicle-qc.md`](../architecture/armored-vehicle-qc.md)
