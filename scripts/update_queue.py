"""Update queue metadata and initialize a simple performance log entry."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"


def load_json(path: Path, default: dict) -> dict:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=["dry_run", "semi_auto", "one_week_auto_test"],
        default="dry_run",
    )
    args = parser.parse_args()

    queue = load_json(DATA_DIR / "queue.json", {"items": []})
    performance_log = load_json(DATA_DIR / "performance_log.json", {"entries": []})

    for item in queue.get("items", []):
        item["last_mode"] = args.mode
        item["last_updated"] = datetime.now(timezone.utc).isoformat()

    performance_log["entries"].append(
        {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "mode": args.mode,
            "summary": "Placeholder performance entry. Human analysis remains semi-automated.",
        }
    )

    write_json(DATA_DIR / "queue.json", queue)
    write_json(DATA_DIR / "performance_log.json", performance_log)


if __name__ == "__main__":
    main()
