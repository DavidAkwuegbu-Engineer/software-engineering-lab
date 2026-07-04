# Lesson 1 Evidence

Date started: 2026-07-04

## Goal

Implement `src/profile_card.py` so it validates untrusted input and passes the Lesson 1 unit tests.

## Learning Goal

Build Python muscle memory by implementing small functions, running tests, reading failures, and tightening the solution with secure input validation.

## Verification Log

- Environment check: ran with `powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\tools\check-environment.ps1`; passed by finding `C:\Users\akwue\AppData\Local\Python\bin\python.exe` running Python 3.14.3.
- Unit tests: passed with `C:\Users\akwue\AppData\Local\Python\bin\python.exe -m unittest discover -s tests -v`.

## Notes

- The current Windows shell still exposes broken WindowsApps aliases for `python`, `py`, and `python3`; use the Python Install Manager shim until PATH/app aliases are cleaned up.
- Git is now initialized for this lab, with `main` as the portfolio branch.
