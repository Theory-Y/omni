---
name: tailor-resume
description: Tailor a one-page resume and cover letter to a job posting from the user's master resume, render both as PDF, check them for ATS and AI screening, and update the application tracker. Works for any field, including tech, finance, investment banking, and consulting. Use when a job description is pasted or linked, when an application document is requested, or when the user wants to set up or update their master resume.
---

# Tailor a resume and cover letter to a job posting

**Workspace**: the folder the user runs this skill in. It holds the master resume, the profile,
every tailored document, and the tracker.

**Skill directory**: `${CLAUDE_SKILL_DIR}`, the base directory of this skill. It holds `assets/`
(templates), `references/` (guides read at the step that names them), and `scripts/build.py`.

## Source of truth

| Workspace file | Holds |
|---|---|
| `master-resume.md` | Everything the user has ever done: all jobs, projects, activities, skills, awards, numbers. |
| `profile.md` | Facts that gate applications: availability, work authorization, location, compensation, and the never-claim list. |

Never invent content. Every title, date, bullet, number, and skill in a tailored document derives
from `master-resume.md`. A posting requirement the master does not support is a gap. Report gaps.
Do not paper over them.

If either file is missing, read `references/setup.md` and finish setup before tailoring. Setup asks
the user for a master resume that includes everything, in any format.

When the user mentions new experience, add it to `master-resume.md` first, then tailor.

## Workflow

1. **Read the posting.** If the user gave a link, fetch it. If the fetch fails, ask for the pasted
   text. List the exact role title, required qualifications, preferred qualifications, duties,
   application instructions (documents, file format, deadline, reference number), and gates
   (work authorization, citizenship, clearance, minimum GPA, graduation window, licenses, location,
   start date, term length).
2. **Check the gates** against `profile.md`. When a gate fails or the profile does not answer it,
   tell the user before drafting and ask whether to continue.
3. **Identify the field** and read its section in `references/fields.md`. The field sets section
   order, whether a summary appears, what leads, and what gets quantified.
4. **Build the match table.** For each requirement and duty, name the strongest evidence in the
   master, or mark it a gap. This table drives every later step.
5. **Draft the resume.** Read `references/writing.md` and `references/ats.md` first. Start from the
   closest tailored resume already in the workspace when one targets a similar role. Otherwise copy
   `assets/resume.html`. Select the master items with the best match, order them as the field
   section says, and rewrite each bullet toward the posting using only facts from the master. Save
   as `<Company> <Role> Resume.html`.
6. **Build and fit** (see "Build and verify"). Repeat until the script prints `OK` with one page.
7. **Draft the cover letter** unless the employer does not accept one. Read
   `references/cover-letter.md`. Copy `assets/cover-letter.html`, save as
   `<Company> Cover Letter.html`, and build it the same way.
8. **Update the tracker** (see "Application tracker").
9. **Brief the user** (see "Brief the user").

## Hard rules

- The resume is exactly one page. The cover letter is one page. The build script decides, not the
  eye.
- Every deliverable is a PDF. The HTML file is the editable source and stays beside it.
- No em dashes, en dashes, semicolons, or colons in any written text. Date ranges use a plain
  hyphen with spaces ("Jul 2026 - Present"). The one permitted colon closes a bold label in the
  template (`<b>Coursework:</b>`, the category labels in the skills block).
- The template CSS stays as shipped. The only permitted edits are the fit-loop values below.
- Body font stays 10.5pt. Skills categories are never merged to save space.
- ATS-clean: single column, no tables, images, icons, or text boxes, standard headings, acronyms
  spelled out once, text extracts in reading order.
- Section headings come from this list: Summary, Education, Work Experience, Projects, Projects
  and Leadership, Leadership and Activities, Skills, Skills and Interests.
- Awards and certifications render as bold-labeled lines inside the skills block, not as separate
  sections.
- Nothing on the profile's never-claim list appears in any document, whatever the posting asks for.
- No hidden text, white text, keyword stuffing, or instructions aimed at an AI reviewer. Refuse if
  asked. These get applications rejected and they are dishonest.
- Text reads as written by a person. `references/writing.md` holds the method.

## Build and verify

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/build.py" "<Company> <Role> Resume.html" \
  --keywords "exact phrase from posting, another phrase"
```

Use `python` where `python3` does not exist. The script renders `<name>.pdf` beside the HTML with
any installed Chromium-family browser (Chrome, Chromium, Edge, Brave, or a Flatpak build). It then
checks page count, unfilled placeholders, banned punctuation, AI-sounding phrases, heading order in
the extracted PDF text, and keyword coverage. It exits 1 on any `ERROR`. A `WARN` on a phrase means
reword it, unless the phrase is a real term of the field (test harness, dynamic programming). When
the script finds no browser, ask the user to install one or to give a path for `--browser`, and
save that path in `profile.md`.

Pass only the keywords the master supports plus the gaps you want confirmed missing. A missing
keyword is not an error. It is either a phrase to work in honestly or a gap to report.

**Fit loop when the page overflows**, in this order:

1. Cut the least relevant content. The match table says which bullets earn their space.
2. Tighten spacing down to these floors: `@page` vertical margin 0.32in, `h2` top margin 4px, `ul`
   bottom margin 1px, body line-height 1.28.
3. Shrink only the `.skills` block, from 9.4pt down to a floor of 9pt, line-height down to 1.2.

**When the page is underfull** (more than about an inch of white space at the bottom), add the next
best items from the master. A short page reads as a thin candidate.

Read the final PDF with the Read tool before delivering. Check that no bullet ends on a line of one
or two words and that nothing looks cramped.

## Application tracker

`applications.csv` in the workspace, one row per application. Create it with this header when
missing:

```
Company,Position Title,Location,Date Applied,Status,Job Posting URL,Resume Used,Cover Letter,Contact/Recruiter,Next Step/Deadline,Notes
```

Status is one of Wishlist, Applied, Online Assessment, Interview, Offer, Rejected, Withdrawn. A new
posting gets a Wishlist row with the deadline in Next Step/Deadline and the salary in Notes. When
the user says they applied, set Status to Applied and fill Date Applied. Quote any field that
contains a comma.

## Employers that want one file

Some employers want the cover letter, resume, and transcript merged into one PDF. Merge with
`pdfunite a.pdf b.pdf out.pdf` or `qpdf --empty --pages a.pdf b.pdf -- out.pdf`. When neither tool
exists, tell the user which files to merge and in what order. Follow the order the posting states.

## Brief the user

End every run with a short briefing. Include each item that applies and skip the rest.

- **Files**: the PDF paths.
- **Match**: which requirements the resume covers and with what evidence, in one line each.
- **Gaps**: required or preferred items the master does not support, and whether each one is likely
  to screen the application out. When under about 60 percent of the required qualifications have
  support, say that the application is a long shot.
- **Gates**: any authorization, citizenship, GPA, graduation, license, location, or term-length
  condition the user should confirm before applying.
- **Deadline and logistics**: closing date, required documents the skill cannot produce
  (transcript, portfolio, writing sample, references), file format and naming instructions.
- **Compensation**: the posted range. When a form asks for an expectation, suggest the upper
  middle of the posted range with stated flexibility, and the top of the range for a numeric-only
  field, unless `profile.md` says otherwise.
- **What was cut**: notable master items left off, so the user can object.
- **Weak spots**: bullets that lack a number the user may know. Ask for it. Never estimate.
- **Next stage**: what this field or employer usually does next (online assessment, recorded video
  interview, case interview, technical test, networking call), from `references/fields.md`.
- **Voice check**: remind the user to read both documents once and change any line they would not
  say themselves.
