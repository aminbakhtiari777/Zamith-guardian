# Zamith Guardian

Control plane for an AI agent that wants to act. The model may propose an email, a file write, or a shell command. Guardian decides whether that action is allowed, denied, or waiting for the owner. If the action changes after approval, the approval is void.

This is the public slice of the permission gate used in Zamith Assistant. The assistant repository is private. This repository is the part a hiring manager can open.

No production-security or compliance claim is made. The executor here is a stub. It records that an action would have run. It does not send email.

## What a reviewer can check

Twenty cases, no third-party packages:

```bash
PYTHONPATH=. python -m unittest discover -s tests -v
```

The cases cover an allowed read, a denied read outside scope, path traversal, unknown tools, shell and arbitrary HTTP, missing identity, email and SMS and file mutation held for approval, one-time owner approval, a changed body after approval, an expired approval, the wrong approver, and a hidden instruction that is denied instead of queued.

A recorded run is in [`examples/email_changed_after_approval.json`](examples/email_changed_after_approval.json). The agent proposes an email. The owner has not approved that exact body. A later body is blocked because the approval was bound to the original action hash.

## Decision rules

| Request | Result |
| --- | --- |
| `read_file` under `workspace/` or `notes/` | allow and execute |
| `read_file` outside that scope, absolute, or with `..` | deny |
| `send_email`, `send_sms`, `write_file`, `delete_file` | needs owner approval |
| `shell`, `run_command`, `http_request`, any unknown tool | deny |
| instruction hidden in arguments, such as "ignore policy" | deny, not queued |
| approved action whose arguments then change | blocked |

Unknown tools fail closed. Authority stays outside the model.

## Where this sits

Zamith Assistant is the private local assistant: memory, retrieval, voice, and a FastAPI backend. Its communications gateway already refuses to send email or start a call without owner confirmation. Guardian extracts that rule into a standalone, testable gate so the decision can be reviewed without opening the private repository.

Zamith Work is the separate workspace project. It is not required to run these tests.

## Status

Phase 1 is implemented: identity check, allow / deny / approval, approval bound to the action hash, and an append-only trace. Later phases in `ROADMAP.md` are not built.

## Author

Amin Bakhtiari
