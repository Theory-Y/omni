# ROADMAP: omni

TODO list + change log. Usage lives in `README.md`, rules in `skills/tailor-resume/SKILL.md`.

## Open TODOs

- [ ] **Chromium on the GitHub Ubuntu runner**: `/usr/bin/chromium` printed no PDF there. Cause
  not investigated (sandbox restriction suspected). `build.py` falls through to the next installed
  browser, and Chrome worked. A machine with only that Chromium gets the browser's error text.

## Changes

- 2026-10-03: README restructured to the TheoryY Workflow layout: Pre-text, Solution, Team, run
  steps, Under the hood. Credits Lunear01 as author and aier9500 as co-author.
- 2026-10-03: `render-test` workflow runs `tests/test_build.py` on Linux, macOS, and Windows. All
  three pass. `build.py` now tries every installed browser and prints each failure reason.
- 2026-10-03: Install from GitHub verified (`omni@omni` 0.1.0 at `99d5411`). Full tailoring run
  from an empty workspace produced both PDFs, the tracker row, and the briefing.
- 2026-10-03: 0.1.1. Cover letters may not invent anecdotes or personal details. Runs leave no
  temporary files in the workspace.
- 2026-10-03: Decided: bold template labels keep their colon.
- 2026-10-03: README rewritten for non-technical job seekers: step-by-step setup and examples.
  Developer details removed.
- 2026-10-03: Published to `github.com/Theory-Y/omni` under MIT.
- 2026-10-03: README rewritten for outside readers: first-run guide, field table, screening
  method, troubleshooting, privacy, limits.
- 2026-10-03: First version. Generalized the personal `tailor-resume` skill into a plugin: master
  resume and profile setup, field conventions, writing and ATS references, cover letter strategy,
  CSV tracker, cross-platform `build.py`.
