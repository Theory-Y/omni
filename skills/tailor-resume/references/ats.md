# Passing ATS and AI screening

**ATS** (applicant tracking system): the software an employer uses to collect applications. It
extracts the text of a resume into fields, then ranks or filters candidates against the posting.
Many employers now add an AI reviewer that scores each resume against the posting's requirements.
A recruiter usually sees the top of the ranking and skims each resume for a few seconds.

A resume passes when three things hold: the parser reads it without errors, the posting's
requirements appear in its text with evidence, and nothing in it looks manipulated.

## 1. Parse cleanly

The shipped template already does this. Keep it that way.

- Single column. No tables, text boxes, images, icons, charts, or skill bars.
- Contact details are plain text in the body, first lines of the page.
- Section headings are the standard names from the hard rules in `SKILL.md`.
- Each role has a title, an employer, and dates in one format ("Jun 2025 - Aug 2025").
- The PDF holds real text. The build script confirms that headings extract in reading order.

## 2. Harvest the posting's keywords

Collect the terms a screener would score:

- the exact role title
- hard skills, tools, software, and languages
- methods and domain terms (variance analysis, incident response, due diligence)
- certifications, licenses, and degree names
- required years or levels of experience

Rank them. A term in the title, in the required qualifications, or repeated across the posting
outranks a term mentioned once under preferred qualifications.

## 3. Place each supported keyword

For every keyword the master resume supports:

- Use the posting's exact wording and spelling ("financial modelling" stays British when the
  posting writes it that way, "React.js" stays "React.js").
- Put it in a bullet beside the evidence, and once more in the skills block. Twice is enough.
  Repetition beyond that reads as stuffing to software and to people.
- Write the long form and the short form together on first use, such as "search engine
  optimization (SEO)". Screeners search for either one.
- Put the exact role title in the summary when the field uses a summary. Never change a job title
  the user actually held to match the posting.

A keyword the master does not support stays out. It goes in the briefing as a gap.

## 4. Answer every requirement in a quotable sentence

AI reviewers grade against a rubric built from the posting. They reward explicit evidence and mark
down vague claims, inflated titles, and dates that do not add up.

- Walk the match table. Each required qualification with support in the master maps to one
  sentence on the resume that a reviewer could quote as proof.
- Degree, graduation date, and required certifications appear in plain words.
- Years of experience are countable from the dates on the page.
- Titles, dates, and employers match the user's LinkedIn profile and the master. Tell the user
  when they differ.

## 5. Verify

Pass the harvested keywords to the build script:

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/build.py" "<file>.html" --keywords "term one, term two"
```

The script searches the text extracted from the PDF, which is what a parser sees. For each keyword
reported missing, either work it in honestly or list it as a gap in the briefing.

## 6. Screening questions

Application forms ask knockout questions (work authorization, sponsorship, degree, years of
experience, salary). Answer them from `profile.md`, truthfully. A resume cannot rescue a failed
knockout question. Tell the user when one is likely to fail.

## Refusals

Never add hidden or white text, keywords the candidate cannot back up, or instructions addressed to
an AI reviewer. Screening systems detect these and reject the application, and recruiters who find
them blacklist the candidate.
