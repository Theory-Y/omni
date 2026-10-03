"""Render test for build.py. The sample must pass. A broken copy must fail."""

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "skills" / "tailor-resume" / "scripts" / "build.py"


def build(html, *extra):
    run = subprocess.run(
        [sys.executable, str(BUILD), str(html), *extra],
        capture_output=True, encoding="utf-8", errors="replace",
    )
    return run.returncode, run.stdout + run.stderr


with tempfile.TemporaryDirectory(dir=ROOT / "tests") as tmp:
    good = Path(tmp) / "Sample Resume.html"  # space in the name is deliberate
    shutil.copy(ROOT / "tests" / "sample-resume.html", good)
    code, out = build(good, "--keywords", "discounted cash flow, Capital IQ, pitch book")
    print(out)
    assert code == 0, "sample should pass"
    assert "pages=1" in out and "keywords 2/3 found" in out
    assert good.with_suffix(".pdf").stat().st_size > 10_000

    bad = Path(tmp) / "bad.html"
    filler = "<p>Broken; on purpose.</p>" + "<p>Filler past the page limit.</p>" * 60
    bad.write_text(good.read_text(encoding="utf-8") + filler, encoding="utf-8")
    code, out = build(bad)
    print(out[-300:])
    assert code == 1, "broken copy should fail"
    assert "pages, must be 1" in out and "ERROR semicolon" in out

print("PASS")
