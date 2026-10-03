# Omni

> [!WARNING]
> Read both PDFs before you send them. No tool can promise you pass screening. Each employer's
> software is different.

A plugin that writes a tailored resume and cover letter for each job you apply to. You give it one
long document listing everything you have ever done, then paste a job posting. It hands back two
one-page PDFs written for that posting. You talk to it in plain English. No coding is involved.

Runs on:

- **[Claude Code](https://claude.com/claude-code).** An AI assistant from Anthropic. Using it
  requires a paid Claude plan or API credits.
- **A web browser.** Chrome, Edge, Brave, or Chromium. Omni uses it to create the PDFs.
- **Python.** Most Mac and Linux computers have it. Windows users can get it from
  [python.org](https://www.python.org/downloads/).

## Pre-text

Most large employers use software, and often an AI reviewer, to rank resumes before a recruiter
reads them.

Each posting stresses different duties and names skills in its own words. One resume cannot match
every posting.

## Solution

`/omni:tailor-resume`

- **One master resume.** A private document listing everything you have ever done. Omni draws from
  it for every resume, so anything missing from it can never appear on one.

`Tailor my resume to this job: https://example.com/careers/analyst`

- **A one-page resume** as a PDF, built from your most relevant experience.
- **A one-page cover letter** as a PDF, built around the duties the posting stresses most.
- **A briefing.** The requirements you meet, the ones you do not, anything that could disqualify
  you, the deadline, and what the next hiring stage usually is.
- **A tracker row** in `applications.csv`, which opens in Excel or Google Sheets.

`Shorten the second bullet under my internship and bring back the case competition.`

- **Changes in plain words.** Omni rewrites the document and fits it back to one page.

## Team

- **Author.** [Lunear01](https://github.com/Lunear01)
- **Co-author.** [aier9500](https://github.com/aier9500)

> [!NOTE]
> Omni never adds a skill, a job, or a number you did not give it.

## How an application runs

1. **Setup, once.** Install Claude Code from [claude.com/claude-code](https://claude.com/claude-code).
   Create a folder for your job search and open Claude Code in it. Type these two lines, pressing
   Enter after each:

   ```
   /plugin marketplace add Theory-Y/omni
   /plugin install omni@omni
   ```

2. **Master resume.** Type `/omni:tailor-resume`. Give Omni a Word document, a PDF, old resumes, a
   LinkedIn export, or notes typed into the chat. If you have nothing written, Omni interviews you.
   Include every job, project, club, skill, certification, and award, even ones you would normally
   cut. Numbers matter most:

   > **Thin.** Helped with month-end accounting.
   >
   > **Useful.** Reconciled 38 vendor accounts during month-end close and found a $94,000 freight
   > overcharge that the company recovered.

3. **Profile.** Omni asks when you graduate, when you can start, where you are allowed to work,
   what pay you expect, and which skills you never want claimed. It saves everything in two plain
   text files, `master-resume.md` and `profile.md`. Edit them whenever something changes.
4. **Apply.** Paste the job posting, or a link to it. Omni checks whether anything disqualifies
   you, writes both documents, fits each to one page, adds the job to your tracker, and gives you
   the briefing.
5. **Review.** Read both PDFs. Ask for changes in plain words.
6. **Keep track.** Tell Omni when you apply or hear back, and it updates the tracker. Tell it about
   new experience too. It adds that to your master resume for every later application.

## Under the hood (high level)

- **Writing.** Plain verbs: built, ran, led, sold, fixed. Not "spearheaded" or "leveraged". Facts
  over adjectives: it shows a result and does not call you "passionate". No long dashes,
  semicolons, or colons in sentences.

  > **Before.** Spearheaded a robust reconciliation process; leveraged Excel to drive efficiency.
  >
  > **After.** Rebuilt the monthly reconciliation in Excel and cut preparation time from 3 days
  > to 1.

- **Cover letter.** Four short paragraphs: the role and your strongest link to it, your evidence,
  what sets you apart, and one true reason you want this employer.
- **Screening software.** The layout is one column with standard headings and no tables or images.
  The posting's own words sit beside what you did, wherever your experience matches. A final check
  reads the finished PDF the way screening software does.
- **Refusals.** Omni refuses to hide invisible text, list skills you do not have, or add
  instructions meant to trick an AI reviewer. Employers detect these and reject the application.
- **Fields.** The page looks the same in every field. The section order and the evidence change.
  Tech resumes open with a short summary. Finance, banking, and consulting resumes open with
  Education.

| Field | What Omni puts forward |
|---|---|
| Tech | What you built, who used it, and the tools, named the way the posting names them |
| Finance | Money you handled, accuracy, analysis, and certifications with their exact status |
| Investment banking | GPA, deals with their size, valuation work, and specific interests |
| Consulting | Problems you solved, people you led, and results with numbers |
| Everything else | The numbers your field trusts, such as sales against quota or funds raised |

Licensed under [MIT](LICENSE).
