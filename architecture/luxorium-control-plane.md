# Luxorium / JCB Control Plane — Portfolio Architecture

```mermaid
flowchart TB
    Owner[Owner / Commercial Authority]
    Admin[Company Admin]
    User[Company User]
    FE[Web Frontend]
    API[NestJS API]
    Auth[Authentication / Sessions]
    DB[(PostgreSQL)]
    Audit[(Audit Records)]

    Owner --> FE
    Admin --> FE
    User --> FE
    FE --> API
    API --> Auth
    API --> DB
    API --> Audit

    Owner -. defines commercial limits .-> API
    Admin -. manages within limits .-> API
```

## Boundary Principle

Company administrators may manage their tenant within owner-defined limits; they do not receive authority to increase commercial entitlements.
