# Crash debugging

Use this when the mod fails during startup or runtime.

## Fast classification

Try to place the failure into one bucket before editing:

- missing class / missing dependency
- mapping drift / symbol mismatch
- Mixin target or injector failure
- registry or bootstrap failure
- data/resource/datapack load failure
- renderer / client-only failure
- networking / packet mismatch
- Java / Gradle / plugin / toolchain failure
- compat failure with another mod

## Workflow

1. reproduce if possible
2. run `mc-tail-logs`
3. run `mc-summarize-crash`
4. identify:
   - primary exception
   - first user-mod frame
   - implicated mod ids
   - failure bucket
5. change the narrowest likely cause
6. rerun the nearest sufficient validation
7. collect artifacts

## Output discipline

A good crash summary should fit on one screen:
- source file
- primary exception
- probable category
- first user-mod frame
- next-check suggestions

## Anti-patterns

- huge speculative refactors before reproducing
- “fixing” multiple unrelated systems at once
- calling it fixed because the exception changed shape
