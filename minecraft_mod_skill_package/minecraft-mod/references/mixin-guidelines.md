# Mixin guidelines

Use this when writing, fixing, or reviewing Mixins.

## First principle

Mixins are a last-mile tool, not a default instinct.

Prefer:
1. existing loader/platform events or hooks
2. access wideners / access transformers / accessors / invokers
3. narrow injections
4. redirects only when necessary
5. overwrites only as a last resort

## Before editing a Mixin

Confirm:
- target class name under the current mappings
- method name and descriptor
- side (client/server/common)
- config file path
- refmap expectations
- `minVersion` or loader-specific requirements
- whether the failure is actually target drift, not a missing dependency or classloading issue

## Common failure buckets

- target not found
- invalid descriptor
- wrong environment side
- refmap/config mismatch
- priority / ordering conflicts
- local capture instability
- injector firing at the wrong phase
- actual bug elsewhere, Mixin only being blamed downstream

## Validation rule

For any Mixin change, gather at least one of:
- log excerpt proving successful target application
- exported / debug artifact where available
- nearest runtime or behavior validation artifact

Do not call a Mixin fix complete without evidence that the injection now resolves and the relevant behavior still works.
