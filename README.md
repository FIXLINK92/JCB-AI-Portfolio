# JCB AI Portfolio

**AI-assisted software development • workflow digitization • full-stack systems • automation • data analytics**

This repository is a recruiter-facing technical portfolio for **JCB**. It presents selected systems, architecture decisions, validation practices, and project evidence while intentionally excluding production secrets, customer data, credentials, and proprietary source repositories.

> **Portfolio scope:** architecture, project summaries, screenshots, test evidence, selected non-sensitive implementation patterns, and demonstrations. Production repositories remain private.

## Featured Projects

| Project | Focus | Selected Technologies | Status represented here |
|---|---|---|---|
| [Luxorium / JCB Control Plane](projects/luxorium-control-plane.md) | Multi-company control plane, access control, licensing, authentication | TypeScript, NestJS, PostgreSQL, WebAuthn/passkeys, Playwright, GitHub Actions | Active development; frontend and backend foundations validated |
| [TAG Armored Vehicle QC](projects/armored-vehicle-qc.md) | Offline-first armored-vehicle quality-control workflow | Kotlin, Jetpack Compose, Room/SQLCipher, NestJS, PostgreSQL, CameraX, Docker | Milestone-gated development; security/auth foundations validated |
| [UAE Real Estate Analytics](projects/real-estate-analytics.md) | Evidence-backed property and investment analysis | Python, Dash, SQLite, Excel/PDF reporting, data QC pipelines | Analyst workflow and report/export capabilities validated locally |
| [AI-HQ](projects/ai-hq.md) | AI development control plane and governed agent/tooling experimentation | GitHub Actions, Docker, Python/TypeScript tooling, CI, MCP/tool integrations | Active R&D and development infrastructure |

## What I Build

I use AI-assisted development to accelerate implementation, but I do **not** treat generated code as automatically correct. My projects use scoped requirements, explicit architecture, milestone gates, automated tests, security controls, and human review before release.

Typical work includes:

- Full-stack application architecture and implementation
- REST APIs and backend services
- PostgreSQL / SQLite data models
- Authentication, authorization, sessions, passkeys, MFA, and audit controls
- Offline-first mobile workflows
- Workflow automation and business-process digitization
- Data ingestion, normalization, quality control, analytics, and reporting
- CI/CD, GitHub Actions, Docker, local development environments
- DNS/domain/server troubleshooting and deployment preparation
- AI-assisted development workflows with governed human review

## Development Method

```mermaid
flowchart LR
    A[Business problem] --> B[Requirements & scope]
    B --> C[Architecture]
    C --> D[AI-assisted implementation]
    D --> E[Automated tests]
    E --> F[Security / QC review]
    F --> G[Human approval]
    G --> H[Release or next milestone]
```

## Portfolio Safety

This portfolio intentionally excludes:

- API keys, tokens, passwords, `.env` files, and secrets
- Customer or employer confidential information
- Production databases and personal data
- Complete proprietary application source code
- Internal security details that would create unnecessary exposure

## Review Guide

1. Start with the four project case studies in [`projects/`](projects/).
2. Open [`architecture/`](architecture/) for GitHub-rendered system diagrams.
3. Review [`screenshots/`](screenshots/) for the evidence checklist and image naming convention.
4. Review [`demos/`](demos/) for recommended short walkthroughs.
5. Review [`code-samples/`](code-samples/) for the policy governing any public code examples.

## Contact / Availability

Available for AI-assisted full-stack development, workflow automation, business-process digitization, technical troubleshooting, and implementation-focused roles in the UAE.

---

**Important:** This repository is an evaluation portfolio. Unless a file explicitly states otherwise, no license is granted to copy, redistribute, commercialize, or reuse the underlying project designs or proprietary systems.
