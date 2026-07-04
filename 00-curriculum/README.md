# Software Engineering Lab Curriculum

This lab exists to build real software engineering muscle memory. The long-term target is expert-level proficiency across Python, JavaScript, TypeScript, frontend engineering, full-stack systems, databases, APIs, applied AI, testing, debugging, deployment, and secure engineering practice.

Each lesson should train the habits of a strong engineer:

1. Working code.
2. Tests or checks that prove the behavior.
3. A short evidence note explaining what was built, what was verified, and what still needs work.
4. A small repetition loop that makes the skill easier to perform next time.
5. A clean Git commit that makes the progress understandable on GitHub.

## Training Principles

- Code before theory, then explain the code after it works.
- Build small pieces, test them, then improve them.
- Treat all external input as untrusted.
- Keep solutions simple enough to reason about and secure enough to defend.
- Practice the same core moves until they become automatic: read, edit, run, test, debug, document.
- Every module should produce portfolio evidence, not just notes.
- Git history should be readable by a future employer: small commits, clear messages, no secrets.

## GitHub Workflow

Use [git-github-workflow.md](git-github-workflow.md) to practice commits and GitHub publishing as part of every lesson.

## Current Lesson

Start here:

```powershell
Set-Location .\01-python-fundamentals\lesson-01
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\tools\check-environment.ps1
python -m unittest discover -s tests -v
```

If Python does not launch, fix the local Python installation before continuing. Lesson 1 uses only the Python standard library.

On this Windows machine, the reliable Python command found by the environment check is:

```powershell
C:\Users\akwue\AppData\Local\Python\bin\python.exe -m unittest discover -s tests -v
```

## Roadmap

- `01-python-fundamentals`: syntax, functions, validation, files, errors, testing, command-line tools.
- `02-javascript-typescript`: JavaScript fluency, TypeScript types, async code, package tooling.
- `03-react-frontend`: components, state, forms, accessibility, user experience.
- `04-nextjs-fullstack`: routing, server actions, data loading, production app structure.
- `05-supabase-postgres`: relational modeling, SQL, auth-aware data access, migrations.
- `06-apis-auth-realtime`: API design, authentication, authorization, realtime workflows.
- `07-applied-ai`: AI-assisted product features, prompt discipline, evaluation, safety.
- `08-testing-debugging-deployment`: automated testing, observability, deployment, incident-quality debugging.
