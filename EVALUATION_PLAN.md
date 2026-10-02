# Evaluation Plan

Zamith Guardian should be evaluated as a control system, not only as an AI feature.

## Primary evaluation questions

1. Does Guardian block actions that are not allowed?
2. Does it allow legitimate actions without unnecessary friction?
3. Does it request human approval at the correct time?
4. Does execution match the approved action?
5. Are all important decisions and results auditable?
6. Can an agent escape its intended scope?
7. Do policy changes create regressions?

## Initial metrics

### Permission correctness
- Allowed-action success rate
- Forbidden-action block rate
- False allow rate
- False deny rate

### Approval behavior
- Required-approval detection rate
- Approval bypass rate
- Stale-approval rejection rate
- Changed-action reapproval rate

### Execution reliability
- Tool success rate
- Timeout rate
- Retry rate
- Duplicate-action rate
- Task completion rate

### Safety boundaries
- Cross-user access violations
- Cross-tenant access violations
- Unauthorized tool attempts
- Unauthorized delegation attempts
- Secret exposure incidents

### Observability
- Audit coverage
- Missing action records
- Missing policy decisions
- Trace completeness

### Performance
- Policy-decision latency
- Approval-gateway latency
- Tool-gateway overhead

## Test categories

- Unit-level policy tests
- Integration tests
- End-to-end agent tests
- Adversarial prompt/content tests
- Regression suites
- Failure-recovery tests
- Multi-agent delegation tests

## Release gate principle

A new capability should not be released only because the implementation works.

It should be released only when:

- intended actions succeed,
- forbidden actions remain blocked,
- approval rules behave correctly,
- audit records are complete,
- critical regression tests pass.
