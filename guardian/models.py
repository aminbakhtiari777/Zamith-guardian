"""Action and decision types. The model proposes; Guardian decides."""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class Decision(str, Enum):
    ALLOW = "allow"
    DENY = "deny"
    NEEDS_APPROVAL = "needs_approval"


@dataclass(frozen=True)
class ActionRequest:
    agent_id: str
    tool: str
    args: dict[str, Any] = field(default_factory=dict)
    owner_id: str = "owner"

    def canonical(self) -> dict[str, Any]:
        return {
            "agent_id": self.agent_id,
            "tool": self.tool,
            "args": self.args,
            "owner_id": self.owner_id,
        }
