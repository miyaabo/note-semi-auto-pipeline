"""Select a generated draft for the human review queue."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
OUTPUT_DIR = ROOT / "output" / "drafts"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {"topics": []} if path.name == "scored_topics.json" else {"items": []}
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def select_target() -> dict:
    scored = load_json(DATA_DIR / "scored_topics.json").get("topics", [])
    queue = load_json(DATA_DIR / "queue.json").get("items", [])
    if not scored:
        return {"items": queue}

    selected = scored[0]
    slug = "".join(char.lower() if char.isalnum() else "-" for char in selected.get("title", ""))
    slug = "-".join(part for part in slug.split("-") if part) or "untitled-topic"

    queue_item = {
        "topic_id": selected.get("id"),
        "title": selected.get("title"),
        "slug": slug,
        "draft_path": f"output/drafts/{slug}.md",
        "status": "pending_review",
        "selected_at": datetime.now(timezone.utc).isoformat(),
    }

    if all(item.get("topic_id") != queue_item["topic_id"] for item in queue):
        queue.append(queue_item)

    return {"items": queue}


def main() -> None:
    argparse.ArgumentParser().parse_args()
    write_json(DATA_DIR / "queue.json", select_target())


if __name__ == "__main__":
    main()
