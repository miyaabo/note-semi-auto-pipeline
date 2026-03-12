"""Normalize and deduplicate topics in data/raw_topics.json."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW_TOPICS_PATH = ROOT / "data" / "raw_topics.json"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {"topics": []}
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def normalize_title(title: str) -> str:
    return " ".join(title.lower().split())


def merge_topics() -> dict:
    raw_data = load_json(RAW_TOPICS_PATH)
    seen = set()
    merged = []

    for topic in raw_data.get("topics", []):
        key = normalize_title(topic.get("title", ""))
        if not key or key in seen:
            continue
        seen.add(key)
        merged.append(topic)

    return {"topics": merged}


def main() -> None:
    argparse.ArgumentParser().parse_args()
    write_json(RAW_TOPICS_PATH, merge_topics())


if __name__ == "__main__":
    main()
