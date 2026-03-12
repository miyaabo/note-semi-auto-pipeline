# AGENTS.md

## Project goal
Build a semi-automated note content pipeline for low-priced note products.

## Human-controlled parts
- Topic collection
- Topic selection
- Performance analysis / interpretation
- Final note publishing

## Automated parts
- Draft generation
- Title generation
- Section structure generation
- Promo text generation
- Draft storage
- Review queue creation
- Optional GitHub Pages test publishing
- Logging
- Scheduled/manual workflow execution

## Workflow policy
The project should support three modes:

1. dry_run
   - used for the first end-to-end environment verification
   - generates output files without real publishing

2. semi_auto
   - default mode
   - human handles topic collection, topic selection, and analysis
   - system handles draft generation and queue output

3. one_week_auto_test
   - scheduled automated generation for about one week
   - used for cost and quality review
   - no note auto-publishing

## Required repository structure
- data/
- prompts/
- scripts/
- output/
- docs/
- .github/workflows/

## Required scripts
- collect_topics.py
- merge_topics.py
- score_topics.py
- generate_drafts.py
- select_publish_target.py
- export_note_draft.py
- update_queue.py

## Data expectations
Use JSON files for intermediate data:
- data/seed_topics.json
- data/raw_topics.json
- data/scored_topics.json
- data/performance_log.json
- data/queue.json

## Output expectations
- output/drafts/
- output/review_queue/
- output/published/
- output/rejected/

## Constraints
- Do not auto-publish to note
- Keep the implementation low-cost
- Prefer simple modular Python scripts
- Prefer deterministic file-based workflow
- Make GitHub Actions support both manual trigger and scheduled trigger

## Priority order
1. Make the first dry run work end-to-end
2. Support semi-automated operation
3. Support one-week automated testing
