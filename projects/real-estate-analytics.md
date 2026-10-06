# UAE Real Estate Analytics Platform

## Overview

This project is an analyst-oriented real-estate decision platform for UAE property analysis. The guiding principle is simple: **AI is not the source of truth**. Data must be sourced, normalized, quality-checked, and traceable before it is used to support an investment conclusion.

## Business Problem

Property decisions often combine listing data, transactions, rents, fees, financing, and assumptions from multiple sources. Without evidence lineage and quality controls, automated analysis can produce convincing but unreliable conclusions.

The platform is designed to structure that work into a repeatable analyst workflow.

## My Role

- Product owner and analyst-workflow designer
- Defined evidence/QC requirements
- Directed dashboard and calculation implementation
- Defined approval-state logic and report expectations
- Tested decision scenarios and output behavior

## Core Capabilities

- controlled data imports
- immutable/raw-data preservation concepts
- normalization and duplicate detection
- evidence registers
- comparable-property analysis
- market trends
- investment calculations
- cash and mortgage scenarios
- case history and approvals
- Excel/XLSX and PDF exports
- decision/report workflow controls

## Selected Financial Analysis

The analytical model supports metrics such as:

- gross rental yield
- NOI-oriented analysis
- cash-flow scenarios
- DSCR
- investment return comparisons
- off-plan paid capital vs remaining liability
- comparable AED/sq ft analysis

## Architecture / Technologies

- Python
- Dash-based local analytical UI
- SQLite case history
- structured import/normalization pipeline
- XLSX export
- PDF report generation
- scenario/regression testing

## Governance Model

A broader decision package separates:

1. Market Analysis
2. Investment Analysis
3. Certified Valuation
4. Legal Due Diligence

The software assists analysis; it does not replace licensed valuation or legal review.

## What This Project Demonstrates

- Python analytics
- data quality controls
- evidence lineage
- calculation engines
- dashboard/UI iteration
- analytical reporting
- export workflows
- scenario testing
- responsible use of AI in data-driven decisions

## Portfolio Evidence

Recommended screenshots:

- `screenshots/realestate-01-dashboard.png`
- `screenshots/realestate-02-market-data.png`
- `screenshots/realestate-03-comparables.png`
- `screenshots/realestate-04-investment-analysis.png`
- `screenshots/realestate-05-report-export.png`

Architecture: [`../architecture/real-estate-analytics.md`](../architecture/real-estate-analytics.md)
