# 03 · Fix the bug

[`bugs.py`](bugs.py) has six small functions. Each one has **one** bug.
Most real programming work looks like this: reading code someone else wrote
and working out why it does the wrong thing.

## Task

1. Run the checker and read what fails:

   ```powershell
   python exercises\03_fix_the_bug\check.py
   ```

2. Pick one FAIL line. Find that function in `bugs.py`.
3. Before changing anything, explain to yourself **why** it gives the wrong answer.
4. Fix it, save, and run the checker again.
5. **Commit after each fix**, so your PR has six small commits, for example
   `Fix count_to so it includes n`.

## Hints (only if stuck)

<details><summary>count_to</summary>What is the last number <code>range(1, n)</code> gives you?</details>
<details><summary>can_vote</summary>Is 18 greater than 18?</details>
<details><summary>add_typed</summary>Look back at <code>p3</code> in exercise 02.</details>
<details><summary>average</summary>Does every list have 3 numbers? There's a built-in that counts items in a list.</details>
<details><summary>greeting</summary>Python checks conditions top to bottom and stops at the first true one. Look back at <code>p4</code>.</details>
<details><summary>total_price</summary>When does <code>return</code> happen? Look at the indentation.</details>

## Branch name

`ex-03-fix-the-bug`
