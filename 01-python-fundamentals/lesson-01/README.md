# Lesson 1: Python Fundamentals

## Goal

Implement a small profile-card module using secure input handling and test-driven development.

You will edit:

- `src/profile_card.py`

You will verify with:

- `python -m unittest discover -s tests -v`

## First Checkpoint

Run the environment check:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\tools\check-environment.ps1
```

If it reports that Python is not available, install or repair Python first. Use Python 3.11 or newer for this lab.

## Exercise

Implement the TODOs in `src/profile_card.py` until every test passes.

Required behavior:

- Names, roles, and cities must be strings.
- Leading and trailing whitespace must be removed.
- Repeated internal whitespace must collapse to one space.
- Blank values must raise `ValueError`.
- Control characters must raise `ValueError`.
- Names must be title-cased.
- Ages must accept integers or digit-only strings.
- Boolean ages must be rejected, even though `bool` is an `int` subclass in Python.
- Ages must be between `0` and `130`, inclusive.
- `build_profile_card` must return a deterministic dictionary with a readable summary.

Security rule for this lesson: do not use `eval`, `exec`, subprocesses, network calls, or file reads to solve the exercise.

## Done Means

1. The environment check passes.
2. The unit tests pass.
3. The evidence note at `../../portfolio-evidence/lesson-01.md` is updated.
