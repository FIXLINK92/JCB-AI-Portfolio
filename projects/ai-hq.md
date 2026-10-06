# AI-HQ

## Executive Summary

AI-HQ is my development control-plane and R&D environment for governed AI-assisted software work. It focuses on reusable development controls, CI/runner infrastructure, tool integration, validation and human approval rather than unrestricted autonomous execution.

## Objective

Use AI to increase development speed **without surrendering engineering control**.

The recurring delivery model is:

```text
Scope → Architecture → AI-assisted implementation → Tests → Evidence → Human review → Approval → Commit/merge
```

## My Role

- Founder / owner
- Defined the development-control model
- Directed CI, runner, tooling and integration work
- Required evidence-backed validation before accepting milestones
- Maintained human authority over consequential actions and release decisions

## Selected Areas

- GitHub Actions
- self-hosted runner work
- Docker/rootless container experimentation
- Python/TypeScript tooling
- Git/GitHub governance
- agent/tool integration planning
- reusable milestone-gated delivery patterns
- structured/typed AI decision experiments
- human confirmation for consequential decisions

Architecture: [`../architecture/ai-hq.md`](../architecture/ai-hq.md)

## Engineering Principle

AI-generated output is not automatically accepted. A useful implementation loop is:

1. Give the AI a bounded task with explicit constraints.
2. Require acceptance criteria and validation commands.
3. Implement on an isolated branch/workspace where appropriate.
4. Run automated checks.
5. Collect evidence.
6. Review failures and unintended scope changes.
7. Approve only when evidence supports the claim.

## What I Would Demonstrate Live

1. A scoped technical task.
2. How implementation instructions are bounded.
3. How validation evidence is produced.
4. CI/runner status or project-control artifacts.
5. Why AI does not receive automatic release authority.

## What This Demonstrates

- AI-native development workflow,
- disciplined use of coding agents,
- CI/CD concepts,
- local-first tooling,
- Git governance,
- repeatable development controls,
- ability to learn and integrate new developer tools while maintaining verification boundaries.

## Claim Boundary

This portfolio does **not** claim deep production mastery of every AI tool named in current job postings. Capability is represented only where I can explain and demonstrate the underlying work.

## Portfolio Evidence To Add

- `screenshots/ai-hq-01-ci.png`
- `screenshots/ai-hq-02-runner.png`
- `screenshots/ai-hq-03-project-controls.png`
- `screenshots/ai-hq-04-validation.png`
