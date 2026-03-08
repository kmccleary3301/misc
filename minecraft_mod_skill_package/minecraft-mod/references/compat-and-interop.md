# Compat and interop

Use this when adding compatibility with another mod or platform-specific system.

## Distinguish three cases

### 1. Soft compat
The other mod may or may not be present.
Goal:
- guard behavior
- avoid hard crashes
- integrate when available

### 2. Hard dependency
The other mod is required.
Goal:
- make the dependency contract explicit
- validate boot/runtime with it enabled

### 3. Cross-loader interop
Goal:
- preserve shared behavior where practical
- isolate platform-specific code where necessary

## General rules

- detect the other mod/platform first
- keep compat boundaries narrow
- avoid leaking optional compat everywhere
- prefer feature detection and clear guards
- validate with the dependency actually enabled whenever possible

## FFAPI rule

Forgified Fabric API can help preserve familiar Fabric APIs on NeoForge.
Use it as interop support, not a promise that platform differences disappear.

## Compat signoff

Do not claim compat is fixed without:
- evidence with the compat path enabled
- and a clear statement of what was actually exercised
