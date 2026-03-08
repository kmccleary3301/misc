# Loader porting playbook

Use this when adding or switching between Fabric and NeoForge.

## Start with a classification pass

Split the code mentally into:

### Likely common
- domain logic
- pure data models
- serialization helpers
- algorithmic code
- generated content definitions that are not loader-bound

### Likely platform-specific
- loader entrypoints
- registration idioms
- events/hooks
- Mixins / access transformers / wideners
- rendering glue
- networking glue
- config UIs and platform services
- compat hooks against platform-specific mods/APIs

## Decision order

1. direct port
2. separate branch
3. shared-core / multi-loader structure

That is the order of preference unless the product requirements clearly reverse it.

## Use FFAPI carefully

Forgified Fabric API can reduce friction on NeoForge by porting Fabric API concepts.
It is useful for interop.
It is **not** a full abstraction layer.
Expect loader-specific code to remain.

## Loader-port completion rule

Do not sign off on a loader port from compilation alone.

Minimum evidence:
- build
- nearest relevant tests/GameTests/datagen
- runtime-oriented artifact on the target loader
