# Minecraft Mod Skill Package Overview

## Included

- `SKILL.md` — polished main orchestrator skill
- `agents/openai.yaml` — minimal Codex interface metadata
- `references/` — lane-specific playbooks and decision docs
- `scripts/` — helper commands for detection, validation, artifact collection, and crash/log summarization
- `assets/` — signoff, scenario, and helper-mod artifact specs
- `evals/` — starter prompt set, rubric, and artifact assertions

## Key entrypoints

- `scripts/mc-bootstrap`
- `scripts/mc-doctor`
- `scripts/mc-run-build`
- `scripts/mc-run-test`
- `scripts/mc-run-gametest`
- `scripts/mc-run-datagen`
- `scripts/mc-run-smoke`
- `scripts/mc-tail-logs`
- `scripts/mc-summarize-crash`
- `scripts/mc-collect-artifacts`

## Canonical artifact root

`.codex-mc/artifacts/latest/`
