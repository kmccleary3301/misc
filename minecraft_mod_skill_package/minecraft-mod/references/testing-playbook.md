# Testing playbook

## Goal

Convert Minecraft runtime uncertainty into the cheapest sufficient evidence.

## Evidence ladder

1. build / static checks
2. narrow automated checks
3. GameTests
4. runtime smoke
5. behavior artifact
6. signoff

## Choose the smallest correct tool

### Pure logic / serialization / utility code
Prefer:
- JUnit or equivalent narrow tests

### Registration or in-world behavior
Prefer:
- GameTests

### Load sanity / startup confidence
Prefer:
- smoke run with filtered logs and summary

### Resource / generated content work
Prefer:
- datagen + generated diff
- plus GameTest or smoke if behavior changed

### Visible UI / renderer behavior
Prefer:
- screenshot + structured state/log artifact
- not screenshot-only if a state dump is possible

## Fabric notes
- Use the repo’s existing Fabric testing setup if present.
- If no tests exist, add the smallest useful GameTest or narrow loader-backed test rather than building an elaborate harness first.
- Events often beat Mixins for compatibility and maintainability.

## NeoForge notes
- Use the repo’s current run/test/data conventions.
- Prefer narrow JUnit tests for pure logic and GameTests for behavior.
- Respect current ModDevGradle / run configuration patterns already present in the repo.

## Smoke philosophy

Smoke is not “prove everything”.
Smoke is “confirm the changed surface does not immediately explode”.

A good smoke artifact usually answers:
- Did the chosen runtime boot?
- Did the mod initialize?
- Did we avoid immediate fatal errors?
- What remains unvalidated?

## Good validation loops

### Content change
- build
- datagen
- GameTest if behavior matters

### Crash fix
- reproduce
- summarize crash
- rerun smoke or the nearest affected scenario

### Renderer fix
- build
- smoke
- screenshot/state artifact if visual output matters

### Port
- build
- datagen/tests
- runtime-oriented artifact
