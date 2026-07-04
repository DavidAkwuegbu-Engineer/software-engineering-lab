# Lesson 1 Evidence

Date started: 2026-07-04

## Goal

Implement `src/profile_card.py` so it validates untrusted input and passes the Lesson 1 unit tests.

## Learning Goal

Build Python muscle memory by implementing small functions, running tests, reading failures, and tightening the solution with secure input validation.

## Verification Log

- Environment check: ran with `powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\tools\check-environment.ps1`; failed because `python`, `py`, and `python3` point to Windows launcher aliases that did not launch.
- Unit tests: not run because no working Python launcher is available.

## Notes

- The current Windows shell exposes Python launcher aliases, but they did not launch during setup.
- Next step: install or repair Python 3.11+, then run `python -m unittest discover -s tests -v` from `01-python-fundamentals/lesson-01`.
- Git is now initialized for this lab, with `main` as the portfolio branch.
