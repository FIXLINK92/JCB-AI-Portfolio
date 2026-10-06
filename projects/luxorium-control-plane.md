# Luxorium / JCB Control Plane

## Executive Summary

Luxorium / JCB Control Plane is a multi-company administration, licensing and access-control platform. Its defining rule is **owner-controlled activation**: commercial authority stays with the owner, while company administrators operate only inside explicitly granted limits.

This project is the strongest full-stack example in this portfolio because it combines UI, backend API, PostgreSQL persistence, authentication/session controls, role boundaries and automated validation.

## Business Problem

A multi-company platform needs more than authentication. It must prevent tenant administrators from silently changing commercial entitlements or security-sensitive limits.

The platform therefore separates:

- company creation and activation,
- user/device/application limits,
- licensing term and expiry,
- tenant administration,
- owner-only commercial authority,
- high-risk security actions,
- persistent audit-oriented records.

## My Role

- Founder / product owner / interim technical decision owner
- Defined the owner-controlled activation model
- Directed milestone-gated AI-assisted implementation
- Reviewed architecture and validation evidence before milestone acceptance
- Defined security/session decisions and commercial authority boundaries

## Selected Architecture

- **Frontend:** multi-section administrative UI
- **Backend:** NestJS / TypeScript REST API
- **Persistence:** PostgreSQL + migration framework
- **Authentication:** WebAuthn/passkey foundation, MFA/session controls
- **Validation:** unit, integration and Playwright E2E testing
- **Governance:** milestone gates and owner review before baseline approval

Architecture: [`../architecture/luxorium-control-plane.md`](../architecture/luxorium-control-plane.md)

## Security Decisions Represented

- mandatory passkey direction for the owner role,
- passkey + MFA direction for administrators,
- password + TOTP treated as transitional where applicable,
- privileged idle-session limits,
- absolute-session limits,
- fresh-factor requirement for selected high-risk actions,
- database-backed organization/user/membership/audit foundations.

## Validation Evidence Recorded During Development

Selected validated milestone evidence includes:

- frontend baseline with automated unit and Playwright coverage,
- NestJS backend API foundation with unit/integration validation,
- PostgreSQL core schema/migration foundation,
- organization/user/membership/audit persistence structures,
- authentication/session foundation progressed under a dedicated milestone.

Exact production source and private implementation details are intentionally excluded from this portfolio.

## What I Would Demonstrate Live

1. Navigate the company control surface.
2. Explain the owner vs. company-admin authority boundary.
3. Show a license/limit flow and why the admin cannot increase commercial limits.
4. Show test evidence and explain how a change is accepted.
5. Trace one request conceptually from UI → API → authorization → persistence → audit.

## What This Demonstrates for an AI / Full-Stack Role

- practical system decomposition,
- Node.js/TypeScript backend work,
- REST API thinking,
- relational data modelling and migrations,
- authentication/session architecture,
- browser automation/testing,
- security-first product decisions,
- AI-assisted implementation under human-controlled acceptance.

## Portfolio Evidence To Add

Use sanitized development data only:

- `screenshots/luxorium-01-dashboard.png`
- `screenshots/luxorium-02-company-master.png`
- `screenshots/luxorium-03-licenses.png`
- `screenshots/luxorium-04-auth-flow.png`
- `screenshots/luxorium-05-test-evidence.png`
