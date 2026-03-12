"""Generate minimal draft artifacts from scored topics."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
OUTPUT_DIR = ROOT / "output" / "drafts"


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"topics": []}
    return json.loads(path.read_text(encoding="utf-8"))


def slugify(text: str) -> str:
    cleaned = "".join(char.lower() if char.isalnum() else "-" for char in text)
    return "-".join(part for part in cleaned.split("-") if part) or "untitled-topic"


def build_draft(topic: dict[str, Any], mode: str) -> str:
    title = topic.get("title", "Untitled topic")
    return f"""# {title}

## Mode
{mode}

## Target Reader
People who need a practical explanation about this topic.

## Draft Outline
1. Problem
2. Why it matters
3. Practical steps
4. Common mistakes
5. Summary

## Draft Body
This is a placeholder draft generated to verify the pipeline structure.

## Promo Text
Short promo text will be generated here in a later implementation.
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=["dry_run", "semi_auto", "one_week_auto_test"],
        default="dry_run",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    scored_topics = load_json(DATA_DIR / "scored_topics.json").get("topics", [])
    if not scored_topics:
        return

    topic = scored_topics[0]
    slug = slugify(topic.get("title", "untitled-topic"))
    draft_path = OUTPUT_DIR / f"{slug}.md"
    draft_path.write_text(build_draft(topic, args.mode), encoding="utf-8")

    manifest = {
        "topic_id": topic.get("id"),
        "title": topic.get("title"),
        "slug": slug,
        "mode": args.mode,
        "draft_path": str(draft_path.relative_to(ROOT)),
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }
    (OUTPUT_DIR / f"{slug}.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
