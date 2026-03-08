# Helper tooling specification

This skill expects an agent-friendly tool surface, but it does not assume the repo already has one.

## Minimal helper suite

- `mc-bootstrap`
- `mc-doctor`
- `mc-run-build`
- `mc-run-test`
- `mc-run-client`
- `mc-run-server`
- `mc-run-gametest`
- `mc-run-datagen`
- `mc-run-smoke`
- `mc-tail-logs`
- `mc-summarize-crash`
- `mc-collect-artifacts`

## Optional full-power helpers

- `mc-capture-screenshot`
- `mc-world-state`
- `mc-matrix`
- companion MCP
- companion dev-only helper mod

## Design goals

- 1–2 commands to signal after a meaningful change
- deterministic output paths
- summaries that fit on one screen
- repo-safe bootstrap
- easy artifact inspection

## Preferred layering

### Layer 1 — deterministic runner
Native Gradle tasks, GameTests, datagen, smoke wrappers

### Layer 2 — agent-facing CLI
The `mc-*` commands in this package

### Layer 3 — optional MCP / helper mod
For screenshots, runtime state dumps, scenario loading, and richer perception
