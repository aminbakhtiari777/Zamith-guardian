# Zamith Guardian Roadmap

## Stage 0 — Foundation

- [ ] Define first agent use cases
- [ ] Define threat model
- [ ] Define agent identity model
- [ ] Define action schema
- [ ] Define permission model
- [ ] Define approval levels
- [ ] Define evaluation baseline

## Stage 1 — Guardian Gateway

- [ ] Receive structured action requests
- [ ] Identify agent and task context
- [ ] Validate requested tool/action
- [ ] Allow / deny decision
- [ ] Structured reason codes
- [ ] Audit every decision

## Stage 2 — Permission Engine

- [ ] Tool permissions
- [ ] Data scopes
- [ ] Resource scopes
- [ ] User and role policies
- [ ] Agent-specific policies
- [ ] Default-deny behavior

## Stage 3 — Human Approval

- [ ] Approval queue
- [ ] Action preview
- [ ] Approve / deny
- [ ] Approval expiration
- [ ] Detect action changes after approval
- [ ] Re-approval rules

## Stage 4 — Controlled Execution

- [ ] Tool gateway
- [ ] Timeouts
- [ ] Retry limits
- [ ] Step limits
- [ ] Rate limits
- [ ] Budget controls
- [ ] Sandboxing
- [ ] Emergency stop / kill control

## Stage 5 — Audit & Observability

- [ ] Searchable action logs
- [ ] Approval history
- [ ] Failure records
- [ ] Agent/tool metrics
- [ ] Cost tracking
- [ ] Latency tracking
- [ ] Policy-violation reports

## Stage 6 — Evaluation

- [ ] Policy-compliance tests
- [ ] Permission regression tests
- [ ] Tool-call evaluation
- [ ] Repeated-action detection
- [ ] Infinite-loop detection
- [ ] Hallucinated-action detection
- [ ] End-to-end task verification

## Stage 7 — Multi-Agent Governance

- [ ] Delegation policy
- [ ] Agent handoff control
- [ ] Supervisor/worker boundaries
- [ ] Shared-resource policy
- [ ] Cross-agent audit trail
- [ ] Delegation depth limits

## Stage 8 — Organization Readiness

- [ ] Admin console
- [ ] Policy templates
- [ ] Tenant isolation
- [ ] Backup and recovery
- [ ] Deployment hardening
- [ ] Monitoring
- [ ] Incident workflow

## Rule

Guardian must never treat an LLM response as authority by itself.

Every real-world action must pass through explicit application-controlled policy and permission checks.
