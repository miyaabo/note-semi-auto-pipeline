"""Export the selected queue item into output/review_queue/ for manual review.

This script prepares note-ready markdown but does not publish anywhere.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
REVIEW_DIR = ROOT / "output" / "review_queue"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {"items": []}
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    argparse.ArgumentParser().parse_args()
    queue_items = load_json(DATA_DIR / "queue.json").get("items", [])
    if not queue_items:
        return

    selected = queue_items[0]
    draft_path = ROOT / selected["draft_path"]
    if not draft_path.exists():
        return

    export_path = REVIEW_DIR / f"{selected['slug']}.md"
    export_path.write_text(draft_path.read_text(encoding="utf-8"), encoding="utf-8")


if __name__ == "__main__":
    main()
