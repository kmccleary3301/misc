# Release prep

Use this when preparing a mod for release or a high-confidence handoff.

## Release posture

Be explicit about:
- supported loader(s)
- supported Minecraft version(s)
- what was validated
- what was not validated

## Checklist

1. verify metadata and mod id consistency
2. verify versioning inputs
3. rerun datagen if content/resources changed
4. run the highest relevant artifact ladder
5. verify build outputs and jar locations
6. confirm generated resource policy
7. collect artifacts
8. write a concise signoff summary

## Good release summary

A good summary states:
- supported targets
- exact checks run
- artifact paths
- known limitations
