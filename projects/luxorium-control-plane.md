# Luxorium / JCB Control Plane

## Overview

Luxorium / JCB Control Plane is a multi-company administration and licensing platform designed around **owner-controlled activation**. The platform separates commercial authority from company administration: the owner creates and activates a company, defines limits, and issues secure activation/invitation flows; company administrators operate only within those approved limits.

## Business Problem

A SaaS-style product serving multiple companies needs more than login screens. It needs clear authority boundaries around:

- company activation
- user and device limits
- license term and expiry
- application/module entitlement
- administrative roles
- security-sensitive changes
- auditability

The objective is to prevent tenant administrators from silently increasing commercial limits or bypassing owner governance.

## My Role

- Product owner and system decision owner
- Defined the activation and commercial-control model
- Directed frontend and backend implementation through milestone-gated AI-assisted development
- Reviewed architecture, test evidence, security controls, and handoff criteria
- Kept production-impacting decisions under explicit owner approval

## Architecture / Technologies

- TypeScript
- NestJS backend API
- PostgreSQL
- Database migrations
- WebAuthn/passkeys foundation
- MFA/session controls
- REST API architecture
- Frontend automated tests
- Playwright end-to-end testing
- GitHub-based version control and CI practices

## Security Model

Selected security decisions include:

- passkeys mandatory for the owner role
- passkey + MFA support for administrative roles
- password + TOTP treated as transitional where applicable
- privileged-session idle limits
- absolute session limits
- fresh-factor authentication for high-risk actions
- audit-oriented persistence and role separation

## Validation Evidence

Current validated foundations include:

- frontend baseline with navigation, company master areas, notifications/settings concepts, licensing views, and agreement placeholders
- backend API foundation with automated unit/integration validation
- PostgreSQL schema foundation covering organization, user, membership, and audit-oriented structures
- authentication/session foundation under dedicated milestone review

The private production repository is intentionally not exposed through this portfolio.

## What This Project Demonstrates

- full-stack system decomposition
- access-control design
- multi-tenant thinking
- authentication and session-security concepts
- PostgreSQL schema/migration discipline
- API foundation design
- automated testing
- milestone-based technical governance

## Portfolio Evidence

Recommended screenshots:

- `screenshots/luxorium-01-dashboard.png`
- `screenshots/luxorium-02-company-master.png`
- `screenshots/luxorium-03-licenses.png`
- `screenshots/luxorium-04-auth-flow.png`
- `screenshots/luxorium-05-test-evidence.png`

Architecture: [`../architecture/luxorium-control-plane.md`](../architecture/luxorium-control-plane.md)
