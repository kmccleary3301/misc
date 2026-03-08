# Loader and architecture selection

## Default bias

Choose the **simplest viable architecture**.

That usually means:

- single-loader
- single-version
- no shared-core build unless there is a real ongoing need

## Greenfield defaults

### Prefer Fabric when all are true
- the user did not name a loader
- no dependency or ecosystem constraint pushes NeoForge
- fast, lean iteration matters more than breadth
- the mod does not obviously need a multi-loader lifecycle now

### Prefer NeoForge when any are true
- the user explicitly asked for NeoForge
- the repo already is NeoForge
- key dependencies or examples are NeoForge-first
- the task is naturally aligned with NeoForge’s current APIs and run/test/data flows

## Porting choices

When asked to support another loader, choose among:

### 1. Direct port
Best when:
- only one loader target is needed at the end
- the codebase is not huge
- the work is bounded
- long-term dual maintenance is not the goal

### 2. Separate branch
Best when:
- there is temporary dual support
- divergence is expected to stay high
- shared build complexity is not worth it
- platform-specific rendering/mixin code dominates

### 3. Shared-core / multi-loader structure
Best when:
- supporting multiple loaders is a **product requirement**
- shared domain logic is substantial
- the team expects sustained maintenance across targets
- the release workflow benefits from one workspace

## Multi-version choices

Prefer a shared multi-version workspace only when:
- adjacent-version support is ongoing and expected
- the repo already wants a version matrix
- the maintenance cost is justified

Otherwise:
- port in place
- or use separate branches for materially divergent lines

## Stonecutter / Stonecraft / Architectury rule

Do not introduce this stack casually.

Use it only when:
- the repository truly wants one codebase across multiple loaders and/or versions
- the team accepts the build-system complexity
- the expected maintenance horizon is long enough to repay the setup cost
