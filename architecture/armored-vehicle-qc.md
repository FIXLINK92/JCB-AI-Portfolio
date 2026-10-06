# TAG Armored Vehicle QC — Portfolio Architecture

```mermaid
flowchart LR
    Inspector[Inspector Tablet]
    Local[(Encrypted Local Store)]
    Photos[Photo Evidence]
    Sync[Controlled Sync/API]
    Backend[NestJS Backend]
    DB[(PostgreSQL)]
    QCM[QCM Review]
    QAM[QAM Approval]
    Report[Final Controlled Report]

    Inspector --> Local
    Inspector --> Photos
    Local --> Sync
    Photos --> Sync
    Sync --> Backend
    Backend --> DB
    Backend --> QCM
    QCM --> QAM
    QAM --> Report
    QCM -. recheck / rework .-> Inspector
```

## Design Principle

The tablet remains useful offline; synchronization, approvals, and final records are controlled rather than assumed to be continuously connected.
