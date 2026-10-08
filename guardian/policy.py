"""Fail-closed policy. Unknown tools and uncertain scope are denied."""

from guardian.models import ActionRequest, Decision

READ_PREFIXES = ("workspace/", "notes/")
APPROVAL_TOOLS = frozenset({"send_email", "send_sms", "write_file", "delete_file"})
DENIED_TOOLS = frozenset({"shell", "run_command", "http_request"})

INJECTION_MARKERS = (
    "ignore previous",
    "ignore policy",
    "bypass approval",
    "you are now",
    "system prompt",
)


def _text_blob(args: dict) -> str:
    parts: list[str] = []
    for value in args.values():
        if isinstance(value, str):
            parts.append(value.lower())
    return "\n".join(parts)


def contains_injection(args: dict) -> bool:
    blob = _text_blob(args)
    return any(marker in blob for marker in INJECTION_MARKERS)


def _path_allowed(path: str) -> bool:
    if not path or path.startswith("/") or ".." in path.split("/"):
        return False
    return path.startswith(READ_PREFIXES)


class Policy:
    def evaluate(self, request: ActionRequest) -> tuple[Decision, str]:
        if not request.agent_id.strip() or not request.tool.strip():
            return Decision.DENY, "missing agent or tool identity"
        if contains_injection(request.args):
            return Decision.DENY, "untrusted instruction hidden in tool arguments"
        if request.tool in DENIED_TOOLS:
            return Decision.DENY, "tool is outside the allowlist"
        if request.tool == "read_file":
            path = str(request.args.get("path", ""))
            if _path_allowed(path):
                return Decision.ALLOW, "read inside the owner workspace"
            return Decision.DENY, "read outside the allowed scope"
        if request.tool in APPROVAL_TOOLS:
            return Decision.NEEDS_APPROVAL, "external or mutating action needs owner approval"
        return Decision.DENY, "unknown tool fails closed"
