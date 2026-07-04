# Lesson 1 Plan: Python Fundamentals

## Outcome

Build small, secure Python functions that validate user input and return predictable profile data.

## Muscle Memory Target

Practice the core Python loop: write a function, run a focused unit test, read the failure, adjust the code, and repeat until the behavior is correct.

## Engineering Focus

- Use clear function boundaries.
- Validate untrusted input before using it.
- Prefer deterministic behavior that can be tested.
- Avoid risky shortcuts such as `eval`, shelling out, or hidden global state.
- Learn the difference between `TypeError` for the wrong kind of value and `ValueError` for the wrong value.

## Completion Criteria

- `tools/check-environment.ps1` finds a working Python launcher.
- `python -m unittest discover -s tests -v` passes from `01-python-fundamentals/lesson-01`.
- `portfolio-evidence/lesson-01.md` is updated with the final test command and result.
