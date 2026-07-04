# Git and GitHub Workflow

This repository should train Git muscle memory as much as coding muscle memory. Future employers should be able to read the history and understand steady progress.

## Daily Loop

Run these commands at the start of a session:

```powershell
git status
git branch --show-current
```

## First-Time Identity Check

Before the first commit, check the name and email Git will attach to your commits:

```powershell
git config --get user.name
git config --get user.email
```

If either value is missing or wrong, set it for this repository:

```powershell
git config user.name "YOUR NAME"
git config user.email "YOUR-GITHUB-EMAIL@example.com"
```

Use the email connected to the GitHub account you want future employers to see, or use GitHub's private no-reply email if you prefer not to expose a personal address.

During the session:

```powershell
git status --short
git diff
```

At the end of a completed unit of work:

```powershell
git add <files>
git commit -m "lesson-01: start python validation exercise"
git status
```

After a GitHub remote is connected:

```powershell
git push -u origin main
```

## Commit Standards

Good commits are small, honest, and explain one meaningful change.

Use messages like:

- `lesson-01: add python profile-card tests`
- `lesson-01: implement text validation`
- `lesson-01: record verification evidence`
- `curriculum: add git workflow`

Avoid messages like:

- `update`
- `stuff`
- `fix`
- `changes`

## What To Commit

Commit:

- Source code.
- Tests.
- Documentation.
- Evidence notes.
- Small scripts that help verification.

Do not commit:

- `.env` files.
- API keys or tokens.
- Virtual environments.
- Cache folders.
- Large generated artifacts unless they are intentionally part of the portfolio.

## First GitHub Setup

After creating the empty repository on GitHub, connect this local repo:

```powershell
git remote add origin https://github.com/YOUR-USERNAME/software-engineering-lab.git
git push -u origin main
```

Replace `YOUR-USERNAME` with the GitHub account name you created.

## Portfolio Rule

Every lesson should end with:

1. Working code or an honest blocker.
2. A test or verification command.
3. An updated evidence note.
4. A commit that tells the story clearly.
