# 04 · Build it yourself

This time there's no code to start from, only a description of what each
function should do. That's how real work arrives: as a requirement.

## Task

1. Open [`build.py`](build.py). Each function has a comment saying what it must do.
2. Before writing code, write the steps in plain English as comments.
   For example, for `biggest`:

   ```python
   # remember the first number as the biggest so far
   # go through each number
   #   if it's bigger than the biggest so far, remember it instead
   # give back the biggest so far
   ```

3. Turn those steps into code, one function at a time.
4. Check your work:

   ```powershell
   python exercises\04_build\check.py
   ```

5. Commit after each function passes.

## Stretch

Make a new file `expenses.py` in this folder. It should:

- keep asking "Amount spent?" until you press Enter on an empty line
- then print the total, the biggest expense, and how many were over 1000

Use your own functions from `build.py`, with `from build import biggest, count_over`.
There's no checker for this one. We'll review it together in the PR.

## Branch name

`ex-04-build`
