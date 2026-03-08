# Runtime smoke

## Goal
Confirm the chosen runtime boots, the mod initializes, and no immediate fatal errors occur on the changed surface.

## Setup
- choose the nearest relevant profile: client / server / GameTest
- choose a timeout suitable for startup
- choose a log summary path

## Expected artifacts
- `runtime-log.txt`
- `log-tail.txt`
- `smoke-summary.md`

## Exit rule
Pass only if:
- no fatal patterns are detected
- and the runtime either exits cleanly or reaches the timeout without obvious startup failure

If the run times out, say so explicitly.
