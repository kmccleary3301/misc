# New NeoForge mod playbook

Use this for a greenfield NeoForge mod or a clean NeoForge module.

## Default posture

- single-loader
- single-version
- current NeoForge / ModDevGradle conventions
- keep the scaffold minimal
- wire validation immediately

## Suggested order

1. Confirm target Minecraft version and Java/toolchain.
2. Start from a modern NeoForge baseline.
3. Establish mod id, metadata, and runs.
4. Add the smallest requested content surface.
5. Wire data generation if generated resources are part of the requested surface.
6. Add the narrowest useful tests:
   - GameTests for game behavior
   - JUnit for pure logic / serialization where appropriate
7. Run:
   - build
   - data / datagen
   - tests / GameTests
   - smoke if runtime surfaces changed
8. Collect artifacts and summarize the exact validation performed.

## Good first artifacts

- `build.txt`
- `datagen-diff.txt`
- `test.txt` and/or `gametest.txt`
- `runtime-log.txt`
- `summary.md`

## Common mistakes

- assuming old Forge-era patterns are still the right baseline
- overfitting the scaffold to a future multi-loader dream
- skipping runtime validation because build/test passed
