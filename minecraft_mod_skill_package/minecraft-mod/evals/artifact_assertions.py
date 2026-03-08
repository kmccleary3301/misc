#!/usr/bin/env python3
"""
Simple artifact-policy checks for skill evals.

Usage:
    python evals/artifact_assertions.py .codex-mc/artifacts/latest
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)

def main() -> None:
    if len(sys.argv) != 2:
        fail("pass the artifact directory path")

    root = Path(sys.argv[1]).resolve()
    if not root.exists():
        fail(f"artifact root missing: {root}")

    manifest = root / "manifest.json"
    summary = root / "summary.md"

    if not manifest.exists():
        fail("manifest.json is missing")
    if not summary.exists():
        fail("summary.md is missing")

    data = json.loads(manifest.read_text(encoding="utf-8"))
    names = {entry["relative_path"] for entry in data.get("files", [])}

    if "doctor.json" not in names:
        fail("doctor.json missing")
    if not any(name in names for name in ("build.txt", "runtime-log.txt", "gametest.txt", "crash-summary.md")):
        fail("no meaningful validation artifact present")

    print("PASS: artifact structure looks sane")

if __name__ == "__main__":
    main()
