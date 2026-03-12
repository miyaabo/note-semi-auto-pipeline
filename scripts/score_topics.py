"""Score topics and write results to data/scored_topics.json.

This is intentionally deterministic for now. Replace the scoring function with
an API-backed implementation later.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {"topics": []}
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def score_topic(topic: dict) -> dict:
    title = topic.get("title", "")
    notes = topic.get("notes", "")
    base_score = min(100, 50 + len(title) + min(20, len(notes) // 4))
    return {
        **topic,
        "score": base_score,
        "reasons": [
            "Placeholder heuristic score.",
            "Human review is still required before publishing.",
        ],
        "recommended": base_score >= 60,
        "status": "needs_human_review",
    }


def score_topics() -> dict:
    raw_data = load_json(DATA_DIR / "raw_topics.json")
    scored = [score_topic(topic) for topic in raw_data.get("topics", [])]
    scored.sort(key=lambda item: item.get("score", 0), reverse=True)
    return {"topics": scored}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=["dry_run", "semi_auto", "one_week_auto_test"],
        default="dry_run",
    )
    return parser.parse_args()


def main() -> None:
    parse_args()
    write_json(DATA_DIR / "scored_topics.json", score_topics())


if __name__ == "__main__":
    main()
