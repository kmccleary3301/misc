# Evaluation rubric

## 1. Lane choice (0–5)
- 5: chose the simplest correct lane
- 3: eventually correct, but noisy or overcomplicated
- 0: wrong lane

## 2. Environment detection (0–5)
Did the agent correctly detect:
- loader
- Minecraft version
- mappings
- Java/toolchain
- available tasks
- repo shape

## 3. Architecture discipline (0–5)
- did **not** introduce multi-loader or multi-version complexity without a real reason
- respected the existing repo shape unless the task required a port

## 4. Artifact discipline (0–10)
Must-fail conditions:
- claimed runtime success with no runtime-oriented artifact
- claimed a port complete from build alone
- claimed visible behavior correct with no visual/state artifact when one was necessary
- changed generated resources without surfacing the diff

## 5. Technical correctness (0–10)
- changes fit the loader/version conventions of the repo
- Mixins were handled carefully
- compat boundaries stayed narrow
- validation matched the changed surface

## 6. Workspace improvement (0–5)
- bootstrap/tooling/artifact paths were improved safely when needed

## 7. Final signoff quality (0–5)
The final report should clearly state:
- what changed
- what commands ran
- what artifacts exist
- what each artifact proves
- what remains unvalidated
