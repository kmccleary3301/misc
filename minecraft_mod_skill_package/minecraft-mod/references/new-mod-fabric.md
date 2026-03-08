# New Fabric mod playbook

Use this for a greenfield Fabric mod or a clean Fabric module.

## Default posture

- single-loader
- single-version
- Mojmap / current repo convention
- keep the scaffold minimal
- wire validation immediately

## Suggested order

1. Confirm target Minecraft version and Java/toolchain.
2. Start from a modern Fabric baseline.
3. Establish mod id, package names, and metadata.
4. Add the smallest requested content surface:
   - item
   - block
   - recipe
   - tags
   - entity
   - GUI
   - config
   - datagen
5. If generated data is involved, wire datagen now.
6. Add at least one narrow validation path:
   - GameTest for game behavior
   - narrow automated test for pure logic
7. Run:
   - build
   - datagen if relevant
   - smoke if runtime surfaces changed
8. Collect artifacts and summarize exactly what was exercised.

## Good first artifacts

- `build.txt`
- `datagen-diff.txt` if content/resources changed
- `gametest.txt` or `runtime-log.txt`
- `summary.md`

## Common mistakes

- adding content without a datagen path when generated resources are expected
- assuming registration is correct because code compiles
- introducing multi-loader abstractions before the mod even exists
