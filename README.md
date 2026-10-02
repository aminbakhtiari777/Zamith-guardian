# Zamith Guardian

### Trust, Governance, and Control Layer for AI Agents

**Zamith Guardian** is a long-term AI product concept for controlling, supervising, evaluating, and auditing AI agents across personal and company environments.

The goal is not to build another agent framework. Zamith Guardian is intended to become a **control plane** around agents: deciding what they may access, what they may do, when they must ask for approval, and how their actions can be reviewed.

## Product vision

As AI systems become more agentic, the hard problem is no longer only whether a model can perform a task.

The hard problem becomes:

- Which agent is allowed to do what?
- Which data may it access?
- Which tools may it call?
- Which actions require human approval?
- How do we know what actually happened?
- How do we detect failures, regressions, or suspicious behavior?
- How do we stop or contain an agent when needed?

Zamith Guardian is designed around those questions.

## Core principles

- **Authority is separate from intelligence** — the model may propose an action; policy decides whether it may happen.
- **Least privilege** — agents receive only the minimum permissions needed.
- **Human approval for high-impact actions** — sensitive operations require confirmation.
- **Full traceability** — important decisions, tool calls, and outcomes should be auditable.
- **Fail closed** — uncertainty about identity, scope, or permission should block execution.
- **Model independent** — governance should continue working even when the underlying LLM changes.
- **Measurable reliability** — agent behavior should be evaluated, not trusted by appearance.
- **Containment by design** — agents should operate inside explicit boundaries.

## Planned capabilities

### Agent identity and scope
- Agent identity
- Owner / organization scope
- Purpose and allowed tasks
- Session and task boundaries
- Per-agent permissions

### Permission and policy engine
- Tool-level permissions
- Data-access permissions
- Resource scopes
- Role-based policies
- Time- or context-based rules
- Deny / allow / approval decisions

### Human approval
- Approval gates
- High-risk action confirmation
- Action previews
- Approval expiration
- Re-approval after material changes
- Multi-step approval flows

### Execution controls
- Tool allowlists
- Sandboxed execution
- Rate limits
- Budget limits
- Step limits
- Retry limits
- Timeout policies
- Stop / kill controls

### Audit and observability
- Agent action logs
- Tool-call logs
- Inputs and outputs
- Decision traces at the application level
- Approval history
- Failure records
- Cost and latency metrics

### Evaluation
- Task success rate
- Tool success rate
- Permission violations
- Regression testing
- Repeated-action detection
- Infinite-loop detection
- Hallucinated-action detection
- Policy compliance tests

### Multi-agent governance
- Supervisor/worker boundaries
- Agent-to-agent handoff controls
- Shared resource policies
- Delegation limits
- Cross-agent audit trails

## Example future workflow

```text
Agent proposes action
      ↓
Guardian receives request
      ↓
Identify agent + user + task
      ↓
Evaluate permission and policy
      ↓
Low-risk? ── yes ──→ Execute
      │
      no
      ↓
Request human approval
      ↓
Approved? ── no ──→ Block + log
      │
      yes
      ↓
Execute through controlled tool gateway
      ↓
Verify result
      ↓
Audit + metrics + final status
```

Example:

> An AI sales agent wants to send an email, update a CRM record, and attach a contract.

Guardian should independently check whether the agent may access that customer, whether the file is permitted, whether sending requires approval, and whether the final action matches what the human approved.

## Planned architecture

```text
AI Agent / Agent Platform
          ↓
     Guardian Gateway
          ↓
 Agent Identity + Context
          ↓
      Policy Engine
     ↙      ↓       ↘
Permissions Approval  Risk Rules
     ↘      ↓       ↙
 Controlled Tool Gateway
          ↓
Tools • Files • Email • APIs • Databases • Devices
          ↓
   Audit + Evaluation + Monitoring
```

Guardian is intentionally positioned **between agents and real-world authority**.

## Development stages

**Phase 0 — Product definition**  
Define agent threat model, permission model, approval model, and evaluation criteria.

**Phase 1 — Policy gateway**  
Agent identity, action requests, allow/deny rules, tool scopes, and logging.

**Phase 2 — Human approval**  
Approval queue, action previews, expiration, and confirmation boundaries.

**Phase 3 — Controlled execution**  
Tool gateway, limits, sandboxing, retries, timeouts, and kill controls.

**Phase 4 — Audit and observability**  
Searchable audit trail, metrics, failure analysis, and policy-violation reporting.

**Phase 5 — Evaluation**  
Regression suites, policy-compliance tests, agent reliability scoring inputs, and release gates.

**Phase 6 — Multi-agent governance**  
Delegation, handoffs, supervisor/worker controls, and cross-agent resource rules.

**Phase 7 — Organization readiness**  
Admin controls, tenant isolation, policy templates, deployment, backup, and production hardening.

## What this repository will demonstrate

This project is intended to demonstrate applied AI engineering across:

- Agent architecture
- Tool calling
- MCP
- Authentication and authorization
- Permission systems
- Human-in-the-loop design
- AI evaluation
- Observability
- Security
- Backend/API design
- Multi-agent systems
- Production governance

## Current status

**Planning / architecture stage.**

No production-security or compliance claims are made yet. Capabilities will be marked complete only after implementation and testing.

## Relationship to other Zamith projects

- **Zamith Assistant** — personal local-first AI assistant
- **Zamith Work** — AI operating layer for teams and companies
- **Zamith Guardian** — trust, control, and governance layer for AI agents

Each product is maintained as an independent repository.

## Author

**Amin Bakhtiari**  
AI system builder focused on applied AI products, architecture, evaluation, and product engineering.
