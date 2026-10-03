# Setup: master resume and profile

Run once per workspace, and again whenever the user wants to rebuild their master resume.

## 1. Ask for the master resume

Ask the user for a master resume that includes everything they have ever done. Say this plainly,
because most people hand over their latest one-page resume instead:

- every job, internship, contract, and part-time or unrelated role
- every project, including class, personal, research, and competition work
- every club, team, volunteer role, and leadership position
- every skill, tool, language, certification, license, and test score
- every award, scholarship, publication, and presentation
- every number they remember: money, percentages, volumes, team sizes, rankings

The master is never sent to anyone. Longer is better. Three pages is normal and ten is fine.

Accept any form: `.docx`, `.pdf`, `.md`, `.txt`, pasted text, a LinkedIn profile export, or several
old resumes to merge. When the user has nothing written, copy `assets/master-resume.md` into the
workspace for them to fill in, or interview them section by section using that file as the script.

## 2. Convert it to `master-resume.md`

Write the content into `master-resume.md` in the workspace, following the section layout of
`assets/master-resume.md`. Leave the user's original file untouched.

- Read PDFs with the Read tool. Convert `.docx` with
  `soffice --headless --convert-to txt:Text <file>` when LibreOffice exists. Otherwise unzip the
  file and read the text runs in `word/document.xml`.
- Keep every item, every number, and the user's own wording. Do not polish, merge, or drop
  anything. Tailoring happens later, per posting.
- When sources disagree (two dates for one job, two titles), ask the user which is correct.

## 3. Fill the holes

Review the converted master and ask about what is missing, in one batch of questions:

- roles without start and end months, employer, or location
- bullets without a number where one plausibly exists
- tools and methods used but not named
- the commonly forgotten items: part-time jobs, tutoring, case competitions, hackathons, athletics,
  spoken languages, GPA, test scores, certifications in progress, interests

For finance and banking candidates, also ask for each deal, transaction, or model they worked on,
with its size and their part in it.

Record the answers in `master-resume.md`. Leave a number out when the user does not know it. Never
estimate one.

## 4. Build `profile.md`

Copy `assets/profile.md` into the workspace and fill it by asking the user. Ask about every
section: status, availability, work authorization, location, target fields, compensation, the
never-claim list, and voice.

The never-claim list needs a direct question. Ask which tools or skills the user has touched too
lightly to defend in an interview. Those go on the list.

When the user has a cover letter or other text they wrote alone, save its path under Voice and
match its tone in later letters.

## 5. Confirm

Tell the user what the master now holds (counts of roles, projects, and skills) and which facts in
the profile are still blank. Then continue with the posting, if one was given.
