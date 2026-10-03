#!/usr/bin/env python3
"""Render one resume or cover letter HTML file to PDF, then check it. Exit 1 on any error."""

import argparse
import html
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

PATH_NAMES = [
    "chromium", "chromium-browser", "google-chrome", "google-chrome-stable", "chrome",
    "brave-browser", "microsoft-edge", "microsoft-edge-stable", "msedge",
]
MAC_APPS = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
]
WIN_APPS = [
    r"Google\Chrome\Application\chrome.exe",
    r"Microsoft\Edge\Application\msedge.exe",
    r"Chromium\Application\chrome.exe",
    r"BraveSoftware\Brave-Browser\Application\brave.exe",
]
FLATPAK_IDS = [
    "org.chromium.Chromium", "com.google.Chrome",
    "io.github.ungoogled_software.ungoogled_chromium",
    "com.brave.Browser", "com.microsoft.Edge",
]

BANNED = {
    "—": "em dash", "–": "en dash", "‒": "figure dash", "―": "horizontal bar",
    ";": "semicolon", ":": "colon",
}
AI_TELLS = [
    "spearheaded", "spearhead", "utilize", "utilized", "utilizing", "synergy", "synergies", "delve", "tapestry", "testament", "passionate",
    "seamless", "seamlessly", "cutting-edge", "robust", "dynamic", "results-driven",
    "results-oriented", "detail-oriented", "fast-paced", "team player", "proven track record",
    "thrilled", "honed", "showcase", "showcasing", "underscore", "pivotal", "realm", "landscape",
    "foster", "fostered", "elevate", "harness", "unlock", "game-changing", "world-class",
    "i am writing to express", "i am confident", "perfect fit", "ideal candidate",
    "moreover", "furthermore", "additionally",
]
# finance terms (leveraged buyout, financial leverage) are not tells
LEVERAGE = r"(?<!financial )(?<!operating )leverag(?:e|ed|ing)\b(?! (?:buyout|finance|loan|ratio|recap))"


def find_browsers(folder):
    """Yield a command prefix for each installed Chromium-family browser."""
    for name in PATH_NAMES:
        path = shutil.which(name)
        if path:
            yield [path]
    for path in MAC_APPS:
        if os.path.exists(path):
            yield [path]
    for base in ("PROGRAMFILES", "PROGRAMFILES(X86)", "LOCALAPPDATA"):
        root = os.environ.get(base)
        for app in WIN_APPS if root else []:
            path = os.path.join(root, app)
            if os.path.exists(path):
                yield [path]
    if shutil.which("flatpak"):
        listed = subprocess.run(
            ["flatpak", "list", "--app", "--columns=application"],
            capture_output=True, text=True,
        ).stdout.split()
        for app in FLATPAK_IDS:
            if app in listed:
                # sandbox cannot write the PDF without access to the folder
                yield ["flatpak", "run", f"--filesystem={folder}", app]


def render(src, pdf, browser):
    """Print src to pdf with the first browser that works. Exits when none does."""
    pdf.unlink(missing_ok=True)  # a stale PDF must not pass the checks
    failures = []
    for prefix in [[browser]] if browser else find_browsers(src.parent):
        try:
            run = subprocess.run(
                prefix + [
                    "--headless", "--disable-gpu", "--no-pdf-header-footer",
                    "--print-to-pdf-no-header", f"--print-to-pdf={pdf}", src.as_uri(),
                ],
                capture_output=True, encoding="utf-8", errors="replace", timeout=120,
            )
            reason = run.stderr.strip()[-300:] or f"exit code {run.returncode}"
        except (OSError, subprocess.TimeoutExpired) as error:
            reason = str(error)
        if pdf.exists():
            return
        failures.append(f"{' '.join(prefix)}: {reason}")
    if not failures:
        sys.exit(
            "ERROR no Chromium-family browser found. Install Chrome, Chromium, Edge, or Brave, "
            "or pass --browser /path/to/browser."
        )
    sys.exit("ERROR no browser produced a PDF\n" + "\n".join(failures))


def visible_text(source):
    """HTML source to the text a reader sees. Colons closing a bold label are dropped."""
    text = re.sub(r"<(style|script|title)\b.*?</\1>", "", source, flags=re.S | re.I)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r":\s*</b>", "</b>", text)
    text = re.sub(r"<br\s*/?>|</(p|li|div|h1|h2)>", "\n", text, flags=re.I)
    text = re.sub(r"<[^>]+>", "", text)
    lines = (" ".join(line.split()) for line in html.unescape(text).splitlines())
    return [line for line in lines if line]


def pdf_text(pdf, first_page=None):
    """Extracted PDF text via pdftotext, or None when poppler is absent."""
    if not shutil.which("pdftotext"):
        return None
    cmd = ["pdftotext"] + (["-f", str(first_page)] if first_page else []) + [str(pdf), "-"]
    # utf-8 forced: Windows decodes with the locale codepage otherwise
    return subprocess.run(cmd, capture_output=True, encoding="utf-8", errors="replace").stdout


def squash(text):
    return " ".join(text.lower().split())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html", type=Path)
    parser.add_argument("--keywords", default="", help="comma-separated posting keywords")
    parser.add_argument("--browser", help="path to a Chromium-family browser")
    args = parser.parse_args()
    sys.stdout.reconfigure(errors="replace")  # Windows consoles cannot print every character

    src = args.html.resolve()
    pdf = src.with_suffix(".pdf")
    source = src.read_text(encoding="utf-8")
    errors, warnings = [], []

    if "{{" in source:
        errors.append("unfilled {{placeholder}} left in the HTML")

    render(src, pdf, args.browser)

    pages = len(re.findall(rb"/Type\s*/Page(?![A-Za-z])", pdf.read_bytes()))
    if pages != 1:
        errors.append(f"{pages} pages, must be 1")
        overflow = pdf_text(pdf, first_page=2)
        if overflow and overflow.strip():
            print("--- text past page 1 ---")
            print(overflow.strip())
            print("---")

    lines = visible_text(source)
    for line in lines:
        for char, name in BANNED.items():
            if char in line:
                errors.append(f"{name} in: {line[:90]}")
    body = squash(" ".join(lines))
    for phrase in AI_TELLS:
        if re.search(rf"(?<![a-z]){re.escape(phrase)}(?![a-z])", body):
            warnings.append(f"AI-sounding phrase: {phrase}")
    if re.search(LEVERAGE, body):
        warnings.append("AI-sounding phrase: leverage")

    extracted = pdf_text(pdf)
    if extracted is None:
        warnings.append("pdftotext not installed, PDF text order not verified (install poppler)")
        haystack = body
    else:
        haystack = squash(extracted)
        position = 0
        for heading in re.findall(r"<h2>(.*?)</h2>", source, flags=re.S | re.I):
            found = haystack.find(squash(html.unescape(heading)), position)
            if found < 0:
                errors.append(f"heading out of order or missing in PDF text: {heading}")
            else:
                position = found

    keywords = [k.strip() for k in args.keywords.split(",") if k.strip()]
    if keywords:
        missing = [k for k in keywords if squash(k) not in haystack]
        print(f"keywords {len(keywords) - len(missing)}/{len(keywords)} found")
        if missing:
            print("missing: " + ", ".join(missing))

    for item in warnings:
        print(f"WARN  {item}")
    for item in errors:
        print(f"ERROR {item}")
    print(f"{'FAIL' if errors else 'OK'}  {pdf.name}  pages={pages}")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
