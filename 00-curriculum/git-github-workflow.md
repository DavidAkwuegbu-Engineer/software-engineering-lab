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

## Repository Not Found

If `git push -u origin main` returns:

```text
remote: Repository not found.
fatal: repository 'https://github.com/.../software-engineering-lab.git/' not found
```

Check these in order:

1. The repository exists on GitHub.
2. The URL uses your exact GitHub username, not your display name.
3. The repository name matches exactly: `software-engineering-lab`.
4. You are signed in to the GitHub account that owns the repository.
5. If the URL is wrong, fix it instead of adding another `origin`:

```powershell
git remote set-url origin https://github.com/YOUR-USERNAME/software-engineering-lab.git
git remote -v
git push -u origin main
```

For a brand-new learning repo, create it empty on GitHub first. Do not add a README, `.gitignore`, or license on GitHub if those files already exist locally.

## Permission Denied To Another Account

If `git push -u origin main` returns:

```text
remote: Permission to YOUR-USERNAME/software-engineering-lab.git denied to OTHER-ACCOUNT.
fatal: unable to access 'https://github.com/YOUR-USERNAME/software-engineering-lab.git/': The requested URL returned error: 403
```

GitHub found the repository, but Git authenticated with the wrong GitHub account. Commit identity and push identity are separate:

- `git config user.name` controls the name written into commits.
- Git Credential Manager controls which GitHub account is used when pushing.

Check the current local commit identity:

```powershell
git config --get user.name
git config --get user.email
```

Then remove the wrong cached GitHub login and sign in with the account that owns the repository:

```powershell
git credential-manager github logout OTHER-ACCOUNT
git credential-manager github login
git push -u origin main
```

Replace `OTHER-ACCOUNT` with the account shown in the error message.

## Portfolio Rule

Every lesson should end with:

1. Working code or an honest blocker.
2. A test or verification command.
3. An updated evidence note.
4. A commit that tells the story clearly.
