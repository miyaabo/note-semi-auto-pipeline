# Note Semi-Auto Pipeline

Minimal Python skeleton for a semi-automated note content pipeline.

## Operating rules

- Topic collection is semi-automated.
- Topic selection is semi-automated.
- Performance analysis is semi-automated.
- Draft generation is automated.
- Queue output is automated.
- note publishing stays manual.

## Repository layout

- `data/`: JSON inputs, intermediate files, and logs
- `prompts/`: placeholder prompt files for future LLM integration
- `scripts/`: modular Python pipeline scripts
- `output/`: generated drafts, review queue, and archive folders
- `.github/workflows/`: GitHub Actions workflow skeleton
- `docs/`: planning and project documentation

## Modes

- `dry_run`: first end-to-end environment verification without publishing
- `semi_auto`: default operating mode for human-guided topic flow
- `one_week_auto_test`: scheduled generation mode for short-term cost and quality review

## Local setup

1. Install Python 3.11 or newer.
2. Edit `data/seed_topics.json` with your topic seeds.
3. Run the scripts in order.

```bash
python scripts/collect_topics.py --mode dry_run
python scripts/merge_topics.py
python scripts/score_topics.py --mode dry_run
python scripts/generate_drafts.py --mode dry_run
python scripts/select_publish_target.py
python scripts/export_note_draft.py
python scripts/update_queue.py --mode dry_run
```

## Expected outputs

- `data/raw_topics.json`: collected topics
- `data/scored_topics.json`: ranked candidate topics
- `data/queue.json`: human review queue
- `data/performance_log.json`: simple review log
- `output/drafts/`: generated markdown drafts and metadata
- `output/review_queue/`: note-ready files for manual review

## GitHub Actions

The workflow supports:

- manual trigger with mode selection
- scheduled trigger for `one_week_auto_test`

The workflow uploads `data/` and `output/` as artifacts after each run.

## Next steps

1. Replace placeholder scoring and drafting logic with API-backed implementations.
2. Refine the prompt files in `prompts/`.
3. Expand queue updates and performance review logic.
4. Add tests once the first real implementation details are fixed.
