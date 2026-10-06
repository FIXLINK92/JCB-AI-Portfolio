-- Synthetic portfolio example. No production schema or customer data.

CREATE TABLE demo_company (
    id UUID PRIMARY KEY,
    name TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE demo_membership (
    company_id UUID NOT NULL REFERENCES demo_company(id),
    user_subject TEXT NOT NULL,
    role TEXT NOT NULL CHECK (role IN ('OWNER', 'COMPANY_ADMIN', 'USER')),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    PRIMARY KEY (company_id, user_subject)
);

CREATE TABLE demo_audit_event (
    id BIGSERIAL PRIMARY KEY,
    company_id UUID REFERENCES demo_company(id),
    actor_subject TEXT NOT NULL,
    action TEXT NOT NULL,
    object_type TEXT NOT NULL,
    object_id TEXT,
    occurred_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    metadata JSONB NOT NULL DEFAULT '{}'::jsonb
);

CREATE INDEX demo_audit_company_time_idx
    ON demo_audit_event (company_id, occurred_at DESC);
