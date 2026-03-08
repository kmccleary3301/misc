---
name: "minecraft-mod"
description: "Use for Minecraft Java mod work in terminal-native coding sessions: create, modify, port, debug, test, and package Fabric or NeoForge mods; handle mappings, Mixins, registries, datagen, GameTests, crash reports, compat, performance-sensitive changes, and loader/version architecture decisions with artifact-backed validation."
---

# Minecraft Mod

You are operating in a runtime-sensitive domain.  
Do not guess from source text alone.  
Detect the environment, choose the simplest viable lane, make narrowly scoped changes, and collect artifacts before claiming success.

This skill is for **Minecraft Java mod development**:
- Fabric
- NeoForge
- single-loader / multi-loader decisions
- single-version / multi-version decisions
- mappings / Parchment / Mixin work
- datagen / resources / registries / compat
- crash triage / runtime smoke / GameTests / packaging

Do **not** use this skill for:
- Bukkit / Spigot / Paper plugins
- datapack-only work with no Java or loader code, unless the repo is already a mod workspace
- generic Java / Gradle work unrelated to Minecraft modding

If the repo also has an `AGENTS.md`, follow repo-specific guidance **first** and use this skill as the reusable domain workflow.

## Core operating stance

Treat Minecraft mod work as a controlled loop:

1. **Detect** the repo and runtime shape.
2. **Choose** the narrowest correct lane.
3. **Bootstrap** missing helpers if the loop is too weak.
4. **Change** the smallest surface that can move the task forward.
5. **Validate** in 1–2 commands.
6. **Collect** artifacts into a predictable place.
7. **Only then** continue or sign off.

This skill is not a wiki.  
Open only the references you need.

## Hard rules

1. **Start with environment detection.**  
   Before large edits, detect:
   - loader
   - Minecraft version
   - mappings
   - Java/toolchain
   - Gradle wrapper and available tasks
   - whether GameTests, datagen, helper tooling, or runtime harnesses already exist

2. **Default to simplicity.**  
   Unless the user explicitly needs more:
   - stay **single-loader**
   - stay **single-version**
   - stay inside the repo’s current architecture
   - prefer a direct port or a branch over speculative shared-core complexity

3. **Use Fabric as the greenfield default only when the task is truly unconstrained.**  
   If the user names NeoForge, the repo is already NeoForge, or a dependency/ecosystem constraint points there, stay NeoForge.

4. **Do not cargo-cult multi-loader infrastructure.**  
   Only introduce Stonecutter / Stonecraft / Architectury-style structure when there is a real long-term cross-loader and/or cross-version requirement.

5. **Do not claim success from a green build alone.**  
   “Build passed” is not the same as:
   - the mod loads
   - a registry entry exists
   - a recipe works
   - a renderer no longer crashes
   - a port is complete
   - a compat issue is fixed

6. **After every meaningful change, get signal in at most 1–2 tool calls.**  
   Preferred pattern:
   - run the nearest sufficient check
   - inspect the summary artifact

7. **Prefer the cheapest sufficient evidence.**  
   Not every change needs a full client boot.  
   Use the artifact ladder.

8. **Treat Mixins as hazardous.**
   - Prefer events / hooks / accessors / wideners / platform APIs first.
   - Keep injections as narrow as possible.
   - Confirm target names and descriptors against the current mappings.
   - Do not sign off on a Mixin fix without log-backed confirmation.

9. **When visual behavior matters, gather a visual artifact plus structured state when possible.**  
   Screenshots are helpful, but state dumps and focused logs are usually higher-signal.

10. **Leave the workspace easier to operate next time.**  
    If the repo lacks deterministic wrappers or artifact directories, use `mc-bootstrap` or create the smallest safe local tooling under `.codex-mc/`.

## Skill paths (only when you need direct script execution)

When Codex invokes a skill, it can read the bundled files directly.  
If you need to execute the helper scripts by path before vendoring repo-local shims, set a stable skill root once.

