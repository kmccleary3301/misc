# Performance-sensitive work

Use this when optimizing hot paths, render paths, or tick-heavy systems.

## First rule

Do not claim something is faster without a before/after artifact.

## Procedure

1. identify the hot path or symptom
2. capture a baseline artifact
3. make one narrow change
4. rerun the same scenario
5. compare artifacts
6. preserve correctness

## Useful artifacts

- timing logs
- profiler output
- focused benchmark/test output
- smoke logs proving no regressions
- before/after scenario summaries

## Anti-patterns

- “should be faster”
- optimizing speculative code paths before measuring
- mixing architectural refactors with micro-optimizations
- skipping behavior validation after low-level changes
