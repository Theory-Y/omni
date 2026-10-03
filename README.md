# Omni

Omni writes a tailored resume and cover letter for each job you apply to. You give it one long
document listing everything you have ever done, then paste a job posting. It hands back two
one-page PDFs written for that posting.

It runs inside [Claude Code](https://claude.com/claude-code), an AI assistant from Anthropic. You
talk to it in plain English. No coding is involved.

## What you get for each job

- **A one-page resume** as a PDF, built from your most relevant experience.
- **A one-page cover letter** as a PDF, built around the duties the posting stresses most.
- **A briefing**: the requirements you meet, the ones you do not, anything that could disqualify
  you, the deadline, and what the next hiring stage usually is.
- **A tracker row** in `applications.csv`, which opens in Excel or Google Sheets.

Omni never adds a skill, a job, or a number you did not give it.

## What you need

- **Claude Code.** Using it requires a paid Claude plan or API credits.
- **A web browser.** Chrome, Edge, Brave, or Chromium. Omni uses it to create the PDFs.
- **Python.** Most Mac and Linux computers have it. Windows users can get it from
  [python.org](https://www.python.org/downloads/).

## Setup

You do this once.

1. Install Claude Code from [claude.com/claude-code](https://claude.com/claude-code).
2. Create a folder for your job search and open Claude Code in it.
3. Type these two lines, pressing Enter after each:

   ```
   /plugin marketplace add Theory-Y/omni
   /plugin install omni@omni
   ```

## Step 1. Your master resume

A master resume is a private document listing everything you have ever done. Omni draws from it
for every resume, so anything missing from it can never appear on one.

Type `/omni:tailor-resume`. Omni asks for your master resume. Give it a Word document, a PDF, old
resumes, a LinkedIn export, or notes typed into the chat. If you have nothing written, Omni
interviews you.

Include every job, project, club, skill, certification, and award, even ones you would normally
cut. Numbers matter most:

> **Thin.** Helped with month-end accounting.
>
> **Useful.** Reconciled 38 vendor accounts during month-end close and found a $94,000 freight
> overcharge that the company recovered.

Omni then asks when you graduate, when you can start, where you are allowed to work, what pay you
expect, and which skills you never want claimed. It saves everything in two plain text files,
`master-resume.md` and `profile.md`. Edit them whenever something changes.

## Step 2. Apply to a job

Paste the job posting, or a link to it:

```
Tailor my resume to this job: https://example.com/careers/analyst
```

Omni checks whether anything disqualifies you, writes both documents, fits each to one page, adds
the job to your tracker, and gives you the briefing.

Read both PDFs before sending them. Ask for changes in plain words:

```
Shorten the second bullet under my internship and bring back the case competition.
```

## Step 3. Keep track

Tell Omni when you apply or hear back, and it updates the tracker. Tell it about new experience
too. It adds that to your master resume for every later application.

## Fields

The page looks the same in every field. The section order and the evidence change.

| Field | What Omni puts forward |
|---|---|
| Tech | What you built, who used it, and the tools, named the way the posting names them |
| Finance | Money you handled, accuracy, analysis, and certifications with their exact status |
| Investment banking | GPA, deals with their size, valuation work, and specific interests |
| Consulting | Problems you solved, people you led, and results with numbers |
| Everything else | The numbers your field trusts, such as sales against quota or funds raised |

Tech resumes open with a short summary. Finance, banking, and consulting resumes open with
Education.

## How it writes

- **Plain verbs.** Built, ran, led, sold, fixed. Not "spearheaded" or "leveraged".
- **Facts over adjectives.** It shows a result. It does not call you "passionate".
- **Simple punctuation.** No long dashes, semicolons, or colons in sentences.

> **Before.** Spearheaded a robust reconciliation process; leveraged Excel to drive efficiency.
>
> **After.** Rebuilt the monthly reconciliation in Excel and cut preparation time from 3 days to 1.

The cover letter has four short paragraphs: the role and your strongest link to it, your evidence,
what sets you apart, and one true reason you want this employer.

## Getting past screening software

Most large employers use software, and often an AI reviewer, to rank resumes before a recruiter
reads them. Omni handles this in three ways:

- **A layout the software can read.** One column, standard headings, no tables or images.
- **The posting's own words**, placed beside what you did, wherever your experience matches.
- **A final check** that reads the finished PDF the way screening software does.

Omni refuses to hide invisible text, list skills you do not have, or add instructions meant to
trick an AI reviewer. Employers detect these and reject the application.

No tool can promise you pass. Each employer's software is different.
