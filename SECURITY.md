# Security Model

Zamith Guardian exists to reduce the risk of AI agents performing actions outside intended boundaries.

## Security assumptions

- Models can produce incorrect or manipulated outputs.
- Agent prompts and retrieved content can contain hostile instructions.
- Tool output may be malformed or untrusted.
- A successful tool call is not proof that the action was authorized.
- Agent memory can contain stale or incorrect information.
- Humans can approve an action without noticing a material change unless the system detects it.

## Core controls

### 1. Default deny

Unknown agents, tools, resources, and actions are denied until explicitly permitted.

### 2. Separation of intelligence and authority

The model can:

- propose
- plan
- explain
- request

The Guardian-controlled application decides whether execution is permitted.

### 3. Least privilege

Permissions should be narrow across:

- tool
- action
- resource
- user
- project
- tenant
- time
- task

### 4. Human approval

High-impact operations should require approval with a clear preview of:

- intended action
- target
- data involved
- side effects
- scope

### 5. Approval integrity

If the requested action materially changes after approval, previous approval must not silently carry over.

### 6. Auditability

Privileged actions should record:

- agent identity
- user/owner context
- action requested
- policy decision
- approval result
- execution result
- timestamps
- relevant error/status information

### 7. Tool isolation

Agents should not receive direct unrestricted credentials to external systems.

Where possible, privileged access should pass through a controlled gateway.

### 8. Limits

Agents should have explicit:

- step limits
- retry limits
- timeout limits
- request-rate limits
- spending/budget limits

### 9. Safe failure

If authorization, identity, policy, or approval state cannot be verified, execution should fail closed.

### 10. Evaluation

Security-sensitive behavior needs regression tests before release.

## Threat areas to evaluate

- Prompt injection
- Indirect prompt injection
- Permission bypass
- Cross-user or cross-tenant leakage
- Tool misuse
- Repeated destructive actions
- Unauthorized delegation
- Stale approvals
- Infinite loops
- Secret exposure
- Audit-log gaps
- Agent impersonation

## Current status

This repository is in planning/development stage.

Nothing in this repository should currently be interpreted as a production security guarantee or compliance certification.
