"""Collect topic candidates into data/raw_topics.json.

This stub keeps collection semi-automated. It prepares deterministic JSON output
from seed topics and can produce dry-run data for environment verification.
"""

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


def collect_topics(mode: str) -> dict:
    seed_data = load_json(DATA_DIR / "seed_topics.json", {"topics": []})
    topics = []

    for index, topic in enumerate(seed_data.get("topics", []), start=1):
        topics.append(
            {
                "id": topic.get("id", f"raw-{index:03d}"),
                "title": topic.get("title", f"Untitled topic {index}"),
                "source": topic.get("source", "manual_seed"),
                "priority": topic.get("priority", index),
                "notes": topic.get("notes", ""),
                "status": "collected",
                "collected_at": datetime.now(timezone.utc).isoformat(),
            }
        )

    if mode == "dry_run" and not topics:
        topics.append(
            {
                "id": "raw-dry-run-001",
                "title": "Dry run verification topic",
                "source": "dry_run_seed",
                "priority": 1,
                "notes": "Generated automatically to verify the pipeline environment.",
                "status": "collected",
                "collected_at": datetime.now(timezone.utc).isoformat(),
            }
        )

    return {"topics": topics}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=["dry_run", "semi_auto", "one_week_auto_test"],
        default="dry_run",
        help="Pipeline operating mode.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    write_json(DATA_DIR / "raw_topics.json", collect_topics(args.mode))


if __name__ == "__main__":
    main()