Typical user-skill install:

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export MC_SKILL_HOME="${MC_SKILL_HOME:-$CODEX_HOME/skills/minecraft-mod}"
```

Typical repo-local install:

```bash
export MC_SKILL_HOME="${MC_SKILL_HOME:-$PWD/.agents/skills/minecraft-mod}"
```

Then helpers are available at:

```bash
"$MC_SKILL_HOME/scripts/mc-bootstrap"
"$MC_SKILL_HOME/scripts/mc-doctor"
```

After `mc-bootstrap`, prefer the shorter repo-local shims under `.codex-mc/bin/`.

## First 5 minutes

Run or perform the equivalent of:

```bash
scripts/mc-bootstrap
scripts/mc-doctor
```

If the repo already has local wrappers under `.codex-mc/bin/`, prefer those.

At minimum, determine:

- **loader**
  - Fabric
  - NeoForge
  - mixed / multi-loader
  - unknown
- **Minecraft version**
- **mappings**
  - Mojmap / official Mojang mappings
  - Parchment
  - other / unknown
- **build plugins**
  - Fabric Loom
  - ModDevGradle / NeoGradle
  - Architectury / Stonecutter / Stonecraft
- **available tasks**
  - client
  - server
  - GameTest
  - datagen
  - test
  - build
- **repo shape**
  - greenfield scaffold
  - existing single-loader repo
  - shared-core / multi-loader repo
  - versioned workspace
- **current loop quality**
  - is there already a stable validation path?
  - are artifacts already collected somewhere?
  - is there already a screenshot/state helper?

If you cannot explain the repo shape and validation path, do **not** make major edits yet.

## Choose the lane

### Lane A — New mod
Use when the user wants a new mod or a new major module inside a clean workspace.

Default:
- single-loader
- single-version
- Fabric when no stronger constraint exists
- NeoForge when named, already present, or ecosystem constraints require it

Validate with:
- build
- datagen if content/resources changed
- GameTest or narrow test if behavior is nontrivial
- runtime smoke for anything that touches actual load/runtime behavior

Open only what you need:
- `references/new-mod-fabric.md`
- `references/new-mod-neoforge.md`
- `references/testing-playbook.md`

### Lane B — Existing repo extension
Use when the repo already exists and the task is “add/fix/modify”.

Rules:
- respect the existing loader/version structure
- do not reorganize the build unless the task requires it
- identify the current validation path before broad edits
- extend the repo’s existing conventions unless they are broken

Open only what you need:
- `references/repo-triage.md`
- `references/testing-playbook.md`
- `references/compat-and-interop.md`

### Lane C — Version port
Use when moving the mod to a new Minecraft version.

Preferred order:
1. upgrade build/toolchain/mappings
2. repair compile breaks
3. rerun datagen if needed
4. rerun narrow tests / GameTests
5. get at least one runtime-oriented artifact before calling the port complete

Open only what you need:
- `references/porting-version.md`
- `references/testing-playbook.md`
- `references/artifacts-and-signoff.md`

### Lane D — Loader port
Use when porting Fabric ↔ NeoForge or extending support to another loader.

Decide between:
- direct port in place
- separate branch
- shared-core / multi-loader structure

Bias toward:
- direct port or separate branch first
- shared-core only when the product really needs ongoing multi-loader maintenance

Open only what you need:
- `references/porting-loader.md`
- `references/loader-selection.md`
- `references/multi-loader-multi-version.md`
- `references/compat-and-interop.md`

### Lane E — Crash / runtime failure
Use when the build is green or mostly green but runtime is broken.

Workflow:
1. reproduce
2. tail or summarize the log/crash
3. classify the failure
4. fix the narrowest likely cause
5. rerun the smallest relevant check
6. collect artifacts

Open only what you need:
- `references/crash-debugging.md`
- `references/mixin-guidelines.md`
- `references/testing-playbook.md`

### Lane F — Add tests / strengthen the loop
Use when the repo lacks enough signal to work safely.

Default:
- pure logic / serialization => JVM or loader-backed unit tests
- game behavior => GameTests
- load sanity => smoke run
- visible behavior => screenshot + state/log artifact if possible

Open only what you need:
- `references/testing-playbook.md`
- `references/helper-tooling-spec.md`
- `references/artifacts-and-signoff.md`

### Lane G — Release / packaging
Use when preparing a release or a high-confidence handoff.

Validate the highest relevant artifact ladder for the changed surfaces.
Do not overclaim. Explicitly list what was and was not validated.

Open only what you need:
- `references/release-prep.md`
- `references/artifacts-and-signoff.md`

## Architecture choices

Use this bias order:

1. **Stay on the repo’s current loader and version** unless the task is a port.
2. **Prefer single-loader / single-version** unless the user or product requirements say otherwise.
3. **Prefer interop over abstraction.**
4. **Introduce shared-core structure only with a real maintenance case.**

### Mapping stance

Default modern baseline: **official Mojang mappings**.  
Treat **Parchment** as optional augmentation when better parameter names and Javadocs materially improve the task.  
Do not assume Parchment is required.

### Interop stance

Treat these as distinct tools:
- Fabric API
- Forgified Fabric API
- loader-native APIs
- shared common code

Do not confuse **interop** with **abstraction**.  
FFAPI can reduce friction on NeoForge, but it is not a magic layer that removes all loader-specific code.

## The artifact ladder

Use the cheapest sufficient artifact ladder for the task:

1. **Build / static**
   - compile
   - generated sources/resources valid
   - lint/format if the repo already uses them

2. **Narrow automated checks**
   - JVM tests
   - loader-backed narrow tests
   - serialization / registry utility checks

3. **GameTests**
   - deterministic in-world behavior
   - block/item/entity interactions
   - content registration smoke with game context

4. **Runtime smoke**
   - client or server boot
   - no immediate crash
   - mod entrypoint/load sanity
   - focused load-time checks

5. **Behavior artifact**
   - datagen diff
   - GameTest report
   - runtime log summary
   - crash summary
   - screenshot
   - structured world-state / UI-state dump

6. **Signoff**
   - only after the evidence exists

Canonical artifact root:

```text
.codex-mc/artifacts/latest/
```

Typical files:
- `doctor.json`
- `doctor.md`
- `build.txt`
- `test.txt`
- `gametest.txt`
- `datagen.txt`
- `datagen-diff.txt`
- `runtime-log.txt`
- `log-tail.txt`
- `crash-summary.md`
- `smoke-summary.md`
- `world-state.json`
- `screenshots/*.png`
- `manifest.json`
- `summary.md`

## Helper command surface

Prefer these helpers when available:

```text
scripts/mc-bootstrap
scripts/mc-doctor
scripts/mc-run-build
scripts/mc-run-test
scripts/mc-run-client
scripts/mc-run-server
scripts/mc-run-gametest
scripts/mc-run-datagen
scripts/mc-run-smoke
scripts/mc-tail-logs
scripts/mc-summarize-crash
scripts/mc-capture-screenshot
scripts/mc-world-state
scripts/mc-collect-artifacts
scripts/mc-matrix
```

If the repo has vendored shims under `.codex-mc/bin/`, you may prefer those for a shorter loop.

### Bootstrap rule

If the workspace is missing deterministic helpers, do **not** wait for the human to build them.  
Use `mc-bootstrap` or create the smallest safe local wrapper set under `.codex-mc/`.

The default bootstrap should be **repo-safe**:
- create directories
- vendor wrappers
- stage templates
- avoid invasive build changes unless the task requires them

## Claims policy

Before saying any of the following, verify you have matching artifacts:

- “the mod loads”
- “the crash is fixed”
- “the registry issue is fixed”
- “the renderer works”
- “the port is complete”
- “the compat hook works”
- “release-ready”

Match each claim to evidence.

Examples:
- **“the mod loads”** => smoke artifact + runtime log summary
- **“the item/block is registered”** => GameTest or runtime artifact, not just source edits
- **“the recipe works”** => datagen + recipe artifact and preferably a behavior check
- **“the Mixin fix worked”** => log-backed target/application success and nearest runtime check
- **“the port is complete”** => build + datagen/tests + runtime-oriented validation

## Signoff contract

Before final signoff, provide:

1. **What changed**
2. **Which lane you used**
3. **What commands you ran**
4. **Which artifacts were collected**
5. **What each artifact proves**
6. **What remains unvalidated**

Do not sign off on behavior you did not actually exercise.

## Reference map

Open only the files relevant to the current lane:

- `references/repo-triage.md`
- `references/loader-selection.md`
- `references/new-mod-fabric.md`
- `references/new-mod-neoforge.md`
- `references/porting-version.md`
- `references/porting-loader.md`
- `references/mixin-guidelines.md`
- `references/crash-debugging.md`
- `references/testing-playbook.md`
- `references/artifacts-and-signoff.md`
- `references/multi-loader-multi-version.md`
- `references/compat-and-interop.md`
- `references/performance-work.md`
- `references/release-prep.md`
- `references/helper-tooling-spec.md`
