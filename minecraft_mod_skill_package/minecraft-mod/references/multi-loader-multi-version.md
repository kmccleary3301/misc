# Multi-loader and multi-version guidance

This document exists to stop unnecessary complexity.

## Default answer

Do **not** introduce multi-loader or multi-version infrastructure by default.

## When shared-core structure is justified

Use Stonecutter / Stonecraft / Architectury-style structure only when:
- supporting multiple loaders and/or versions is a real product requirement
- shared code is substantial and expected to stay substantial
- the team will actually maintain the workspace long-term
- unified build and publishing flows materially help

## When not justified

Avoid it when:
- the task is a one-off port
- support horizon is unclear
- platform divergence is already high
- rendering, Mixins, and platform hooks dominate
- the repo is small enough that direct ports are cheaper

## Common mistake

“Future-proofing” a small mod by building the most complex workspace first.

That is often the wrong trade.
