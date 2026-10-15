# coding-practice

Practice exercises for learning Python and Git. Each exercise is sent in as
its own **pull request (PR)**, and every PR gets reviewed before it is merged.

## Exercises

| Folder | What you practise | Checked by |
|---|---|---|
| [`01_first_pr/`](exercises/01_first_pr/) | The full PR loop: branch, commit, push, open a PR | Review only |
| [`02_predict/`](exercises/02_predict/) | Reading code: guess the output first, then run it | Review only |
| [`03_fix_the_bug/`](exercises/03_fix_the_bug/) | Debugging: six small programs, each with one bug | `check.py` + review |
| [`04_build/`](exercises/04_build/) | Writing functions from a description | `check.py` + review |

Do them in order. Each folder has its own `README.md` with the task.

## One-time setup (PowerShell)

```powershell
cd ~\Documents
git clone https://github.com/hariship/coding-practice.git
cd coding-practice
code .
```

If Git asks you to sign in, a browser window opens. Log in to GitHub there.

## The loop for every exercise

```powershell
# 1. Start from the latest main
git switch main
git pull

# 2. Make a branch just for this exercise
git switch -c ex-03-fix-the-bug

# 3. Do the work in VS Code, then check it
python exercises\03_fix_the_bug\check.py

# 4. Save it
git add .
git commit -m "Fix off-by-one bug in count_to"

# 5. Send the branch to GitHub
git push -u origin ex-03-fix-the-bug
```

Then:

1. Open the repo on GitHub. A yellow bar says **Compare & pull request**. Click it.
2. Fill in the template and click **Create pull request**.
3. Wait for review. A green tick or a red cross also appears at the bottom.
   That's GitHub running `check.py` for you.
4. If there are comments, fix them on the **same branch**, then run `git add`,
   `git commit` and `git push` again. The PR updates by itself.
5. Once it's merged, go back to step 1 for the next exercise.

## Rules

- One exercise per PR.
- Never commit straight to `main`. Always use a branch.
- Small commits with clear messages: say *what* changed, not "update" or "fix".
- Stuck for more than 20 minutes? Push what you have and open the PR anyway.
  Write your question in the PR description.
