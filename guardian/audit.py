"""Append-only action trace. A recruiter should be able to read one record."""

import json
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class TraceRecord:
    agent_id: str
    tool: str
    args: dict[str, Any]
    decision: str
    reason: str
    status: str
    approval_id: str | None = None
    at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class AuditLog:
    def __init__(self) -> None:
        self.records: list[TraceRecord] = []

    def add(self, record: TraceRecord) -> TraceRecord:
        self.records.append(record)
        return record

    def to_json(self) -> str:
        return json.dumps([record.to_dict() for record in self.records], indent=2)
