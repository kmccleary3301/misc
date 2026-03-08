# Artifacts and signoff

## Canonical artifact root

```text
.codex-mc/artifacts/latest/
```

Keep outputs predictable.  
If the repo already uses another artifact directory, either mirror into the canonical root or clearly document the alternate path.

## Minimum artifact expectations by task family

### New content
- build output
- datagen diff if applicable
- GameTest or runtime artifact for actual behavior

### Crash fix
- crash summary
- rerun output showing the previous failure no longer occurs
- remaining uncertainty stated explicitly

### Port
- build output
- datagen/tests if relevant
- runtime-oriented artifact on the target lane

### Release prep
- build outputs
- metadata/version verification
- strongest practical validation artifact ladder for the changed surfaces

## Signoff checklist

Before calling the work done, state:

1. what changed
2. the validation lane used
3. commands run
4. artifact paths
5. what each artifact proves
6. what remains unvalidated

## Bad signoff patterns

- “Looks good”
- “Should work”
- “Build passes”
- “Port complete” with no runtime evidence
- screenshot-only validation when better structured artifacts were available
