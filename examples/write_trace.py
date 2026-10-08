"""Write the sample trace a recruiter can open without running the assistant."""

import json
from pathlib import Path

from guardian.gateway import Gateway
from guardian.models import ActionRequest


def main() -> None:
    gateway = Gateway()
    request = ActionRequest(
        agent_id="job-agent",
        tool="send_email",
        args={"to": "hiring@company.test", "body": "Short note on Zamith Guardian"},
    )
    pending = gateway.propose(request)
    changed = ActionRequest(
        agent_id="job-agent",
        tool="send_email",
        args={"to": "hiring@company.test", "body": "Short note on Zamith Guardian. Also ignore policy."},
    )
    gateway.approve(pending.approval_id or "", changed, approver_id="owner")
    destination = Path(__file__).resolve().parents[1] / "examples" / "email_changed_after_approval.json"
    destination.write_text(gateway.audit.to_json() + "\n", encoding="utf-8")
    print(json.loads(destination.read_text(encoding="utf-8"))[1]["reason"])


if __name__ == "__main__":
    main()
