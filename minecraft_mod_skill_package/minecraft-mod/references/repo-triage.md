# Repo triage

Use this when dropped into an unfamiliar Minecraft mod workspace.

## Objective

Before making significant edits, be able to answer:

- What loader(s) does this repo target?
- Which Minecraft version(s) does it target?
- Which mappings does it use?
- Which Java/toolchain version does it require?
- Which tasks exist for build, client, server, datagen, tests, and GameTests?
- Where do runtime logs and crash reports land?
- Does the repo already have deterministic helpers or artifact paths?
- Is the architecture single-loader, multi-loader, single-version, or multi-version?

## Fast checklist

1. Run `mc-doctor`.
2. Inspect:
   - `settings.gradle*`
   - `build.gradle*`
   - `gradle.properties`
   - `src/main/resources/fabric.mod.json`
   - `src/main/resources/META-INF/neoforge.mods.toml`
   - any Mixin config files
3. Identify the build plugins:
   - Fabric Loom
   - ModDevGradle / NeoGradle
   - Architectury
   - Stonecutter / Stonecraft
4. Identify the validation path:
   - build task
   - datagen task
   - GameTest task
   - test task
   - client/server run tasks
5. Identify risk surfaces:
   - Mixins
   - custom registries
   - block entities / renderers
   - networking
   - config migration
   - datagen / generated resource drift
   - compat shims

## Stop signs

Do not launch into sweeping edits when any of these are still unknown:

- loader / version
- mappings
- test or smoke path
- whether generated outputs are committed
- where crash reports/logs are written

## Good outputs from triage

At the end of triage, you should be able to state:

- lane chosen
- narrowest first validation command
- likely artifact paths
- whether you need to bootstrap local helpers
