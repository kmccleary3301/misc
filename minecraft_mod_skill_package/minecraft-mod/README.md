# Minecraft Mod Skill for Codex

A production-oriented Codex skill package for **Minecraft Java mod development**.

This skill is designed for **terminal-native, evidence-backed** work across:
- new mod scaffolding
- existing repo modification
- version porting
- loader porting
- crash / mixin / registry triage
- datagen
- GameTests
- runtime smoke checks
- packaging / release prep

## Install

Recommended repo-local install path for Codex:

```text
.agents/skills/minecraft-mod/
```

User-level install also works in Codex-supported skill locations.

## What this package contains

- `SKILL.md` — the orchestrator
- `references/` — focused decision docs and playbooks
- `scripts/` — helper commands for detection, validation, artifact collation, and crash/log summarization
- `assets/` — scenario and helper-mod specifications
- `evals/` — a starter prompt/rubric set

## First use

Inside a mod repo, the skill usually works best if Codex first runs:

```bash
scripts/mc-bootstrap
scripts/mc-doctor
```

`mc-bootstrap` creates a repo-local `.codex-mc/` workspace, optional vendored wrappers, and canonical artifact directories.
`mc-doctor` writes a structured environment report into `.codex-mc/artifacts/latest/doctor.json`.

## Design stance

This package is intentionally biased toward:

- **single-loader / single-version by default**
- **small validated changes**
- **artifacts before claims**
- **instructions first; scripts for determinism**
- **closed-loop runtime signal**


## Direct script execution

If you want to execute the bundled helper scripts before vendoring repo-local shims:

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export MC_SKILL_HOME="${MC_SKILL_HOME:-$CODEX_HOME/skills/minecraft-mod}"
"$MC_SKILL_HOME/scripts/mc-bootstrap"
"$MC_SKILL_HOME/scripts/mc-doctor"
```

For repo-local installs, set `MC_SKILL_HOME` to the skill folder path instead.
