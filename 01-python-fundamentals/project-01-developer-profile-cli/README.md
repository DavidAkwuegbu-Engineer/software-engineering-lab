# Project 1: Developer Profile CLI

## Goal

Build a Python command-line app that creates, validates, saves, and displays a developer profile suitable for a portfolio workflow.

This is the first real project in the lab. It should still be small, but it should feel like software:

- clear source files
- tests
- validation
- JSON persistence
- a CLI entry point
- evidence notes
- clean commits

## Milestone 1: Data Model and Validation

Implement the TODOs in:

- `src/developer_profile/model.py`

Run:

```powershell
$env:PYTHONPATH = "src"
C:\Users\akwue\AppData\Local\Python\bin\python.exe -m unittest discover -s tests -v
```

Milestone 1 is complete when every active test passes.

### How To Work Through Milestone 1

Do not try to solve all 16 tests at once. Use this order:

1. Implement `clean_text`.
2. Run the tests.
3. Implement `normalise_name`.
4. Run the tests.
5. Implement `normalise_skill`.
6. Run the tests.
7. Implement `parse_skills`.
8. Run the tests.
9. Implement `normalise_github_username`.
10. Run the tests.
11. Implement `build_developer_profile`.
12. Run the full test suite.

Focused command for the first step:

```powershell
$env:PYTHONPATH = "src"
C:\Users\akwue\AppData\Local\Python\bin\python.exe -m unittest tests.test_model.CleanTextTests -v
```

## Milestone 2: JSON Storage

Implement:

- `src/developer_profile/storage.py`

The app should save profiles as readable JSON and load them back without losing data.

## Milestone 3: CLI

Implement:

- `src/developer_profile/cli.py`

Target usage:

```powershell
$env:PYTHONPATH = "src"
C:\Users\akwue\AppData\Local\Python\bin\python.exe -m developer_profile.cli create --name "David Akwuegbu" --role "Software Engineer" --skills "Python, Git, Testing" --goal "Build secure portfolio projects"
```

## Security Rules

- Treat every CLI argument as untrusted input.
- Do not use `eval` or `exec`.
- Do not shell out to other programs.
- Do not write outside the project unless the user explicitly provides a safe path.
- Validate before saving.

## Commit Plan

Use one commit per milestone:

```powershell
git add .
git commit -m "project-01: scaffold developer profile cli"
git push
```

Then:

```powershell
git commit -m "project-01: implement profile validation"
git commit -m "project-01: add json profile storage"
git commit -m "project-01: add developer profile cli"
```
