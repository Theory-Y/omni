# ROADMAP: omni

TODO list + change log. Usage lives in `README.md`, rules in `skills/tailor-resume/SKILL.md`.

## Open TODOs

- [ ] **Real-path install test**: manifest passes `claude plugin validate`. Install through
  `/plugin marketplace add` once and run a full tailoring from an empty workspace.
- [ ] **macOS and Windows render test**: `build.py` browser detection is tested only on Linux with
  Flatpak Chromium.
- [ ] **Template label colons**: bold labels keep their colon (`Coursework:`). Decide whether the
  no-colon rule should remove these too.

## Changes

- 2026-10-03: Published to `github.com/Theory-Y/omni` under MIT.
- 2026-10-03: README rewritten for outside readers: first-run guide, field table, screening
  method, troubleshooting, privacy, limits.
- 2026-10-03: First version. Generalized the personal `tailor-resume` skill into a plugin: master
  resume and profile setup, field conventions, writing and ATS references, cover letter strategy,
  CSV tracker, cross-platform `build.py`.
