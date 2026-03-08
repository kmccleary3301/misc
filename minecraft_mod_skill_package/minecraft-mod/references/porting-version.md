# Version porting playbook

Use this when moving a mod to a new Minecraft version.

## Strong bias

Port in the smallest safe sequence:

1. build/toolchain/mappings
2. compile breaks
3. resource/datagen drift
4. automated checks
5. runtime smoke
6. signoff

## Procedure

### 1. Establish the port boundary
Write down:
- current version
- target version
- loader
- mappings
- Java version requirement
- whether the port is in place or branch-based

### 2. Update build and toolchain first
Do not start by randomly fixing code while the build metadata is stale.

Update:
- version constants
- Gradle plugin versions
- mappings / Parchment if used
- Java/toolchain if required

### 3. Repair compile-time breakage
Common breakage buckets:
- renamed or moved classes/methods
- registry and bootstrap changes
- resource/data schema changes
- client renderer/model changes
- networking changes
- Mixin target drift

### 4. Regenerate or diff generated outputs
If the mod uses datagen or generated assets/resources, rerun it and inspect the diff.

### 5. Exercise the narrowest runtime path
A port is not done until you have runtime-oriented evidence.

Minimum good finish:
- build succeeds
- datagen/tests are reconciled
- smoke or GameTest artifact is clean

## Port completion rule

Do not say “ported” unless you can also say:
- what runtime surfaces were actually exercised
- what remains unvalidated
