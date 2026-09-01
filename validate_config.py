"""Validate the shape of a credential-free account example."""
import json
import sys
from pathlib import Path


def validate(path: str) -> None:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    required = {"account_id", "profile_directory", "session", "dry_run"}
    missing = sorted(required - data.keys())
    if missing:
        raise SystemExit(f"Missing fields: {', '.join(missing)}")
    if data["dry_run"] is not True:
        raise SystemExit("Examples must keep dry_run=true")
    if data["session"].get("isolated_storage") is not True:
        raise SystemExit("Session isolation must be explicit")
    print(f"Validated {data['account_id']} (dry-run)")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python examples/validate_config.py <json-file>")
    validate(sys.argv[1])
