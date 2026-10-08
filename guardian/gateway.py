"""Propose, approve, execute. Approval is bound to the exact action hash."""

import hashlib
import json
import uuid
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Callable

from guardian.audit import AuditLog, TraceRecord
from guardian.models import ActionRequest, Decision
from guardian.policy import Policy

Executor = Callable[[ActionRequest], str]


def action_hash(request: ActionRequest) -> str:
    payload = json.dumps(request.canonical(), sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode()).hexdigest()


@dataclass
class Approval:
    approval_id: str
    action_hash: str
    owner_id: str
    expires_at: datetime
    used: bool = False


class Gateway:
    def __init__(self, policy: Policy | None = None, executor: Executor | None = None) -> None:
        self.policy = policy or Policy()
        self.executor = executor or _stub_executor
        self.audit = AuditLog()
        self._approvals: dict[str, Approval] = {}

    def propose(self, request: ActionRequest) -> TraceRecord:
        decision, reason = self.policy.evaluate(request)
        approval_id = None
        status = "blocked"
        if decision is Decision.ALLOW:
            self.executor(request)
            status = "executed"
        elif decision is Decision.NEEDS_APPROVAL:
            approval_id = self._issue(request)
            status = "pending_approval"
        record = TraceRecord(
            agent_id=request.agent_id,
            tool=request.tool,
            args=request.args,
            decision=decision.value,
            reason=reason,
            status=status,
            approval_id=approval_id,
        )
        return self.audit.add(record)

    def approve(self, approval_id: str, request: ActionRequest, approver_id: str, now: datetime | None = None) -> TraceRecord:
        now = now or datetime.now(timezone.utc)
        approval = self._approvals.get(approval_id)
        reason = "approval accepted"
        status = "executed"
        if approval is None:
            reason, status = "unknown approval", "blocked"
        elif approval.used:
            reason, status = "approval already used", "blocked"
        elif approval.owner_id != approver_id:
            reason, status = "approver is not the owner", "blocked"
        elif now > approval.expires_at:
            reason, status = "approval expired", "blocked"
        elif approval.action_hash != action_hash(request):
            reason, status = "action changed after approval", "blocked"
        else:
            approval.used = True
            self.executor(request)
        record = TraceRecord(
            agent_id=request.agent_id,
            tool=request.tool,
            args=request.args,
            decision=Decision.ALLOW.value if status == "executed" else Decision.DENY.value,
            reason=reason,
            status=status,
            approval_id=approval_id,
        )
        return self.audit.add(record)

    def _issue(self, request: ActionRequest) -> str:
        approval_id = uuid.uuid4().hex
        self._approvals[approval_id] = Approval(
            approval_id=approval_id,
            action_hash=action_hash(request),
            owner_id=request.owner_id,
            expires_at=datetime.now(timezone.utc) + timedelta(minutes=15),
        )
        return approval_id


def _stub_executor(request: ActionRequest) -> str:
    return f"stub:{request.tool}"
