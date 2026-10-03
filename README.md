# Omni

A Claude Code plugin that turns a job posting into a tailored one-page resume and cover letter,
both as PDF. It works from your master resume, follows the conventions of the field you are
applying to, checks the result against resume screening software, and tracks every application.

**Master resume**: one long file holding everything you have ever done. Each tailored resume picks
from it. Nothing outside it ever appears on a resume.

**ATS** (applicant tracking system): the software employers use to parse and rank resumes before a
person reads them.

## What you get per posting

| File | Content |
|---|---|
| `<Company> <Role> Resume.pdf` | One-page resume tailored to the posting |
| `<Company> Cover Letter.pdf` | One-page cover letter built from the posting's duties |
| Matching `.html` files | Editable sources of both PDFs |
| `applications.csv` | A tracker row with status, deadline, and salary |

Each run ends with a briefing:

- which requirements your resume covers, and with what evidence
- which requirements you do not meet, and whether they are likely to screen you out
- eligibility conditions to confirm (work authorization, GPA minimum, graduation window, license)
- the deadline, plus documents the employer wants that the plugin cannot produce
- the posted salary range and how to answer a salary question
- what was left off the resume
- what the next hiring stage usually is

## Requirements

| Need | Notes |
|---|---|
| [Claude Code](https://claude.com/claude-code) | The plugin runs inside it. |
| Python 3 | Runs the build script. No packages to install. |
| A Chromium-family browser | Chrome, Chromium, Edge, or Brave. Renders the PDF. Flatpak builds work. |
| poppler (optional) | Provides `pdftotext`. With it, the check reads the PDF the way an ATS parser does. |

## Install

In Claude Code:

```
/plugin marketplace add Theory-Y/omni
/plugin install omni@omni
```

To try it without installing, clone the repository and start Claude Code with
`claude --plugin-dir /path/to/omni`.

## First run: your master resume

1. Make a folder for your job search and start Claude Code in it.
2. Run `/omni:tailor-resume`.
3. Hand over your master resume when asked. Any format works: Word, PDF, plain text, a LinkedIn
   export, or several old resumes to merge.

Put everything in it. The master is never sent to an employer, so length does not matter:

- every job, internship, contract, and part-time or unrelated role
- every project, including class, personal, research, and competition work
- every club, team, volunteer role, and leadership position
- every skill, tool, language, certification, license, and test score
- every award, scholarship, and publication
- every number you remember: money, percentages, volumes, team sizes, rankings

No master resume yet? The plugin gives you a form to fill in, or interviews you section by section.

The plugin then asks a few questions and saves two files in your folder:

| File | Holds |
|---|---|
| `master-resume.md` | Your full history, in your own wording |
| `profile.md` | Availability, work authorization, location, compensation, and the skills you do not want claimed |

Edit either file by hand at any time. When you gain new experience, tell the plugin or add it to
`master-resume.md` yourself.

## Every application after that

Paste a job posting or a link to one. Examples:

```
Tailor my resume to this posting: <link>
```

```
Here is a job description. Resume and cover letter please.
<pasted text>
```

```
I applied to the Acme analyst role today.
```

The last one updates the tracker.

## Fields

The template and the one-page limit stay the same in every field. Section order, the summary, and
what counts as proof change.

| Field | Sections | What leads |
|---|---|---|
| Tech | Summary, Education, Work Experience, Projects and Leadership, Skills | Shipped systems, scale, tools named as the posting names them |
| Finance | Education, Work Experience, Leadership and Activities, Skills and Interests | Money handled, accuracy, analysis, certifications with exact status |
| Investment banking | Education, Work Experience, Leadership and Activities, Skills and Interests | GPA, transaction experience with deal size, valuation work |
| Consulting | Education, Work Experience, Leadership and Activities, Skills and Interests | Impact and leadership with measured results |
| Anything else | Derived from the posting | The numbers that field trusts (quota, patients, campaigns, funds raised) |

## Rules the plugin enforces

- **One page** per document. The build script counts the pages.
- **PDF output** every time.
- **No invented content.** Every title, date, number, and skill comes from your master resume. A
  requirement you do not meet is reported as a gap.
- **Punctuation.** No em dashes, en dashes, semicolons, or colons in written text. The colon after
  a bold label (`Coursework:`, skills categories) belongs to the template and stays.
- **Plain wording.** The build script warns on phrases that read as AI-written, such as
  "spearheaded" and "passionate".
- **Never-claim list.** Skills you list in `profile.md` stay off every document, whatever the
  posting asks for.

## How screening is handled

The resume template is a single column of real text with standard headings, which ATS parsers read
without errors. For each posting the plugin:

1. Collects the posting's keywords: role title, tools, methods, certifications.
2. Places each one your master resume supports, in the posting's exact wording, beside the evidence.
3. Extracts the text from the finished PDF and confirms each keyword is there.
4. Reports the keywords you cannot honestly claim.

The plugin refuses hidden text, white text, keyword stuffing, and instructions aimed at AI
reviewers. Screening systems detect these and reject the application.

No tool can promise a pass. Screening software differs by employer, and no writing style beats
every AI-writing detector. Read both documents once before sending and change any line you would
not say yourself.

## Editing a document by hand

Edit the `.html` file, then rebuild:

```
python3 /path/to/omni/skills/tailor-resume/scripts/build.py "Acme Analyst Resume.html" --keywords "variance analysis, SQL"
```

The script writes the PDF beside the HTML and prints `OK` or a list of errors. It exits 1 when the
page count is not 1, a placeholder is unfilled, banned punctuation appears, or headings extract
out of order. `--keywords` is optional.

## Troubleshooting

| Problem | Fix |
|---|---|
| `no Chromium-family browser found` | Install Chrome, Chromium, Edge, or Brave, or pass `--browser /path/to/browser`. |
| `python3` not found (Windows) | Use `python` instead. |
| `pdftotext not installed` warning | Install poppler. The build still works without it, with a weaker text check. |
| Resume runs to two pages | Ask the plugin to refit. It cuts the least relevant content first, then tightens spacing within fixed limits. |
| A keyword is reported missing | Your master resume does not support it. Add the experience to `master-resume.md` if you have it. |

## Privacy

The plugin makes no network calls of its own and stores nothing outside your folder. Claude Code
reads your files to do the work, as it does for any file in a session.

## Limits

- Output is always one page. Academic CVs, some government applications, and senior executive
  resumes run longer by convention. The plugin tells you when that applies.
- The template follows United States and Canadian practice: no photo, age, or marital status.
- PDF rendering is tested on Linux. macOS and Windows browser detection is written but untested.

## Layout

| Path | Purpose |
|---|---|
| `.claude-plugin/` | Plugin and marketplace manifests |
| `skills/tailor-resume/SKILL.md` | Workflow and hard rules |
| `skills/tailor-resume/assets/` | Resume and cover letter templates, master resume and profile forms |
| `skills/tailor-resume/references/` | Setup, field conventions, writing style, ATS method, cover letter strategy |
| `skills/tailor-resume/scripts/build.py` | Renders HTML to PDF and runs the checks |
| `ROADMAP.md` | Open TODOs and change log |

To add a field or change a convention, edit `skills/tailor-resume/references/fields.md`.

## License

MIT. See `LICENSE`.
