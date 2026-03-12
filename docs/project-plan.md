# Project Plan

## Objective
Build a semi-automated note content pipeline for low-priced note products.

The short-term goal is to validate whether this system can generate useful note drafts with low cost.
The first business goal is not large profit, but getting the first paid result with minimal manual effort.

---

## Core Operating Policy

This project is intentionally **semi-automated**, not fully automated.

### Human-controlled parts
- Topic collection
- Topic selection
- Performance analysis / interpretation
- Final note publishing

### Automated parts
- Draft generation
- Title generation
- Section structure generation
- Promo text generation
- Draft storage
- Review queue creation
- Optional GitHub Pages test publishing
- Logging
- Scheduled/manual workflow execution

---

## Workflow Overview

### Step 1: Topic collection (semi-automated)
The operator gathers topic candidates manually or with light assistance from external sources.

Examples:
- personal idea stock
- current practical issues
- trends from technical communities
- repeated questions or confusion points

Topic collection is not fully automated because topic quality is critical and should remain human-controlled at first.

### Step 2: Topic selection (semi-automated)
The operator asks AI to evaluate candidate topics.

AI should score candidates based on:
- practical usefulness
- suitability for a low-priced note
- ability to explain without face/voice content
- potential for series expansion
- relevance to the creator’s knowledge area

The operator reviews the ranking and decides which topic to use.

### Step 3: Draft generation (automated)
Once a topic is selected, the system automatically generates:
- title candidates
- target reader summary
- draft note structure
- body draft
- short promo text

Generated files are saved to the repository.

### Step 4: Queueing and storage (automated)
Generated drafts are stored in:
- draft storage
- review queue
- optional publish/test output

### Step 5: Publishing (manual for note)
Final note publishing remains manual.

The system should prepare note-ready markdown/text files, but must not auto-publish to note for now.

### Step 6: Performance review (semi-automated)
Results are reviewed by the operator with AI support.

The operator and AI together evaluate:
- whether the topic was good
- whether the structure was useful
- whether similar topics should be added to stock
- whether future priority should change

---

## Initial Rollout Strategy

### Phase 1: First run = automated dry run
The first content item should be generated end-to-end automatically for environment verification.

Purpose:
- confirm pipeline execution
- confirm output format
- confirm storage and queue behavior

This first run does not require real note publishing.

### Phase 2: From second run onward = semi-automated
From the second item onward:
- topic collection is semi-automated
- topic selection is semi-automated
- performance analysis is semi-automated
- draft generation and storage stay automated

### Phase 3: One-week automation test
At some point, run the pipeline automatically for about one week.

Purpose:
- estimate API cost
- estimate draft volume
- inspect output quality drift
- measure stock accumulation

This one-week mode should generate drafts automatically but does not need automatic note publishing.

### Phase 4: Decision point
After the one-week test, decide whether to continue with:
- semi-automated operation
- more automation
- reduced automation

Decision criteria:
- cost
- draft quality
- usable stock accumulation
- manual workload

---

## Content Strategy

This project is based on the idea of building and using topic stock.

### Topic stock cycle
1. prepare topic candidates
2. generate drafts from selected topics
3. accumulate stock
4. analyze results
5. reprioritize future topics

Important:
The system should not become a closed loop where AI only copies its own previous outputs.
Future topic creation should be influenced by:
- seed topics
- external observations
- past performance

---

## Repository Structure

Expected structure:

- `data/`
- `prompts/`
- `scripts/`
- `output/`
- `.github/workflows/`
- `docs/`

---

## Key Data Files

### `data/seed_topics.json`
Stores manually prepared topic seeds.

### `data/raw_topics.json`
Stores collected candidate topics.

### `data/scored_topics.json`
Stores AI-evaluated topics and scores.

### `data/performance_log.json`
Stores performance review data.

### `data/queue.json`
Stores current publishing/review queue.

---

## Output Directories

### `output/drafts/`
Generated draft files.

### `output/review_queue/`
Drafts ready for human review.

### `output/published/`
Published or archived finalized outputs.

### `output/rejected/`
Rejected or low-quality drafts.

---

## Planned Scripts

### `collect_topics.py`
Collect candidate topics from seed stock and optional external inputs.

### `merge_topics.py`
Normalize and deduplicate collected topics.

### `score_topics.py`
Use AI to score and rank topics.

### `generate_drafts.py`
Generate draft note content and promo text.

### `select_publish_target.py`
Choose which draft should move to review queue.

### `export_note_draft.py`
Export note-ready markdown/text.

### `update_queue.py`
Update topic priority and queue data after review.

---

## Workflow Modes

### dry_run
- used for first automated verification
- no real publishing
- saves generated files only

### semi_auto
- standard operating mode
- human controls topic collection/selection and analysis
- system generates and stores drafts automatically

### one_week_auto_test
- scheduled automated generation for about one week
- used only for cost/quality evaluation
- no note auto-publishing

---

## Current Non-Goals

These are intentionally out of scope for now:
- note auto-publishing
- fully autonomous topic strategy
- automatic monetization optimization
- complex analytics integration
- aggressive trend scraping

---

## Success Criteria

Short-term success:
- first dry run works end-to-end
- second and later runs support semi-automated workflow
- review queue is generated correctly
- one-week automation test is possible

Business success (early stage):
- build reusable stock
- reduce manual writing effort
- prepare a repeatable process for low-priced note publishing
- eventually achieve the first paid result

---

## Operating Principle

Use AI heavily for writing and structuring.
Keep humans responsible for choosing, judging, and publishing.
