# Codex MC Helper Mod (spec)

This is a **design target**, not a mandatory runtime dependency for the skill.

Purpose:
Provide deterministic runtime artifacts during development so the agent is not flying blind.

## Scope

The helper mod should be:
- dev-only
- excluded from release jars
- able to emit deterministic artifacts into `.codex-mc/live/`

## Recommended commands

- `/codexmc screenshot <name>`
- `/codexmc state dump <name>`
- `/codexmc scene load <scene>`
- `/codexmc wait <ticks>`

## Recommended outputs

### Screenshot
- `.codex-mc/live/screenshots/<name>.png`
- `.codex-mc/live/screenshots/<name>.json`

Suggested metadata:
- dimension
- player position
- yaw / pitch
- held item
- targeted block/entity
- open screen id/title
- GUI scale
- scene id
- world identifier

### State dump
- `.codex-mc/live/state/<name>.json`

Suggested contents:
- dimension and coordinates
- inventory summary
- selected stack
- target summary
- open screen summary
- registry assertions relevant to the scenario
